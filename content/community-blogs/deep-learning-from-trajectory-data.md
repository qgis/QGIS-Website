---
source: "blog"
title: "anitagraser.com: Deep learning from trajectory data"
image: "deep-learning-from-trajectory-data."
date: "2023-03-31"
link: "https://anitagraser.com/2023/03/30/deep-learning-from-trajectory-data/"
draft: "true"
showcase: "planet"
---

<p>I&#8217;ve previously written about <a href="https://anitagraser.com/2019/05/01/movement-data-in-gis-and-the-ai-hype/">Movement data in GIS and the AI hype</a> and today&#8217;s post is a follow-up in which I want to share with you a new review of the state of the art in deep learning from trajectory data. </p>



<p>Our review covers 8 use cases:</p>



<ol>
<li>Location classification</li>



<li>Arrival time prediction</li>



<li>Traffic flow / activity prediction </li>



<li>Trajectory prediction</li>



<li>Trajectory classification</li>



<li>Next location prediction</li>



<li>Anomaly detection </li>



<li>Synthetic data generation</li>
</ol>



<p>We particularly looked into the trajectory data preprocessing steps and the specific movement data representation used as input to train the neutral networks:</p>



<figure class="wp-block-image size-large"><img data-attachment-id="8396" data-permalink="https://anitagraser.com/2023/03/30/deep-learning-from-trajectory-data/screenshot_20230330_100728_dropbox/" data-orig-file="https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg" data-orig-size="1041,2097" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="Screenshot_20230330_100728_Dropbox" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=149" data-large-file="https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=508" src="https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=508" alt="" class="wp-image-8396" srcset="https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=508 508w, https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=1016 1016w, https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=74 74w, https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=149 149w, https://underdark.files.wordpress.com/2023/03/screenshot_20230330_100728_dropbox.jpg?w=768 768w" sizes="(max-width: 508px) 100vw, 508px" /></figure>



<p>On a completely subjective note: the price for most surprising approach&nbsp;goes to natural language processing (NLP) Transfomers for traffic volume prediction.</p>



<figure class="wp-block-image size-large"><img data-attachment-id="8395" data-permalink="https://anitagraser.com/2023/03/30/deep-learning-from-trajectory-data/c55abc39fa370223/" data-orig-file="https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png" data-orig-size="640,360" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="c55abc39fa370223" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png?w=545" src="https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png?w=640" alt="" class="wp-image-8395" srcset="https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png 640w, https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png?w=150 150w, https://underdark.files.wordpress.com/2023/03/c55abc39fa370223.png?w=300 300w" sizes="(max-width: 640px) 100vw, 640px" /></figure>



<p>The paper was presented at <a href="https://www.datastories.org/bmda23/BMDA23Program.html">BMDA2023</a> and you can watch the full talk recording here:</p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe class="youtube-player" width="545" height="307" src="https://www.youtube.com/embed/zHI-52U8gjU?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en&#038;autohide=2&#038;wmode=transparent" allowfullscreen="true" style="border:0;" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation"></iframe>
</div></figure>



<p><strong>References</strong></p>



<p><a href="https://www.dropbox.com/s/ex6jq7nay7d3l00/Graser-et-al_2023_Deep_Learning_From_Trajectory_Data_Review_fixed-fig-ref.pdf?dl=0">Graser, A., Jalali, A., Lampert, J., Weißenfeld, A., &amp; Janowicz, K. (2023). Deep Learning From Trajectory Data: a Review of Neural Networks and the Trajectory Data Representations to Train Them. Workshop on Big Mobility Data Analysis BMDA2023 in conjunction with EDBT/ICDT 2023.</a></p>



<hr class="wp-block-separator has-alpha-channel-opacity" />



<p>This post is part of a series. Read more about&nbsp;<a href="https://anitagraser.com/movement-data-in-gis/">movement data in GIS.</a></p>
