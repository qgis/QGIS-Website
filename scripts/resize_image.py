from PIL import Image
import io
import ipaddress
import os
import socket
import warnings
import xml.etree.ElementTree as ET
import requests
from urllib.parse import urljoin, urlsplit
from PIL import UnidentifiedImageError


SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'tiff']

def resize_image(image_filename, max_height=120):
    """
    Resize an image to a maximum height, keeping the aspect ratio.
    The image is resized in place.
    param image_filename: The image file to resize
    param max_height: The maximum height in pixels
    """
    if os.path.exists(image_filename):
        with Image.open(image_filename) as img:

            # Determine the file format
            file_format = img.format
            if not file_format or file_format.lower() not in SUPPORTED_FORMATS:
                return
            if file_format == 'JPG':
                file_format = 'JPEG'
            width, height = img.size
            if height > max_height:
                new_height = max_height
                new_width = int((new_height / height) * width)

                img_resized = img.resize(
                    (new_width, new_height), Image.LANCZOS
                )

                # Save the resized image with optimization
                img_resized.save(
                    image_filename,
                    format=file_format,
                    optimize=True,
                    quality=85
                )
    else:
        print(f'File not found: {image_filename}')

# Transform an image into webp format
def convert_to_webp(image_filename, replace=False):
    """
    Convert an image to webp format.
    The image is converted in place.
    param image_filename: The image file to convert
    """
    with Image.open(image_filename) as img:
        # Determine the file format
        file_format = img.format
        if file_format.lower() not in SUPPORTED_FORMATS:
            return image_filename
        if os.path.exists(image_filename):
            # Save the image in webp format with optimization
            webp_filename = image_filename + '.webp'
            img.save(
                webp_filename,
                format='WEBP',
                optimize=True,
                quality=85
            )
            if replace:
                os.remove(image_filename)
            return webp_filename
        else:
            print(f'File not found: {image_filename}')
            raise FileNotFoundError
    
# Check if the image is valid
def is_valid_image(image_filename):
    """
    Check if the image file is valid.
    param image_filename: The image file to check
    return: True if the image is valid, False otherwise
    """
    try:
        img = Image.open(image_filename)
        img.verify()
        return True
    except Exception as e:
        print(f'Invalid image: {image_filename}')

def is_valid_svg(svg_filename):
    """
    Check if the svg file is valid.
    param svg_filename: The svg file to check
    return: True if the svg is valid, False otherwise
    """
    try:
        ET.parse(svg_filename)  # Try to parse the XML
        return True  # No error means it's valid
    except ET.ParseError:
        return False  # If parsing fails, it's invalid

# ---------------------------------------------------------------------------
# Untrusted logos (user groups)
#
# Logos come from links and uploads that anyone can propose in a pull request,
# so they are handled as hostile input: the download refuses internal network
# addresses, is size and time capped, and the image is decoded and re-encoded
# from scratch by Pillow. Only raster formats are accepted. SVG is refused
# because an SVG served from our domain can carry scripts.
# ---------------------------------------------------------------------------
LOGO_FORMATS = {'PNG', 'JPEG', 'GIF', 'WEBP'}
LOGO_MAX_BYTES = 5 * 1024 * 1024
LOGO_MAX_PIXELS = 25_000_000
LOGO_TIMEOUT = 15
LOGO_MAX_REDIRECTS = 3


class LogoError(Exception):
    """A logo that cannot be used. The message is written for the editor."""


def _check_public_url(url):
    """Refuse anything but a plain http(s) URL to a public internet address."""
    parts = urlsplit(url)
    if parts.scheme not in ('http', 'https'):
        raise LogoError('The logo link must start with https:// or http://.')
    if parts.username or parts.password:
        raise LogoError('The logo link must not contain a user name or password.')
    if not parts.hostname:
        raise LogoError('The logo link has no web address.')
    port = parts.port or (443 if parts.scheme == 'https' else 80)
    try:
        addresses = socket.getaddrinfo(parts.hostname, port, type=socket.SOCK_STREAM)
    except socket.gaierror:
        raise LogoError(f'We could not find the website {parts.hostname}.')
    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])
        if not ip.is_global or ip.is_multicast:
            raise LogoError('The logo link points to a private network address.')


