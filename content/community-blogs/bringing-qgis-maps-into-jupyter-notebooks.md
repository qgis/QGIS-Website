---
source: "blog"
title: "anitagraser.com: Bringing QGIS maps into Jupyter notebooks"
image: "bringing-qgis-maps-into-jupyter-notebooks."
date: "2023-11-10"
link: "https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/"
draft: "true"
showcase: "planet"
---

<p>Earlier this year, we explored how to use <a href="https://anitagraser.com/2023/01/21/pyqgis-jupyter-notebooks-on-windows-using-conda/">PyQGIS in Juypter notebooks</a> to run QGIS Processing tools from a notebook and visualize the Processing results using GeoPandas plots.</p>



<p>Today, we&#8217;ll go a step further and replace the GeoPandas plots with maps rendered by QGIS. </p>



<p>The following script presents a minimum solution to this challenge: initializing a QGIS application, canvas, and project; then loading a GeoJSON and displaying it: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from IPython.display import Image

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication

from qgis.core import QgsApplication, QgsVectorLayer, QgsProject, QgsSymbol, \
    QgsRendererRange, QgsGraduatedSymbolRenderer, \
    QgsArrowSymbolLayer, QgsLineSymbol, QgsSingleSymbolRenderer, \
    QgsSymbolLayer, QgsProperty
from qgis.gui import QgsMapCanvas

