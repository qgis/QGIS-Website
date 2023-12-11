---
source: "blog"
title: "anitagraser.com: Mapping relationships between Neo4j spatial nodes with GeoPandas"
image: "mapping-relationships-between-neo4j-spatial-nodes-with-geopandas."
date: "2023-12-09"
link: "https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/"
draft: "true"
showcase: "planet"
---

<p>Previously, <a href="https://anitagraser.com/2023/12/03/mapping-neo4j-spatial-nodes-with-geopandas/">we mapped neo4j spatial nodes</a>. This time, we want to take it one step further and map relationships. </p>



<p>A prime example, are the relationships between GTFS StopTime and Trip nodes. For example, this is the Cypher query to get all StopTime nodes of Trip 17:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
MATCH 
    (t:Trip  {id: &quot;17&quot;})
    &lt;-&#91;:BELONGS_TO]-
    (st:StopTime) 
RETURN st
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/12/image-5.png"><img width="1024" height="544" data-attachment-id="8684" data-permalink="https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/image-5-8/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-5.png" data-orig-size="1214,645" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-5" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-5.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-5.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-5.png?w=1024" alt="" class="wp-image-8684" srcset="https://underdark.files.wordpress.com/2023/12/image-5.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/12/image-5.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-5.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-5.png?w=768 768w, https://underdark.files.wordpress.com/2023/12/image-5.png 1214w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>To get the stop locations, we also need to get the stop nodes:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
MATCH 
    (t:Trip {id: &quot;17&quot;})
    &lt;-&#91;:BELONGS_TO]-
    (st:StopTime)
    -&#91;:STOPS_AT]-&gt;
    (s:Stop)
RETURN st ,s
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/12/image-6.png"><img width="895" height="566" data-attachment-id="8687" data-permalink="https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/image-6-8/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-6.png" data-orig-size="895,566" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-6" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-6.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-6.png?w=545" src="https://underdark.files.wordpress.com/2023/12/image-6.png?w=895" alt="" class="wp-image-8687" srcset="https://underdark.files.wordpress.com/2023/12/image-6.png 895w, https://underdark.files.wordpress.com/2023/12/image-6.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-6.png?w=300 300w, https://underdark.files.wordpress.com/2023/12/image-6.png?w=768 768w" sizes="(max-width: 895px) 100vw, 895px" /></a></figure>



<p>Adapting our code from the previous post, we can plot the stops: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from shapely.geometry import Point

QUERY = &quot;&quot;&quot;MATCH (
    t:Trip {id: &quot;17&quot;})
    &lt;-&#91;:BELONGS_TO]-
    (st:StopTime)
    -&#91;:STOPS_AT]-&gt;
    (s:Stop)
RETURN st ,s
ORDER BY st.stopSequence
&quot;&quot;&quot;

with driver.session(database=&quot;neo4j&quot;) as session:
    tx = session.begin_transaction()
    results = tx.run(QUERY)
    df = results.to_df(expand=True)
    gdf = gpd.GeoDataFrame(
        df&#91;&#91;'s().prop.name']], crs=4326,
        geometry=df&#91;&quot;s().prop.location&quot;].apply(Point)
    )

tx.close() 
m = gdf.explore()
m
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/12/image-10.png"><img width="527" height="879" data-attachment-id="8696" data-permalink="https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/image-10-6/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-10.png" data-orig-size="527,879" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-10" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-10.png?w=180" data-large-file="https://underdark.files.wordpress.com/2023/12/image-10.png?w=527" src="https://underdark.files.wordpress.com/2023/12/image-10.png?w=527" alt="" class="wp-image-8696" srcset="https://underdark.files.wordpress.com/2023/12/image-10.png 527w, https://underdark.files.wordpress.com/2023/12/image-10.png?w=90 90w, https://underdark.files.wordpress.com/2023/12/image-10.png?w=180 180w" sizes="(max-width: 527px) 100vw, 527px" /></a></figure>



