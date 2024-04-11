---
source: "blog"
title: "OPENGIS.ch blog: QField 3.2 “Congo”: Making your life easier"
image: "qfield-3-2-congo-making-your-life-easier."
date: "2024-04-04"
link: "https://www.opengis.ch/2024/04/04/qfield-3-2-congo-making-your-life-easier/"
draft: "true"
showcase: "planet"
---

<p>Focused on stability and usability improvements, most users will find something to celebrate in QField 3.2</p>



<h2 class="wp-block-heading"><strong>Main highlights</strong></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="750" height="468" data-attachment-id="14228" data-permalink="https://www.opengis.ch/2024/04/04/qfield-3-2-congo-making-your-life-easier/qfield32/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?fit=956%2C597&amp;ssl=1" data-orig-size="956,597" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="qfield32" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?fit=300%2C187&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?fit=750%2C468&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?resize=750%2C468&#038;ssl=1" alt="" class="wp-image-14228" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?w=956&amp;ssl=1 956w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?resize=300%2C187&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?resize=768%2C480&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>This new release introduces <strong>project-defined tracking sessions, which are automatically activated when the project is loaded</strong>. Defined while setting up and tweaking a project on QGIS, these sessions permit the automated tracking of device positions without taking any action in QField beyond opening the project itself. This liberates field users from remembering to launch a session on app launch and lowers the knowledge required to collect such data. For more details, please read the <a href="https://docs.qfield.org/how-to/tracking/#configure-a-project-tracking-session" data-type="link" data-id="https://docs.qfield.org/how-to/tracking/#configure-a-project-tracking-session">relevant QField documentation section</a>.</p>



<figure class="wp-block-image size-full"><img decoding="async" width="750" height="464" data-attachment-id="14229" data-permalink="https://www.opengis.ch/2024/04/04/qfield-3-2-congo-making-your-life-easier/session/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?fit=942%2C583&amp;ssl=1" data-orig-size="942,583" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="session" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?fit=300%2C186&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?fit=750%2C464&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?resize=750%2C464&#038;ssl=1" alt="" class="wp-image-14229" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?w=942&amp;ssl=1 942w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?resize=300%2C186&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?resize=768%2C475&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>As good as the above-described functionality sounds, it really shines through in cloud projects when paired with two other new featurs.</p>



<p>First, cloud projects can now automatically push accumulated changes at regular intervals. The functionality can be manually toggled for any cloud project by going to the synchronization panel in QField and activating the relevant toggle (see middle screenshot above). It can also be turned on project load by enabling automatic push when setting up the project in QGIS via the project properties dialog. When activated through this project setting, the functionality will always be activated, and the need for field users to take any action will be removed.</p>



<p>Pushing changes regularly is great, but it could easily have gotten in the way of blocking popups. This is why QField 3.2 can now push changes and synchronize cloud projects in the background. We still kept a ‘successfully pushed changes’ toast message to let you know the magic has happened <img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f680.png" alt="🚀" class="wp-smiley" style="height: 1em; max-height: 1em;" /></p>



<p>With all of the above, cloud projects on QField can now deliver near real-time tracking of devices in the field, all configured on one desktop machine and deployed through QFieldCloud. Thanks to <a href="https://groupementsforestiers.quebec/" data-type="link" data-id="https://groupementsforestiers.quebec/">Groupements forestiers Québec</a> for sponsoring these enhancements.</p>



<p>Other noteworthy feature additions in this release include:</p>



<ul>
<li>A <strong>brand new undo/redo mechanism allows users to rollback feature addition, editing, and/or deletion</strong> at will. The redesigned QField main menu is accessible by long pressing on the top-left dashboard button.</li>



<li>Support for projects&#8217; <strong>titles and copyright map decorations as overlays</strong> on top of the map canvas in QField allows projects to better convey attributions and additional context through informative titles.</li>
</ul>



<h2 class="wp-block-heading"><strong>Additional improvements</strong></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="750" height="425" data-attachment-id="14230" data-permalink="https://www.opengis.ch/2024/04/04/qfield-3-2-congo-making-your-life-easier/cloud/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?fit=866%2C491&amp;ssl=1" data-orig-size="866,491" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="cloud" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?fit=300%2C170&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?fit=750%2C425&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?resize=750%2C425&#038;ssl=1" alt="" class="wp-image-14230" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?w=866&amp;ssl=1 866w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?resize=300%2C170&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?resize=768%2C435&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>The <strong>QFieldCloud user experience continues to be improved</strong>. In this release, we have reworked the visual feedback provided when downloading and synchronizing projects through the addition of a progress bar as well as additional details, such as the overall size of the files being fetched. In addition, a visual indicator has been added to the dashboard and the cloud projects list to alert users to the presence of a newer project file on the cloud for projects locally available on the device.</p>



<p>With that said, if you haven&#8217;t signed onto <a href="https://app.qfield.cloud/">QFieldCloud</a> yet, try it! Psst, the community account is free <img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f92b.png" alt="🤫" class="wp-smiley" style="height: 1em; max-height: 1em;" /></p>



<p>The <strong>creation of relationship children during feature digitizing is now smoother</strong> as we lifted the requirement to save a parent feature <em>before</em> creating children. Users can now proceed in the order that feels most natural to them.</p>



<p>Finally, Android users will be happy to hear that a <strong>significant rework of native camera, gallery, and file picker</strong> activities has led to increased stability and much better integration with Android itself. Activities such as the gallery are now properly overlayed on top of the QField map canvas instead of showing a black screen.</p>
