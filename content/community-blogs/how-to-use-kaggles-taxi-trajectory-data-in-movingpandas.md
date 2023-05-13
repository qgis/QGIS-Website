---
source: "blog"
title: "anitagraser.com: How to use Kaggle’s Taxi Trajectory Data in MovingPandas"
image: "how-to-use-kaggles-taxi-trajectory-data-in-movingpandas."
date: "2023-05-12"
link: "https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/"
draft: "true"
showcase: "planet"
---

<p><a href="https://www.kaggle.com/datasets/crailtap/taxi-trajectory">Kaggle&#8217;s &#8220;Taxi Trajectory Data from ECML/PKDD 15: Taxi Trip Time Prediction (II) Competition&#8221;</a> is one of the most used mobility / vehicle trajectory datasets in computer science. However, in contrast to other similar datasets, Kaggle&#8217;s taxi trajectories are provided in a format that is not readily usable in MovingPandas since the spatiotemporal information is provided as:</p>



<ul>
<li>TIMESTAMP: (integer) Unix Timestamp (in seconds). It identifies the trip’s start;</li>



<li>POLYLINE: (String): It contains a list of GPS coordinates (i.e. WGS84 format) mapped as a string. The beginning and the end of the string are identified with brackets (i.e. [ and ], respectively). Each pair of coordinates is also identified by the same brackets as [LONGITUDE, LATITUDE]. This list contains one pair of coordinates for each 15 seconds of trip. The last list item corresponds to the trip’s destination while the first one represents its start;</li>
</ul>



<p>Therefore, we need to create a DataFrame with one point + timestamp per row before we can use MovingPandas to create Trajectories and analyze them.</p>



<p>But first things first. Let&#8217;s download the dataset:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import datetime
import pandas as pd
import geopandas as gpd
import movingpandas as mpd
import opendatasets as od
from os.path import exists
from shapely.geometry import Point

input_file_path = 'taxi-trajectory/train.csv'

def get_porto_taxi_from_kaggle():
    if not exists(input_file_path):
        od.download("https://www.kaggle.com/datasets/crailtap/taxi-trajectory")

get_porto_taxi_from_kaggle()
df = pd.read_csv(input_file_path, nrows=10, usecols=&#91;'TRIP_ID', 'TAXI_ID', 'TIMESTAMP', 'MISSING_DATA', 'POLYLINE'])
df.POLYLINE = df.POLYLINE.apply(eval)  # string to list
df
</pre></div>


<figure class="wp-block-image size-large"><img data-attachment-id="8437" data-permalink="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/image-23/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image.png" data-orig-size="992,372" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image.png?w=992" alt="" class="wp-image-8437" srcset="https://underdark.files.wordpress.com/2023/05/image.png 992w, https://underdark.files.wordpress.com/2023/05/image.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image.png?w=768 768w" sizes="(max-width: 992px) 100vw, 992px" /></figure>



<p>And now for the remodelling:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
def unixtime_to_datetime(unix_time):
    return datetime.datetime.fromtimestamp(unix_time)

def compute_datetime(row):
    unix_time = row&#91;'TIMESTAMP']
    offset = row&#91;'running_number'] * datetime.timedelta(seconds=15)
    return unixtime_to_datetime(unix_time) + offset

new_df = df.explode('POLYLINE')
new_df&#91;'geometry'] = new_df&#91;'POLYLINE'].apply(Point)
new_df&#91;'running_number'] = new_df.groupby('TRIP_ID').cumcount()
new_df&#91;'datetime'] = new_df.apply(compute_datetime, axis=1)
new_df.drop(columns=&#91;'POLYLINE', 'TIMESTAMP', 'running_number'], inplace=True)
new_df
</pre></div>


<figure class="wp-block-image size-large"><img data-attachment-id="8439" data-permalink="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/image-1-9/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-1.png" data-orig-size="905,446" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-1" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-1.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-1.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-1.png?w=905" alt="" class="wp-image-8439" srcset="https://underdark.files.wordpress.com/2023/05/image-1.png 905w, https://underdark.files.wordpress.com/2023/05/image-1.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-1.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-1.png?w=768 768w" sizes="(max-width: 905px) 100vw, 905px" /></figure>



<p>And that&#8217;s it. Now we can create the trajectories:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
trajs = mpd.TrajectoryCollection(
    gpd.GeoDataFrame(new_df, crs=4326), 
    traj_id_col='TRIP_ID', obj_id_col='TAXI_ID', t='datetime')
trajs.hvplot(title='Kaggle Taxi Trajectory Data', tiles='CartoLight')
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/05/image-2.png"><img data-attachment-id="8443" data-permalink="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/image-2-8/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-2.png" data-orig-size="1121,872" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-2" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-2.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-2.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-2.png?w=1024" alt="" class="wp-image-8443" srcset="https://underdark.files.wordpress.com/2023/05/image-2.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/05/image-2.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-2.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-2.png?w=768 768w, https://underdark.files.wordpress.com/2023/05/image-2.png 1121w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>That&#8217;s it. Now our MovingPandas.TrajectoryCollection is ready for further analysis. </p>



<p>By the way, the plot above illustrates a new feature in the recent <a href="https://github.com/movingpandas/movingpandas/releases/tag/v0.16">MovingPandas 0.16 release</a> which, among other features, introduced plots with arrow markers that show the movement direction. Other new features include a completely new custom distance, speed, and acceleration unit support. This means that, for example, instead of always getting speed in meters per second, you can now specify your desired output units, including km/h, mph, or nm/h (knots). </p>
