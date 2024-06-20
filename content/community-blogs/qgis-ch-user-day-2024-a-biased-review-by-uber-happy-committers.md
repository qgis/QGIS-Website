---
source: "blog"
title: "OPENGIS.ch blog: QGIS.ch user-day 2024 – A biased review by uber-happy committers"
image: "qgis-ch-user-day-2024-a-biased-review-by-uber-happy-committers."
date: "2024-06-19"
link: "https://www.opengis.ch/2024/06/20/qgis-ch-user-day-2024-a-biased-review-by-uber-happy-committers/"
draft: "true"
showcase: "planet"
---

<p>During the pandemic, people noticed how well they could work remotely, how productive meetings via video call could be, and how well webinars worked. At OPENGIS.ch, this wasn&#8217;t news because we have always been 100% remote. However, we missed the unplanned, in-person interactions that occur during meetups with a <img alt="🍺" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f37a.png" style="height: 1em;" />or <img alt="☕" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/2615.png" style="height: 1em;" />. That&#8217;s why we&#8217;re very pleased that last week we could join the Swiss QGIS user day for the second time after the pandemic.</p>



<p>OPENGIS.ch has been invested in QGIS since its inception in 2014, actually even before; our CEO Marco started working with QGIS 0.6 in 2004 and our CTO Matthias with version 1.7 in 2012. We definitely can say that OPENGIS.ch has been one of the main driving forces behind the large adoption of QGIS in Switzerland and worldwide.&nbsp;</p>



<figure class="wp-block-image size-large is-resized is-style-default"><img alt="" class="wp-image-14568" height="422" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/contrib.png?resize=750%2C422&#038;ssl=1" style="width: 840px; height: auto;" width="750" /><figcaption class="wp-element-caption">Contributions to the QGIS core measured in commit numbers</figcaption></figure>



<p>Looking at the work done in the QGIS code we’re by far the most prolific company in Switzerland and second worldwide only to North Road Consulting. On top of it, we were the first &#8211; and still only one of two- companies to <a href="https://qgis.org/en/site/about/sustaining_members.html" rel="noreferrer noopener" target="_blank">sustain QGIS.org at a Large level</a> since 2021.</p>



<p>This makes us very proud and it is why we’re even happier to see how much that is happening around QGIS in Switzerland aligns with the visions and goals we set out to reach years ago.</p>



<p>The morning started with a presentation by our CTO Matthias “What’s new in QGIS” featuring plenty of work sponsored by the Anwendergruppe CH.</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14562" height="563" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/IMG_20240611_085925.jpg?resize=750%2C563&#038;ssl=1" width="750" /><figcaption class="wp-element-caption">Our CTO Matthias answering QGIS questions</figcaption></figure>



<p>DXF Improvements, the release of SwissLocator 3.0 with swissalti3d and vector tiles integration, and an update on the advances towards solid curve handling in QGIS, a prerequisite for properly handling AV data in Switzerland, were only some of the many noteworthy points he touched.</p>



<p>The highlight of Matthias’ presentation was the better OGC API Features support in QGIS, which was also highlighted in a subsequent talk about Kablo, showing how the next generation of industry solutions (Fachschalen) will be implemented.</p>



<pre class="wp-block-code"><code>Slides: <a href="https://docs.google.com/presentation/d/1ITN71d_Otv3e0DH63Muod9kpdE1FMd-wRmSPUVO-1Yg/edit?usp=sharing" rel="noreferrer noopener" target="_blank">Neues aus der QGIS Welt - QGIS Anwendertag 2024</a></code></pre>



<p>Following was a short presentation on the project DMAV, Christoph Lauber introduced a project that aims to implement an industry solution for official cadastral surveying with QGIS.</p>



<p>Adrian Wicki of the Federal Office for the Environment (FOEN) and Isabel presented how OPENGIS.ch and the partners Puzzle and Zeilenwerk help the FOEN with the SAM project with assess the hazards of flood, forest fire, or landslides, and warn authorities and the population. With an agile project organisation, the complex project succeeds in fulfilling requirements by applying user-centred development concepts. QGIS is used for visualizing and analyzing data and helping forecasters gain insights into the current situation.</p>



