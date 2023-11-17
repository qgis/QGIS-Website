---
source: "blog"
title: "Lutra Consulting: 3D Tiles in QGIS"
image: "3d-tiles-in-QGIS."
date: "2023-11-16"
link: "https://lutraconsulting.co.uk/blog/2023/11/16/3d-tiles-in-QGIS/"
draft: "true"
showcase: "planet"
---

<p>Earlier this year, in collaboration with <a href="https://north-road.com/2023/06/01/cesium-ecosystem-grant-win-for-qgis-3d-tiles/">North Road</a> we were awarded a <a href="https://cesium.com/cesium-ecosystem-grants/grant-directory/">grant from Cesium</a> to introduce 3D tiles support in QGIS. The feature was developed successfully and shipped with QGIS 3.34.</p>

<p>In this blog post, you can read more about how to work with this feature, where to get data and how to display your maps in 2D and 3D. For a video demo of this feature, you can watch <a href="https://www.youtube.com/watch?v=vazJlXTcLsw">Nyall Dawson’s presentation on Youtube</a>.</p>

<h1 id="what-are-3d-tiles">What are 3D tiles?</h1>

<p>3D tiles are a specification for streaming and rendering large-scale 3D geospatial datasets. They use a hierarchical structure to efficiently manage and display 3D content, optimising performance by dynamically loading appropriate levels of detail. This technology is widely used in urban planning, architecture, simulation, gaming, and virtual reality, providing a standardised and interoperable solution for visualising complex geographical data.</p>

<p>Examples of 3D tiles:</p>