<p>Ordering by stop sequence is actually completely optional. Technically, we could use the sorted GeoDataFrame, and aggregate all the points into a linestring to plot the route. But I want to try something different: we&#8217;ll use the NEXT_STOP relationships to get a DataFrame of the start and end stops for each segment:  </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
QUERY = &quot;&quot;&quot;
MATCH (t:Trip {id: &quot;17&quot;})
   &lt;-&#91;:BELONGS_TO]-
   (st1:StopTime)
   -&#91;:NEXT_STOP]-&gt;
   (st2:StopTime)
MATCH (st1)-&#91;:STOPS_AT]-&gt;(s1:Stop)
MATCH (st2)-&#91;:STOPS_AT]-&gt;(s2:Stop)
RETURN st1, st2, s1, s2
&quot;&quot;&quot;

from shapely.geometry import Point, LineString

def make_line(row):
    s1 = Point(row&#91;&quot;s1().prop.location&quot;])
    s2 = Point(row&#91;&quot;s2().prop.location&quot;])
    return LineString(&#91;s1,s2])

with driver.session(database=&quot;neo4j&quot;) as session:
    tx = session.begin_transaction()
    results = tx.run(QUERY)
    df = results.to_df(expand=True)
    gdf = gpd.GeoDataFrame(
        df&#91;&#91;'s1().prop.name']], crs=4326,
        geometry=df.apply(make_line, axis=1)
    )

tx.close() 
gdf.explore(m=m)
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/12/image-11.png"><img loading="lazy" width="527" height="975" data-attachment-id="8698" data-permalink="https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/image-11-6/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-11.png" data-orig-size="527,975" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-11" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-11.png?w=162" data-large-file="https://underdark.files.wordpress.com/2023/12/image-11.png?w=527" src="https://underdark.files.wordpress.com/2023/12/image-11.png?w=527" alt="" class="wp-image-8698" srcset="https://underdark.files.wordpress.com/2023/12/image-11.png 527w, https://underdark.files.wordpress.com/2023/12/image-11.png?w=81 81w, https://underdark.files.wordpress.com/2023/12/image-11.png?w=162 162w" sizes="(max-width: 527px) 100vw, 527px" /></a></figure>



<p>Finally, we can also use Cypher to calculate the travel time between two stops: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
MATCH (t:Trip {id: &quot;17&quot;})
   &lt;-&#91;:BELONGS_TO]-
   (st1:StopTime)
   -&#91;:NEXT_STOP]-&gt;
   (st2:StopTime)
MATCH (st1)-&#91;:STOPS_AT]-&gt;(s1:Stop)
MATCH (st2)-&#91;:STOPS_AT]-&gt;(s2:Stop)
RETURN st1.departureTime AS time1, 
   st2.arrivalTime AS time2, 
   s1.location AS geom1, 
   s2.location AS geom2, 
   duration.inSeconds(
      time(st1.departureTime), 
      time(st2.arrivalTime)
   ).seconds AS traveltime
</pre></div>


<figure class="wp-block-image size-large"><img loading="lazy" width="538" height="322" data-attachment-id="8709" data-permalink="https://anitagraser.com/2023/12/09/mapping-relationships-between-neo4j-spatial-nodes-with-geopandas/image-14-4/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-14.png" data-orig-size="538,322" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-14" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-14.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-14.png?w=538" src="https://underdark.files.wordpress.com/2023/12/image-14.png?w=538" alt="" class="wp-image-8709" srcset="https://underdark.files.wordpress.com/2023/12/image-14.png 538w, https://underdark.files.wordpress.com/2023/12/image-14.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-14.png?w=300 300w" sizes="(max-width: 538px) 100vw, 538px" /></figure>



<p>As always, here&#8217;s the notebook: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/neo4j.ipynb">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/neo4j.ipynb</a> </p>
