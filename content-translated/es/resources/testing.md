---
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Probando
type: page

---
{{<content-start >}}
# Pruebas
## Continuous Integration Tests
Both QGIS Desktop and QGIS server are tested rigorously. Each pull request (i.e. code contribution) to QGIS undergoes automated Continuous Integration build tests (github workflows). Our QGIS Server platform is tested using our OGC conformance testing suite.

<a href="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush" target="_blank">
<img src="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg">
</a>

<a href="https://hub.docker.com/r/qgis/qgis/tags" target="_blank">
<img src="https://img.shields.io/docker/automated/qgis/qgis.svg">
</a>

See [Unit testing](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) in our documentation for notes on the test suite.
## OGC Conformance
See the [OGC conformance testing documentation](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) for more information and notes on how to run these tests yourself.

{{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite" text="OGC Cite tests" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wms_130/latest/report.html" text="WMS 1.3.0 Tests" >}} {{< button class="is-primary1 is-small" link="http://test.qgis.org/ogc_cite/wfs_110/latest/report.html" text="WFS 1.1.0 Tests" >}}

{{<content-end >}}
