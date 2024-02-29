---
type: "page"
title: "Reports"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start  >}}

# Daily Reports

Some reports are generated on a daily basis to monitor the status of QGIS Server.

## OGC Certification

QGIS Server 3.28 is currently certified for WMS 1.3.0 (see [OGC Reference Implementation](http://www.opengeospatial.org/resource/products)).

![](qgis_server_wms_ogc_badge.png)

In order to keep an eye on regressions, OGC tests are run on a daily basis on the **master** branch. Corresponding reports are generated for several OGC testsuites:

- WMS 1.3.0 : http://test.qgis.org/ogc_cite/wms_130/

- OGC API Features (aka WFS 3) : http://test.qgis.org/ogc_cite/ogcapif/

- WFS 1.1.0 : http://test.qgis.org/ogc_cite/wfs_110/


Latest reports are [WMS 1.3.0](http://test.qgis.org/ogc_cite/wms_130/latest/report.html) and [WFS 1.1.0](http://test.qgis.org/ogc_cite/wfs_110/latest/report.html).

## Performance

At the moment, two tools are living together to test and generate performance reports.

The first one is [MS-Perfs](https://github.com/camptocamp/ms_perfs) which allows to compare QGIS Server with other map servers (like GeoServer or MapServer). Reports are generated weekly and available [here](http://test.qgis.org/perf_test/ms_perf/).

The second one is [Graffiti](https://github.com/pblottiere/graffiti), allowing to generate a performance report between several versions of QGIS Server and/or specific project options (parallel rendering effect, trust option, and so on). Reports are also generated daily and available [in](http://test.qgis.org/perf_test/graffiti/). Note that [QGIS-Server-PerfSuite](https://github.com/Oslandia/QGIS-Server-PerfSuite) project is the deployment infrastructure to run Graffiti in continuous integration.

## Security

// text will appear soon

{{< content-end >}}
