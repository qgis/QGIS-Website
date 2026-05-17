---
draft: 'true'

---
# QGIS aan het Federal Department of Town and Country Planning, Peninsular Malaysia
## Introductie
Het Federal Department of Town and Country Planning, Peninsular Malaysia (JPBD) is een federaal agentschap dat adviseert over zaken met betrekking tot de planning van steden en landschappen. Het doel van de administratie voor het departement is echter beperkt tot het schiereiland van Maleisië omdat Sabah en Sarawak in Oost-Maleisië hhun eigen respectievelijke agentschappen voor planning van steden en landschappen hebben. Planning van steden en landschappen staat op de huidige lijst in de federale wetgeving, dus, op federaal niveau, JPBD adviseert de Housing and Local Government Minister onder wiens gezag de JPBD staat en adviseert ook de National Physical Planning Council, die wordt voorgezeten door de Premier. Op het niveau van de staat adviseert de state director de State Planning Committee, voorgezeten door de Chief Minister. Op lokaal niveau adviseert JPBD lokale planning-autoriteiten over zaken met betrekking tot planning door betrokken te zijn bij de voorbereiding van voorgeschreven plannen voor ontwikkeling. Op het hoofdkwartier bereidt de National Physical Plan Division het National Physical Plan voor terwijl vier regionale projectkantoren assisteren bij de voorbereiding van State Structure Plans, District Local Plans en Special Area Plans. Omdat publieke agentschappen traditioneel werden ingesteld op basis van hun specialisatie, is JPBD de beheerder van informatie over landgebruik.
## Het project
QGIS werd als eerste geïntroduceerd aan de Maleisische Open Source-gemeenschap als een waardig alternatief voor merkgebonden GIS voor publieke agentschappen door JPBD op de Maleisische Government Open Source Conference (MyGOSSCON) in 2009 en aan de Maleisische GIS-gemeenschap aan de 4e National GIS Conference and Exhibition (NGIS) in 2010. JPBD was van oudsher ene gebruiker van merkgebonden GIS dus de introductie van QGIS was een echte eye opener, biet alleen vanuit het oogpunt van Open Source Software (OSS), maar ook OSS GIS. Open source filosofie was anders dus QGIS voelde buitenaards, onzeker en onveilig, niet verrassend dus dar het idee om QGIS te gebruiken intern op niet veel steun kon rekenen, in feite werd weerstand ondervonden in 2010 vanaf het management aan de top tot onder in de ondersteuningsgroep.

![MyGOSSCON, 2009](./images/malaysia_kuala1.png){.align-right}

Aan de andere kant kwamen verzoeken voor technische verhalen over QGIS van andere technische agentschappen, die JPBD gaf aan het Ministry of Works en het Department of Irrigation and Drainage. Ander werk om QGIS te promoten vanuit JPBD kwam in de vorm van artikelen in een nieuwsbrief over QGIS aan het Open Source Competency Centre (OSCC) van het departement van de premier en artikelen die QGIS introduceerden in het Survey Department\'s GIS Bulletin en het Ministry of Natural Resource\'s Public Sector GeoSpatial Bulletin. In de tussenliggende tijd onderzocht JPBD het ontwikkelen van een hellingsanalysemodel voor QGIS\'s versies van Windows en Ubuntu.

De studie accentueerde de voors en tegens van het aanpassen van een module en het benodigde hoge niveau van betrokkenheid van het management om het voortgaande succes en adoptie te verzekeren. In 2011 begon JPBD met verder onderzoek naar QGIS meer als een analytisch gereedschap in plaats van een kaartgereedschap om te pionieren in nog niet uitgewerkte modules of nieuwe benaderingen bij het exploiteren van QGIS.

Het departement promootte uiteindelijk het pakket QGIS-GRASS in plaats van alleen QGIS omdat dat het meest krachtige en nuttige werd bevonden voor doeleinden met betrekking tot planning van steden, zoals het opschonen van fouten in topologie en het overwinnen van de beperkingen van standaard invoer. Dat was slechts het begin.

![Northern Project Office get QGIS training](./images/malaysia_kuala2.png){.align-right}

