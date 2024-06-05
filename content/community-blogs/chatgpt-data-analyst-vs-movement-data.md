---
source: "blog"
title: "anitagraser.com: ChatGPT Data Analyst vs movement data"
image: "chatgpt-data-analyst-vs-movement-data."
date: "2024-05-30"
link: "https://anitagraser.com/2024/05/30/chatgpt-data-analyst-vs-movement-data/"
draft: "true"
showcase: "planet"
---

<p>Today, I took <a href="https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt">ChatGPT&#8217;s Data Analyst</a> for a spin. You&#8217;ve probably seen the fancy advertising videos: just drop in a dataset and AI does all the analysis for you?! Let&#8217;s see &#8230;</p>



<p>Of course, I&#8217;m not going to use some lame movie database or flower petals data. Instead, let&#8217;s go all in and test with a <a href="https://github.com/movingpandas/movingpandas/blob/main/tutorials/data/demodata_geolife.csv">movement dataset</a>. </p>



<p>You don&#8217;t get a second chance to make a first impression, they say. &#8212; Well, Data Analyst, you didn&#8217;t impress on the first try. How hard can it be to guess the delimiter and act accordingly?  </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-28.png"><img alt="" class="wp-image-9010" height="653" src="https://anitagraser.com/wp-content/uploads/2024/05/image-28.png?w=663" width="663" /></a></figure>



<p>Anyway, let&#8217;s help it a little:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-29.png"><img alt="" class="wp-image-9011" height="657" src="https://anitagraser.com/wp-content/uploads/2024/05/image-29.png?w=663" width="663" /></a></figure>



<p>That looks much better. It makes an effort to guess what the columns could mean and successfully identifies the spatiotemporal information. </p>



<p>Now for some spatial analysis. On first try, it didn&#8217;t want to calculate the length of the trajectories in geographic terms, but we can make it to: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-30.png"><img alt="" class="wp-image-9012" height="736" src="https://anitagraser.com/wp-content/uploads/2024/05/image-30.png?w=664" width="664" /></a></figure>



<p>It will also show the code used to get to the results:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-31.png"><img alt="" class="wp-image-9013" height="688" src="https://anitagraser.com/wp-content/uploads/2024/05/image-31.png?w=550" width="550" /></a></figure>



<p>And indeed, these are close enough to the results computed using MovingPandas:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8997" height="111" src="https://anitagraser.com/wp-content/uploads/2024/05/image-24.png?w=788" width="788" /></figure>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-23.png"><img alt="" class="wp-image-8995" height="272" src="https://anitagraser.com/wp-content/uploads/2024/05/image-23.png?w=915" width="915" /></a></figure>



<p>&#8220;What about plots?&#8221; I hear you ask.</p>



<p>For a first try, not bad at all: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-32.png"><img alt="" class="wp-image-9014" height="500" src="https://anitagraser.com/wp-content/uploads/2024/05/image-32.png?w=665" width="665" /></a></figure>



<p>Let&#8217;s see if we can push it further:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-33.png"><img alt="" class="wp-image-9015" height="512" src="https://anitagraser.com/wp-content/uploads/2024/05/image-33.png?w=666" width="666" /></a></figure>



<p>Looks like poor Data Analyst ended up in geospatial library dependency hell <img alt="😈" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f608.png" style="height: 1em;" /></p>



<p>It&#8217;s interesting to watch it try find a solution. </p>



<p>Alas, no background map appears:  </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-34.png"><img alt="" class="wp-image-9016" height="707" src="https://anitagraser.com/wp-content/uploads/2024/05/image-34.png?w=666" width="666" /></a></figure>



<p>Not giving up yet :)</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-35.png"><img alt="" class="wp-image-9017" height="536" src="https://anitagraser.com/wp-content/uploads/2024/05/image-35.png?w=667" width="667" /></a></figure>



<p>Woah, what happened here? It claims it created an interactive map in an HTML file. </p>



<p>And indeed it did: </p>



<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2024/05/image-27.png"><img alt="" class="wp-image-9002" height="664" src="https://anitagraser.com/wp-content/uploads/2024/05/image-27.png?w=780" style="width: 775px; height: auto;" width="780" /></a></figure>



<p>This has been a very interesting experiment for me with many highs and lows. The whole process is a bit hit and miss. But when it does work, it&#8217;s fun. </p>



<p>I wasn&#8217;t sure what to expect with regards to Data Analyst&#8217;s spatial data processing capabilities. Looks like there are enough examples in its training data to find solutions for the basic trajectory analysis problems I asked it solve today, eventually, at least. </p>



<p>What&#8217;s the conclusion? Most AI marketing videos are severely overselling the capabilities of these tools. However, that doesn&#8217;t mean that they are completely useless, either. I&#8217;m looking forward to seeing the age of smaller open source models specifically trained for geospatial analysis to finally make it unnecessary for humans to memorize data analysis library syntax. </p>
