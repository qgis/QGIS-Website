---
source: "blog"
title: "anitagraser.com: Tracking geoprocessing workflows with QGIS & DVC"
image: "tracking-geoprocessing-workflows-with-qgis-dvc."
date: "2023-02-25"
link: "https://anitagraser.com/2023/02/25/tracking-geoprocessing-workflows-with-qgis-dvc/"
draft: "true"
showcase: "planet"
---

<p>Today&#8217;s post is a geeky deep dive into how to leverage <a href="http://dvc.org/">DVC (not just) data version control</a> to track QGIS geoprocessing workflows.</p>



<p>&#8220;Why is this great?&#8221; you may ask. </p>



<p>DVC tracks data, parameters, and code. If anything changes, we simply rerun the process and DVC will figure out which stages need to be recomputed and which can be skipped by re-using cached results.</p>



<p>This can lead to huge time savings compared to re-running the whole model</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png"><img data-attachment-id="8376" data-permalink="https://anitagraser.com/2023/02/25/tracking-geoprocessing-workflows-with-qgis-dvc/qgis-model-to-dvc-stages3/" data-orig-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png" data-orig-size="1501,444" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="qgis-model-to-dvc-stages3" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=545" src="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=1024" alt="" class="wp-image-8376" srcset="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=150 150w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=300 300w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png?w=768 768w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages3.png 1501w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>You can find the source code used in this post on my repo <a href="https://github.com/anitagraser/QGIS-resources/tree/dvc">https://github.com/anitagraser/QGIS-resources/tree/dvc</a></p>



<p>I&#8217;m using DVC with the DVC plugin for VSCode but DVC can be used completely from the command line, if you prefer this appraoch.</p>



<p>Basically, what follows is a proof of concept: converting a QGIS Processing model to a DVC workflow. In the following screenshot, you can see the main stages</p>



<ol>
<li>The QGIS model in the upper left corner</li>



<li>The Python script exported from the QGIS model builder in the lower left corner</li>



<li>The DVC stages in my <code>dvc.yaml</code> file in the upper right corner (And please ignore the hello world stage. It&#8217;s a left over from my first experiment)</li>



<li>The DVC DAG visualizing the sequence of stages. Looks similar to the QGIS model, doesn&#8217;t it ;-)</li>
</ol>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png"><img data-attachment-id="8374" data-permalink="https://anitagraser.com/2023/02/25/tracking-geoprocessing-workflows-with-qgis-dvc/qgis-model-to-dvc-stages/" data-orig-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png" data-orig-size="2497,1439" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="qgis-model-to-dvc-stages" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=545" src="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=1024" alt="" class="wp-image-8374" srcset="https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=1024 1024w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=2048 2048w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=150 150w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=300 300w, https://underdark.files.wordpress.com/2023/02/qgis-model-to-dvc-stages.png?w=768 768w" sizes="(max-width: 1024px) 100vw, 1024px" /></a></figure>



<p>Besides the stage definitions in <code>dvc.yaml</code>, there&#8217;s a parameters file:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
random-points:
  n: 10
buffer-points:
  size: 0.5
</pre></div>


<p>And, of course, the two stages, each as it&#8217;s own Python script.</p>



<p>First, <code>random-points.py</code> which reads the <code>random-points.n</code> parameter to create the desired number of points within the polygon defined in <code>qgis3/data/test.geojson</code>:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import dvc.api

from qgis.core import QgsVectorLayer
from processing.core.Processing import Processing
import processing

Processing.initialize()

params = dvc.api.params_show()
pts_n = params&#91;'random-points']&#91;'n']

input_vector = QgsVectorLayer("qgis3/data/test.geojson")
output_filename = "qgis3/output/random-points.geojson"

alg_params = {
    'INCLUDE_POLYGON_ATTRIBUTES': True,
    'INPUT': input_vector,
    'MAX_TRIES_PER_POINT': 10,
    'MIN_DISTANCE': 0,
    'MIN_DISTANCE_GLOBAL': 0,
    'POINTS_NUMBER': pts_n,
    'SEED': None,
    'OUTPUT': output_filename
}
processing.run('native:randompointsinpolygons', alg_params)
</pre></div>


<p>And second, <code>buffer-points.py</code> which reads the <code>buffer-points.size</code> parameter to buffer the previously generated points:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import dvc.api
import geopandas as gpd
import matplotlib.pyplot as plt

from qgis.core import QgsVectorLayer
from processing.core.Processing import Processing
import processing

Processing.initialize()

params = dvc.api.params_show()
buffer_size = params&#91;'buffer-points']&#91;'size']

input_vector = QgsVectorLayer("qgis3/output/random-points.geojson")
output_filename = "qgis3/output/buffered-points.geojson"

alg_params = {
    'DISSOLVE': False,
    'DISTANCE': buffer_size,
    'END_CAP_STYLE': 0,  # Round
    'INPUT': input_vector,
    'JOIN_STYLE': 0,  # Round
    'MITER_LIMIT': 2,
    'SEGMENTS': 5,
    'OUTPUT': output_filename
}
processing.run('native:buffer', alg_params)

gdf = gpd.read_file(output_filename)
gdf.plot()

plt.savefig('qgis3/output/buffered-points.png')
</pre></div>


<p>With these things in place, we can use dvc to run the workflow, either from within VSCode or from the command line. Here, you can see the workflow (and how dvc skips stages and fetches results from cache) in action: </p>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe class="youtube-player" width="545" height="307" src="https://www.youtube.com/embed/f2BL2ISmXAc?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en&#038;autohide=2&#038;wmode=transparent" allowfullscreen="true" style="border:0;" sandbox="allow-scripts allow-same-origin allow-popups allow-presentation"></iframe>
</div></figure>



<p>If you try it out yourself, let me know what you think. </p>



<p></p>