<pre class="wp-block-code"><code>Slides: <a href="https://docs.google.com/presentation/d/18bGeUzrVw7g58VxKrdLuAhTVt-BEYMpTvIDVTp4ZMJY/edit?usp=sharing" rel="noreferrer noopener" target="_blank">BAFU_SAM</a></code></pre>



<p>Andreas Neumann from ETH Zurich and Michael presented the <a href="https://github.com/qgis/qgis-js" rel="noreferrer noopener" target="_blank">qgis-js project</a>. QGIS-js is an effort to port QGIS core to WebAssembly so that it can be run in a web browser. Although still in the early experimentation phase, this project has great potential to leverage interesting new use cases that weren’t even thinkable before.</p>



<pre class="wp-block-code"><code>Slides: <a href="https://boardend.github.io/qgis-js-demo/">https://boardend.github.io/qgis-js-demo/</a>&nbsp;</code></pre>



<p>Olivier Monod from the City of Yverdon presented <a href="https://kablo.ch/" rel="noreferrer noopener" target="_blank">Kablo</a>, an electricity management proof of concept of the next generation implementation for industry solutions developed in collaboration with OPENGIS.ch.</p>



<p>By applying a middleware based on OGC API Features and Django, Kablo shows how common limitations of current industry solutions (like permission management and atomic operations) can be overcome and how the future brings desktop and web closer together.</p>



<pre class="wp-block-code"><code>Slides: <a href="https://docs.google.com/presentation/d/1PQx48mr33cJcppWhoswofSj0zxGpHmncsjj24OtUCtI/edit?usp=sharing" rel="noreferrer noopener" target="_blank">kablo-qgis-user-days</a></code></pre>



<p>Obviously, it wasn’t just OPENGIS.ch. Sandro Mani from Sourcepole presented the latest and greatest improvements on <a href="https://github.com/qgis/qwc2" rel="noreferrer noopener" target="_blank">QWC2</a>, like street view integration and cool QGIS features brought to a beautiful web gis. Andreas Schmid from Kt. Solothurn presented how cool cloud-optimized geotiff (COG) is and what challenges come with it. Interested in the topic? Read more in our <a href="https://www.opengis.ch/de/2024/04/09/cloud-optimized-geospatial-formats/" rel="noreferrer noopener" target="_blank">report about cloud optimized formats</a>. Mattia Panduri from Canton Ticino explained how they used QGIS to harmonise the cantonal building datasets and Timothée Produit from IG Group SA presented how pic2map helps bring photos to maps.&nbsp;</p>



<p>To round up the morning, Nyall Dawson from North Road Consulting did a live session around the world to show the latest developments around elevation filtering in QGIS.</p>



<p>In the afternoon, workshops followed. Claas Leiner led a QGIS expression one while Matthias and Michael showed how to leverage QGIS processing for building geospatial data processing workflows.&nbsp;</p>



<p>The first <a href="https://modelbaker.ch/" rel="noreferrer noopener" target="_blank">QGIS model baker </a>user meeting took place in the third room. The participants discussed this fantastic tool we developed to make INTERLIS work smarter and more productive.</p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-14559" height="563" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/1000050805.jpg?resize=750%2C563&#038;ssl=1" width="750" /><figcaption class="wp-element-caption">First ModelBaker user meeting</figcaption></figure>



<p>It was a very rich and constructive QGIS user day. We came home with plenty of new ideas and a sense of fulfilment, seeing how great the community we observed and helped grow has become.</p>



<p>A big thanks go to the organisers and everyone involved in making such a great event happen. Only the beer in the sunshine was literally watered by the rain. Nevertheless, there were exciting discussions in the station bistro or in the restaurant coaches on the way home.</p>



<p>See you next time and keep contributing <img alt="🙂" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f642.png" style="height: 1em;" /></p>
