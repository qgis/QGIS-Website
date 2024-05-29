---
source: "blog"
title: "anitagraser.com: New Trajectools 2.1 and MovingPandas 0.18 releases"
image: "new-trajectools-2-1-and-movingpandas-0-18-releases."
date: "2024-05-20"
link: "https://anitagraser.com/2024/05/20/new-trajectools-2-1-and-movingpandas-0-18-releases/"
draft: "true"
showcase: "planet"
---

<p>Today marks the 2.1 release of <a href="https://plugins.qgis.org/plugins/processing_trajectory/version/2.1/">Trajectools for QGIS</a>. This release adds multiple new algorithms and improvements. Since some improvements involve upstream <a href="https://github.com/movingpandas/movingpandas/releases">MovingPandas</a> functionality, I recommend to also update MovingPandas while you&#8217;re at it.</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8950" height="131" src="https://anitagraser.com/wp-content/uploads/2024/05/trajectools-6.png?w=545" width="545" /></figure>



<p>If you have installed QGIS and MovingPandas via conda / mamba, you can simply: </p>



<pre class="wp-block-code"><code>conda activate qgis
mamba install movingpandas=0.18</code></pre>



<p>Afterwards, you can check that the library was correctly installed using:</p>



<pre class="wp-block-code"><code>import movingpandas as mpd<br />mpd.show_versions()</code></pre>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8976" height="203" src="https://anitagraser.com/wp-content/uploads/2024/05/image-14.png?w=382" width="382" /></figure>



<h2 class="wp-block-heading">Trajectools 2.1</h2>



<p>The new Trajectools algorithms are: </p>



<ul class="wp-block-list">
<li>Trajectory overlay &#8212; Intersect trajectories with polygon layer</li>



<li>Privacy &#8212; Home work attack (requires scikit-mobility)
<ul class="wp-block-list">
<li>This algorithm determines how easy it is to identify an individual in a dataset. In a home and work attack the adversary knows the coordinates of the two locations most frequently visited by an individual. </li>
</ul>
</li>



<li>GTFS &#8212; Extract segments (requires gtfs_functions) </li>



<li>GTFS &#8212; Extract shapes (requires gtfs_functions)
<ul class="wp-block-list">
<li>These algorithms extract <a href="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/">public transport routes (GTFS shapes) and route segments </a>between stops (GTFS segments) from GTFS ZIP files using gtfs_functions.Feed.shapes and .segments, respectively. </li>
</ul>
</li>
</ul>



<p>Furthermore, we have fixed issue with previously ignored minimum trajectory length settings. </p>



<div class="wp-block-group"><div class="wp-block-group__inner-container is-layout-constrained wp-block-group-is-layout-constrained">
<div class="wp-block-columns is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex">
<div class="wp-block-column is-layout-flow wp-block-column-is-layout-flow">
<div class="wp-block-jetpack-tiled-gallery aligncenter is-style-rectangular"><div class=""><div class="tiled-gallery__gallery"><div class="tiled-gallery__row"><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="https://anitagraser.com/wp-content/uploads/2024/05/image-8.png" /></figure></div><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="https://anitagraser.com/wp-content/uploads/2024/05/image-6.png" /></figure></div></div></div></div></div>
</div>
</div>
</div></div>



<p>Scikit-mobility and gtfs_functions are optional dependencies. You do not need to install them, if you do not want to use the corresponding algorithms. In any case, they can be installed using mamba and pip: </p>



<pre class="wp-block-code"><code>mamba install scikit-mobility
pip install gtfs_functions</code></pre>



<h2 class="wp-block-heading">MovingPandas 0.18</h2>



<p>This release adds multiple new features, including </p>



<ul class="wp-block-list">
<li>Method chaining support for add_speed(), add_direction(), and other functions</li>



<li>New TrajectoryCollection.get_trajectories(obj_id) function</li>



<li>New trajectory splitter based on heading angle </li>



<li>New TrajectoryCollection.intersection(feature)  function</li>



<li>New plotting function hvplot_pts() </li>



<li>Faster TrajectoryCollection operations through multi-threading</li>



<li>Added moving object weights support to trajectory aggregator </li>
</ul>



<div class="wp-block-jetpack-tiled-gallery aligncenter is-style-rectangular"><div class=""><div class="tiled-gallery__gallery"><div class="tiled-gallery__row"><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="https://anitagraser.com/wp-content/uploads/2024/05/image-13.png" /></figure></div><div class="tiled-gallery__col"><figure class="tiled-gallery__item"><img alt="" src="https://anitagraser.com/wp-content/uploads/2024/05/329805211-ad1a0822-e95b-43ee-96ed-4bd029bf26ce.png" /></figure></div></div></div></div></div>



<p>For the <a href="https://github.com/movingpandas/movingpandas/releases/tag/v0.18">full change log, check out the release page</a>.</p>



<p></p>
