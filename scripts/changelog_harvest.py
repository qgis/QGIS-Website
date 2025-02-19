#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
this script should be run from the root repo directory (../)

$ python scripts/changelog_harvest.py

will create/update a visual-changelogs at content/project/visual-changelogs based
on the data at data/conf.json.

To fetch changelogs for a specific version:

$ python3 scripts/changelog_harvest.py --version 3.34 --release 21.06.2024

# To trigger the images resize/transform process only for existing changelog
$ ./scripts/changelog_harvest.py --version 3.34 --release 21.06.2024 --use_existing

'''

import os
import re
import requests
import json
import argparse
import sys
from zipfile import ZipFile
from datetime import datetime
from resize_image import resize_image, convert_to_webp, is_valid_image

class ChangelogHarvester:
    def __init__(self, version=None, release_date=None):
        """
        Initialize the ChangelogHarvester object.
        :param version: The QGIS version (e.g., '3.34')
        :param release_date: The release date in 'dd.mm.yyyy' format
        
        If version and release_date are provided, they will be used.
        Otherwise, the values from the config file will be used.
        
        """
        self.version = version
        self.release_date = release_date
        self.version_formatted = re.sub(r'\D', '', self.version)
        self.url = f'https://changelog.qgis.org/en/qgis/version/{self.version}/md/'
        self.zip_filename = f'qgis_changelog_{self.version_formatted}.zip'
        self.extract_path = f'content/project/visual-changelogs/visualchangelog{self.version_formatted}/'

    def download_and_extract_zip(self):

        print(f'Downloading {self.url}')
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Error: Could not download the file from {self.url}. HTTP status code: {response.status_code}")
            return

        with open(self.zip_filename, 'wb') as file:
            file.write(response.content)
        print(f'Downloaded {self.zip_filename}')

        print(f'Extracting {self.zip_filename} to {self.extract_path}')
        with ZipFile(self.zip_filename, 'r') as zip_ref:
            zip_ref.extractall(self.extract_path)
        print(f'Extracted to {self.extract_path}')

        os.remove(self.zip_filename)
        print(f'Removed {self.zip_filename}')

    def add_frontmatter_to_index(self):
        index_file_path = os.path.join(self.extract_path, 'index.md')
        print(f'Modifying {index_file_path}')
        with open(index_file_path, 'r') as file:
            content = file.read()

        front_matter = f"""---
title: "Changelog for QGIS {self.version}"
draft: false
HasBanner: false
sidebar: true
releaseDate: "{self.release_date}"
section: "project"
type: "visual-changelog"

---

{{{{< content-start >}}}}

"""
        content = front_matter + content
        content = re.sub(r'^(# .+)', r'\1 {#changelog' + self.version_formatted + '}', content, flags=re.M)
        content = re.sub(r'(!\[.*?\]\(.*?\))', r'\1\n\nRelease date: ' + self.release_date, content, 1)
        content += '\n\n{{< content-end >}}'

        with open(index_file_path, 'w') as file:
            file.write(content)
        print(f'Modified {index_file_path}')

    # Resize and Convert images in the index.md to webp format
    def resize_and_convert_images(self):
        index_file_path = os.path.join(self.extract_path, 'index.md')
        print(f'Converting images in {index_file_path} to webp format')

        with open(index_file_path, 'r') as file:
            content = file.read()

        image_paths = re.findall(r'!\[.*?\]\((images/.*?)\)', content)
        for image_path in image_paths:
            full_image_path = os.path.join(self.extract_path, image_path)
            
            if is_valid_image(full_image_path):
                resize_image(full_image_path, max_height=600)
                webp_image_path = convert_to_webp(full_image_path, replace=True)
                content = content.replace(
                    image_path, 
                    webp_image_path.replace(self.extract_path, '')
                )

        with open(index_file_path, 'w') as file:
            file.write(content)
        print(f'Converted images in {index_file_path} to webp format')
        

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
        return config

    @staticmethod
    def format_release_date(date_str):
        return datetime.strptime(date_str, "%d.%m.%Y").strftime("%Y-%m-%d")

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Download and extract QGIS changelog.")
        parser.add_argument('--version', type=str, help="QGIS version (e.g., '3.34')")
        parser.add_argument('--release', type=str, help="Release date in 'dd.mm.yyyy' format")
        parser.add_argument(
            '--use_existing',
            action='store_true',
            help="Use existing files instead of downloading from the changelog site"
        )
        return parser.parse_args()

if __name__ == '__main__':
    args = ChangelogHarvester.parse_arguments()

    if args.version and args.release:
        version = args.version
        release_date = ChangelogHarvester.format_release_date(args.release)
    elif not args.version and not args.release:
        config_path = 'data/conf.json'
        config = ChangelogHarvester.load_config(config_path)
        version = config['version']
        release_date = config['releasedate']
    else:
        print("Error: You must specify both --version and --release, or neither.")
        sys.exit(1)

    harvester = ChangelogHarvester(version, release_date)
    if not args.use_existing:
        harvester.download_and_extract_zip()
        harvester.add_frontmatter_to_index()
    harvester.resize_and_convert_images()
