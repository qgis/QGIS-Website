---
type: "page"
title: "Releases"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start  >}}

# List of Releases

TODO

# Tests

Both QGIS and QGIS server are being tested via all kind of ways.

From build tests (github workflows) and code unit tests to OGC conformance testing.


<a href="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml?query=branch%3Amaster+event%3Apush" target="_blank">
<img src="https://github.com/qgis/QGIS/actions/workflows/run-tests.yml/badge.svg">
</a>

<a href="https://hub.docker.com/r/qgis/qgis/tags" target="_blank">
<img src="https://img.shields.io/docker/automated/qgis/qgis.svg">
</a>


See [Unit testing](https://docs.qgis.org/testing/en/docs/developers_guide/unittesting.html)


See [OGC conformance testing](https://docs.qgis.org/testing/en/docs/developers_guide/ogcconformancetesting.html) for more information and how to run these tests yourself.

Recent tests output can be found here: http://test.qgis.org/ogc_cite. For latest WMS 1.3.0 test see http://test.qgis.org/ogc_cite/wms_130/latest/report.html and for WFS 1.1.0 see http://test.qgis.org/ogc_cite/wfs_110/latest/report.html.

{{< content-end >}}
