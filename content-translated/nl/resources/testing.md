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

[![Tests](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg)](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush) [![Docker Automated Build](https://img.shields.io/docker/automated/qgis/qgis.svg)](https://hub.docker.com/r/qgis/qgis/tags)

Bekijk [Eenheidstesten](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) in onze documentatie voor opmerkingen over het testpakket.
## OGC conformiteit
Bekijk [OGC conformiteit testen documentatie](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) voor meer informatie en opmerkingen over hoe u deze testen zelf kunt uitvoeren.

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 Tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 Tests" >}}

{{<content-end >}}
