---
date: '2023-11-16'
draft: 'true'
image: 3d-tiles-in-QGIS.
link: https://lutraconsulting.co.uk/blog/2023/11/16/3d-tiles-in-QGIS/
showcase: planet
source: blog
title: 'Lutra Consulting: 3D-tegels in QGIS'

---
<p>Eerder dit jaar, in samenwerking met <a href="https://north-road.com/2023/06/01/cesium-ecosystem-grant-win-for-qgis-3d-tiles/">North Road</a> kregen we een <a href="https://cesium.com/cesium-ecosystem-grants/grant-directory/">bijdrage van Cesium</a> om ondersteuning voor 3D-tegels in QGIS te introduceren. De mogelijkheid werd met succes ontwikkeld en ingebouwd in QGIS 3.34.</p>

<p>In deze blogpost kunt u meer lezen over hoe met deze mogelijkheid te werken, waar de gegevens te verkrijgen zijn en hoe u uw kaarten in 2D en 3D kunt weergeven. Voor een videodemo van deze mogelijkheid, kunt u <a href="https://www.youtube.com/watch?v=vazJlXTcLsw">de presentatie van Nyall Dawson bekijken op Youtube</a>.</p>

<h1 id="what-are-3d-tiles">Wat zijn 3D-tegels?</h1>

<p>3D-tegels zijn een specificatie voor het stromen en renderen van grootschalige 3D-georuimtelijke gegevenssets. Zij gebruiken een hiërarchische structuur om efficiënt 3D-inhoud te beheren en weer te geven, optimaliseren van uitvoering door het dynamisch laden van de toepasselijke niveaus van detail. Deze technologie wordt breed gebruikt in stedelijke planning, architectuur, simulatie, gamen en virtual reality, wat een gestandaardiseerde en interoperabele oplossing biedt voor het visualiseren van complexe geografische gegevens.</p>

<p>Voorbeelden van 3D-tegels:</p>

