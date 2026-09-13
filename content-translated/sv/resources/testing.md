---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Testar
type: page

---
{{<content-start >}}
# Tester
## Tester för kontinuerlig integration
Både QGIS Desktop och QGIS server testas noggrant. Varje pull request (dvs. kodbidrag) till QGIS genomgår automatiserade Continuous Integration-byggtester (github-arbetsflöden). Vår QGIS Server-plattform testas med hjälp av vår OGC-överensstämmelse testsvit.

[![Tests](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg)](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush) [![Docker Automated Build](https://img.shields.io/docker/automated/qgis/qgis.svg)](https://hub.docker.com/r/qgis/qgis/tags)

Se [Unit testing](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) i vår dokumentation för information om testsviten.
## OGC-överensstämmelse
Se [OGC conformance testing documentation] (https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) för mer information och anvisningar om hur du själv kan köra dessa tester.

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 Tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 Tests" >}}

{{<content-end >}}
