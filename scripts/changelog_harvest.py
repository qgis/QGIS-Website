#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
this script should be run from the root repo directory (../)

$ python scripts/changelog_harvest.py

will create/update a visual-changelogs at content/project/visual-changelogs based
on the data at data/conf.json.

To fetch changelogs for a specific version:

$ python3 scripts/changelog_harvest.py --version 3.34 --release 21.06.2024
'''

import os
import re
import requests
import json
import argparse
import sys
from zipfile import ZipFile
from datetime import datetime

def download_and_extract_zip(version, release_date):
    # Format version without special characters
    version_formatted = re.sub(r'\D', '', version)

    # URL of the zip file
    url = f'https://changelog.qgis.org/en/qgis/version/{version}/md/'

    # Define file paths
    zip_filename = f'qgis_changelog_{version_formatted}.zip'
    extract_path = f'content/project/visual-changelogs/visualchangelog{version_formatted}'

    # Download the zip file
    print(f'Downloading {url}')
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not download the file from {url}. HTTP status code: {response.status_code}")
        return

    with open(zip_filename, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded {zip_filename}')

    # Extract the zip file
    print(f'Extracting {zip_filename} to {extract_path}')
    with ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f'Extracted to {extract_path}')

    # Remove the zip file after extraction
    os.remove(zip_filename)
    print(f'Removed {zip_filename}')

    # Modify the index.md file
    index_file_path = os.path.join(extract_path, 'index.md')
    modify_index_file(index_file_path, version, version_formatted, release_date)

def modify_index_file(index_file_path, version, version_formatted, release_date):
    print(f'Modifying {index_file_path}')
    with open(index_file_path, 'r') as file:
        content = file.read()

    # Add front matter
    front_matter = f"""---
title: "Changelog for QGIS {version}"
draft: false
HasBanner: false
sidebar: true
releaseDate: "{release_date}"
section: "project"
type: "visual-changelog"

---

{{{{< content-start >}}}}

"""
    content = front_matter + content

    # Add id to the first heading
    content = re.sub(r'^(# .+)', r'\1 {#changelog' + version_formatted + '}', content, flags=re.M)

    # Insert release date after the first image
    content = re.sub(r'(!\[.*?\]\(.*?\))', r'\1\n\nRelease date: ' + release_date, content, 1)

    # Append content-end
    content += '\n\n{{< content-end >}}'

    # Write the modified content back to the file
    with open(index_file_path, 'w') as file:
        file.write(content)
    print(f'Modified {index_file_path}')


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

def format_release_date(date_str):
    # Convert date from dd.mm.yyyy to yyyy-mm-dd
    return datetime.strptime(date_str, "%d.%m.%Y").strftime("%Y-%m-%d")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Download and extract QGIS changelog.")
    parser.add_argument('--version', type=str, help="QGIS version (e.g., '3.34')")
    parser.add_argument('--release', type=str, help="Release date in 'dd.mm.yyyy' format")
    return parser.parse_args()

if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_arguments()

    if args.version and args.release:
        version = args.version
        release_date = format_release_date(args.release)
    elif not args.version and not args.release:
        # Load configuration from JSON
        config_path = 'data/conf.json'
        config = load_config(config_path)
        version = config['version']
        release_date = format_release_date(config['releasedate'])
    else:
        print("Error: You must specify both --version and --release, or neither.")
        sys.exit(1)

    download_and_extract_zip(version, release_date)
