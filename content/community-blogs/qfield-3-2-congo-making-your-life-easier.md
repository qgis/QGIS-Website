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



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14228" height="468" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/qfield32.png?resize=750%2C468&#038;ssl=1" width="750" /></figure>



<p>This new release introduces <strong>project-defined tracking sessions, which are automatically activated when the project is loaded</strong>. Defined while setting up and tweaking a project on QGIS, these sessions permit the automated tracking of device positions without taking any action in QField beyond opening the project itself. This liberates field users from remembering to launch a session on app launch and lowers the knowledge required to collect such data. For more details, please read the <a href="https://docs.qfield.org/how-to/tracking/#configure-a-project-tracking-session">relevant QField documentation section</a>.</p>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14229" height="464" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/session.png?resize=750%2C464&#038;ssl=1" width="750" /></figure>



<p>As good as the above-described functionality sounds, it really shines through in cloud projects when paired with two other new featurs.</p>



<p>First, cloud projects can now automatically push accumulated changes at regular intervals. The functionality can be manually toggled for any cloud project by going to the synchronization panel in QField and activating the relevant toggle (see middle screenshot above). It can also be turned on project load by enabling automatic push when setting up the project in QGIS via the project properties dialog. When activated through this project setting, the functionality will always be activated, and the need for field users to take any action will be removed.</p>



<p>Pushing changes regularly is great, but it could easily have gotten in the way of blocking popups. This is why QField 3.2 can now push changes and synchronize cloud projects in the background. We still kept a ‘successfully pushed changes’ toast message to let you know the magic has happened <img alt="🚀" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f680.png" style="height: 1em;" /></p>



<p>With all of the above, cloud projects on QField can now deliver near real-time tracking of devices in the field, all configured on one desktop machine and deployed through QFieldCloud. Thanks to <a href="https://groupementsforestiers.quebec/">Groupements forestiers Québec</a> for sponsoring these enhancements.</p>



<p>Other noteworthy feature additions in this release include:</p>



<ul>
<li>A <strong>brand new undo/redo mechanism allows users to rollback feature addition, editing, and/or deletion</strong> at will. The redesigned QField main menu is accessible by long pressing on the top-left dashboard button.</li>



<li>Support for projects&#8217; <strong>titles and copyright map decorations as overlays</strong> on top of the map canvas in QField allows projects to better convey attributions and additional context through informative titles.</li>
</ul>



<h2 class="wp-block-heading"><strong>Additional improvements</strong></h2>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14230" height="425" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/03/cloud.png?resize=750%2C425&#038;ssl=1" width="750" /></figure>



<p>The <strong>QFieldCloud user experience continues to be improved</strong>. In this release, we have reworked the visual feedback provided when downloading and synchronizing projects through the addition of a progress bar as well as additional details, such as the overall size of the files being fetched. In addition, a visual indicator has been added to the dashboard and the cloud projects list to alert users to the presence of a newer project file on the cloud for projects locally available on the device.</p>



<p>With that said, if you haven&#8217;t signed onto <a href="https://app.qfield.cloud/">QFieldCloud</a> yet, try it! Psst, the community account is free <img alt="🤫" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f92b.png" style="height: 1em;" /></p>



<p>The <strong>creation of relationship children during feature digitizing is now smoother</strong> as we lifted the requirement to save a parent feature <em>before</em> creating children. Users can now proceed in the order that feels most natural to them.</p>



<p>Finally, Android users will be happy to hear that a <strong>significant rework of native camera, gallery, and file picker</strong> activities has led to increased stability and much better integration with Android itself. Activities such as the gallery are now properly overlayed on top of the QField map canvas instead of showing a black screen.</p>
