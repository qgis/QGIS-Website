---
source: "blog"
title: "Lutra Consulting: Summary of the 3D features & enhancements in QGIS 3.30"
image: "pointcloud-qgis-cf3-update1."
date: "2023-03-08"
link: "https://lutraconsulting.co.uk/blog/2023/03/07/pointcloud-qgis-cf3-update1/"
draft: "true"
showcase: "planet"
---

<p>QGIS 3.30 was released late last week and we are pleased to announce the new features introduced as a part of our <a href="https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/">latest crowdfunding campaign to improve 3D, point cloud and elevation data.</a></p>

<h2 id="thank-you">Thank you</h2>

<p>First and foremost, thanks to the generous support from the community to fund our work. Here is the list of our contributors in no particular order:</p>

<p><a href="https://ign.fr/">IGN (INSTITUT NATIONAL DE L’INFORMATION GEOGRAPHIQUE ET FORESTIERE)</a>, <a href="https://www.maanmittauslaitos.fi/en">National Land Survey of Finland</a>, K2 Engineering GmbH, ProScape Consulting, <a href="https://www.vgregion.se/">Västra Götalandsregionen</a>, <a href="http://www.kristianstad.se">Kristianstads kommun</a>, <a href="http://www.ignfi.com">IGN FI</a>, <a href="https://larriereguichet.fr/">L’Arrière Guichet</a>, <a href="https://septima.dk/">Septima</a>, <a href="https://www.qwast-gis.com/">QWAST-GIS</a>, <a href="www.atapex.sk">ATAPEX s.r.o.</a>, <a href="http://www.redcatch.at">REDcatch GmbH</a>, F.A.R.M. Facilitazioni Agroecologiche Regionali Mobili, EPYMA TERRITORIO Y MEDIO AMBIENTE, SL, GEO EXPLORATION LTD, <a href="http://www.bhinc.com">Bohannan Huston, Inc.</a>, <a href="http://www.lidarguys.com">Lidar Guys</a>, <a href="https://www.ne.ch/Pages/accueil.aspx">Neuchâtel- Service de la géomatique</a>, <a href="https://wgsair.com/">Wooding Geospatial Solutions</a>, <a href="https://www.vevey.ch/">Ville de Vevey</a>, <a href="http://qgis.ch">QGIS User Group Switzerland</a>, <a href="https://www.ecophylla.ca/">Ecophylla Consulting</a>, <a href="https://refactor.com.au">Refactor</a>, <a href="https://locatepress.com/">Locate Press</a>, <a href="https://www.alta.is/">Alta ehf</a>, <a href="https://messtechnik.ch/">Oester Messtechnik GmbH</a>, <a href="https://www.rudaz.ch/index.php/en/">RUDAZ+PARTNER AG</a>, <a href="http://bayesmap.com/">BayesMap Solutions LLC</a>, <a href="https://geoace.net">GEOACE</a>, Natalie Gyles, Andreas Neumann, Dougal Munro, <a href="https://spatialthoughts.com/">Spatial Thoughts</a>, <a href="https://cicadagis.com/">Cicada Systems GIS Consulting</a>, Cori Hermle, <a href="https://powellmapping.com/">Powell Asset Mapping LLC</a>, Darren Farmer, Greg Hall, <a href="http://www.ecothought.com">Ecothought Pty Ltd</a>, Gabriel Diosan, Bhutan QGIS Group, <a href="https://www.ultimatumfinesse.co.bw/">Ultimatum Finesse</a>, <a href="http://www.balrisk.com/">Balanced Risk Strategies, Ltd</a>, Concordia University, <a href="https://burmis.ca/">Burmis Studio Inc.</a>, Nicholas Hadaller, Angello Villatoro, Yoichi Kayama, Hennessy Amor Becerra Ayala, <a href="http://flowdesign.co.nz/">Flow Design Limited</a>, <a href="https://bnhr.xyz">BNHR.XYZ</a>, Roberto Moyano, Benjamin Kuster, Goldspot, <a href="https://www.northrivergeographic.com/">North River Geographic Systems, Inc</a>, David W. Wormuth, Victor Graphics, Valley Spatial, Stephen Mather, SANTIAGO AURELIO MOTA, Kelly Crowell, Brian Duhan, Paddy Fisher, <a href="https://uk.osgeo.org/">OSGEO:UK</a>, Christian Gugl, <a href="https://www.craig.fr/">GIP CRAIG - Centre Régional Auvergne-Rhône-Alpes de l’Infromation Géographqiue</a>, Raphael Mabit, Tibor Lieskovský, Kerstin Fohlert, Zhan Li, Bernd Vogelgesang, Marlin Müller, Johannes Bonekamp, <a href="http://eurojams-last-exit.blogspot.com/">Stefan Giese</a>, Fabian Faßnacht, <a href="https://www.qgis.se/">QGIS Sweden user group</a>, <a href="http://www.falo.se">Falo</a>, <a href="https://genal.es/">DAVID GARCIA HERNANDEZ</a>, <a href="http://www.lintgeospatial.ie">Lint Data and Geospatial</a>, Cliff Sin Wai Lau, Grzegorz Sapijaszko, Łukasz Rapa, Alessandro Pintucci and Maarten Pronk.</p>

