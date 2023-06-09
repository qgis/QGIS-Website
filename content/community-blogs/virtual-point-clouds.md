---
source: "blog"
title: "Lutra Consulting: Virtual Point Clouds (VPC)"
image: "virtual-point-clouds."
date: "2023-06-08"
link: "https://lutraconsulting.co.uk/blog/2023/06/08/virtual-point-clouds/"
draft: "true"
showcase: "planet"
---

<p>As a part of our <a href="https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/">crowdfunding</a> campaign we have introduced a new method to handle a large number of point cloud files. In this article, we delve into the technical details of the new format, rationale behind our choice and how you can create, view and process virtual point cloud files.</p>

<h2 id="rationale">Rationale</h2>
<p>Lidar surveys of larger areas are often multi-terabyte datasets with many billions of points. Having such large datasets represented as a single point cloud file is not practical due to the difficulties of storage, transfer, display and analysis. Point cloud data are therefore typically stored and distributed split into square tiles (e.g. 1km x 1km), each tile having a more manageable file size (e.g. ~200 MB when compressed).</p>

<p>Tiling of data solves the problems with size of data, but it introduces issues when processing or viewing an area of interest that does not fit entirely into a single tile. Users need to develop workflows that take into account multiple tiles and special care needs to be taken to deal with data near edges of tiles to avoid unwanted artefacts in outputs. Similarly, when viewing point cloud data, it becomes cumbersome to load many individual files and apply the same symbology.</p>

<p>Here is an example of several point cloud tiles loaded in QGIS. Each tile is styled based on min/max Z values of the tile, creating visible artefacts on tile edges. The styling has to be adjusted for each layer separately:</p>

<center>
  <p><img title="An example of individual point cloud tiles loaded in QGIS, each styled differently" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_individual_tiles.png" alt="An example of individual point cloud tiles loaded in QGIS, each styled differently" /></p>
</center>

<h2 id="virtual-point-clouds">Virtual Point Clouds</h2>
<p>In the GIS world, many users are familiar with the concept of virtual rasters. A virtual raster is a file that simply references other raster files with actual data. In this way, GIS software then treats the whole dataset comprising many files as a single raster layer, making the display and analysis of all the rasters listed in the virtual file much easier.</p>

<p>Borrowing the concept of virtual rasters from GDAL, we have introduced a new file format that references other point cloud files - and we started to call it <strong>virtual point cloud (VPC)</strong>. Software supporting virtual point clouds handles the whole tiled dataset as a single data source.</p>

<p>At the core, a virtual point cloud file is a simple JSON file with .vpc extension, containing references to actual data files (e.g. LAS/LAZ or COPC files) and additional metadata extracted from the files. Even though it is possible to write VPC files by hand, it is strongly recommended to create them using an automated tool as described later in this post.</p>

<p>On a more technical level, a virtual point cloud file is based on the increasingly popular STAC specification (the whole file is a STAC API ItemCollection). For more details, please refer to the <a href="https://github.com/PDAL/wrench/blob/main/vpc-spec.md">VPC specification</a> that also contains best practices and optional extensions (such as overviews).</p>

<h2 id="virtual-point-clouds-in-qgis">Virtual Point Clouds in QGIS</h2>

<p>We have added support for virtual point clouds in QGIS 3.32 (released in June 2023) thanks to the many organisations and individuals who contributed to our last year’s joint <a href="https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-processing-qgis/">crowdfunding with North Road and Hobu</a>. The support in QGIS consists of three parts:</p>

<ol>
  <li>Create virtual point clouds from a list of individual files</li>
  <li>Load virtual point clouds as a single map layer</li>
  <li>Run processing algorithms using virtual point clouds</li>
</ol>

<p>Those who prefer using command line tools, <a href="https://github.com/PDAL/wrench">PDAL wrench</a> includes a build_vpc command to create virtual point clouds, and all the other PDAL wrench commands support virtual point clouds as the input.</p>