def fetch_image_bytes(url, session=None):
    """Download an image from an untrusted URL and return its bytes.

    Redirects are followed by hand so every hop is checked. The remaining
    risk is DNS rebinding between the check and the connection, which only
    matters on networks with internal services; CI runners are disposable.
    """
    session = session or requests.Session()
    for _ in range(LOGO_MAX_REDIRECTS + 1):
        _check_public_url(url)
        try:
            response = session.get(
                url, stream=True, timeout=LOGO_TIMEOUT, allow_redirects=False,
                headers={'User-Agent': 'QGIS-Website user groups logo check'},
            )
        except requests.RequestException:
            raise LogoError('We could not download the logo. Check that the link opens in a browser.')
        with response:
            if response.is_redirect or response.status_code in (301, 302, 303, 307, 308):
                location = response.headers.get('Location')
                if not location:
                    raise LogoError('The logo link redirects nowhere.')
                url = urljoin(url, location)
                continue
            if response.status_code != 200:
                raise LogoError(f'The logo link answered with error {response.status_code}.')
            data = bytearray()
            for chunk in response.iter_content(64 * 1024):
                data.extend(chunk)
                if len(data) > LOGO_MAX_BYTES:
                    raise LogoError('The logo is larger than 5 MB. Use a smaller image.')
            return bytes(data)
    raise LogoError('The logo link redirects too many times.')


def _describe_non_image(data):
    head = data[:512].lstrip().lower()
    if head.startswith(b'<svg') or b'<svg' in head:
        return 'SVG logos are not accepted. Use a PNG, JPEG, GIF or WebP image.'
    if head.startswith((b'<!doctype html', b'<html')) or b'<html' in head:
        return 'The logo link returns a web page, not an image. Link to the image file itself.'
    return 'The logo is not a PNG, JPEG, GIF or WebP image.'


def normalize_logo(data, dest, max_px=256, min_px=16):
    """Validate untrusted image bytes and write a clean WebP to dest.

    The image is decoded and re-encoded, which drops metadata and anything
    hidden after the image data. Animated images keep their first frame.
    """

    previous_limit = Image.MAX_IMAGE_PIXELS
    Image.MAX_IMAGE_PIXELS = LOGO_MAX_PIXELS
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('error', Image.DecompressionBombWarning)
            try:
                with Image.open(io.BytesIO(data)) as probe:
                    if probe.format not in LOGO_FORMATS:
                        raise LogoError('The logo is not a PNG, JPEG, GIF or WebP image.')
                    probe.verify()
                with Image.open(io.BytesIO(data)) as img:
                    img.seek(0)
                    img.load()
                    img = img.convert('RGBA')
            except LogoError:
                raise
            except (Image.DecompressionBombError, Image.DecompressionBombWarning):
                raise LogoError('The logo has too many pixels. Use an image under 5000 by 5000 pixels.')
            except UnidentifiedImageError:
                raise LogoError(_describe_non_image(data))
            except Exception:
                raise LogoError('The logo file is damaged and cannot be read.')
    finally:
        Image.MAX_IMAGE_PIXELS = previous_limit

    if min(img.size) < min_px:
        raise LogoError(f'The logo is too small. Use an image at least {min_px} pixels wide and high.')
    img.thumbnail((max_px, max_px), Image.LANCZOS)

    out = io.BytesIO()
    img.save(out, format='WEBP', quality=85, method=6)
    dest = os.fspath(dest)
    os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
    tmp = dest + '.tmp'
    with open(tmp, 'wb') as fh:
        fh.write(out.getvalue())
    os.replace(tmp, dest)
    return dest
