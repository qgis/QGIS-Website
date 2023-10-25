---
source: "blog"
title: "OPENGIS.ch blog: Analyzing and visualizing large-scale fire events using QGIS processing with ST-DBSCAN"
image: "analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan."
date: "2023-09-05"
link: "https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/"
draft: "true"
showcase: "planet"
---

<p>A while back, one of our ninjas added a <strong>new algorithm in QGIS</strong>’ processing toolbox named ST-DBSCAN Clustering, short for <strong>spatio temporal density-based spatial clustering of applications with noise</strong>. The algorithm regroups features falling within a user-defined maximum distance and time duration values.</p>



<p>This post will walk you through one practical use for the algorithm: large-scale fire event analysis and visualization through remote-sensed fire detection. More specifically, we will be looking into one of the larger fire events which occurred in Canada’s Quebec province in June 2023.</p>



<figure class="wp-block-image size-full"><img decoding="async" width="750" height="645" data-attachment-id="13888" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/fires_cover/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?fit=1021%2C878&amp;ssl=1" data-orig-size="1021,878" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="fires_cover" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?fit=300%2C258&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?fit=750%2C645&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?resize=750%2C645&#038;ssl=1" alt="" class="wp-image-13888" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?w=1021&amp;ssl=1 1021w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?resize=300%2C258&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fires_cover.png?resize=768%2C660&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<h2 class="wp-block-heading">Fetching and preparing FIRMS data</h2>



<p>NASA’s <a href="https://firms.modaps.eosdis.nasa.gov/">Fire Information for Resource Management System (<strong>FIRMS</strong>)</a> offers a fantastic worldwide archive of all fire detected through three spaceborne sources: MODIS C6.1 with a resolution of roughly 1 kilometer as well as VIIRS S-NPP and VIIRS NOAA-20 with a resolution of 375 meters. Each detected fire is represented by a point that sits at the center of the source’s resolution grid.</p>



<p>Each source will cover the whole world several times per day. Since detection is impacted by atmospheric conditions, a given pass by one source might not be able to register an ongoing fire event. It’s therefore advisable to rely on more than one source.</p>



<p>To look into our fire event, we have chosen the two fire detection sources with higher resolution &#8211; VIIRS S-NPP and VIIRS NOAA-20 – covering the whole month of June 2023. The datasets were downloaded from <a href="https://firms.modaps.eosdis.nasa.gov/download/">FIRMS’ archive download page</a>.</p>



<p>After downloading the two separate datasets, we combined them into one merged geopackage dataset using QGIS processing toolbox’s <strong>Merge Vector Layers algorithm</strong>. The merged dataset will be used to conduct the <strong>clustering analysis</strong>.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" width="619" height="520" data-attachment-id="13881" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/merge/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?fit=619%2C520&amp;ssl=1" data-orig-size="619,520" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="merge" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?fit=300%2C252&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?fit=619%2C520&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?resize=619%2C520&#038;ssl=1" alt="" class="wp-image-13881" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?w=619&amp;ssl=1 619w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/merge.png?resize=300%2C252&amp;ssl=1 300w" sizes="(max-width: 619px) 100vw, 619px" data-recalc-dims="1" /></figure></div>


<p>In addition, we will use QGIS’s field calculator to create a new Date &amp; Time field named ACQ_DATE_TIME using the following expression:</p>



<pre class="wp-block-code"><code><code>to_datetime("ACQ_DATE" || "ACQ_TIME", 'yyyy-MM-ddhhmm')</code></code></pre>



<p>This will allow us to calculate precise time differences between two dates.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" loading="lazy" width="750" height="674" data-attachment-id="13882" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/fieldcalculator-2/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?fit=786%2C706&amp;ssl=1" data-orig-size="786,706" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="fieldcalculator" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?fit=300%2C269&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?fit=750%2C674&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?resize=750%2C674&#038;ssl=1" alt="" class="wp-image-13882" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?w=786&amp;ssl=1 786w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?resize=300%2C269&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/fieldcalculator.png?resize=768%2C690&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure></div>


<h2 class="wp-block-heading">Modeling and running the analysis</h2>



<p>The large-scale fire event analysis requires running two distinct algorithms:</p>



<ul>
<li>a <strong>spatiotemporal clustering of points</strong> to regroup fires into a series of events confined in space and time; and</li>



<li>an <strong>aggregation of the points within the identified clusters</strong> to provide additional information such as the beginning and end date of regrouped events.</li>
</ul>



<p>This can be achieved through QGIS’ modeler to sequentially execute the <a href="https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html#st-dbscan-clustering">ST-DBSCAN Clustering algorithm</a> as well as the <a href="https://docs.qgis.org/3.28/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html#aggregate">Aggregate algorithm</a> against the output of the first algorithm.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" loading="lazy" width="629" height="745" data-attachment-id="13883" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/model/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?fit=629%2C745&amp;ssl=1" data-orig-size="629,745" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="model" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?fit=253%2C300&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?fit=629%2C745&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?resize=629%2C745&#038;ssl=1" alt="" class="wp-image-13883" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?w=629&amp;ssl=1 629w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/model.png?resize=253%2C300&amp;ssl=1 253w" sizes="(max-width: 629px) 100vw, 629px" data-recalc-dims="1" /></figure></div>