<p>Our gratitude also goes to those who want to remain anonymous.</p>

<h2 id="global-map-shading">Global map shading</h2>

<center>
  <p><img title="Map data without global terrain shading" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_gtr1.png" alt="Map data without global terrain shading" /></p>
</center>

<center>
  <p><img title="Global terrain shading for point clouds, dem and vectors" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_gtr2.png" alt="Global terrain shading for point clouds, dem and vectors" /></p>
</center>

<p>To see this feature in action, you can open QGIS project properties and under Terrain, there should be an option for Global Map Shading. You will need to first add a raster as your DEM under the Terrain section.</p>

<p>Elevations of all these layers are combined and the considered elevation is chosen depending on one of two methods:</p>
<ol>
  <li>the highest elevation between raster, mesh or point cloud layers will be selected.</li>
  <li>elevation will be selected based on the order of layers in the layer panel.</li>
</ol>

<p>Depending on the context and the use of the map the user can choose the more appropriate method.</p>

<p>For now, the shading methods implemented are the Eye Dome Lighting and the hill-shade. More methods could be added in the future - such as ambient occlusion.</p>

<p>The user can choose the elevation shading settings in a specific UI widget that can be found in two places:</p>

<ol>
  <li>under the Project Properties, within the same tab of the project elevation settings.</li>
  <li>under the Styling Panel, a new tab is added for quick access to the user.</li>
</ol>

<center>
  <p><img title="Global terrain shading settings in project properties" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_gtr3.png" alt="Global terrain shading settings in project properties" /></p>
</center>

<center>
  <p><img title="Global terrain shading settings in style panel" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_gtr4.png" alt="Global terrain shading settings in style panel" /></p>
</center>

<h2 id="profile-elevation-within-print-composer">Profile elevation within print composer</h2>

<p>This work was carried out by our collaborator <a href="https://north-road.com/">North Road</a>. The profile tool can embed elevation profiles within print layouts. It is possible to add beautifully styled profiles in your print outputs.</p>

<center>
  <p><img title="Embeding elevation profile in the print composer" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_profile.png" alt="Embeding elevation profile in the print composer" /></p>
</center>

<p>To use elevation profiles in print layouts, simply click the  Add Elevation Profile button <img title="icon elevation profile in print composer" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_profile_icon.png" alt="icon elevation profile in print composer" /> in the toolbar, and then to initialize it, copy profile configuration from an existing elevation profile from QGIS main window using the “Copy From Profile” button.</p>

<center>
  <p><img title="Elevation profile settings in the print composer" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_profile_pc_settings.png" alt="Elevation profile settings in the print composer" /></p>
</center>

<h2 id="3d-navigation-improvements">3D navigation improvements</h2>

<p>With the new improvements, you can:</p>
<ol>
  <li>move camera vertically using ctrl+shift+left mouse button</li>
  <li>keep zooming with the wheel while moving the mouse</li>
  <li>continue right mouse button zooming when pointer exits the viewport</li>
</ol>

<h2 id="improve-zoom-extents-in-3d">Improve zoom-extents in 3D</h2>

<p>The terrain’s and point cloud layers’ elevation range are taken into account so that the camera is not positioned below the scene’s contents, which was the case when using the terrain’s vertical scale setting to exaggerate the elevation differences.</p>

<h2 id="limit-3d-scenes-2d-extent">Limit 3D scenes’ 2D extent</h2>
<p>3D Views can now be limited to a specific 2D extent. The terrain is clipped and no 3D features beyond that extent are loaded, making it easy to render specific areas of big QGIS projects. The project’s 2D extent is used by default which can then be adjusted in each 3D view separately using the new General tab in 3D configuration.</p>

<center>
  <p><img title="Limiting 3D map extent" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_3d_extent_clip_inaction.gif" alt="Limiting 3D map extent" /></p>
</center>

<center>
  <p><img title="Limiting 3D map extent" src="https://lutraconsulting.co.uk/img/posts/pc3_update1_3d_extent_clip1.png" alt="Limiting 3D map extent" /></p>
</center>

<h2 id="future-updates">Future updates</h2>
<p>There will be more features planned for QGIS 3.32. We are finalising the Processing framework for point cloud data and it should be available on QGIS master in coming weeks.</p>

<p>Please do not hesitate to <a href="mailto:info@lutraconsulting.co.uk">contact us</a> if you have any suggestions to improve QGIS 3D and point cloud support.</p>
