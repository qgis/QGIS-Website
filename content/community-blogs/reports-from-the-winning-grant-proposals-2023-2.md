---
source: "blog"
title: "QGIS Project blog: Reports from the winning grant proposals 2023"
image: "reports-from-the-winning-grant-proposals-2023-2."
date: "2024-08-16"
link: "https://blog.qgis.org/2024/08/16/reports-from-the-winning-grant-proposals-2023-2/"
draft: "true"
showcase: "planet"
---

<p>With the <a href="https://blog.qgis.org/2023/06/26/qgis-grant-programme-2023-results/">QGIS Grant Programme 2023</a>, we were able to support six proposals (four in the first round and two in the second round) that are aimed to improve the QGIS project, including software, infrastructure, and documentation. The following reports summarize the work performed in the first four proposals:  </p>



<ol class="wp-block-list">
<li><span class="reference"><a class="issue-link js-issue-link" href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/243"><strong>QGIS Bug Tracker cleanup (#266) </strong></a></span> &#8211; <a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/266#issuecomment-1889177413" rel="nofollow">Report</a><br /> We have identified and closed ~291 tickets, among them:
<ul class="wp-block-list">
<li>162 bugreports and feature requests which were already fixed or implemented</li>



<li>29 bugreports and feature requests which are invalid (data issues, wrong use of functionality, etc)</li>



<li>57 duplicate bugreports and feature requests</li>



<li>5 won&#8217;t fix bugreports</li>



<li>5 bugreports were converted to feature requests</li>



<li>33 tickets were closed (does not contain steps to reproduce, test data and no feedback was provided within several month)</li>



<li>Additionally we ensured that all tickets has correct tags assigned to to make them easier to find.</li>
</ul>
</li>



<li><span class="reference"><a class="issue-link js-issue-link" href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/242"><strong>Porting to C++ and harmonization of Processing algorithms (#271)</strong></a></span> &#8211; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2023-October/010145.html" rel="nofollow">Report</a><br />The QGIS Porting to C++ and Harmonisation of Processing Algorithms grant is now complete.
<ul class="wp-block-list">
<li>Existing Processing algorithms Voronoi Polygons and Delaunay Triangulation have been ported to C++ and now use GEOS instead of the unmaintained Python module. </li>



<li>Two algorithms for generating XYZ tiles (directory and MBTiles variants) have been ported to C++ using a safer and cleaner multi-threading approach. </li>



<li>The Align Rasters tool, which was not exposed to Processing, has been removed and a new Processing algorithm with the same functionality has been added. </li>



<li>The existing Raster Calculator algorithm has been ported to C++. The algorithm now has two variants: a toolbox version that works the same way as before, and a modeler version that uses the same approach to input naming as the GDAL raster calculator.</li>
</ul>
</li>



<li><strong><span class="reference"><a class="issue-link js-issue-link" href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/245">Add vertical CRS handling to QGIS (#267)</a></span> </strong>&#8211; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-July/010301.html">Report</a>
<ul class="wp-block-list">
<li>As of QGIS 3.34, QGIS can now create and handle vertical and compound CRSes.</li>



<li>In QGIS 3.34 coordinate transforms were reworked so that they function correctly with vertical transformation, if both the source and destination CRS have vertical components. </li>



<li>In QGIS 3.36 the coordinate reference selection widgets were updated to offer choices of 2d only, compound, or vertical only CRSes. </li>



<li>In version 3.38, we introduced a new setting for QGIS projects, for their vertical reference system. Users can control this through project properties, and it&#8217;s accessible via PyQGIS and via associated expression variables (eg @project_vertical_crs) for use in print layouts. </li>



<li>Similarly, in 3.38 we introduced the API support for map layers to have a vertical CRS. (This was not exposed to users in 3.38 though) </li>



<li>In QGIS 3.40 so far we have exposed the vertical CRS setting for vector layers to users (via the layer properties dialog), allowing users to specify the associated vertical CRS for these layers. The vertical CRS is respected in elevation profile plots, in Identify tool results, and in 3D Map views (assuming the 3D map is created with an associated vertical CRS). </li>



<li>There is an open pull-request for 3.40 to expose the vertical CRS for point cloud layers in a similar way, with the vertical CRS being respected in elevation profiles, identify tool results, and 3D map views </li>



<li>We have open pull requests for 3.40 to show layer vertical CRS information in the layer properties &#8220;information&#8221; pages, and add expression variables at the layer scope (eg @layer_vertical_crs).</li>
</ul>
</li>



<li><strong><span class="reference"><a class="issue-link js-issue-link" href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/247">Improve test result handling on QGIS CI (#268)</a></span> </strong>&#8211; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2023-November/010162.html">Report</a><br />Any tests which fail a rendering comparison will write a descriptive comment to the PR. The comment details which render tests failed, where they are in the code, and includes some helpful pointers to downloading the full test report and the QGIS developer documentation. We also implemented lots of improvements in running the tests locally and how the render test reports are generated and presented to developers.</li>
</ol>



<p>Thank you to everyone who participated and made this round of grants a great success and thank you to all our <a href="https://qgis.org/en/site/about/sustaining_members.html">sustaining members</a> and donors who make this initiative possible!</p>



<p></p>
