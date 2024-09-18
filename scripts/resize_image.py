from PIL import Image
import os


def resize_image(image_filename, max_height=120):
    """
    Resize an image to a maximum height, keeping the aspect ratio.
    The image is resized in place.
    param image_filename: The image file to resize
    param max_height: The maximum height in pixels
    """
    if (
        image_filename.lower().endswith('.png') or
        image_filename.lower().endswith('.jpg')
    ):
        if os.path.exists(image_filename):
            print(f'Processing: {image_filename}')
            with Image.open(image_filename) as img:
                width, height = img.size
                if height > max_height:
                    new_height = max_height
                    new_width = int((new_height / height) * width)

                    img_resized = img.resize(
                        (new_width, new_height), Image.LANCZOS
                    )

                    # Determine the file format
                    file_format = (
                        'PNG' if image_filename.lower().endswith('.png')
                        else 'JPEG'
                    )

                    # Save the resized image with optimization
                    img_resized.save(
                        image_filename,
                        format=file_format,
                        optimize=True,
                        quality=85
                    )
                    print(f'Resized and optimized: {image_filename}')
                else:
                    print(f'No resizing needed for: {image_filename}')
        else:
            print(f'File not found: {image_filename}')
