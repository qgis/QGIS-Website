#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import shutil
from urllib.parse import urlparse
import json

class MapHarvester:
  def __init__(self, api_url, output_dir):
    self.api_url = api_url
    self.output_dir = output_dir
    os.makedirs(self.output_dir, exist_ok=True)
  
  def clean_output_dir(self):
    for filename in os.listdir(self.output_dir):
      if filename == "index.md":
        continue
      file_path = os.path.join(self.output_dir, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)
      except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

  def fetch_maps(self):
    next_page = self.api_url
    while next_page:
      response = requests.get(next_page)
      response.raise_for_status()
      data = response.json()

      for map_item in data.get("results", []):
        if map_item.get("is_publishable"):
          self.process_map(map_item)

      next_page = data.get("next")

  def process_map(self, map_item):
    name = map_item["name"]
    description = map_item["description"]
    creator = map_item["creator"]
    map_id = map_item["id"]
    upload_date = map_item["upload_date"]
    link = map_item["file"]
    thumbnail_url = map_item["thumbnail"]
    uuid = map_item["uuid"]

    # Parse the thumbnail URL to get the file name
    path = urlparse(thumbnail_url).path
    image_ext = os.path.splitext(path)[1]
    image_name = f"{uuid}{image_ext}"

    # Download the thumbnail
    image_path = os.path.join(self.output_dir, image_name)
    self.download_file(thumbnail_url, image_path)

    # Generate the markdown content
    content = f"""---
source: "hub"
title: "{name}"
description: {json.dumps(description.strip())}
creator: "{creator.strip()}"
image: "{image_name}"
date: "{upload_date}"
link: "{link}"
hub_link: "https://hub.qgis.org/map-gallery/{map_id}"
draft: "false"
showcase: "map"
---
"""
    # Write the markdown file
    md_filename = os.path.join(self.output_dir, f"{uuid}.md")
    with open(md_filename, "w", encoding="utf-8") as f:
      f.write(content)
      print(f"Markdown file created: {md_filename}")

  def download_file(self, url, dest_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(dest_path, "wb") as out_file:
      shutil.copyfileobj(response.raw, out_file)
    print(f"Downloaded: {dest_path}")

if __name__ == "__main__":
  API_URL = "http://hub.qgis.org/api/v1/resources/?resource_type=map"
  OUTPUT_DIR = "content/hub-maps"

  harvester = MapHarvester(api_url=API_URL, output_dir=OUTPUT_DIR)
  harvester.clean_output_dir()
  harvester.fetch_maps()