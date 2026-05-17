---
HasBanner: false
archived: true
date: 2013-03-01
draft: false
featured: false
section: project
sidebar: true
thumbnail: images/india_assam1.png
title: QGIS voor monitoren van tijgers (met behulp van cameravallen in Nameri Tiger
  Reserve, Assam, India Sonitpur District)
type: case-study

---
{{<content-start >}}
# QGIS voor monitoren van tijgers (met behulp van cameravallen in Nameri Tiger Reserve, Assam, India Sonitpur District)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>1 maart 2013</span>
</p>

Nameri Tiger Reserve (NTR) is één van de 3 tijgerreservaten van Assam en is gelegen in het noordelijke deel van het Sonitpur District van Assam langs de uitlopers van de oostelijke Himalaya. Verspreid over een gebied van 344 km² biedt NTR een rijke diversiteit aan flora en fauna. Het belangrijkste gebied van het reservaat, dat de naam "Nameri National Park" draagt, wordt begrensd door de rivier Jia-Bhoreli in het westen en de rivier Bor-Dikorai in het oosten. Ten noorden van Nameri ligt het Pakke Tiger Reserve van Arunachal Pradesh.

![](../images/india_assam1.png)

in dit landschap zijn de belangrijkste soorten om te behouden de koninklijke Bengaalse tijger, Aziatische olifant, Indiase bison, gewone luipaard, gevlekte luipaard, wilde hond, Samba-hert, muntjak, zwijnshert, wild zwijn en verschillende andere soorten. De diversiteit aan vogels in NTR is ook behoorlijk indrukwekkend en meer dan 370 soorten vogels zijn op dit moment geïdentificeerd. Het reservaat wordt beheerd door het Assam Forest Department, Government of Assam.
## Toepassing van QGIS voor ontwerpen studie met cameravallen
Vanaf 2011 heeft de National Tiger Conservation Authority (NTCA) van India het verplicht gemaakt voor alle tijgerreservaten in het land om tijgers te monitoren met behulp van cameravallen. Onder dit nieuwe protocol, zullen 25 paren camera's worden geïnstalleerd voor 100 km² van de tijgerreservaten en de periode van verzamelen is 40-60 dagen. Dit nieuwe protocol voor het monitoren van tijgers is in grote mate afhankelijk van het GIS.

<figure>
<img src="../images/india_assam2.png" class="align-right" alt="india_assam2.png" />
<figcaption>Afbeelding van een mannelijke tijger die door een van de cameravallen werd vastgelegd</figcaption>
</figure>

Gedurende 2012-13 implementeerden we dit nieuwe protocol voor het monitoren van tijgers in NTR met behulp van QGIS. We digitaliseerden. om te beginnen, de begrenzing van NTR in QGIS en sloegen die op als polygoon. Dit polygoon voor de begrenzing werd geëxporteerd naar GPS voor navigatie-doeleinden gedurende de opnamen in het veld. We voerden een uitgebreide zoekactie naar tekenen van bewijs van de aanwezigheid van tijgers in NTR zoals voetafdrukken, krassporen en uitwerpselen. GPS-coördinaten van de teken van aanwezigheid van tijgers, alsmede geschikte locaties voor de cameravallen werden opgenomen. Na het voltooien van dit onderzoek werden de gegevens getransfereerd naar QGIS met behulp van GPS-programma's, voor verdere verwerking en het vaststellen van de locaties voor de cameravallen. Een shapefile dat de tekenen van aanwezigheid van de tijgers en de mogelijke locaties voor de cameravallen bevatte, werd voorbereid.

<figure>
<img src="../images/india_assam3.png" alt="india_assam3.png" />
<figcaption>Bloksgewijze verdeling van locaties van cameravallen en toewijzen van verschillende cameravallen aan verschillende boskampen met behulp van Voronoi-polygonen & hub distance.</figcaption>
</figure>

Vervolgens bereidden we een 4 km^2^ rasterlaag voor met behulp van de plug-in mmqgis. De shapefile die de resultaten bevatte van het onderzoek naar de tekenen van aanwezigheid werd over het raster van 4 km^2^ gelegd om de verdeling van de cameravallen in NTR te visualiseren. De optie Afstandsmatrix onder Vector. Analyse-gereedschappen waren erg handig voor het bepalen van de afstanden tussen de camera's. Cameralocaties die minder dan 1,8 km afstand hadden tot een andere werden verwijderd om te voldoen aan de bepalingen van het protocol voor het monitoren. Wegens een tekort aan camera's om het gehele reservaat in één keer te kunnen verwerken, besloten we het reservaat op te delen in 2 blokken van gebieden van elk 100 km^2^. Grenzen van deze twee blokken werden gedigitaliseerd en opgeslagen als afzonderlijke shapefiles voor beide blokken. Met behulp van de plug-in RGB compositie werd een negatieve kleurcompositie van het reservaat gemaakt en het shapefile van de tekenen van aanwezigheid werd daaroverheen gelegd om de type leefgebieden te bepalen die door de tijgers werden gebruikt. Gedurende de periode van de studie werden de cameravallen intensief gemonitord door de staf in het veld. We gebruikten de mogelijkheid Voronoi-polygonen van de plug-in Geometrie-gereedschap en hub distance van de plug-in mmqgis voor het plannen van logistieke vereisten om het gladjes functioneren van het proces van monitoren te waarborgen. De geografische coördinaten van cameravallen zijn vereist voor het bepalen van de dichtheid aan tijgers en het modelleren van de bewoning door andere soorten. Deze details van de coördinaten werden eenvoudig gegenereerd uit de shapefiles van de cameravallen met behulp van de mogelijkheid "Geometriekolommen toevoegen/exporteren" van Vector > Geometrie-gereedschappen.

<figure>
<img src="../images/india_assam4.png" class="align-right" alt="india_assam4.png" />
<figcaption>Onderzoeksraster met aanwezigheid tijgers</figcaption>
</figure>

## Conclusie
Voor het eerst in de geschiedenis van dit kleine tijgerreservaat in noordoost-India was het mogelijk tijgers te monitoren met behulp van cameravallen, voornamelijk dankzij QGIS. Resultaten van deze oefening in monitoren geven aan dat er ongeveer 8-15 tijgers in deze omgeving aanwezig zijn. In aanvulling op de tijgers werden ook verschillende uitzonderlijke soorten fotografisch gedocumenteerd. Los van het monitoren van de tijgers gebruikten we QGIS ook voor activiteiten zoals het plannen van het werk voor het beheer van de woonomgeving, herzien van schema's voor patrouilles en het ontwerpen van kaarten voor bezoekers. De gebruiksvriendelijke interface, vele mogelijkheden, diepgang in de documentatie, online ondersteuning en de vrije/open source-filosofie zijn enkele van de kwaliteiten van QGIS die ons ertoe bewogen het te kiezen boven andere merkgebonden software. We geloven dat QGIS een groot potentieel heeft voor bijdragen aan individuen/instituten/betrokken bij de bescherming van wilde dieren in de ontwikkelingswereld door GIS-technologie ter beschikking te stellen tegen weinig of geen kosten.
## Auteur
<figure>
<img src="../images/india_assamaut.png" class="align-left" height="200" alt="india_assamaut.png" />
<figcaption>Rajendra Garawad</figcaption>
</figure>

Dit artikel werd bijgedragen door Rajendra G. Garawad in maart 2013. Hij is de Field Director of Nameri Tiger Reserve, Assam, India. Hij bezit Master Degrees in Forestry Science and Conservation & Land Management.

{{<content-end >}}
