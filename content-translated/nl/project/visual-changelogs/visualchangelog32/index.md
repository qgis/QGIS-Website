---
HasBanner: false
draft: false
releaseDate: 22-06-2018
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Datum uitgave 22-06-2018

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Dankwoord**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 3.2
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## Algemeen
### Mogelijkheid: Nieuwe gezipte projectbestandsindeling .qgz is nu de standaard indeling
QGZ werd als optionele indeling toegevoegd in 3.0. Door van deze indeling de standaard te maken maakt het eenvoudiger om te komen tot een container die in staat is om bronnen zoals SVG, offline gegevens in GPKG, kleurverlopen, plug-ins of scripts in te bedden.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Mogelijkheid: Filteren op veldwaarden in widget Querybouwer
Bij het maken van een nieuw filter met een expressie in Querybouwer kunt u nu de waarden van de velden filteren in een voorbeeldpaneel.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Mogelijkheid: Kaart op VOLLEDIG scherm met Ctrl-Shift-Tab
Naast Ctrl-Tab kunt u nu Ctrl-Shift-Tab gebruiken, wat u de kaart zal laten zien en ALLEEN de kaart, geen werkbalken of knoppen meer (of zelfs zonder titel voor het venster in combinatie met F11). Geweldig voor projecteren op Volledig scherm via beamer of op grote schermen. U kunt nog steeds zoomen en verschuiven! (Gebaseerd op het werk van Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Richard Duivenvoorde
## Kaartgereedschap
### Mogelijkheid: Gereedschap Kaart vereenvoudigen kan nu ook objecten gladder maken
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Gereedschap Objecten identificeren met extra opties
Met de nieuwe verbeteringen kan de gebruiker nu soortgelijke gereedschappen gebruiken als met Selecteren om meerdere objecten te identificeren.

Dit werd mogelijk gemaakt door Leicestershire County Council en East Hampshire District Council

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Sla ook de status Uitgevouwen/Ingeklapt op van knopen op de kaartthema's
Elk kaartthema zal ook vastleggen welke lagengroepen en items van de legenda uitgevouwen zijn, wanneer dus een kaartthema wordt geselecteerd, wordt de status Uitgevouwen/Ingeklapt toegepast op de boom van de lagen.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
Een nieuwe kaartweergave kan worden geconfigureerd om automatisch in te zoomen op de huidige selectie. Kan worden gecombineerd met verschillende kaartthema's, zoals in dit voorbeeld.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Mogelijkheid: Keuze voor methode van vereenvoudigen voor gereedschap Kaart vereenvoudigen
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Zoomen naar gerelateerde objecten toegevoegd in formulieren
Er verschijnt een nieuwe knop in het subformulier van objectattributen wanneer één of meer records zijn geselecteerd in een gerelateerde tabel. De knop zoomt op de kaart nar deze objecten als zij geometrieën hebben.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Cartesiaanse gebieden/lengtes/perimeters in Identificatieresultaten
In QGIS 3.2 laten we nu zowel ellipsoïde als Cartesiaanse gebieden, lengtes en perimeters afzonderlijk zien in het paneel Identificatieresultaten. Het zien van de twee afzonderlijke metingen geeft gebruikers een beter begrip van potentiële problemen in gebieds- of afstandsberekeningen, veroorzaakt door incorrecte projectie of ellipsoïde keuzes.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Expressies
### Mogelijkheid: Nieuwe functies voor expressies
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Nieuwe variabelen:
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Deze mogelijkheid werd ontwikkeld door Mathieu Pellerin, Nyall Dawson
### Mogelijkheid: Meer hulpvaardiger expressiebouwer
De expressiebouwer maakt het nu eenvoudiger om expressies in QGIS te bouwen!
- De bouwer laat nu de beschrijving voor gegevensgedefinieerde waarden zien, inclusief het bereik van verwachte waarden uit de expressie
- Ctrl+klikken op een naam van een functie in de huidige expressie zal automatisch de Help voor die functie openen
- Het laat nu indicaties voor delen van expressies met fouten zien
- Het laat een volledige lijst van foutberichten zien, verkregen uit het parsen van de expressie

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Gebruikersinterface
### Mogelijkheid: Lagenpaneel: indicaties voor gefilterde kaartlagen
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

Dit voegt een mini-framewerk toe voor de weergave van extra pictogrammen in weergaven van de boom met lagen, naast de namen voor lagen en groepen. Tekst voor Helptips kan worden geassocieerd met indicaties om extra context voor indicaties te geven. In aanvulling daarop wordt een signaal gegeven als de gebruiker op indicaties klikt en aangepaste acties kunnen worden gedefinieerd. Het idee is dat indicaties in de toekomst kunnen worden gebruikt voor een subtiele weergave van verscheidene stukjes informatie, bijvoorbeeld:
- kaartlaag met ongeldige geometrieën
- kaartlaag met uitzonderingen voor direct opnieuw projecteren
- kaartlaag heeft een ontbrekende gegevensbron
- kaartlaag met ongeldig CRS

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Toestaan van aangepast voorvoegsel voor filters voor lokaliseren
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Openen van vectoren en rasters, opgeslagen op HTTP(S), FTP, of clouddiensten
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Snel veld voor veldberekening in werkbalk voor Lokaliseren
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Sneltoetsen voor het schakelen van panelen
sneltoets Ctrl+{no} 

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Mogelijkheid: Zoeken naar Favoriete plaatsen in Lokaliseren
Maakt het zoeken naar Favoriete plaatsen mogelijk. Dubbelklikken op een zoekresultaat zal zoomen naar de Favoriete plaats.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Deze mogelijkheid werd ontwikkeld door Klavs Pihlkjær
### Mogelijkheid: Projectacties sluiten en terugdraaien
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door: Nathan Woodrow, Nyall Dawson
### Mogelijkheid: Indicatie voor niet opgeslagen wijzigingen in titelbalk
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Te configureren vertraging voor kaarttips
Deze mogelijkheid werd ontwikkeld door jdugge
### Mogelijkheid: Laag of groep verplaatsen naar bovenste positie in paneel Lagen
Verplaatst de geselecteerde la(a)g(en) of groep(en) naar de bovenste positie in het paneel Lagen.

Deze mogelijkheid werd ontwikkeld door Mie Winstrup
### Mogelijkheid: Knop Inhoud van paneel Statistieken naar klembord kopiëren
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Zoeken naar pagina's Instellingen, Opties en projecteigenschappen vanuit Lokaliseren
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Deze mogelijkheid werd ontwikkeld door Klavs Pihlkjær
### Mogelijkheid: Indicaties voor ingebedde lagen en groepen
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Symbologie
### Mogelijkheid: Mooiere kleuren voor nieuwe lagen
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Renderen
### Mogelijkheid: Verbeterde kaartdecoratie Copyright
- Ondersteuning voor expressie voor de tekst van het auteursrecht.
- Verbeterde opties voor opmaken van de tekst, inclusief schaduwen, omtrekken, achtergronden, etc.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Lettertype en soort lettertype kan nu worden aangepast voor Schaalbalk in het hoofdvenster
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Aangepast SVG-pad en grootte voor decoratie Noordpijl
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Gegevensbeheer
### Mogelijkheid: Een gematerialiseerde weergave vernieuwen
Vanuit de browser kunt u, met een rechtsklik op een gematerialiseerde weergave, die nu vernieuwen.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: Ondersteuning voor Z en M in offline bewerken
Offline bewerken ondersteunt nu ook lagen met coördinaten Z en M.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Metadata voor projecten van QGIS
Volgend op het werk aan de metadata dat begon in QGIS 3.0, ondersteunt 3.2 nu metadata voor projecten van QGIS. Dit maakt het mogelijk gedetailleerde metadata in te stellen in projecteigenschappen, inclusief abstracten, sleutelwoorden, contact details, links, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door `Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS <https://www.arpa.piemonte.it/>`__

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formulieren en widgets
### Mogelijkheid: Multi-kolom lay-out voor widget relatie met waarden voor meerdere selecties
Het widget voor waarde van relatie met meerdere selecties ingeschakeld ondersteunt nu meerdere kolommen. Dit maakt een beter gebruik van de horizontale schermruimte mogelijk.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Toestaan van het gebruiken van een URL voor aangepaste formulieren voor attributen (UI-bestand)
Het UI-bestand zal bij elke sessie voor het eerste gebruik worden gedownload. Dit maakt het mogelijk om bijgewerkte UI-bestanden eenvoudiger te verdelen over cliënten.

This feature was funded by [SIRS](http://www.sirs-fr.com)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Formulieren voor dieper zoeken (cascading)
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS Danish User Group, Bo Victor Thomsen en Lene Fischer, North River Geographic

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## Legenda van laag
### Mogelijkheid: Optionele tekst boven symbolen voor vectorlagen
Deze mogelijkheid stelt gebruikers in staat extra informatie toe te voegen aan de symbolen in de legenda.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Groepen/Lagen kopiëren & plakken vanuit het ene project van QGIS naar een ander.
Maakt het mogelijk groepen en lagen te kopiëren en te plakken tussen projecten en profielen.

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## Printvormgeving
### Mogelijkheid: Data bepaalde tabelbron voor items in de attributentabel
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(Alle bestaande tabelattributen (instellingen voor kolommen) worden intact gelaten, dus het instellen van een data bepaalde-tabel om een laag met andere velden te maken zal resulteren in lege kolommen in de tabel.)

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Metadata voor project ingebed in exports van de lay-out
Opslaan van een afdruklay-out naar SVG, PDF of afbeeldingen zal nu enige metadata voor het project inbedden in het gemaakte bestand. Ondersteuning voor verschillende elementen van de metadata is afhankelijk van de individuele indeling van de export.

Dit werd mogelijk gemaakt door `Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS <https://www.arpa.piemonte.it/>`__

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Betere opmaak voor tekst van schaalbalk
QGIS 3.2 maakt het mogelijk dat het volledige bereik aan opties voor het opmaken van tekst wordt gebruikt in de tekst voor de schaalbalk, bijv. buffers, schaduwen, en vormen voor de achtergrond.

Onleesbare tekst voor de schaalbalk is iets uit het verleden!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Processing
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Mogelijkheid: Script laden uit sjabloon
Nieuwe optie om scripts voor Processing uit een aangepast sjabloon te laden

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Mogelijkheid: Algoritme Objectfilter voor modellen van Processing
Voegt een nieuw algoritme Objectfilter toe aan Grafische modellen bouwen. Maakt het mogelijk objecten van een bron te filteren, gebaseerd op expressies en de overeenkomende objecten te versturen naar verschillende uitvoeren als uiteindelijke producten of een andere pijplijn voor een algoritme voor verdere verwerking.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Zonehistogram
Dit nieuwe algoritme voegt velden toe die tellingen weergeven van elke unieke waarde uit een rasterlaag, opgenomen in zones die zijn gedefinieerd als polygonen.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Algoritmes Union, Difference and Intersection geporteerd naar C++
QGIS eigen algoritmes voor geoprocessing  zijn geporteerd van Python naar C++. In aanvulling daarop, om de uitvoering te verbeteren, zijn een aantal problemen met deze update opgelost.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
Dit nieuwe algoritme voor Processing projecteert punten uit een invoer puntenlaag met een gespecificeerde afstand en richting (azimut). Het ondersteunt dynamische parameters voor de afstand en richting zodat de afstand en richting kunnen worden overgenomen uit veldwaarden of expressies.

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Dynamische waarden voor parameters voor meer algoritmes
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

In 3.2 ondersteunen de volgende algoritmes nu dynamische parameters:
- Gaten verwijderen
- Duplicaatpunten verwijderen
- Vereenvoudigen
- Glad maken
- Aan grid 'snappen'
- Onderverdelen
- Doorsnede
- Transleren

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Multi-ring buffer (constante afstand)
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Feature: New \"segmentize\" algorithms
In QGIS 3.2 zijn twee nieuwe algoritmes voor het segmenteren van gebogen geometrieën toegevoegd aan Processing.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Optie om punten op alle delen van polygonen te maken
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Algoritme Rotate Features
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Foto's met geoverwijzingen importeren
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Optioneel mag de scan recursief zijn en kunt u een optionele tabel met goto's maken die niet konden worden gelezen of waarin geoverwijzingen ontbreken.

Het algoritme stelt automatisch de uitvoertabel in om een widget Externe bron te gebruiken om de gekoppelde foto's weer te geven in het formulier met attributen.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Swap x/y coordinate values
Dit algoritme verwisselt de waarden van de X- en Y-coördinaten in invoergeometrieën. Het kan worden gebruikt om geometrieën te repareren waarvan per ongeluk hun waarden voor breedte- en lengtegraad zijn verwisseld.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
Deze wijziging stelt gebruikers in staat op optioneel een sorteervolgorde in te stellen bij het toewijzen van waarden in het algoritme Oplopend veld toevoegen. Eerdere waarden werden altijd toegevoegd met behulp van de originele volgorde van de objecten. Met deze wijziging kunnen gebruikers de volgorde beheren waarin aan objecten waarden worden toegekend.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Indicaties voor eenheden van parameters voor afstand
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Aanvullend - als de eenheid in graden is, wordt naast de parameter een klein pictogram als waarschuwing weergegeven. De Helptip voor dit pictogram adviseert gebruikers om gegevens opnieuw te projecteren in een geschikt geprojecteerd lokaal coördinatensysteem.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Log voor algoritme kan worden opgeslagen/leeg gemaakt/gekopieerd
In het dialoogvenster voor de uitvoering van het algoritme zijn nieuwe knoppen toegevoegd om gebruikers in staat te stellen het huidige log op te slaan (naar tekst- of HTML-bestanden), de inhoud van het log te kopiëren naar het klembord en het log leeg te maken.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Wedge buffer
Dit nieuwe algoritme maakt wigvormige buffers vanuit invoerpunten.

De parameter azimut geeft de hoek (in graden) aan voor het midden van de wig naar het punt. De breedte van de buffer (in graden) wordt gespecificeerd door de parameter breedte. Onthoud dat de wig zich aan beide zijden van de richting van de azimut zal uitstrekken tot de helft van de breedte van de hoek. De buitenste radius van de buffer wordt gespecificeerd via outer radius, en optioneel mag ook een inner radius worden gespecificeerd.

Het algoritme ondersteunt dynamische parameters voor azimut, breedte, en radius.

De eigen uitvoer voor dit algoritme zijn geometrieën CurvePolygon, maar deze mogen automatisch worden gesegmenteerd naar Polygonen, afhankelijk van de indeling van de uitvoer.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid Buffers met variabele breedte
Nieuwe algoritmes voor Processing zijn toegevoegd om buffers met variabele breedten te maken, inclusief spits toelopende buffers (met een gespecificeerde diameter voor begin en eind) en buffers met variabele breedte uit waarden van M-lijnen.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritmes Rasters opnieuw classificeren 
Twee nieuwe eigen QGIS algoritmes voor het opnieuw classificeren van rasters zijn toegevoegd aan Processing. Deze zijn eenvoudig te gebruiken, maar toch snel en stabiel, en werken voor ELK type rasterlaag dat wordt ondersteund door QGIS!
- Opnieuw classificeren op laag: classificeert een raster opnieuw met behulp van de gespecificeerde bereiken via velden min/max/waarde uit een vectortabel
- Opnieuw classificeren op tabel: classificeert een raster opnieuw met behulp van een vaste tabel die door de gebruikers is ingevoerd in het dialoogvenster van het algoritme

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Union met één enkele laag
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Opties voor toepassing en projecten
### Mogelijkheid: Verplichte lagen in project
Voor verplichte lagen geldt dat zij niet uit het project kunnen worden verwijderd. Dit voegt extra beveiliging toe om gebruikers van het project te beschermen tegen het verwijderen van lagen waarvan zij denken dat die niet nodig zijn (bijv. gebruikt bij samenvoegingen, relaties, expressies).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Projecten in database PostgreSQL opslaan en laden
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Browser
### Mogelijkheid: Verbindingen voor XYZ-tegels opslaan/laden 
Vanuit het paneel Browser kunnen items voor XYZ-tegels worden geëxporteerd/geïmporteerd naar/vanuit een XML-bestand.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Mogelijkheid: Het thuispad voor het project kan handmatig worden ingesteld
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Thuispaden mogen ook worden ingesteld voor relatieve paden, in welk geval zij relatief zullen zijn aan de locatie waar het project is opgeslagen.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor lagen met mazen
Het initiële werk is gedaan om lagen met mazen te introduceren die het weergeven van gegevens op gestructureerde of niet gestructureerde mazen (rasters) ondersteunen in aanvulling op raster- en vectorlagen. Dit is nog steeds een werk in uitvoering, waarvan verwacht wordt dat het volledig zal zijn uitgevoerd QGIS 3.4. Het werk tot dusver leidt tot het maken vaneen nieuwe bibliotheek MDAL voor afhandeling van de verschillende indelingen van op mazen gebaseerde gegevens en onder de motorkap zijn er nieuwe APIs geïntroduceerd, echter de gebruikersinterface is nog niet geïmplementeerd.

Voor meer informatie, zie:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

en

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Automatisch instellen van standaard stijl voor lagen voor ArcGIS Feature Server-lagen
Wanneer lagen vanaf een Feature Server worden geladen in QGIS 3.2, zal daarop automatisch dezelfde stijl worden toegepast als die welke is gespecificeerd voor die laag op de server, overeenkomend met het uiterlijk van de laag wanneer die wordt geladen in ArcGIS.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Snellere query's voor Oracle
Bepaalde bewerkingen voor lagen van Oracle zijn behoorlijk sneller gemaakt, bijv. overeenkomsten van niet hoofdlettergevoelige waarden voor objecten.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Tabellijst voor een verbinding van een database voor Oracle beperken tot een vooraf ingesteld schema
Deze wijziging maakt het mogelijk at een schema wordt ingesteld in de eigenschappen voor verbindingen van een database van Oracle. Indien ingesteld zullen alleen tabellen die in dat schema zijn opgenomen worden gescand en vermeld voor de verbinding.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor Alleen-lezen voor gebogen geometrieën van Oracle
Eerder werden deze geometrieën geluidloos genegeerd.

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Plug-ins
### Mogelijkheid: Geschiedenis voor query in DB Manager toegevoegd
In 3.2 is het mogelijk om query's voor SQL op te slaan. De geschiedenis voor de query 's is beschikbaar op de tab SQL-venster van de plug-in DB Manager.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Feature: DB Manager uitvoeren van SQL op achtergrond
Deze mogelijkheid werd ontwikkeld door Paul Blottiere
## 3D-objecten
### Mogelijkheid: 3D-polygonen: Optioneel genereren van achterkanten
Soms hebben gegevenssets met 3D-polygonen geen consistente ordening van punten (met de klok mee vs. tegen de klok in) en dat zorgde voor sub-optimale resultaten in de 3D-weergave: ofwel enkele polygonen (muren) lijken te ontbreken als maken van achterkanten is ingeschakeld - of sommige polygonen zijn niet juist voorzien van een schaduw als maken van achterkanten is uitgeschakeld. met de nieuwe optie **Achterkanten toevoegen** ingeschakeld, zal de vormgever driehoeken genereren in beide richtingen (voor- en achterkant) wat de kwaliteit van renderen voor dergelijke gegevenssets aanmerkelijk verbeterd.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

De afbeelding bevat de vrij verkrijgbare gegevensset Prague 3D buildings.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
