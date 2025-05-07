---
date: '2023-11-10'
draft: 'true'
image: bringing-qgis-maps-into-jupyter-notebooks.
link: https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/
showcase: planet
source: blog
title: 'anitagraser.com:  QGIS kaarten naar Jupyter notebooks brengen'

---
<p>Eerder dit jaar verkenden we hoe <a href="https://anitagraser.com/2023/01/21/pyqgis-jupyter-notebooks-on-windows-using-conda/">PyQGIS in Juypter notebooks</a> te gebruiken om gereedschappen van QGIS Processing uit te voeren vanuit een notebook en de resultaten van processing te visualiseren met plots van GeoPandas.</p>

<p>Vandaag gaan we ene stap verder en vervangen de plots van GeoPandas door kaarten die zijn gerenderd door QGIS. </p>

<p>Het volgende script presenteert een minimale oplossing voor deze uitdaging: initialiseren van een toepassing voor QGIS, kaartvenster en project; daarna een GeoJSON laden en die weergeven: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from IPython.display import Image

from PyQt5.QtGui import QColor from PyQt5.QtWidgets import QApplication

from qgis.core import QgsApplication, QgsVectorLayer, QgsProject, QgsSymbol, <br />QgsRendererRange, QgsGraduatedSymbolRenderer, <br />QgsArrowSymbolLayer, QgsLineSymbol, QgsSingleSymbolRenderer, <br />QgsSymbolLayer, QgsProperty from qgis.gui import QgsMapCanvas

