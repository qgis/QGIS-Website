---
source: "blog"
title: "anitagraser.com: Exploring a hierarchical graph-based model for mobility data representation and analysis"
image: "exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis."
date: "2023-11-05"
link: "https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/"
draft: "true"
showcase: "planet"
---

<p>Today&#8217;s post is a first quick dive into Neo4J (really just getting my toes wet). It&#8217;s based on a publicly available Neo4J dump containing mobility data, ship trajectories to be specific. You can find this data and the setup instructions at:  </p>



<p><a href="https://doi.org/10.5281/zenodo.6405212">Maryam Maslek ELayam, Cyril Ray, &amp; Christophe Claramunt. (2022). A hierarchical graph-based model for mobility data representation and analysis [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6405212</a></p>



<p>I was made aware of this work since they cited <a href="https://movingpandas.org">MovingPandas</a> in their paper in <a href="https://www.sciencedirect.com/science/article/abs/pii/S0169023X22000532">Data &amp; Knowledge Engineering</a>:&nbsp;<em>&#8220;The implementation combines several open source tools such as Python, MovingPandas library, Uber H3 index, Neo4j graph database management system&#8221;</em></p>



<p>Once set up, this gives us a database with three hierarchical levels: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-8.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8531" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-8-5/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-8.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-8" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-8.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-8.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-8.png?w=1024" alt="" class="wp-image-8531" srcset="https://underdark.files.wordpress.com/2023/11/image-8.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-8.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-8.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-8.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-8.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Neo4j comes with a nice graphical browser that lets us explore the data. We can switch between levels and click on individual node labels to get a quick preview: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-9.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8533" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-9-5/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-9.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-9" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-9.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-9.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-9.png?w=1024" alt="" class="wp-image-8533" srcset="https://underdark.files.wordpress.com/2023/11/image-9.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-9.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-9.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-9.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-9.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-10.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8535" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-10-5/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-10.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-10" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-10.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-10.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-10.png?w=1024" alt="" class="wp-image-8535" srcset="https://underdark.files.wordpress.com/2023/11/image-10.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-10.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-10.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-10.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-10.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Level 2 is a generalization / aggregation of level 1. Expanding the graph of one of the level 2 nodes shows its connection to level 1. For example, the level 2 port node &#8220;Audierne&#8221; actually refers to two level 1 nodes: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-11.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8536" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-11-5/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-11.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-11" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-11.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-11.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-11.png?w=1024" alt="" class="wp-image-8536" srcset="https://underdark.files.wordpress.com/2023/11/image-11.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-11.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-11.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-11.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-11.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Every &#8220;road&#8221; level 1 relationship between ports provide information about the ship, its arrival, departure, travel time, and speed. We can see that this two level 1 ports must be pretty close since travel times are only 5 minutes:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-14.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8542" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-14-3/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-14.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-14" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-14.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-14.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-14.png?w=1024" alt="" class="wp-image-8542" srcset="https://underdark.files.wordpress.com/2023/11/image-14.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-14.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-14.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-14.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-14.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Further expanding one of the port level 1 nodes shows its connection to waypoints of level1: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-12.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8538" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-12-4/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-12.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-12" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-12.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-12.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-12.png?w=1024" alt="" class="wp-image-8538" srcset="https://underdark.files.wordpress.com/2023/11/image-12.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-12.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-12.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-12.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-12.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Switching to level 2, we gain access to nodes of type Traj(ectory). Additionally, the road level 2 relationships represent aggregations of the trajectories, for example, here&#8217;s a relationship with only one associated trajectory: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-16.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8545" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-16-3/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-16.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-16" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-16.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-16.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-16.png?w=1024" alt="" class="wp-image-8545" srcset="https://underdark.files.wordpress.com/2023/11/image-16.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-16.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-16.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-16.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-16.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>There are also some odd relationships, for example, trajectory 43 has two ends and begins relationships and there are also two road relationships referencing this trajectory (with identical information, only differing in their automatic &lt;id&gt;). I&#8217;m not yet sure if that is a feature or a bug: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-17.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8546" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-17-3/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-17.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-17" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-17.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-17.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-17.png?w=1024" alt="" class="wp-image-8546" srcset="https://underdark.files.wordpress.com/2023/11/image-17.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-17.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-17.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-17.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-17.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>On level 1, we also have access to ship nodes. They are connected to ports and waypoints. However, exploring them visually is challenging. Things look fine at first:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-18.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8548" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-18-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-18.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-18" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-18.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-18.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-18.png?w=1024" alt="" class="wp-image-8548" srcset="https://underdark.files.wordpress.com/2023/11/image-18.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-18.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-18.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-18.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-18.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>But after a while, once all relationships have loaded, we have it: the MIGHTY BALL OF YARN &#8482;:  </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-19.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8549" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-19-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-19.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-19" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-19.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-19.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-19.png?w=1024" alt="" class="wp-image-8549" srcset="https://underdark.files.wordpress.com/2023/11/image-19.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-19.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-19.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-19.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-19.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>I guess this is the point where it becomes necessary to get accustomed to the query language. And no, it&#8217;s not SQL, it is Cypher. For example, selecting a specific trajectory with id 0, looks like this: </p>



<pre class="wp-block-code"><code> MATCH&nbsp;(t1&nbsp;{traj_id:&nbsp;0})&nbsp;RETURN&nbsp;t1</code></pre>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-20.png"><img loading="lazy" width="1024" height="668" data-attachment-id="8551" data-permalink="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/image-20-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-20.png" data-orig-size="1296,846" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-20" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-20.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-20.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-20.png?w=1024" alt="" class="wp-image-8551" srcset="https://underdark.files.wordpress.com/2023/11/image-20.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-20.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-20.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-20.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-20.png 1296w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>But more on this another time. </p>



<hr class="wp-block-separator has-alpha-channel-opacity" />



<p>This post is part of a series. Read more about&nbsp;<a href="https://anitagraser.com/movement-data-in-gis/">movement data in GIS.</a></p>
