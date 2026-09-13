---
draft: 'true'

---
# Použití QGIS v grafickém týmu Financial Times
## Rozhovor se Stevenem Bernardem (redaktorem interaktivního designu)
Steven is an Interactive Design Editor at Financial Times. You can find him on [Twitter](https://twitter.com/sdbernard). He also publishes useful [HOWTO Videos on Youtube](https://t.co/6aTE6G8h0T) for certain cartographic tasks in QGIS.

**QGIS**: Stevene, jak se jmenuje tým, ve kterém pracujete na FT? Můžete nám poskytnout trochu informací o tom, čím se váš tým na FT zabývá?

**Steve**: (dříve pracoval pro ONS), který se snaží změnit situaci a vytvořit jednotný grafický tým. Tradičně jsme měli tým webové grafiky a tým tiskové grafiky. Tým pro tisk měl na starosti veškerou grafiku novin a také vytváření jejich webových verzí. Můj tým byl zodpovědný za veškerý obsah určený pouze pro web a také úzce spolupracoval s interaktivními producenty/vývojáři při navrhování interaktivní grafiky.

Nově vytvořený tým umožní mnohem větší propojení dovedností mezi jednotlivými médii.

Alan zavedl jednotný digitální pracovní postup pro náš tým, včetně použití d3, který pomáhá vytvářet větší grafický slovník a zkracuje čas potřebný k vytvoření vizuálů.

![](./images/ft_europe_migration_balkan-route.png){.align-left width="100.0%"}

*Příklad: Příklad: toky migrantů. Západobalkánská trasa.*

**QGIS**: Kolik je ve vašem týmu spolupracovníků?

**Steven**: Včetně všech designérů, vývojářů, producentů a statistiků máme tým 24 lidí.

**QGIS**: What\'s your specific role within the team?

**Steven**: We are a multi-disciplinary department so I don't have a specific role as such. My role includes producing responsive designs for interactive graphics as well as doing the front-end development on the less complicated interactives (e.g. [Inside Isis Inc: The journey of a barrel of oil](http://ig.ft.com/sites/2015/isis-oil/)). I also produce the standard news related charts and maps on a daily basis. Over the past two years I have been concentrating on developing our cartographic offerings at the FT. QGIS has been instrumental in changing how we produce maps, and in conjunction with other tools such Blender have helped me to be more creative with how we approach maps.

![](./images/ft_nigeria-migration_animation.gif){.align-left width="100.0%"}

*Example: Animation of Dora\'s journey from Nigeria to Sicily - one of thousands by trafficked women each year.*

**QGIS**: Can you tell us a bit about yourself? What\'s your educational background? What did you do before joining the data visualization team at FT?

![](./images/ft_gotthard-tunnel.png){.align-left width="60.0%"}

*Příklad: Gotthardský železniční a silniční tunel ve švýcarských Alpách.*

**Steven**: I am traditionally trained as scientific illustrator. What's that I hear you ask? It involves producing illustrations for medical journals, natural history publications anything where you are trying to convey information visually where a photograph can't. Think of diagrams showing the human circulatory system, or showing a procedure to fix a broken bone. Sadly there wasn't much call for that kind of work when I left university and I basically fell into the job at the FT. I have always been good at maths, which I think is important when working with data visualisations, it has certainly helped me with my coding as well.

**QGIS**: Jak jste objevil QGIS?

**Steven**: I came across QGIS in 2013 when we were working on a [project mapping the ethnicity of the Middle East](http://ig.ft.com/features/2013-07-19_middleeast_religion_map/dist/index.html)

We used it to georeference maps that were created by a professor at Columbia University. At first I found it really tricky using the add feature drawing tool, probably because it was unlike anything I'd used in Adobe Illustrator for 17 years prior! I also found it frustrating that you had to save things twice, once when done editing the shapefile, then again to save the project. However, this was just down to inexperience with the program and in the end it did exactly what we needed, which was to produce shapefiles that we could add to a Mapbox base map.

**QGIS**: What\'s the role of QGIS within your usual workflows?

**Steven**: QGIS is now an integral part of our mapping workflow. I don't use any other GIS tool to create our maps. Although a few members of our team also use Map Publisher as they feel more comfortable staying within Adobe Illustrator. I would say 80% of our maps are now produced in QGIS.

![](./images/ft_blm-federal-land-map.png){.align-left width="100.0%"}

*Příklad: Veřejná území v USA.*

**QGIS**: Jaké další nástroje kromě QGIS používáte a jak je kombinujete?

**Steven**: Pokud se jedná pouze o jednoduchou lokalizační mapu, 95 % práce se provádí v QGIS a konečné doladění v Adobe Illustratoru.

Pokud dělám reliéfní mapu, je proces mnohem složitější. Získám soubory DEM z Nasa Earth Explorer a přenesu je do QGIS, kde je oříznu na požadovanou velikost. Oříznutý DEM pak přenesu do programu Blender a vytvořím 3D render. Pokud budu používat překrytí kopců družicemi, stáhnu si z Nasa snímek BlueMarble a ten také přenesu do Blenderu. Exportovaný render z Blenderu pak přenesu zpět do QGIS a použiji ho jako vrstvu pozadí. V případě potřeby jej mohu předem upravit ve Photoshopu.

For responsive maps like those in the [Isis oil story](http://ig.ft.com/sites/2015/isis-oil/), I used all of the above tools but the final step is to use an open source Adobe Illustrator script developed by the New York Times' Archie Tse. This allows me to create responsive versions of my maps that work on all devices.

Dalším užitečným nástrojem je Google My Maps, který umožňuje reportérům z celého světa označit místa na mapě a poté je můžeme stáhnout jako soubor kmz a importovat přímo do QGIS.

Posledním nástrojem, který používám, je Adobe After Effects, protože jsem se nedávno pustil do animace svých map, abych uživatele vzal na cestu. Jak bylo nedávno použito v sérii Land Rush:
- [Land Rush Ethiopia](https://ig.ft.com/sites/land-rush-investment/ethiopia/)
- [Land Rush Myanmar](https://ig.ft.com/sites/land-rush-investment/myanmar/)
- [Land Rush Indonesia](https://ig.ft.com/sites/land-rush-investment/indonesia/)

**QGIS**: Používáte kromě QGIS i jiné prostorové nástroje nebo GIS, a pokud ano, jaké?

**Steven**: QGIS je pro mě naprostou jedničkou, ale jak bylo uvedeno výše, někteří z mých kolegů používají také Map Publisher.

![](./images/ft_isis-air-strikes_febupdate.png){.align-left width="100.0%"}

*Příklad: Údery na Sýrii v únoru 2016.*

**QGIS**: Můžete popsat silné a slabé stránky QGIS v souvislosti s úkoly, které musíte řešit?

**Steven**: When I first used QGIS I saw it as a specialist tool, fit for only dealing with specific tasks. I really didn't see it a production tool. In late 2014 two of my colleagues went on a QGIS course held by Alasdair Rae at Sheffield University. They both enthused about how good QGIS was, so I took it upon myself to evaluate it as a tool that could be used to produce all our maps.

Asi za dva týdny jsem byl přesvědčen, že to bude životaschopné. Hlavním prodejním argumentem byla možnost nastavit průvodce styly pro všechno, včetně stylování na úrovni přiblížení pro mapy na úrovni ulic.

Mám nastavený systém, ve kterém máme sady listů Google se sloupci pro název, zeměpisnou šířku, délku, ikonu značky, váhu písma, velikost písma a zda chcete značku vidět, nebo ne.

Ikona značky je rozevírací okno připojené k tabulce vLookUp, která vyplní všechny podrobnosti o dané značce.

Takže stačí stáhnout csv, importovat ho do QGIS, použít styl a mám mapu, která je z 95 % připravená k použití.

To be perfectly honest I can't think of any weaknesses, there are a couple of things that I would like to see or be able to do but, I don't see that as a weakness, just a missing feature.

![](./images/ft_chinaMigration.png){.align-left width="100.0%"}

*Příklad: Přitažlivost měst a migrace v Číně.*

**QGIS**: Jaké koncepty nebo funkce se vám v QGIS líbí nejvíce?

**Steven**: Existuje mnoho funkcí, které bych označil za zachránce života! Ale především Quick OSM a Georeferencer mi ušetřily tolik času, že je to naprosto nezbytné, když jsou termíny napjaté. Což je při práci pro zpravodajskou organizaci obvykle 90 % času.

![](./images/ft_china_henanGuangdong.png){.align-left width="100.0%"}

*Příklad: Přitažlivost měst a migrace v Číně. Detailní pohledy.*

**QGIS**: Jaké vlastnosti nebo funkce v QGIS postrádáte nejvíce? Máte seznam chybějících funkcí, jejichž implementace by vám velmi pomohla?

**Steven**: A couple of things I would like to see in future versions are\...

Bezier curve support, this would be particularly useful in conjunction with Georeferencer. I know there is a spline plugin but it doesn't give you the full control a bezier curve would.

Možnost ukládat jako obrázek ve větších velikostech. V současné době je to jediný způsob, jak mohu vytvořit georeferencovaný výřez souboru DEM a přenést jej do programu Blender. Je to však omezeno velikostí obrazovky. Pokud bych měl soubor DEM o velikosti 8 000 pixelů načtený do QGIS, chtěl bych mít možnost exportovat výřez ve větší velikosti, než je velikost obrazovky, například pro použití v HD videu.

**QGIS**: Pokud vám v QGIS chybí určité funkce, které by vám pomohly - uvažovali byste o tom, že byste QGIS vylepšili sami (kódováním v jádře QGIS nebo pluginy v Pythonu), nebo byste zvážili najmout vývojáře QGIS, který by chybějící funkci implementoval za vás? Nebo byste se raději poohlédli po jiných nástrojích, které by tuto mezeru zaplnily?

**Steven**: I certainly don't have the necessary skills to do the coding myself, I'm fairly proficient in Javascript but would struggle with Python. I would love to hire a developer to get features implemented but unfortunately I'm not in control of any budgets, so I use other tools to get around this.

![](./images/ft_us_broadband_internet_subscription.png){.align-left width="100.0%"}

*Příklad: Procento domácností s předplaceným širokopásmovým internetem v USA*.

**QGIS**: Let\'s talk about user experience - the QGIS team is aware that there are various places in the UI (dialogs, panels, etc) that could be improved a lot. Can you tell us a little bit where in the UI you see the biggest potential for a UI overhaul?

**Steven**: I think the main tools are fine as they are, once you are familiar with them they're pretty obvious. However, one thing I do find a little frustrating is trying to hunt down a plugin once it's been installed. They either create their own menu (MMQGIS), live under one of the menus (Georeferencer) or create their own icon (threejs). It would be handy to have a plugin window that has all installed plugins in it. Again this isn't a deal breaker but would make it easier than hunting in several different locations.

**QGIS**: Děkujeme vám za váš čas a práci, kterou odvádíte pro propagaci a dokumentaci pracovních postupů v QGIS!

![](./images/ft_potrait_steve_bernard.jpg){.align-left width="50.0%"}

*Portrét Steva Bernarda. Redaktor interaktivního designu ve Financial Times.*

**Steven**: A pleasure, I'm almost evangelical about QGIS! Hence the [31 video tutorials](https://t.co/6aTE6G8h0T) and always happy to spread the word.

Otázky k rozhovoru: A. Neumann a T. Sutton. Duben 2016.
