---
source: "blog"
title: "anitagraser.com: GTFS algorithms about to land in Trajectools"
image: "gtfs-algorithms-about-to-land-in-trajectools."
date: "2024-05-04"
link: "https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/"
draft: "true"
showcase: "planet"
---

<p><a href="https://anitagraser.com/trajectools/">Trajectools</a> continues growing. Lately, we have started expanding towards public transport analysis. The algorithms available through the current <a href="https://github.com/movingpandas/qgis-processing-trajectory/tree/emeralds">Trajectools development version</a> are courtesy of the <a href="https://github.com/Bondify/gtfs_functions">gtfs_functions</a> library.</p>



<p>There are a couple of existing plugins that deal with GTFS. However, in my experience, they either don&#8217;t integrate with Processing and/or don&#8217;t provide the functions I was expecting. </p>



<p>So far, we have two GTFS algorithms to cover essential public transport analysis needs: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8874" height="415" src="https://anitagraser.com/wp-content/uploads/2024/05/image.png?w=326" width="326" /></figure>



<p>The &#8220;Extract shapes&#8221; algorithm gives us the public transport routes: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8882" height="366" src="https://anitagraser.com/wp-content/uploads/2024/05/image-4.png?w=495" width="495" /></figure>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-2.png"><img alt="" class="wp-image-8879" height="735" src="https://anitagraser.com/wp-content/uploads/2024/05/image-2.png?w=887" width="887" /></a></figure>



<p>The &#8220;Extract segments&#8221; algorithm has one more options. In addition to extracting the segments between public transport stops, it can also enrich the segments with the scheduled vehicle speeds:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8884" height="366" src="https://anitagraser.com/wp-content/uploads/2024/05/image-5.png?w=495" width="495" /></figure>



<p>Here you can see the scheduled speeds: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-1.png"><img alt="" class="wp-image-8876" height="734" src="https://anitagraser.com/wp-content/uploads/2024/05/image-1.png?w=897" width="897" /></a></figure>



<p></p>



<p>To show the stops, we can put marker line markers on the segment start and end locations:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-6.png"><img alt="" class="wp-image-8886" height="584" src="https://anitagraser.com/wp-content/uploads/2024/05/image-6.png?w=937" width="937" /></a></figure>



<p>The segments contain route information and stop names, so these can be extracted and used for labeling as well: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-7.png"><img alt="" class="wp-image-8888" height="632" src="https://anitagraser.com/wp-content/uploads/2024/05/image-7.png?w=1024" width="1024" /></a></figure>



<p>If you want to reproduce the above examples, grab the open <a href="https://www.mobilitydata.gv.at/daten/soll-fahrplandaten-gtfs">Vorarlberg public transport schedule GTFS</a>.</p>



<p><em>These developments are supported by the <a href="https://emeralds-horizon.eu">Emeralds Horizon Europe project</a>. </em></p>
