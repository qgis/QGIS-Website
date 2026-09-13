---
HasBanner: false
draft: false
releaseDate: '2020-02-21'
section: projekter
sidebar: true
title: Endringslogg for QGIS 3.12
type: visual-changelog

---
{{<content-start >}}
# Endringslogg for QGIS 3.12{#changelog312 }
![image1](images/projects/dbf38cfe3b603e7e0b840336d39b399a1a46e52d.png)

Release date: 2020-02-21

QGIS 3.12 har en del ny funksjonalitet og et tonn av feilrettinger. Denne utgaven har noe for alle, for eksempel påskriftsmaskeringer, lokal PostGIS-rastertilbyder og nye muligheter med maskenettlag. Vi minner om at QGIS har åpen kildekode, og hadde satt pris på støtte gjennom f.eks. donasjon, sponsing, bidrag til hjelpetekster eller nettsida.

**Takk**

Takk til alle utviklerne, hjelpetekstforfatterne, testerne og alle dere andre frivillige som bidrar med deres tid og krefter (eller betaler andre for å gjøre det). QGIS-fellesskapet håper du setter pris på denne utgivelsen. Besøk qgis.org hvis du har anledning til å donere tid, penger eller på andre måter hjelpe QGIS med å bli bedre.

QGIS støttes av donasjoner og sponsing. Donasjonslista viser alle som har bidratt økonomisk til prosjektet. Besøk sponsorsida vår hvis du vil bli offisiell prosjektsponsor. Sponsing av QGIS understøtter våre seks årlige utviklertreff, vedlikehold av prosjektets infrastruktur og feilretting. Nedenfor følger ei fullstendig liste over dagens sponsorer – takk til dem.

{{<fund type="active" >}}

QGIS er fri programvare og du forpliktes ikke til å betale for bruk. Tvert imot oppfordrer vi alle til å bruke programmet uavhengig av økonomisk og sosial status. Vi mener at å gi ut et romlig beslutningsverktøy vil føre til et bedre samfunn for hele menneskeheten.

{{<table-of-contents >}}
## Kartverktøyer
### Funksjonalitet: QgsMapLayerAction: Legger til ny oppføring i kontekstmenyen for handlinger på utvalg
Det er lagt til en ny menyoppføring (handlinger på utvalg) i lagtreets kontekstmeny. Den vises kun når nødvendig (laget har et utvalg, og handlinger kan utføres på dette utvalget). 

