---
source: "blog"
title: "anitagraser.com: GTFS algorithms about to land in Trajectools"
image: "gtfs-algorithms-about-to-land-in-trajectools."
date: "2024-05-04"
link: "https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/"
draft: "true"
showcase: "planet"
---

<p>Trajectools continues growing. Lately, we have started expanding towards public transport analysis. The algorithms available through the current <a href="https://github.com/movingpandas/qgis-processing-trajectory/tree/emeralds">Trajectools development version</a> are courtesy of the <a href="https://github.com/Bondify/gtfs_functions">gtfs_functions</a> library.</p>



<p>There are a couple of existing plugins that deal with GTFS. However, in my experience, they either don&#8217;t integrate with Processing and/or don&#8217;t provide the functions I was expecting. </p>



<p>So far, we have two GTFS algorithms to cover essential public transport analysis needs: </p>



<figure class="wp-block-image size-large"><img width="326" height="415" data-attachment-id="8874" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-47/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image.png" data-orig-size="326,415" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image.png?w=236" data-large-file="https://underdark.files.wordpress.com/2024/05/image.png?w=326" src="https://underdark.files.wordpress.com/2024/05/image.png?w=326" alt="" class="wp-image-8874" srcset="https://underdark.files.wordpress.com/2024/05/image.png 326w, https://underdark.files.wordpress.com/2024/05/image.png?w=118 118w, https://underdark.files.wordpress.com/2024/05/image.png?w=236 236w" sizes="(max-width: 326px) 100vw, 326px" /></figure>



<p>The &#8220;Extract shapes&#8221; algorithm gives us the public transport routes: </p>



<figure class="wp-block-image size-large"><img width="495" height="366" data-attachment-id="8882" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-4-13/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-4.png" data-orig-size="495,366" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-4" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-4.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-4.png?w=495" src="https://underdark.files.wordpress.com/2024/05/image-4.png?w=495" alt="" class="wp-image-8882" srcset="https://underdark.files.wordpress.com/2024/05/image-4.png 495w, https://underdark.files.wordpress.com/2024/05/image-4.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-4.png?w=300 300w" sizes="(max-width: 495px) 100vw, 495px" /></figure>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/05/image-2.png"><img width="887" height="735" data-attachment-id="8879" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-2-15/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-2.png" data-orig-size="887,735" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-2" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-2.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-2.png?w=545" src="https://underdark.files.wordpress.com/2024/05/image-2.png?w=887" alt="" class="wp-image-8879" srcset="https://underdark.files.wordpress.com/2024/05/image-2.png 887w, https://underdark.files.wordpress.com/2024/05/image-2.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-2.png?w=300 300w, https://underdark.files.wordpress.com/2024/05/image-2.png?w=768 768w" sizes="(max-width: 887px) 100vw, 887px" /></a></figure>



<p>The &#8220;Extract segments&#8221; algorithm has one more options. In addition to extracting the segments between public transport stops, it can also enrich the segments with the scheduled vehicle speeds:</p>



<figure class="wp-block-image size-large"><img loading="lazy" width="495" height="366" data-attachment-id="8884" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-5-11/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-5.png" data-orig-size="495,366" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-5" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-5.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-5.png?w=495" src="https://underdark.files.wordpress.com/2024/05/image-5.png?w=495" alt="" class="wp-image-8884" srcset="https://underdark.files.wordpress.com/2024/05/image-5.png 495w, https://underdark.files.wordpress.com/2024/05/image-5.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-5.png?w=300 300w" sizes="(max-width: 495px) 100vw, 495px" /></figure>



<p>Here you can see the scheduled speeds: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/05/image-1.png"><img loading="lazy" width="897" height="734" data-attachment-id="8876" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-1-16/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-1.png" data-orig-size="897,734" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-1" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-1.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-1.png?w=545" src="https://underdark.files.wordpress.com/2024/05/image-1.png?w=897" alt="" class="wp-image-8876" srcset="https://underdark.files.wordpress.com/2024/05/image-1.png 897w, https://underdark.files.wordpress.com/2024/05/image-1.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-1.png?w=300 300w, https://underdark.files.wordpress.com/2024/05/image-1.png?w=768 768w" sizes="(max-width: 897px) 100vw, 897px" /></a></figure>



<p></p>



<p>To show the stops, we can put marker line markers on the segment start and end locations:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/05/image-6.png"><img loading="lazy" width="937" height="584" data-attachment-id="8886" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-6-11/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-6.png" data-orig-size="937,584" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-6" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-6.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-6.png?w=545" src="https://underdark.files.wordpress.com/2024/05/image-6.png?w=937" alt="" class="wp-image-8886" srcset="https://underdark.files.wordpress.com/2024/05/image-6.png 937w, https://underdark.files.wordpress.com/2024/05/image-6.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-6.png?w=300 300w, https://underdark.files.wordpress.com/2024/05/image-6.png?w=768 768w" sizes="(max-width: 937px) 100vw, 937px" /></a></figure>



<p>The segments contain route information and stop names, so these can be extracted and used for labeling as well: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/05/image-7.png"><img loading="lazy" width="1024" height="632" data-attachment-id="8888" data-permalink="https://anitagraser.com/2024/05/04/gtfs-algorithms-about-to-land-in-trajectools/image-7-10/" data-orig-file="https://underdark.files.wordpress.com/2024/05/image-7.png" data-orig-size="1101,680" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-7" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/05/image-7.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/05/image-7.png?w=545" src="https://underdark.files.wordpress.com/2024/05/image-7.png?w=1024" alt="" class="wp-image-8888" srcset="https://underdark.files.wordpress.com/2024/05/image-7.png?w=1024 1024w, https://underdark.files.wordpress.com/2024/05/image-7.png?w=150 150w, https://underdark.files.wordpress.com/2024/05/image-7.png?w=300 300w, https://underdark.files.wordpress.com/2024/05/image-7.png?w=768 768w, https://underdark.files.wordpress.com/2024/05/image-7.png 1101w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>If you want to reproduce the above examples, grab the open <a href="https://www.mobilitydata.gv.at/daten/soll-fahrplandaten-gtfs">Vorarlberg public transport schedule GTFS</a>.</p>



<p><em>These developments are supported by the <a href="https://emeralds-horizon.eu">Emeralds Horizon Europe project</a>. </em></p>
