---
source: "blog"
title: "anitagraser.com: Setting up a graph db using GTFS data & Neo4J"
image: "setting-up-a-graph-db-using-gtfs-data-neo4j."
date: "2023-11-27"
link: "https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/"
draft: "true"
showcase: "planet"
---

<p>In a recent post, we looked into <a href="https://anitagraser.com/2023/11/05/exploring-a-hierarchical-graph-based-model-for-mobility-data-representation-and-analysis/">a graph-based model for maritime mobility data</a> and how it may be represented in Neo4J. Today, I want to look into another type of mobility data: public transport schedules in GTFS format. </p>



<p>In this post, I&#8217;ll be using the <a href="https://transitfeeds.com/p/rigas-satiksme/333">public GTFS data for Riga</a> since Riga is one of the demo sites for our current <a href="https://emeralds-horizon.eu">EMERALDS research project</a>.  </p>



<p>The workflow is heavily inspired by <a href="https://blog.faboo.org/">Bert Radke</a>&#8216;s post <a href="https://faboo.org/2021/01/loading-uk-gtfs/">&#8220;Loading the UK GTFS data feed&#8221;</a> from 2021 and his <a href="https://github.com/taseroth/gtfs-routing/blob/main/src/main/resources/import.cypher">import Cypher script</a> which I used as a template, adjusted to the requirements of the Riga dataset, and updated to recent Neo4J changes.</p>



<p>Here we go.</p>



<p>Since a GTFS export is basically a ZIP archive full of CSVs, we will be making good use of <a href="https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/">Neo4Js CSV loading capabilities</a>. The basic script for importing the stops file and <a href="https://neo4j.com/docs/cypher-manual/current/values-and-types/spatial/">creating point geometries</a> from lat and lon values would be: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
LOAD CSV with headers 
FROM "file:///stops.txt" 
AS row 
CREATE (:Stop {
   stop_id: row&#91;"stop_id"],
   name: row&#91;"stop_name"], 
   geom: point({
    longitude: toFloat(row&#91;"stop_lon"]),
    latitude: toFloat(row&#91;"stop_lat"])
    })
})
</pre></div>


<p>This requires that the stops.txt is located in the import directory of your Neo4J database. When we run the above script and the file is missing, Neo4J will tell us where it tried to look for it. In my case, the directory ended up being: </p>



<p><code>C:\Users\Anita\.Neo4jDesktop\relate-data\dbmss\dbms-72882d24-bf91-4031-84e9-abd24624b760\import</code></p>



<p>So, let&#8217;s put all GTFS CSVs into that directory and we should be good to go.</p>



<p>Let&#8217;s start with the agency file: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
load csv with headers from
'file:///agency.txt' as row
create (a:Agency {
   id: row.agency_id, 
   name: row.agency_name, 
   url: row.agency_url, 
   timezone: row.agency_timezone, 
   lang: row.agency_lang
});
</pre></div>


<p>… Added 1 label, created 1 node, set 5 properties, completed after 31 ms.</p>



<p>The routes file does not include agency info but, luckily, there is only one agency, so we can hard-code it:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
load csv with headers from
'file:///routes.txt' as row
match (a:Agency {id: &quot;rigassatiksme&quot;})
create (a)-&#91;:OPERATES]-&gt;(r:Route {
   id: row.route_id, 
   shortName: row.route_short_name,
   longName: row.route_long_name, 
   type: toInteger(row.route_type)
});
</pre></div>


<p>… Added 81 labels, created 81 nodes, set 324 properties, created 81 relationships, completed after 28 ms.</p>



<p>From stops, I&#8217;m removing non-existent or empty columns:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
load csv with headers from
'file:///stops.txt' as row
create (s:Stop {
   id: row.stop_id, 
   name: row.stop_name, 
   location: point({
      latitude: toFloat(row.stop_lat), 
      longitude: toFloat(row.stop_lon)
   }),
   code: row.stop_code
});
</pre></div>