app = QApplication(&#91;]) qgs = QgsApplication(&#91;], False) canvas = QgsMapCanvas() project = QgsProject.instance()

vlayer = QgsVectorLayer("./data/traj.geojson", "My trajectory") if not vlayer.isValid(): print("Layer failed to load!")

def saveImage(path, show=True): canvas.saveAsImage(path) if show: return Image(path)

project.addMapLayer(vlayer) canvas.setExtent(vlayer.extent()) canvas.setLayers(&#91;vlayer]) canvas.show() app.exec_()

saveImage("my-traj.png") </pre></div>

<p>Als deze code wordt uitgevoerd, opent het een afzonderlijk venster dat het kaartvenster weergeeft. En in dat venster kunnen we zelfs verschuiven en zoomen om de kaart aan te passen. De lijnkleur wordt echter willekeurig toegewezen (zoals wanneer we een nieuwe laag in QGIS openen):</p>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-21.png"><img loading="lazy" width="912" height="853" data-attachment-id="8567" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-21-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-21.png" data-orig-size="912,853" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-21" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-21.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-21.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-21.png?w=912" alt="" class="wp-image-8567" srcset="https://underdark.files.wordpress.com/2023/11/image-21.png 912w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-21.png?w=768 768w" sizes="(max-width: 912px) 100vw, 912px" /></a></figure>

<p>We kunnen, om een specifieke kleur te specificeren, gebruiken: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
vlayer.renderer().symbol().setColor(QColor("red"))

vlayer.triggerRepaint() canvas.show() app.exec_() saveImage("my-traj.png") </pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-22.png"><img loading="lazy" width="899" height="547" data-attachment-id="8568" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-22-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-22.png" data-orig-size="899,547" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-22" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-22.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-22.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-22.png?w=899" alt="" class="wp-image-8568" srcset="https://underdark.files.wordpress.com/2023/11/image-22.png 899w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-22.png?w=768 768w" sizes="(max-width: 899px) 100vw, 899px" /></a></figure>

<p>Maar normale lijnen zijn saai. We zouden die gemakkelijk kunnen maken met plots van GeoPandas.</p>

<p>Dingen worden al vele interessanter als we aangepaste sym,bolen en renderers van QGIS gebruiken. Bijvoorbeeld, om pijlen te tekenen met QgsArrowSymbolLayer, kunnen we schrijven: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
vlayer.renderer().symbol().appendSymbolLayer(QgsArrowSymbolLayer())

vlayer.triggerRepaint() canvas.show() app.exec_() saveImage("my-traj.png") </pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-23.png"><img loading="lazy" width="897" height="537" data-attachment-id="8570" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-23-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-23.png" data-orig-size="897,537" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-23" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-23.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-23.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-23.png?w=897" alt="" class="wp-image-8570" srcset="https://underdark.files.wordpress.com/2023/11/image-23.png 897w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-23.png?w=768 768w" sizes="(max-width: 897px) 100vw, 897px" /></a></figure>

<p>We kunnen ook een QgsGraduatedSymbolRenderer maken: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
geom_type = vlayer.geometryType()
myRangeList = &#91;]

symbol = QgsSymbol.defaultSymbol(geom_type) symbol.setColor(QColor("#3333ff")) myRange = QgsRendererRange(0, 1, symbol, 'Group 1') myRangeList.append(myRange)

symbol = QgsSymbol.defaultSymbol(geom_type) symbol.setColor(QColor("#33ff33")) myRange = QgsRendererRange(1, 3, symbol, 'Group 2') myRangeList.append(myRange)

myRenderer = QgsGraduatedSymbolRenderer('speed', myRangeList) vlayer.setRenderer(myRenderer)

vlayer.triggerRepaint() canvas.show() app.exec_() saveImage("my-traj.png") </pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-24.png"><img loading="lazy" width="901" height="800" data-attachment-id="8572" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-24-2/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-24.png" data-orig-size="901,800" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-24" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-24.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-24.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-24.png?w=901" alt="" class="wp-image-8572" srcset="https://underdark.files.wordpress.com/2023/11/image-24.png 901w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-24.png?w=768 768w" sizes="(max-width: 901px) 100vw, 901px" /></a></figure>

<p>En we kunnen beide combineren QgsGraduatedSymbolRenderer en QgsArrowSymbolLayer:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
geom_type = vlayer.geometryType()
myRangeList = &#91;]

symbol = QgsSymbol.defaultSymbol(geom_type) symbol.appendSymbolLayer(QgsArrowSymbolLayer()) symbol.setColor(QColor("#3333ff")) myRange = QgsRendererRange(0, 1, symbol, 'Group 1') myRangeList.append(myRange)

symbol = QgsSymbol.defaultSymbol(geom_type) symbol.appendSymbolLayer(QgsArrowSymbolLayer()) symbol.setColor(QColor("#33ff33")) myRange = QgsRendererRange(1, 3, symbol, 'Group 2') myRangeList.append(myRange)

myRenderer = QgsGraduatedSymbolRenderer('speed', myRangeList) vlayer.setRenderer(myRenderer)

vlayer.triggerRepaint() canvas.show() app.exec_() saveImage("my-traj.png") </pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-25.png"><img loading="lazy" width="898" height="889" data-attachment-id="8574" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-25/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-25.png" data-orig-size="898,889" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-25" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-25.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-25.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-25.png?w=898" alt="" class="wp-image-8574" srcset="https://underdark.files.wordpress.com/2023/11/image-25.png 898w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-25.png?w=768 768w" sizes="(max-width: 898px) 100vw, 898px" /></a></figure>

<p>Misschien is wel de meest krachtige optie om data-bepaalde symbologie te gebruiken. Bijvoorbeeld om lijnbreedte en -kleur te beheren: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
renderer = QgsSingleSymbolRenderer(QgsSymbol.defaultSymbol(geom_type))

exp_width = 'scale_linear("speed", 0, 3, 0, 7)' exp_color = "coalesce(ramp_color('Viridis',scale_linear(\"speed\", 0, 3, 0, 1)), '#000000')"
# https://qgis.org/pyqgis/3.0/core/Symbol/QgsSymbolLayer.html?highlight=property#qgis.core.QgsSymbolLayer.PropertySize
renderer.symbol().symbolLayer(0).setDataDefinedProperty( QgsSymbolLayer.PropertyStrokeWidth, QgsProperty.fromExpression(exp_width)) renderer.symbol().symbolLayer(0).setDataDefinedProperty( QgsSymbolLayer.PropertyStrokeColor, QgsProperty.fromExpression(exp_color)) renderer.symbol().symbolLayer(0).setDataDefinedProperty( QgsSymbolLayer.PropertyCapStyle, QgsProperty.fromExpression("'round'"))

vlayer.setRenderer(renderer)

vlayer.triggerRepaint() canvas.show() app.exec_() saveImage("my-traj.png") </pre></div>

<p></p>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-26.png"><img loading="lazy" width="904" height="842" data-attachment-id="8575" data-permalink="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/image-26/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-26.png" data-orig-size="904,842" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-26" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-26.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-26.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-26.png?w=904" alt="" class="wp-image-8575" srcset="https://underdark.files.wordpress.com/2023/11/image-26.png 904w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-26.png?w=768 768w" sizes="(max-width: 904px) 100vw, 904px" /></a></figure>

<p>U kunt het gehele notebook vinden op: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/layer-styling.ipynb" rel="nofollow">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/layer-styling.ipynb</a></p>

<p></p>

