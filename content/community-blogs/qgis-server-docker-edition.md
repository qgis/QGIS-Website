---
source: "blog"
title: "anitagraser.com: QGIS Server — Docker edition"
image: "qgis-server-docker-edition."
date: "2024-04-20"
link: "https://anitagraser.com/2024/04/20/qgis-server-docker-edition/"
draft: "true"
showcase: "planet"
---

<p>Today&#8217;s post is a QGIS Server update. It&#8217;s been a while (12 years <img src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f635.png" alt="😵" class="wp-smiley" style="height: 1em; max-height: 1em;" />) since I  <a href="https://anitagraser.com/2012/03/30/qgis-server-on-ubuntu-step-by-step/">last posted about QGIS Server</a>. It would be an understatement to say that things have evolved since then, not least due to the development of Docker which, <a href="https://en.wikipedia.org/wiki/Docker_(software)">Wikipedia tells me</a>, was released 11 years ago. </p>



<p>There have been multiple Docker images for QGIS Server provided by QGIS Community members over the years. Recently, OPENGIS.ch&#8217;s Docker image has been adopted as official QGIS Server image <a href="https://github.com/qgis/qgis-docker">https://github.com/qgis/qgis-docker</a> which aims to be a starting point for users to develop their own customized applications.</p>



<p>The following steps have been tested on Ubuntu (both native and in WSL). </p>



<p>First, we need Docker. I installed Docker from the apt repository <a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository">as described in the official docs</a>. </p>



<p>Once Docker is set up, we can get the QGIS Server, e.g. for the LTR: </p>



<pre class="wp-block-code"><code>docker pull qgis/qgis-server:ltr</code></pre>



<p>Now we only need to start it:</p>



<pre class="wp-block-code"><code>docker run -v $(pwd)/qgis-server-data:/io/data --name qgis-server -d -p 8010:80 qgis/qgis-server:ltr</code></pre>



<p>Note how we are mapping the qgis-server-data directory in our current working directory to /io/data in the container. This is where we&#8217;ll put our QGIS project files.</p>



<p>We can already check out the OGC API landing page at <a href="http://localhost:8010/wfs3/" rel="nofollow">http://localhost:8010/wfs3/</a></p>



<figure class="wp-block-image size-large"><img width="395" height="375" data-attachment-id="8858" data-permalink="https://anitagraser.com/2024/04/20/qgis-server-docker-edition/image-1-15/" data-orig-file="https://underdark.files.wordpress.com/2024/04/image-1.png" data-orig-size="395,375" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-1" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/04/image-1.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/04/image-1.png?w=395" src="https://underdark.files.wordpress.com/2024/04/image-1.png?w=395" alt="" class="wp-image-8858" srcset="https://underdark.files.wordpress.com/2024/04/image-1.png 395w, https://underdark.files.wordpress.com/2024/04/image-1.png?w=150 150w, https://underdark.files.wordpress.com/2024/04/image-1.png?w=300 300w" sizes="(max-width: 395px) 100vw, 395px" /></figure>



<p>Let’s add a sample project from the <a href="https://github.com/qgis/QGIS-Training-Data/">Training demo data</a> repo. (You may need to install unzip if you haven&#8217;t yet.)</p>



<pre id="codecell3" class="wp-block-code"><code>mkdir qgis-server-data
cd qgis-server-data
wget https://github.com/qgis/QGIS-Training-Data/archive/release_3.22.zip
unzip release_3.22.zip
mkdir world
cp QGIS-Training-Data-release_3.22/exercise_data/qgis-server-tutorial-data/world.qgs world/
cp QGIS-Training-Data-release_3.22/exercise_data/qgis-server-tutorial-data/naturalearth.sqlite world</code></pre>



<p>Giving us:</p>



<figure class="wp-block-image size-large"><img width="538" height="119" data-attachment-id="8860" data-permalink="https://anitagraser.com/2024/04/20/qgis-server-docker-edition/image-2-14/" data-orig-file="https://underdark.files.wordpress.com/2024/04/image-2.png" data-orig-size="538,119" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-2" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/04/image-2.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/04/image-2.png?w=538" src="https://underdark.files.wordpress.com/2024/04/image-2.png?w=538" alt="" class="wp-image-8860" srcset="https://underdark.files.wordpress.com/2024/04/image-2.png 538w, https://underdark.files.wordpress.com/2024/04/image-2.png?w=150 150w, https://underdark.files.wordpress.com/2024/04/image-2.png?w=300 300w" sizes="(max-width: 538px) 100vw, 538px" /></figure>



<p>QGIS Server should now be serving this sample project. Let&#8217;s check with a WMS GetMap request:</p>



<p><a href="http://localhost:8010/ogc/world?LAYERS=countries&#038;SERVICE=WMS&#038;VERSION=1.3.0&#038;REQUEST=GetMap&#038;CRS=EPSG:4326&#038;WIDTH=400&#038;HEIGHT=200&#038;BBOX=-90,-180,90,180" rel="nofollow">http://localhost:8010/ogc/world?LAYERS=countries&#038;SERVICE=WMS&#038;VERSION=1.3.0&#038;REQUEST=GetMap&#038;CRS=EPSG:4326&#038;WIDTH=400&#038;HEIGHT=200&#038;BBOX=-90,-180,90,180</a></p>



<p>Giving us: </p>



<figure class="wp-block-image size-large"><img width="400" height="200" data-attachment-id="8861" data-permalink="https://anitagraser.com/2024/04/20/qgis-server-docker-edition/image-3-13/" data-orig-file="https://underdark.files.wordpress.com/2024/04/image-3.png" data-orig-size="400,200" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-3" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/04/image-3.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/04/image-3.png?w=400" src="https://underdark.files.wordpress.com/2024/04/image-3.png?w=400" alt="" class="wp-image-8861" srcset="https://underdark.files.wordpress.com/2024/04/image-3.png 400w, https://underdark.files.wordpress.com/2024/04/image-3.png?w=150 150w, https://underdark.files.wordpress.com/2024/04/image-3.png?w=300 300w" sizes="(max-width: 400px) 100vw, 400px" /></figure>



<p><em>If you instead get the error &#8220;&lt;ServerException&gt;Project file error. For OWS services: please provide a SERVICE and a MAP parameter pointing to a valid QGIS project file&lt;/ServerException&gt;&#8221;, it probably means that the world.qgs file is not found in the qgis-server-data/world directory. </em></p>



<p>Of course, we can also add <a href="http://localhost:8010/ogc/world">http://localhost:8010/ogc/world</a> to the WMS and WFS server connections in our QGIS Desktop: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/04/image-4.png"><img loading="lazy" width="1024" height="600" data-attachment-id="8863" data-permalink="https://anitagraser.com/2024/04/20/qgis-server-docker-edition/image-4-12/" data-orig-file="https://underdark.files.wordpress.com/2024/04/image-4.png" data-orig-size="1026,602" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-4" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2024/04/image-4.png?w=300" data-large-file="https://underdark.files.wordpress.com/2024/04/image-4.png?w=545" src="https://underdark.files.wordpress.com/2024/04/image-4.png?w=1024" alt="" class="wp-image-8863" srcset="https://underdark.files.wordpress.com/2024/04/image-4.png?w=1024 1024w, https://underdark.files.wordpress.com/2024/04/image-4.png?w=150 150w, https://underdark.files.wordpress.com/2024/04/image-4.png?w=300 300w, https://underdark.files.wordpress.com/2024/04/image-4.png?w=768 768w, https://underdark.files.wordpress.com/2024/04/image-4.png 1026w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>
