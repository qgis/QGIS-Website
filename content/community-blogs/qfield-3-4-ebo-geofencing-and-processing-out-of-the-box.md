---
source: "blog"
title: "OPENGIS.ch blog: QField 3.4 “Ebo”: Geofencing and processing out of the box"
image: "qfield-3-4-ebo-geofencing-and-processing-out-of-the-box."
date: "2024-10-04"
link: "https://www.opengis.ch/2024/10/08/qfield-3-4-ebo-geofencing-and-processing-out-of-the-box/"
draft: "true"
showcase: "planet"
---

<p>QField 3.4 is out, and it won’t disappoint. It has tons of new features that continue to push the limits of what users can do in the field.</p>



<h2 class="wp-block-heading">Main highlights</h2>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-15064" height="458" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/34.png?resize=750%2C458&#038;ssl=1" width="750" /></figure>



<p><br />A new <strong>geofencing framework</strong> has landed, enabling users to configure QField behaviors in relation to geofenced areas and user positioning. Geofenced areas are defined at the project-level and shaped by polygons from a chosen vector layer. The three available geofencing behaviours in this new release are:</p>



<ul class="wp-block-list">
<li>Alert user when <em>inside</em> an area polygon;</li>



<li>Alert user when <em>outside</em> all defined area polygons and</li>



<li>Inform the user when entering and leaving an area polygons.</li>
</ul>



<p>In addition to being alerted or informed, users can also prevent digitizing of features when being alerted by the first or second behaviour. The configuration of this functionality is done in QGIS using QFieldSync.</p>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-15065" height="497" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/geofencing_settings.png?resize=750%2C497&#038;ssl=1" width="750" /></figure>



<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p><span style="margin: 0px; padding: 0px;">Pro tip: geofencing settings are embedded within projects, which means it is easy to deploy these constraints to a team of field workers through <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>. Thanks <a href="https://www.terrexseismic.com/" rel="noopener" target="_blank">Terrex Seismic</a> for sponsoring</span> this functionality.</p>
</blockquote>



<p>QField now offers users access to a brand new <strong>processing toolbox containing over a dozen algorithms </strong><span style="margin: 0px; padding: 0px;"><strong>for manipulating digitized geometries</strong> directly </span>in the field. As with many parts of QField, this feature relies on QGIS’ core library, namely its processing framework and the numerous, well-maintained algorithms it comes with.</p>



<p>The algorithms exposed in QField unlock many useful functionalities for refining geometries, including orthogonalization, smoothing, buffering, rotation, affine transformation, etc. As users configure algorithms’ parameters, a grey preview of the output will be visible as an overlay on top of the map canvas.</p>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-15066" height="386" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/ortho_alg.png?resize=750%2C386&#038;ssl=1" width="750" /></figure>



<p>To reach the processing toolbox in QField, select one or more features by long-pressing on them in the features list, open the 3-dot menu and click on the process selected feature(s) action. Are you excited about this one? Send your thanks to the <a href="https://www.maanmittauslaitos.fi/">National Land Survey of Finland</a>, who’s support made this a reality.</p>



<p>QField’s camera has gained support for <strong>customized ratio and resolution of photos</strong>, as well as the <strong>ability to stamp details – date and time as well as location details &#8211; onto captured photos</strong>. In fact, QField’s own camera has received so much attention in the last few releases that we have decided to make it the default one. On supported platforms, users can switch to their OS camera by disabling the native camera option found at the bottom of the QField settings’ general tab.</p>



<h2 class="wp-block-heading">Wait, there&#8217;s more</h2>



<p>There are plenty more improvements packed into this release from <strong>project variables editing using a revamped variables editor</strong> through to <strong>integration of QField documentation help in the search bar</strong> and the <strong>ability to search cloud project lists</strong>. Read the <a href="https://github.com/opengisch/QField/releases/tag/v3.4.0">full 3.4 changelog</a> to know more, and enjoy the release!</p>
