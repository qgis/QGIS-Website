---
type: "page"
title: "Reports"
subtitle: ""
draft: false
sidebar: true
Reviewed: 5 June 2024
Reviewer: Tim Sutton
---

{{< content-start  >}}

# Daily Reports

We generate reports on a daily basis to monitor the status of QGIS Server.

## OGC Certification

QGIS Server 3.28 is currently certified for WMS 1.3.0 (see [OGC Reference Implementation](http://www.opengeospatial.org/resource/products)).

![](qgis_server_wms_ogc_badge.png)

In order to detect regressions, OGC tests are run daily basis **master** branch. Reports are generated for several OGC testsuites:

- WMS 1.3.0 : http://test.qgis.org/ogc_cite/wms_130/

- OGC API Features (aka WFS 3) : http://test.qgis.org/ogc_cite/ogcapif/

- WFS 1.1.0 : http://test.qgis.org/ogc_cite/wfs_110/


Latest reports are [WMS 1.3.0](http://test.qgis.org/ogc_cite/wms_130/latest/report.html) and [WFS 1.1.0](http://test.qgis.org/ogc_cite/wfs_110/latest/report.html).

## Performance

At the moment, two tools are available to test and generate performance reports.

The first one is [MS-Perfs](https://github.com/camptocamp/ms_perfs) which supports comparison of QGIS Server with other map servers (like GeoServer or MapServer). Reports are generated weekly and available [here](http://test.qgis.org/perf_test/ms_perf/).

The second one is [Graffiti](https://github.com/pblottiere/graffiti), which supports comparing versions of QGIS Server and/or specific project options (parallel rendering, trust option, and so on). Reports are also generated daily, and are available [at](http://test.qgis.org/perf_test/graffiti/). Note that [QGIS-Server-PerfSuite](https://github.com/Oslandia/QGIS-Server-PerfSuite) provides the deployment infrastructure to run Graffiti in continuous integration.

## Security

A global overview of our security can be found using the [OpenSSF Scorecard report tool](https://securityscorecards.dev/viewer/?uri=github.com/qgis/QGIS).  

This gives a quick overview of the best practices used in QGIS project. Some practices are however not applicable to a desktop GUI, like Fuzz testing, or Pinned Dependencies.

Security is a permanent process, more details about our security approach are available on [our dedicated page](/resources/support/security/).


{{< content-end >}}
