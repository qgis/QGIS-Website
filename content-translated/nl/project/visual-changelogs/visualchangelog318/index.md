---
HasBanner: false
draft: false
releaseDate: 19-02-2021
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.18
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.18{#changelog318 }
![image1](images/projects/606afcefcc3f5fd4ff00db9b4cb04b22485044db.png)

Datum uitgave 19-02-2021

Following on from the feature-filled releases of [QGIS 3.14](https://qgis.org/en/site/forusers/visualchangelog314/) and [QGIS 3.16](https://qgis.org/en/site/forusers/visualchangelog316/), QGIS 3.18 introduces a host of enhancements and new features, along with a long-awaited feature - Native Point Cloud support in QGIS! Thanks to the efforts of [Lutra](https://www.lutraconsulting.co.uk/), [North Road](https://north-road.com/), and [Hobu](https://hobu.co/), QGIS is now able to import and render point cloud data in various formats by leveraging the Open Source PDAL library. This functionality has been introduced due to the success of a [crowd-funding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/) and would not have been possible without the support of the QGIS community and contributors. Thank you to all those involved in realizing this incredible milestone!

Omdat QGIS Desktop 3.18 afscheid heeft genomen van de databaseprovider DB2, introduceert het ondersteuning voor de gebruikers van het databasesysteem van SAP HANA.

The QGIS ecosystem has also seen some exciting changes in the form of the [QGIS HUB](https://plugins.qgis.org/) which is an extension of the plugin site which now supports the distribution of community developed [styles](https://plugins.qgis.org/styles/), [projects](https://plugins.qgis.org/geopackages/), and even [processing models](https://plugins.qgis.org/models/).

<div style="position:relative;width:100%;height:0;padding-bottom:56.25%"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%" src="https://www.youtube.com/embed/Yeo6sXVpXvA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;" allowfullscreen></iframe></div>

We would also like to extend a big thank you to the developers, documenters, testers, and all the many folks out there who volunteer their time and effort (or fund people to do so) to make these releases possible. From the QGIS community, we hope you enjoy this release! If you wish to donate time, money, or otherwise get involved in making QGIS more awesome, please wander along to [QGIS.ORG](https://www.qgis.org/) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://www.qgis.org/en/site/about/sustaining_members.html#list-of-donors). If you would like to become an official project sustaining member, please visit our [sustaining member page](https://www.qgis.org/en/site/getinvolved/governance/sustaining_members/sustaining_members.html#qgis-sustaining-memberships) for details. Sponsoring QGIS helps us to fund our regular developer meetings, maintain project infrastructure, and fund bug fixing efforts. A complete list of current sponsors is provided below - our very great thank you to all of our sponsors!

{{<fund type="active" >}}

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruiken ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken, ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Gebruikersinterface
### Mogelijkheid: Afgeleide attributen in Identificatie-resultaten verbergen
Eerder liet het QGIS Desktop  gereedschap *Identificeren* een groot aantal afgeleide attributen zien, zoals informatie over de geometrie. Hoewel bijzonder waardevol is voor veel gebruiksgevallen die informatie te langdradig. Gebruikers hebben nu de optie om te schakelen met de weergave van de afgeleide attributen om een meer beperkte weergave van de Identificatie-resultaten weer te geven.

![image2](images/entries/96178054-1aa78d80-0f2f-11eb-8d75-299bfd6aa73e.webp)

![image3](images/entries/c9eea14d2c01670795967bd1e42fcb8777330718.webp)

This feature was developed by [Richard Duivenvoorde](https://api.github.com/users/rduivenvoorde)
### Mogelijkheid: Alle tabs van de interface voor Logberichten in één keer sluiten
The QgsMessageLogViewer now includes an **\"Empty tab and close others\"** to the log viewer panel context menu, supporting a quicker action to a clean interface when debugging.

![image4](images/entries/5adbd9ce0bfeb73ec308ed003603aacceab728d4.webp)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Mogelijkheid: API voor bronwidgets van lagen
An API has been added in the provider GUI to allow a provider to create a custom widget, which exposes options to customize and change the layer\'s source. For example, a file-based layer provider could expose a widget for selecting a new file path, or an online provider could expose widgets for changing the host or authentication information.

Hiervoor zijn twee implementaties toegevoegd:
1. Een widget bestandskiezer voor op GDAL op bestand gebaseerde lagen.
2. Een widget voor het aanpassen van eigenschappen van XYZ-lagen.

![image5](images/entries/24c8af6d1314e7a22f8f70a7628f3aeae9b3ce1a-1.webp)

![image6](images/entries/14df1b85a3e3ada3024a39499a245bbdd7e2ca64-1.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: GUI voor dynamische SVG's
QGIS now supports dynamic standard vector graphic elements, as outlined in [QEP #199](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/199). This allows QGIS to dynamically replace attributes or node values in the XML of the SVG and apply data-driven values to SVG elements. QGIS Desktop has additionally added a GUI editor to ensure that users are able to properly leverage this new functionality.

![image7](images/entries/c6d55ffc6be5f0e4962d9b971cac6e54ab316717.webp)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud](https://api.github.com/users/3nids)
### Mogelijkheid: Zoomen naar meerdere lagen
The \"Zoom to Layer\" function available from the context menu, the View menu and the Map Navigation toolbar can now zoom to the extent of all the selected layers in the layer tree.

![image8](images/entries/101234295-f1cc8a80-368b-11eb-9b52-8f42a4f994a2.gif)

This feature was developed by [Patrice Pineault](https://api.github.com/users/TurboGraphxBeige)
### Mogelijkheid: Zoomen en verschuiven naar selectie voor meerdere lagen
The \"Zoom to Selection\" and \"Pan Map to Selection\" functions available from the context menu, the View menu or the Map Navigation toolbox now offer the ability to navigate to the extent of the selection from the selected layers in the layer tree.

![image9](images/entries/a76fca5cfc367779584da0655cd18474e4518329-1.gif)

This feature was developed by [Patrice Pineault](https://api.github.com/users/TurboGraphxBeige)
### Mogelijkheid: In-/uitzoomen met scrollwiel van de muis in de kaart van het paneel Overzichtskaart
Gebruikers kunnen nu in- en uitzoomen in het paneel Overzichtskaart met het scrollwiel van de muis.

![image10](images/entries/77b55b4c85c9c4f5076b1a735f7971819cc2a2ee.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Toegankelijkheid
### Mogelijkheid: Verbeterde simulatie kleurenblindheid
Dit past de eerdere ondersteuning voor grijswaarden en op LMS gebaseerde simulatie voor protanopie en deuteranopie, wat het in lijn brengt met de toegepaste methodologie die momenteel wordt gebruikt in Chromium en Firefox. QGIS gebruikt nu bijgewerkte berekeningen voor helderheid in grijswaarden (hernoemd naar achromatopsie), een vooraf berekende matrix voor protanopie (hernoemd vanuit protanope), een vooraf berekende matrix voor deuteranopie (hernoemd vanuit deuteranope), en een aanvullende modus voor tritanopie met een soortgelijke een vooraf berekende matrix.

This feature was developed by [Will Cohen](https://api.github.com/users/willcohen)
### Mogelijkheid: Widget Rotatie voor de Georeferencer
Het kaartvenster van Georeferencer kan nu worden gedraaid om het plaatsen van de verwijzingpunten te faciliteren. Dit is in het bijzonder nuttig voor gescande afbeeldingen die geen uniforme oriëntaties zouden kunnen hebben.

![image11](images/entries/aba35ba4bb5ff0f2a8c1afcb55673e496efea18a.gif)

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
## Symbologie
### Mogelijkheid: Data-bepaalde doorzichtbaarheid voor alle symbolen
Waar het eerder mogelijk was om de doorzichtbaarheid voor kleuren van individuele symboollagen in te stellen via data-bepaalde expressies, is het nu mogelijk om een data-bepaalde expressie in te stellen om de doorzichtbaarheid voor alle symbolen in te stellen.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Galerij Stijlen openen vanuit Stijlmanager
The Style Manager interface now includes a button to open the [styles gallery](https://plugins.qgis.org/styles/) from the QGIS HUB.

![image12](images/entries/0d6dd72f8089ee52196001751451d42c7107fbe8.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Mazen
### Mogelijkheid: Nieuwe algoritmes voor exporteren van lagen met mazen
Nieuwe opties voor exporteren zijn toegevoegd voor lagen met mazen. Deze staan de volgende opties toe bij het exporteren van een laag met mazen naar een vectorlaag:
- Zijden mazen exporteren
- Randen mazen exporteren (1D mazen)
- Mazen op raster exporteren

![image13](images/entries/4738ffe8180f8fc320cf464121ec10fc27bd4c33.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
### Mogelijkheid: Eigen export voor lagen met mazen
Eerdere versies van QGIS vereisten het gebruiken van de plug-in Crayfish, echter, die functionaliteit is nu ingebouwd in de bron van QGIS en stelt gebruikers in staat lagen met mazen te exporteren naar vectoren en de waarde van de gegevensset toe te voegen als een attribuut.

![image14](images/entries/41bdfc3d3c6afabc0e3e23986e42dbc22eb794df.gif)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
### Mogelijkheid: Vereenvoudigen van mazen voor 3D 
Gegevens voor mazen kunnen nu worden vereenvoudigd door een niveau voor het detail voor het renderen van 3D te definiëren. Dit helpt bij de uitvoering voor complexe gegevenssets en zorgt voor een gladdere ervaring als navigatie voor 3D is vereist.

![image15](images/entries/6461d329ef7d4936ddbc932b0bf96edcb071b398.gif)

This feature was developed by [Vincent Cloarec](https://api.github.com/users/vcloarec)
### Mogelijkheid: Meerdere eigen algoritmes voor Processing voor lagen met mazen
Een aantal nieuwe algoritmes voor Processing zijn geporteerd vanuit de plug-in Crayfish, inclusief:
- Gegevensset laag met mazen rasteriseren
- Contouren exporteren naar vectorlagen
- Exporteer waarden van gegevensset die gedeelte kruisen naar tekstbestand (csv)
- Exporteer waarden van tijdreeksen naar tekstbestand (csv)

![image16](images/entries/3acf2cfe05dc7550f16e183026350914d028a6da.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/projects/mdal/)
## Renderen
### Feature: \"Merged feature\" renderer for polygon and line layers
A new rendering option allows area and line features to be \"dissolved\" into a single object prior to rendering to ensure that complex symbols or overlapping features are represented by a uniform and contiguous cartographic symbol.

![image17](images/entries/4f1a29b4c0552c362d0bd87f3034af0ef07b642c.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Slimmer opnieuw tekenen van kaart
Previously, map redraws would attempt to redraw all elements in the frame. The map rendering has been significantly improved and now the existing map frame elements are used during the redraw process. This work was completed as a part of [QEP #181](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/181) and was funded by the QGIS Grant program for 2020.

De volgende weergave laat het opnieuw tekenen zien vóór de verbetering:

![image18](images/entries/7d0a503ab9ae05427e42e2987335ef569c761a3e-1.gif)

This feature was funded by [QGIS grant 2020](https://qgis.org/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
## 3D-objecten
### Mogelijkheid: Eye dome lighting
Eye dome lighting (EDL) is een effect voor nabewerking dat de diepte van elke pixel (afstand vanaf de camera) vergelijkt met de diepte van naburige pixels en accentueert randen overeenkomstig de berekende verschillen.

Een element voor configuratie van EDL is toegevoegd aan de tab Opties van het dialoogvenster voor configuratie van de 3D-weergave. EDL sterkte heeft het effect van vergroten van het contrast, wat betere perceptie van de diepte (wat nodig kan zijn om aan te passen bij inzoomen) mogelijk maakt. EDL-afstand is de afstand van de gebruikte pixels vanaf de middelste pixel en heeft het effect van het dikker maken van randen.

The eye dome lighting is, by principle, an image-based rendering solution similar to SSAO (screen space ambient occlusion), and therefore works on the whole scene and doesn\'t differ between point clouds or regular 3D objects.

![image19](images/entries/4e7b365e9e991bf06f15a3ad15ff50a0ac9692e2.webp)

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Nedjima Belgacem)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Data-bepaalde kleuren 3D-materiaal
Kleuren voor 3D-materiaal kunnen nu data-bepaald worden, wat het mogelijk maakt dat kleuren van objecten worden bepaald door de waarde van een attribuut of expressie.

Renderen van polygonen kan nu worden gedaan met meerdere typen materiaal, die elk een verschillend uiterlijk en configuratie van keuren hebben:
- Realistisch (Phong) materiaal - berekent met 3 kleuren (diffuus, omgeving, gespiegeld), dat de configuratie voor verlichting van de 3D-weergave gebruikt
- CAD (Gooch) materiaal - berekent met 4 kleuren (diffuus, warm, koel, spiegelend), dat de configuratie voor de verlchting van de 3D-weergave negeert

Materiaal met textuur wordt op dit moment niet ondersteund.

![image20](images/entries/97449982-9da1ee00-1908-11eb-9276-32c863c3f6e1.webp)

![image21](images/entries/504010202dcff6a9b78450fedfa493b6e726b5c0.webp)

This feature was funded by [Kristianstad](https://www.kristianstad.se)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Ondersteuning voor 3D orthografische projectie
QGIS biedt nu ondersteuning voor orthografische projectie voor 3D-scenes, een mogelijkheid die vaak is gewenst in de context van architectuur, archeologie, en meer.

![image22](images/entries/7e43323cea578f6f50e83de6307c22bdef948f8d.gif)

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Puntenwolken
### Mogelijkheid: Ondersteuning voor puntenwolken
Following the successful [crowdfunding campaign](https://www.lutraconsulting.co.uk/crowdfunding/pointcloud-qgis/) for point cloud support in QGIS, the engineers at Lutra, North Road, and Hobu have been able to introduce the ability for QGIS to import and render point cloud data.

Dit omvat de mogelijkheid om lagen met puntenwolken toe te voegen aan projecten van QGIS, met ondersteuning voor de indeling EPT, en ze te renderen in 2D- en 3D-context.

![image23](images/entries/3d87d5647d363b53b1a19ffd67de7406632df572.webp)

This feature was funded by [Point Cloud data support in QGIS](https://www.lutraconsulting.co.uk/blog/2021/02/18/qgis-3-18-point-cloud/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Puntenwolken toevoegen aan browser
De QGIS Browser en interface voor het beheren van databronnen ondersteunen nu de basisstructuur van door PDAL ondersteunde lagen met puntenwolken.

![image24](images/entries/96aca5c2d2f428f0aa7fee0d11b5c8600c5c523c.webp)

This feature was funded by [Point Cloud data support in QGIS crowd funding campaign](https://www.lutraconsulting.co.uk/blog/2021/02/18/qgis-3-18-point-cloud/)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Integratie van PDAL-provider ontvlechten 
Ability to generate EPT index for (smaller) laz files directly in QGIS via the [untwine](https://github.com/hobu/untwine) library

This feature was funded by [Point Cloud data support in QGIS crowd funding campaign](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Peter Petrik)](https://www.lutraconsulting.co.uk)
## Afdruklay-outs
### Mogelijkheid: Op kleurverlopen gebaseerde legenda's
A new QgsColorRampLegendNode class was added which allows for the creation of color ramp-based legend nodes. It\'s now used for raster layers when using a pseudocolor renderer with the linear interpolation type or for the single-band gray renderer, as well as for point clouds using a ramp based renderer.

In een legenda van een lay-out erft het item kleurenbalk de breedte en hoogte van het standaard legendasymbool, maar het is optioneel mogelijk dat gedrag te overschrijven.

Er zijn labels opgenomen voor de minimum en maximum waarde van de kleurenbalk, die worden gerenderd met dezelfde instellingen voor het lettertype als andere tekst voor het item Legenda:

![image25](images/entries/86e6d57200857c701d9438eabe246289e74f5194-1.gif)

Uitlijnen van de labels volgt de instellingen voor Legenda:

![image26](images/entries/7c80cc107b0e3fb1098d416834463478367b555e-1.gif)

En, uiteraard, werken de items netjes in legenda's met meerdere kolommen:

![image27](images/entries/145e2d7f00d3a2b33f383e3cbd808a6b21a792c4-1.gif)

![image28](images/entries/0dad8d8307a3c3fe1f5b28aa56790b307c090f33-1.gif)

This feature was funded by [Hans van der Kwast](https://www.youtube.com/c/HansvanderKwast)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Verbeteringen voor kleurverlopen legenda
Legenda-items voor kleurenbalken ondersteunen nu de volgende te configureren opties:
- Een voor- en achtervoegsel voor de tekst van de kleurenbalk
- Numerieke opmaak
- Richting kleurenbalk
- Aanpassen van de opmaak van de tekst
- De mogelijkheid om horizontale balken te maken.

Gebruikers kunnen er ook voor kiezen om deze instellingen te verfijnen voor een bepaald Legenda-itm in de lay-out. Deze functionaliteit is beschikbaar voor alle items van balken, inclusief raster-, puntenwolkenlagen, of lagen met mazen.

![image29](images/entries/9a48f9d2970e50c7d4f70358b6cfd870033427a5-1.gif)

![image30](images/entries/fb52826e81fd08763c269aaab50ea0c25b7af9b8-1.gif)

This feature was funded by [Hans van der Kwast](https://www.youtube.com/c/HansvanderKwast)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Dynamische voorkeuzen tekst
The new *Add Item -\> Dynamic Text* menu contains preset dynamic text expressions that users can use to insert a label automatically containing the corresponding expression.

For example, using the dynamic text element **Layout Name** will insert a label containing the expression \[% \@layout_name %\]. This improves the feature awareness, discoverability, and provides an easy method for users to access dynamic attributes.

![image31](images/entries/c41a7d2a5ec018bfba237429aa5d125d11ad9310.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Expressies
### Mogelijkheid: Optionele opmaak voor resultaten van UUID
There is now a string format parameter available for the `uuid()` function in QGIS expressions. Users now have various options that they can use to stipulate the format of the returned UUID value, including the following options:
- `uuid()`: **{0bd2f60f-f157-4a6d-96af-d4ba4cb366a1}**
- `uuid('WithoutBraces')`: **0bd2f60f-f157-4a6d-96af-d4ba4cb366a1**
- `uuid('Id128')`: **0bd2f60ff1574a6d96afd4ba4cb366a1**

![image32](images/entries/3f0471353b72cffc4b69defb87cea2d7a1c44017.webp)

Deze mogelijkheid werd ontwikkeld door [signedav](https://api.github.com/users/signedav)
### Mogelijkheid: Variabele laag-CRS in expressies
QGIS expressions now support a *layer_crs* variable which will return the AuthID for a particular layer\'s coordinate reference system. This allows expressions to identify the layer CRS dynamically and perform transformations without needing to manually specify the CRS.

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Mogelijkheid: Ondersteuning voor functies min, max, meerderheid, som, gemiddelde en mediaan in numerieke arrays
Expressies in QGIS bevatten nu functies voor samenvoegen voor arrays, wat het eenvoudig ophalen mogelijk maakt van specifieke waarden uit een array die zouden kunnen worden gebruikt in elementen van QGIS, zoals symbologieën. De volgende functies werden geïntroduceerd:
- array_min
- array_max
- array_majority
- array_sum
- array_mean
- array_median

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
### Feature: Negative index for array_get function
The function array_get now supports the use of negative index positions.

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Feature: Add map_credits function
A *map_credits* function was added that collates a list of all the layer metadata attribution strings for the layers shown inside a specified map item.

Bijvoorbeeld:

    array_to_string( map_credits( 'Main Map' ) )
    
Returns a comma-separated list of layer credits for layers shown in the \'Main Map\' layout item, e.g \'CC-BY-NC, CC-BY-SA\'

There\'s an optional *include_layer_names* argument you can use to include layer names before their attribution:

    array_to_string( map_credits( 'Main Map',
       include_layer_names := true,
       layer_name_separator := ': ' ) )
    
This would return a comma-separated list of layer names and their credits for layers shown in the \'Main Map\' layout item, e.g. \'Railway lines: CC-BY-NC, Basemap: CC-BY-SA\'

Dit werd mogelijk gemaakt door [SLYR](https://north-road.com/slyr/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Digitaliseren
### Mogelijkheid: Contextmenu Objecten selecteren 
Het is nu mogelijk objecten te selecteren met een contextmenu in het kaartvenster. Klikken met rechts op de kaart zal intelligent de objecten onder de muiscursor identificeren en het mogelijk maken de beschikbare objecten toe te voegen of te verwijderen uit de huidige selectie. Waar meerdere objecten beschikbaar zijn zou een korte vertraging op kunnen treden, terwijl het systeem probeert te zoeken naar beschikbare objecten die in een genest menu-item beschikbaar komen voor selecteren, of gebruikers kunnen eenvoudigweg de functie *Alles selecteren* gebruiken om alle beschikbare objecten te selecteren op de  opgegeven positie.

![image33](images/entries/edec99086412445b929c0926f69600279e56d4fb.gif)

This feature was funded by [Kristianstad](https://www.kristianstad.se)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Instellingen voor traceren boog toegevoegd aan UI
Existing curve tracing settings [were introduced previously](https://github.com/qgis/QGIS/pull/37826) and have now been exposed in the user interface to enable users to incrementally modify settings to optimize their results when capturing curve data.

![image34](images/entries/29b75d5574181d5b7570090b9801ede92bec2fcd.webp)

This feature was developed by [Olivier Dalang](https://api.github.com/users/olivierdalang)
### Mogelijkheid: Gereedschap Object op schaal brengen
A new digitizing tool allows for selected features to be scaled when in editing mode. This implementation was based on the work of [\@roya0045](https://github.com/roya0045) with [#40650](https://github.com/qgis/QGIS/pull/40650).

![image35](images/entries/16ac8bca1e78da740dc8ea8b6b46a916f8f0b83d.gif)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Gegevensbeheer
### Mogelijkheid: Nieuw algoritme voor exporteren naar werkblad
Gebruikers kunnen een selectie van vectorlagen exporteren als bladen in een nieuw werkbladdocument of ze toevoegen als aanvullende werkbladen aan een bestaand werkbladdocument

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Coördinaten opnieuw projecteren in de Georeferencer
De Georeferencer  projecteert nu gegevenspunten opnieuw in een gewenste projectie voor de uitvoer, in plaats van het CRS van het kaartvenster te gebruiken voor het bepalen van de posities van de gegevenspunten. Dit geeft gebruikers meer flexibiliteit en beheer bij het vastleggen van controlepunten.

![image36](images/entries/50d4d1d6353ebfa251c53ea29c28821bf4c5ac18.gif)

This feature was developed by [Alex](https://api.github.com/users/roya0045)
### Mogelijkheid: Polymorfische relaties/ Document beheerssysteem
A new GUI is available to manage polymorphic relations, implemented as a part of the dynamic relations described in [QEP #79](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/79).

The \"Add relation\" button in the relation manager screen now has additional options for adding and editing polymorphic relations:

The \"Add polymorphic relation\" and \"Edit polymorphic relation\" open the same dialog, although in the latter case it will automatically be populated with existing values.

Eenmaal opgeslagen verschijnt de lijst met relaties als een widget Boom, waarin de gemaakte relatie-objecten voor een polymorfische relatie verschijnen als kinderen. De namen van de gemaakte relaties kunnen niet worden gewijzigd.

Polymorfische relaties worden opgeslagen binnen een project en kunnen momenteel niet worden geëxporteerd.

![image37](images/entries/6628cd483a00a52f51cd963febd883d2756eb299.webp)

This feature was developed by [Ivan Ivanov](https://api.github.com/users/suricactus)
## Formulieren en widgets
### Mogelijkheid: Zachte en harde beperkingen in formulieren
Historically, required fields would prevent a form from being saved entirely. Using soft constraints allow forms to notify users that expected information has been omitted, without preventing the form submission. Hard constraints, by contrast, function identically to the previous \"required fields\" functionality and will prevent form submissions unless data is correctly captured for the field.

This feature was funded by [Lutra Consulting](https://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting (Viktor Sklencar)](https://www.lutraconsulting.co.uk)
## Analyse-gereedschappen
### Mogelijkheid: Nominatim geocoder API
Although not exposed through the locator or as an algorithm, QGIS now includes a Nominatim API geocoder class. The geocoder class\' implementation insures that it respects the OpenStreetMap Foundation Terms of Use by caching results and throttling requests by default.

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
## Processing
### Mogelijkheid: Expressie toestaan voor velden voor volgorde in algoritme Punten naar pad
`$id` may be used as an expression for a csv with ordered values, and the `ORDER_EXPRESSION` parameter has been added to the PointsToPath algorithm.

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Mogelijkheid: CRS overschrijven voor uitvoer van Raster op bereik clippen
In some instances, the **Clip raster by extent** algorithm may output features without a CRS specified, which can now be modified by explicitly enforcing the output to inherit it\'s CRS from the input layer.

This feature was developed by [rldhont](https://api.github.com/users/rldhont)
### Feature: Add \"retain fields\" algorithm
Allows users to select a list of fields to keep, and all other fields will be dropped from the layer. Helps with making flexible models where input datasets may have a range of different fields and only a certain subset of them need to be retained. This work was inspired by [#39114](https://github.com/qgis/QGIS/pull/39114)

![image38](images/entries/c02ae93517a537925c870d3a9d477cc26af5f9e7.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Parameter voor verwijzing naar gemeenschappelijk veld voor meerdere lagen
Parameters voor velden in gereedschappen van Processing kunnen het verwerken van een gemeenschappelijk veld voor meerdere vectorlagen ondersteunen, in een implementatie die is geïnspireerd op het gedrag van enkele algoritmen voor Processing in Orfeo ToolBox.

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Feature: Extend import geotagged photos to include exif_orientation
The \"Import geotagged photos\" tool has been updated so that the exif_orientation parameter value is extracted to the output table. This ensures that maptips and other HTML widgets can be configured to correctly transform the photos to be correctly displayed based on the orientation value.

This feature was developed by [Pelle Rosenbeck Gøeg](https://api.github.com/users/pellegoeg)
### Mogelijkheid: Algoritme Informatie van lagen exporteren 
Een nieuw algoritme in de Toolbox van Processing, genaamd Informatie van lagen exporteren, is toegevoegd om het maken te ondersteunen van een polygoonlaag, die overeenkomt met het bereik van gebruikergedefinieerde la(a)g(en) met aanvullende details voor de laag die als attributen aan elk object polygoon worden gehecht. De verzamelde informatie ondersteunt momenteel de volgende elementen:
- CRS
- Naam provider 
- Bestandspad
- Laagnaam
- Filter subset
- Samenvatting
- Naamsvermelding

This feature was developed by [Mathieu Pellerin](https://api.github.com/users/nirvn)
### Mogelijkheid: Algoritmes Percentiel stapelen cellen en Rang percentage gestapelde cellen 
De karakteristieken van het gereedschap voor Processing **Celstatistieken** is opnieuw vorm gegeven en aangepast om het mogelijk te maken drie nieuwe algoritmes voor Processing toe te voegen, die QGIS in staat stellen om celstatistieken te berekenen op een soortgelijke manier als voor veel voorkomende functies voor percentages in programma's met werkbladen. De nieuwe algoritmes voor Processing zijn:
- **Percentiel stapelen cellen**
- **Rang percentage gestapelde cellen uit waarde**
- **Rang percentage gestapelde cellen uit rasterlaag**

Waar het algoritme voor het percentiel alleen de mogelijkheid beidt voor het berekenen van percentielen gebaseerd op een invoer fractiewaarde (liggend tussen 0 en 1), kan een rang percentage voor een raster ook worden berekend gebaseerd op een raster met invoerwaarden. Dit geeft de gebruiker de mogelijkheid om rangen van percentages te berekenen per cel, gebaseerd op invoer van waarden uit een gegevensset (bijv. monsterlagen).

Alle algoritmes verschaffen verschillende methoden voor het berekenen van percentielen en rangen percentage:

**Percentile:** - Nearest Rank - Inclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTILE.INC* function) - Exclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTILE.EXC* function)

**Percentrank:** - Inclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTRANK.INC* function) - Exclusive linear interpolation (see LibreOffice\'s and Microsoft Excel\'s *PERCENTRANK.EXC* function)

![image39](images/entries/febde74bab33bb165971509e90fb112c4b643001.webp)

This feature was developed by [Clemens Raffler](https://api.github.com/users/root676)
### Mogelijkheid: Algoritme voor Processing Punten naar lijn
Een eigen algoritme voor Processing in C++ is toegevoegd dat lijnlagen maakt uit puntlagen, soortgelijk aan de bestaande *Punten naar pad* voor Python, maar met uitgebreide functionaliteit:
- Added support for *natural sorting* ( \'10\' \> \'9\' )
- Maken van ongeldige lijnen met een enkel punt vermijden
- Maken van gesloten lijnen met twee punten vermijden

This feature was developed by [uclaros](https://api.github.com/users/uclaros)
## Opties voor toepassing en projecten
### Mogelijkheid: Verborgen lagen
Projecten van QGIS ondersteunen nu het opnemen van verborgen lagen, wat het mogelijk maakt ze op te nemen in een project, maar dat ze niet zichtbaar zijn in de inhoudsopgave.

De  eigenschap voor de laag is te configureren op de tab **Databronnen** van de projecteigenschappen en bevat ondersteuning van de API voor filteren van tekst.

![image40](images/entries/95af3e621abc52bc04d94eca629279df2b987961.gif)

Dit werd mogelijk gemaakt door **ARPA Piemonte**

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Custom \"Full Extent\" definition
A new \"View Settings\" tab has been added to the project properties, with the option to manually defined the full extent of a project. The extent defined here will be the extent used when zooming to the full map extent, instead of the calculated or maximum extent of all layers. This is useful for defining a particular area of interest for a project and does not limit user\'s ability to \"zoom out\" further than the defined extent.

![image41](images/entries/d0109e9db23e15765f201c3b292f23fa4230b608.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Netwerk cachen schakelen naar QgsNetworkAccessManager
Een keuzevak in het paneel Gereedschap voor debuggen/ontwikkeling staat gebruikers nu toe om tijdelijk de cache van het netwerk uit te schakelen, wat nuttig is bij het debuggen van activiteiten van QGIS op het netwerk, of bij het gebruiken van QGIS om wijzigingen aan de kant van de server te testen.

Dit is ontworpen als een vluchtige instelling en wordt vergeten zodra QGIS wordt afgesloten.

![image42](images/entries/0115a38666f35166fa9e6fd53791a7bc8f73b6dc.webp)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Browser
### Mogelijkheid: Verbindingen in browser voor ArcGis Feature Service en ArcGIS Map Service geünificeerd
The separate \"ArcGis Feature Service\" and \"ArcGIS Map Service\" browser connections have been replaced with a single, unified, **\"ArcGIS Rest Servers\"** connection and browser node, which shows a definitive view of the server and exposes both service types.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: Bladeren door ArcGIS REST door groepen voor inhoud toestaan
Verbindingen voor ArcGIS Feature Service die hun overeenkomende URL's voor het Portal-eindpunt hebben ingesteld kunnen worden verkend door groepen voor inhoud in het paneel Browser.

If a connection has the Portal endpoints set, then expanding out the connection in the browser will show a \"Groups\" and \"Services\" folder, instead of the full list of services usually shown. Expanding out the groups folder will show a list of all content groups that the user is a member of, each of which can be expanded to show the service items belonging to that group.

This feature was funded by [SRK Consulting](https://www.srk.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Gegevensproviders
### Mogelijkheid: Eigen algoritme voor exporteren DXF
Maakt het exporteren van individuele of meerdere lagen naar één enkel DXF-bestand mogelijk. Voor elke invoerlaag kan de gebruiker selecteren welk attribuut moet worden gebruikt voor het splitsen van één enkele laag naar meerdere uitvoerlagen.

Implements a native DXF export algorithm using `QgsDxfExport` functionality, which is also used by `Project -> Import/Export -> Export Project to DXF`.

![image43](images/entries/7800af6d2597ad04650532f201c8d4ee005c8e53.gif)

This feature was developed by [Alexander Bruy](https://api.github.com/users/alexbruy)
### Mogelijkheid: Aanvullende typen geometrie voor exporteren naar PostGIS
Some available geometry types from the GDAL ogr2ogr operation used for exporting data to PostGIS databases have been added to the tool interface. This functionality also includes the option to specify vector dimensions for exported data and resolves issue [39003](https://github.com/qgis/QGIS/issues/39003).

![image44](images/entries/48415fefe669fa93d5c7e13959c4a35e6dab60e2.gif)

This feature was developed by [mazano](https://api.github.com/users/NyakudyaA)
### Mogelijkheid: Verbeterde netwerkverzoeken met GDAL
A QgsCPLHTTPFetchOverrider utility class was added and used in the OGR provider which redirects GDAL\'s CPL HTTP calls through QgsBlockingNetworkRequest. This ensures that GDAL can use the QGIS network provider rather than redirecting requests through cURL. Additional head(), put() and deleteResource() methods were added to QgsBlockingNetworkRequest.

This feature was developed by [Even Rouault](https://api.github.com/users/rouault)
### Mogelijkheid: Alleen-lezen gemaakte velden
Een API-methode is toegevoegd om er voor te zorgen dat gemaakte kolommen, die Alleen-lezen zijn, niet worden weergegeven in berwerkers.

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Mogelijkheid: Verbeterd laden van MSSQL met vooraf gedefinieerde parameters
Om laadtijd te verminderen kan het bereik van de kaart vooraf worden berekend, en Primaire sleutels kunnen worden opgegeven, wat de noodzaak verwijdert voor QGIS om deze karakteristieken te berekenen en uitvoering te verbeteren.

This is done by extending dbo.geometry_columns tables and adding the following extra columns, which may be populated accordingly by database administrators:
- Extent : qgis_xmin, qgis_xmax, qgis_ymin, qgis_ymax
- Primary key : qgis_pkey

In de widget voor het configureren van de database staan nu twee extra keuzevakken die gebruikmaken van deze parameters:
- Laagbereik uit tabel geometry_columns gebruiken
- Primaire sleutel uit tabel geometry_columns gebruiken

![image45](images/entries/3d77459436d542190afa88f6d927be7f8245dbf0.gif)

This feature was funded by [ms.GIS](http://msgis.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Schema's voor MS SQL filteren
Gebruikers kunnen nu de beschikbare schema's voor verbindingen van MS SQL filteren De widget voor de verbinding van de database bevat nu opties voor het filteren van beschikbare schema's, zodat alleen de verwachte schema's beschikbaar zijn in d browser van QGIS.

![image46](images/entries/1e2fe1a94747c9aa2fbbaab3053bfc6631cfbb22.gif)

This feature was funded by [ms.GIS](http://msgis.com/)

This feature was developed by [Lutra Consulting (Vincent Cloarec)](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Ondersteuning voor database SAP HANA
QGIS ondersteunt nu databases van SAP HANA. SAP HANA is een in-geheugen database met een OGC-compliant ruimtelijk programma met een gratis expres-uitgave die beschikbaar is op www.sap.com

This feature was developed by [Maxim Rylov](https://api.github.com/users/mrylov)
### Mogelijkheid: Vervallen ondersteuning voor DB2
**De gegevensprovider DB2 is gemarkeerd als vervallen**, en is standaard verborgen in de gebruikersinterface van QGIS.

QGIS has adopted a gentle approach to removing unmaintained core providers, and users of deprecated providers may enable support for them by setting the hidden \"providers/showDeprecated\" settings key to *true*.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Mogelijkheid: API Oracle-verbinding
De QGIS API bevat nu *QgsAbstractDatabaseProviderConnection* voor de provider Oracle.

Dit werd mogelijk gemaakt door Metropole de Lille

This feature was developed by [Julien Cabieces](https://api.github.com/users/troopa81)
### Mogelijkheid: Geavanceerde opties voor importeren van rastergegevens toegevoegd
Nieuwe functionaliteit is geïntroduceerd die het mogelijk maakt geavanceerde parameters te specificeren bij het importeren van lagen met de gegevensprovider GDAL, openen van een uitgebreid bereik van nieuwe mogelijkheden, speciaal bij het werken rondom verwachte problemen met gegevenssets en tekortkomingen.

![image47](images/entries/5d7ccf71a162d927706fd6e6517a67452ec653e1.webp)

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin
## QGIS Server
### Mogelijkheid: Schaal symbool GetLegendGraphics
Het QGIS Server-verzoek WMS GetLegendGraphics ondersteunt nu het opnemen van het benoemen van min/max schaal voor JSON symboolexport

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Mogelijkheid: Slepen en neerzetten van WMS antwoord GetFeatureInfo
Met het bewerkersfomulier slepen en neerzetten is het mogelijk de attributen opnieuw te sorteren en groepen of subgroepen toe te voegen in het berwerkersformulier. Deze functionaliteit is uitgebreid zodat het antwoord van WMS GetFeatureInfo kan worden aangepast om groepen en subgroepen te bevatten, als ook toe te staan dat de inhoud van het antwoord kan worden aangepast en opnieuw geschikt met het bewerkersformulier, met ondersteuning voor functionaliteit voor slepen en neerzetten.

This feature was developed by [mhugent](https://api.github.com/users/mhugent)
## Programmeerbaarheid
### Mogelijkheid: Meerdere items uitvoeren vanuit het dialoogvenster voor geschiedenis van de opdrachtregel
De QGIS Python Console ondersteunt nu het uitvoeren van meerdere geselecteerde opdrachten uit het dialoogvenster Geschiedenis door het toevoegen van een nieuwe knop **Plakken**.

![image48](images/entries/1de42c7dc35c2b73dce1605a3c36b97166d81850.webp)

This feature was developed by [Salvatore Larosa](https://api.github.com/users/slarosa)
### Mogelijkheid: Plug-ins in- of uitschakelen vanaf de opdrachtregel
The qgis_process command line tool has had new commands added which allow users to enable or disable plugins using the commands as outlined below:
- `qgis_process plugins enable plugin_name`: enables the named plugin
- `qgis_process plugins disable plugin_name`: disables the named plugin

This improves the automation capabilities of QGIS and allows the use of plugins on headless environments with the qgis_process tool.

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Belangrijke reparaties
### Mogelijkheid: Reparaties van problemen door Alessandro Pasotti
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Crash with VRT layers using Python pixel functions | [#41048](https://github.com/qgis/QGIS/issues/41048) | Werkt bij mij wel |  |
| Cannot enter attributes and save edits on PostGIS table when user has only the INSERT privilige | [#40922](https://github.com/qgis/QGIS/issues/40922) | [PR #41059](https://github.com/qgis/QGIS/pull/41059) | nee |
| GeoPackage layer name truncated when filename contains more that one dot | [#40864](https://github.com/qgis/QGIS/issues/40864) | [PR #41061](https://github.com/qgis/QGIS/pull/41061) | nee |
| Unable to right click GeoPackage table from browser | [#40856](https://github.com/qgis/QGIS/issues/40856) | Werkt bij mij wel |  |
| Empty Temporary scratch layer made permanent is not editable | [#38834](https://github.com/qgis/QGIS/issues/38834) | [PR #41075](https://github.com/qgis/QGIS/pull/41075) | nee |
| Update MXE build, several issues | meerdere problemen | [Commit afff8ba7be2794fe521a462feaf83b1a5d7cce63](https://github.com/qgis/QGIS/commit/afff8ba7be2794fe521a462feaf83b1a5d7cce63) [PR #40923](https://github.com/qgis/QGIS/pull/40923) | ja (CI) |
| can\'t change value in vertex editor if \"locale\" settings use commas as decimal separator | [#29682](https://github.com/qgis/QGIS/issues/29682) | [PR #41082](https://github.com/qgis/QGIS/pull/41082) | [PR #41607](https://github.com/qgis/QGIS/pull/41607) |
| Empty String \'\' is shown as NULL with a spatialite layer using OGR provider | [#41076](https://github.com/qgis/QGIS/issues/41076) | [PR #41109](https://github.com/qgis/QGIS/pull/41109) | [PR #41123](https://github.com/qgis/QGIS/pull/41123) |
| Wrong WFS 2.0.0 request returns duplicate features | [#41087](https://github.com/qgis/QGIS/issues/41087) | [PR #41169](https://github.com/qgis/QGIS/pull/41169) | nee |
| Server WMS GetFeatureInfo feature ID inconsitencies | [#41124](https://github.com/qgis/QGIS/issues/41124) | [PR #41137](https://github.com/qgis/QGIS/pull/41137) | [PR #41148](https://github.com/qgis/QGIS/pull/41148) |
| WMS throws LayerNotDefined when layer name contains plus sign (+) | [#41116](https://github.com/qgis/QGIS/issues/41116) | [PR #41211](https://github.com/qgis/QGIS/pull/41211) | [PR #41331](https://github.com/qgis/QGIS/pull/41331) |
| QGIS Server WFS 1.1: issue with axis order | [#36584](https://github.com/qgis/QGIS/issues/36584) | [PR #41242](https://github.com/qgis/QGIS/pull/41242) | [PR #41608](https://github.com/qgis/QGIS/pull/41608) |
| raster export (save as\...) not working if QGIS locale uses commas as decimal separator | [#41284](https://github.com/qgis/QGIS/issues/41284) | [PR #41316](https://github.com/qgis/QGIS/pull/41316) | [PR #41330](https://github.com/qgis/QGIS/pull/41330) |
| QGISserver WFS returns invalid GML in case of cascading WFS | [#41292](https://github.com/qgis/QGIS/issues/41292) | [PR #41335](https://github.com/qgis/QGIS/pull/41335) | [PR #41387](https://github.com/qgis/QGIS/pull/41387) |
| Better handling of duplicated FIDs in GPKGs | [#41156](https://github.com/qgis/QGIS/issues/41156) | Werkt bij mij wel |  |
| Cannot Create New Tables in a Geopackage (browser) | [#41342](https://github.com/qgis/QGIS/issues/41342) | [PR #41355](https://github.com/qgis/QGIS/pull/41355) | [PR #41403](https://github.com/qgis/QGIS/pull/41403) |
| QGIS crashes when cancelling add child form | [#41295](https://github.com/qgis/QGIS/issues/41295) | [PR #41375](https://github.com/qgis/QGIS/pull/41375) | N/B |
| Group has no name when importing sublayers from browser panel | [#41343](https://github.com/qgis/QGIS/issues/41343) | [PR #41379](https://github.com/qgis/QGIS/pull/41379) | [PR #41402](https://github.com/qgis/QGIS/pull/41402) |
| Identifty tool does not work anymore on arcgis map services layers | [#41311](https://github.com/qgis/QGIS/issues/41311) | [PR #41427](https://github.com/qgis/QGIS/pull/41427) | [PR #41430](https://github.com/qgis/QGIS/pull/41430) |
| Signal committedAttributeValuesChanges not emitted when project in auto transaction mode | [#41477](https://github.com/qgis/QGIS/issues/41477) | [PR #41539](https://github.com/qgis/QGIS/pull/41539) | riskant |
| The project file does not store variables with formatted text | [#41541](https://github.com/qgis/QGIS/issues/41541) | Bovenliggend probleem in QT |  |
| New spatial table in a geopackage with index always throw a warning | [#41436](https://github.com/qgis/QGIS/issues/41436) | [PR #41556](https://github.com/qgis/QGIS/pull/41556) | [PR #41609](https://github.com/qgis/QGIS/pull/41609) |
| Empty \"Exclude layers\" selection list in Server settings dialog when using projects saved in GPKG files or PGSQL databases | [#40552](https://github.com/qgis/QGIS/issues/40552) | [PR #41605](https://github.com/qgis/QGIS/pull/41605) |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.qcooperative.net/)
### Mogelijkheid: Reparaties van problemen door Peter Petrik
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Skipping unknown layer type circle in vector tiles | [#41529](https://github.com/qgis/QGIS/issues/41529) | [PR #41584](https://github.com/qgis/QGIS/pull/41584) | nog te doen |
| Passwords cannot be saved into keychain on macOS with QGIS 3.16 | [#40541](https://github.com/qgis/QGIS/issues/40541) | [QGIS-Mac-Packager PR #112](https://github.com/qgis/QGIS-Mac-Packager/pull/112) | automatisch |
| Symbol not found: \_curl_mime_addpart with GDAL merge | [QGIS-Mac-Packager Issue #111](https://github.com/qgis/QGIS-Mac-Packager/issues/111) | [QGIS-Mac-Packager PR #112](https://github.com/qgis/QGIS-Mac-Packager/pull/112) | automatisch |
| initGUI() results in Segmentation fault on macOS in standalone PyQgis | [#40378](https://github.com/qgis/QGIS/issues/40378) | beantwoord met de reparatie van het script |  |
| QgsCompoundColorWidget instance crash when QgsApplication::colorSchemeRegistry() is empty \\ | [#28208](https://github.com/qgis/QGIS/issues/28208) | ongeldig |  |
| Include missing fonts in build | [QGIS-Mac-Packager Issue #105](https://github.com/qgis/QGIS-Mac-Packager/issues/105) | [PR #41412](https://github.com/qgis/QGIS/pull/41412) | niet nodig? |
| Mishandling Grib Data Values | [#37504](https://github.com/qgis/QGIS/issues/37504) | kan het niet reproduceren in QGIS 3.16 macOS |  |
| Error opening .2dm and .xmdf mesh data | [#40385](https://github.com/qgis/QGIS/issues/40385) | [PR libspatialindex #221](https://github.com/libspatialindex/libspatialindex/pull/221) | automatisch |
| r.watershed error on macOS | [#40996](https://github.com/qgis/QGIS/issues/40996) | [QGIS-Mac-Packager Commit 7238782](https://github.com/qgis/QGIS-Mac-Packager/commit/7238782f4b3408f1d69b2adbafe52d9698c4f20c) | [QGIS-Mac-Packager Commit 7238782](https://github.com/qgis/QGIS-Mac-Packager/commit/7238782f4b3408f1d69b2adbafe52d9698c4f20c) |
| OpenCL Acceleration not found on macOS | [#41182](https://github.com/qgis/QGIS/issues/41182) | [PR #41374](https://github.com/qgis/QGIS/pull/41374) | [Github commit](https://github.com/nyalldawson/QGIS/commit/997d3c1ab8386a5035b70a65e9843ec64feaa377) |
| Proj.db not found for SAGA tools on QGIS 3.17 Mac nightly | [#41606](https://github.com/qgis/QGIS/issues/41606) | [QGIS-Mac-Packager Commit 7a71390](https://github.com/qgis/QGIS-Mac-Packager/commit/7a713903cf001a9e156eac60e25e84789e1e534a) | automatisch |
| \[mesh\]\[ui\] Changing settings for 2D Contour color ramp shader shows confusing widgets | \"[#39571](https://github.com/qgis/QGIS/issues/39571) | [PR #41442](https://github.com/qgis/QGIS/pull/41442) | niet nodig? |
| QGIS crashes when \"open directory\" is selected from the recent projects contextual menu | [PR #41591](https://github.com/qgis/QGIS/pull/41591) | [PR #41591](https://github.com/qgis/QGIS/pull/41591) | nog te doen |
| Data-defined setting in html frame does not work | [#41590](https://github.com/qgis/QGIS/issues/41590) | onderzoek gedaan |  |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Peter Petrik](https://www.lutraconsulting.co.uk/)
### Mogelijkheid: Reparaties van problemen door Even Rouault
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| PostgreSQL provider doesn\'t support special characters for authentication on Windows | [#41132](https://github.com/qgis/QGIS/issues/41132) | [PR #41144](https://github.com/qgis/QGIS/pull/41144) | [PR #41179](https://github.com/qgis/QGIS/pull/41179) |
| WMS/WFS connections XML import fails silently if there are two connections with the same name | [#39758](https://github.com/qgis/QGIS/issues/39758) | [PR #41145](https://github.com/qgis/QGIS/pull/41145) | [PR #41195](https://github.com/qgis/QGIS/pull/41195) |
| QgsAttributeWidgetRelationEditWidget::setRelationEditorConfiguration(): avoid crash on corrupted relation | [#40495](https://github.com/qgis/QGIS/issues/40495) | [PR #41147](https://github.com/qgis/QGIS/pull/41147) | [PR #41175](https://github.com/qgis/QGIS/pull/41175) |
| \[Processing\] Rescale Raster gives bad results | [#41084](https://github.com/qgis/QGIS/issues/41084) | [PR #41155](https://github.com/qgis/QGIS/pull/41155) | [PR #41194](https://github.com/qgis/QGIS/pull/41194) |
| QGIS not using PostGIS spatial index on geography column | [#39453](https://github.com/qgis/QGIS/issues/39453) | [PR #41296](https://github.com/qgis/QGIS/pull/41296) | [PR #41301](https://github.com/qgis/QGIS/pull/41301) |
| Geopackage with DateTime field (temporal selection) behave different for painting and attributetable | [#41074](https://github.com/qgis/QGIS/issues/41074) | Analyse van het probleem |  |
| Crash with VRT layers using Python pixel functions | [#41048](https://github.com/qgis/QGIS/issues/41048) | [GDAL PR 3424](https://github.com/OSGeo/gdal/pull/3424) | [GDAL Commit a2ed089](https://github.com/OSGeo/gdal/commit/a2ed0894b83e023e21a6dfa19fa399d0784b339a) |
| Empty layer names adding Raster layer from GDAL / OGCAPI driver | [#41428](https://github.com/qgis/QGIS/issues/41428) | [PR #41452](https://github.com/qgis/QGIS/pull/41452) | niet van toepassing |
| Imported GeoTIFF not using data extent to select CRS - NAD83 vs NAD83(CSRS) | [#41456](https://github.com/qgis/QGIS/issues/41456) | ongeldig |  |
| Georeferencer: fix crash on .points files generated by older QGIS versions | niet gerapporteerd | [PR #41480](https://github.com/qgis/QGIS/pull/41480) | N/B |
| Crash trying to load ArcGis community map vector tiles | [#41401](https://github.com/qgis/QGIS/issues/41401) | [PR #41481](https://github.com/qgis/QGIS/pull/41481) | [PR #41516](https://github.com/qgis/QGIS/pull/41516) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Even Rouault](http://www.spatialys.com/)
### Mogelijkheid: Reparaties van problemen door Julien Cabieces
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Record count regression on views | [#41188](https://github.com/qgis/QGIS/issues/41188) | Zal niet gerepareerd worden |  |
| Integer overflow errors creating and saving virtual layers | [#40503](https://github.com/qgis/QGIS/issues/40503) | [PR #41332](https://github.com/qgis/QGIS/pull/41332) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Vertex Tool uses old cached data resulting in corrupted data in db | [#40720](https://github.com/qgis/QGIS/issues/40720) | [PR #41357](https://github.com/qgis/QGIS/pull/41357) | [PR #41509](https://github.com/qgis/QGIS/pull/41509) |
| WMS layer metadata - count for available CRS is not correct | [#40318](https://github.com/qgis/QGIS/issues/40318) | [PR #41363](https://github.com/qgis/QGIS/pull/41363) |  |
| Layer variables missing from Field Calculator algorithm on QGIS 3.16.1 | [#40255](https://github.com/qgis/QGIS/issues/40255) | [PR #41417](https://github.com/qgis/QGIS/pull/41417) | [PR #41510](https://github.com/qgis/QGIS/pull/41510)/ |
| Filter is not applied in duplicated layers | [#40349](https://github.com/qgis/QGIS/issues/40349) | Terugkoppeling |  |
| Unable to save results to PostgreSQL database when iterating features in processing algorithms | [#39620](https://github.com/qgis/QGIS/issues/39620) | [PR #41446](https://github.com/qgis/QGIS/pull/41446) |  |
| Closed Python call to \--processing.run(\'qgis:fieldcalculator\'\-- fails to catch divide by zero | [#37737](https://github.com/qgis/QGIS/issues/37737) | Al gerepareerd |  |
| Expression widget does not list fields when Selected features only is checked | [#40055](https://github.com/qgis/QGIS/issues/40055) | [PR #41457](https://github.com/qgis/QGIS/pull/41457) | [PR #41511](https://github.com/qgis/QGIS/pull/41511) |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://oslandia.com/en/)
### Mogelijkheid: Reparaties van problemen door Nyall Dawson
| Titel probleem | URL issues.qgis.org (indien gerapporteerd) | URL Commit (Github) | 3.16 backport commit (GitHub) |
| --- | --- | --- | --- |
| Fix text edit widget wrapper incorrectly shows \"NULL\" string for indeterminate state | niet gerapporteerd | [Commit fa91357](https://github.com/qgis/QGIS/commit/fa9135792574ff5dbbd1ab53d15faec3d190e3db) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| \[layouts\] Expose the correct expression context for attribute and manual table text format widgets | niet gerapporteerd | [Commit f337271](https://github.com/qgis/QGIS/commit/f3372716060f2c1eecff46c99c999b66505504fc) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix incorrect error when saving attribute modifications to layers with joins | niet gerapporteerd | [Commit 01889d9](https://github.com/qgis/QGIS/commit/01889d96b22757028e62c156a945ae8b86e69a68) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix misleading JSON error message when an attribute form fails to save changes | niet gerapporteerd | [Commit fd657be](https://github.com/qgis/QGIS/commit/fd657bee96c2b58c035a69a71fd58d1cb409770e) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix project \"avoid tile artifacts\" setting has no effect on server | [#37679](https://github.com/qgis/QGIS/issues/37679) | [Commit 04d6ea9](https://github.com/qgis/QGIS/commit/04d6ea99b43fb8e426dc1cb31b2b7e913aca203c) | Niet van toepassing |
| Don\'t crash when a relation is created where the field names defined in the relation differ in case from the layer\'s field names | niet gerapporteerd | [Commit 0f49cb9](https://github.com/qgis/QGIS/commit/0f49cb909732882e4c0b3ba26a6987fff95e29ea) | [Commit c708ca58](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Fix add/remove buttons have no icons in create relationship dialogs | niet gerapporteerd | [Commit 2e81dbc](https://github.com/qgis/QGIS/commit/2e81dbcc50e510afc9033be9a99bfcb2512f6fd9) | N/B |
| Fix restoring previous GDAL alg raster creation options when running an algorithm from processing history | niet gerapporteerd | [Commit 645397e](https://github.com/qgis/QGIS/commit/645397e83d88c124e8ca8faa46b304c2e74ec3e9) | [Commit c708ca5](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Fix setting the current GDAL profile options temporarily overwrites the definition of one of the stored GDAL profiles | [#41378](https://github.com/qgis/QGIS/issues/41378) | [Commit 7ff0187](https://github.com/qgis/QGIS/commit/7ff01871d0c72b92070aed3b66f95f7f268ce6e0) | [Commit c708ca58e](https://github.com/qgis/QGIS/commit/c708ca58e81734abed0193d596a451609edd295a) |
| Fix crash when running model from file through qgis_process with the \--json switch | niet gerapporteerd | [Commit ccd4fb6](https://github.com/qgis/QGIS/commit/ccd4fb67eb309a077e959df60c0d3556321453da) | [Commit 8bda37c](https://github.com/qgis/QGIS/commit/8bda37ca0f2b914fa5fe9916398a2d08c1ef774d) |
| When labelling job takes a long time to render, don\'t clear the map canvas between the finished layer render state and final state | niet gerapporteerd | [Commit 1beb1bd](https://github.com/qgis/QGIS/commit/1beb1bdc788ba64f826c54d3ab587fcc5289afb4) | N/B |
| Don\'t loop through all selected features multiple times (once per field) when the attribute form is opened | [#41366](https://github.com/qgis/QGIS/issues/41366) | [Commit c661359](https://github.com/qgis/QGIS/commit/c6613593c72ac0411417d5a9aacf0335d52c4e66) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix incorrect feature request filter expression generated when rule based renderer uses a NOT IN rule | niet gerapporteerd | [Commit a895598](https://github.com/qgis/QGIS/commit/a89559879743242d2b7138c2d3d73179c380af97) | [Commit 5eec9e4](https://github.com/qgis/QGIS/commit/5eec9e42f3e4ddeb17f63a194df7a1f9ccb2e5e5) |
| Ask users for existing destination fields for Sum Line Length and Count Points In Polygons result fields when running in in-place mode | [#39807](https://github.com/qgis/QGIS/issues/39807) | [Commit 12e8130](https://github.com/qgis/QGIS/commit/12e8130beb0836fe18bf741f5ad26bf599feb84f) | Niet van toepassing |
| Fix crash when no layers exist in project | niet gerapporteerd | [Commit 039bc20](https://github.com/qgis/QGIS/commit/039bc202733d57e5daaa13d417eb78b2c072851d) | N/B |
| \[processing\] Fix exception in algorithm locator filter if an algorithm has no group set | niet gerapporteerd | [Commit 46dbd8b](https://github.com/qgis/QGIS/commit/46dbd8b2d6275256779c14938de7424ab1053d7a) | [Commit 7ef7b17](https://github.com/qgis/QGIS/commit/7ef7b17f2601bd8ee8f31dc5be7a69b90c89550f) |
| Expose additional GDAL supported resampling methods as options for \"early\" raster resampling | [#40746](https://github.com/qgis/QGIS/issues/40746) | [Commit 13fbcd1c](https://github.com/qgis/QGIS/commit/13fbcd1cff3dfa31a7c592566de9d2f5be1cf965) | Niet van toepassing |
| \[processing\] Add commands to qgis_process tool to enable or disable plugins from the command line | [#41218](https://github.com/qgis/QGIS/issues/41218) | [Commit d140970](https://github.com/qgis/QGIS/commit/d1409703fbc1eff1c80cc0895e53e2764f332e92) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix transparency for ImageServer layers added via browser | [#41126](https://github.com/qgis/QGIS/issues/41126) | [Commit 9fb554f](https://github.com/qgis/QGIS/commit/9fb554fde0348c3a78aad6070c6c83986e5470ab) | Niet van toepassing |
| \[server\] Just skip any broken projects on the landing page, instead of blocking the whole landing pag | niet gerapporteerd | [Commit e4a4b83](https://github.com/qgis/QGIS/commit/e4a4b832dff47e552271c8b024eb8105b88483cb) | Niet van toepassing |
| Automatically update map canvas and layouts if set to a user crs and the user changes that crs definition | niet gerapporteerd | [Commit ea57cfe](https://github.com/qgis/QGIS/commit/ea57cfea1ff4320b2bd6b7e6be5aea699bdeabe3) | Niet van toepassing |
| Don\'t show duplicate \"source\"/\"path\" rows for local files | niet gerapporteerd | [Commit 8aa9c6a](https://github.com/qgis/QGIS/commit/8aa9c6a142523aed85ce74d70b93c04553e13dc0) | N/B |
| Fix retrieval of sql results from geopackages | [#40856](https://github.com/qgis/QGIS/issues/40856) | [Commit f65fe3d](https://github.com/qgis/QGIS/commit/f65fe3dbc95a7f38b24271e9fb979eed68823cff) |  |
| Don\'t default to input field for optional expression parameters | [#41063](https://github.com/qgis/QGIS/issues/41063) | [Commit 1fed902](https://github.com/qgis/QGIS/commit/1fed9020a21a3f3deb9cece03ebb533aeae8c6a2) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| \[layouts\] Always update label after text changes | [#40203](https://github.com/qgis/QGIS/issues/40203) | [Commit 5d14c61](https://github.com/qgis/QGIS/commit/5d14c61f224e0f3621f701f96aa499ab355e1888) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix fill symbol only related properties (like ring filters) show for line symbols in some contexts. | [#33398](https://github.com/qgis/QGIS/issues/33398) | [Commit 9cba248](https://github.com/qgis/QGIS/commit/9cba2489bcde55ee6e072dc7690ff2401928c507) | Niet van toepassing |
| Ensure layer style dock is updated when toggling legend items through layer tree menu | [#40630](https://github.com/qgis/QGIS/issues/40630) | [Commit 457d661](https://github.com/qgis/QGIS/commit/457d6618ad6e9843b785854cf85ab5a0b815cd8c) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix rendering of Vector Field marker symbol layer when map is rotated | [#40916](https://github.com/qgis/QGIS/issues/40916) | [Commit 157bdca](https://github.com/qgis/QGIS/commit/157bdcab884dde6523e78897ec1a8618a26b6d06) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix marker line symbol layer renders vertices for segmentized versions of curved geometries instead of the actual vertices | [#39750](https://github.com/qgis/QGIS/issues/39750) | [Commit 71090b0](https://github.com/qgis/QGIS/commit/71090b077f6968eef2c428d2de74c63c78f3f3a1) | [PR #41054](https://github.com/qgis/QGIS/pull/41054) |
| Fix scalebar decoration uses incorrect map extent when restoring a project | [#40748](https://github.com/qgis/QGIS/issues/40748) | [Commit f1ea5a9](https://github.com/qgis/QGIS/commit/f1ea5a9c560eaba6f3947cc8447d6f25226c2b5d) | [Commit 6b1e67d](https://github.com/qgis/QGIS/commit/6b1e67dd947e41359a7ad3d1a8f44ef1ec20b442) |
| Fix missing identify results right click menu items for non vector layer types | niet gerapporteerd | [Commit 176e972](https://github.com/qgis/QGIS/commit/176e9728c5ebb24f309369878664c2c49dc6eb16) | Niet van toepassing |

Deze mogelijkheid werd mogelijk gemaakt door [QGIS.ORG (door donoren en dragende leden)](https://www.qgis.org/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
