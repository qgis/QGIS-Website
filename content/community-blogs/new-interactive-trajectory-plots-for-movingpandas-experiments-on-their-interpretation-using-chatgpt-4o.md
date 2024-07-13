---
source: "blog"
title: "anitagraser.com: New interactive trajectory plots for MovingPandas & experiments on their interpretation using ChatGPT 4o"
image: "new-interactive-trajectory-plots-for-movingpandas-experiments-on-their-interpretation-using-chatgpt-4o."
date: "2024-06-30"
link: "https://anitagraser.com/2024/06/30/new-interactive-trajectory-plots-for-movingpandas-experiments-on-their-interpretation-using-chatgpt-4o/"
draft: "true"
showcase: "planet"
---

<figure class="wp-block-image size-large"><img alt="" class="wp-image-9114" height="131" src="https://anitagraser.com/wp-content/uploads/2024/07/movingpandas-1.png?w=545" tabindex="0" width="545" /></figure>



<p>With the release of GeoPandas 1.0 this month, we&#8217;ve been finally able to close a long-standing issue in MovingPandas by <strong><a href="https://github.com/movingpandas/movingpandas/commit/bd13a62aec2ea8eb6f9bde144dcb2ed2818905ef">adding support for the explore function</a></strong> which provides interactive maps using Folium and Leaflet. </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-9027" height="636" src="https://anitagraser.com/wp-content/uploads/2024/06/mpd-explore.gif?w=936" tabindex="0" width="936" /></figure>



<p>Explore() will be available in the upcoming MovingPandas 0.19 release if your Python environment includes GeoPandas &gt;= 1.0 and Folium. Of course, if you are curious, you can already test this new functionality using the current development version.</p>



<p>This enables users to access interactive trajectory plots even in environments where it is not possible to install geoviews / hvplot (the previously only option for interactive plots in MovingPandas). </p>



<p>I really like the legend for the speed color gradient, but unfortunately, the legend labels are not readable on the dark background map since they lack the semi-transparent white background that has been applied to the scale bar and credits label. </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/06/image.png"><img alt="" class="wp-image-9031" height="638" src="https://anitagraser.com/wp-content/uploads/2024/06/image.png?w=936" tabindex="0" width="936" /></a></figure>



<p>Speaking of reading / interpreting the plots &#8230;</p>



<p>You&#8217;ve probably seen the claims that AI will help make tools more accessible. Clearly AI can interpret and describe photos, but can it also interpret MovingPandas plots? </p>



<h2 class="wp-block-heading">ChatGPT 4o interpretations of MovingPandas plots</h2>



<figure class="wp-block-image size-full"><a href="https://anitagraser.com/wp-content/uploads/2024/06/image-2.png"><img alt="" class="wp-image-9034" src="https://anitagraser.com/wp-content/uploads/2024/06/image-2.png" tabindex="0" /></a></figure>



<p>Not bad. </p>



<p>And what happens if we ask it to interpret the animated GIF from the beginning of the blog post? </p>



<figure class="wp-block-image size-full"><a href="https://anitagraser.com/wp-content/uploads/2024/06/image-4.png"><img alt="" class="wp-image-9038" src="https://anitagraser.com/wp-content/uploads/2024/06/image-4.png" tabindex="0" /></a></figure>



<p>So it looks like ChatGPT extracts 12 frames and analyzes them to answer our question: </p>



<figure class="wp-block-image size-full"><a href="https://anitagraser.com/wp-content/uploads/2024/06/image-5.png"><img alt="" class="wp-image-9039" src="https://anitagraser.com/wp-content/uploads/2024/06/image-5.png" tabindex="0" /></a></figure>



<p>Its guesses are not completely off but it made up the facts such as that the view shows &#8220;how traffic speeds vary over time&#8221;.</p>



<p>The problem remains that models such as ChatGPT rather make up interpretations than concede when they do not have enough information to make a reliable statement. </p>
