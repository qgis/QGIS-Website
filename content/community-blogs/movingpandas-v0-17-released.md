---
source: "blog"
title: "anitagraser.com: MovingPandas v0.17 released!"
image: "movingpandas-v0-17-released."
date: "2023-11-15"
link: "https://anitagraser.com/2023/11/15/movingpandas-v0-17-released/"
draft: "true"
showcase: "planet"
---

<div class="wp-block-image">
<figure class="alignright"><img loading="lazy" width="150" height="100" data-attachment-id="7259" data-permalink="https://anitagraser.com/movingpandas/logo/" data-orig-file="https://underdark.files.wordpress.com/2020/06/logo.png" data-orig-size="1881,1256" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="logo" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2020/06/logo.png?w=300" data-large-file="https://underdark.files.wordpress.com/2020/06/logo.png?w=545" src="https://underdark.files.wordpress.com/2020/06/logo.png?w=150" alt="" class="wp-image-7259" srcset="https://underdark.files.wordpress.com/2020/06/logo.png?w=150 150w, https://underdark.files.wordpress.com/2020/06/logo.png?w=300 300w" sizes="(max-width: 150px) 100vw, 150px" /></figure></div>


<p>Over the last couple of months, I have not been posting release announcements here, so there is quite a bit to catch up. </p>



<p>The latest <a href="https://github.com/movingpandas/movingpandas/releases">v0.17.2</a> release is now available from <a href="https://anaconda.org/conda-forge/movingpandas">conda-forge</a>.</p>



<p>New features (since 0.14):</p>



<ul>
<li>Improved MovingFeatures MF-JSON support
<ul>
<li>Ability to parse a MovingFeatureCollection from a json file&nbsp;<a href="https://github.com/movingpandas/movingpandas/pull/330">#330</a></li>



<li>GeoDataFrame to MF-JSON <a href="https://github.com/movingpandas/movingpandas/pull/325">#325</a></li>



<li>Adding read_mf_dict function&nbsp;<a href="https://github.com/movingpandas/movingpandas/pull/357">#357</a></li>
</ul>
</li>



<li>New OutlierCleaner&nbsp;<a href="https://github.com/movingpandas/movingpandas/pull/334">#334</a></li>



<li>Faster stop detection&nbsp;<a href="https://github.com/movingpandas/movingpandas/pull/316">#316</a></li>



<li>New arrow markers to indicate trajectory direction in plots <a href="https://github.com/movingpandas/movingpandas/commit/fb1174b51f0ef31ce95ffc1403b78c7eff3642b7">fb1174b</a>&nbsp;</li>



<li>Distance, speed, and acceleration unit handling <a href="https://github.com/movingpandas/movingpandas/pull/295">#295</a></li>



<li>New aggregation parameter (agg) for to_traj_gdf() <a href="https://github.com/movingpandas/movingpandas/commit/574506837f5e04f6e49ff1cd99da28bc54fc30ba">5745068</a>&nbsp;</li>



<li>New get_segments_between() for TrajectoryCollection <a href="https://github.com/movingpandas/movingpandas/issues/287">#287</a> </li>
</ul>



<p>Behind the scenes:</p>



<ul>
<li>We now have a dedicated Github organization: <a href="https://github.com/movingpandas">https://github.com/movingpandas</a> that houses all related repositories</li>



<li>And we finally added https support to the website</li>
</ul>



<p>As always, all tutorials are available from the <a href="https://github.com/movingpandas/movingpandas-examples">movingpandas-examples</a> repository and on MyBinder:</p>


<div class="wp-block-image">
<figure class="aligncenter"><a href="https://mybinder.org/v2/gh/movingpandas/movingpandas-examples/main"><img loading="lazy" width="545" height="100" data-attachment-id="7159" data-permalink="https://anitagraser.com/2020/03/21/movingpandas-v0-3-released/binder/" data-orig-file="https://underdark.files.wordpress.com/2020/03/binder.png" data-orig-size="109,20" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="binder" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2020/03/binder.png?w=109" data-large-file="https://underdark.files.wordpress.com/2020/03/binder.png?w=109" src="https://underdark.files.wordpress.com/2020/03/binder.png?w=545" alt="" class="wp-image-7159" /></a></figure></div>


<p>If you have questions about using MovingPandas or just want to discuss new ideas, you&#8217;re welcome to join our <a href="https://github.com/movingpandas/movingpandas/discussions"><strong>discussion forum</strong></a>.</p>



<p></p>
