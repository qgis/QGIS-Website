---
source: "blog"
title: "OPENGIS.ch blog: QGIS Swiss Locator 3.0 brings elevation profiles and vector tiles"
image: "swiss-locator-plugin-3-0-is-here-with-exciting-features."
date: "2024-06-25"
link: "https://www.opengis.ch/2024/06/25/swiss-locator-plugin-3-0-is-here-with-exciting-features/"
draft: "true"
showcase: "planet"
---

<h2 class="wp-block-heading">Swiss elevation profiles</h2>



<p>Get high-precision elevation profiles in QGIS right from Swisstopo&#8217;s official <a href="https://api3.geo.admin.ch/services/sdiservices.html#profile" rel="noreferrer noopener" target="_blank">profile service</a>, based on <a href="https://www.swisstopo.admin.ch/en/height-model-swissalti3d" rel="noreferrer noopener" target="_blank">swissALTI3D</a> data!</p>



<figure class="wp-block-video wp-block-embed is-type-video is-provider-videopress"><div class="wp-block-embed__wrapper">

</div><figcaption>Swiss elevation profiles are available with QGIS 3.38.</figcaption></figure>



<p>Thanks to this integration, you can take advantage of existing QGIS features, such as exporting 2d/3d features or distance/elevation tables, as well as displaying profiles directly in QGIS layouts.</p>



<p><strong>Tip</strong>: Swiss elevation profiles will be available as long as the Swiss Locator plugin is installed and active. Should you need to turn Swiss elevation profiles off to create other profiles with your own data, go to the Plugin manager and deactivate the plugin in the meantime.</p>



<h4 class="wp-block-heading">For developers</h4>



<p>We&#8217;re paving the way for adding custom elevation profiles to QGIS. For that, we&#8217;ve added a <a href="https://api.qgis.org/api/classQgsProfileSourceRegistry.html" rel="noreferrer noopener" target="_blank">QGIS profile source registry</a> so that plugin developers can register their own profile sources (e.g., based on profile web services, just like we did here) and make them available for QGIS end users. The registry is available from QGIS 3.38. It&#8217;s your turn! <img alt="👩‍💻" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f469-200d-1f4bb.png" style="height: 1em;" /></p>



<h2 class="wp-block-heading">Swiss vector tiles base maps</h2>



<p>Loading Swiss vector tiles is now easier than ever. Just go to the locator bar, type the prefix &#8220;<kbd>chb</kbd>&#8221; (add a white space after that) and you&#8217;ll get a list of available and already styled Swiss vector tiles layers. Some of them will even load grouped auxiliary imagery for reference.</p>



<p>Vector tiles will be loaded at the bottom of the QGIS layer tree as base maps, so you will see all your data on top of them.</p>



<p>Vector tiles are optimized for local caching and scale-independent rendering. This also makes it a perfect fit for adding it to your <a href="https://qfield.org/">QField</a> project.</p>



<p>There are a couple of different vector tile sets available</p>



<h4 class="wp-block-heading">leichte-basiskarte</h4>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14627" height="466" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/vt_leichte_basiskarte.png?resize=750%2C466&#038;ssl=1" width="750" /></figure>



<h4 class="wp-block-heading">Light base map</h4>



<p>Similar to the <em>leichte-basiskarte</em> layer, but using an older version of the data source and adjusted styles.</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14625" height="466" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/vt_lightbasemap.png?resize=750%2C466&#038;ssl=1" width="750" /></figure>



<h4 class="wp-block-heading">leichte-basiskarte-imagery (with WMTS sublayer)</h4>



<p>This layer is similar to the Imagery base map layer, but it uses a more recent version of the data source and adjusted styles.</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14628" height="466" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/vt_leichte_basiskarte_imagery.png?resize=750%2C466&#038;ssl=1" width="750" /></figure>



<h4 class="wp-block-heading">Base map</h4>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14624" height="466" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/vt_basemap.png?resize=750%2C466&#038;ssl=1" width="750" /></figure>



<h4 class="wp-block-heading">Imagery base map (with WMTS sublayer)</h4>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14626" height="466" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/vt_imagery_basemap.png?resize=750%2C466&#038;ssl=1" width="750" /></figure>



<p>See the <a href="https://www.geo.admin.ch/en/vector-tiles-service-available-services-and-data" rel="noreferrer noopener" target="_blank">official services documentation</a> for details on data sources and styles.</p>



<h2 class="wp-block-heading">Fixes</h2>



<p>Thanks to your feedback, we&#8217;ve also fixed some issues. Don&#8217;t hesitate to reach out to us at <a href="https://github.com/opengisch/qgis-swiss-locator/" rel="noreferrer noopener" target="_blank">GitHub</a> if you&#8217;d like to suggest or report something related to the Swiss Locator plugin.</p>



<p>Happy (and now more powerful) mapping! <img alt="🗺" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f5fa.png" style="height: 1em;" /><img alt="🚀" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f680.png" style="height: 1em;" /></p>