app = QApplication(&#91;])
qgs = QgsApplication(&#91;], False)
canvas = QgsMapCanvas()
project = QgsProject.instance()

vlayer = QgsVectorLayer("./data/traj.geojson", "My trajectory")
if not vlayer.isValid():
    print("Layer failed to load!")

def saveImage(path, show=True): 
    canvas.saveAsImage(path)
    if show: return Image(path)

project.addMapLayer(vlayer)
canvas.setExtent(vlayer.extent())
canvas.setLayers(&#91;vlayer])
canvas.show()
app.exec_()

saveImage("my-traj.png")
</pre></div>


<p>When this code is executed, it opens a separate window that displays the map canvas. And in this window, we can even pan and zoom to adjust the map. The line color, however, is assigned randomly (like when we open a new layer in QGIS):</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-21.png"><img width="912" height="853" data-attachment-id="8567" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-21-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-21.png" data-orig-size="912,853" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-21" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-21.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-21.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-21.png?w=912" alt="" class="wp-image-8567" srcset="https://underdark.files.wordpress.com/2023/11/image-21.png 912w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=768 768w" sizes="(max-width: 912px) 100vw, 912px" /></a></figure>



<p>To specify a specific color, we can use: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
vlayer.renderer().symbol().setColor(QColor("red"))

vlayer.triggerRepaint()
canvas.show()
app.exec_()
saveImage("my-traj.png")
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-22.png"><img loading="lazy" width="899" height="547" data-attachment-id="8568" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-22-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-22.png" data-orig-size="899,547" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-22" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-22.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-22.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-22.png?w=899" alt="" class="wp-image-8568" srcset="https://underdark.files.wordpress.com/2023/11/image-22.png 899w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=768 768w" sizes="(max-width: 899px) 100vw, 899px" /></a></figure>



<p>But regular lines are boring. We could easily create those with GeoPandas plots.</p>



<p>Things get way more interesting when we use QGIS&#8217; custom symbols and renderers. For example, to draw arrows using a QgsArrowSymbolLayer, we can write: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
vlayer.renderer().symbol().appendSymbolLayer(QgsArrowSymbolLayer())

vlayer.triggerRepaint()
canvas.show()
app.exec_()
saveImage("my-traj.png")
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-23.png"><img loading="lazy" width="897" height="537" data-attachment-id="8570" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-23-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-23.png" data-orig-size="897,537" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-23" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-23.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-23.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-23.png?w=897" alt="" class="wp-image-8570" srcset="https://underdark.files.wordpress.com/2023/11/image-23.png 897w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=768 768w" sizes="(max-width: 897px) 100vw, 897px" /></a></figure>



<p>We can also create a QgsGraduatedSymbolRenderer: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
geom_type = vlayer.geometryType()
myRangeList = &#91;]

symbol = QgsSymbol.defaultSymbol(geom_type)
symbol.setColor(QColor("#3333ff"))
myRange = QgsRendererRange(0, 1, symbol, 'Group 1')
myRangeList.append(myRange)

symbol = QgsSymbol.defaultSymbol(geom_type)
symbol.setColor(QColor("#33ff33"))
myRange = QgsRendererRange(1, 3, symbol, 'Group 2')
myRangeList.append(myRange)

myRenderer = QgsGraduatedSymbolRenderer('speed', myRangeList)
vlayer.setRenderer(myRenderer)

vlayer.triggerRepaint()
canvas.show()
app.exec_()
saveImage("my-traj.png")
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-24.png"><img loading="lazy" width="901" height="800" data-attachment-id="8572" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-24-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-24.png" data-orig-size="901,800" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-24" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-24.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-24.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-24.png?w=901" alt="" class="wp-image-8572" srcset="https://underdark.files.wordpress.com/2023/11/image-24.png 901w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=768 768w" sizes="(max-width: 901px) 100vw, 901px" /></a></figure>



<p>And we can combine both QgsGraduatedSymbolRenderer and QgsArrowSymbolLayer:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
geom_type = vlayer.geometryType()
myRangeList = &#91;]

symbol = QgsSymbol.defaultSymbol(geom_type)
symbol.appendSymbolLayer(QgsArrowSymbolLayer())
symbol.setColor(QColor("#3333ff"))
myRange = QgsRendererRange(0, 1, symbol, 'Group 1')
myRangeList.append(myRange)

symbol = QgsSymbol.defaultSymbol(geom_type)
symbol.appendSymbolLayer(QgsArrowSymbolLayer())
symbol.setColor(QColor("#33ff33"))
myRange = QgsRendererRange(1, 3, symbol, 'Group 2')
myRangeList.append(myRange)

myRenderer = QgsGraduatedSymbolRenderer('speed', myRangeList)
vlayer.setRenderer(myRenderer)

vlayer.triggerRepaint()
canvas.show()
app.exec_()
saveImage("my-traj.png")
</pre></div>


<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-25.png"><img loading="lazy" width="898" height="889" data-attachment-id="8574" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-25/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-25.png" data-orig-size="898,889" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-25" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-25.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-25.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-25.png?w=898" alt="" class="wp-image-8574" srcset="https://underdark.files.wordpress.com/2023/11/image-25.png 898w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=768 768w" sizes="(max-width: 898px) 100vw, 898px" /></a></figure>



<p>Maybe the most powerful option is to use data-defined symbology. For example, to control line width and color: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
renderer = QgsSingleSymbolRenderer(QgsSymbol.defaultSymbol(geom_type))

exp_width = 'scale_linear("speed", 0, 3, 0, 7)'
exp_color = "coalesce(ramp_color('Viridis',scale_linear(\"speed\", 0, 3, 0, 1)), '#000000')"

# https://qgis.org/pyqgis/3.0/core/Symbol/QgsSymbolLayer.html?highlight=property#qgis.core.QgsSymbolLayer.PropertySize
renderer.symbol().symbolLayer(0).setDataDefinedProperty(
    QgsSymbolLayer.PropertyStrokeWidth, QgsProperty.fromExpression(exp_width))
renderer.symbol().symbolLayer(0).setDataDefinedProperty(
    QgsSymbolLayer.PropertyStrokeColor, QgsProperty.fromExpression(exp_color))
renderer.symbol().symbolLayer(0).setDataDefinedProperty(
    QgsSymbolLayer.PropertyCapStyle, QgsProperty.fromExpression("'round'"))

vlayer.setRenderer(renderer)

vlayer.triggerRepaint()
canvas.show()
app.exec_()
saveImage("my-traj.png")
</pre></div>


<p></p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-26.png"><img loading="lazy" width="904" height="842" data-attachment-id="8575" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-26/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-26.png" data-orig-size="904,842" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-26" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-26.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-26.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-26.png?w=904" alt="" class="wp-image-8575" srcset="https://underdark.files.wordpress.com/2023/11/image-26.png 904w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=768 768w" sizes="(max-width: 904px) 100vw, 904px" /></a></figure>



<p>Find the full notebook at: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/layer-styling.ipynb" rel="nofollow">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/layer-styling.ipynb</a></p>



<p></p>
