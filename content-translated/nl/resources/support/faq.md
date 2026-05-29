---
draft: false
sidebar: true
subtitle: ''
title: FAQ
type: page

---
{{<content-start >}}
# FAQ
Hier verzamelen we antwoorden op veelgestelde vragen.
## Gebruikersvragen
### Problemen met downloaden
Als u probeert QGIS te downloaden en er lijkt niets te gebeuren, raadpleeg dan de downloadbeheerder van uw browser. Dit is gewoonlijk te vinden als een pictogram (gebaseerd op een pijl, stopwatch of taartstuk-diagram) in de rechterbovenhoek van het venster van uw browser. Klik op het pictogram om de voortgang van het proces van downloaden te zien of om het downloaden te annuleren. De normale procedure voor downloads in de browser is, dat het u eerst vraagt waar het bestand moet worden opgeslagen (met een dialoogvenster in de browser) en dan moet u wachten tot het downloaden is voltooid. Omdat QGIS pakketten installeert, afhankelijk van het besturingssysteem, die nogal groot kunnen zijn, moet u geduldig zijn. De grootte van de download kan ergens liggen tussen enkele honderden megabytes tot wel meer dan een gigabyte (in het geval van MS Windows MSI-pakketten). Afhankelijk van uw downloadsnelheid en de belasting op de server van QGIS, kunnen downloads variëren in duur van enkele minuten tot enkele uren.
### Moet ik doneren om QGIS te kunnen downloaden?
Dat is een misvatting die we af en toe horen, maar het is niet waar. Doneren aan QGIS is optioneel. Na het downloaden van QGIS verschijnt er een bericht dat u eraan herinnert dat u optioneel kunt doneren aan QGIS. U kunt echter drukken op "Sluit dit venster" en zonder problemen doorgaan met downloaden. We willen dat QGIS toegankelijk is voor iedereen, het maakt ons niet uit hoe uw financiële situatie is. Als u QGIS voor het eerst gebruikt raden wij u aan dat u QGIS eerst download, installeert en test en kijkt of de software nuttig is voor de taken die u wilt uitvoeren. Alleen als u QGIS goed genoeg vindt en het u substantieel helpt met uw zaken, taken of processen, zou u erover kunnen denken om te doneren aan QGIS of het als een ondersteunend lid te ondersteunen.
### Hoe stel je een vraag over QGIS?
Als u een aan QGIS gerelateerde vraag gaat stellen via de [mailinglijsten]({{< ref "community/organisation/mailinglists" >}}), verschaf dan voldoende informatie om anderen eenvoudig te laten begrijpen wat uw probleem is. Zonder een heldere en precieze vraag is het voor iedereen moeilijk om een antwoord te geven of vergt dat te veel tijd, omdat het antwoord een vraag aan u zal zijn, etc etc. U wordt gevraagd informatie te verschaffen zoals:
- bij voorkeur een duidelijk onderwerp van uw e-mail
- welke versie van QGIS heeft u gebruikt op dat moment (exact)
- wat u verwacht te krijgen
- indien van toepassing, wat u probeerde te doen en het resultaat dat u verkreeg
- als uw vraag gaat over iets dat stuk is, kunt u ook toevoegen:
  - wat is de exacte fout (indien mogelijk: schermafdruk, stacktrace, kopie van de tekst van de fout)
  - welk besturingssysteem (OS) en welke versie
  - welke installatie heeft u gebruikt (osgeo4w? standalone-installer? zelf gecompileerd?)
  - wanneer ging het mis (opnieuw installeren, nieuwe installatie, bijwerken van het systeem, wijzigingen in het project)

