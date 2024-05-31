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



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8989" height="716" src="https://anitagraser.com/wp-content/uploads/2024/05/image-19.png?w=817" width="817" /></figure>



<p>Anyway, let&#8217;s help it a little:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8987" height="726" src="https://anitagraser.com/wp-content/uploads/2024/05/image-18.png?w=808" width="808" /></figure>



<p>That looks much better. It makes an effort to guess what the columns could mean and successfully identifies the spatiotemporal information. </p>



<p>Now for some spatial analysis. On first try, it didn&#8217;t want to calculate the length of the trajectories in geographic terms, but we can make it to: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8986" height="770" src="https://anitagraser.com/wp-content/uploads/2024/05/image-17.png?w=814" width="814" /></figure>



<p>It will also show the code use to get to the results: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8984" height="840" src="https://anitagraser.com/wp-content/uploads/2024/05/image-16.png?w=812" width="812" /></figure>



<p>And indeed, these are close enough to the results computed using MovingPandas:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8997" height="111" src="https://anitagraser.com/wp-content/uploads/2024/05/image-24.png?w=788" width="788" /></figure>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8995" height="272" src="https://anitagraser.com/wp-content/uploads/2024/05/image-23.png?w=915" width="915" /></figure>



<p>&#8220;What about plots?&#8221; I hear you ask.</p>



<p>For a first try, not bad at all: </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8990" height="538" src="https://anitagraser.com/wp-content/uploads/2024/05/image-20.png?w=806" width="806" /></figure>



<p>Let&#8217;s see if we can push it further:</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8999" height="516" src="https://anitagraser.com/wp-content/uploads/2024/05/image-25.png?w=809" width="809" /></figure>



<p>Looks like poor Data Analyst ended up in geospatial library dependency hell <img alt="😈" class="wp-smiley" src="https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f608.png" style="height: 1em;" /></p>



<p>It&#8217;s interesting to watch it try find a solution. </p>



<p>Alas, no background map appears:  </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-8993" height="710" src="https://anitagraser.com/wp-content/uploads/2024/05/image-22.png?w=821" width="821" /></figure>



<p>Not giving up yet :)</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-9001" height="542" src="https://anitagraser.com/wp-content/uploads/2024/05/image-26.png?w=819" width="819" /></figure>



<p>Woah, what happened here? It claims it created an interactive map in an HTML file. </p>



<p>And indeed it did: </p>



<figure class="wp-block-image size-large is-resized"><img alt="" class="wp-image-9002" height="664" src="https://anitagraser.com/wp-content/uploads/2024/05/image-27.png?w=780" style="width: 775px; height: auto;" width="780" /></figure>



<p>This has been a very interesting experiment for me with many highs and lows. The whole process is a bit hit and miss. But when it does work, it&#8217;s fun. </p>



<p>I wasn&#8217;t sure what to expect with regards to Data Analyst&#8217;s spatial data processing capabilities. Looks like there are enough examples in its training data to find solutions for the basic trajectory analysis problems I asked it solve today, eventually, at least. </p>



<p>What&#8217;s the conclusion? Most AI marketing videos are severely overselling the capabilities of these tools. However, that doesn&#8217;t mean that they are completely useless, either. I&#8217;m looking forward to seeing the age of smaller open source models specifically trained for geospatial analysis to finally make it unnecessary for humans to memorize data analysis library syntax. </p>
