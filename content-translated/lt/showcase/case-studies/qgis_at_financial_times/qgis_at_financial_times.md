---
draft: 'true'

---
# QGIS naudojimas Financial Times Grafikos komandoje
## Pokalbis su Steven Bernard (Interaktyvaus Dizaino Redaktorius)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Stevenai, kaip vadinasi komanda, kurioje jūs dirbate FT? Ar galite mums šiek tiek papasakoti apie tai, ką jūsų komanda daro FT?

**Stevenas**: Mūsų komanda šiuo metu yra transformacijos periode, mes turime naują duomenų vizualizavimo redaktorių, Alan Smith OBE (anksčiau ONS), kuris judina dalykus ir kuria vieną grafikos komandą. Tradiciškai mes turėjome žiniatinklio grafikos komandą ir spausdinamos grafikos komandą. Spausdinimo komanda atsakinga už visas laikraščių grafikas bei žiniatinkliui pritaikytų jų versijų kūrimą. Mano komanda buvo atsakinga už visą tik žiniatinklio turinį bei artimai dirbo su interaktyviais kūrėjais/vystytojais kuriant interaktyvius grafinius produktus.

Naujai suformuota komanda leis daug daugiau bendrų įgūdžių tarp skirtingų medijų.

Alanas pristatė mūsų komandai vieną skaitmeninį procesą, įskaitant d3 naudojimą kuriant platesnį grafikos žodyną bei sumažinant vaizdo medžios kūrimui reikalingą laiką.

![](./images/ft_europe_migration_balkan-route.png){.align-left width="100.0%"}

*Pavyzdys: Migrantų srautai. Vakarų Balkanų maršrutas.*

**QGIS**: Kiek bendradarbių yra jūsų komandoje?

**Stevenas**: Įskaitant visus dizainerius, programuotojus, prodiuserius ir statistus, mūsų komandoje yra 24 žmonės

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](./images/ft_nigeria-migration_animation.gif){.align-left width="100.0%"}

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](./images/ft_gotthard-tunnel.png){.align-left width="60.0%"}

*Pavyzdys: Gotardo traukinys ir kelio tunelis Šveicarijos Alpėse.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Kaip jūs atradote QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](./images/ft_blm-federal-land-map.png){.align-left width="100.0%"}

*Pavyzdys: Viešos žemės JAV.*

**QGIS**: Kokius kitus įrankius be QGIS jūs naudojate ir kaip juos kombinuojate?

**Stevenas**: Jei tai tiesiog orientacinis žemėlapis, 95% darbo atliekama su QGIS, paskutinį grąžinimą darant su Adobe Illustrator.

Jei darau reljefo žemėlapį, tada procesas yra daug sudėtingesnis. Aš ištraukiu DEM failus iš Nasa Earth Explorer ir įkeliu juos į QGIS, kad apkarpyčiau pagal reikiamą dydį. Tada apkarpytas DEM įkeliamas į Blender, 3D vaizdo sukūrimui. Jei naudoju palydovinį perdengimą ant šešėliavimo, tada atsisiunčiu BlueMarble nuotrauką iš Nasa ir ją taipogi įkeliu į Blender. Iš Blender eksportuotas vaizdas vėl įkeliamas į QGIS kaip foninis sluoksnis. Jei reikia, rezultatą dar patikslinu su Photoshop.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Kitas naudingas įrankis yra Google My Maps, kuris leidžia viso pasaulio žurnalistams pažymėti žemėlapyje vietas ir tada atsisiųsti jas kaip kmz failą, kurį galima importuoti tiesiai į QGIS.

Paskutinis mano naudojamas įrankis yra Adobe After Effects, kadangi paskutiniu metu pradėjau animuoti žemėlapius, kad išleisčiau naudotoją į kelionę. Kaip buvo neseniai panaudota Land Rush serijoje:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Ar be QGIS naudojate kokius nors kitus GIS įrankius, jei taip - kokius?

