---
source: "blog"
title: "anitagraser.com: Analyzing mobility hotspots with MovingPandas & CARTO"
image: "analyzing-mobility-hotspots-with-movingpandas-carto."
date: "2023-11-28"
link: "https://anitagraser.com/2023/11/28/analyzing-mobility-hotspots-with-movingpandas-carto/"
draft: "true"
showcase: "planet"
---

<p>Today, I want to point out a blog post over at</p>



<p><a href="https://carto.com/blog/analyzing-mobility-hotspots-with-movingpandas" rel="nofollow">https://carto.com/blog/analyzing-mobility-hotspots-with-movingpandas</a></p>



<p>written together with my fellow co-authors and EMERALDS project team members Argyrios Kyrgiazos and Helen McKenzie. </p>



<figure class="wp-block-image size-large is-resized"><a href="https://underdark.files.wordpress.com/2023/11/image-41.png"><img width="1024" height="616" data-attachment-id="8650" data-permalink="https://anitagraser.com/2023/11/28/analyzing-mobility-hotspots-with-movingpandas-carto/image-41/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-41.png" data-orig-size="2152,1296" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-41" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-41.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-41.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-41.png?w=1024" alt="" class="wp-image-8650" style="width:840px;height:auto" srcset="https://underdark.files.wordpress.com/2023/11/image-41.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-41.png?w=2046 2046w, https://underdark.files.wordpress.com/2023/11/image-41.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-41.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-41.png?w=768 768w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>In this blog post, we walk you through a trajectory hotspot analysis using open <a href="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/">taxi trajectory data from Kaggle</a>, combining data preparation with MovingPandas (including the <a href="https://anitagraser.com/2023/11/15/movingpandas-v0-17-released/">new OutlierCleaner</a> illustrated above) and spatiotemporal hotspot analysis from Carto.</p>
