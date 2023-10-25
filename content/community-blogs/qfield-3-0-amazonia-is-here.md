---
source: "blog"
title: "OPENGIS.ch blog: QField 3.0 “Amazonia” is here – Feature-packed and super slick."
image: "qfield-3-0-amazonia-is-here."
date: "2023-10-24"
link: "https://www.opengis.ch/2023/10/24/qfield-3-0-amazonia-is-here/"
draft: "true"
showcase: "planet"
---

<p>We’re so excited and proud of this latest QField version that we’ve opted for a major 3.0 version update. </p>



<div class="wp-block-buttons is-content-justification-center is-layout-flex wp-container-1 wp-block-buttons-is-layout-flex">
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="https://qfield.app">Get it now</a></div>
</div>



<p>Shipped with many new features and built with the latest generation of Qt’s cross-platform framework, this new chapter marks an important milestone for the most powerful open-source field GIS solution.</p>



<figure class="wp-block-image"><img decoding="async" src="https://lh5.googleusercontent.com/tN3P-TFu7O2_hcEwShJYmQeneSN9oddAMQ64xkdoSr5Yn9MVZ-v9iBCkRo-3Sb7Ya1AGZSKID-_mG1PbR3sFma6ST66Zi0bqmm9-xqMnIZx_C5vNWz-3wp7TwoQADLWhtpT0KF5ghZz33hP23xKcap4" alt=""/></figure>



<h2 class="wp-block-heading">Main highlights</h2>



<p>Upon launching this new version of QField, users will be greeted by a revamped recent projects list featuring shiny map canvas thumbnails. While this is one of the most obvious UI improvements, countless interface tweaks and harmonization have occurred. From the refreshed dark theme to the further polishing of countless widgets, QField has never looked and felt better.</p>



<p>The top search bar has a new functionality that allows users to look for features within the currently active vector layer by matching any of its attributes against a given search term. Users can also refine their searches by specifying a specific attribute. The new functionality can be triggered by typing the ‘f’ prefix in the search bar followed by a string or number to retrieve a list of matching features. When expanding it, a new list of functionalities appears to help users discover all of the tools available within the search bar.</p>



<p>QField’s tracking has also received some love. A <strong>new erroneous distance safeguard</strong> setting has been added, which, when enabled, will dictate the tracker not to add a new vertex if the distance between it and the previously added vertex is greater than a user-specified value. This aims at preventing “spikes” of poor position readings during a tracking session. QField is now also capable of resuming a tracking session after being stopped. When resuming, tracking will reuse the last feature used when first starting, allowing sessions interrupted by battery loss or momentary pause to be continued on a single line or polygon geometry.&nbsp;&nbsp;</p>





<p>On the feature form front, QField has gained <strong>support for feature form text widgets, </strong>a new read-only type introduced in QGIS 3.30<strong>,</strong> which allows users to create expression-based text labels within complex feature form configurations. In addition, <strong>relationship-related form widgets now allow for zooming to children/parent</strong> features within the form itself.</p>



<p>To enhance digitizing work in the field, QField now makes it <strong>possible to turn snapping on and off</strong> through a new snapping button on top of the map canvas when in digitizing mode. When a project has enabled advanced snapping, the dashboard’s legend item now showcases snapping badges, allowing users to <strong>toggle snapping for individual vector layers</strong>.&nbsp;</p>





<p>In addition, digitising lines and polygons by using the volume up/down hardware keys on devices such as smartphones is now possible. This can come in handy when digitizing data in harsh conditions where gloves can make it harder to use a touch screen.&nbsp;</p>



<p>While we had to play favourites in describing some of the new functionalities in QField, we’ve barely touched the surface of this feature-packed release. Other major additions include support for <strong>Near-Field Communication (NFC) text tag reading</strong> and a new geometry editor’s eraser tool to delete part of lines and polygons as you would with a pencil sketch using an eraser.</p>



<p>Thanks to <a href="https://www.dainst.org/dai/meldungen">Deutsches Archäologisches Institut</a>, <a href="https://groupementsforestiers.quebec/">Groupements forestiers Québec</a>, <a href="https://www.amsa.it/cittadini">Amsa</a>, and <a href="https://www.luzern.ch/">Kanton Luzern</a> for sponsoring these enhancements.&nbsp;</p>



<h2 class="wp-block-heading">Quality of life improvements</h2>



<p>Starting with this new version, the scale bar overlay will now respect projects’ distance measurement units, allowing for <strong>scale bars in imperial and nautical units</strong>.</p>



<p>QField now offers a <strong>rendering quality setting which, at the cost of a slightly reduced visual quality, results in faster rendering speeds and lower memory usage</strong>. This can be a lifesaver for older devices having difficulty handling large projects and helps save battery life.</p>



<p>Vector tile layer support has been improved with the automated download of missing fonts and the possibility of toggling label visibility. This pair of changes makes this resolution-independent layer type much more appealing.</p>



<p><strong>On iOS, layouts are now printed by QField as PDF documents</strong> instead of images. While this was the case for other platforms, it only became possible on iOS recently after work done by one of our ninjas in QGIS itself.</p>



<p>Many thanks to <a href="https://fahrweg.dbnetze.com/fahrweg-de">DB Fahrwgdienste</a> for sponsoring stabilization efforts and fixes during this development cycle.</p>



<h2 class="wp-block-heading">Qt 6, the latest generation of the cross-platform framework powering QField</h2>



<p>Last but not least, QField 3.0 is now built against Qt 6. This is a significant technological milestone for the project as this means we can fully leverage the latest technological innovations into this cross-platform framework that has been powering QField since day one.</p>



<p>On top of the new possibilities, QField benefited from years of fixes and improvements, including better integration with Android and iOS platforms. In addition, the positioning framework in Qt 6 has been improved with awareness of the newer GNSS constellations that have emerged over the last decade.</p>



<h2 class="wp-block-heading">Forest-themed release names</h2>



<figure class="wp-block-image size-large"><img data-attachment-id="13962" data-permalink="https://www.opengis.ch/2023/10/24/qfield-3-0-amazonia-is-here/qfield3/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?fit=1676%2C1116&amp;ssl=1" data-orig-size="1676,1116" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="qfield3" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?fit=300%2C200&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?fit=750%2C500&amp;ssl=1" decoding="async" fetchpriority="high" width="750" height="500" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=750%2C500&#038;ssl=1" alt="" class="wp-image-13962" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=1024%2C682&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=300%2C200&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=768%2C511&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=1536%2C1023&amp;ssl=1 1536w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=360%2C240&amp;ssl=1 360w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?w=1676&amp;ssl=1 1676w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>Forests are critical in climate regulation, biodiversity preservation, and economic sustainability. Beginning with QField 3.0 “Amazonia” and throughout the 3.X’s life cycle, we will choose forest names to underscore the importance of and advocate for global forest conservation.&nbsp;</p>



<p>As always, we hope you enjoy this new release. Happy field mapping!</p>
