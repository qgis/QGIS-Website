---
Reviewed: 5 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
subtitle: ''
title: Rapporten
type: page

---
{{<content-start >}}
# Dagelijkse rapporten
We maken rapporten op een dagelijkse basis om de status van QGIS Server te monitoren.
## OGC Certificatie
QGIS Server 3.28 is momenteel gecertificeerd voor WMS 1.3.0 (zie [OGC Reference Implementation](http://www.opengeospatial.org/resource/products)).

![](qgis_server_wms_ogc_badge.png)

Om regressies te detecteren, worden op dagelijkse basis testen van OGC uitgevoerd op de branch **master**. Rapporten worden gegenereerd voor verscheidene testpakketten van OGC:
- WMS 1.3.0 : http://test.qgis.org/ogc_cite/wms_130/
- OGC API Features (alias WFS 3) : http://test.qgis.org/ogc_cite/ogcapif/
- WFS 1.1.0 : http://test.qgis.org/ogc_cite/wfs_110/

De laatste rapporten zijn [WMS 1.3.0](http://test.qgis.org/ogc_cite/wms_130/latest/report.html) en [WFS 1.1.0](http://test.qgis.org/ogc_cite/wfs_110/latest/report.html).
## Uitvoering
Op dit moment zijn twee programma's beschikbaar voor testen en het maken van rapporten over prestaties.

Het eerste is [MS-Perfs](https://github.com/camptocamp/ms_perfs) wat het mogelijk maakt QGIS Server te vergelijken met andere kaartservers (zoals GeoServer of MapServer). Rapporten worden wekelijks gegenereerd en zijn [hier](http://test.qgis.org/perf_test/ms_perf/) beschikbaar.

Het tweede is [Graffiti](https://github.com/pblottiere/graffiti), dat het vergelijken ondersteunt van verschillende versies van QGIS Server en/of specifieke projectopties (parallell renderen, optie vertrouwen, enzovoort). Rapporten worden ook dagelijks gegenereerd en zijn beschikbaar [op](http://test.qgis.org/perf_test/graffiti/). Onthoud dat het project [QGIS-Server-PerfSuite](https://github.com/Oslandia/QGIS-Server-PerfSuite) de uitvoeringsinfrastructuur is om Graffiti uit te voeren in doorlopende integratie.
## Beveiliging
Een globaal overzicht van onze beveiliging is te vinden met het [gereedschap OpenSSF Scorecard report](https://securityscorecards.dev/viewer/?uri=github.com/qgis/QGIS).

Dat geeft een snel overzicht van de beste werkwijzen die in het project QGIS worden gebruikt. Sommige werkwijzen zijn echter niet toe te passen op een gebruikersinterface voor een desktop, zoals Fuzz testing, of Pinned Dependencies.

Beveiliging is een permanent proces; meer details over onze benadering van beveiliging zijn beschikbaar op [onze aangewezen pagina](/resources/support/security/).

{{<content-end >}}