![imageQ1](https://user-images.githubusercontent.com/127259/74035907-7f334580-49bb-11ea-8d2d-b99eaa10aa89.png)

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funksjonalitet: Vis avstand fra GPS-posisjon til musepeker
Avstand og retning mellom musepekers posisjon i kartvinduet og GPS-posisjon vises i sanntid i statuslinja når en GPS-enhet er tilkoblet.

Denne visningen følger prosjektinnstillingene for avstander og retninger. 

![Peek 2020-01-14 16-06](https://user-images.githubusercontent.com/1829991/72318360-cd6c6600-36e7-11ea-9f2d-9a47d8772623.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Ny prosjektinnstilling for formatert visning av retningsvinkler
Fanen Innstillinger – Oppsett … – Kartverktøy har en ny innstilling som styrer forvalgt format for visning av retningsvinkler i nye prosjekter. Nylig opprettede prosjekter vil arve denne forvalgte innstillingen.

Dialogvinduet «prosjektegenskaper» har også en ny innstilling for prosjektspesifikt visningsformat for retningsvinkel.

The intention is that whenever angular bearings are shown in QGIS, they will be formatted using the current project\'s bearing format settings.

Det er også lagt til nye API-funksjoner som gir en stabil og enkel måte å velge og hente denne og lignende innstillinger.

![Peek 2020-01-09 11-08](https://user-images.githubusercontent.com/1829991/72029046-5fcbce80-32d0-11ea-8571-0ae8fa8e3bb0.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
## Brukergrensesnitt
### Funksjonalitet: Fravelg tabeller etter at PostgreSQL-data er lagt til med «Legg til»-knappen.
QGIS bør fravelge tidligere valgte tabeller etter at PostgreSQL-data legges til i datakildehåndteringen.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funksjonalitet: Vis i statuslinja hvor langt og i hvilken retning utsnittet er flyttet
We added the total pan distance and bearing in the status bar during canvas pan operations. Allows users to know exactly how far (and in what direction) they\'ve dragged the map.

![image5](images/entries/48c75d20d3805af3dad8c7faae3c3786a8f6fed0.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Ny innstilling som velger prosjektfilas standard filformat (qgs/qgz)
Vi har lagt til en global innstilling der man kan velge foretrukket filformat for prosjektfila.

![imageQ2](https://user-images.githubusercontent.com/127259/72597971-2bc75d80-390f-11ea-84af-7f2c25d5568a.png)

Denne funksjonaliteten ble finansiert av GEM foundation.

This feature was developed by [Denis Rouzaud](https://api.github.com/users/3nids)
### Funksjonalitet: Fikse ugyldige attributter ved kopiering til et annet lag
It\'s possible to copy features from one layer to another. If there are the same fields in the destination layer, then the attributes for them are taken from the original feature. If not, the default value is taken. Otherwise, the new attribute is null.

Hvis mållaget har skranker for feltene så bør de kontrolleres. Tidligere ble attributtene bare kopiert rett over slik at verdiene kunne bli ugyldige.

That\'s why now the attributes are checked against the constraints. And for all the invalid features a dialog pops up.

![copydialog2](https://user-images.githubusercontent.com/28384354/72243171-7e410b00-35eb-11ea-8903-11bd56cd9da6.gif)

Dialogvinduet har færre valgmuligheter når kun ett objekt limes inn:

![copypastesingle](https://user-images.githubusercontent.com/28384354/72243125-5ce01f00-35eb-11ea-897e-0bccdcf083d7.png)

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Funksjonalitet: Dra et kartlag fra lagtreet til et skjermelement for valg av KRS
\...to set the projection to match that layer. Just a little timesaving shortcut!

![Peek 2019-12-20 11-27](https://user-images.githubusercontent.com/1829991/71222288-b7070080-231b-11ea-89f4-af856dece4c3.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Rasterkalkulatoren har nå fått flere knapper og valideringsfunksjon
Det er nå lagt til knapper for ABS/MIN/MAX og validering av uttrykk.

![image10](https://user-images.githubusercontent.com/142164/68952420-1bd0b780-07c0-11ea-88d1-2ad0a8b5591e.gif)

Denne funksjonaliteten ble utviklet av Alessandro Pasotti.
## Symbologi
### Funksjonalitet: Animering av vektorspor og strømlinjer for maskenettlag
Mesh vector renderer now can visualize streamlines and particles on top of existing \"arrow\" mode.

![image11](images/entries/5b772e74d433e766b50023cd107aad9cb1d68de6.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Selektiv maskering
A new advanced rendering feature has been added: selective masking. It allows the definition of \'masks\' areas around labels or point markers. These masks will \"un-draw\" only some symbol layers of other layers underneath, chosen by the user.

![image12](https://user-images.githubusercontent.com/1618556/62111873-d68c8680-b2b1-11e9-8cd4-19077f99a8ff.gif)

This feature was funded by [QGIS.CH and others through a cofunding campaign](https://oslandia.com/en/offre-qgis/selective-masking/)

This feature was developed by [Hugo Mercier (Oslandia)](https://www.oslandia.com)
### Funksjonalitet: Fall tilbake til statisk verdi for rotasjon hvis uttrykket ikke kan evalueres
Datadefinert rotasjon fungerer endelig fullgodt i tegnforklaringen. Man kunne også tidligere bruke datadefinert rotasjon av symboler og de enkelte symbollagene, men dette gav en ødelagt tegnforklaring. Rotasjon av symboler (og symboldeler i symbollag) i tegnforklaringen kan nå styres ved å endre standardverdiene ved siden av de datadefinerte egenskapene.

Tidligere falt man tilbake til verdien 0 hvis uttrykket mislyktes, og dermed kunne det i noen tilfeller bli vanskelig å lage en ordentlig tegnforklaring.

F.eks. to symbollag med følgende rotasjonsuttrykk

    "orientation"
    
og

    90 + "orientation"
    
som gir to vinkelrette symbollag, rotert i henhold til et felt med rotasjonsverdier.

I tegnforklaringen (og i forhåndsvisningen av symbolene) vises begge lagene med rotasjon lik 0, fordi det ikke finnes noe tilhørende objekt med verdi i feltet for rotasjon.

Nå faller man tilbake til gitte, statiske, verdier. Dette gjør det intuitivt å sette opp tegnforklaringen i slike tilfeller.

**Før**

![Peek 2019-12-08 09-18](https://user-images.githubusercontent.com/588407/70386652-acec1600-199b-11ea-8457-f9dd54c84272.gif)

**Etter**

![Peek 2019-12-08 09-16](https://user-images.githubusercontent.com/588407/70386651-acec1600-199b-11ea-8ce2-27798aec38a7.gif)

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Funksjonalitet: Tilfeldig markørfyll kan nå legge til punkter ut fra tetthet
QGIS har nå fått tilfeldig markørfyll, der antall punkt er basert på tetthet.

![image15](https://user-images.githubusercontent.com/1728657/67672096-c2881c00-f9a9-11e9-8394-d73505d05309.gif)

Denne funksjonaliteten ble utviklet av Mathieu Pellerin.
### Funksjonalitet: Ny symbollagstype, tilfeldig markørfyll
This feature adds a new fill symbol layer type \"Random marker fill\". It allows polygon features to be rendered using a marker symbol placed at random locations within the polygon boundary.

Den har følgende valg:
- antall markørsymboler per flate
- skal flatekanten beskjære markører eller ikke
- selvvalgt initialiseringsverdi for tilfeldige tall – samme verdi låser plasseringen av markørene, noe som er nyttig når kartet oppdateres (og gir et visuelt bra resultat i QGIS Server og ved flisebasert opptegning)

![image16](https://user-images.githubusercontent.com/1829991/66734145-51267480-eea5-11e9-9e0a-3bfeee15f976.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Velg uttegningsfarge for nulldatapiksler i rasterlag 
Allows raster nodata pixels to be colored in a specific (non-transparent) color. Designed to match the \"Display background value\" option from ArcMap.

![image17](https://user-images.githubusercontent.com/1728657/64846100-f4c9fe00-d635-11e9-8acb-367ad2dd2915.png)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Påskriftsverktøy
### Funksjonalitet: Slette selvvalgt påskriftsposisjon
Det er nå mulig å slette selvvalgt påskriftsposisjon ved å trykke Del-tasten når påskriften flyttes.

![image18](images/entries/e8064c56705b7a74befa85e8a34e7b7311626f0a.gif)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch)
## Diagrammer
### Funksjonalitet: Tegneeffekter i i tegnemotoren for diagrammer
this new feature allows for diagrams to use paint effects, including drop shadows, outer glows, etc\...

![image19](images/entries/37d0a22707eca463e5aba7c0a349b2d8029fb823.gif)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: New diagram type \"stacked bars\"
With this new feature users will have possibility to create stacks bars of varying colors for each attribute on top of each other vertically or horizontally. Designed to match the \"Stacked\" chart renderer option available in ArcGIS.

![image20](images/entries/933c25cf0cd8997e177eee809b4fa26462b6d8c2.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Velge mellomrom i stolpediagrammer i vektorlag
Det er nå mulig å velge mellomrom mellom hver stolpe i diagrammet.

![image21](images/entries/7906ea6467d1d5ea19550ce1711fcc277df709a0.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Velge kakediagrammers retning
Det er nå mulig å velge om kakediagram tegnes med eller mot klokka.

![image22](images/entries/c2484d36648c335d16d1e3a45ac1a132ca2baafe.webp)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
## Opptegning
### Funksjonalitet: Avspillings- og stopp-knapper styrer avspilling av maskenettlag
It is possible to switch the timeframes of mesh layer\'s datasets by play/stop button. The playback setting could be adjusted in the time setting dialog.

![image23](images/entries/4799685965addef6ca2c788d82eea77e67e2f1f3.webp)

This feature was funded by [Lutra Consulting](http://www.lutraconsulting.co.uk)

This feature was developed by [Lutra Consulting](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Sanntids resampling av data definert på flater til hjørner (maskenettlag)
Datasett definert på flater kan interpoleres til hjørner ved å ta nabolagsgjennomsnitt. Hver piksel på en flate har en enkelt verdi/farge hvis ingen interpolering velges. Når data er definert på hjørnene kan hver piksel tegnes interpolert med verdiene fra hjørnene, og dermed blir figurene glattere.

Use mesh contours styling panel to switch between the data interpolation methods.

![image24](images/entries/c9c38ee8c59693b2971ab6269db22681a61002a1.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Støtte referansetid for maskenett
QGIS kan automatisk hente referansetid fra rådata for noen datasett-typer, slik som GRIB og NetCDF. Vi har også fikset flere feil i fortolkning av tid, slik at QGIS 3.12 kan formatere og vise riktige tider i plott/animasjoner:
- Dersom datasettgruppene har en gyldig referansetid, så brukes denne til å vise tid (absolutt tid).
- Hvis det ikke er oppgitt noen referansetid, så vises tida relativt. Man kan selv velge referansetid for å vise absolutt tid.
- Hvis det ikke er oppgitt noen referansetid, så brukes gjeldende dato + tid 00:00:00 som standard.

Det er lagt til en knapp som laster inn referansetid på nytt fra datasettgrupper ved behov.

Det er også mulig å velge en egen tidsenhet med en kombinasjonsboks, hvis tilbyders enhet er forskjellig fra timer.

![imageQ3](https://user-images.githubusercontent.com/7416892/70955568-bb939680-2047-11ea-9857-8aba122e43dd.png)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## 3D-funksjonalitet
### Funksjonalitet: Terrengopptegning av 3D-maskenett
Det er nå mulig å tegne et maskenettlag i 3D-visning som et terreng.

Man kan velge om trekanter skal glattes eller ikke, eller om kun kantlinjene skal tegnes. Man kan velge kantlinjenes tykkelse og farge, loddrett skalering, og opptegningsstil (unik farge, eller skyggelegging med fargeovergang.

Det er to måter å aktivere opptegning av maskenettlag i 3D-visningen:
- velge maskenettet som terreng i oppsettet
- aktivere 3D-visningen i lagets egenskaper

Brukeren kan stille inn følgende:
- slå av/på trekantglatting
- slå av/på kantlinjer
- velge kantlinjenes tykkelse og farge
- endre loddrett skalering
- velge opptegningsstil: unik farge eller skyggelegging med fargeovergang
- oppsett av skyggelegging med fargeovergang er tilsvarende som for rasterlag

For øyeblikket kan maskenettet tegnes ut som TIN, men tegning av datasett støttes ikke. Dette kommer ved en senere anledning.

![mesh3dsettings](https://user-images.githubusercontent.com/7416892/72482783-41d10300-37d5-11ea-9a21-8f906abcb14a.gif)

![image27](images/entries/f19c25acbd1eb462cdc0365d3af3f706c1b4d2fe.gif)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Vincent Cloarec (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Last data fra 3D-vektorlag i bakgrunn + flislegging
Data kan nå lastes inn i bakgrunnen fra vektorlag som tegnes i 3D. Tidligere kunne innlasting (og tessellering) fryse brukergrensesnittet – det kunne ta flere sekunder hvis data hadde en viss kompleksitet.

Tegnemotorene for vektorlag og regelstyrt opptegning ble konvertert til å bruke QgsChunkedEntity, som allerede er i bruk for terrengopptegning. Dette gjør mulig følgende forbedringer:
- innlastingsprosessen bruker nå flere tråder istedenfor én
- innlasting skjer flisevis, slik at man ser fliser med 3D-data komme til syne mens andre data fortsatt lastes

There is a new configuration option in the 3D tab of vector layers - it determines how deep the quadtree will be. For example, one zoom level means there will be a single tile for the whole layer. Three zoom levels means there will be 16 tiles at the leaf level (every extra zoom level multiplies that by 4, so I have limited GUI to max. 8 levels which gives \~16K tiles which is already a lot).

How a vector layer\'s tiling quadtree gets populated: all internal tree nodes are empty and thus the 3D map scene tries to immediately replace them with their children - this goes until leaf nodes are reached. Only nodes at the leaf level currently hold any data. This may change in the future when we introduce more elaborate strategies - for example, internal nodes may contain a small percentage of features of the child nodes (this would allow us to show something while zoomed out a lot, not requiring to load all data).

For debugging purposes, there is also a new configuration option \"show bounding boxes\". This allows you to see the bounding box of each tile (especially useful if there are some issues with tiles not showing up when they should).

Denne funksjonaliteten ble finansiert av QGIS.org-stipend.

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
## Utskriftslayouter
### Funksjonalitet: Dra og slipp bilder i kartlayouter
Det er nå mulig å dra f.eks. en SVG-fil fra filutforskeren til layouten for å lage et nytt bildeelement som inneholder akkurat det SVG-bildet. 

![image28](images/entries/21b9f2fba7bf1576f794410fd238ef7553154d53.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Ny layoutelement-type – manuelt opprettede faste tabeller
Det er nå mulig å opprette tabeller der innholdet skrives inn av brukere, lignende et regneark. Tabellene støtter selvvalgt celleinnhold, forgrunns- og bakgrunnsfarge (forvalgt rad- og kolonnehøyde kommer senere). Det er også en ny tabelldesigner som kan tilpasse disse tabellene.

![image29](images/entries/95cfa9a8c44fb0141474d80e4b3a5e7f98352e70.webp)

Denne funksjonaliteten ble finansiert av byen Canning.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: La brukeren velge målestokklinjalens tallformatering
Det er nå mulig å velge målestokklinjalens tallformatering.

You can manage all the formatting properties for the numbers in scale bars, including whether they want a thousand separator, decimal places, scientific notation, etc. Very useful in the case of making maps for audiences outside of the current QGIS locale, or when you\'d just prefer to vary the style from the locale defaults (e.g. adding thousands separators when the locale default is to hide them).

![image30](images/entries/99c97baaee3e5930bca0cb63db1391b6fd49b34f.gif)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Betinget valg av for- og bakgrunnsfarger til attributtabeller i utskriftslayouter
When the new \"Apply layer conditional styling colors\" option is enabled in the layout attribute table settings, any conditional styling rules present in the layer will be applied inside the layout attribute table (foreground and background colors only, for now!).

![image31](images/entries/baded0d05539439d58e6df5a8f24157293cf8022.gif)

Denne funksjonaliteten ble finansiert av byen Canning.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Layout-håndteringen har nå søkeboks
Søkeboksen gjør det mulig å filtrere listen med layouter etter navn. Dette kan komme godt med hvis prosjektet har mange layouter.

![image32](images/entries/fb510c6c079d55dab2dd22f02c7c5355b317ac47.webp)

Denne funksjonaliteten ble utviklet av Nyall Dawson.
## Uttrykk
### Funksjonalitet: Søkestikkord for funksjoner
Tags on static expression functions to make them more retrievable. Functions like array_to_string are listed when the user enters \"split\" or \"convert\" or - like before - a part of the function name.

![image33](images/entries/689a669fe84721d7574aba7e595e019a9936f0b9.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Funksjonalitet: Vis refererte lagverdier
Felt som er RelationReference, ValueRelation eller ValueMap kan ikke bare vise verdiene til gjeldende lag, men også mulige verdier i det referte laget eller konfigurerte muligheter.

![image34](images/entries/394c762c41e71764d9be397b718252eddb2dbd3e.gif)

This feature was funded by [SwissTierras-Colombia](https://www.proadmintierra.info)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Funksjonalitet: Nye uttrykk
- `is_empty(geom)`, check if a geometry is empty (geometry that contain no coordinates)
- `is_empty_or_null(geom)`, check if a geometry is empty or NULL (does not have geometry)
- `hash`, cryptographic hashes functions using [QCryptographicHash](https://doc.qt.io/qt-5/qcryptographichash.html). Use case is the same as PgCrypto but in client side for all supported format.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
### Feature: New algorithm \"Rename table field\"
Algoritmen tar et inndatalag, et eksisterende felt og dets nye navn og lager et nytt lag der det valgte feltet har fått nytt navn.

While this result could also be achieved with the Refactor Fields algorithm, Refactor Fields isn\'t particularly model friendly. It relies on a constant, fixed table structure, and can\'t adapt to input tables with different field structures.

Algoritmen «endre navn på felt» kan lettere brukes i modeller fordi den kun behandler ett felt og ikke bryr seg om de andre.

![image35](images/entries/c01edc8ee51dff2b4df8f825e0dcaf27940e4aba.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Lagrede uttrykk
- Lagre brukergitte uttrykk
- Ikon for tømming

![expression-storage-opt](https://user-images.githubusercontent.com/142164/70983414-faae0000-20b8-11ea-9f25-14b338d4c680.gif)

See also QEP <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/135>

This feature was funded by [Salvatore Fiandaca](https://pigrecoinfinito.com/2019/12/14/field-calc-di-qgis-save-expressions-crowdfunding/)

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Funksjonalitet: Vis refererte lagverdier i uttrykksbyggeren
Felt som er RelationReference, ValueRelation eller ValueMap kan ikke bare vise verdiene til gjeldende lag, men også mulige verdier i det referte laget eller konfigurerte muligheter.

*age* is a ValueMap, *species* is a ValueRelation and *island_id* is a RelationReference

![uniquevalues](https://user-images.githubusercontent.com/28384354/70978774-ab63d180-20b0-11ea-901b-d51d44fa8fa4.gif)

Dette eksempelet har følgende personer:
- *George (i Cuba, i tjueårene, er menneske), Paul (i Vietnam, i tredveårene, er menneske), Ringo (i Venezuela, i førtiårene, er katt), John (i Vietnam, i førtiårene, er tabell)*
- Oppføringene i land-laget er *USSR, Cuba, Vietnam, Burma, Venezuela, Nord-Korea*

This feature was developed by [signedav](https://api.github.com/users/signedav)
### Funksjonalitet: Nye uttrykk som konverterer til og fra WKB
- `geom_from_wkb( geom_to_wkb( make_point(4,5) ) ) → a point geometry object` Returns a geometry created from a Well-Known Binary (WKB) representation.
- `geom_to_wkb( $geometry ) → binary blob containing a geometry object` Returns the Well-Known Binary (WKB) representation of a geometry as a binary blob.

Adds geom_from_wkb and geom_to_wkb, which mirror the existing geom_from_wkt/geom_to_wkt functions but for WKB representations of geometries.

Since QGIS 3.6 we\'ve had good support for binary blob values in expressions and field values, so adding these functions allows users to work with binary blob fields containing WKB representations of geometries (e.g. with a geometry generator showing the encoded geometries)

This feature was funded by [SLYR](https://north-road.com/slyr/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: is_valid expression
`is_valid(geom_from_wkt('LINESTRING(0 0, 1 1, 2 2, 0 0)')) → true` Returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules

Add an is_valid function to the expressions, which reuses GEOS is valid and returns true if a geometry is valid; if it is well-formed in 2D according to the OGC rules.

Denne funksjonaliteten ble utviklet av Pete King.
### Feature: Add datetime_from_epoch (MSec from epoch) expression function
`datetime_from_epoch(1483225200000) → 2017-01-01T00:00:00` Returns a datetime whose date and time are the number of milliseconds, msecs, that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (Qt.UTC), and converted to Qt.LocalTime.

Denne funksjonaliteten ble utviklet av Richard Duivenvoorde.
### Funksjonalitet: Funksjonen rotate()
`rotate($geometry, 45, make_point(4, 5)) → geometry rotated 45 degrees clockwise around the (4, 5) point` Returns a rotated version of a geometry. Calculations are in the Spatial Reference System of this geometry.

Denne funksjonaliteten ble utviklet av Raymond Nijssen, Nyall Dawson.
### Funksjonalitet: Tilfeldig-tall-funksjoner kan nå ta initialiseringsverdi
- `rand(10, 80, 1) → 30` Returns a random integer within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.
- `randf(10, 80, 1) → 19.37136508087729` Returns a random float within the range specified by the minimum and maximum argument (inclusive). If a seed is provided, the returned will always be the same, depending on the seed.

This feature adds an optional seed parameter to rand() and randf() functions This is very useful if you want the result to be deterministic, for instance to assign random but fixed colors to features. Using color_hsb(rand(0,360,\$id),50,50) for instance yields always the same color for the same feature. We also improves the rand() function, which didn\'t work for high values (over 32000) by using Qt\'s QRandomGenerator instead of qrand (which it seems was deprecated in Qt 5.11).

Denne funksjonaliteten ble utviklet av olivierdalang.
### Feature: Language support for format_date() and to\_{date,datetime,time}()
- `format_date('2012-05-15','d MMMM yyyy','fr') → '15 mai 2012'`
- `format_date('2012-05-15','d MMMM yyyy','it') → '15 maggio 2012'`
- `format_date('2012-05-15','d MMMM yyyy','en') → '15 May 2012'` Formats a date type or string into a custom string format. Uses Qt date/time format strings. See QDateTime::toString.

By default, those expression use the application\'s locale. The addition of an optional language parameter allows handling of dates that wouldn\'t match that default locale (say for e.g. an English system running QGIS trying to transform a French-formatted string into a date object).

Denne funksjonaliteten ble utviklet av Mathieu Pellerin.
## Digitalisering
### Funksjonalitet: Fikse ugyldige attributter ved kopiering til et annet lag
Når objekter kopieres til et annet lag kan mållaget ha skranker (f.eks. ikke null) som ikke oppfylles automatisk av standardverdier. Nå vises et dialogvindu der man kan velge å fikse de ugyldige attributtene, eller bevisst se bort fra skrankene.

![image38](images/entries/5bd43dd39955e37ace130038b968550c6fa260c5.gif)

This feature was funded by [Amt für Wald und Wild Zug](https://www.zg.ch/behoerden/direktion-des-innern/wald-und-wild)

This feature was developed by [David Signer (OPENGIS.ch)](http://www.opengis.ch)
### Funksjonalitet: Parallellisering av hurtiglager for festing
In previous version of QGIS, the snapping index cache was built sequentially and you had to wait for all your layers to be indexed before starting edition. Thanks to the QGIS.org grant program, QGIS now builds the snapping index cache in parallel for each layer, so it speeds up the whole process. Snapping has also been relaxed, meaning that you don\'t have to wait for the cache to be complete, you can start editing and snapping information will appear as soon as they are ready.

![image39](images/entries/d77958db7175267448d9b94950532dee8b90145c.webp)

This feature was funded by [QGIS.org](https://qgis.org)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
## Datahåndtering
### Funksjonalitet: Forbedret eksportering av DXF
Eksportprosessen til DXF er nå forbedret. Den er mer robust og har ny funksjonalitet.
- Geometristiler eksporteres, og blokker tas i bruk
- Z-koordinatene til 3D-geometrier bevares
- Påskrifter eksporteres med oppsett av ankerpunkt, vannrett og loddrett justering, samt kvadrant

The whole DXF export process has also been made ready for running in a thread. With this in place, it\'s now only one step away from being sent to the background, allow cancellation of an ongoing export process or being exposed as a processing algorithm.

This feature was funded by [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
## Skjemaer og skjermelementer
### Funksjonalitet: Opprette geometriske objekter ved relasjonsredigering
We added the ability to add a new feature and digitize its geometry directly from within the relation editor widget. It\'s now easier to add a geometric feature related to your currently displayed parent feature.

![image40](images/entries/fe03aefab87464e54b70569e6d05ad09a1b8fae5.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Funksjonalitet: Forbedret dialogvindu for objektvalg
From the relation editor widget, you can link your currently displayed feature with existing features. The feature selection dialog allows you to choose these features. Thanks to the QWAT user group, feature selection is now shared with the canvas\' one so it is easy to find out and pick the feature you want to link. We have also added the ability to filter displayed features (selected ones, visible on map, matching an expression\...) reusing the same widgets already existing in attribute form.

![image41](images/entries/a65364e6a48857a8720643c41a3cb17461d9e16a.gif)

This feature was funded by [QWAT user group](http://qwat.org/about/)

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Feature: UX improvements in drag\'n\'drop form designer
The drag\'n\'drop form designer has received some nice UX improvements
- De to listene (tilgjengelige felt og layout-treet) er nå synkroniserte. Når man velger en oppføring i ei liste så vises den tilhørende oppføringen i den andre.
- Skjulte oppsettsvinduer (ved dobbeltklikking) vises nå i høyre rute

![image42](images/entries/5f47cb6311a9bffef94128a703719d709deb995a.gif)

Denne funksjonaliteten ble finansiert av feilretting via QGIS.org.

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
## Lagliste
### Funksjonalitet: Viser WMTS-grafikk i lagtreet
Lagtreet kan nå vise WMTS-grafikk, slik som man allerede kunne for WMS-grafikk.

Eksempel:

![imageQ4](https://user-images.githubusercontent.com/1298852/72462785-33351c80-37d2-11ea-98f2-ce0d5221e1f5.png)

Sample use case: <https://wmts10.geo.admin.ch/EPSG/2056/1.0.0/WMTSCapabilities.xml>

This feature was developed by [Sandro Mani](https://api.github.com/users/manisandro)
## Analyseverktøy
### Feature: Smooth Export of the Contours from Mesh Layer
A new algorithm in QGIS's analysis library API to export directly contour lines and polygons is added. The method is not based on GDAL algorithms, but directly uses mesh layer triangular mesh interpolation methods. It is both fast and with smooth shapes, matching rendered images from QGIS. You can try the new processing algorithm in Crayfish processing toolbox.

![image44](images/entries/044ad55bfb4287026b4e002c46c8687093488d22.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Maskenettkalkulatoren støtter datasett definert på flater
Maskenettkalkulatoren kan brukes på alle typer datasett, definert både på hjørner og flater. Resultatet kan lagres med selvvalgte navn og formater. Maskenettkalkulatoren kan nå jobbe med data på FLO-2D- og HEC-RAS-format.

![image45](images/entries/044d52fe937887854583ecfdc551e73eafb94a41.webp)

This feature was funded by [Austrian Ministry of Agriculture, Forestry, Environment and Water Management](https://www.bmlfuw.gv.at)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
## Prosessering
### Funksjonalitet: Legg til lag i eksisterende GeoPackage
Prosesseringsalgoritmen *pakk lag* kan nå legge til nye lag i en GeoPackage ved at brukeren slår av parameteren OVERWRITE og velger en eksisterende GeoPackage.

![image46](images/entries/35d87f4826aad132de4a0b99ac7c775f6aa9b029.webp)

This feature was funded by [BikePlan](https://www.bikeplan.ch/)

This feature was developed by [Matthias Kuhn (OPENGIS.ch)](https://www.opengis.ch)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (lineært medlemskap)
Algoritmen fuzzy-raster (lineært medlemskap) er en kompilert utgave av en fuzzy-logikk-algoritme. Den transformerer et inndataraster til et fuzzy-raster. Det vil si at den tilordner verdier mellom 0 og 1 i henhold til en medlemskapsfunksjon. Verdien 0 betyr intet medlemskap i fuzzy-mengden, mens 1 betyr fullt medlemskap. Mellom 0 og 1 følger rasterverdiene en lineær medlemskapsfunksjon.

![image47](images/entries/bfb37d710293c252dae11b67b25bdc1431f13815.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (potensmedlemskap)
Algoritmen fuzzy-raster (potensmedlemskap) er en kompilert utgave av en fuzzy-logikk-algoritme. Den transformerer et inndataraster til et fuzzy-raster. Det vil si at den tilordner verdier mellom 0 og 1 i henhold til en medlemskapsfunksjon. Verdien 0 betyr intet medlemskap i fuzzy-mengden, mens 1 betyr fullt medlemskap. Mellom 0 og 1 følger rasterverdiene en potensfunksjon.

![image48](images/entries/7a81ecd4414ee39b37e575863687615c88e9a856.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (små medlemmer)
The Fuzzify raster (small membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'small\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'small\' membership function. The \'small\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image49](images/entries/2bef948a7b02bd26208ca98e9ddb243d46d104a6.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (store medlemmer)
The Fuzzify raster (large membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'large\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'large\' membership function.The \'large\' function is constructed using two user-defined input raster values which set the point of half membership (midpoint, results to 0.5) and a predefined function spread which controls the function uptake.

![image50](images/entries/10963d11812664a76d4fc3fac72777c34a08c767.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (gaussisk medlemskap)
The Fuzzify raster (gaussian membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'gaussian\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'gaussian\' membership function. The gaussian function is constructed using two user-defined input values which set the midpoint of the gaussian function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image51](images/entries/58068dc6518a0df20a39df69ea4175f7b196b049.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Fuzzy-logikk – fuzzy-raster (nære medlemmer)
The Fuzzify raster (near membership) algorithm is a native implementation of a fuzzy logic algorithm. It transforms an input raster to a fuzzified raster and thereby assigns values between 0 and 1 following the \'near\' fuzzy membership function. The value of 0 implies no membership with the defined fuzzy set, a value of 1 depicts full membership. In between, the degree of membership of raster values follows the \'near\' membership function. The near function is constructed using two user-defined input values which set the midpoint of the near function (midpoint, results to 1) and a predefined function spread which controls the function spread.

![image52](images/entries/a4873da4c5e782a14caaa02f279ef92ba5bf5a38.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Overførte algoritmen «fortett ved antall» til C++
We ported the Densify by count algorithm to C++ in order to enhance it\'s speed when compared to the previous Python implementation. The new algorithm also exposes the count parameter as dynamic parameter so that it can be controlled by expressions or field values.

![image53](images/entries/680eb97f65d08de5541f4b1f5ac4425f45988cc2.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Overførte algoritmen «tilfeldige punkt i utstrekning» til C++
We ported the Random points in extent algorithm to C++. This boosts it\'s speed when comparing it to the previous Python implementation. The new algorithm also exposes an advanced parameter of maximum numbers of retrys for the algorithm when searching for randomly placed points that respect a certain distance between all points.

![image54](images/entries/c452431d9a2cd9f9f76869cf98e09e18bf2a81a4.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Funksjonalitet: Algoritmen «linjetetthet»
Den kompilerte algoritmen «linjetetthet» beregner rasterbasert linjetetthet ut fra en søkeradius og linjenes vektfaktor inni søkeradien. Algoritmen er mer funksjonell enn dens motpart i ArcGIS Spatial Analyst.

![image55](images/entries/b28bbe3d5129ccc5dd61585dc1a9e31383a59c6f.webp)

This feature was developed by [Clemens Raffler](https://github.com/root676)
### Feature: New algorithm \"Repair Shapefile\"
Denne nye algoritmen bruker GDAL til å reparere shapefiler som har ødelagt eller manglende .SHX-fil.

![image56](images/entries/c3a6a174187284126ea0af289614505ab8c0c593.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Add new algorithm \"Detect Dataset Changes\"
Denne algoritmen sammenligner to vektorlag og fastslår hvilke objekter som er uendret, lagt til eller slettet. Den er ment å brukes til å sammenligne to versjoner av samme datasett.

De originale og reviderte objektgeometriene sammenlignes. Man kan velge om de skal sammenlignes eksakt (samme rekkefølge og antall knekkpunkter) eller topologisk (alle kantene overlapper; det vil si at knekkpunktene har samme plassering, men linja kan ha motsatt retning). Ved topologisk sammenligning vil ikke z- eller m-verdier tas med i betraktningen.

Som standard vil algoritmen sammenligne alle attributtene i de originale og de reviderte objektene. Parameteren «attributter som skal samsvare» overstyrer dette. Man kan dermed utelate tidsstempler og ID-felt som kan endre seg mellom revisjoner.

Hvis noen objekter i det originale eller reviderte laget mangler geometri så må disse objektene ha unike attributter som kan sammenlignes. Det vil advares hvis ikke, og resultatet kan bli misvisende.

Algoritmen resulterer i tre lag, ett med uendrede objekter, ett med de objektene som er slettet i det reviderte laget, og ett med objektene i det reviderte laget som ikke er i originalen.

![image57](images/entries/e38dcea12e1198341eb9f0bd45a33ebf7eda390b.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: New mode to \"Join Attributes by Location\" to take attributes from matching feature with largest area of overlap only
This allows for easy polygon-\>polygon joins, where you expect there to be only a single matching feature and don\'t want to include features which are just touching or have just tiny sliver polygon overlaps.

![image58](images/entries/27b8e5e11deca93ffade31b86edc712ce918d179.webp)

Denne funksjonaliteten ble finansiert av SMEC/SJ.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Kompilert affin transformasjonsalgoritme for vektorer
Den har følgende fordeler over GRASS/SAGA-versjonene:
- Full støtte for z- og m-verdier, håndterer kurvede geometrier uten at kurvene går tapt
- Støtter alle QGIS' datatyper; formatkonvertering er unødvendig
- Støtter dynamiske parametre (datadefinerte, per objekt) slik som translasjon, skalering og rotasjon
- Z- og m-verdier kan transformeres og skaleres (hvis de finnes)
- Støtter direkteredigering

![image59](images/entries/1bfee3c2e208ecca6c235d96f83966ec808a0b1c.webp)

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Feature: add gdal_viewshed algorithm
Expose new gdal_viewshed tool via Processing toolbox. Note: this requires GDAL \>= 3.1.

Denne funksjonaliteten ble utviklet av Alexander Bruy.
## Utforsker
### Funksjonalitet: Tilpasse elementer i utforskeren
Add customization of the items shown in browser to the Interface Customization dialog. User can hide some of the root items in the browser panel (e.g. Favourites, PostGIS provider, MSSQL, Oracle, Volumes, \...)

![image60](images/entries/5e8e9037420b83cd44d4e1994d4119e4ae92c8aa.webp)

This feature was funded by [Limerick City and County Council](https://www.limerick.ie/council)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Vis HTML-filer i utforskerpanelet
Det er nå mulig å åpne og vise HTML-filer i utforskerpanelet. De kan brukes til å dokumentere datafiler eller kartprosjekter.

![image61](images/entries/0db8930d20ca6f2fbf5b29593afdcf59e1af8d1e.webp)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Feature: Show \"Open Document\...\" action in browser
Det er nå mulig å åpne visse filtyper med forvalgt eksternt program når man høyreklikker dem i utforskeren.

For eksempel vil PDF-filer åpnes med operativsystemets forvalgte visningsprogram.

Works with PDF, ODS, XLS(X), CSV, TXT, PNG, JPEG, TIFF, SVG (other types will likely need more work, since they aren\'t currently shown in the browser).

![image62](images/entries/447f201d2342a64912bbef1e1d0aa3ebb8963ae4.gif)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com/)
### Funksjonalitet: Tilpasse elementer i utforskeren
You can now customize items shown in the browser. User can decide (in the Interface Customization dialog) to hide some of the root items in the browser panel (e.g. Favourites, or POSTGIS provider, \...)

![Screenshot 2020-01-09 at 09 17 05](https://user-images.githubusercontent.com/804608/72050388-466f5600-32c1-11ea-94f5-092cc8471243.png)

Denne funksjonaliteten ble finansiert av Limerick City and County Council.

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Funksjonalitet: OGC-tjenester kan nå oppdateres
Man kan nå oppdatere OGC-tjenester i utforskeren. Følgende skjermbilde viser et eksempel på hvordan dette virker med WMS/WMTS-tilkoblinger:

![OGCrefreshonaction](https://user-images.githubusercontent.com/2663775/71974919-cfd04b00-3223-11ea-834d-ff016c70a8c6.gif)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
## Datatilbydere
### Funksjonalitet: Endret lagsamlingsikon for WMTS
Tidligere hadde WMTS-lagsamlinger ikon for databaseskjema. Det er nå endret til et WMS-ikon.

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funksjonalitet: La til egenskapen metadata-URL i lagets metadatafane for WMS/WMTS- og WCS-tjenester
This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funksjonalitet: Henter og viser et WMS-lags dimensjonsmetadata i egenskapsvinduet
![image65](images/entries/d058ac6b89a8d06169b06580843967ad26e1ef54.webp)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funksjonalitet: OGC-tjenester kan nå oppdateres
![image66](images/entries/7ce331ee78be7f8b0693c653ecc58916d70a1a92.gif)

This feature was funded by [Kartoza](http://kartoza.com/)

This feature was developed by [Samweli Mwakisambwe](http://samweli.github.io/)
### Funksjonalitet: 3D-stablede maskenett
MDAL og QGIS støtter nå 3D-stablede maskenett, nærmere bestemt formatet TUFLOW-FV. Man må velge en passende gjennomsnittsberegning i QGIS' brukergrensesnitt for å kunne utforske dataene slik som andre 2D-datasett.

![image67](images/entries/dc3d85153d9bcecdf7ebbc6433c7cb40319e00dd.webp)

This feature was funded by [TUFLOW](http://www.tuflow.com)

This feature was developed by [Peter Petrik (Lutra Consulting)](http://www.lutraconsulting.co.uk)
### Funksjonalitet: Fikser en rekke tegnkodingsproblemer med shapefiler
Nå er endelig håndteringen av tegnkodinger i shapefiler fikset. Dette har vært et problem i flere år.

Dette er omdiskutert på
- [#21264](https://github.com/qgis/QGIS/issues/21264)
- <http://osgeo-org.1560.x6.nabble.com/Shapefile-with-file-cpg-codepage-td5275106.html>
- <http://osgeo-org.1560.x6.nabble.com/QGIS-ignore-the-cpg-files-when-loading-shapefiles-td5348021.html>

(og flere)

The situation was that we had two different code paths for handling GDAL side attribute decoding OR QGIS side decoding. Unfortunately, they are both incompatible with each other, and due to GDAL API for this, we can\'t unify the two approaches. (More technical detail in the commit log message!)

Nå gjøres følgende:
- always do the decoding on QGIS\' side. This allows users to manually override a shapefile\'s declared encoding because they are often incorrect!
- use a port of GDAL\'s shapefile detection logic (it\'s not exposed in GDAL API, so I had to re-implement it here) so that we default to reading shapefiles by respecting the embedded encoding information (via CPG files or DBF LDID information)
- Completely remove the confusing/broken \"Ignore shapefile encoding declaration\" option, as it\'s no longer required \-- users are ALWAYS able to manually change the encoding of shapefiles layers if needed
- Always show users the detected embedded encoding in the layer properties, instead of always showing \"UTF-8\" when the embedded encoding information is used

This should give the best of both worlds \-- a nice default behavior resulting in shapefiles being read with the correct encoding, whilst still allowing users to override this on a layer-by-layer basis as needed.

This feature was developed by [Nyall Dawson](https://api.github.com/users/nyalldawson)
### Funksjonalitet: Støtte for Oracles kurvetyper
Tidligere utgivelser av QGIS støttet ikke alle geometritypene i en Oracle-database. Det er nå lagt til støtte for de følgende geometritypene:
- CircularString(Z)
- CompoundCurve(Z)
- MultiCurve(Z)
- CurvePolygon(Z)
- MultiSurface(Z)

Denne funksjonaliteten ble finansiert av Lille Metropole.

This feature was developed by [Julien Cabieces (Oslandia)](https://oslandia.com/en/)
### Funksjonalitet: WMS-tilbyderen støtter MBTiles-rastere
WMS-tilbyderen støtter nå MBTiles-fliser på samme måte som WMTS- og XYZ-fliser. Det har følgende fordeler:
- Riktig skalering av fliser på skjerm med høy DPI.
- Visuelt bedre resultat når man er zoomet ut av flisenes opprinnelige oppløsning. WMS-tilbyderen støtter skalering med glatting, mens GDAL bruker nærmeste nabo som standard.
- map tile showing up while rendering (with GDAL it\'s blank map until everything is loaded)
- Det er mulig å legge til skjermelement for skalering i samlevinduet.
- Raskere – fordi man laster færre fliser på skjerm med høy DPI.

This feature was developed by [Martin Dobias](https://api.github.com/users/wonder-sk)
### Funksjonalitet: Kompilert datatilbyder av PostGIS-raster
Datatilbyder av PostGIS-raster er nå implementert i QGIS-kjernen. Flisene hurtiglagres i RAM.

Denne funksjonaliteten ble finansiert av Christmas Holidays Inc.

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Funksjonalitet: Viser et WMS-lags dimensjonsmetadata i egenskapsvinduet
![wms-ttimelayermetadataqgis](https://user-images.githubusercontent.com/2663775/71542497-37f77500-2978-11ea-854b-d9a9ca2d6c77.png)

This feature was developed by [Samweli Mwakisambwe](https://api.github.com/users/Samweli)
### Funksjonalitet: Flere typer gjennomsnittsberegning av 3D-maskenett
QGIS now includes numerous methods for averaging mesh layers (see [related QEP](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/158), and for a description of the methods see [TUFLOW documentation](https://fvwiki.tuflow.com/index.php?title=Depth_Averaging_Results).
- SingleLevelAverageMethod (topp)
- SingleLevelAverageMethod (bunn)
- MultiLevelsFromTopAveragingMethod
- MultiLevelsFromBottomAveragingMethod
- SigmaAveragingMethod
- DepthAveragingMethod
- HeightAveragingMethod
- ElevationAveragingMethod

![Screenshot 2019-12-19 at 13 59 47](https://user-images.githubusercontent.com/804608/71175509-068bf480-2268-11ea-9d60-adad896912e2.png)

This feature was developed by [Peter Petrik](https://api.github.com/users/PeterPetrik)
### Funksjonalitet: OGC API-objekttilbyder
This new provider is a client-side implementation of the recently adopted [OGC API - Features - Part 1: Core](http://docs.opengeospatial.org/is/17-069r3/17-069r3.html) specification, previously known as WFS3. It is integrated within the graphical user interface of the WFS provider, and leverages its core mechanisms to offer background downloading of features, using paging, and a local cache of already downloaded features for a smoother interactive use of datasets.

![image70](images/entries/d74a13f520336e0c2e44469ee4e527188e2466de.webp)

This feature was funded by [Planet](https://planet.com)

This feature was developed by [Even Rouault (Spatialys)](https://www.spatialys.com)
## QGIS Server
### Funksjonalitet: Program for QGIS Utviklingstjener
**QGIS HTTP-tjener for utvikling**

Dette er et lite, frittstående, kommandolinjeprogram som implementerer en minimal HTTP-utviklingstjener for QGIS Server.

Den er nyttig ved utvikling og testing av QGIS Server-prosjekter, moduler og programtillegg fordi man slipper å installere en full webtjener med FCGI.

![qgismapserver](https://user-images.githubusercontent.com/142164/73081781-84c36280-3ec8-11ea-9285-ab4c41e3082c.gif)
``` bash
Usage: qgis\_mapserver [options] [address:port]
QGIS Development Server

Options:
-h, --help Displays this help.
-v, --version Displays version information.
-l Sets log level (default: 0)
0: INFO
1: WARNING
2: CRITICAL
-p Path to a QGIS project file (*.qgs or* .qgz),
if specified it will override the query string MAP argument
and the QGIS\_PROJECT\_FILE environment variable

Arguments:
addressAndPort Listen to address and port (default: "localhost:8000")
address and port can also be specified with the environment
variables QGIS\_SERVER\_ADDRESS and QGIS\_SERVER\_PORT
```
Eksempel på utdata:

`bash QGIS Development Server listening on http://localhost:8000 CTRL+C to exit 127.0.0.1 [lun gen 20 15:16:41 2020] 5140 103ms "GET /wfs3/?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 3298 2ms "GET /wfs3/static/jsonFormatter.min.js HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1678 3ms "GET /wfs3/static/jsonFormatter.min.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:41 2020] 1310 5ms "GET /wfs3/static/style.css HTTP/1.1" 200 127.0.0.1 [lun gen 20 15:16:43 2020] 4285 13ms "GET /wfs3/collections?MAP=/home/ale/dev/QGIS/tests/testdata/qgis_server/test_project.qgs HTTP/1.1" 200`

This feature was developed by [Alessandro Pasotti](https://api.github.com/users/elpaso)
### Feature: Add DXF server export params NO_MTEXT and FORCE_2D
QGIS server now supports the new parameters `NO_MTEXT` and `FORCE_2D` to control text and line symbology for generated DXF files. Adds missing parameters to GetDxf request

This feature was developed by [Matthias Kuhn](https://api.github.com/users/m-kuhn)
### Funksjonalitet: WMS GetLegendGraphic støtter nå JSON
This feature adds support for GetLegendGraphic responses encoded as JSON. It builds on previous work by \@pblottiere, who added QgsLegendRenderer::exportLegendToJson for that exact purpose.

For eksempel vil en GetLegendGraphic-forespørsel med FORMAT=image/png som danner bildet

![image72](https://user-images.githubusercontent.com/76594/64876231-fbb13a80-d64e-11e9-83e5-120fb1bc0ea8.png)

danne følgende hvis FORMAT=application/json

Miniatyrbildet er kodet i base64 og kan vises direkte i en nettside.

Denne funksjonaliteten ble utviklet av Éric Lemoine.
## Programmering
### Funksjonalitet: Tilgjengeliggjøre digitaliseringsmetoder i QgisInterface
The actions to trigger the drawing tools were not exposed in the API, if you wanted to do an action for one of these tools, you had to recreate classes. So a call of the type `qgis.utils.iface.actionCircleCenterPoint().trigger()` simplifies programmability.

Denne funksjonaliteten ble finansiert av QWAT/QGEP-gruppen.

This feature was developed by [Loïc Bartoletti (Oslandia)](https://www.oslandia.com)
## Viktige feilrettinger
### Funksjonalitet: Stephen Knox' feilrettinger
| Bug Title | URL issues (if reported) | URL PR or commit |----|----|----|----| | Allow editing of postgres JSON fields from Text Edit Widget | [#29361](https://github.com/qgis/QGIS/issues/29361) | [#30758](https://github.com/qgis/QGIS/pull/30758)

Denne funksjonaliteten ble utviklet av Stephen Knox.
### Funksjonalitet: Alessandro Pasottis feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| \"Recent\" Group do not appear when opening the \"Select by expression\" dialog | [#33791](https://github.com/qgis/QGIS/issues/33791) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) |
| QGIS Server finner ikke shp; forsøker å åpne absolutt istedenfor relativ sti | [#33200](https://github.com/qgis/QGIS/issues/33200) | [PR #33925](https://github.com/qgis/QGIS/pull/33925) | risikabel |
| ikke rapportert: feil lenke i tjeners WFS3-side (for mange skråstreker) | ikke rapportert | [PR #33926](https://github.com/qgis/QGIS/pull/33926) | risikabel |
| QGIS gjennomsøker rastertabeller ved tilkobling til PostGIS | [#33885](https://github.com/qgis/QGIS/issues/33885) | [PR #33922](https://github.com/qgis/QGIS/pull/33922) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Informasjonsfane i lagegenskaper – formateringsproblemer | [#33862](https://github.com/qgis/QGIS/issues/33862) | [PR #33955](https://github.com/qgis/QGIS/pull/33955) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Can\'t set min/max values to decimal in raster symbology with QGis Linux versions | [#33859](https://github.com/qgis/QGIS/issues/33859) | virker i gjeldende master |  |
| QgsVectorLayer readStyle leser ikke «tegn opp innenfor målestokksintervall» | [#33840](https://github.com/qgis/QGIS/issues/33840) | [PR #33987](https://github.com/qgis/QGIS/pull/33987) | [PR #34289](https://github.com/qgis/QGIS/pull/34289) |
| Kategorisert symbolisering virker ikke med bigint-kolonner i QGIS | [#33585](https://github.com/qgis/QGIS/issues/33585) | [PR #33992](https://github.com/qgis/QGIS/pull/33992) | [PR #34290](https://github.com/qgis/QGIS/pull/34290) |
| QGIS bruker ikke stilfil på rastere | [#29427](https://github.com/qgis/QGIS/issues/29427) | endring kreves ikke, men etterforskning pågår |  |
| kopier / lim inn objekt virker ikke for MultilinestringZ | [#33977](https://github.com/qgis/QGIS/issues/33977) | virker i gjeldende master |  |
| Skjemaredigering viser og lagrer råe standardverdier fra geopackage, spatialite og sqlite | [#33383](https://github.com/qgis/QGIS/issues/33383) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| Det er ikke mulig å fravelge lag i lagrekkefølge-panelet | [#33854](https://github.com/qgis/QGIS/issues/33854) | [PR #34015](https://github.com/qgis/QGIS/pull/34015) | [PR #34288](https://github.com/qgis/QGIS/pull/34288) |
| Identitetskolonnen til PostgreSQL gjenkjennes ikke | [#29560](https://github.com/qgis/QGIS/issues/29560) | [PR #34017](https://github.com/qgis/QGIS/pull/34017) | [PR #34291](https://github.com/qgis/QGIS/pull/34291) |
| Spatialite-tilbyder gjenkjenner ikke automatisk økende primærnøkler når tabelldefinisjonen bruker gravis «`» | [#34085](https://github.com/qgis/QGIS/issues/34085) | [PR #34012](https://github.com/qgis/QGIS/pull/34012) | [PR #34298](https://github.com/qgis/QGIS/pull/34298) |
| QGIS crash when I click on the button \"Manage Map Themes\" | [#33295](https://github.com/qgis/QGIS/issues/33295) | [PR #34090](https://github.com/qgis/QGIS/pull/34090) | [PR #34098](https://github.com/qgis/QGIS/pull/34098) |
| QGIS Server - WMS Request GetPrint fails with ATLAS_PK | [#30817](https://github.com/qgis/QGIS/issues/30817) | virker i gjeldende master |  |
| QGIS 3.10.2 erstatter 0 med NULL | [#34118](https://github.com/qgis/QGIS/issues/34118) | [PR #34152](https://github.com/qgis/QGIS/pull/34152) | [PR #34292](https://github.com/qgis/QGIS/pull/34292) |
| Inkonsistent bruk og visning av representasjonen av NULL-verdier | [#28643](https://github.com/qgis/QGIS/issues/28643) | [PR #34157](https://github.com/qgis/QGIS/pull/34157) | [PR #34293](https://github.com/qgis/QGIS/pull/34293) |
| DB Manager in 3.11 Master can\'t connect to PostGIS Enabled database | [#34132](https://github.com/qgis/QGIS/issues/34132) | [PR #34171](https://github.com/qgis/QGIS/pull/34171) | N/A |
| QGIS doesn\'t respect OGC guidelines for KVP parameters | [#34148](https://github.com/qgis/QGIS/issues/34148) | [PR #34175](https://github.com/qgis/QGIS/pull/34175) | [PR #34294](https://github.com/qgis/QGIS/pull/34294) |
| QGIS 3.10 can\'t find pkey of postgres views | [#34167](https://github.com/qgis/QGIS/issues/34167) | [PR #34179](https://github.com/qgis/QGIS/pull/34179) | [PR #34295](https://github.com/qgis/QGIS/pull/34295) |
| Duplisering av kladdelag ignorerer felt som er lagt til | [#34134](https://github.com/qgis/QGIS/issues/34134) | [PR #34199](https://github.com/qgis/QGIS/pull/34199) | [PR #34203](https://github.com/qgis/QGIS/pull/34203) |
| Prosjekt-XML til QGIS Master er ugyldig | [#34218](https://github.com/qgis/QGIS/issues/34218) | [PR #34219](https://github.com/qgis/QGIS/pull/34219) | [PR #34297](https://github.com/qgis/QGIS/pull/34297) |
| Betinget formatering av hele rader formaterer feil rader | [#34122](https://github.com/qgis/QGIS/issues/34122) | [PR #34305](https://github.com/qgis/QGIS/pull/34305) | [PR #34315](https://github.com/qgis/QGIS/pull/34315) |
| Feil ved evaluering av filteruttrykk returnerer sann | [#34259](https://github.com/qgis/QGIS/issues/34259) | [PR #34309](https://github.com/qgis/QGIS/pull/34309) | [PR #34512](https://github.com/qgis/QGIS/pull/34512) |
| Felt forskyver seg når man importerer et lag med FID-attributt til GeoPackage | [#32927](https://github.com/qgis/QGIS/issues/32927) | [PR #32934](https://github.com/qgis/QGIS/pull/32934) | N/A |
| \"split features\" of PostGIS layers become slow since 3.6 | [#34326](https://github.com/qgis/QGIS/issues/34326) | Lukket: Kan ikke reprodusere dette med noen av de leverte datasettene |  |
| Kan ikke legge til/lagre mer enn 1 oppføring/objekt i et Spatialite-lag/tabell | [#34379](https://github.com/qgis/QGIS/issues/34379) | [PR #34423](https://github.com/qgis/QGIS/pull/34423) | [PR #34513](https://github.com/qgis/QGIS/pull/34513) |
| QGIS crashes when changing \"default value\" in layer property on a point scratch layer, after editing feature | [#34404](https://github.com/qgis/QGIS/issues/34404) | [PR #34428](https://github.com/qgis/QGIS/pull/34428) | [PR #34514](https://github.com/qgis/QGIS/pull/34514) |
| Rasterkalkulatoren endrer en pikselrad til nodata | [#34435](https://github.com/qgis/QGIS/issues/34435) | [PR #34460](https://github.com/qgis/QGIS/pull/34460) | [PR #34511](https://github.com/qgis/QGIS/pull/34511) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Alessandro Pasotti](https://www.itopen.it/)
### Funksjonalitet: Sandro Santillis feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| repository files modified by \'make check\' | [#25830](https://github.com/qgis/QGIS/issues/25830) |  |  |
| Runs of testsuite leaves hundreds of directories in \~/.local/share | [#34185](https://github.com/qgis/QGIS/issues/34185) | [Commit 96a7fb8](https://github.com/qgis/QGIS/commit/96a7fb8f5acf3a278919f88c7c5abc4d20b8b6c2) | N/A |
| Ikke bruk QgsCoordinateReferenceSystems foreldede konstruktør  | [PR #34186](https://github.com/qgis/QGIS/pull/34186) | [Commit b4fa419](https://github.com/qgis/QGIS/commit/b4fa419f7654ea7d1bce666b99f0534c415d8634) | N/A |
| Se kun etter pointcloud i dens installerte extension-skjema | [#33509](https://github.com/qgis/QGIS/issues/33509) | [Commit 1f44b29](https://github.com/qgis/QGIS/commit/1f44b29933bff3b8806bba75b761dd47b6c349c8) | N/A |
| QGIS 3.10 på MacOS Catalina kan ikke laste inn PostGIS-tabell | [#32558](https://github.com/qgis/QGIS/issues/32558) | [Commit d15ce6b](https://github.com/qgis/QGIS/commit/d15ce6b4c30f9faed8b818c575d6b729192fa064) | [Commit a06b164](https://github.com/qgis/QGIS/commit/a06b164b5465ee7a0f8509e737d7c71ea7c166db) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Denne funksjonaliteten ble utviklet av Sandro Santilli.
### Funksjonalitet: Even Rouaults feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Krasj ved bruk av feil filter på OAFeat-lag | [#33878](https://github.com/qgis/QGIS/issues/33878) | [PR #33927](https://github.com/qgis/QGIS/pull/33927) | [PR #33958](https://github.com/qgis/QGIS/pull/33958) |
| Oracle-tilbyder: Fikse kompilatoradvarsler | - | [PR #33930](https://github.com/qgis/QGIS/pull/33930) | - |
| Kan ikke importere 3D-vektorer til Spatialite-datakilde (virker med GPKG) | [#33883](https://github.com/qgis/QGIS/issues/33883) | [PR #33938](https://github.com/qgis/QGIS/pull/33938) | [PR #33945](https://github.com/qgis/QGIS/pull/33945) |
| \[Oracle\] Fix MultiSurface with straight polygon | - | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | ikke mulig |
| Geometries stored in Oracle table fail sdo_geom.validate_geometry_with_context(..) check | [#29085](https://github.com/qgis/QGIS/issues/29085) | [PR #33959](https://github.com/qgis/QGIS/pull/33959) | ikke mulig |
| QGIS WFS / OGC API -- Features not showing list typed attributes correctly | [#33758](https://github.com/qgis/QGIS/issues/33758) | [PR #33983](https://github.com/qgis/QGIS/pull/33983) | N/A |
| Tegnforklaring fører til krasj | [#32913](https://github.com/qgis/QGIS/issues/32913) | [PR #34004](https://github.com/qgis/QGIS/pull/34004) | [PR #34063](https://github.com/qgis/QGIS/pull/34063) |
| Draw effects units setting doesn\'t persist | [#34089](https://github.com/qgis/QGIS/issues/34089) | [PR #34135](https://github.com/qgis/QGIS/pull/34135) | [PR #34151](https://github.com/qgis/QGIS/pull/34151) |
| Dårlig georeferering av OZI .map | [#34299](https://github.com/qgis/QGIS/issues/34299) | [GDAL commit](https://github.com/OSGeo/gdal/commit/7bedf61bbb8d8c331642b44f30c083abb43f4085) | - |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Even Rouault](http://www.spatialys.com/)
### Funksjonalitet: Alexander Bruys feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Fjerne ordgyterske verktøyknapper | [#30161](https://github.com/qgis/QGIS/issues/30161) | [PR #33912](https://github.com/qgis/QGIS/pull/33912) |  |
| Kan ikke lime inn lag i tomt prosjekt | [#26710](https://github.com/qgis/QGIS/issues/26710) | [PR #33961](https://github.com/qgis/QGIS/pull/33961) | [PR #33965](https://github.com/qgis/QGIS/pull/33965) |
| DB-håndtering: Dialogvinduet for oppretting av lag må lukkes eller tømmes etter at det nye laget er opprettet | [#25535](https://github.com/qgis/QGIS/issues/25535) | [PR #33910](https://github.com/qgis/QGIS/pull/33910) |  |
| Det er to ulike hurtigtaster for lagstilpanelet (F7 og Ctrl + 3) | [#26696](https://github.com/qgis/QGIS/issues/26696) | [PR #33984](https://github.com/qgis/QGIS/pull/33984) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

Denne funksjonaliteten ble utviklet av Alexander Bruy.
### Funksjonalitet:Paul Blottieres feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Fixes compilation on Arch Linux | Ikke rapportert | [PR #34110](https://github.com/qgis/QGIS/pull/34110) | [PR #34146](https://github.com/qgis/QGIS/pull/34146) |

| Move labels doesn\'t work with GPKG QGIS 3.4 | [#30408](https://github.com/qgis/QGIS/issues/30408) | Closed (works on master and 3.10) | - |

| Auxiliary storage not usable in non editable layer | [#30376](https://github.com/qgis/QGIS/issues/30376) | Feedback (works on master and 3.10) | - |

| Labels Buffer DD options do not have fields set and do not render in map canvas | [#28544](https://github.com/qgis/QGIS/issues/28544) | [PR #34153](https://github.com/qgis/QGIS/pull/34153) | risky |

| QGIS does not load embedded layers when opening projects | [#34060](https://github.com/qgis/QGIS/issues/34060) | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Embedded layers are duplicated after opening | Unreported | [PR #34311](https://github.com/qgis/QGIS/pull/34311) | [PR #34706](https://github.com/qgis/QGIS/pull/34706) |

| Raise log level of server exception | [Discussed on qgis-developers list](https://lists.osgeo.org/pipermail/qgis-developer/2020-February/060108.html) | [PR #34256](https://github.com/qgis/QGIS/pull/34256) | [PR #34539](https://github.com/qgis/QGIS/pull/34539) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Paul Blottiere](https://hytech-imaging.fr/)
### Funksjonalitet: Denis Rouzauds feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Krasj ved bruk av relasjoner | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34255](https://github.com/qgis/QGIS/pull/34255) | - |
| Krasj ved bruk av relasjoner V2 | [#33120](https://github.com/qgis/QGIS/issues/33120) | [PR #34403](https://github.com/qgis/QGIS/pull/34403) | ferdig |
| Fikse uttegning av kartlagshandlinger i attributtabellen | Ikke rapportert | [PR #34266](https://github.com/qgis/QGIS/pull/34266) | ferdig |
| Dra-og-slipp-forbedringer (synkr. utvalg) | [#28570](https://github.com/qgis/QGIS/issues/28570) | [PR #34411](https://github.com/qgis/QGIS/pull/34411) | TODO? |
| Dra-og-slipp-forbedringer (beholderoppsett) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34433](https://github.com/qgis/QGIS/pull/34433) |  |
| Dra-og-slipp-forbedringer (ikke skjul bak dobbelklikk) | [#29063](https://github.com/qgis/QGIS/issues/29063) | [PR #34479](https://github.com/qgis/QGIS/pull/34479) |  |
| Slå av automatisk panorering/skalering når attributtabellen viser kun synlige objekter | [#34486](https://github.com/qgis/QGIS/issues/34486) | [PR #34493](https://github.com/qgis/QGIS/pull/34493) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Denis Rouzaud](https://www.opengis.ch/)
### Funksjonalitet: Julien Cabieces' feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Feste- og knekkpunktverktøy virker ikke med noen lag hvis festing var aktivert ved innlasting | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Festing virker ikke i nye prosjekt med nytt lag | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplikat | - |
| Hurtiglageret til knekkpunktverktøyet oppdaterte seg ikke etter endring av linjeobjekter | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Lukket (fikset i 3.10 og master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | TODO |
| Utdata fra setFilterExpression og QGIS-filter er forskjellige | [#33454](https://github.com/qgis/QGIS/issues/33454) | Lukket (feilen er ikke i QGIS) | - |
| Krasj ved bruk av Oracle-visninger der primærnøkkel er definert som presisjonsløst tall | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | TODO |
| WCS-klient stoppet å virke med en spesifikk tjeneste fra 2.18 til 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | TODO |
| Krasj i test av relasjonsreferanser | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Julien Cabieces](https://www.oslandia.com/)
### Funksjonalitet: Bertrand Rix' feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Feste- og knekkpunktverktøy virker ikke med noen lag hvis festing var aktivert ved innlasting | [#33449](https://github.com/qgis/QGIS/issues/33449) | [PR #33757](https://github.com/qgis/QGIS/pull/33757) | N/A |
| Festing virker ikke i nye prosjekt med nytt lag | [#32969](https://github.com/qgis/QGIS/issues/32969) | Duplikat | - |
| Hurtiglageret til knekkpunktverktøyet oppdaterte seg ikke etter endring av linjeobjekter | [#33947](https://github.com/qgis/QGIS/issues/33947) | Won\'t fix | - |
| \"fill ring\" do not trigger the correct computation of the area in the \"default value\" expression | [#32377](https://github.com/qgis/QGIS/issues/32377) | Lukket (fikset i 3.10 og master) | - |
| \"view feature form\" opens the wrong feature/record | [#33880](https://github.com/qgis/QGIS/issues/33880) | [PR #34009](https://github.com/qgis/QGIS/pull/34009) | TODO |
| Utdata fra setFilterExpression og QGIS-filter er forskjellige | [#33454](https://github.com/qgis/QGIS/issues/33454) | Lukket (feilen er ikke i QGIS) | - |
| Krasj ved bruk av Oracle-visninger der primærnøkkel er definert som presisjonsløst tall | [#31626](https://github.com/qgis/QGIS/issues/31626) | [PR #34312](https://github.com/qgis/QGIS/pull/34312) | TODO |
| WCS-klient stoppet å virke med en spesifikk tjeneste fra 2.18 til 3.x | [#33339](https://github.com/qgis/QGIS/issues/33339) | [PR #34300](https://github.com/qgis/QGIS/pull/34300) | TODO |
| Krasj i test av relasjonsreferanser | [#34779](https://github.com/qgis/QGIS/issues/34779) | [PR #34822](https://github.com/qgis/QGIS/pull/34822) | TODO |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Bertrand Rix](https://www.oslandia.com/)
### Funksjonalitet: Loïc Bartolettis feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Lukk knekkpunkt i linje under redigering | [#32359](https://github.com/qgis/QGIS/issues/32359) | [PR #34217](https://github.com/qgis/QGIS/pull/34217) | [PR #34285](https://github.com/qgis/QGIS/pull/34285) |
| Fikse Grass-lenking på FreeBSD | rapportert på e-postlista til FreeBSD | [PR #34088](https://github.com/qgis/QGIS/pull/34088) | [PR #34238](https://github.com/qgis/QGIS/pull/34238) |
| \[Regular Shape\] Allow undo click when digitizing new features | [#25597](https://github.com/qgis/QGIS/issues/25597) | [PR #34080](https://github.com/qgis/QGIS/pull/34080) | [PR #34302](https://github.com/qgis/QGIS/pull/34302) |
| Fjern nytt knekkpunkt ved bruk av «Legg til bue» | [#29688](https://github.com/qgis/QGIS/issues/29688) | [PR #34058](https://github.com/qgis/QGIS/pull/34058) | [PR #34301](https://github.com/qgis/QGIS/pull/34301) |
| Rubberband not working correctly with \"Shapes\" digtizing in rotated map window | [#33287](https://github.com/qgis/QGIS/issues/33287) | Duplikat |  |
| Digitalisering: LineStringZ henter ikke z-koordinater fra punkter hvis linjen startes ved å snappe til et punkt uten z-koordinat | [#33201](https://github.com/qgis/QGIS/issues/33201) | [PR #33642](https://github.com/qgis/QGIS/pull/33642) | [PR #33951](https://github.com/qgis/QGIS/pull/33951) |
| Splitt objekt krasjer QGIS 3.4.6 | [#33408](https://github.com/qgis/QGIS/issues/33408) | Allerede fikset |  |
| Fikse algoritmen til rotert minste omsluttende rektangel | [#33532](https://github.com/qgis/QGIS/issues/33532) | [PR #34334](https://github.com/qgis/QGIS/pull/34334) | [PR #34338](https://github.com/qgis/QGIS/pull/34338) |
| orientedMinimumBoundingBox() returnerer feil vinkel | [#31371](https://github.com/qgis/QGIS/issues/31371) | Lukket pga manglende tilbakemelding |  |
| Fix build with txt2tags \>= 3.5 | FreeBSDs QGIS-ansvarlig rapporterte direkte | [PR #34377](https://github.com/qgis/QGIS/pull/34377) | [PR #34389](https://github.com/qgis/QGIS/pull/34389) |
| Fikse identifiseringsmenyen når et uttrykk brukes som visningsnavn | ikke rapportert | [PR #34361](https://github.com/qgis/QGIS/pull/34361) | [PR #34402](https://github.com/qgis/QGIS/pull/34402) |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Loïc Bartoletti](https://www.oslandia.com/)
### Funksjonalitet: Sebastien Peillets feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Fortsett linje virker ikke i compoundCurvedZ-lag | [#32080](https://github.com/qgis/QGIS/issues/32080) | [PR #34055](https://github.com/qgis/QGIS/pull/34055) |  |
| Designfeil ved valg av objektattributt | [#29542](https://github.com/qgis/QGIS/issues/29542) | [PR #34359](https://github.com/qgis/QGIS/pull/34359) |  |
| Kan ikke legge til nytt objekt når to PostGIS-tabeller sammenføyes | [#33148](https://github.com/qgis/QGIS/issues/33148) | [PR #34216](https://github.com/qgis/QGIS/pull/34216) |  |
| Man kan ikke kopiere/lime inn mellom lag når laget har skranken «ikke null» og transaksjonsgrupper er aktivert | [#29603](https://github.com/qgis/QGIS/issues/29603) | Already fixed by [PR #33688](https://github.com/qgis/QGIS/pull/33688) |  |
| QGIS fryser ved oppretting av nye shapefiler | [#32069](https://github.com/qgis/QGIS/issues/32069) | Allerede fikset |  |
| Oracle: Tabeller listes én gang for Polygon og én gang for MultiPolygon, men begge viser alle geometrier | [#32521](https://github.com/qgis/QGIS/issues/32521) | [PR #34358](https://github.com/qgis/QGIS/pull/34358) |  |
| FEIL: Fikse ugyldige lagresultater når Oracle-versjonen er under 12 | ikke rapportert | [PR #34546](https://github.com/qgis/QGIS/pull/34546) |  |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Sebastien Peillet](https://www.oslandia.com/)
### Funksjonalitet: Nyall Dawsons feilrettinger
| Feil | URL til feilrapport (hvis rapportert) | URL til innsjekk (Github) | Tilbakeføring til 3.10 (Github) |
| --- | --- | --- | --- |
| Fikse evaluering av IN/NOT IN med veldig lange tall-lignende tekststrenger | [#34314](https://github.com/qgis/QGIS/issues/34314) | [Commit 167e0de](https://github.com/qgis/QGIS/commit/167e0de65b0106a3c19181a2c415c2b0ba0da117) | [Commit aca059a](https://github.com/qgis/QGIS/commit/aca059a82021cb05b58664d3b0f2db751b8f37df) |
| \[processing\] Define Layer Projection tool should write .prj files using ESRI WKT1 format | [#34007](https://github.com/qgis/QGIS/issues/34007) | [Commit f41dd11e](https://github.com/qgis/QGIS/commit/f41dd11e9214b4d6ca5dcc31c6612a65d134ce83) | Meldt inn |
| Show \'unknown CRS\' in status bar instead of blank text when project is set to an unknown CRS | [#33458](https://github.com/qgis/QGIS/issues/33458) | [Commit c6319b2](https://github.com/qgis/QGIS/commit/c6319b263992c9d52646096d851cab6c674125ff) | Meldt inn |
| Don\'t force users to make a choice in the datum transform dialog | [#34234](https://github.com/qgis/QGIS/issues/34234) | [Commit 644a552](https://github.com/qgis/QGIS/commit/644a5525ec08a77b4c703a7066c94802bbfa1036) | Meldt inn |
| Fikse krasj ved endring av rasterdatakilde | [#34231](https://github.com/qgis/QGIS/issues/34231) | [Commit caf334e6](https://github.com/qgis/QGIS/commit/caf334e65b11f9ee1590f74fe395e97d92bbe699) | [Commit b4142c3](https://github.com/qgis/QGIS/commit/b4142c3832b9f14de97df08caf20a06dee12c02f) |
| Handle unit type \"m\" in custom WKT strings on proj 6 builds | [#34196](https://github.com/qgis/QGIS/issues/34196) | [Commit bb20cee](https://github.com/qgis/QGIS/commit/bb20cee00a931da46b830f0d1e9565d9863f9ba3) | [Commit 97c50f9](https://github.com/qgis/QGIS/commit/97c50f929fbbdd9b3eaef8f8bdf423f9daa3a163) |
| Vise full KRS-WKT for selvvalgte KRS i lagegenskaper | [#33862](https://github.com/qgis/QGIS/issues/33862) | [Commit 19d58bda](https://github.com/qgis/QGIS/commit/19d58bda08c202b29020a3e9c485fac80350fc79) | [Commit 2908227](https://github.com/qgis/QGIS/commit/2908227f91ccfde245a0a608b50b7758b3eba8dd) |
| \[processing\] Fix modeler draws lines to wrong output when connecting green output boxes | Ikke rapportert | [Commit 5ae9807](https://github.com/qgis/QGIS/commit/5ae9807303e909a504288d97a2efc4cc04a62670) | [Commit 528a45d](https://github.com/qgis/QGIS/commit/528a45d7453b7cbeb44450d5c81de80c8dd66611) |
| \[processing\] Fix Points Along Geometry handling of multipart geometries | [#34022](https://github.com/qgis/QGIS/issues/34022) | [Commit 3fb18a2](https://github.com/qgis/QGIS/commit/3fb18a2260cbc432e892a4dacbae0092a775ec9d) | [Commit ac3b446](https://github.com/qgis/QGIS/commit/ac3b446aead90d5ea5cab101807859e5ce6f1b44) |
| \[processing\] Fix QStringList values are not accepted as valid values for multi-field parameters | Ikke rapportert | [Commit abcb8d2](https://github.com/qgis/QGIS/commit/abcb8d20c66b3c235802b10e68d6abc34736e2c5) | [Commit d421313](https://github.com/qgis/QGIS/commit/d421313f05fd0e5a6974568eccd36c4213f41f8f) |
| \[processing\] Fix some field names are rejected in modeler for non-multi field parameters | Ikke rapportert | [Commit 9bcd980](https://github.com/qgis/QGIS/commit/9bcd98094c015265e7e94c55f248248e56c24e51) | Ikke aktuelt, kun 3.12 |
| Fikse krasj i objektinformasjon fra tjener | Ikke rapportert | [Commit b3f37fde](https://github.com/qgis/QGIS/commit/b3f37fde9bc4785aebca29e6553d6c1de715f523) | Meldt inn |
| Fikse overflyt ved tilordning av double maks til float, ugyldig min | Ikke rapportert | [Commit 2b15e255](https://github.com/qgis/QGIS/commit/2b15e255eaf63f1d45b8e963fca7f9f9e4bf8d40) | Ikke aktuelt, kun 3.12 |
| Fikse krasj i QgsGeometryDuplicateCheck pga bruk av haug etter ressursfrigjøring | Ikke rapportert | [Commit 195576e](https://github.com/qgis/QGIS/commit/195576e57f0aff064e962ce16b37533ab4924dce) | [Commit dc647bc](https://github.com/qgis/QGIS/commit/dc647bc56fb37207a75d55638926e7a2db75a8be) |
| Fikse krasj ved destruksjon av QgsPointLocator, dersom objekt destrueres mens indeksering pågår i bakgrunnen | Ikke rapportert | [Commit 08adb23](https://github.com/qgis/QGIS/commit/08adb23a7ec284a2f84ecf7ac469fbe9004ab57e) | Ikke aktuelt, kun 3.12 |
| Fikse krasj ved lesing av visse resamplede rasterfiler | [#33711](https://github.com/qgis/QGIS/issues/33711) | [Commit b2c5a45](https://github.com/qgis/QGIS/commit/b2c5a456fa4e9613ac33b8aaaed774ad3b7293a1) | [Commit 388277e](https://github.com/qgis/QGIS/commit/388277e642d99b93bd7f25197d6418b5dfb888bd) |
| Fikse bruk etter ressursfrigjøring i 3D-punktsymbol | Ikke rapportert | [Commit df7979c](https://github.com/qgis/QGIS/commit/df7979cf94c43352cd10db97c16075b8816ec6c4) | [Commit 7204de2](https://github.com/qgis/QGIS/commit/7204de27f3305146fbd6f8e32355c365030afc31) |
| Fikse lekkasjer i geometrigenerert symbollag | Ikke rapportert | [Commit 1610fb8](https://github.com/qgis/QGIS/commit/1610fb8766a13351bb303ee3bfd6301dbdc6648b) | [Commit 3944db4](https://github.com/qgis/QGIS/commit/3944db47dda6b08ea4b22f61c5e72d97597362b1) |
| Fikse krasj ved uttegning i proj 6-bygg | [#33902](https://github.com/qgis/QGIS/issues/33902) | [Commit 8a71091](https://github.com/qgis/QGIS/commit/8a7109163a9362af2a5e0187cf2b57fc0219fe59) | [Commit f41076d](https://github.com/qgis/QGIS/commit/f41076d45f5f259c50e3ead2cac4d664be11bbfb) |
| Don\'t try to label empty geometries | [#33931](https://github.com/qgis/QGIS/issues/33931) | [Commit 1144974](https://github.com/qgis/QGIS/commit/11449743788f3fd346c01c46cff01bcf3f84edf0) | Ikke aktuelt, kun 3.12 |
| Fikse krasj ved eksportering av KRS-konverterte rasterlag | [#33801](https://github.com/qgis/QGIS/issues/33801) | [Commit bbd055c](https://github.com/qgis/QGIS/commit/bbd055ca13a3d6ee150251222d73e3b9e76d94c5) | [Commit 2fff8e1](https://github.com/qgis/QGIS/commit/2fff8e1205daffafa257b9312cc2c005b5e3017e) |
| Fikse tegnkodingsproblemer med shapefiler | [#21264](https://github.com/qgis/QGIS/issues/21264) | Meldt inn | Avventer 3.10.4 |

This feature was funded by [QGIS.ORG (through donations and sustaining memberships)](https://www.qgis.org/)

This feature was developed by [Nyall Dawson](https://north-road.com/)

{{<content-end >}}
