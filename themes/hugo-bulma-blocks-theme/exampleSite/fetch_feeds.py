#!/usr/bin/env python3

# Simple script to get sustaining members and 
# other feeds and update our web site with them
# (c) Tim Sutton, 2023

import requests
import argparse
import json
import shutil
import os
from rss_parser import Parser
from requests import get
import atoma
from dateutil.parser import parse as date_parse
try:
    import urlparse
except ImportError:
    from urllib.parse import urlparse

### Funders
def fetch_funders():
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

        start_date = date_parse(start_date, fuzzy_with_tokens=True)[0]
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = date_parse(end_date, fuzzy_with_tokens=True)[0]
        end_date = end_date.strftime("%Y-%m-%d")

        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(link))
        image_name = "%s.%s" % (name, image_ext)
        image_name = image_name.replace("..",".")

        content = f"""---
level: "{level}"
title: "{title}"
logo: "{image_name}"
startDate: "{start_date}"
endDate: "{end_date}"
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

### Flickr screenshots
def fetch_flickr_screenshots(showcase_type, rss_url):

    response = requests.get(rss_url)
    feed = atoma.parse_atom_bytes(response.content)
    #print(feed.description)
    print(feed.title.value)
    for entry in feed.entries:
        print('----')
        #print(dir(entry))
        print(entry.title.value)
        for author in entry.authors:
            print(author.name)
            print(author.uri)
        image_url = entry.links[len(entry.links)-1].href
        print(image_url)

        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(image_url))
        image_name = "%s.%s" % (name, image_ext)
        image_name = image_name.replace("..",".")

        entry_date = entry.published.strftime("%Y-%m-%d")
        print(entry_date)

        content = f"""---
source: "flickr"
title: "{entry.title.value}"
image: "{image_name}"
date: "{entry_date}"
link: "{image_url}"
draft: "true"
showcase: "{showcase_type}"
---
"""
        markdown_filename = f"content/flickr-images/{name}.md"
        with open(markdown_filename , "w", encoding="utf=8") as f:
            f.write(content)
            print(f"Writing: {markdown_filename}")

        response = requests.get(image_url, stream=True)
        image_filename = f"content/flickr-images/{image_name}"
        with open(image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"Writing: {image_filename}")
        del response    

# Blogs with atom feeds
def fetch_blog_feed(showcase_type, rss_url):
    response = requests.get(rss_url)
    feed = atoma.parse_atom_bytes(response.content)
    #print(feed.description)
    print(feed.title.value)
    for entry in feed.entries:
        print('----')
        #print(dir(entry))
        print(entry.title.value)
        for author in entry.authors:
            print(author.name)
            print(author.uri)
        image_url = entry.links[len(entry.links)-1].href
        print(image_url)

        path = urlparse(image_url).path
        image_ext = os.path.splitext(path)[1]
        name = os.path.basename(os.path.normpath(image_url))
        image_name = "%s.%s" % (name, image_ext)
        image_name = image_name.replace("..",".")

        try:
            entry_date = entry.published.strftime("%Y-%m-%d")
        except:
            entry_date = ""

        try:
            summary = entry.summary.value
        except:
            summary = ""

        content = f"""---
source: "blog"
title: "{entry.title.value}"
image: "{image_name}"
date: "{entry_date}"
link: "{image_url}"
draft: "true"
showcase: "{showcase_type}"
---

{summary}
"""
        markdown_filename = f"content/community-blogs/{name}.md"
        with open(markdown_filename , "w", encoding="utf=8") as f:
            f.write(content)
            print(f"Writing: {markdown_filename}")

        response = requests.get(image_url, stream=True)
        image_filename = f"content/community-blogs/{image_name}"
        with open(image_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"Writing: {image_filename}")
        del response   


parser = argparse.ArgumentParser(description='Import items from various feeds.')
parser.add_argument(
    "--flickr", 
    help="Import flickr items (defaults to no)",
    default="no",
    type=bool, 
    required=False)
parser.parse_args()
args = parser.parse_args()

fetch_funders()

if args.flickr:
    fetch_flickr_screenshots(
        showcase_type="map",
        rss_url = "https://api.flickr.com/services/feeds/groups_pool.gne?id=2244553@N22&lang=en-us&format=atom"
    )
    fetch_flickr_screenshots(
        showcase_type="screenshot",
        rss_url = "https://api.flickr.com/services/feeds/groups_pool.gne?id=2327386@N22&lang=en-us&format=atom"
    )

# Planet blog aggregator
fetch_blog_feed(
    showcase_type="planet",
    rss_url="https://plugins.qgis.org/planet/feed/atom/"
)
# QGIS User group feed
fetch_blog_feed(
    showcase_type="qug",
    rss_url="https://raw.githubusercontent.com/qgis/QGIS-Website/master/source/feeds/qugsnews.atom"
)
