---
date: '2023-11-15'
draft: 'true'
image: adding-basemaps-to-pyqgis-maps.
link: https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/
showcase: planet
source: blog
title: 'anitagraser.com: basiskaarten toevoegen aan kaarten van PyQGIS in Jupyter
  notebooks'

---
<p>In de vorige post onderzochten we hoe <a href="https://anitagraser.com/2023/11/10/bringing-qgis-maps-into-jupyter-notebooks/">kaarten van QGIS in Jupyter notebooks te brengen</a>.</p>

<p>Vandaag nemen we de volgende stap en voegen basiskaarten toe aan onze kaarten. Dit is iets ingewikkelder dan ik had verwacht. In het bijzonder moest ik ene gevecht leveren met &#8220;ongeldige&#8221; OSM tegellagen, totdat ik mij realiseerde dat mijn instantie van de toepassing QGIS, op een of andere manier, de proivder &#8220;WMS&#8221; miste. </p>

<p>In aanvulling daarop betekent het werkend krijgen van basiskaarten ook dat we rekening moeten houden met de CRSen van laag en project en direct opnieuw projecteren. Laten we dus aan het werk gaan:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
from IPython.display import Image
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from qgis.core import QgsApplication, QgsVectorLayer, QgsProject, QgsRasterLayer, \
    QgsCoordinateReferenceSystem, QgsProviderRegistry, QgsSimpleMarkerSymbolLayerBase
from qgis.gui import QgsMapCanvas
app = QApplication(&#91;])
qgs = QgsApplication(&#91;], False)
qgs.setPrefixPath(r"C:\temp", True)  # instellen van een pad zal de provider WMS inschakelen
qgs.initQgis()
canvas = QgsMapCanvas()
project = QgsProject.instance()
map_crs = QgsCoordinateReferenceSystem('EPSG:3857')
canvas.setDestinationCrs(map_crs)
print("providers: ", QgsProviderRegistry.instance().providerList())
</pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-28.png"><img loading="lazy" width="906" height="767" data-attachment-id="8586" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-28/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-28.png" data-orig-size="906,767" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-28" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-28.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-28.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-28.png?w=906" alt="" class="wp-image-8586" srcset="https://underdark.files.wordpress.com/2023/11/image-28.png 906w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-28.png?w=768 768w" sizes="(max-width: 906px) 100vw, 906px" /></a></figure>

<p>Voor het toevoegen van een OSM basiskaart gebruiken we de optie XYZ tegels van de WMS provider: </p>

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

<p>Als er problemen zijn met de provider WMS, zou <code>rlayer.error().summary()</code> dat aan moeten geven. </p>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-29.png"><img loading="lazy" width="905" height="614" data-attachment-id="8589" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-29/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-29.png" data-orig-size="905,614" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-29" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-29.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-29.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-29.png?w=905" alt="" class="wp-image-8589" srcset="https://underdark.files.wordpress.com/2023/11/image-29.png 905w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-29.png?w=768 768w" sizes="(max-width: 905px) 100vw, 905px" /></a></figure>

<p>met zowel de vectorlaag als de basismap gereed, kunnen we eindelijk de kaart plotten: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
canvas.setExtent(rlayer.extent())
plot_layers(&#91;vlayer,rlayer])
</pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-30.png"><img loading="lazy" width="903" height="642" data-attachment-id="8591" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-30/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-30.png" data-orig-size="903,642" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-30" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-30.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-30.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-30.png?w=903" alt="" class="wp-image-8591" srcset="https://underdark.files.wordpress.com/2023/11/image-30.png 903w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-30.png?w=768 768w" sizes="(max-width: 903px) 100vw, 903px" /></a></figure>

<p>Natuurlijk kunnen we creatiever zijn en <a href="https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis-101-styling-vector-layers/">onze vector lagen opmaken</a>:</p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
vlayer.renderer().symbol().setColor(QColor("yellow"))
vlayer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
vlayer.renderer().symbol().symbolLayer(0).setSize(10)
plot_layers(&#91;vlayer,rlayer])
</pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-31.png"><img loading="lazy" width="891" height="680" data-attachment-id="8592" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-31/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-31.png" data-orig-size="891,680" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-31" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-31.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-31.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-31.png?w=891" alt="" class="wp-image-8592" srcset="https://underdark.files.wordpress.com/2023/11/image-31.png 891w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-31.png?w=768 768w" sizes="(max-width: 891px) 100vw, 891px" /></a></figure>

<p>En om te wisselen met andere basiskaarten hoeven we alleen de URL maar overeenkomstig bij te werken, bijvoorbeeld om in plaats daarvan Carto-tegels te laden: </p>

<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
urlWithParams = 'type=xyz&url=http://basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png&zmax=19&zmin=0&crs=EPSG3857'
rlayer2 = QgsRasterLayer(urlWithParams, 'Carto', 'wms')  
print(rlayer2.crs())
if rlayer2.isValid():
    project.addMapLayer(rlayer2)
else:
    print('invalid layer')
    print(rlayer2.error().summary()) 

plot_layers(&#91;vlayer,rlayer2]) </pre></div>

<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/11/image-32.png"><img loading="lazy" width="902" height="839" data-attachment-id="8594" data-permalink="https://anitagraser.com/2023/11/17/adding-basemaps-to-pyqgis-maps/image-32/" data-orig-file="https://underdark.files.wordpress.com/2023/11/image-32.png" data-orig-size="902,839" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-32" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/11/image-32.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/11/image-32.png?w=545" src="https://underdark.files.wordpress.com/2023/11/image-32.png?w=902" alt="" class="wp-image-8594" srcset="https://underdark.files.wordpress.com/2023/11/image-32.png 902w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=150 150w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=300 300w, https://underdark.files.wordpress.com/2023/11/image-32.png?w=768 768w" sizes="(max-width: 902px) 100vw, 902px" /></a></figure>

<p>U kunt het gehele notebook vinden op: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/basemaps.ipynb" rel="nofollow">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/basemaps.ipynb</a></p>

<p></p>

