---
source: "blog"
title: "anitagraser.com: Visualizing trajectories with QGIS & MobilityDB"
image: "visualizing-trajectories-with-qgis-mobilitydb."
date: "2022-11-19"
link: "https://anitagraser.com/2022/11/19/visualizing-trajectories-with-qgis-mobilitydb/"
draft: "true"
showcase: "planet"
---

<p>In <a href="https://anitagraser.com/2022/10/01/visualizing-iot-time-series-with-qgis-mobilitydb/">the previous post</a>, we — creatively ;-) — used <a href="https://mobilitydb.com">MobilityDB</a> to visualize stationary IOT sensor measurements. </p>



<p>This post covers the more obvious use case of visualizing trajectories. Thus bringing together the MobilityDB trajectories created in <a href="https://anitagraser.com/2022/09/30/detecting-close-encounters-using-mobilitydb-1-0/">Detecting close encounters using MobilityDB 1.0</a> and visualization using Temporal Controller.</p>



<p>Like in the previous post, the <strong>valueAtTimestamp </strong>function does the heavy lifting. This time, we also apply it to the geometry time series column called <strong>trip</strong>: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
SELECT mmsi,
    valueAtTimestamp(trip, '2017-05-07 08:55:40') geom,
    valueAtTimestamp(SOG, '2017-05-07 08:55:40') SOG
FROM "public"."ships"
</pre></div>


<p>Using this SQL query, we again set up a — not yet Temporal Controller-controlled — QueryLayer. </p>



<p>To configure Temporal Controller to update the timestamp in our SQL query, we again need to run the Python script from <a href="https://anitagraser.com/2022/10/01/visualizing-iot-time-series-with-qgis-mobilitydb/">the previous post</a>. </p>



<p>With this done, we are all set up to animate and explore the movement patterns in our dataset: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2022/11/mobilitydb-qgis-temporalcontroller1.gif"><img data-attachment-id="8289" data-permalink="https://anitagraser.com/2022/11/19/visualizing-trajectories-with-qgis-mobilitydb/mobilitydb-qgis-temporalcontroller1/" data-orig-file="https://underdark.files.wordpress.com/2022/11/mobilitydb-qgis-temporalcontroller1.gif" data-orig-size="1213,713" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="mobilitydb-qgis-temporalcontroller1" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2022/11/mobilitydb-qgis-temporalcontroller1.gif?w=300" data-large-file="https://underdark.files.wordpress.com/2022/11/mobilitydb-qgis-temporalcontroller1.gif?w=545" src="https://underdark.files.wordpress.com/2022/11/mobilitydb-qgis-temporalcontroller1.gif?w=1024" alt="" class="wp-image-8289" /></a></figure>



<hr class="wp-block-separator has-alpha-channel-opacity" />



<p>This post is part of a series. Read more about&nbsp;<a href="https://anitagraser.com/movement-data-in-gis/">movement data in GIS.</a></p>