<center>
  <p><img title="3D tiles of Zurich from Swisstopo" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_example_1.png" alt="3D tiles of Zurich from Swisstopo" /></p>
  Gegevens van Swisstopo (https://map.geo.admin.ch/)
</center>

<center>
  <p><img title="Washington - 3D Surface Model (Vricon, Cesium)" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_example_2.png" alt="Washington - 3D Surface Model (Vricon, Cesium)" /></p>
  Washington - 3D Surface Model (Vricon, Cesium)
</center>

<h1 id="3d-tiles-in-qgis">3D-tegels in QGIS</h1>

<p>Om 3D-tegels in QGIS te kunnen gebruiken moet u QGIS 3.34 of later hebben. U kunt een nieuwe verbinding naar een 3D-tegelservice maken binnen <strong>Databronnen beheren</strong> onder <strong>Scene</strong>:</p>

<center>
  <p><img title="Adding a new 3D tile service from Data Source Manager in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_data_source_manager.png" alt="Adding a new 3D tile service from Data Source Manager in QGIS" /></p>
  Toevoegen van een nieuwe 3D-tegelservice in Databronnen beheren in QGIS
</center>

<p>Als alternatief kunt u de service toevoegen vanuit uw <strong>paneel Browser</strong>:</p>

<center>
  <p><img title="3D tiles data provider in the Browser panel" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_browser_panel.png" alt="3D tiles data provider in the Browser panel" /></p>
  3D-tegels gegevensprovider in het paneel Browser
</center>

<p>U kunt de volgende 3D-tegelservice gebruiken om de mogelijkheid te testen:</p>

<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>
Naam: Bathurst
URL: https://nsw.digitaltwin.terria.io/api/v0/data/bathurst-reality-mesh-2022-03-29/Scene/Cesium_Bathurst.json

</code></pre></div></div>

<center>
  <p><img title="Creating a new connection to a 3D tiles service" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_scene_bathurst.png" alt="Creating a new connection to a 3D tiles service" /></p>
  Maken van een nieuwe verbinding naar een 3D-tegelservice
</center>

<p>U kunt dan de kaart aan QGIS toevoegen vanuit de nieuwe gemaakte verbinding:</p>

<center>
  <p><img title="Adding a new 3D tiles to QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_bathurst.png" alt="Adding a new 3D tiles to QGIS" /></p>
  Nieuwe 3D-tegels toevoegen aan QGIS
</center>

<p>Standaard wordt de laag opgemaakt met textuur, maar u kunt dat wijzigen om de mazen van het draadmodel achter de schermen te zien:</p>

<center>
  <p><img title="3D tiles’ mesh wireframe" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_mesh_bathurst.png" alt="3D tiles’ mesh wireframe" /></p>
  3D-tegels mazen draadmodel
</center>

<p>U kunt de vulling van mazen en lijnsymbolen wijzigen, soortgelijk als bij vectorpolygonen. Als alternatief kunt u kleuren voor textuur gebruiken. Dat zal elk element van de mazen renderen met de gemiddelde waarde van de volledige textuur. Dat is ideaal voor het afhandelen van een grote gegevensset en een snel overzicht willen van de gegevens:</p>

<center>
  <p><img title="3D tiles with texture color for meshes" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_2d_mesh_styled_bathurst.png" alt="3D tiles with texture color for meshes" /></p>
  3D-tegels met kleur voor textuur voor mazen
</center>

<p>U kunt, om de gegevens in 3D te bekijken, een nieuwe 3D-kaart openen. Soortgelijk aan de 2D-kaart, door in of uit te zoomen, zullen tegels met een fijnere resolutie worden opgehaald en weergegeven:</p>

<center>
   <iframe width="560" height="315" src="https://www.youtube.com/embed/fCnxkzkc3-M?si=oheQwvOZH-0xaZBe&amp;start=11" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen=""></iframe>
</center>

<h1 id="using-data-from-cesium-ion">Gegevens gebruiken van Cesium ion</h1>

<p><a href="https://ion.cesium.com/">Cesium ion</a> is een op de cloud gebaseerd platform voor het beheren en stromen van 3D georuimtelijke gegevens. Het vereenvoudigt gegevensbeheer, visualiseren en delen.</p>

<p>U moet, om 3D-tegels van Cesium ion te kunnen toevoegen, u eerst aanmelden bij hun service hier:
https://ion.cesium.com/tokens</p>

<p>Onder <strong>Asset Depot</strong> zult u een catalogus zien met openbaar beschikbaar gegevenssets. U mag ook uw eigen 3D-modellen uploaden (zoals OBJ of PLY), ze voorzien van geoverwijzingen en ze geconverteerd krijgen naar 3D-tegels.</p>

<p>U kunt ook een van de bestaande tegelservices onder <a href="https://ion.cesium.com/assetdepot">https://ion.cesium.com/assetdepot</a> toevoegen en de tegelservice selecteren en dan klikken op <strong>Add to my assets</strong>:</p>

<center>
  <p><img title="Adding an existing dataset to your Cesium ion assets" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_cesium_ion.png" alt="Adding an existing dataset to your Cesium ion assets" /></p>
  Toevoegen van een bestaande gegevensset aan uw assets van Cesium ion
</center>

<p>U kunt de excellente plug-in voor Cesium ion van <a href="https://plugins.qgis.org/plugins/cesium_ion/">North Road</a> uit de opslagplaats van QGIS gebruiken om de gegevens aan QGIS toe te voegen:</p>

<center>
  <p><img title="Adding Cesium ion assets to QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_cesium_ion_assets.png" alt="Adding Cesium ion assets to QGIS" /></p>
  Tegels van Cesium ion toevoegen aan QGIS
</center>

<h1 id="working-with-google-3d-data">Werken met Google 3D-gegevens</h1>

<p>In aanvulling op de toegang tot Google Photorealistic 3D-tegels van Cesium ion, kunt u ook direct tegels toevoegen in QGIS. Als eerste zult u de instructies hieronder moeten volgen en API-sleutels verkrijgen voor 3D-tegels:
<a href="https://developers.google.com/maps/documentation/tile/cloud-setup">https://developers.google.com/maps/documentation/tile/cloud-setup</a></p>

<p>Gedurende het registratieproces zult u worden gevraagd om de gegevens van uw creditcard toe te voegen. Momenteel (november 2023) brengen ze nog geen kosten in rekening voor het gebruiken van de service.</p>

<p>Als u eenmaal de API-sleutel hebt verkregen, kunt u tegels van Google toevoegen met de volgende details voor de verbinding:</p>

<center>
  <p><img title="Adding Google 3D tiles in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_google_connection.png" alt="Adding Google 3D tiles in QGIS" /></p>
  Google Photorealistic-tegels toevoegen in QGIS
</center>

<h1 id="notes-and-remarks">Notities en opmerkingen</h1>

<ul>
  <li><strong>Kaartbereiken aanpassen voor grote scenes</strong></li>
</ul>

<p>Bij het behandelen van grote scenes, zouden kaartbereiken moeten kunnen worden ingesteld op een kleiner gebied om het in 3D te kunnen bekijken. Dat is de huidige beperking van QGIS 3D-kaarten, omdat het geen scenes kan behandelen die groter zijn dan 500 x 500 km.</p>

<p>U kunt, om het kaartbereik te wijzigen <strong>Projecteigenschappen</strong> openen en onder <strong></strong> het bereik wijzigen. In het voorbeeld hieronder is het kaartbereik beperkt tot slechts een deel van Londen, dus kunnen we de Google Photorealistic-tegels in de 3D-kaart bekijken zonder problemen met renderen.</p>

<center>
  <p><img title="Limiting project extent in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_map_extent.png" alt="Limiting project extent in QGIS" /></p>
  Bereik project beperken in QGIS
</center>

<center>
  <p><img title="3D tiles from Google in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_map_3d_london.png" alt="3D tiles from Google in QGIS" /></p>
  3D-tegels van Google in QGIS
</center>

<ul>
  <li><strong>Grootte netwerk cache</strong></li>
</ul>

<p>Als u een grote gegevensset behandelt, wordt aanbevolen om de grootte van de netwerkcache te verhogen tot 1 GB of meer. De standaard waarde in QGIS is veel lager en dat resulteert in heel traag renderen van de gegevens.</p>

<center>
  <p><img title="Increasing Cache size in QGIS for faster rendering" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_network_cache.png" alt="Increasing Cache size in QGIS for faster rendering" /></p>
  Grootte van de cache verhogen in QGIS voor sneller renderen
</center>

<ul>
  <li><strong>Andere 3D-gegevens overleggen</strong></li>
</ul>

<p>Wanneer u probeert andere gegevenssets te overleggen bovenop globale 3D-tegels, zou de verticale datum niet overeen kunnen komen en zult u daarom de gegevens op een verkeerde plaats in de 3D-kaart zien. U moet, om het probleem op te lossen, de verschuiving voor de hoogte onder Laageigenschappen gebruiken om de gegevens alsnog langs de Z-as te verschuiven:</p>

<center>
  <p><img title="Offsetting elevation of a layer in QGIS" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_elevation_offset.png" alt="Offsetting elevation of a layer in QGIS" /></p>
  Hoogte van een laag verschuiven in QGIS
</center>

<h1 id="future-works">Werk voor de toekomst</h1>

<p>Dit is de eerste implementatie van de 3D-tegels in QGIS. In de toekomst zouden we meer mogelijkheden willen toevoegen voor het behandelen en maken van de 3D-tegels. Onze wensenlijst, in een willekeurige volgorde, is:</p>

<ul>
  <li>Weergave als wereldbol: QGIS 3D kan geen grote scenes of niet geprojecteerde weergaven behandelen.</li>
  <li>Meer geavanceerd opmaken van mazen: als een voorbeeld: gebruikers zouden hun eigen stijl willen maken.</li>
  <li>3D indoor-navigatie: als een voorbeeld: gebruikers willen in staat zijn binnen gebouwen te navigeren en het zal potentieel BIM-gegevens dichter bij QGIS brengen.</li>
  <li>Genereren van 3D-tegels binnen QGIS: toevoegen van ene verwerkingsprogramma in QGIS om 3D-tegels te maken uit uw kaartgegevens.</li>
</ul>

<center>
  <p><img title="Styling of 3D tiles" src="https://lutraconsulting.co.uk/img/posts/3d_tiles_3d_styled_mesh.png" alt="Styling of 3D tiles" /></p>
  opmaken van 3D-tegels (afbeelding vanaf https://cesium.com/learn/ion/stories-styling/)
</center>

<p>Als u deze mogelijkheden in QGIS zou willen zien en bij wilt dragen aan de inspanningen, aarzel dan niet om <a href="mailto:info@lutraconsulting.co.uk">contact met ons op te nemen</a>.</p>

