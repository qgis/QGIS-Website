---
type: "page"
title: "Testing"
subtitle: ""
draft: false
sidebar: true
Reviewed: 1 June 2024
Reviewer: Tim Sutton
---

{{< content-start  >}}



# Tests

## Continuous Integration Tests

Both QGIS Desktop and QGIS server are tested rigorously. Each pull request (i.e. code contribution) to QGIS undergoes automated Continuous Integration build tests (github workflows). Our QGIS Server platform is tested using our OGC conformance testing suite.


[![Tests](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg)](https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush) [![Docker Automated Build](https://img.shields.io/docker/automated/qgis/qgis.svg)](https://hub.docker.com/r/qgis/qgis/tags)


See [Unit testing](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html) in our documentation for notes on the test suite.

## OGC Conformance

See the [OGC conformance testing documentation](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) for more information and notes on how to run these tests yourself.

{{< button
class = "is-primary1 is-small"
link = "https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html"
text = "OGC Conformance tests" >}}

{{< button
class = "is-primary1 is-small"
link = "https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html#wms-1-3-0-test-suite"
text = "WMS 1.3.0 tests" >}}

{{< button
class = "is-primary1 is-small"
link = "https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html#ogc-api-features-test-suite"
text = "OGC API Features tests" >}}

{{< content-end >}}
