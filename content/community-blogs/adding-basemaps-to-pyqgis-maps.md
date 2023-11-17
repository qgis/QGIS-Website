---
source: "blog"
title: "anitagraser.com: Adding basemaps to PyQGIS maps"
image: "adding-basemaps-to-pyqgis-maps."
date: "2023-11-15"
link: "https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/"
draft: "true"
showcase: "planet"
---

<p>In the previous post, we investigated how to <a href="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/">bring QGIS maps into Jupyter notebooks</a>.</p>



<p>Today, we&#8217;ll take the next step and add basemaps to our maps. This is trickier than I would have expected. In particular, I was fighting with &#8220;invalid&#8221; OSM tile layers until I realized that my QGIS application instance somehow lacked the &#8220;WMS&#8221; provider. </p>



<p>In addition, getting basemaps to work also means that we have to take care of layer and project CRSes and on-the-fly reprojections. So let&#8217;s get to work:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from IPython.display import Image
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject, QgsRasterLayer, \
    QgsCoordinateReferenceSystem, QgsProviderRegistry, QgsSimpleMarkerSymbolLayerBase
from qgis.gui import QgsMapCanvas

app = QApplication(&#91;])
qgs = QgsApplication(&#91;], False)
qgs.setPrefixPath(r"C:\temp", True)  # setting a prefix path should enable the WMS provider
qgs.initQgis()
canvas = QgsMapCanvas()
project = QgsProject.instance()
map_crs = QgsCoordinateReferenceSystem('EPSG:3857')
canvas.setDestinationCrs(map_crs)

print("providers: ", QgsProviderRegistry.instance().providerList())
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-28.png"><img width="906" height="767" data-attachment-id="8586" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-28/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-28.png" data-orig-size="906,767" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-28" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-28.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-28.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-28.png?w=906" alt="" class="wp-image-8586" srcset="https://underdark.files.wordpress.com/2023/11/image-28.png 906w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=768 768w" sizes="(max-width: 906px) 100vw, 906px" /></a></figure>



<p>To add an OSM basemap, we use the xyz tiles option of the WMS provider: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
urlWithParams = 'type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0&crs=EPSG3857'
rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  
print(rlayer.crs())
if rlayer.isValid():
    project.addMapLayer(rlayer)
else:
    print('invalid layer')
    print(rlayer.error().summary()) 
</pre></div>


<p>If there are issues with the WMS provider, <code>rlayer.error().summary()</code> should point them out. </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-29.png"><img width="905" height="614" data-attachment-id="8589" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-29/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-29.png" data-orig-size="905,614" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-29" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-29.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-29.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-29.png?w=905" alt="" class="wp-image-8589" srcset="https://underdark.files.wordpress.com/2023/11/image-29.png 905w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=768 768w" sizes="(max-width: 905px) 100vw, 905px" /></a></figure>



<p>With both the vector layer and the basemap ready, we can finally plot the map: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-30.png"><img width="903" height="642" data-attachment-id="8591" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-30/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-30.png" data-orig-size="903,642" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-30" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-30.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-30.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-30.png?w=903" alt="" class="wp-image-8591" srcset="https://underdark.files.wordpress.com/2023/11/image-30.png 903w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=768 768w" sizes="(max-width: 903px) 100vw, 903px" /></a></figure>



<p>Of course, we can get more creative and <a href="https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis-101-styling-vector-layers/">style our vector layers</a>:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-31.png"><img loading="lazy" width="891" height="680" data-attachment-id="8592" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-31/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-31.png" data-orig-size="891,680" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-31" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-31.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-31.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-31.png?w=891" alt="" class="wp-image-8592" srcset="https://underdark.files.wordpress.com/2023/11/image-31.png 891w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=768 768w" sizes="(max-width: 891px) 100vw, 891px" /></a></figure>



<p>And to switch to other basemaps, we just need to update the URL accordingly, for example, to load Carto tiles instead: </p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-32.png"><img loading="lazy" width="902" height="839" data-attachment-id="8594" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-32/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-32.png" data-orig-size="902,839" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-32" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-32.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-32.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-32.png?w=902" alt="" class="wp-image-8594" srcset="https://underdark.files.wordpress.com/2023/11/image-32.png 902w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=768 768w" sizes="(max-width: 902px) 100vw, 902px" /></a></figure>



<p>You can find the whole notebook at: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/basemaps.ipynb" rel="nofollow">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/basemaps.ipynb</a></p>



<p></p>
