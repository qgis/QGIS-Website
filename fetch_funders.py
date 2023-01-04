#!/bin/python

# Simple script to get sustaining members and update our web site with them
# (c) Tim Sutton, 2023

import requests
import json
import shutil
import os
try:
    import urlparse
except ImportError:
    from urllib.parse import urlparse

response = requests.get("https://changelog.qgis.org/en/qgis/members/json/")
data = json.loads(response.text)
items = data["rss"]["channel"]["item"]
for item in items:
    link = item["member_url"]
    image_url = item["image_url"]
    title = item["title"]
    level = item["member_level"]
    country = item["member_country"]
    start_date = item["start_date"]
    end_date = item["end_date"]

    path = urlparse(image_url).path
    image_ext = os.path.splitext(path)[1]
    name = os.path.basename(os.path.normpath(link))
    image_name = "%s.%s" % (name, image_ext)
    image_name = image_name.replace("..",".")

    content = f"""
---
level: "{level}"
title: "{title}"
logo: "{image_name}"
start_date: "{start_date}"
end_date: "{end_date}"
link: "{link}"
country: "{country}"
---
"""
    markdown_filename = f"content/funders/{name}.md"
    with open(markdown_filename , "w", encoding="utf=8") as f:
        f.write(content)
        print(f"Writing: {markdown_filename}")

    response = requests.get(image_url, stream=True)
    image_filename = f"content/funders/{image_name}"
    with open(image_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        print(f"Writing: {image_filename}")
    del response
