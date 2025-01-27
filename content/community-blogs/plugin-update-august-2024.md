---
source: "blog"
title: "QGIS Project blog: Plugin Update – August, 2024"
image: "plugin-update-august-2024."
date: "2024-09-08"
link: "https://blog.qgis.org/2024/09/09/plugin-update-august-2024/"
draft: "true"
showcase: "planet"
---

<p>In last August, there were 24 new plugins published in the <a href="https://plugins.qgis.org/plugins/"><strong>QGIS plugin repository</strong>.</a></p>



<h2 class="wp-block-heading">Highlight</h2>



<p><strong>&#8220;Help us create the world&#8217;s most advanced open database on litter, brands &amp; plastic pollution.&#8221;</strong></p>



<p>This sentence welcomes us to the <a href="https://openlittermap.com/"><strong>website</strong></a> of the <strong>OpenLitterMap</strong> project, which aims at providing tools for any and all citizens to capture data on litter worldwide. This data can now be directly accessed in QGIS for visualisation and analysis purposes, thanks to the efforts of the plugin&#8217;s author <strong><a href="https://plugins.qgis.org/plugins/author/NaturalGIS/">NaturalGIS</a></strong>. Well done to everyone involved, and we wish all the luck to this great project.</p>



<h2 class="wp-block-heading">Overview</h2>



<p>Here follows the quick overview in reverse chronological order. If any of the names or short descriptions catches your attention, you can find the direct link to the plugin page in the table below: </p>



<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td><a href="https://plugins.qgis.org/plugins/theme_switcher/"><strong>Theme Switcher</strong></a></td></tr><tr><td>This plugin adds a popup to easily switch between layer themes.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/clickhouse_connector-main/"><strong>Clickhouse_Connector</strong></a></td></tr><tr><td>This plugin connects to Clickhouse.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/yarding_distance/"><strong>Yarding Distance</strong></a></td></tr><tr><td>This plugin calucurates the &#8220;Yarding Distance&#8221; (average of distance from Polygon to Points).</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/realearth-main/"><strong>RealEarth</strong></a></td></tr><tr><td>This plugin allows users to directly access SSEC RealEarth web services public catalog of near real-time satellite imagery and related ancillary data through the OGC standard web services of WMTS and WFS. A login to RealEarth is recommended to extend data volume quota before watermarking occurs, but is not required.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/SkyDeck-QGIS-Plugin-master/"><strong>SkyGIS</strong></a></td></tr><tr><td>This is a plugin to download files from Skydeck, process it in QGIS and upload the results back to Skydeck portal.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/arc_3d/"><strong>3D Arcs</strong></a></td></tr><tr><td>Tool to convert 2D lines to 3D Arcs.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/transit_reachability_analyser/"><strong>Transit Reachability Analyser</strong></a></td></tr><tr><td>Using OpenTripPlanner to calculate public transport reachability from a starting point to all stops in a GTFS feed.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/qmapod/"><strong>QMapOD</strong></a></td></tr><tr><td>Cartographie d&#8217;enquêtes O/D sous QGIS / Spatialite.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/PackageStyler/"><strong>PackageStyler</strong></a></td></tr><tr><td>Style all loaded layers in the GPKG in a few clicks.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/AutonomousGIS_GeodataRetrieverAgent/"><strong>AutonomousGIS_GeoDataRetrieverAgent</strong></a></td></tr><tr><td>An autonomous agent framework to select geospatial data and then fetch data by generating and executing programs with self-debugging.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/merqantile/"><strong>merqantile</strong></a></td></tr><tr><td>Easy visualisation of XYZ tile bounds.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/featuretransfer/"><strong>Feature Transfer GIS Tool</strong></a></td></tr><tr><td>Feature Transfer Tool provides a seamless way to copy and paste features between layers.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/SelectLines/"><strong>Select Lines</strong></a></td></tr><tr><td>Select Lines.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/layeratlas/"><strong>Layer Atlas</strong></a></td></tr><tr><td>Discover and share geospatial layers easily within QGIS.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/verificar_sobreposicao/"><strong>Verificar_Sobreposicao</strong></a></td></tr><tr><td>Verifica sobreposição de feição.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/chainage_tool/"><strong>Chainage Tool</strong></a></td></tr><tr><td>This tool provides utility to convert line to chainage points.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/Raster-Value-Regular/"><strong>Raster Value Regular</strong></a></td></tr><tr><td>Smooth and interpolate grid from a Raster Layer using RegularGridInterpolator from scipy, then apply values to a vector layer as attribute.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/eo_pavement_analysis/"><strong>Earth Observation Pavement Analysis</strong></a></td></tr><tr><td>This plugin prepares the data sets to train, validate and assess earth observation imagery for pavement analysis.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/openlittermap/"><strong>OpenLitterMap</strong></a></td></tr><tr><td>Processing provider to download raw data from the OpenLitterMap (<a href="https://openlittermap.com" rel="nofollow">https://openlittermap.com</a>) project.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/TilePick/"><strong>TilePick</strong></a></td></tr><tr><td>Easy load raster or point cloud tiles from index vector layer or map canvas position.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/QgisWcs2Client/"><strong>WCS 2</strong></a></td></tr><tr><td>A OGC WCS 2.0 / EO-WCS Client to download spatio-temporal subsets from time-series datacubes.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/iadb_toolbox/"><strong>Disaster Risk Management IADB Toolbox</strong></a></td></tr><tr><td>Processing provider that integrates various disaster risk management tools into QGIS.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/PhotoViewer360/"><strong>PhotoViewer360</strong></a></td></tr><tr><td>PL: Wtyczka umożliwiająca import i wizualizację zdjęć panoramicznych. ENG: Plugin for importing and visualising local panoramic images.</td></tr><tr><td><a href="https://plugins.qgis.org/plugins/online_map_linker/"><strong>Online Map Linker</strong></a></td></tr><tr><td>This plugin makes links from points to online map.</td></tr></tbody></table></figure>
