---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Testen
type: page

---
{{<content-start >}}
# Testen
## Doorlopende integratie testen (CI-tests)
Zowel QGIS Desktop als QGIS server worden rigoureus getest. Elk pull request (d.i. bijdrage aan de code) voor QGIS ondergaat geautomatiseerde Continuous Integration bouwtesten (GitHub werkstromen). Ons platform voor QGIS Server is getest met ons OGC conforme testpakket.

<a href="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush" target="_blank">
<img src="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg">
</a>

<a href="https://hub.docker.com/r/qgis/qgis/tags" target="_blank">
<img src="https://img.shields.io/docker/automated/qgis/qgis.svg">
</a>

Bekijk [Eenheidstesten](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) in onze documentatie voor opmerkingen over het testpakket.
## OGC conformiteit
Bekijk [OGC conformiteit testen documentatie](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) voor meer informatie en opmerkingen over hoe u deze testen zelf kunt uitvoeren.

{{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite testen" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 testen" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 testen" >}}

{{<content-end >}}
