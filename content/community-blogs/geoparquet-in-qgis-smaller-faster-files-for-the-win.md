---
source: "blog"
title: "anitagraser.com: GeoParquet in QGIS – smaller & faster files for the win!"
image: "geoparquet-in-qgis-smaller-faster-files-for-the-win."
date: "2024-11-23"
link: "https://anitagraser.com/2024/11/23/geoparquet-in-qgis-smaller-faster-files-for-the-win/"
draft: "true"
showcase: "planet"
---

<p>tldr; Tired of working with large CSV files? Give GeoParquet a try!</p>



<p><em>&#8220;Parquet is a powerful column-oriented data format, built from the ground up to as a modern alternative to CSV files.&#8221;</em> <a href="https://geoparquet.org/">https://geoparquet.org/</a></p>



<p>(Geo)Parquet is both smaller and faster than CSV. Additionally, (Geo)Parquet columns are typed. Text, numeric values, dates, geometries retain their data types. GeoParquet also stores CRS information and support in GIS solutions is growing.</p>



<p>I&#8217;ll be giving a quick overview using AIS data in <a href="https://geopandas.org/en/stable/docs/reference/api/geopandas.read_parquet.html">GeoPandas</a> 1.0.1 (with pyarrow) and QGIS 3.38 (with <a href="https://gdal.org/en/latest/drivers/vector/parquet.html#vector-parquet">GDAL</a> 3.9.2). </p>



<h2 class="wp-block-heading">File size</h2>



<p>The example AIS dataset for this demo contains ~10 million rows with 22 columns. I&#8217;ve converted the original zipped CSV into GeoPackage and GeoParquet using GeoPandas to illustrate the huge difference in file size: ~470 MB for GeoParquet and zipped CSV, 1.6 GB for CSV, and a whopping 2.6 GB for GeoPackage: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-9291" height="95" src="https://anitagraser.com/wp-content/uploads/2024/11/image-1.png?w=397" width="397" /></figure>



<h2 class="wp-block-heading">Reading performance</h2>



<p>Pandas and GeoPandas both support selective reading of files, i.e. we can specify the specific columns to be loaded. This does speed up reading, even from CSV files: </p>



<figure class="wp-block-table"><table class="has-fixed-layout"><tbody><tr><td></td><td class="has-text-align-right"><strong>Whole file</strong></td><td class="has-text-align-right"><strong>Selected columns</strong></td></tr><tr><td><strong>CSV</strong></td><td class="has-text-align-right">27.9 s</td><td class="has-text-align-right">13.1 s</td></tr><tr><td><strong>Geopackage</strong></td><td class="has-text-align-right">2min 12s <img alt="😵" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f635.png" style="height: 1em;" /></td><td class="has-text-align-right">20.2 s</td></tr><tr><td><strong>GeoParquet</strong></td><td class="has-text-align-right">7.2 s</td><td class="has-text-align-right">4.1 s</td></tr></tbody></table></figure>



<p>Indeed, reading the whole GeoPackage is getting quite painful. </p>



<p>Here&#8217;s the code I used for timing the read times: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/11/image-2.png"><img alt="" class="wp-image-9296" height="482" src="https://anitagraser.com/wp-content/uploads/2024/11/image-2.png?w=770" width="770" /></a></figure>



<p>As you can see, these times include the creation of the GeoPandas.GeoDataFrame. </p>



<p>If we don&#8217;t need a GeoDataFrame, we can read the files even faster: </p>



<h3 class="wp-block-heading">Non-spatial DataFrames</h3>



<p>GeoParquet files can be read by non-GIS tools, such as Pandas. This makes it easier to collaborate with people who may not be familiar with geospatial data stacks. </p>



<p>And reading plain DataFrames is much faster than creating GeoDataFrames: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/11/image-3.png"><img alt="" class="wp-image-9298" height="520" src="https://anitagraser.com/wp-content/uploads/2024/11/image-3.png?w=743" width="743" /></a></figure>



<p>But back to GIS &#8230; </p>



<h2 class="wp-block-heading">GeoParquet in QGIS</h2>



<p>In QGIS, GeoParquet files can be loaded like any other vector layer, thanks to GDAL:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/11/image-4.png"><img alt="" class="wp-image-9301" height="418" src="https://anitagraser.com/wp-content/uploads/2024/11/image-4.png?w=682" width="682" /></a></figure>



<p>Loading the GeoParquet and GeoPackage files is pretty quick, especially if we zoom into a small region of interest (even though, unfortunately, it doesn&#8217;t seem possible to restrict the columns to further speed up loading). Loading the CSV, however, is pretty painful due to the lack of spatial indexing, which becomes apparent very quickly in the direct comparison: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/11/geoparquet.gif"><img alt="" class="wp-image-9305" height="540" src="https://anitagraser.com/wp-content/uploads/2024/11/geoparquet.gif?w=960" width="960" /></a><figcaption class="wp-element-caption">(You can see how slowly the red CSV points are rendering. I didn&#8217;t have the patience to include the whole process in the GIF.)</figcaption></figure>



<p>As far as I can tell, my QGIS 3.38 &#8216;Grenoble&#8217; does not support writing to or editing of GeoParquet files. So I&#8217;m limited to reading GeoParquet for now. </p>



<p>However, seeing how much smaller GeoParquets are compared to GeoPackages (and also faster to write), I hope that we will soon get the option to export to GeoParquet. </p>



<p>For now, I&#8217;ll start by converting my large CSV files to GeoParquet using GeoPandas. </p>



<p>If you want to see an even larger example, have a look at Matt Travis&#8217; presentation using Overture data: </p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<div class="embed-youtube"></div>
</div></figure>