<h2 id="using-virtual-point-clouds">Using Virtual Point Clouds</h2>

<p>In this tutorial, we are going to generate a VPC using the new Processing algorithm, load it in QGIS and then generate a DTM from terrain class. You will need QGIS 3.32 or later for this. For the purpose of this example, we are using the LiDAR data provided by the <a href="https://geoservices.ign.fr/lidarhd#telechargementclassifiees">IGN France data hub</a>.</p>

<p>In QGIS, open the Processing toolbox panel, search for the <strong>Build virtual point cloud (VPC)</strong> algorithm ((located in the Point cloud data management group):</p>

<center>
  <p><img title="VPC in the Processing toolbox" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_processing.png" alt="VPC in the Processing toolbox" /></p>
  VPC algorithm in the Processing toolbox
</center>

<p>In the algorithm’s window, you can add point cloud layers already loaded in QGIS or alternatively point it to a folder containing your LAZ/LAS files. It is recommended to also check the optional parameters:</p>

<ul>
  <li>
    <p>Calculate boundary polygons - QGIS will be able to show the exact boundaries of data (rather than just rectangular extent)</p>
  </li>
  <li>
    <p>Calculate statistics - will help QGIS to understand ranges of values of various attributes</p>
  </li>
  <li>
    <p>Build overview point cloud - will also generate a single “thinned” point cloud of all your input data (using only every 1000th point from original data). The overview point cloud will be created next to the VPC file - for example, for mydata.vpc, the overview point cloud would be named mydata-overview.copc.laz</p>
  </li>
</ul>

<center>
  <p><img title="VPC algorithm inputs, outputs and options" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_alg.png" alt="VPC algorithm inputs, outputs and options" /></p>
  VPC algorithm inputs, outputs and options
</center>

<p>After you set the output file and start the process, you should end up with a single VPC file referencing all your data. If you leave the optional parameters unchecked, the VPC file will be built very quickly as the algorithm will only read metadata of input files. With any of the optional parameters set, the algorithm will read all points which can take some time.</p>

<p>Now you can load the VPC file in QGIS as any other layer - using QGIS browser, Data sources dialog in QGIS or by doing drag&amp;drop from a file browser. After loading a VPC in QGIS, the 2D canvas will show boundaries of individual files - and as you zoom in, the actual point cloud data will be shown. Here, a VPC loaded together with the overview point cloud:</p>

<center>
  <p><img title="VPC algorithm output" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_output.png" alt="VPC algorithm output" /></p>
  Virtual point cloud (thinned version) generated by the VPC algorithm
</center>

<p>Zooming in QGIS in 2D map with elevation shading - initially showing just the overview point, later replaced by the actual dense point cloud:</p>

<center>
  <p><img title="VPC algorithm output in 2D maps" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_2d_output.gif" alt="VPC algorithm output in 2D maps" /></p>
  VPC output on 2D: displaying details when zooming in
</center>

<p>In addition to 2D maps, you can view the VPC in a 3D map windows too:</p>

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/gBoyPjuWkBs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>
</center>

<p>If the input files for VPCs are not COPC files, QGIS will currently only show their boundaries in 2D and 3D views, but processing algorithms will work fine. It is however possible to use the <strong>Create COPC</strong> algorithm to batch convert LAS/LAZ files to COPC files, and then load VPC with COPC files.</p>

<p>It is also worth noting that VPCs also work with input data that is not tiled - for example, in some cases the data are distributed as flightlines (with lots of overlaps between files). While this is handled fine by QGIS, for the best performance it is generally recommended to first tile such datasets (using the Tile algorithm) before doing further display and analysis.</p>

<h2 id="processing-data-with-virtual-point-clouds">Processing Data with Virtual Point Clouds</h2>

<p>Now that we have the VPC generated, we can run other processing algorithms. For this example, we are going to convert the ground class of the point cloud to a digital terrain model (DTM) raster. In the QGIS Processing toolbox, search for <strong>Export to raster</strong> algorithm (in the Point cloud conversion group):</p>

<center>
  <p><img title="VPC as an input to processing algorithms" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_export_to_raster.png" alt="VPC as an input to processing algorithms" /></p>
  VPC layer can be used as an input to the point cloud processing algorithm
</center>

<p>This will use the Z values from the VPC layer and generate a terrain raster based on a user defined resolution. The algorithm will process the tiles in parallel, taking care of edge artefacts (at the edges, it will read data also from the neighbouring tiles). The output of this algorithm will look like this:</p>

<center>
  <p><img title="Converting a VPC layer to a raster" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_export_to_raster_output.png" alt="Converting a VPC layer to a raster" /></p>
  Converting a VPC layer to a DTM
</center>

<p>The output raster contains holes where there were no points classified as ground. If needed for your use case, you can fill the holes using <strong>Fill nodata</strong> algorithm from GDAL in the Processing toolbox and create a smooth terrain model for your input Virtual Point Cloud layer:</p>

<center>
  <p><img title="Filling the holes in the DTM" src="https://lutraconsulting.co.uk/img/posts/
pc3_vpc_export_to_raster_output_filled.png" alt="Filling the holes in the DTM" /></p>
  Filling the holes in the DTM
</center>

<p>Virtual point clouds can be used also for any other algorithms in the point cloud processing toolbox. For more information about the newly introduced algorithms, please see our previous <a href="https://www.lutraconsulting.co.uk/blog/2023/05/30/pointcloud-qgis-processing/">blog post</a>.</p>

<p>All of the point cloud algorithms also allow setting filtering extent, so even with a very large VPC, it is possible to run algorithms directly on a small region of interest without having to create temporary point cloud files. Our recommendation is to have input data ready in COPC format, as this format provides more efficient access to data when spatial filtering is used.</p>

<h2 id="streaming-data-from-remote-sources-with-vpcs">Streaming Data from Remote Sources with VPCs</h2>

<p>One of the very useful features of VPCs is that they work not only with local files, but they can also reference data hosted on remote HTTP servers. Paired with COPCs, point cloud data can be streamed to QGIS for viewing and/or processing - that means QGIS will only download small portions of data of a virtual point cloud, rather than having to download all data before they could be viewed or analysed.</p>

<p>Using IGN’s lidar data provided as COPC files, we have built a small virtual point cloud <a href="/downloads/ign-chambery.vpc">ign-chambery.vpc</a> referencing 16 km2 of data (nearly 700 million points). This VPC file can be loaded in QGIS and used for 2D/3D visualisation, elevation profiles and processing, with QGIS handling data requests to the server as necessary. Processing algorithms only take a couple of seconds if the selected area of interest is small (make sure to set the “Cropping extent” parameter of algorithms).</p>

<p>All this greatly simplifies data access to point clouds:</p>

<ul>
  <li>
    <p><strong>Data producers</strong> can use very simple infrastructure - a server hosting static COPC files together with a single VPC file referencing those COPC files.</p>
  </li>
  <li>
    <p><strong>Users</strong> can use QGIS to view and process point cloud data as a single map layer, with no need to download large amounts of data, QGIS (and PDAL) taking care of streaming data as needed.</p>
  </li>
</ul>

<p>We are very excited about the opportunities that virtual point clouds are bringing to users, especially when combined with COPC format and access from remote servers!</p>

<p>Thanks again to all <a href="https://www.lutraconsulting.co.uk/blog/2023/03/07/pointcloud-qgis-cf3-update1/">contributors to our crowdfunding</a> campaign - without their generous support, this work would not have been possible.</p>

<p><a href="mailto:info@lutraconsulting.co.uk">Contact us</a> if you would like to add more features in QGIS to handle, analyse or visualise lidar data.</p>