Om bevindingen te centraliseren en te delen met betrekking tot het gebruiken van QGIS voor doeleinden van stedelijke planning die ook op andere gebieden, die werken met ruimtelijke analyses, zouden kunnen worden gebruikt, werd een niet officieel blog opgestart door de auteur, genaamd "QGIS MALAYSIA" op <http://www.qgismalaysia.blogspot.com> om een QGIS-gemeenschap in Maleisië op te bouwen. Externe agentschappen leken meer interesse te hebben in QGIS dan JPBD zelf en op hun verzoek gaf JPBD QGIS-training aan het Fire and Safety Department en ook het Ministry of Education dat later was overtuigd dat QGIS hun de facto gereedschap voor GIS zal zijn.

JPBD\'s Research and Development Division, dat hiervan hoorde, nam het initiatief en verzocht om QGIS-training en aansluitend werden 12 personen getraind. Mond-tot-mondreclame (een door God gegeven ding, hoewel soms extreem nadelig) gaf door dat QGIS inderdaad gebruikersvriendelijk, eenvoudig te gebruiken en te vergelijken was met merkgebonden GIS bij taken voor het in kaart brengen en een waardig tegenstander was voor merkgebonden GIS indien geoptimaliseerd met modules van GRASS.

Interesse in QGIS steeg en in 2012, met ondersteuning van alle directeuren van de projectkantoren, werd een alles of niets poging ondernomen bij de National Landuse Information Division dat het voortouw nam voor QGIS om de 4 projectkantoren te trainen omdat zij het grootste aantal GIS-gebruikers huisvesten. Aan het eind van 2012, wordt verwacht, dat ten minste 320 stafleden, over geheel JPBD, QGIS zullen gebruiken wat geldt vals ongeveer 90% van de GIS-gebruikers in het gehele departement.

Dat is niet alles. Departementen van stedelijke planning voor de staat hebben ook training in QGIS verzocht, zoals Perak inclusief sterke interesse uit armere staten zoals Perlis en Kelantan. Als dit aanslaat, wordt verwacht dat het gebruiken van QGIS de staatsdepartementen voor planning zal domineren en zelfs zal worden uitgebreid tot lokale planningsautoriteiten, waarvan vele niet rijk zijn. In de tussenliggende tijd studeert JPBD serieus op het gebruiken van het pakket QGIS-PosgreSQL-PostGIS voor elk planningskantoor cliënt-GIS-geodatabase-serverstructuur om te dienen als de fundering voor JPBD\'s geïntegreerde netwerk voor landgebruik (iPLAN).
## Uitkomsten van het gebruiken van QGIS
- Uitgaande van RM10,000 per merkgebonden licentie voor GIS, zal het gebruiken van 320 QGIS installaties de federale overheid een bedrag besparen van RM3,200,000;
- Een totaal uitbanning van illegale GIS en het vergroten van het vertrouwen in het gebruiken van OSS in het algemeen en specifiek OSS GIS;
- QGIS-training was eenvoudiger te beheren. Dit betekent kruisend leren tussen staf, divisies, publieke agentschappen en zelfs lokale planningsautoriteiten die QGIS gebruiken kan meer effectief zijn omdat het GIS uniform wordt gebruikt;
- Het gebruiken van QGIS helpt bij het zoeken naar de synergie met een geodatabase van PostgreSQL-PostGIS die het departement van plan is te gaan gebruiken als fundering voor geodatabase voor landgebruik op het gehele schiereiland van Maleisië.
- Het was sneller om gegevens te verifiëren en fouten in topologie op te schonen.
- Gebruikers worden moediger en duiken in Google Maps en andere internetbronnen voor aanvullende informatie;
- Omdat QGIS zo gebruikersvriendelijk is moedigt het gebruikers aan avontuurlijker te worden en de vele beschikbare plug-ins in hun voordeel te verkennen en hun taak eenvoudiger te maken.
- GIS: een complex gereedschap wordt meer ene vriend dan een hindernis.

## Auteur
![Abbas Abdul Wahab](./images/malaysia_kualaaut.jpg){.align-left height="200px"}

Dit artikel werd bijgedragen in januari 2012 door Abbas Abdul Wahab. Abbas, afgestudeerd als stadsplanner aan het Gloucestershire College of Arts & Design, United Kingdom in 1980 en heeft een Masters of Science in GIS & Geomatic Engineering van de Putra University Malaysia in 2002. Hij is momenteel Head of the National Landuse Information Unit aan de National Landuse Information Division van het Federal Department of Town & Country Planning, Peninsular Malaysia.
