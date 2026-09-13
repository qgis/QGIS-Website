---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: project
sidebar: true
title: Log met wijzigingen voor QGIS 3.2
type: visual-changelog

---
{{<content-start >}}
# Log met wijzigingen voor QGIS 3.2{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Datum uitgave 22-06-2018

De grootste uitgave van QGIS ooit! QGIS 3.2 brengt een enorme lijst met nieuwe wijzigingen - de hoogtepunten daarvan zullen we hier proberen te behandelen. Zoals altijd herinneren we u eraan dat QGIS een openbronproject is en vragen we u om te overwegen ons te sponsoren door [donaties]({{< ref "/funding/donate.md" >}}), [dragende lidmaatschappen]({{< ref "/funding/membership.md" >}}) of bijdragen aan de documentatie van de code, website, enzovoort.

**Dankwoord**

We willen onze dank uitspreken aan alle ontwikkelaars, schrijvers van documentatie, testers en alle andere mensen die vrijwillig hun tijd en inspanningen ter beschikking stellen (of mensen sponsoren om dat te kunnen doen). Vanuit de gemeenschap van QGIS hopen we dat u van deze uitgave zult genieten! Als u tijd of geld wilt doneren of op een andere wijze betrokken wilt zijn bij het opwaarderen van QGIS, kijk dan ook eens op [qgis.org](https://qgis.org) en help een handje!

QGIS wordt ondersteund door donoren en dragende leden. Een huidige lijst van donoren die grote en kleine bijdragen hebben gegeven aan het project kan worden bekeken op onze [lijst met donoren]({{< ref "/funding/donate.md" >}}). Als u een officieel dragend lid voor het project zou willen worden, bekijk dan [onze pagina voor dragende lidmaatschappen]({{< ref "/funding/membership.md" >}}) voor details. Ondersteuning van QGIS helpt ons om fondsen te verkrijgen voor onze halfjaarlijkse ontmoetingen van ontwikkelaars, de infrastructuur van het project te onderhouden en inspanningen voor het oplossen van problemen te financieren. Een volledige lijst van huidige dragende leden wordt hieronder weergegeven - een welgemeend bedankt voor al onze ondersteuners!

QGIS is gratis software en u bent niet verplicht om maar iets te betalen voor het gebruik ervan - in feite willen we mensen, wijd en zijd verspreid, aanmoedigen om het te gebruiken ongeacht uw financiële of sociale status - wij geloven dat het uitrusten van mensen met gereedschappen voor het maken van ruimtelijke beslissingen zal resulteren in een betere wereld voor de gehele mensheid.

{{<table-of-contents >}}
## Sponsoren voor QGIS versie 3.2
Een speciaal woord van dank aan al onze [dragende leden, sponsoren en donoren]({{< ref "/funding/membership.md" >}}) voor de hulp om het ons mogelijk te maken deze uitgave te doen!
## Algemeen
### Mogelijkheid: Nieuwe gezipte projectbestandsindeling .qgz is nu de standaard indeling
QGZ werd als optionele indeling toegevoegd in 3.0. Door van deze indeling de standaard te maken maakt het eenvoudiger om te komen tot een container die in staat is om bronnen zoals SVG, offline gegevens in GPKG, kleurverlopen, plug-ins of scripts in te bedden.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Mogelijkheid: Filteren op veldwaarden in widget Querybouwer
Bij het maken van een nieuw filter met een expressie in Querybouwer kunt u nu de waarden van de velden filteren in een voorbeeldpaneel.

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Salvatore Larosa](https://github.com/slarosa)
### Mogelijkheid: Kaart op VOLLEDIG scherm met Ctrl-Shift-Tab
Naast Ctrl-Tab kunt u nu Ctrl-Shift-Tab gebruiken, wat u de kaart zal laten zien en ALLEEN de kaart, geen werkbalken of knoppen meer (of zelfs zonder titel voor het venster in combinatie met F11). Geweldig voor projecteren op Volledig scherm via beamer of op grote schermen. U kunt nog steeds zoomen en verschuiven! (Gebaseerd op het werk van Mathieu Pellerin)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Richard Duivenvoorde
## Kaartgereedschap
### Mogelijkheid: Gereedschap Kaart vereenvoudigen kan nu ook objecten gladder maken
Het gereedschap Kaart vereenvoudigen is hernoemd naar \"Object vereenvoudigen\", en ondersteunt nu het interactief gladmaken van objecten.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Gereedschap Objecten identificeren met extra opties
Met de nieuwe verbeteringen kan de gebruiker nu soortgelijke gereedschappen gebruiken als met Selecteren om meerdere objecten te identificeren.

Dit werd mogelijk gemaakt door Leicestershire County Council en East Hampshire District Council

Deze mogelijkheid werd ontwikkeld door [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Sla ook de status Uitgevouwen/Ingeklapt op van knopen op de kaartthema's
Elk kaartthema zal ook vastleggen welke lagengroepen en items van de legenda uitgevouwen zijn, wanneer dus een kaartthema wordt geselecteerd, wordt de status Uitgevouwen/Ingeklapt toegepast op de boom van de lagen.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Automatische modus \"Zoomen naar selectie\" voor nieuwe kaartweergaven
Een nieuwe kaartweergave kan worden geconfigureerd om automatisch in te zoomen op de huidige selectie. Kan worden gecombineerd met verschillende kaartthema's, zoals in dit voorbeeld.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Technology One](https://www.technologyonecorp.com/)

Deze mogelijkheid werd ontwikkeld door [Nathan Woodrow](https://nathanw.net/)
### Mogelijkheid: Keuze voor methode van vereenvoudigen voor gereedschap Kaart vereenvoudigen
Dit maakt het mogelijk dat verschillende technieken worden gebruikt voor vereenvoudigen in het interactieve gereedschap Object vereenvoudigen, inclusief het cartografisch meer plezierige algoritme voor vereenvoudiging \"Visvalingam\".

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Zoomen naar gerelateerde objecten toegevoegd in formulieren
Er verschijnt een nieuwe knop in het subformulier van objectattributen wanneer één of meer records zijn geselecteerd in een gerelateerde tabel. De knop zoomt op de kaart nar deze objecten als zij geometrieën hebben.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door Jürgen Fischer
### Mogelijkheid: Cartesiaanse gebieden/lengtes/perimeters in Identificatieresultaten
In QGIS 3.2 laten we nu zowel ellipsoïde als Cartesiaanse gebieden, lengtes en perimeters afzonderlijk zien in het paneel Identificatieresultaten. Het zien van de twee afzonderlijke metingen geeft gebruikers een beter begrip van potentiële problemen in gebieds- of afstandsberekeningen, veroorzaakt door incorrecte projectie of ellipsoïde keuzes.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
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

Dit werd mogelijk gemaakt door [Technology One](https://www.technologyonecorp.com/)

Deze mogelijkheid werd ontwikkeld door [Nathan Woodrow](https://nathanw.net/)
## Gebruikersinterface
### Mogelijkheid: Lagenpaneel: indicaties voor gefilterde kaartlagen
De weergave van de boom met lagen in het hoofdvenster (ToC) krijgt ondersteuning voor indicaties die worden weergegeven als op een vectorlaag een filter is toegepast. Dit maakt het voor gebruikers eenvoudiger om te begrijpen dat ze kijken naar een subset van alle gegevens. Klikken op het pictogram van de indicatie brengt de Querybouwer naar voren.

Dit voegt een mini-framewerk toe voor de weergave van extra pictogrammen in weergaven van de boom met lagen, naast de namen voor lagen en groepen. Tekst voor Helptips kan worden geassocieerd met indicaties om extra context voor indicaties te geven. In aanvulling daarop wordt een signaal gegeven als de gebruiker op indicaties klikt en aangepaste acties kunnen worden gedefinieerd. Het idee is dat indicaties in de toekomst kunnen worden gebruikt voor een subtiele weergave van verscheidene stukjes informatie, bijvoorbeeld:
- kaartlaag met ongeldige geometrieën
- kaartlaag met uitzonderingen voor direct opnieuw projecteren
- kaartlaag heeft een ontbrekende gegevensbron
- kaartlaag met ongeldig CRS

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Toestaan van aangepast voorvoegsel voor filters voor lokaliseren
Voorvoegsels voor filters voor lokaliseren kunnen nu worden aangepast in de instellingen voor de toepassing op de tab \"Lokaliseren\"

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Openen van vectoren en rasters, opgeslagen op HTTP(S), FTP, of clouddiensten
In 3.2 zijn de panelen voor het beheren van vector en raster bijgewerkt om het openen van gegevenssets van vector en raster die zijn opgeslagen op HTTP(S), FTP, of clouddiensten te vereenvoudigen. Inclusief ondersteuning voor Basis HTTP(S) authenticatie.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Snel veld voor veldberekening in werkbalk voor Lokaliseren
QGIS 3.2 staat het evalueren van eenvoudige expressies toe (wel, in feite ELKE QGIS-expressie\… dus u zou optellen en dergelijke kunnen gebruiken als u dat echt zou willen!) door \"= \" in te voeren, gevolgd door een expressie in de werkbalk Lokaliseren. Als een geldige expressie wordt ingevoerd, wordt gebruikers een optie gegeven om het resultaat naar het klembord te kopiëren.

Invoeren van bijvoorbeeld \"= 10/3\" geeft een invoer voor Lokaliseren \"Kopieer\'3.3333333\' naar klembord\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Sneltoetsen voor het schakelen van panelen
sneltoets Ctrl+{no} 

Dit werd mogelijk gemaakt door [Technology One](https://www.technologyonecorp.com/)

Deze mogelijkheid werd ontwikkeld door [Nathan Woodrow](https://nathanw.net/)
### Mogelijkheid: Zoeken naar Favoriete plaatsen in Lokaliseren
Maakt het zoeken naar Favoriete plaatsen mogelijk. Dubbelklikken op een zoekresultaat zal zoomen naar de Favoriete plaats.

Korte video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

Het nieuwe filter presenteert zichzelf met een voorvoegsel \"b\" en met tr( \"Favoriete plaats\" ) als naam voor de weergave.

Deze mogelijkheid werd ontwikkeld door Klavs Pihlkjær
### Mogelijkheid: Projectacties sluiten en terugdraaien
Twee nieuwe acties zijn toegevoegd aan het menu \"Project\"
- \"Sluiten\": Sluit het actieve project, brengt het venster van QGIS terug naar de lijst \"Recente projecten\"
- \"Terugdraaien\": herstelt het actieve project naar de laatst opgeslagen status, zonder rekening te houden met alle niet-opgeslagen wijzigingen

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door: Nathan Woodrow, Nyall Dawson
### Mogelijkheid: Indicatie voor niet opgeslagen wijzigingen in titelbalk
QGIS 3.2 volgt nu de standaardbenadering voor de gebruikersinterface om aan te geven dat het huidige project niet opgeslagen wijzigingen heeft door een voorvoegsel \"\*\" toe te voegen aan de naam van het project in de titelbalk van de toepassing. Dit maakt het eenvoudiger om in één oogopslag te zien of u nog niet opgeslagen wijzigingen heeft!

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Te configureren vertraging voor kaarttips
Deze mogelijkheid werd ontwikkeld door jdugge
### Mogelijkheid: Laag of groep verplaatsen naar bovenste positie in paneel Lagen
Verplaatst de geselecteerde la(a)g(en) of groep(en) naar de bovenste positie in het paneel Lagen.

Deze mogelijkheid werd ontwikkeld door Mie Winstrup
### Mogelijkheid: Knop Inhoud van paneel Statistieken naar klembord kopiëren
Het is nu mogelijk om de uitvoertabel van het paneel Statistieken naar het klembord te kopiëren.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Zoeken naar pagina's Instellingen, Opties en projecteigenschappen vanuit Lokaliseren
Korte video: <https://www.youtube.com/watch?v=duB2YekUmV0>

Het nieuwe filter presenteert zichzelf met een voorvoegsel \"set\" en met tr( \"Instellingen\" ) als naam voor de weergave.

Deze mogelijkheid werd ontwikkeld door Klavs Pihlkjær
### Mogelijkheid: Indicaties voor ingebedde lagen en groepen
Ingebedde projectlagen en -groepen worden nu aangegeven door een handige indicatie \"ingebed\", wat het voor gebruikers onmiddellijk duidelijk maakt welke lagen en groepen in een project zijn ingebed.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Symbologie
### Mogelijkheid: Mooiere kleuren voor nieuwe lagen
De \"willekeurige\" kleuren die worden toegewezen aan nieuwe lagen zijn niet langer \"willekeurig\" maar worden in plaats daarvan willekeurig geselecteerd uit een voorkeuzepalet van "visueel prettige" kleuren. Zeg maar tot ziens tegen de lelijke groene babyspuug-lagen!

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Renderen
### Mogelijkheid: Verbeterde kaartdecoratie Copyright
- Ondersteuning voor expressie voor de tekst van het auteursrecht.
- Verbeterde opties voor opmaken van de tekst, inclusief schaduwen, omtrekken, achtergronden, etc.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Lettertype en soort lettertype kan nu worden aangepast voor Schaalbalk in het hoofdvenster
Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Aangepast SVG-pad en grootte voor decoratie Noordpijl
Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
## Gegevensbeheer
### Mogelijkheid: Een gematerialiseerde weergave vernieuwen
Vanuit de browser kunt u, met een rechtsklik op een gematerialiseerde weergave, die nu vernieuwen.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Etienne Trimaille](https://github.com/Gustry)
### Mogelijkheid: Ondersteuning voor Z en M in offline bewerken
Offline bewerken ondersteunt nu ook lagen met coördinaten Z en M.

Dit werd mogelijk gemaakt door [Oester Messtechnik](https://messtechnik.ch/)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Metadata voor projecten van QGIS
Volgend op het werk aan de metadata dat begon in QGIS 3.0, ondersteunt 3.2 nu metadata voor projecten van QGIS. Dit maakt het mogelijk gedetailleerde metadata in te stellen in projecteigenschappen, inclusief abstracten, sleutelwoorden, contact details, links, etc.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door `Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS <https://www.arpa.piemonte.it/>`__

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formulieren en widgets
### Mogelijkheid: Multi-kolom lay-out voor widget relatie met waarden voor meerdere selecties
Het widget voor waarde van relatie met meerdere selecties ingeschakeld ondersteunt nu meerdere kolommen. Dit maakt een beter gebruik van de horizontale schermruimte mogelijk.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

Deze mogelijkheid werd ontwikkeld door [David Signer, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Toestaan van het gebruiken van een URL voor aangepaste formulieren voor attributen (UI-bestand)
Het UI-bestand zal bij elke sessie voor het eerste gebruik worden gedownload. Dit maakt het mogelijk om bijgewerkte UI-bestanden eenvoudiger te verdelen over cliënten.

Dit werd mogelijk gemaakt door [SIRS](http://www.sirs-fr.com)

Deze mogelijkheid werd ontwikkeld door [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Formulieren voor dieper zoeken (cascading)
QGIS 3.2 introduceert ondersteuning voor dieper zoeken met formulieren (cascading), waarbij de waarden die beschikbaar zijn in één veld afhankelijk zijn van de waarden van andere velden. Deze mogelijkheid maakt het voor gebruikers mogelijk \“waarde-relatie\”-expressies te maken, gebaseerd op de huidige waarde van een ander veld in hetzelfde formulier. Wanneer de gebruiker de waarde van een veld aanpast, worden de in alle gerelateerde velden beschikbare waarden gefilterd om overeen te komen met de nieuwe waarde -- wat een hiërarchische filterstrategie mogelijk maakt (dieper zoeken, of cascading) in een formulier.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS Danish User Group, Bo Victor Thomsen en Lene Fischer, North River Geographic

Deze mogelijkheid werd ontwikkeld door [Alessandro Pasotti (North Road)](https://north-road.com)
## Legenda van laag
### Mogelijkheid: Optionele tekst boven symbolen voor vectorlagen
Deze mogelijkheid stelt gebruikers in staat extra informatie toe te voegen aan de symbolen in de legenda.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Groepen/Lagen kopiëren & plakken vanuit het ene project van QGIS naar een ander.
Maakt het mogelijk groepen en lagen te kopiëren en te plakken tussen projecten en profielen.

Deze mogelijkheid werd ontwikkeld door [Salvatore Larosa](https://github.com/slarosa)
## Printvormgeving
### Mogelijkheid: Data bepaalde tabelbron voor items in de attributentabel
Wanneer een attributentabel is ingesteld voor een bron \"Laagobjecten\", staat deze nieuwe mogelijkheid het toe dat de onderliggende vectorlaag, van waaruit de objecten afkomstig zijn, data bepaald-gedefinieerd is.

(Alle bestaande tabelattributen (instellingen voor kolommen) worden intact gelaten, dus het instellen van een data bepaalde-tabel om een laag met andere velden te maken zal resulteren in lege kolommen in de tabel.)

Dit werd mogelijk gemaakt door [Kartoza/InaSAFE](http://kartoza.com/en/)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Metadata voor project ingebed in exports van de lay-out
Opslaan van een afdruklay-out naar SVG, PDF of afbeeldingen zal nu enige metadata voor het project inbedden in het gemaakte bestand. Ondersteuning voor verschillende elementen van de metadata is afhankelijk van de individuele indeling van de export.

Dit werd mogelijk gemaakt door `Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS <https://www.arpa.piemonte.it/>`__

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Betere opmaak voor tekst van schaalbalk
QGIS 3.2 maakt het mogelijk dat het volledige bereik aan opties voor het opmaken van tekst wordt gebruikt in de tekst voor de schaalbalk, bijv. buffers, schaduwen, en vormen voor de achtergrond.

Onleesbare tekst voor de schaalbalk is iets uit het verleden!

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Processing
### Mogelijkheid: Verbeterd algoritme \'Join by attribute table\'
Het algoritme \'Join by attribute table\' is opgewaardeerd om een-tot-veel-samenvoegingen te ondersteunen (d.i. maken van afzonderlijke objecten voor elk overeenkomend object) alsook een optie om records die niet konden worden samengevoegd te negeren. Aanvullend kan nu een optioneel voorvoegsel voor samengevoegde velden worden gespecificeerd.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Mogelijkheid: Script laden uit sjabloon
Nieuwe optie om scripts voor Processing uit een aangepast sjabloon te laden

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Mogelijkheid: Algoritme Objectfilter voor modellen van Processing
Voegt een nieuw algoritme Objectfilter toe aan Grafische modellen bouwen. Maakt het mogelijk objecten van een bron te filteren, gebaseerd op expressies en de overeenkomende objecten te versturen naar verschillende uitvoeren als uiteindelijke producten of een andere pijplijn voor een algoritme voor verdere verwerking.

Lees deze [blogpost voor meer informatie](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Zwitserse QGIS gebruikersgroep](https://qgis.ch)

Deze mogelijkheid werd ontwikkeld door [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Mogelijkheid: Zonehistogram
Dit nieuwe algoritme voegt velden toe die tellingen weergeven van elke unieke waarde uit een rasterlaag, opgenomen in zones die zijn gedefinieerd als polygonen.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Algoritmes Union, Difference and Intersection geporteerd naar C++
QGIS eigen algoritmes voor geoprocessing  zijn geporteerd van Python naar C++. In aanvulling daarop, om de uitvoering te verbeteren, zijn een aantal problemen met deze update opgelost.

Dit werd mogelijk gemaakt door [InaSAFE DFAT](https://www.dfat.gov.au/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Algoritme \'Project points (cartesian)\'
Dit nieuwe algoritme voor Processing projecteert punten uit een invoer puntenlaag met een gespecificeerde afstand en richting (azimut). Het ondersteunt dynamische parameters voor de afstand en richting zodat de afstand en richting kunnen worden overgenomen uit veldwaarden of expressies.

Dit werd mogelijk gemaakt door [Nyall Dawson (North Road)](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Dynamische waarden voor parameters voor meer algoritmes
QGIS 3.2 borduurt voort op het werk dat begon in 3.0 om \"dynamische\" parameters voor geselecteerde algoritmes van Processing toe te staan. Dynamische parameters maken het voor gebruikers mogelijk om expressies of veldwaarden te gebruiken om de waarde van een parameter te specificeren terwijl het algoritme wordt uitgevoerd. Dus bijvoorbeeld de grootte van de buffer kan dynamisch worden berekend voor elk gebufferd individueel object.

In 3.2 ondersteunen de volgende algoritmes nu dynamische parameters:
- Gaten verwijderen
- Duplicaatpunten verwijderen
- Vereenvoudigen
- Glad maken
- Aan grid 'snappen'
- Onderverdelen
- Doorsnede
- Transleren

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Multi-ring buffer (constante afstand)
Dit nieuwe algoritme berekent een multi-ring (\'donuts\') buffer voor alle objecten in een invoerlaag, met behulp van een vaste of dynamische afstand en het aantal ringen.

Deze mogelijkheid werd ontwikkeld door Alex Bruy
### Mogelijkheid: Nieuw algoritme \"segmentize\"
In QGIS 3.2 zijn twee nieuwe algoritmes voor het segmenteren van gebogen geometrieën toegevoegd aan Processing.

\"Segmentize by maximum distance\": Het segmenteren wordt uitgevoerd door de maximale verschuivingsafstand te specificeren tussen de originele boog en de gesegmenteerde weergave.

\"Segmentize by maximum angle\": Het segmenteren wordt uitgevoerd door de maximale hoek van de radius te specificeren tussen punten op de recht gemaakte geometrie (bijv. de hoek van de boog die werd gemaakt vanuit het originele midden van de boog vergeleken met opvolgende punten op de gelineariseerde geometrie).

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Optie om punten op alle delen van polygonen te maken
De algoritmes \"Centroid\" en \"Point on surface\" hebben een nieuwe optie om punten te maken voor elk individueel deel van invoergeometrieën.

Deze mogelijkheid werd ontwikkeld door [Mathieu Pellerin](http://www.imhere-asia.com/)
### Mogelijkheid: Algoritme Rotate Features
Dit nieuwe algoritme maakt het draaien van objecten rond een ingestelde hoek mogelijk. Het draaien kan gebeuren rondom een ingesteld punt of rond het zwaartepunt van elk individueel object.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Lijnverloop in \"Add Geometry Attributes\"
Het algoritme \"Add Geometry Attributes\" berekent nu het lijnverloop en rechte afstanden voor lijnlagen.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Foto's met geoverwijzingen importeren
In QGIS 3.2 is een nieuw algoritme \"Import geotagged photos\" toegevoegd aan Processing. Het maakt het mogelijk een map te selecteren die het zal scannen op jpg-bestanden die zijn voorzien van geoverwijzingen en maakt een laag PointZ met het resultaat, met attributen voor pad van de foto, hoogte, richting en tijdstempel.

Optioneel mag de scan recursief zijn en kunt u een optionele tabel met goto's maken die niet konden worden gelezen of waarin geoverwijzingen ontbreken.

Het algoritme stelt automatisch de uitvoertabel in om een widget Externe bron te gebruiken om de gekoppelde foto's weer te geven in het formulier met attributen.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Swap x/y coordinate values
Dit algoritme verwisselt de waarden van de X- en Y-coördinaten in invoergeometrieën. Het kan worden gebruikt om geometrieën te repareren waarvan per ongeluk hun waarden voor breedte- en lengtegraad zijn verwisseld.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Optie voor volgorde voor \"Oplopend veld toevoegen\"
Deze wijziging stelt gebruikers in staat op optioneel een sorteervolgorde in te stellen bij het toewijzen van waarden in het algoritme Oplopend veld toevoegen. Eerdere waarden werden altijd toegevoegd met behulp van de originele volgorde van de objecten. Met deze wijziging kunnen gebruikers de volgorde beheren waarin aan objecten waarden worden toegekend.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Indicaties voor eenheden van parameters voor afstand
Wanneer een algoritme een typeparameter \"distance\" gebruikt, zullen de eenheden nu naast de parameter worden weergegeven. Dit vermijdt de verwarring bij het uitvoeren van algoritmes die afstanden gebruiken waarbij de eenheid afhankelijk is van een parameter Laag of CRS. Bijvoorbeeld: de parameter distance in het algoritme Buffer geeft de afstand in laageenheden\… Dus nu tonen we in QGIS 3.2 die eenheden direct in het dialoogvenster. Hopelijk leidt dit tot minder verwarring voor de gebruiker en ongewenste \"1000 graden buffers\"!

Aanvullend - als de eenheid in graden is, wordt naast de parameter een klein pictogram als waarschuwing weergegeven. De Helptip voor dit pictogram adviseert gebruikers om gegevens opnieuw te projecteren in een geschikt geprojecteerd lokaal coördinatensysteem.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Log voor algoritme kan worden opgeslagen/leeg gemaakt/gekopieerd
In het dialoogvenster voor de uitvoering van het algoritme zijn nieuwe knoppen toegevoegd om gebruikers in staat te stellen het huidige log op te slaan (naar tekst- of HTML-bestanden), de inhoud van het log te kopiëren naar het klembord en het log leeg te maken.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Wedge buffer
Dit nieuwe algoritme maakt wigvormige buffers vanuit invoerpunten.

De parameter azimut geeft de hoek (in graden) aan voor het midden van de wig naar het punt. De breedte van de buffer (in graden) wordt gespecificeerd door de parameter breedte. Onthoud dat de wig zich aan beide zijden van de richting van de azimut zal uitstrekken tot de helft van de breedte van de hoek. De buitenste radius van de buffer wordt gespecificeerd via outer radius, en optioneel mag ook een inner radius worden gespecificeerd.

Het algoritme ondersteunt dynamische parameters voor azimut, breedte, en radius.

De eigen uitvoer voor dit algoritme zijn geometrieën CurvePolygon, maar deze mogen automatisch worden gesegmenteerd naar Polygonen, afhankelijk van de indeling van de uitvoer.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid Buffers met variabele breedte
Nieuwe algoritmes voor Processing zijn toegevoegd om buffers met variabele breedten te maken, inclusief spits toelopende buffers (met een gespecificeerde diameter voor begin en eind) en buffers met variabele breedte uit waarden van M-lijnen.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritmes Rasters opnieuw classificeren 
Twee nieuwe eigen QGIS algoritmes voor het opnieuw classificeren van rasters zijn toegevoegd aan Processing. Deze zijn eenvoudig te gebruiken, maar toch snel en stabiel, en werken voor ELK type rasterlaag dat wordt ondersteund door QGIS!
- Opnieuw classificeren op laag: classificeert een raster opnieuw met behulp van de gespecificeerde bereiken via velden min/max/waarde uit een vectortabel
- Opnieuw classificeren op tabel: classificeert een raster opnieuw met behulp van een vaste tabel die door de gebruikers is ingevoerd in het dialoogvenster van het algoritme

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Algoritme Union met één enkele laag
Het algoritme Union mag nu worden uitgevoerd met een enkele invoerlaag om een overlap tussen de objecten op de laag op te lossen. Als bijvoorbeeld een gebied wordt bedekt door drie objecten, zal dat gebied uit die objecten worden gesneden en zullen drie nieuwe objecten worden toegevoegd, waarbij de attributen van de originele objecten worden gekopieerd.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [InaSAFE DFAT](https://www.dfat.gov.au/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Opties voor toepassing en projecten
### Mogelijkheid: Verplichte lagen in project
Voor verplichte lagen geldt dat zij niet uit het project kunnen worden verwijderd. Dit voegt extra beveiliging toe om gebruikers van het project te beschermen tegen het verwijderen van lagen waarvan zij denken dat die niet nodig zijn (bijv. gebruikt bij samenvoegingen, relaties, expressies).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
### Mogelijkheid: Projecten in database PostgreSQL opslaan en laden
Gebruikers kunnen nu hun projecten opslaan in een database van PostgreSQL. Project kan worden opgeslagen in het menu **Project \> Opslaan naar \> PostgreSQL** en geladen met behulp van het menu **Project \> Openen uit \> PostgreSQL**. In de database opgeslagen projecten kunnen ook worden geladen via het venster van de browser (projecten worden weergegeven onder het schema waaronder ze werden opgeslagen, samen met andere lagen).

Opslaan/laden van projecten van QGIS moet expliciet zijn ingeschakeld in de instellingen voor de verbindingen van PostgreSQL: er is een nieuwe optie \"Allow saving/loading QGIS projects in the database\" die standaard is uitgeschakeld.

Een nieuwe API werd geïntroduceerd die het maken van aangepaste implementaties voor het opslaan van projecten mogelijk maakt (zou kunnen worden gebruikt door plug-ins). Gerelateerde QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

Dit werd mogelijk gemaakt door [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) binnen het project ERIKUS](https://www.arpa.piemonte.it/)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) en [Faunalia](https://www.faunalia.eu)
## Browser
### Mogelijkheid: Verbindingen voor XYZ-tegels opslaan/laden 
Vanuit het paneel Browser kunnen items voor XYZ-tegels worden geëxporteerd/geïmporteerd naar/vanuit een XML-bestand.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Salvatore Larosa](https://github.com/slarosa)
### Mogelijkheid: Het thuispad voor het project kan handmatig worden ingesteld
Deze nieuwe mogelijkheid in QGIS 3.2 maakt het mogelijk het thuispad voor het project (dat wordt gebruikt door de browser om het item \'Thuis voor project\' te maken) door gebruikers te laten worden ingesteld voor een project. In plaats van altijd overeen te komen met de locatie waar het project is opgeslagen.

Dit stelt gebruikers in staat om het thuis voor het project in te stellen voor een map die gegevens en andere inhoud bevat, en is speciaal nuttig voor organisaties waar projecten van QGIS niet worden opgeslagen in de bronmap van een \'project\' van de organisatie.

Thuispaden mogen ook worden ingesteld voor relatieve paden, in welk geval zij relatief zullen zijn aan de locatie waar het project is opgeslagen.

Het pad kan worden ingesteld via het dialoogvenster Projecteigenschappen, of door met rechts te klikken op het item Thuis voor project in de browser en te selecteren \'Thuis voor project instellen\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Gegevensproviders
### Mogelijkheid: Ondersteuning voor lagen met mazen
Het initiële werk is gedaan om lagen met mazen te introduceren die het weergeven van gegevens op gestructureerde of niet gestructureerde mazen (rasters) ondersteunen in aanvulling op raster- en vectorlagen. Dit is nog steeds een werk in uitvoering, waarvan verwacht wordt dat het volledig zal zijn uitgevoerd QGIS 3.4. Het werk tot dusver leidt tot het maken vaneen nieuwe bibliotheek MDAL voor afhandeling van de verschillende indelingen van op mazen gebaseerde gegevens en onder de motorkap zijn er nieuwe APIs geïntroduceerd, echter de gebruikersinterface is nog niet geïmplementeerd.

Voor meer informatie, zie:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

en

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Peter Petrik en Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Mogelijkheid: Automatisch instellen van standaard stijl voor lagen voor ArcGIS Feature Server-lagen
Wanneer lagen vanaf een Feature Server worden geladen in QGIS 3.2, zal daarop automatisch dezelfde stijl worden toegepast als die welke is gespecificeerd voor die laag op de server, overeenkomend met het uiterlijk van de laag wanneer die wordt geladen in ArcGIS.

Deze mogelijkheid werd mogelijk gemaakt door SMEC/SJ

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Snellere query's voor Oracle
Bepaalde bewerkingen voor lagen van Oracle zijn behoorlijk sneller gemaakt, bijv. overeenkomsten van niet hoofdlettergevoelige waarden voor objecten.

Dit werd mogelijk gemaakt door [North Road](https://north-road.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Tabellijst voor een verbinding van een database voor Oracle beperken tot een vooraf ingesteld schema
Deze wijziging maakt het mogelijk at een schema wordt ingesteld in de eigenschappen voor verbindingen van een database van Oracle. Indien ingesteld zullen alleen tabellen die in dat schema zijn opgenomen worden gescand en vermeld voor de verbinding.

Eerder bestond de optie om de scan te beperken tot tabellen die aan de gebruiker toebehoorden. Maar die optie ondersteunt niet het gebruik waarbij een verbinding toegang tot de tabellen van een andere gebruiker moet hebben. En de standaardinstelling \"scan everything\" is te uitgebreid (omdat het vaak meerdere minuten vergt om uit te voeren, in het bijzonder wanneer geometrietabellen worden weergegeven).

Dit werd mogelijk gemaakt door [Open Spatial](http://www.openspatial.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
### Mogelijkheid: Ondersteuning voor Alleen-lezen voor gebogen geometrieën van Oracle
Eerder werden deze geometrieën geluidloos genegeerd.

Dit werd mogelijk gemaakt door [Open Spatial](http://www.openspatial.com)

Deze mogelijkheid werd ontwikkeld door [Nyall Dawson (North Road)](https://north-road.com)
## Plug-ins
### Mogelijkheid: Geschiedenis voor query in DB Manager toegevoegd
In 3.2 is het mogelijk om query's voor SQL op te slaan. De geschiedenis voor de query 's is beschikbaar op de tab SQL-venster van de plug-in DB Manager.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Salvatore Larosa](https://github.com/slarosa)
### Mogelijkheid: DB Manager uitvoeren van SQL op achtergrond
Deze mogelijkheid werd ontwikkeld door Paul Blottiere
## 3D-objecten
### Mogelijkheid: 3D-polygonen: Optioneel genereren van achterkanten
Soms hebben gegevenssets met 3D-polygonen geen consistente ordening van punten (met de klok mee vs. tegen de klok in) en dat zorgde voor sub-optimale resultaten in de 3D-weergave: ofwel enkele polygonen (muren) lijken te ontbreken als maken van achterkanten is ingeschakeld - of sommige polygonen zijn niet juist voorzien van een schaduw als maken van achterkanten is uitgeschakeld. met de nieuwe optie **Achterkanten toevoegen** ingeschakeld, zal de vormgever driehoeken genereren in beide richtingen (voor- en achterkant) wat de kwaliteit van renderen voor dergelijke gegevenssets aanmerkelijk verbeterd.

Het enige nadeel bij het gebruiken van deze optie is dat meer grafisch geheugen wordt gebruikt (dubbele hoeveelheid vergeleken met gegevens van punten). Zorg ervoor dat de modus voor maken is ingesteld op \"Back\" bij het gebruiken van deze optie, anders zal er geen zichtbaar verschil zijn, omdat de scene nog steeds polygonen met onjuiste schaduwen zal renderen.

De afbeelding bevat de vrij verkrijgbare gegevensset Prague 3D buildings.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

Deze mogelijkheid werd ontwikkeld door [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
