import requests
import json


response = requests.get("https://changelog.qgis.org/en/qgis/members/json/")

data = json.loads(response.text)


with open(f"../data/data.json", "w", encoding="utf=8") as f:
    f.write(json.dumps(data, ensure_ascii=False))

# This script downloads the RSS FEED Json file of QGIS Sustaining Members and it as a json file in the data folder
# The json file will be loop through to get each sustaining member
# A github action workflow will created that will be schedule to scrape the feed for incase of update 