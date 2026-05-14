---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Тестване
type: page

---
{{<content-start >}}
# Тест
## Тестове за непрекъсната интеграция
Както QGIS Настолни, както и QGIS Сървърът са стриктно тествани. Всеки pull request (т.е. принос на код) към QGIS преминава през автоматизирани тестове за непрекъсната интеграция (работни процеси в GitHub). Нашата платформа QGIS Server е тествана с помощта на нашия пакет за тестване за съответствие с OGC.

[![Tests](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg)](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush) [![Docker Automated Build](https://img.shields.io/docker/automated/qgis/qgis.svg)](https://hub.docker.com/r/qgis/qgis/tags)

Вижте [Тестване на модули](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) в нашата документация за бележки относно тестовия пакет.
## Съответствие с OGC
Вижте [документацията за тестване за съответствие с OGC] (https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) за повече информация и бележки как да изпълните тези тестове сами.

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 Tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 Tests" >}}

{{<content-end >}}
