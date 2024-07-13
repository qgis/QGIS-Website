---
source: "blog"
title: "anitagraser.com: New MovingPandas tutorial: taking OGC Moving Features full circle with MF-JSON"
image: "new-movingpandas-tutorial-taking-ogc-moving-features-full-circle-with-mf-json."
date: "2024-07-06"
link: "https://anitagraser.com/2024/07/08/new-movingpandas-tutorial-taking-ogc-moving-features-full-circle-with-mf-json/"
draft: "true"
showcase: "planet"
---

<figure class="wp-block-image size-large"><img alt="" class="wp-image-9114" height="131" src="https://anitagraser.com/wp-content/uploads/2024/07/movingpandas-1.png?w=545" tabindex="0" width="545" /></figure>



<p>Last week, I had the pleasure to meet some of the people behind the OGC Moving Features Standard Working group at the IEEE Mobile Data Management Conference (MDM2024). While chatting about the Moving Features (MF) support in <a href="https://movingpandas.org">MovingPandas</a>, I realized that, after the <a href="https://anitagraser.com/2022/04/23/mf-json-update-tutorial-with-official-sample/">MF-JSON update &amp; tutorial with official sample</a> post, we never published a complete tutorial on working with <a href="https://docs.ogc.org/is/19-045r3/19-045r3.html">MF-JSON</a> encoded data in <a href="https://movingpandas.org">MovingPandas</a>. </p>



<figure class="wp-block-image size-large"><img alt="" class="wp-image-9084" height="88" src="https://anitagraser.com/wp-content/uploads/2024/07/image-9-1.png?w=186" tabindex="0" width="186" /></figure>



<p>The current MovingPandas development version (to be release as version 0.19) supports:</p>



<ul class="wp-block-list">
<li>Reading <a href="https://github.com/opengeospatial/mf-json/tree/master/json-sample/movingpoint">MF-JSON MovingPoint</a> (single trajectory features and trajectory collections)</li>



<li>Reading <a href="https://github.com/opengeospatial/mf-json/tree/master/json-sample/trajectory">MF-JSON Trajectory</a></li>



<li>Writing MovingPandas Trajectories and TrajectoryCollections to MF-JSON MovingPoint </li>
</ul>



<p>This means that we can now go full circle: reading &#8212; writing &#8212; reading. </p>



<h2 class="wp-block-heading">Reading MF-JSON </h2>



<p>Both MF-JSON MovingPoint encoding and Trajectory encoding can be read using the MovingPandas function <code>read_mf_json()</code>. The complete Jupyter notebook for this tutorial is available <a href="https://github.com/movingpandas/movingpandas/blob/main/tutorials/8-ogc-moving-features.ipynb">in the project repo</a>.</p>



<p>Here we read one of the official <a href="https://github.com/opengeospatial/mf-json/tree/master/json-sample/movingpoint">MF-JSON MovingPoint</a> sample files: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
traj = mpd.read_mf_json('data/movingfeatures.json')
</pre></div>


<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/07/image-10.png"><img alt="" class="wp-image-9089" height="819" src="https://anitagraser.com/wp-content/uploads/2024/07/image-10.png?w=613" tabindex="0" width="613" /></a></figure>



<h2 class="wp-block-heading">Writing MF-JSON</h2>



<p>To write MF-JSON, the Trajectory and TrajectoryCollection classes provide a <code>to_mf_json()</code> function:</p>



<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/07/image-11.png"><img alt="" class="wp-image-9090" height="694" src="https://anitagraser.com/wp-content/uploads/2024/07/image-11.png?w=615" tabindex="0" width="615" /></a></figure>



<p>The resulting Python dictionary in MF-JSON MovingPoint encoding can then be saved to a JSON file, and then read again:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import json
with open('mf1.json', 'w') as json_file:
    json.dump(mf_json, json_file, indent=4)
</pre></div>


<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/07/image-12.png"><img alt="" class="wp-image-9091" height="397" src="https://anitagraser.com/wp-content/uploads/2024/07/image-12.png?w=610" tabindex="0" width="610" /></a></figure>



<p>Similarly, we can read any arbitrary trajectory data set and save it to MF-JSON.</p>



<p>For example, here we use our usual Geolife sample: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
gdf = gp.read_file('data/demodata_geolife.gpkg')
tc = mpd.TrajectoryCollection(gdf, 'trajectory_id', t='t')
mf_json = tc.to_mf_json(temporal_columns=&#91;'sequence'])
</pre></div>


<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/07/image-13.png"><img alt="" class="wp-image-9092" height="680" src="https://anitagraser.com/wp-content/uploads/2024/07/image-13.png?w=612" tabindex="0" width="612" /></a></figure>



<h2 class="wp-block-heading">And reading again</h2>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import json
with open('mf5.json', 'w') as json_file:
    json.dump(mf_json, json_file, indent=4)
tc = mpd.read_mf_json('mf5.json', traj_id_property='trajectory_id' )
</pre></div>


<figure class="wp-block-image size-large"><a href="https://anitagraser.com/wp-content/uploads/2024/07/image-14.png"><img alt="" class="wp-image-9093" height="574" src="https://anitagraser.com/wp-content/uploads/2024/07/image-14.png?w=613" tabindex="0" width="613" /></a></figure>



<h2 class="wp-block-heading">Conclusion</h2>



<p>The implemented MF-JSON support covers the basic usage of the encodings. There are some fine details in the standard, such as the distinction of time-varying attribute with linear versus step-wise interpolation, which MovingPandas currently does not support. </p>



<p>If you are working with movement data, I would appreciate if you can give the improved MF-JSON support a spin and <a href="https://github.com/movingpandas/movingpandas/discussions">report back with your experiences</a>. </p>



<p></p>



<p></p>