<center>
  <p><img title="3D tiles of Zurich from Swisstopo" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_example_1.png" alt="3D tiles of Zurich from Swisstopo" /></p>
  Data from Swisstopo (https://map.geo.admin.ch/)
</center>

<center>
  <p><img title="Washington - 3D Surface Model (Vricon, Cesium)" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_example_2.png" alt="Washington - 3D Surface Model (Vricon, Cesium)" /></p>
  Washington - 3D Surface Model (Vricon, Cesium)
</center>

<h1 id="3d-tiles-in-qgis">3D tiles in QGIS</h1>

<p>To be able to use 3D tiles in QGIS, you need to have QGIS 3.34 or later. You can add a new connection to a 3D tile service from within the <strong>Data Source Manager</strong> under <strong>Scene</strong>:</p>

<center>
  <p><img title="Adding a new 3D tile service from Data Source Manager in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_data_source_manager.png" alt="Adding a new 3D tile service from Data Source Manager in QGIS" /></p>
  Adding a new 3D tile service from Data Source Manager in QGIS
</center>

<p>Alternatively, you can add the service from your <strong>Browser Panel</strong>:</p>

<center>
  <p><img title="3D tiles data provider in the Browser panel" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_browser_panel.png" alt="3D tiles data provider in the Browser panel" /></p>
  3D tiles data provider in the Browser panel
</center>

<p>To test the feature, you can use the following 3D tiles service:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>
Name: Bathurst
URL: https://nsw.digitaltwin.terria.io/api/v0/data/bathurst-reality-mesh-2022-03-29/Scene/Cesium_Bathurst.json

</code></pre></div></div>

<center>
  <p><img title="Creating a new connection to a 3D tiles service" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_scene_bathurst.png" alt="Creating a new connection to a 3D tiles service" /></p>
  Creating a new connection to a 3D tiles service
</center>

<p>You can then add the map from the newly generated connection to QGIS:</p>

<center>
  <p><img title="Adding a new 3D tiles to QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_bathurst.png" alt="Adding a new 3D tiles to QGIS" /></p>
  Adding a new 3D tiles to QGIS
</center>

<p>By default, the layer is styled using texture, but you can change it to see the wireframe mesh behind the scene:</p>

<center>
  <p><img title="3D tiles’ mesh wireframe" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_mesh_bathurst.png" alt="3D tiles’ mesh wireframe" /></p>
  3D tiles’ mesh wireframe
</center>

<p>You can change the mesh fill and line symbols similar to the vector polygons. Alternatively, you can use texture colors. This will render each mesh element with the average value of the full texture. This is ideal when dealing with a large dataset and want to get a quick overview of the data:</p>

<center>
  <p><img title="3D tiles with texture color for meshes" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_mesh_styled_bathurst.png" alt="3D tiles with texture color for meshes" /></p>
  3D tiles with texture color for meshes
</center>

<p>To view the data in 3D, you can open a new 3D map. Similar to 2D map, by zooming in/out, finer resolution tiles will be fetched and displayed:</p>

<center>
   <iframe width="560" height="315" src="https://www.youtube.com/embed/fCnxkzkc3-M?si=oheQwvOZH-0xaZBe&amp;start=11" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>
</center>

<h1 id="using-data-from-cesium-ion">Using data from Cesium ion</h1>

<p><a href="https://ion.cesium.com/">Cesium ion</a> is a cloud-based platform for managing and streaming 3D geospatial data. It simplifies data management, visualisation, and sharing.</p>

<p>To add 3D tiles from Cesium ion, you need to first sign up to their service here:
https://ion.cesium.com/tokens</p>

<p>Under <strong>Asset Depot</strong>, you will see a catalogue of publicly available datasets. You can also upload your own 3D models (such as OBJ or PLY), georeference them and get them converted to 3D tiles.</p>

<p>You can also add one of the existing tile service under <a href="https://ion.cesium.com/assetdepot">https://ion.cesium.com/assetdepot</a> and select the tile service and then click on <strong>Add to my assets</strong>:</p>

<center>
  <p><img title="Adding an existing dataset to your Cesium ion assets" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_cesium_ion.png" alt="Adding an existing dataset to your Cesium ion assets" /></p>
  Adding an existing dataset to your Cesium ion assets
</center>

<p>You can use the excellent Cesium ion plugin by <a href="https://plugins.qgis.org/plugins/cesium_ion/">North Road</a> from the QGIS repository to add the data to QGIS:</p>

<center>
  <p><img title="Adding Cesium ion assets to QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_cesium_ion_assets.png" alt="Adding Cesium ion assets to QGIS" /></p>
  Adding Cesium ion assets to QGIS
</center>

<h1 id="working-with-google-3d-data">Working with Google 3D data</h1>

<p>In addition to accessing Google Photorealistic 3D tiles from Cesium ion, you can also add the tiles directly in QGIS. First you will need to follow the instructions below and obtain API keys for 3D tiles:
<a href="https://developers.google.com/maps/documentation/tile/cloud-setup">https://developers.google.com/maps/documentation/tile/cloud-setup</a></p>

<p>During the registration process, you will be asked to add your credit card details. Currently (November 2023), they do not charge you for using the service.</p>

<p>Once you have obtained the API key, you can add Google tiles using the following connection details:</p>

<center>
  <p><img title="Adding Google 3D tiles in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_google_connection.png" alt="Adding Google 3D tiles in QGIS" /></p>
  Adding Google Photorealistic tiles in QGIS
</center>

<h1 id="notes-and-remarks">Notes and remarks</h1>

<ul>
  <li><strong>Adjusting  map extents for large scenes</strong></li>
</ul>

<p>When dealing with large scenes, map extents should be set to a smaller area to be able to view it in 3D. This is the current limitation of QGIS 3D maps as it cannot handle scenes larger than 500 x 500 km.</p>

<p>To change the map extent, you can open <strong>Project Properties</strong> and under <strong>View Settings</strong> change the extent. In the example below, the map extent has been limited only to a part of London, so we can view Google Photorealistic tiles in the 3D map without rendering issues.</p>

<center>
  <p><img title="Limiting project extent in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_map_extent.png" alt="Limiting project extent in QGIS" /></p>
  Limiting project extent in QGIS
</center>

<center>
  <p><img title="3D tiles from Google in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_map_3d_london.png" alt="3D tiles from Google in QGIS" /></p>
  3D tiles from Google in QGIS
</center>

<ul>
  <li><strong>Network cache size</strong></li>
</ul>

<p>If you are handling a large dataset, it is recommended to increase network cache size to 1 GB or more. The default value in QGIS is much lower and it results in slower rendering of the data.</p>

<center>
  <p><img title="Increasing Cache size in QGIS for faster rendering" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_network_cache.png" alt="Increasing Cache size in QGIS for faster rendering" /></p>
  Increasing Cache size in QGIS for faster rendering
</center>

<ul>
  <li><strong>Overlaying other 3D data</strong></li>
</ul>

<p>When you try to overlay other data sets on top of a global 3D tiles, the vertical datum might not match and hence you will see the data in the wrong place in a 3D map. To fix the issue, you may need to use elevation offsetting to shift the data along the Z axis under Layer Properties:</p>

<center>
  <p><img title="Offsetting elevation of a layer in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_elevation_offset.png" alt="Offsetting elevation of a layer in QGIS" /></p>
  Offsetting elevation of a layer in QGIS
</center>

<h1 id="future-works">Future works</h1>

<p>This is the first implementation of the 3D tiles in QGIS. For the future, we would like to add more features for handling and creation of the 3D tiles. Our wishlist in no particular order is:</p>

<ul>
  <li>Globe view: QGIS 3D cannot handle large scenes or unprojected views.</li>
  <li>More advanced styling of meshes: as an example, users will be able to create their own style.</li>
  <li>3D In-door navigation: as an example users will be able to navigate inside buildings and potentially it will bring BIM data closer to QGIS</li>
  <li>Generation of 3D tiles inside QGIS: adding a processing tool in QGIS to generate 3D Tiles from your map data.</li>
</ul>

<center>
  <p><img title="Styling of 3D tiles" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_3d_styled_mesh.png" alt="Styling of 3D tiles" /></p>
  Styling of 3D tiles (image from https://cesium.com/learn/ion/stories-styling/)
</center>

<p>If you would like to see those features in QGIS and want to fund the efforts, do not hesitate to <a href="mailto:info@lutraconsulting.co.uk">contact us</a>.</p>
