---
source: "blog"
title: "anitagraser.com: Analyzing video-based bicycle trajectories"
image: "analyzing-video-based-bicycle-trajectories."
date: "2023-05-21"
link: "https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/"
draft: "true"
showcase: "planet"
---

<p>Did you know that <a href="https://movingpandas.org">MovingPandas</a> also supports local image coordinates? Indeed, it does.</p>



<p>In today&#8217;s post, we will explore how we can use this feature to analyze bicycle tracks extracted from video footage published by <a href="https://fosstodon.org/@mszll@datasci.social">Michael Szell @mszll</a>: </p>



<ul>
<li>Dataset: <a href="https://zenodo.org/record/7288616" rel="nofollow">https://zenodo.org/record/7288616</a>  </li>



<li>Data description: <a href="https://arxiv.org/abs/2211.01301" rel="nofollow">https://arxiv.org/abs/2211.01301</a></li>
</ul>



<p>The bicycle trajectory coordinates are stored in two separate lists: xs_640x360 and ys640x360:</p>



<figure class="wp-block-image size-large"><img data-attachment-id="8453" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-4-7/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-4.png" data-orig-size="1043,463" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-4" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-4.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-4.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-4.png?w=1024" alt="" class="wp-image-8453" srcset="https://underdark.files.wordpress.com/2023/05/image-4.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-4.png?w=768 768w, https://underdark.files.wordpress.com/2023/05/image-4.png 1043w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<p>This format is kind of similar to the Kaggle Taxi dataset, we worked with in <a href="https://anitagraser.com/2023/05/12/how-to-use-kaggles-taxi-trajectory-data-in-movingpandas/">the previous post</a>. However, to use the solution we implemented there, we need to combine the x and y coordinates into nice (x,y) tuples:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
df&#91;'coordinates'] = df.apply(
    lambda row: list(zip(row&#91;'xs_640x360'], row&#91;'ys_640x360'])), axis=1)
df.drop(columns=&#91;'xs_640x360', 'ys_640x360'], inplace=True)
</pre></div>


<p>Afterwards, we can create the points and compute the proper timestamps from the frame numbers:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
def compute_datetime(row):
    # some educated guessing going on here: the paper states that the video covers 2021-06-09 07:00-08:00
    d = datetime(2021,6,9,7,0,0) + (row&#91;'frame_in'] + row&#91;'running_number']) * timedelta(seconds=2)
    return d
def create_point(xy):
    try: 
        return Point(xy)
    except TypeError:  # when there are nan values in the input data
        return None
new_df = df.head().explode('coordinates')
new_df&#91;'geometry'] = new_df&#91;'coordinates'].apply(create_point)
new_df&#91;'running_number'] = new_df.groupby('id').cumcount()
new_df&#91;'datetime'] = new_df.apply(compute_datetime, axis=1)
new_df.drop(columns=&#91;'coordinates', 'frame_in', 'running_number'], inplace=True)
new_df
</pre></div>


<p>Once the points and timestamps are ready, we can create the MovingPandas TrajectoryCollection. Note how we explicitly state that there is no CRS for this dataset (crs=None):</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
trajs = mpd.TrajectoryCollection(
    gpd.GeoDataFrame(new_df), 
    traj_id_col='id',  t='datetime', crs=None)
</pre></div>


<h2 class="wp-block-heading">Plotting trajectories with image coordinates</h2>



<p>Similarly, to plot these trajectories, we should tell hvplot that it should not fetch any background map tiles (&#8217;tiles&#8217;:None) and that the coordinates are not geographic (&#8216;geo&#8217;:False):</p>



<figure class="wp-block-image size-large"><img data-attachment-id="8467" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-11-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-11.png" data-orig-size="746,550" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-11" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-11.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-11.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-11.png?w=746" alt="" class="wp-image-8467" srcset="https://underdark.files.wordpress.com/2023/05/image-11.png 746w, https://underdark.files.wordpress.com/2023/05/image-11.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-11.png?w=300 300w" sizes="(max-width: 746px) 100vw, 746px" /></figure>



<p>If you want to explore the full source code, you can find my Github fork with the Jupyter notebook at: <a href="https://github.com/anitagraser/desirelines/blob/main/mpd.ipynb" rel="nofollow">https://github.com/anitagraser/desirelines/blob/main/mpd.ipynb</a></p>



<p>The repository also contains a camera image of the intersection, which we can use as a background for our trajectory plots:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
bg_img = hv.RGB.load_image('img/intersection2.png', bounds=(0,0,640,360)) 
</pre></div>


<figure class="wp-block-image size-large"><img data-attachment-id="8466" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-10-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-10.png" data-orig-size="751,492" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-10" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-10.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-10.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-10.png?w=751" alt="" class="wp-image-8466" srcset="https://underdark.files.wordpress.com/2023/05/image-10.png 751w, https://underdark.files.wordpress.com/2023/05/image-10.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-10.png?w=300 300w" sizes="(max-width: 751px) 100vw, 751px" /></figure>



<p>One important caveat is that speed will be calculated in pixels per second. So when we plot the bicycle speed, the segments closer to the camera will appear faster than the segments in the background:</p>



<figure class="wp-block-image size-large"><img data-attachment-id="8450" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-3-7/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-3.png" data-orig-size="812,492" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-3" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-3.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-3.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-3.png?w=812" alt="" class="wp-image-8450" srcset="https://underdark.files.wordpress.com/2023/05/image-3.png 812w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-3.png?w=768 768w" sizes="(max-width: 812px) 100vw, 812px" /></figure>



<p>To fix this issue, we would have to correct for the distortions of the camera lens and perspective. I&#8217;m sure that there is specialized software for this task but, for the purpose of this post, I&#8217;m going to grab the opportunity to finally test out the <a href="https://plugins.qgis.org/plugins/VectorBender/">VectorBender</a> plugin.</p>



<h2 class="wp-block-heading">Georeferencing the trajectories using QGIS VectorBender plugin</h2>



<p>Let&#8217;s load the five test trajectories and the camera image to QGIS. To make sure that they align properly, both are set to the same CRS and I&#8217;ve created the following basic world file for the camera image:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: plain; title: ; notranslate">
1
0
0
-1
0
360
</pre></div>


<p>Then we can use the VectorBender tools to georeference the trajectories by linking locations from the camera image to locations on aerial images. You can see the whole process in action here: </p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe class="youtube-player" width="545" height="307" src="https://www.youtube.com/embed/LP6oKEUgX30?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en&#038;autohide=2&#038;wmode=transparent" allowfullscreen="true" style="border:0;" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation"></iframe>
</div></figure>



<p>After around 15 minutes linking control points, VectorBender comes up with the following georeferenced trajectory result: </p>



<figure class="wp-block-image size-large"><img data-attachment-id="8463" data-permalink="https://anitagraser.com/2023/05/21/analyzing-video-based-bicycle-trajectories/image-9-4/" data-orig-file="https://underdark.files.wordpress.com/2023/05/image-9.png" data-orig-size="1532,1087" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-9" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/05/image-9.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/05/image-9.png?w=545" src="https://underdark.files.wordpress.com/2023/05/image-9.png?w=1024" alt="" class="wp-image-8463" srcset="https://underdark.files.wordpress.com/2023/05/image-9.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=150 150w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=300 300w, https://underdark.files.wordpress.com/2023/05/image-9.png?w=768 768w, https://underdark.files.wordpress.com/2023/05/image-9.png 1532w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<p>Not bad for a quick-and-dirty hack. Some points on the borders of the image could not be georeferenced since I wasn&#8217;t always able to identify suitable control points at the camera image borders. So it won&#8217;t be perfect but should improve speed estimates.</p>



<hr class="wp-block-separator has-alpha-channel-opacity" />



<p>This post is part of a series. Read more about&nbsp;<a href="https://anitagraser.com/movement-data-in-gis/">movement data in GIS.</a></p>



<p></p>
