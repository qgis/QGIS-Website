---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Test
type: page

---
{{<content-start >}}
# Tests
## Tests d'intégration continue
QGIS Desktop et QGIS Server font tous deux l'objet de tests rigoureux. Chaque pull request (c'est-à-dire chaque contribution au code) soumise à QGIS est soumise à des tests de compilation automatisés dans le cadre de l'intégration continue (workflows GitHub). Notre plateforme QGIS Server est testée à l'aide de notre suite de tests de conformité OGC.

[![Tests](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg)](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush) [![Docker Automated Build](https://img.shields.io/docker/automated/qgis/qgis.svg)](https://hub.docker.com/r/qgis/qgis/tags)

Consultez la section [Tests unitaires](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) de notre documentation pour obtenir des informations sur la suite de tests.
## Conformité aux normes OGC
Consultez la [documentation relative aux tests de conformité OGC](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) pour plus d'informations et des conseils sur la manière d'effectuer ces tests vous-même.

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 Tests" >}}

{{<button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 Tests" >}}

{{<content-end >}}