<p>… Added 1671 labels, created 1671 nodes, set 5013 properties, completed after 71 ms.</p>



<p>From trips, I&#8217;m also removing non-existent or empty columns:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
load csv with headers from
'file:///trips.txt' as row
match (r:Route {id: row.route_id})
create (r)&lt;-&#91;:USES]-(t:Trip {
   id: row.trip_id, 
   serviceId: row.service_id,
   headSign: row.trip_headsign, 
   direction_id: toInteger(row.direction_id),
   blockId: row.block_id,
   shapeId: row.shape_id
});
</pre></div>


<p>… Added 14427 labels, created 14427 nodes, set 86562 properties, created 14427 relationships, completed after 875 ms.</p>



<p>Slowly getting there. We now have around 16k nodes in our graph: </p>



<figure class="wp-block-image size-large"><img width="342" height="165" data-attachment-id="8623" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-33/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-33.png" data-orig-size="342,165" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-33" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-33.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-33.png?w=342" src="https://underdark.files.wordpress.com/2023/11/image-33.png?w=342" alt="" class="wp-image-8623" srcset="https://underdark.files.wordpress.com/2023/11/image-33.png 342w, https://underdark.files.wordpress.com/2023/11/image-33.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-33.png?w=300 300w" sizes="(max-width: 342px) 100vw, 342px" /></figure>



<p>Finally, it&#8217;s stop times time. This is where the serious information is. This file is much larger than all previous ones with over 300k lines (i.e. times when an PT vehicle stops). </p>



<p>This requires another tweak to Bert&#8217;s script since <code>using periodic commit</code> is not supported anymore: <code>The PERIODIC COMMIT query hint is no longer supported. Please use CALL { … } IN TRANSACTIONS instead. </code>So I ended up using the following, based on <a href="https://community.neo4j.com/t/best-practice-for-replacement-of-using-periodic-commit-to-call-in-transactions/48636/2" rel="nofollow">https://community.neo4j.com/t/best-practice-for-replacement-of-using-periodic-commit-to-call-in-transactions/48636/2</a>:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
:auto
load csv with headers from
'file:///stop_times.txt' as row
CALL { with row
match (t:Trip {id: row.trip_id}), (s:Stop {id: row.stop_id})
create (t)&lt;-&#91;:BELONGS_TO]-(st:StopTime {
   arrivalTime: row.arrival_time, 
   departureTime: row.departure_time,
   stopSequence: toInteger(row.stop_sequence)})-&#91;:STOPS_AT]-&gt;(s)
} IN TRANSACTIONS OF 10 ROWS;
</pre></div>


<p>… Added 351388 labels, created 351388 nodes, set 1054164 properties, created 702776 relationships, completed after 1364220 ms.</p>



<p>As you can see, this took a while. But now we have all nodes in place: </p>



