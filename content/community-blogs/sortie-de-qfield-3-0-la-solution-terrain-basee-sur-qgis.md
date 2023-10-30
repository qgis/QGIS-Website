---
source: "blog"
title: "QGIS Oslandia: QField 3.0 release : field mapping app, based on QGIS"
image: "sortie-de-qfield-3-0-la-solution-terrain-basee-sur-qgis."
date: "2023-10-30"
link: "https://oslandia.com/en/2023/10/30/sortie-de-qfield-3-0-la-solution-terrain-basee-sur-qgis/"
draft: "true"
showcase: "planet"
---

<p>We are very happy and enthusiasts at Oslandia to forward the <a href="https://www.opengis.ch/fr/2023/10/24/qfield-3-0-amazonia-is-here/">QField 3.0 release announcement</a>, the new major update of this mobile GIS application based on QGIS.</p>
<p>Oslandia is a <a href="https://oslandia.com/2023/09/14/oslandia-signe-un-partenariat-avec-opengis-ch-sur-qfield/">strategic partner of OPENGIS.ch</a>, the company at the heart of QField development, as well as the QFieldCloud associated SaaS offering. We join <a href="https://www.opengis.ch">OPENGIS.ch</a> to announce all the new features of QField 3.0.</p>
<p style="text-align: center;"><a href="https://qfield.app/">Get QField 3.0 now !</a></p>
<p style="text-align: center;"><a href="https://qfield.app/"><img class="aligncenter " src="https://lh5.googleusercontent.com/tN3P-TFu7O2_hcEwShJYmQeneSN9oddAMQ64xkdoSr5Yn9MVZ-v9iBCkRo-3Sb7Ya1AGZSKID-_mG1PbR3sFma6ST66Zi0bqmm9-xqMnIZx_C5vNWz-3wp7TwoQADLWhtpT0KF5ghZz33hP23xKcap4" alt="QField 3.0 screenshots" width="611" height="383" /></a></p>
<hr />
<p>&nbsp;</p>
<p>Shipped with <strong>many new features</strong> and built with the <strong>latest generation of Qt’s cross-platform framework</strong>, this new chapter marks an important milestone for the most powerful open-source field GIS solution.</p>
<h2>Main highlights</h2>
<p>Upon launching this new version of QField, users will be greeted by a<strong> revamped recent projects</strong> list featuring shiny map canvas thumbnails. While this is one of the most obvious UI improvements, countless <strong>interface tweaks and harmonization</strong> have occurred. From the refreshed dark theme to the further polishing of countless widgets, QField has never looked and felt better.</p>
<p>The<strong> top search bar</strong> has a new functionality that allows users to look for features within the currently active vector layer by matching any of its attributes against a given search term. Users can also refine their searches by specifying a specific attribute. The new functionality can be triggered by typing the ‘f’ prefix in the search bar followed by a string or number to retrieve a list of matching features. When expanding it, a new list of functionalities appears to help users discover all of the tools available within the search bar.</p>
<p><strong>QField’s tracking has also received some love</strong>. A new erroneous distance safeguard setting has been added, which, when enabled, will dictate the tracker not to add a new vertex if the distance between it and the previously added vertex is greater than a user-specified value. This aims at preventing “spikes” of poor position readings during a tracking session. QField is now also capable of resuming a tracking session after being stopped. When resuming, tracking will reuse the last feature used when first starting, allowing sessions interrupted by battery loss or momentary pause to be continued on a single line or polygon geometry.</p>
<p style="text-align: center;"><iframe src="https://videopress.com/embed/2LMsUg9l" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe><script src="https://videopress.com/videopress-iframe.js"></script></p>
<p>On the <strong>feature form</strong> front, QField has gained support for feature form text widgets, a new read-only type introduced in QGIS 3.30, which allows users to create expression-based text labels within complex feature form configurations. In addition, relationship-related form widgets now allow for zooming to children/parent features within the form itself.</p>
<p>To enhance<strong> digitizing work in the field</strong>, QField now makes it possible to turn snapping on and off through a new snapping button on top of the map canvas when in digitizing mode. When a project has enabled advanced snapping, the dashboard’s legend item now showcases snapping badges, allowing users to toggle snapping for individual vector layers.</p>
<p>In addition, digitizing lines and polygons by using the volume up/down hardware keys on devices such as smartphones is now possible. This can come in handy when digitizing data in harsh conditions where gloves can make it harder to use a touch screen.</p>
<p style="text-align: center;"><iframe src="https://videopress.com/embed/2LMsUg9l" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen"></iframe><script src="https://videopress.com/videopress-iframe.js"></script></p>
<p>While we had to play favorites in describing some of the new functionalities in QField, we’ve barely touched the surface of this feature-packed release. Other major additions include support for <strong>Near-Field Communication (NFC)</strong> text tag reading and a new geometry editor’s eraser tool to delete part of lines and polygons as you would with a pencil sketch using an eraser.</p>
<p>Thanks to Deutsches Archäologisches Institut, Groupements forestiers Québec, Amsa, and Kanton Luzern for sponsoring these enhancements.</p>
<h2>Quality of life improvements</h2>
<p>Starting with this new version, the <strong>scale bar overlay</strong> will now respect projects’ distance measurement units, allowing for scale bars in imperial and nautical units.</p>
<p>QField now offers a <strong>rendering quality setting</strong> which, at the cost of a slightly reduced visual quality, results in faster rendering speeds and lower memory usage. This can be a lifesaver for older devices having difficulty handling large projects and helps save battery life.</p>
<p><strong>Vector tile layer support</strong> has been improved with the automated download of missing fonts and the possibility of toggling label visibility. This pair of changes makes this resolution-independent layer type much more appealing.</p>
<p>On iOS, layouts are now printed by QField as <strong>PDF documents</strong> instead of images. While this was the case for other platforms, it only became possible on iOS recently after work done by one of our ninjas in QGIS itself.</p>
<p>Many thanks to DB Fahrwgdienste for sponsoring stabilization efforts and fixes during this development cycle.</p>
<h2>Qt 6, the latest generation of the cross-platform framework powering QField</h2>
<p>Last but not least, <strong>QField 3.0 is now built against Qt 6</strong>. This is a significant technological milestone for the project as this means we can fully leverage the latest technological innovations into this cross-platform framework that has been powering QField since day one.</p>
<p>On top of the new possibilities, QField benefited from years of fixes and improvements, including<strong> better integration with Android and iOS platforms</strong>. In addition, the positioning framework in Qt 6 has been improved with awareness of the <strong>newer GNSS constellations</strong> that have emerged over the last decade.</p>
<h2>Forest-themed release names</h2>
<p>Forests are critical in climate regulation, biodiversity preservation, and economic sustainability. Beginning with <strong>QField 3.0 “Amazonia”</strong> and throughout the 3.X’s life cycle, we will choose forest names to underscore the importance of and advocate for global forest conservation.</p>
<p><img class="aligncenter " src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/10/qfield3.jpg?resize=1024%2C682&amp;ssl=1" width="456" height="304" /></p>
<h2>Software with service</h2>
<p><strong>OPENGIS.ch and Oslandia provides the full range of services around QField and QGIS</strong> : training, consulting, adaptation, specific development and core development, maintenance and assistance. Do not hesitate to contact us and detail your needs, we will be happy to collaborate : <a href="mailto:infos+qfield@oslandia.com">infos+qfield@oslandia.com</a></p>
<p><strong>As always, we hope you enjoy this new release. Happy field mapping!</strong></p>