<p>The above-pictured model outputs two datasets. The first dataset contains single-part points of detected fires with attributes from the original VIIRS products as well as a pair of new attributes: the CLUSTER_ID provides a unique cluster identifier for each point, and the CLUSTER_SIZE represents the sum of points forming each unique cluster. The second dataset contains multi-part points clusters representing fire events with four attributes: CLUSTER_ID and CLUSTER_SIZE which were discussed above as well as DATE_START and DATE_END to identify the beginning and end time of a fire event.</p>



<p>In our specific example, we will run the model using the merged dataset we created above as the “fire points layer” and select ACQ_DATE_TIME as the “date field”. The outputs will be saved as separate layers within a geopackage file.</p>



<p><em>Note that the maximum distance (0.025 degrees) and duration (72 hours) settings to form clusters have been set in the model itself. This can be tweaked by editing the model.</em></p>



<h2 class="wp-block-heading">Visualizing a specific fire event progression on a map</h2>



<p>Once the model has provided its outputs, we are ready to start <strong>visualizing a fire event on a map</strong>. In this practical example, we will focus on detected fires around latitude 53.0960 and longitude -75.3395.</p>



<p>Using the multi-part points dataset, we can identify two clustered events (CLUSTER_ID 109 and 1285) within the month of June 2023. To help map canvas refresh responsiveness, we can filter both of our output layers to only show features with those two cluster identifiers using the following SQL syntax: CLUSTER_ID IN (109, 1285).</p>



<p>To show the <strong>progression of the fire event over time</strong>, we can use a data-defined property to graduate the marker fill of the single-part points dataset along a color ramp. To do so, open the layer’s styling panel, select the simple marker symbol layer, click on the data-defined property button next to the fill color and pick the Assistant menu item.</p>



<p>In the assistant panel, set the source expression to the following: <code>day(age(to_date('2023-07-01'),”ACQ_DATE_TIME”))</code>. This will give us the number of days between a given point and an arbitrary reference date (2023-07-01 here). Set the values range from 0 to 30 and pick a color ramp of your choice.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" loading="lazy" width="631" height="661" data-attachment-id="13884" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/styling/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?fit=631%2C661&amp;ssl=1" data-orig-size="631,661" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="styling" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?fit=286%2C300&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?fit=631%2C661&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?resize=631%2C661&#038;ssl=1" alt="" class="wp-image-13884" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?w=631&amp;ssl=1 631w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/styling.png?resize=286%2C300&amp;ssl=1 286w" sizes="(max-width: 631px) 100vw, 631px" data-recalc-dims="1" /></figure></div>


<p>When applying this style, the resulting map will provide a visual representation of the spread of the fire event over time.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" loading="lazy" width="750" height="562" data-attachment-id="13885" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/attachment/96/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?fit=755%2C566&amp;ssl=1" data-orig-size="755,566" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="96" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?fit=300%2C225&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?fit=750%2C562&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?resize=750%2C562&#038;ssl=1" alt="" class="wp-image-13885" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?w=755&amp;ssl=1 755w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/96.png?resize=300%2C225&amp;ssl=1 300w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /><figcaption class="wp-element-caption">Having identified a fire event via clustering easily allows for identification of the “starting point” of a fire by searching for the earliest fire detected amongst the thousands of points. This crucial bit of analysis can help better understand the cause of the fire, and alongside the color grading of neighboring points, its directionality as it expanded over time.</figcaption></figure></div>


<h2 class="wp-block-heading">Analyzing a fire event through histogram</h2>



<p>Through <a href="https://github.com/ghtmtt/DataPlotly#readme">QGIS’ DataPlotly plugin</a>, it is possible to <strong>create an histogram of fire events</strong>. After installing the plugin, we can open the DataPlotly panel and configure our histogram.</p>



<p>Set the plot type to histogram and pick the model’s single-part points dataset as the layer to gather data from. Make sure that the layer has been filtered to only show a single fire event. Then, set the X field to the following layer attribute: &#8220;ACQ_DATE&#8221;.</p>



<p>You can then hit the Create Plot button, go grab a coffee, and enjoy the resulting histogram which will appear after a minute or so.</p>


<div class="wp-block-image">
<figure class="aligncenter size-full"><img decoding="async" loading="lazy" width="726" height="572" data-attachment-id="13886" data-permalink="https://www.opengis.ch/2023/09/05/analyzing-and-visualizing-large-scale-fire-events-using-qgis-processing-with-st-dbscan/dataplotly/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?fit=726%2C572&amp;ssl=1" data-orig-size="726,572" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="dataplotly" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?fit=300%2C236&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?fit=726%2C572&amp;ssl=1" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?resize=726%2C572&#038;ssl=1" alt="" class="wp-image-13886" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?w=726&amp;ssl=1 726w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/09/dataplotly.png?resize=300%2C236&amp;ssl=1 300w" sizes="(max-width: 726px) 100vw, 726px" data-recalc-dims="1" /></figure></div>


<p>While not perfect, an histogram can quickly provide a good sense of a fire event’s “peak” over a period of time.</p>