<figure class="wp-block-image size-large"><img width="331" height="160" data-attachment-id="8626" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-34/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-34.png" data-orig-size="331,160" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-34" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-34.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-34.png?w=331" src="https://underdark.files.wordpress.com/2023/11/image-34.png?w=331" alt="" class="wp-image-8626" srcset="https://underdark.files.wordpress.com/2023/11/image-34.png 331w, https://underdark.files.wordpress.com/2023/11/image-34.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-34.png?w=300 300w" sizes="(max-width: 331px) 100vw, 331px" /></figure>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-35.png"><img width="1024" height="601" data-attachment-id="8627" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-35/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-35.png" data-orig-size="1826,1072" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-35" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-35.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-35.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-35.png?w=1024" alt="" class="wp-image-8627" srcset="https://underdark.files.wordpress.com/2023/11/image-35.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-35.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-35.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-35.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-35.png 1826w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>The final statement adds additional relationships between consecutive stop times: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
call apoc.periodic.iterate('match (t:Trip) return t',
'match (t)&lt;-&#91;:BELONGS_TO]-(st) with st order by st.stopSequence asc
with collect(st) as stops
unwind range(0, size(stops)-2) as i
with stops&#91;i] as curr, stops&#91;i+1] as next
merge (curr)-&#91;:NEXT_STOP]-&gt;(next)', {batchmode: &quot;BATCH&quot;, parallel:true, parallel:true, batchSize:1});
</pre></div>


<p>This fails with: <code>There is no procedure with the name apoc.periodic.iterate registered for this database instance. Please ensure you've spelled the procedure name correctly and that the procedure is properly deployed.</code></p>



<p>So, let&#8217;s install APOC. That&#8217;s a plugin which we can install into our database from within Neo4J Desktop: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-36.png"><img loading="lazy" width="1024" height="276" data-attachment-id="8630" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-36/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-36.png" data-orig-size="1391,376" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-36" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-36.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-36.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-36.png?w=1024" alt="" class="wp-image-8630" srcset="https://underdark.files.wordpress.com/2023/11/image-36.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-36.png?w=1021 1021w, https://underdark.files.wordpress.com/2023/11/image-36.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-36.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-36.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-36.png 1391w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>After restarting the db, we can run the query:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-37.png"><img loading="lazy" width="1024" height="487" data-attachment-id="8632" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-37/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-37.png" data-orig-size="1725,821" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-37" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-37.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-37.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-37.png?w=1024" alt="" class="wp-image-8632" srcset="https://underdark.files.wordpress.com/2023/11/image-37.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-37.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-37.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-37.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-37.png 1725w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>No errors. Sounds good. </p>



<p>Let&#8217;s have a look at what we ended up with. Here are 25 random Trips. I expanded one of them to show its associated StopTimes. We can see the relations between consecutive StopTimes and I&#8217;ve expanded the final five StopTimes to show their linked Stops: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-38.png"><img loading="lazy" width="1024" height="601" data-attachment-id="8634" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-38/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-38.png" data-orig-size="1826,1072" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-38" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-38.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-38.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-38.png?w=1024" alt="" class="wp-image-8634" srcset="https://underdark.files.wordpress.com/2023/11/image-38.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/11/image-38.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-38.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-38.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-38.png 1826w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>I also wanted to visualize the stops on a map. And there used to be a neat app called <a href="https://registry.npmjs.org/neomap">Neomap</a> which can be installed easily:  </p>



<figure class="wp-block-image size-large"><img loading="lazy" width="436" height="713" data-attachment-id="8636" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-39/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-39.png" data-orig-size="436,713" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-39" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-39.png?w=183" data-large-file="https://underdark.files.wordpress.com/2023/11/image-39.png?w=436" src="https://underdark.files.wordpress.com/2023/11/image-39.png?w=436" alt="" class="wp-image-8636" srcset="https://underdark.files.wordpress.com/2023/11/image-39.png 436w, https://underdark.files.wordpress.com/2023/11/image-39.png?w=92 92w, https://underdark.files.wordpress.com/2023/11/image-39.png?w=183 183w" sizes="(max-width: 436px) 100vw, 436px" /></figure>



<p>However, Neomap <a href="https://github.com/stellasia/neomap/issues/109">does not seem to be compatible with the latest Neo4J</a>: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-40.png"><img loading="lazy" width="1024" height="558" data-attachment-id="8638" data-permalink="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/image-40/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-40.png" data-orig-size="1409,769" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-40" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-40.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-40.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-40.png?w=1024" alt="" class="wp-image-8638" srcset="https://underdark.files.wordpress.com/2023/11/image-40.png?w=1022 1022w, https://underdark.files.wordpress.com/2023/11/image-40.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-40.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-40.png?w=768 768w, https://underdark.files.wordpress.com/2023/11/image-40.png 1409w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>So this final step will have to wait for another time. </p>
