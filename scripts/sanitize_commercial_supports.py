#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlparse
from requests.exceptions import RequestException
import os

def load_yaml(file_path):
    """Load YAML file while preserving formatting"""
    with open(file_path, 'r') as file:
        return file.read()

def save_yaml(content, file_path):
    """Save YAML back to file"""
    with open(file_path, 'w') as file:
        file.write(content)

def is_same_domain(original_url, redirect_url):
    """Check if redirect stays on same domain (including http→https)"""
    original = urlparse(original_url)
    redirect = urlparse(redirect_url)
    
    # Compare netloc (domain) ignoring www prefix and scheme
    original_domain = original.netloc.lower().replace('www.', '')
    redirect_domain = redirect.netloc.lower().replace('www.', '')
    
    return original_domain == redirect_domain

def check_url_redirects(url):
    """Check if URL redirects to different domain"""
    if not url or url.strip() == "":
        return False
        
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        }
        session = requests.Session()
        session.max_redirects = 5
        response = session.head(
            url,
            headers=headers,
            timeout=10,
            allow_redirects=True,
            verify=True
        )
        
        if response.status_code != 200:
            return True
        redirect_url = response.url
        
        # Handle relative redirects
        if redirect_url.startswith('/'):
            redirect_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}{redirect_url}"

        return not is_same_domain(url, redirect_url)

    except requests.exceptions.SSLError:
        print(f"SSL error encountered for URL: {url}")
        return False
    except RequestException:
        return False
    except Exception as e:
        print(f"Unexpected error for URL {url}: {str(e)}")
        return False

def process_file(file_path):
    """Process a single YAML file"""
    try:
        original_content = load_yaml(file_path)
        lines = original_content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            if 'url:' in line.lower():  # Case-insensitive check
                # Extract the URL value
                parts = line.split(':', 1)
                if len(parts) > 1:
                    url = parts[1].strip().strip('"\'')
                    if check_url_redirects(url):
                        # Preserve indentation and formatting
                        indent = line[:line.find('url:')]
                        lines[i] = f"{indent}url: \"\""
                        print(f"Emptying URL in {file_path} (line {i+1}): {url}")
                        modified = True
        
        if modified:
            save_yaml('\n'.join(lines), file_path)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    directory = 'data/commercial_support'
    processed_files = 0
    modified_files = 0
    
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return
    
    for filename in sorted(os.listdir(directory)):
        if filename.lower().endswith('.yml'):
            file_path = os.path.join(directory, filename)
            processed_files += 1
            if process_file(file_path):
                modified_files += 1
    
    print(f"\nProcessing complete:")
    print(f"- Total files processed: {processed_files}")
    print(f"- Files with URLs emptied: {modified_files}")

if __name__ == '__main__':
    main()