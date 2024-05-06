---
source: "blog"
title: "anitagraser.com: QGIS Server — Docker edition"
image: "qgis-server-docker-edition."
date: "2024-04-20"
link: "https://anitagraser.com/2024/04/20/qgis-server-docker-edition/"
draft: "true"
showcase: "planet"
---

<p>Today&#8217;s post is a QGIS Server update. It&#8217;s been a while (12 years <img alt="😵" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f635.png" style="height: 1em;" />) since I  <a href="https://anitagraser.com/2012/03/30/qgis-server-on-ubuntu-step-by-step/">last posted about QGIS Server</a>. It would be an understatement to say that things have evolved since then, not least due to the development of Docker which, <a href="https://en.wikipedia.org/wiki/Docker_(software)">Wikipedia tells me</a>, was released 11 years ago. </p>



<p>There have been multiple Docker images for QGIS Server provided by QGIS Community members over the years. Recently, OPENGIS.ch&#8217;s Docker image has been adopted as official QGIS Server image <a href="https://github.com/qgis/qgis-docker">https://github.com/qgis/qgis-docker</a> which aims to be a starting point for users to develop their own customized applications.</p>



<p>The following steps have been tested on Ubuntu (both native and in WSL). </p>



<p>First, we need Docker. I installed Docker from the apt repository <a href="https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository">as described in the official docs</a>. </p>



<p>Once Docker is set up, we can get the QGIS Server, e.g. for the LTR: </p>



<pre class="wp-block-code"><code>docker pull qgis/qgis-server:ltr</code></pre>



<p>Now we only need to start it:</p>



<pre class="wp-block-code"><code>docker run -v $(pwd)/qgis-server-data:/io/data --name qgis-server -d -p 8010:80 qgis/qgis-server:ltr</code></pre>



<p>Note how we are mapping the qgis-server-data directory in our current working directory to /io/data in the container. This is where we&#8217;ll put our QGIS project files.</p>



<p>We can already check out the OGC API landing page at <a href="http://localhost:8010/wfs3/" rel="nofollow">http://localhost:8010/wfs3/</a></p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8858" height="375" src="https://underdark.files.wordpress.com/2024/04/image-1.png?w=395" width="395" /></figure>



<p>Let’s add a sample project from the <a href="https://github.com/qgis/QGIS-Training-Data/">Training demo data</a> repo. (You may need to install unzip if you haven&#8217;t yet.)</p>



<pre class="wp-block-code" id="codecell3"><code>mkdir qgis-server-data
cd qgis-server-data
wget https://github.com/qgis/QGIS-Training-Data/archive/release_3.22.zip
unzip release_3.22.zip
mkdir world
cp QGIS-Training-Data-release_3.22/exercise_data/qgis-server-tutorial-data/world.qgs world/
cp QGIS-Training-Data-release_3.22/exercise_data/qgis-server-tutorial-data/naturalearth.sqlite world</code></pre>



<p>Giving us:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8860" height="119" src="https://underdark.files.wordpress.com/2024/04/image-2.png?w=538" width="538" /></figure>



<p>QGIS Server should now be serving this sample project. Let&#8217;s check with a WMS GetMap request:</p>



<p><a href="http://localhost:8010/ogc/world?LAYERS=countries&#038;SERVICE=WMS&#038;VERSION=1.3.0&#038;REQUEST=GetMap&#038;CRS=EPSG:4326&#038;WIDTH=400&#038;HEIGHT=200&#038;BBOX=-90,-180,90,180" rel="nofollow">http://localhost:8010/ogc/world?LAYERS=countries&#038;SERVICE=WMS&#038;VERSION=1.3.0&#038;REQUEST=GetMap&#038;CRS=EPSG:4326&#038;WIDTH=400&#038;HEIGHT=200&#038;BBOX=-90,-180,90,180</a></p>



<p>Giving us: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8861" height="200" src="https://underdark.files.wordpress.com/2024/04/image-3.png?w=400" width="400" /></figure>



<p><em>If you instead get the error &#8220;&lt;ServerException&gt;Project file error. For OWS services: please provide a SERVICE and a MAP parameter pointing to a valid QGIS project file&lt;/ServerException&gt;&#8221;, it probably means that the world.qgs file is not found in the qgis-server-data/world directory. </em></p>



<p>Of course, we can also add <a href="http://localhost:8010/ogc/world">http://localhost:8010/ogc/world</a> to the WMS and WFS server connections in our QGIS Desktop: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2024/04/image-4.png"><img alt="" class="wp-image-8863" height="600" src="https://underdark.files.wordpress.com/2024/04/image-4.png?w=1024" width="1024" /></a></figure>
