---
source: "blog"
title: "anitagraser.com: Mapping Neo4j spatial nodes with GeoPandas"
image: "mapping-neo4j-spatial-nodes-with-geopandas."
date: "2023-12-03"
link: "https://anitagraser.com/2023/12/03/mapping-neo4j-spatial-nodes-with-geopandas/"
draft: "true"
showcase: "planet"
---

<p>In the recent post <a href="https://anitagraser.com/2023/11/27/setting-up-a-graph-db-using-gtfs-data-neo4j/">Setting up a graph db using GTFS data &amp; Neo4J</a>, we noted that &#8212; unfortunately &#8212; Neomap is not an option to visualize spatial nodes anymore. </p>



<p>GeoPandas to the rescue!</p>



<p>But first we need the <a href="https://neo4j.com/docs/python-manual/current/">neo4j Python driver</a>: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
pip install neo4j
</pre></div>


<p>Then we can connect to our database. The default user name is <code>neo4j</code> and you get to pick the password when creating the database: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from neo4j import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "password")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
</pre></div>


<p>Once we have confirmed that the connection works as expected, we can run a query:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
QUERY = "MATCH (p:Stop) RETURN p.name AS name, p.location AS geom"

records, summary, keys = driver.execute_query(
    QUERY, database_="neo4j",
)

for rec in records:
    print(rec)
</pre></div>


<figure class="wp-block-image size-large"><img loading="lazy" width="541" height="383" data-attachment-id="8706" data-permalink="https://anitagraser.com/2023/12/03/mapping-neo4j-spatial-nodes-with-geopandas/image-13-4/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-13.png" data-orig-size="541,383" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-13" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-13.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-13.png?w=541" src="https://underdark.files.wordpress.com/2023/12/image-13.png?w=541" alt="" class="wp-image-8706" srcset="https://underdark.files.wordpress.com/2023/12/image-13.png 541w, https://underdark.files.wordpress.com/2023/12/image-13.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-13.png?w=300 300w" sizes="(max-width: 541px) 100vw, 541px" /></figure>



<p>Nice. There we have our GTFS stops, their names and their locations. But how to put them on a map? </p>



<p>Conveniently, there is a <a href="https://neo4j.com/docs/api/python-driver/current/api.html#neo4j.Result.to_df">to_db() function in the Neo4j driver</a>:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import geopandas as gpd
import numpy as np

with driver.session(database=&quot;neo4j&quot;) as session:
    tx = session.begin_transaction()
    results = tx.run(QUERY)
    df = results.to_df(expand=True)
    df = df&#91;df&#91;&quot;geom&#91;].0&quot;]&gt;0]
    gdf = gpd.GeoDataFrame(
        df&#91;'name'], crs=4326,
        geometry=gpd.points_from_xy(df&#91;'geom&#91;].0'], df&#91;'geom&#91;].1']))
    print(gdf)

tx.close() 
</pre></div>


<p>Since some of the nodes lack geometries, I added a quick and dirty hack to get rid of these nodes because &#8212; otherwise &#8212; <code>gdf.explore()</code> will complain about None geometries. </p>



<figure class="wp-block-image size-large"><img loading="lazy" width="539" height="634" data-attachment-id="8673" data-permalink="https://anitagraser.com/2023/12/03/mapping-neo4j-spatial-nodes-with-geopandas/image-3-9/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-3.png" data-orig-size="539,634" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-3" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-3.png?w=255" data-large-file="https://underdark.files.wordpress.com/2023/12/image-3.png?w=539" src="https://underdark.files.wordpress.com/2023/12/image-3.png?w=539" alt="" class="wp-image-8673" srcset="https://underdark.files.wordpress.com/2023/12/image-3.png 539w, https://underdark.files.wordpress.com/2023/12/image-3.png?w=128 128w, https://underdark.files.wordpress.com/2023/12/image-3.png?w=255 255w" sizes="(max-width: 539px) 100vw, 539px" /></figure>



<figure class="wp-block-image size-large"><img loading="lazy" width="537" height="384" data-attachment-id="8675" data-permalink="https://anitagraser.com/2023/12/03/mapping-neo4j-spatial-nodes-with-geopandas/image-4-9/" data-orig-file="https://underdark.files.wordpress.com/2023/12/image-4.png" data-orig-size="537,384" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-4" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/12/image-4.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/12/image-4.png?w=537" src="https://underdark.files.wordpress.com/2023/12/image-4.png?w=537" alt="" class="wp-image-8675" srcset="https://underdark.files.wordpress.com/2023/12/image-4.png 537w, https://underdark.files.wordpress.com/2023/12/image-4.png?w=150 150w, https://underdark.files.wordpress.com/2023/12/image-4.png?w=300 300w" sizes="(max-width: 537px) 100vw, 537px" /></figure>



<p>You can find this notebook at: <a href="https://github.com/anitagraser/QGIS-resources/blob/1e4ea435c9b1795ba5b170ddb176aa83689112eb/qgis3/notebooks/neo4j.ipynb">https://github.com/anitagraser/QGIS-resources/blob/1e4ea435c9b1795ba5b170ddb176aa83689112eb/qgis3/notebooks/neo4j.ipynb</a></p>



<p>Next step will have to be the relationships. Stay posted. </p>
