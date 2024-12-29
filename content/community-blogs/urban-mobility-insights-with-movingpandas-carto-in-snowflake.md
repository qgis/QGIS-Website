---
source: "blog"
title: "anitagraser.com: Urban Mobility Insights with MovingPandas & CARTO in Snowflake"
image: "urban-mobility-insights-with-movingpandas-carto-in-snowflake."
date: "2024-12-17"
link: "https://anitagraser.com/2024/12/17/urban-mobility-insights-with-movingpandas-carto-in-snowflake/"
draft: "true"
showcase: "planet"
---

<p>Today, I want to point out a blog post over at</p>



<p><a href="https://carto.com/blog/urban-mobility-insights-with-movingpandas-carto-in-snowflake">https://carto.com/blog/urban-mobility-insights-with-movingpandas-carto-in-snowflake</a></p>



<p>written together with my fellow&nbsp;co-authors and EMERALDS project team member Argyrios Kyrgiazos.</p>



<figure class="wp-block-image size-large"><a href="https://carto.com/blog/urban-mobility-insights-with-movingpandas-carto-in-snowflake"><img alt="" class="wp-image-9334" height="537" src="https://anitagraser.com/wp-content/uploads/2024/12/image.png?w=1024" width="1024" /></a></figure>



<p>For the technically inclined, the highlight are the presented <strong>UDFs in Snowflake</strong> to process and transform the trajectory data. For example, here&#8217;s a TemporalSplitter UDF: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: sql; title: ; notranslate">
CREATE OR REPLACE FUNCTION CARTO_DATABASE.CARTO.TemporalSplitter(geom ARRAY, t ARRAY, mode STRING)
RETURNS ARRAY
LANGUAGE PYTHON
RUNTIME_VERSION = 3.11
PACKAGES = (&#039;numpy&#039;,&#039;pandas&#039;, &#039;geopandas&#039;,&#039;movingpandas&#039;, &#039;shapely&#039;)
HANDLER = &#039;udf&#039;
AS $$
import numpy as np
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
import shapely
from shapely.geometry import shape, mapping, Point, Polygon
from shapely.validation import make_valid
from datetime import datetime, timedelta

def udf(geom, t, mode):
    valid_df = pd.DataFrame(geom, columns=&#91;&#039;geometry&#039;])
    valid_df&#91;&#039;t&#039;] = pd.to_datetime(t)
    valid_df&#91;&#039;geometry&#039;] = valid_df&#91;&#039;geometry&#039;].apply(lambda x:shapely.wkt.loads(x))
    gdf = gpd.GeoDataFrame(valid_df, geometry=&#039;geometry&#039;, crs=&#039;epsg:4326&#039;)
    gdf = gdf.set_index(&#039;t&#039;)
    traj = mpd.Trajectory(gdf, 1)
    traj_sm = mpd.TemporalSplitter(traj).split(mode=mode)
    if len(traj_sm.trajectories)&gt;0:
        res = traj_sm.to_point_gdf()
        res&#91;&#039;geometry&#039;] = res&#91;&#039;geometry&#039;].apply(lambda x: shapely.wkt.dumps(x))
        return res.reset_index().values
    else:
        return &#91;]
$$;
</pre></div>


<p>You can find the full code here: <a href="https://github.com/anitagraser/carto-research-public/tree/master/movingpandas_carto_in_snowflake">https://github.com/anitagraser/carto-research-public/tree/master/movingpandas_carto_in_snowflake</a> </p>
