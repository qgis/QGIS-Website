---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Tesztelés
type: page

---
{{<content-start >}}
# Tesztek
## Continuous Integration Tests
Mind a QGIS asztali, mind a szerver kiadása szigorúan tesztelt. Minden egyes pull request (azaz kód-hozzájárulás) a QGIS-hez automatizált folyamatos integrációs teszteken megy keresztül (github munkafolyamatok). A QGIS Szerver platformunkat az OGC megfelelőségi tesztcsomagunkkal teszteljük.

<a href="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush" target="_blank">
<img src="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg">
</a>

<a href="https://hub.docker.com/r/qgis/qgis/tags" target="_blank">
<img src="https://img.shields.io/docker/automated/qgis/qgis.svg">
</a>

A tesztkészletekkel kapcsolatos megjegyzéseket lásd a dokumentációnk [Unit tesztelés](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) fejezetében.
## OGC-megfelelőség
További információkért és a tesztek saját futtatására vonatkozó megjegyzésekért lásd az [OGC megfelelőségi tesztelési dokumentációt](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html).

{{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC idézett tesztek" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 tesztek" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 tesztek" >}}

{{<content-end >}}
