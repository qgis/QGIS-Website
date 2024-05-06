---
source: "blog"
title: "anitagraser.com: Getting started with pygeoapi processes"
image: "getting-started-with-pygeoapi-processes."
date: "2024-03-18"
link: "https://anitagraser.com/2024/03/18/getting-started-with-pygeoapi-processes/"
draft: "true"
showcase: "planet"
---

<p>Today&#8217;s post is a quick introduction to <a href="https://pygeoapi.io">pygeoapi</a>, a Python server implementation of the <a href="https://ogcapi.ogc.org/">OGC API suite of standards</a>. OGC API provides many different standards but I&#8217;m particularly interested in <a href="https://ogcapi.ogc.org/processes">OGC API &#8211; Processes</a> which standardizes geospatial data processing functionality. pygeoapi implements this standard by providing a plugin architecture, thereby allowing developers to implement custom processing workflows in Python.</p>



<p>I&#8217;ll provide instructions for setting up and running pygeoapi on Windows using Powershell. The <a href="https://docs.pygeoapi.io/en/stable/installation.html">official docs</a> show how to do this on Linux systems. The <a href="https://pygeoapi.io">pygeoapi</a> homepage prominently features instructions for installing the dev version. For first experiments, however, I&#8217;d recommend using a release version instead. So that&#8217;s what we&#8217;ll do here. </p>



<p>As a first step, lets install the latest release (0.16.1 at the time of writing) from <a href="https://github.com/geopython/pygeoapi/releases">conda-forge</a>:</p>



<pre class="wp-block-code"><code>conda create -n pygeoapi python=3.10<br />conda activate pygeoapi<br />mamba install -c conda-forge pygeoapi</code></pre>



<p>Next, we&#8217;ll clone <a href="https://github.com/geopython/pygeoapi">the GitHub repo</a> to get the example config and datasets:</p>



<pre class="wp-block-code"><code>cd C:\Users\anita\Documents\GitHub\<br />git clone https://github.com/geopython/pygeoapi.git<br />cd pygeoapi\</code></pre>



<p>To finish the setup, we need some configurations:</p>



<pre class="wp-block-code"><code>cp pygeoapi-config.yml example-config.yml  <br /># There is a known issue in pygeoapi 0.16.1: https://github.com/geopython/pygeoapi/issues/1597<br /># To fix it, edit the example-config.yml: uncomment the TinyDB option in the server settings (lines 51-54)<br /><br />$Env:PYGEOAPI_CONFIG = "F:/Documents/GitHub/pygeoapi/example-config.yml"<br />$Env:PYGEOAPI_OPENAPI = "F:/Documents/GitHub/pygeoapi/example-openapi.yml"<br />pygeoapi openapi generate $Env:PYGEOAPI_CONFIG --output-file $Env:PYGEOAPI_OPENAPI</code></pre>



<p>Now we can start the server:</p>



<pre class="wp-block-code"><code>pygeoapi serve</code></pre>



<p>And once the server is running, we can send requests, e.g. the list of processes:</p>



<pre class="wp-block-code"><code>curl.exe http://localhost:5000/processes</code></pre>



<p>And, of course, execute the example &#8220;hello-world&#8221; process:</p>



<pre class="wp-block-code"><code>curl.exe --% -X POST http://localhost:5000/processes/hello-world/execution -H "Content-Type: application/json" -d "{\"inputs\":{\"name\": \"hi there\"}}"</code></pre>



<p>As you can see, writing JSON content for curl is a pain. Luckily, pyopenapi comes with a nice web GUI, including Swagger UI for playing with all the functionality, including the hello-world process: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8840" height="455" src="https://underdark.files.wordpress.com/2024/03/image.png?w=584" width="584" /></figure>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8841" height="634" src="https://underdark.files.wordpress.com/2024/03/image-1.png?w=584" width="584" /></figure>



<p>It&#8217;s not really a geospatial hello-world example, but it&#8217;s a first step. </p>



<p>Finally, I wan&#8217;t to leave you with a teaser since there are more interesting things going on in this space, including work on OGC API &#8211; Moving Features as <a href="https://noc.social/@pygeoapi/112013706668052981">shared by the pygeoapi team recently</a>:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8847" height="325" src="https://underdark.files.wordpress.com/2024/03/image-3.png?w=311" width="311" /></figure>



<p>So, stay tuned. </p>
