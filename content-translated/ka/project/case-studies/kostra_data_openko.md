---
HasBanner: false
archived: false
date: 2026-03-23
draft: false
featured: true
section: პროექტი
sidebar: true
thumbnail: images/thumbnail_openko.webp
title: Free KOSTRA Data on openko.de
type: case-study

---
{{<content-start >}}
# Free KOSTRA Data on openko.de
This article presents the project [openko.de](https://www.openko.de/), which provides **KOSTRA data in a structured and user-friendly way, free of charge**. The platform content was largely implemented using QGIS.
## About KOSTRA
KOSTRA (also known as KOSTRA-DWD) is a heavy rainfall catalogue published by the German Meteorological Service ("Deutscher Wetterdienst" in German, DWD). The acronym stands for *Coordinated Heavy Precipitation Regionalization and Evaluation* ("Koordinierte Starkniederschlagsregionalisierung und -auswertung" in German).

The catalogue contains raster data on precipitation heights and intensities depending on rainfall duration and return period. The dataset covers the entire territory of Germany.

For decades, KOSTRA data was only available from the DWD for a fee. Following an amendment to the DWD Act in 2017, these datasets were made freely accessible.

Although the data is available both with and without spatial reference, its structure is not particularly user-friendly and requires experienced users. Well-structured PDF tables summarizing precipitation values are still only available for a fee, currently €70 (net) per grid cell.
## What is openko.de?
Since 2022, the website openko.de has offered over **21,000 alternative PDF tables and maps** for free download. In addition to the tabular data, each PDF includes a map showing the location of the corresponding grid cell.

![Example excerpt of a KOSTRA PDF table including a map](../images/screenshot_pdf_example_table_and_map.webp)

Navigation to the appropriate KOSTRA grid cell is provided via a web map ([Interactive Map KOSTRA-DWD-2020](https://www.openko.de/kostra-dwd-2020-tabellen-kostenlos-herunterladen/)) with integrated address search (Click on "Interaktive Karte KOSTRA-DWD-2020" to reach the map).

![Selection of grid cells via web map](../images/screenshot_qgis2web_raster_selection.webp)

The project has been very well received. Its users mainly include engineering consultancies, construction companies, and public authorities that require KOSTRA data for the design and verification of hydraulic infrastructure. Universities also use openko.de to provide students with easy access to KOSTRA data.

The success of the project can also be expressed quantitatively: since its launch in July 2022 to March 2026, more than **200,000 tables have been downloaded**. At €70 per table (the DWD price), this corresponds to a **total value of over 14,000,000 euros**!
## How openko.de was created and the role of QGIS
The tables were created using **QGIS Print Layout** and demonstrate how standard QGIS functionality can transform raw data into well-structured and visually appealing outputs.

For easier processing in QGIS, precipitation tables were first merged into a single CSV file using a Python script. The result is a dataset of more than 45 MB, **containing 351,759 rows and over 10.2 million data entries**.

Each row contains a grid cell ID, allowing the data to be assigned accordingly. In the layout, precipitation values and uncertainty information are combined into tables.

While this approach worked well for the smaller KOSTRA-DWD-2010 dataset, performance issues arose with KOSTRA-DWD-2020. Generating the **atlas** required excessive processing time, as data had to be reloaded for each grid cell. A rough estimate indicated that creating approximately 16,000 tables would take around 11 days.

The solution was simple: the dataset was split into four parts, and tables were generated simultaneously using four parallel QGIS instances. This reduced the total processing time to about one day.

Additional Python scripts were developed for:
- Generating HTML-formatted download pages including metadata such as municipalities, federal states, and postal codes
- Uploading preview images and PDF files via the WordPress API

The web map was created using the [qgis2web plugin](https://plugins.qgis.org/plugins/qgis2web/). It contains only two layers: a topographic base map and the raster grid.

Download links are generated systematically based on grid cell IDs, allowing each feature to include a direct link to its corresponding download page. Clicking on a grid cell opens a popup with the correct link leading to the download page.
## Data sources
The following open data sources were used:
- KOSTRA data from the DWD:<br />https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/
- Topographic base map TopPlusOpen from the Federal Agency for Cartography and Geodesy ("Bundesamt für Kartographie und Geodäsie" in German):<br />https://sgx.geodatenzentrum.de/web_public/gdz/datenquellen/Datenquellen_TopPlusOpen.html

## Outlook
A REST API ([REST API](https://www.openko.de/rest-api-kostra-dwd-2020/)) has recently been developed to provide access to KOSTRA data. It is currently available as a beta version and operates reliably.

The official release is planned for July 2026, coinciding with the fourth anniversary of openko.de. This release will be part of a complete website redesign, which will also **introduce additional data formats** alongside the existing PDF outputs.
## ავტორი
![Alexander Altnöder](../images/alexander_altnoeder.webp)

Alexander Altnöder is an engineering geologist based in the Ruhr Area, Germany. He works extensively with GIS and programming, both professionally and privately.

{{<content-end >}}
