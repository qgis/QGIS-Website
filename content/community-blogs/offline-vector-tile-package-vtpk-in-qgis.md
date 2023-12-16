---
source: "blog"
title: "anitagraser.com: Offline Vector Tile Package .vtpk in QGIS"
image: "offline-vector-tile-package-vtpk-in-qgis."
date: "2023-12-15"
link: "https://anitagraser.com/2023/12/15/offline-vector-tile-package-vtpk-in-qgis/"
draft: "true"
showcase: "planet"
---

<p>Starting from 3.26, <a href="https://qgis.org/en/site/forusers/visualchangelog326/index.html#feature-support-reading-esri-vector-tile-packages-vtpk-files-directly">QGIS now supports .vtpk (Vector Tile Package) files</a> out of the box! From the changelog:</p>



<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p>ESRI vector tile packages (VTPK files) can now be opened directly as vector tile layers via drag and drop, including support for style translation.</p>
</blockquote>



<p>This is great news, particularly for users from Austria, since this makes it possible to use the open government basemap.at vector tiles directly, without any fuss: </p>



<p>1. Download the 2GB offline vector basemap from <a href="https://www.data.gv.at/katalog/de/dataset/basemap-at-verwaltungsgrundkarte-vektor-offline-osterreich">https://www.data.gv.at/katalog/de/dataset/basemap-at-verwaltungsgrundkarte-vektor-offline-osterreich</a><br></p>



<figure class="wp-block-image size-large"><img width="953" height="699" data-attachment-id="8719" data-permalink="https://anitagraser.com/2023/12/15/offline-vector-tile-package-vtpk-in-qgis/image-15-4/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-15.png" data-orig-size="953,699" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-15" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-15.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-15.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-15.png?w=953" alt="" class="wp-image-8719" srcset="https://underdark.files.wordpress.com/2023/12/image-15.png 953w, https://underdark.files.wordpress.com/2023/12/image-15.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-15.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-15.png?w=768 768w" sizes="(max-width: 953px) 100vw, 953px" /></figure>



<p><br>2. Add the .vtpk as a layer using the Data Source Manager or via drag-and-drop from the file explorer<br></p>



<figure class="wp-block-image size-large"><img width="1024" height="735" data-attachment-id="8721" data-permalink="https://anitagraser.com/2023/12/15/offline-vector-tile-package-vtpk-in-qgis/image-16-4/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-16.png" data-orig-size="1296,931" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-16" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-16.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-16.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-16.png?w=1024" alt="" class="wp-image-8721" srcset="https://underdark.files.wordpress.com/2023/12/image-16.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/12/image-16.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-16.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-16.png?w=768 768w, https://underdark.files.wordpress.com/2023/12/image-16.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<p><br>3. All done and ready, including the basemap styling and labeling &#8212; which we can customize as well: </p>



<figure class="wp-block-image size-large"><img width="1024" height="735" data-attachment-id="8723" data-permalink="https://anitagraser.com/2023/12/15/offline-vector-tile-package-vtpk-in-qgis/image-17-4/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-17.png" data-orig-size="1296,931" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-17" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-17.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-17.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-17.png?w=1024" alt="" class="wp-image-8723" srcset="https://underdark.files.wordpress.com/2023/12/image-17.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/12/image-17.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-17.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-17.png?w=768 768w, https://underdark.files.wordpress.com/2023/12/image-17.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<figure class="wp-block-image size-large"><img loading="lazy" width="1024" height="735" data-attachment-id="8725" data-permalink="https://anitagraser.com/2023/12/15/offline-vector-tile-package-vtpk-in-qgis/image-18-3/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-18.png" data-orig-size="1296,931" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-18" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-18.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-18.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-18.png?w=1024" alt="" class="wp-image-8725" srcset="https://underdark.files.wordpress.com/2023/12/image-18.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/12/image-18.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-18.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-18.png?w=768 768w, https://underdark.files.wordpress.com/2023/12/image-18.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<p>Kudos to <a href="https://wien.rocks/@DieterKomendera/111568809248327077">https://wien.rocks/@DieterKomendera/111568809248327077</a> for bringing this new feature to my attention. </p>
