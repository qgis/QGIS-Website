---
source: "blog"
title: "anitagraser.com: Trajectools 2.0 released 🎉"
image: "trajectools-2-0-released."
date: "2024-02-24"
link: "https://anitagraser.com/2024/02/24/trajectools-2-0-released/"
draft: "true"
showcase: "planet"
---

<p>It&#8217;s my pleasure to share with you that Trajectools 2.0 just landed in <a href="https://plugins.qgis.org/plugins/processing_trajectory/#plugin-versions">the official QGIS Plugin Repository</a>.</p>



<p>This is the first version without the &#8220;experimental&#8221; flag. If you look at the plugin release history, you will see that the previous release was from 2020. That&#8217;s quite a while ago and a lot has happened since, including the development of <a href="https://movingpandas.org">MovingPandas</a>.</p>



<h2 class="wp-block-heading">Let&#8217;s have a look what&#8217;s new!</h2>



<figure class="wp-block-image size-large"><img loading="lazy" width="624" height="325" data-attachment-id="8812" data-permalink="https://anitagraser.com/2024/02/24/trajectools-2-0-released/trajectools-1-2/" data-orig-file="https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png" data-orig-size="624,325" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="trajectools-1-2" data-image-description="" data-image-caption="" data-medium-file="https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png?w=300" data-large-file="https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png?w=545" src="https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png?w=624" alt="" class="wp-image-8812" srcset="https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png 624w, https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png?w=150 150w, https://anitagraser.com/wp-content/uploads/2024/02/trajectools-1-2.png?w=300 300w" sizes="(max-width: 624px) 100vw, 624px" /></figure>



<p>The old &#8220;Trajectories from point layer&#8221;, &#8220;Add heading to points&#8221;, and &#8220;Add speed (m/s) to points&#8221; algorithms have been superseded by the new <strong>&#8220;Create trajectories&#8221;</strong> algorithm which automatically computes speeds and headings when creating the trajectory outputs. </p>



<p>&#8220;Day trajectories from point layer&#8221; is covered by the new <strong>&#8220;Split trajectories at time intervals&#8221; </strong>which supports splitting by hour, day, month, and year.</p>



<p><strong>&#8220;Clip trajectories by extent&#8221;</strong> still exists but, additionally, we can now also <strong>&#8220;Clip trajectories by polygon layer&#8221;</strong></p>



<p>There are two new event extraction algorithms to <strong>&#8220;Extract OD points&#8221;</strong> and <strong>&#8220;Extract OD points&#8221;</strong>, as well as the related <strong>&#8220;Split trajectories at stops&#8221;</strong>. Additionally, we can also <strong>&#8220;Split trajectories at observation gaps&#8221;</strong>.</p>



<p>Trajectory outputs, by default, come as a pair of a point layer and a line layer. Depending on your use case, you can use both or pick just one of them. By default, the line layer is styled with a gradient line that makes it easy to see the movement direction:</p>



<figure class="wp-block-image size-large"><img loading="lazy" width="624" height="191" data-attachment-id="8817" data-permalink="https://anitagraser.com/2024/02/24/trajectools-2-0-released/image-7-9/" data-orig-file="https://anitagraser.com/wp-content/uploads/2024/02/image-7.png" data-orig-size="624,191" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-7" data-image-description="" data-image-caption="" data-medium-file="https://anitagraser.com/wp-content/uploads/2024/02/image-7.png?w=300" data-large-file="https://anitagraser.com/wp-content/uploads/2024/02/image-7.png?w=545" src="https://anitagraser.com/wp-content/uploads/2024/02/image-7.png?w=624" alt="" class="wp-image-8817" srcset="https://anitagraser.com/wp-content/uploads/2024/02/image-7.png 624w, https://anitagraser.com/wp-content/uploads/2024/02/image-7.png?w=150 150w, https://anitagraser.com/wp-content/uploads/2024/02/image-7.png?w=300 300w" sizes="(max-width: 624px) 100vw, 624px" /></figure>



<p>while the default point layer style shows the movement speed: </p>



<figure class="wp-block-image size-large"><img loading="lazy" width="612" height="207" data-attachment-id="8824" data-permalink="https://anitagraser.com/2024/02/24/trajectools-2-0-released/image-12-6/" data-orig-file="https://anitagraser.com/wp-content/uploads/2024/02/image-12.png" data-orig-size="612,207" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-12" data-image-description="" data-image-caption="" data-medium-file="https://anitagraser.com/wp-content/uploads/2024/02/image-12.png?w=300" data-large-file="https://anitagraser.com/wp-content/uploads/2024/02/image-12.png?w=545" src="https://anitagraser.com/wp-content/uploads/2024/02/image-12.png?w=612" alt="" class="wp-image-8824" srcset="https://anitagraser.com/wp-content/uploads/2024/02/image-12.png 612w, https://anitagraser.com/wp-content/uploads/2024/02/image-12.png?w=150 150w, https://anitagraser.com/wp-content/uploads/2024/02/image-12.png?w=300 300w" sizes="(max-width: 612px) 100vw, 612px" /></figure>



<h2 class="wp-block-heading">How to use Trajectools</h2>



<p>Trajectools 2.0 is powered by MovingPandas. You will need to install MovingPandas in your QGIS Python environment. I recommend installing both QGIS and MovingPandas from conda-forge:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: bash; title: ; notranslate">
(base) conda create -n qgis -c conda-forge python=3.9 
(base) conda activate qgis
(qgis) mamba install -c conda-forge qgis movingpandas
</pre></div>


<p>The plugin download includes small trajectory sample datasets so you can get started immediately. </p>



<h2 class="wp-block-heading">Outlook</h2>



<p>There is still some work to do to reach feature parity with MovingPandas. Stay tuned for more trajectory algorithms, including but not limited to down-sampling, smoothing, and outlier cleaning. </p>



<p>I&#8217;m also reviewing other existing QGIS plugins to see how they can complement each other. If you know a plugin I should look into, please leave a note in the comments. </p>
