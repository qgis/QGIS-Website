---
source: "blog"
title: "QGIS Oslandia: New release for QField : 3.4 &#8220;Ebo&#8221;"
image: "sortie-de-qfield-3-4-ebo."
date: "2024-10-08"
link: "https://oslandia.com/en/2024/10/09/sortie-de-qfield-3-4-ebo/"
draft: "true"
showcase: "planet"
---

<p>Oslandia is the main partner of <a href="https://opengis.ch">OPENGIS.ch</a> around <a href="https://qfield.org">QField</a>. We are proud today to forward the announcement of the new QField release 3.4 &#8220;Ebo&#8221;.</p>
<h2 class="wp-block-heading">Main highlights</h2>
<figure class="wp-block-image size-large"><img alt="" class="wp-image-15064 aligncenter" height="335" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/34.png?resize=750%2C458&amp;ssl=1" tabindex="0" width="549" /></figure>
<p>A new <strong>geofencing framework</strong> has landed, enabling users to configure QField behaviors in relation to geofenced areas and user positioning. Geofenced areas are defined at the project-level and shaped by polygons from a chosen vector layer. The three available geofencing behaviours in this new release are:</p>
<ul class="wp-block-list">
<li>Alert user when <em>inside</em> an area polygon;</li>
<li>Alert user when <em>outside</em> all defined area polygons and</li>
<li>Inform the user when entering and leaving an area polygons.</li>
</ul>
<p>In addition to being alerted or informed, users can also prevent digitizing of features when being alerted by the first or second behaviour. The configuration of this functionality is done in QGIS using QFieldSync.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-15065 aligncenter" height="372" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/geofencing_settings.png?resize=750%2C497&amp;ssl=1" tabindex="0" width="561" /></figure>
<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow"><p><em><span style="margin: 0px; padding: 0px;">Pro tip: geofencing settings are embedded within projects, which means it is easy to deploy these constraints to a team of field workers through <a href="https://qfield.cloud/" rel="noopener" target="_blank">QFieldCloud</a>. Thanks <a href="https://www.terrexseismic.com/" rel="noopener" target="_blank">Terrex Seismic</a> for sponsoring</span> this functionality.</em></p></blockquote>
<p>QField now offers users access to a brand new <strong>processing toolbox containing over a dozen algorithms </strong><span style="margin: 0px; padding: 0px;"><strong>for manipulating digitized geometries</strong> directly </span>in the field. As with many parts of QField, this feature relies on QGIS’ core library, namely its processing framework and the numerous, well-maintained algorithms it comes with.</p>
<p>The algorithms exposed in QField unlock many useful functionalities for refining geometries, including orthogonalization, smoothing, buffering, rotation, affine transformation, etc. As users configure algorithms’ parameters, a grey preview of the output will be visible as an overlay on top of the map canvas.</p>
<figure class="wp-block-image size-full"><img alt="" class="wp-image-15066 aligncenter" height="386" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/10/ortho_alg.png?resize=750%2C386&amp;ssl=1" tabindex="0" width="750" /></figure>
<p>To reach the processing toolbox in QField, select one or more features by long-pressing on them in the features list, open the 3-dot menu and click on the process selected feature(s) action. Are you excited about this one? Send your thanks to the <a href="https://www.maanmittauslaitos.fi/">National Land Survey of Finland</a>, who’s support made this a reality.</p>
<p>QField’s camera has gained support for <strong>customized ratio and resolution of photos</strong>, as well as the <strong>ability to stamp details – date and time as well as location details – onto captured photos</strong>. In fact, QField’s own camera has received so much attention in the last few releases that it was decided to make it the default one. On supported platforms, users can switch to their OS camera by disabling the native camera option found at the bottom of the QField settings’ general tab.</p>
<h2 class="wp-block-heading">Wait, there’s more</h2>
<p>There are plenty more improvements packed into this release from <strong>project variables editing using a revamped variables editor</strong> through to <strong>integration of QField documentation help in the search bar</strong> and the <strong>ability to search cloud project lists</strong>. Read the <a href="https://github.com/opengisch/QField/releases/tag/v3.4.0">full 3.4 changelog</a> to know more, and enjoy the release!</p>
<p>&nbsp;</p>
<h2>Contact us !</h2>
<p>A question concerning QField ? Interested in QField deployment ? Do not hesitate to <a href="mailto://infos+qfield@oslandia.com">contact Oslandia to discuss your project</a> !</p>
<p>&nbsp;</p>