**Stevenas**: Man QGIS viskam, bet, kaip minėta aukščiau, mano kolegos naudoja dar ir Map Publisher.

![](./images/ft_isis-air-strikes_febupdate.png){.align-left width="100.0%"}

*Pavyzdys: 2016 vasario smūgiai Sirijai.*

**QGIS**: Ar galite aprašyti QGIS stipriąsias ir silpnąsias puses, kalbant apie jūsų atliekamas užduotis?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

Per maždaug dvi savaites aš supratau, kad tai bus įmanoma. Pagrindinis pardavimo privalumas buvo galimybė sukurti stiliaus gidus viskam, įskaitant ir mastelių stilius gatvių lygio žemėlapiams.

Aš turiu pasiruošęs sistemą, kurioje mes  turime Google skaičiuokles su stulpeliais pavadinimui, ilgumai, platumai, žymeklio piktogramai, šrifto storiui, šrifto dydžiui ir ar norime, kad žymeklis būtų matomas.

Žymeklio piktograma yra iškrentantis sąrašas, prijungtas prie vLookUp lentelės, kuri užpildo visas to žymeklio detales.

Taigi viskas, ką turiu padaryti, yra atsisiųsti csv, importuoti jį į QGIS, pritaikyti stilių ir aš turiu žemėlapį, kuris yra 95% paruoštas.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](./images/ft_chinaMigration.png){.align-left width="100.0%"}

*Pavyzdys: Miestų trauka ir migracija Kinijos viduje.*

**QGIS**: Kokias QGIS koncepcijas ar savybes jūs mėgstate labiausiai?

**Stevenas**: Yra kelios savybės, kurias aš klasifikuočiau kaip gyvenimo gelbėtojas! Bet visų pirma Quick OSM ir Geopririšimas mane išgelbėjo daug kartų, tai absoliučiai gyvybiškai reikalinga, kai spaudžia terminai. Kas, dirbant naujienų organizacijoje, paprastai būna 90% laiko.

![](./images/ft_china_henanGuangdong.png){.align-left width="100.0%"}

*Pavyzdys: Miestų trauka ir migracija Kinijos viduje. Detalūs vaizdai.*

**QGIS**: Kokių QGIS savybių ar funkcionalumo jūs labiausiai pasigendate? Ar turite sąrašą trūkstamų savybių, kurios jums labai padėtų, jei būtų įgyvendintos?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Galimybė įrašyti kaip piešinį didesnius failus. Dabar tai yra vienintelis būdas, leidžiantis man sukurti geopririštą DEM failo dalį, kurią noriu įkelti Blenderį. Bet jis apribotas jūsų ekrano dydžiu. Jei turiu 8,000 taškų DEM failą, įkeltą į QGIS, aš norėčiau galėti eksportuoti jo dalį didesniu dydžiu nei mano ekranas, kad rezultatą būtų galima naudoti pavyzdžiui HD video.

**QGIS**: Jei jums trūksta QGIS savybių, kurios jums padėtų - ar svarstytumėte galimybę pagerinti QGIS patiems (rašant QGIS kodą arba Python priedus), ar svarstytumėte galimybę pasamdyti QGIS programuotoją, kad įgyvendintų jums trūkstamą savybę? Ar geriau ieškotumėte kito įrankio, kuris galėtų suteikti trūkstamą funkcionalumą?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](./images/ft_us_broadband_internet_subscription.png){.align-left width="100.0%"}

*Pavyzdys: Procentas namų ūkių su plačiajuosčiu internetu JAV.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Ačiū už jūsų laiką ir darbą, kurį atliekate reklamuodami ir dokumentuodami QGIS procesus!

![](./images/ft_potrait_steve_bernard.jpg){.align-left width="50.0%"}

*Steve Bernard portretas. Financial Times interaktyvaus dizaino redaktorius.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Pokalbio klausimus uždavė A. Neumann ir T. Sutton. 2016 balandis.
