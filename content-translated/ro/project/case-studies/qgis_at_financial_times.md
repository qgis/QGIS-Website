---
HasBanner: false
archived: false
date: 2016-04-01
draft: false
featured: true
section: proiect
sidebar: true
thumbnail: images/ft_europe_migration_balkan-route.png
title: Folosirea QGIS în cadrul echipei de grafică de la Financial Times
type: case-study

---
{{<content-start >}}
# Folosirea QGIS în cadrul echipei de grafică de la Financial Times
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2016</span>
</p>

## Interviu cu Steven Bernard (Editor de Design Interactiv)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Steven, care este numele echipei în care lucrezi la FT? Ne poți oferi unele informații generale despre ceea ce face echipa ta în cadrul FT?

**Steve**: Echipa noastră trece printr-o perioadă de tranziție în acest moment, având un nou editor de vizualizare a datelor, Alan Smith OBE (anterior a lucrat la Oficiul Național de Statistică), care a efectuat modificări majore, creând o singură echipă de grafică. În mod tradițional exista o echipă de grafică web și alta pentru grafica de imprimare. Echipa de imprimare era responsabilă pentru toată grafica din ziar precum și pentru crearea de versiuni adecvate pentru web. Echipa mea era responsabilă doar pentru conținutul web, colaborând îndeaproape cu producătorii/dezvoltatorii specializați în proiectarea graficii interactive.

Echipa nou formată beneficiază de o distribuție mult mai extinsă a competențelor între diferitele medii.

Alan a introdus un singur flux de lucru digital pentru echipa noastră, folosind și d3 pentru a ajuta la crearea unui vocabular grafic mai larg și la reducerea timpului necesar creării efectelor vizuale.

![](../images/ft_europe_migration_balkan-route.png)

*Exemplu: Fluxurile de migranți. Ruta Balcanilor de Vest.*

**QGIS**: Cât de mulți colegi ai în echipă?

**Steven**: Cu tot cu designeri, dezvoltatori, producători și statisticieni sunt 24 în echipă

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](../images/ft_nigeria-migration_animation.gif)

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](../images/ft_gotthard-tunnel.png)

*Exemplu: Traseul feroviar Gotthard și un tunel rutier din Alpii elvețieni.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Cum ai aflat de QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](../images/ft_blm-federal-land-map.png)

*Exemplu: Terenuri publice din US.*

**QGIS**: Ce alte instrumente folosiți în afară de QGIS și cum se combină acestea?

**Steven**: În cazul în care este vorba doar de o hartă simplă de localizare, 95% din muncă se face în QGIS, șlefuirea finală efectuându-se în Adobe Illustrator.

În cazul în care lucrez la o hartă în relief, atunci procesul este mult mai complex. După ce obțin fișierele DEM de la NASA Earth Explorer, le aduc în QGIS pentru a le decupa la dimensiunea dorită. DEM-ul decupat îl deschid în Blender unde îi aplic o randare 3D. Dacă trebuie să suprapun o imagine luată din satelit, atunci descarc o imagine BlueMarble de la NASA, pe care o urc, totodată, în Blender. Randarea exportată o aduc înapoi în QGIS, pentru a o utiliza ca fundal. Dacă este cazul, în prealabil, mai efectuez unele modificări în Photoshop.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Un alt instrument util este Google My Maps, care permite reporterilor din întreaga lume să marcheze diverse locații de pe hartă, pe care să le putem descărca sub formă de fișier KMZ, pentru a le putea importa direct în QGIS.

Instrumentul final pe care îl folosesc este Adobe After Effects, care introduce animație în hărților mele. Recent, am folosit această tehnică pentru seria Goana după Pământ:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Utilizezi și alte instrumente spațiale în afară de QGIS, și dacă da, care anume?

**Steven**: QGIS îmi este suficient, dar, așa cum s-a menționat mai sus, unii dintre colegii mei folosesc în plus Map Publisher.

![](../images/ft_isis-air-strikes_febupdate.png)

*Exemplu: Luptele din Siria din Februarie 2016.*

**QGIS**: Poți descrie punctele forte și slăbiciunile QGIS, observate în lucrul de zi cu zi?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

După aproximativ două săptămâni am fost convins că această soluție era viabilă. Principalul argument l-a constituit capacitatea de stilizare omniprezentă, inclusiv pentru hărțile care prezintă străzi la diferite niveluri de măririe.

Am un sistem special creat pentru cazul în care dispun de seturi de foi Google cu coloane pentru nume, latitudine, longitudine, simbolul marcajului, dimensiunile fontului și dacă se dorește ca marcajul să fie vizibil sau nu.

Simbolul marcajului se obține dintr-o casetă cu derulare verticală, conectată la un tabel vLookUp, și care completează automat toate detaliile.

Tot ce am de făcut este să descarc csv-ul, să-l import în QGIS, să-i aplic un stil și, astfel, obțin o hartă care este gata în proporție de 95%.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](../images/ft_chinaMigration.png)

*Exemplu: Atracția urbană și migrația în cadrul Chinei.*

**QGIS**: Care sunt conceptele sau funcțiunile care iți plac cel mai mult la QGIS?

**Steven**: Există numeroase funcții pe care le-aș considera cu adevărat vitale! În primul rând, cu ajutorul plugin-ului QuickOSM și a Georeferențiatorului am economisit o mulțime de timp, acest lucru fiind absolut esențial atunci când termenele sunt strânse. Ceea ce, atunci când lucrezi pentru o organizație de știri, se întâmplă pentru 90% din timp.

![](../images/ft_china_henanGuangdong.png)

*Exemplu: Atracția Urbană și Migrația în cadrul Chinei. Vedere detaliată.*

**QGIS**: Ce caracteristici sau funcționalități ai dori să existe în QGIS? Poți enumera o serie de caracteristici care te-ar ajuta foarte mult dacă ar fi implementate?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Capacitatea de a salva capturi de dimensiuni mai mari. În prezent, acesta este singurul mod în care pot efectua o captură dintr-un DEM georeferențiat, pentru a o încărca în Blender. Din păcate limita este dată de dimensiunea ecranului. De aceea, presupunând că aș avea un fișier DEM de 8.000 de pixeli încărcat în QGIS, aș dori să existe posibilitatea de export a unei dimensiuni mai mari decât ecranul, pentru a o utiliza într-un video HD, de exemplu.

**QGIS**: Dacă prezența unor anumite funcțiuni în QGIS ți-ar fi de folos - ai putea lua în considerare îmbunătățirea QGIS, efectuând tu însuți codificarea (direct în QGIS sau printr-un plugin Python) sau anagajând un dezvoltator QGIS pentru a implementa funcțiunea care îți lipsește? Sau, în schimb, ai căuta un alt instrument pentru a depăși acest impediment?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](../images/ft_us_broadband_internet_subscription.png)

*Exemplu: Procentul gospodăriilor din SUA care dețin un abonament la internetul de bandă largă.*

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Îți mulțumim pentru timpul și munca depuse pentru promovarea și documentarea fluxurilor de lucru în QGIS!

![](../images/ft_potrait_steve_bernard.jpg)

*Imagine cu Steven Bernard. Editor de Design Interactiv la Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Întrebările din acest interviu au fost concepute de A. Neumann și T. Sutton. Aprilie 2016.

{{<content-end >}}
