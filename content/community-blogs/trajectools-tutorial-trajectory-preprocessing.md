---
source: "blog"
title: "anitagraser.com: Trajectools tutorial: trajectory preprocessing"
image: "trajectools-tutorial-trajectory-preprocessing."
date: "2024-09-21"
link: "https://anitagraser.com/2024/09/21/trajectools-tutorial-trajectory-preprocessing/"
draft: "true"
showcase: "planet"
---

<figure class="wp-block-image size-large"><img alt="" class="wp-image-9007" height="131" src="https://anitagraser.com/wp-content/uploads/2024/05/trajectools2.png?w=545" tabindex="0" width="545" /></figure>



<p>Today marks the release of <a href="https://plugins.qgis.org/plugins/processing_trajectory/#plugin-versions">Trajectools 2.3</a> which brings a new set of algorithms, including trajectory generalizing, cleaning, and smoothing. </p>



<p>To give you a quick impression of what some of these algorithms would be useful for, this post introduces a trajectory preprocessing workflow that is quite general-purpose and can be adapted to many different datasets. </p>



<p>We start out with the Geolife sample dataset which you can find in the Trajectools plugin directory&#8217;s sample_data subdirectory. This small dataset includes 5908 points forming 5 trajectories, based on the trajectory_id field:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-2.png"><img alt="" class="wp-image-9208" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-2.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>We first split our trajectories by observation gaps to ensure that there are no large gaps in our trajectories. Let&#8217;s make at cut at 15 minutes: </p>



<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-1.png"><img alt="" class="wp-image-9206" height="645" src="https://anitagraser.com/wp-content/uploads/2024/09/image-1.png?w=729" style="width: 840px; height: auto;" tabindex="0" width="729" /></a></figure>



<p>This splits the original 5 trajectories into 11 trajectories: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-3.png"><img alt="" class="wp-image-9209" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-3.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>When we zoom, for example, to the two trajectories in the north western corner, we can see that the trajectories are pretty noisy and there&#8217;s even a spike / outlier at the western end: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-4.png"><img alt="" class="wp-image-9211" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-4.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>If we label the points with the corresponding speeds, we can see how unrealistic they are: over 300 km/h!</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-5.png"><img alt="" class="wp-image-9213" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-5.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>Let&#8217;s remove outliers over 50 km/h:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-6.png"><img alt="" class="wp-image-9215" height="645" src="https://anitagraser.com/wp-content/uploads/2024/09/image-6.png?w=729" tabindex="0" width="729" /></a></figure>



<p>Better but not perfect: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-7.png"><img alt="" class="wp-image-9217" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-7.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>Let&#8217;s smooth the trajectories to get rid of more of the jittering. </p>



<p>(You&#8217;ll need to pip/mamba install the optional stonesoup library to get access to this algorithm.)</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-8.png"><img alt="" class="wp-image-9219" height="645" src="https://anitagraser.com/wp-content/uploads/2024/09/image-8.png?w=729" tabindex="0" width="729" /></a></figure>



<p>Depending on the noise values we chose, we get more or less smoothing: </p>



<figure class="wp-block-image size-large is-resized"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-10.png"><img alt="" class="wp-image-9223" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-10.png?w=1024" style="width: 840px; height: auto;" tabindex="0" width="1024" /></a></figure>



<p>Let&#8217;s zoom out to see the whole trajectory again: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-11.png"><img alt="" class="wp-image-9225" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-11.png?w=1024" tabindex="0" width="1024" /></a></figure>



<p>Feel free to pan around and check how our preprocessing affected the other trajectories, for example: </p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-14.png"><img alt="" class="wp-image-9229" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-14.png?w=1024" tabindex="0" width="1024" /></a></figure>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/09/image-13.png"><img alt="" class="wp-image-9228" height="611" src="https://anitagraser.com/wp-content/uploads/2024/09/image-13.png?w=1024" tabindex="0" width="1024" /></a></figure>
