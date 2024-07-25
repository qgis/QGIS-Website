---
source: "blog"
title: "Sourcepole: Adding external WMS to the QGIS Cloud Web Map"
image: "qgiscloud-externe-services."
date: "2024-07-23"
link: "https://blog.sourcepole.ch/2024/07/23/qgiscloud-externe-services/"
draft: "true"
showcase: "planet"
---

The use of WMS/WMTS layers in a QGIS Cloud map project can significantly degrade the performance of the map display. I have already discussed how to counter this problem in an earlier post. One of the solutions is to load external WMS as background layers. The problem with this approach, however, is that only one WMS background layer can be loaded at a time. If further WMS layers are to be loaded into the map at the same time, this approach cannot be used.