Onthoud dat hoe nauwkeuriger uw vraag is, des te sneller en nauwkeuriger het antwoord kan zijn.

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
In het geval van een kapotte functie kunt u nog even kijken op [QGIS issue tracker](https://github.com/qgis/QGIS/issues) voordat u naar de lijst mailt. Meer informatie op [bug-reporting]({{< ref "resources/support/bug-reporting" >}}).

{{<rich-content-end >}}

{{<rich-box-end >}}
### Hoe worden namen voor uitgaven van QGIS geselecteerd?
Na een succesvolle bijeenkomst van ontwikkelaars in Zurich (Zwitserland), besloten we dat de volgende uitgave daaraan gerelateerd zou zijn. Sindsdien worden alle uitgaven vernoemd naar locaties van onze ontwikkelaarsbijeenkomsten.
### Kan ik ook ECW (Erdas) bestanden openen met QGIS?
ECW is een bestandsindeling met een eigenaar - bekijk hun [licentiepagina](https://supportsi.hexagon.com/s/article/License-for-reading-or-writing-ECW-in-third-party-software) om te begrijpen hoe u het mag gebruiken. Raadpleeg ook de [documentatie van GDAL](https://gdal.org/en/stable/drivers/raster/ecw.html#creation-options-1) voor opmerkingen over hoe gelicentieerde mogelijkheden in te schakelen als u een betaalde versie van ECW hebt. Ondersteuning voor ECW is niet standaard opgenomen in alle binaire versies van QGIS en voor alle platforms.

**Platformspecifieke opmerkingen:**

***Windows***: Als u Windows gebruikt en de **offline installatieprogramma's** hebt gedownload (verschaft via de knoppen voor downloaden, gelabeld **Lange Termijn Versie voor Windows ({{< param "ltrversion" >}} {{< param "ltrnote" >}})** en **Laatste versie voor Windows ({{< param "version" >}})**), is ondersteuning voor lezen van ECW standaard opgenomen.

Als u het **OSGeo4W netwerk installatiepakket** gebruikt, is ondersteuning voor ECW standaard geïnstalleerd als u de werkstroom Express install gebruikt. Bij het handmatig selecteren van componenten moet u expliciet het pakket `gdal-ecw` inschakelen om ervoor te zorgen dat ondersteuning voor ECW wordt opgenomen in uw installatie.

***macOS***: Als u macOS gebruikt, kunt u het DMG-bestand downloaden vanaf [QGIS downloaden](https://qgis.org/download/). Dat bevat standaard ondersteuning voor ECW.

***Linux***: Standaard bevatten de QGIS binaire bestanden voor de meeste distributies voor Linux *niet* standaard ondersteuning voor ECW. U kunt echter besprekingen en oplossingen voor richtlijnen over het toevoegen van deze ondersteuning vinden in verscheidene bronnen.

Voor Ubuntu bijvoorbeeld kunt u ook de volgende bronnen bekijken:
- [Github - GDAL: How to open ECW Maps in QGIS 3.22](https://github.com/OSGeo/gdal/issues/8239)
- [Reddit - QGIS: Problem loading ECW file in Ubuntu (Linux)](https://www.reddit.com/r/QGIS/comments/icw98f/problem_loading_ecw_file_in_ubuntu_linux/?rdt=54968)
- [GIS Stack Exchange: Installing QGIS with ECW support on ubuntu 20.04](https://gis.stackexchange.com/questions/429214/installing-qgis-with-ecw-support-on-ubuntu-20-04/434980#434980).

### Hoe kan ik een VPAT / HECVAT / ander US-conform formulier of informatie krijgen?
Neem contact op met de US gebruikersgroep. Zij weten veel over deze onderwerpen. Meer info en contactdetails: https://www.qgis-us.org
## Vragen van ontwikkelaars
### Kan ik QGIS zelf compileren?
Ja, compileren van QGIS vanuit de bron is mogelijk, ongeacht welk OS u gebruikt (Windows, macOS, Linux). Lees dan  [Building QGIS from source](https://github.com/qgis/QGIS/blob/master/INSTALL.md)
## Informatie over citeren
### Hoe QGIS te noemen?
Om te refereren aan QGIS in uw werk, of voor een opdracht, gebruik dan een type citaat dat nuttiger kan zijn:

Hier zijn enkele keuzes om te refereren aan het algehele softwareproject QGIS, een specifieke gebruikte versie van QGIS, of documentatie van QGIS om reproduceren toe te staan:

**Het project QGIS als een evoluerend softwareproject, onafhankelijk van een specifieke softwareuitgave, door Digital Object Identifier (concept-DOI)**

Gebruik het concept DOI [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6139224.svg)](https://doi.org/10.5281/zenodo.6139224) bij
- verwijzen naar de software QGIS in het algemeen (bijv. in introducties of delen op de achtergrond)
- beschrijven van werkstromen waar de exacte versie niet zoveel uitmaakt
- citeren van QGIS als een onderzoeksgereedschap voor de lange termijn of infrastructuur

Het concep-DOI zal altijd terugvallen op de laatste versie van QGIS en in de tijd een stabiele referentie verschaffen naar het softwareproject.

**Specifieke softwareuitgaven van QGIS door Digital Object Identifier (versie-DOI)**

Elke QGIS-uitgave vanaf 3.22.4 (2022) heeft zijn eigen versie-DOI die een nauwkeurig, gearchiveerd snapshot van de software identificeert (bijv. een specifieke softwareuitgave). Alle versie-DOI's zijn gekoppeld aan het concept-DOI van het project QGIS.

Bekijk de landingspagina van QGIS Zenodo ([landingspagina QGIS Zenodo](https://zenodo.org/search?q=parent.id%3A6139224&f=allversions%3Atrue&l=list&p=1&s=10&sort=version)) voor alle specifieke versie-DOI's.
- QGIS 4.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18889261.svg)](https://doi.org/10.5281/zenodo.18889261)
- QGIS 3.44 LTR [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15705458.svg)](https://doi.org/10.5281/zenodo.15705458)

**Benoem het project QGIS in het algemeen**

QGIS.org, {{< yeartag >}}. QGIS Geographic Information System. QGIS Association. http://www.qgis.org

**Benoem de handleiding voor ontwikkelaars van QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Developers Manual. QGIS Association. Electronic document: {{< param-link "devcite" >}}

**Benoem de Installatiegids van QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Installation Guide. QGIS Association. Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md

**Benoem de Gebruikershandleiding van QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System User Guide. QGIS Association. Electronic document: {{< param-link "userguidecite" >}}

**Benoem de QGIS Serverdocumentatie**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "servercite" >}}

**Benoem de QGIS API-documentatie**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "apicite" >}}

**Voorkeursindeling:** [BibTeX](https://en.wikipedia.org/wiki/BibTeX)

Voorbeeld item BibTeX:
```
@Manual{QGIS_software,
  title = {QGIS Geographic Information System},
  author = {{QGIS Development Team}},
  organization = {QGIS Association},
  year = {{{< yeartag >}}},
  url = {https://www.qgis.org},
}
```
**Citeer het artikel over QGIS in Patterns**
```
@article{graser2025,
  title = {The QGIS project: Spatial without compromise},
  journal = {Patterns},
  volume = {6},
  number = {7},
  pages = {101265},
  year = {2025},
  issn = {2666-3899},
  doi = {https://doi.org/10.1016/j.patter.2025.101265},
  url = {https://www.sciencedirect.com/science/article/pii/S2666389925001138},
  author = {Anita Graser and Tim Sutton and Marco Bernasocchi}
}
```
### Ik maakte een kaart met QGIS, moet ik QGIS daarop vermelden?
Er is geen verplichting om QGIS te vermelden op kaarten die ermee gemaakt zijn. Het wordt natuurlijk wel op prijs gesteld als u een opmerking zou willen toevoegen die vermeldt dat de kaart werd gemaakt met QGIS. "Gemaakt met QGIS" of "Kaart gemaakt met het vrije en open-bron QGIS" zijn goede voorbeelden van een dergelijke opmerking.

{{<rich-box-start icon="✋" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Opmerking
Vermeld niet ©QGIS, omdat QGIS geen auteursrechten heeft op uw werk.

{{<rich-content-end >}}

{{<rich-box-end >}}

{{<content-end >}}
