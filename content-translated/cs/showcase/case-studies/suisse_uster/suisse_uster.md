---
draft: 'true'

---
# Využití QGIS v geodatové infrastruktuře města Usteru
Město Uster používá QGIS od roku 2007. Povzbuzeno rozhodnutím kantonu Solothurn používat QGIS jako náhradu desktopového GIS za ArcView, rozhodlo se jej vyzkoušet i město Uster. Město se připojilo k úsilí o další rozvoj aplikace QGIS tím, že navrhovalo a testovalo nové funkce a finančně podporovalo vývoj. Na oplátku získala společnost Uster rychle se vyvíjející a platformově nezávislé řešení Desktop GIS a WebGIS, za kterým stojí celosvětová komunita uživatelů a vývojářů.

![](./images/suisse_uster1.png){.align-right}

Postgis/PostgreSQL se používá jako centrální úložiště geodat. Ostatní databáze a zdroje dat jsou do PostgreSQL replikovány v pravidelných intervalech pomocí nástrojů, jako jsou OGR a FME. Zpočátku se QGIS používal hlavně jako prohlížeč. Prvním uživatelem QGIS byl zemědělec, který měl za úkol dohlížet na deklarace podávané místními zemědělci pro získání zemědělských dotací. Později byl QGIS zaveden také jako editor dat a platforma pro publikování map spolu s vylepšením editačních nástrojů a tiskového kompozitoru. Společně s dalšími švýcarskými uživateli QGIS (Solothurn, Thun a CDE (univerzita v Bernu)) koordinujeme a sponzorujeme vylepšení těchto nástrojů spolu s některými vylepšeními v oblasti symbolizace řízené daty, automatického označování, práce s atributy a formuláři.

![](./images/suisse_uster2.png){.align-right}

Městská správa používá také komerční software GIS: Autodesk Topobase pro snímání a editaci dat katastrální a odpadové infrastruktury a GE Smallworld pro správu plynových, vodovodních a elektrických sítí. Jedná se však o expertní systémy, které používají speciálně vyškolení pracovníci. Všechny ostatní projekty GIS a prohlížení všech dat zajišťuje QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

V současné době se QGIS používá pro následující projekty GIS:
- prohlížení dat o odpadních vodách, integrace dalších databází a přímý přístup k videozáznamům z kanálů a protokolům o kontrolách.
- prohlížení a úpravy pro monitorování a environmentální a urbanistické plánování odpadních vod a hydrologických systémů (německy: Genereller Entwässerungsplan).
- prohlížení podzemních katastrálních údajů (odpadní voda, voda, plyn a elektřina, později také telekomunikace) (německy: Leitungskataster).
- prohlížení katastrálních a zeměměřických údajů
- prohlížení a editace společného soupisu chráněných přírodních lokalit.
- prohlížení a editace urbanistických a regionálních dat.
- prohlížení a editace dat silniční infrastruktury
- prohlížení statistik generovaných přímo z databáze současných a minulých rezidentů.
- plánování a vizualizace pro energetické plánování (plynárenské oblasti, využití tepla z odpadních vod, geotermální energie v blízkosti povrchu, blokové teplárny atd.)

Další projekty se v současné době připravují.

![](./images/suisse_uster4.png){.align-right}

V roce 2007 nebylo zcela jasné, jakým tempem se bude QGIS dále vyvíjet a jak se bude vyvíjet komunitní i komerční podpora. Dnes lze konstatovat, že rychlost vývoje a vylepšení, která komunita QGIS provedla, předčila naše očekávání. Komunitní i komerční podpora ze strany společností SourcePole a Norbit je vynikající. Existuje přímá komunikace s vývojáři, aniž by byli odstíněni produktovým managementem nebo obchodním týmem. Vývojáři těchto dvou společností jsou zároveň vedoucími vývojáři projektu QGIS a mají vynikající znalosti kódové základny.

Chyby jsou často opraveny během několika hodin nebo dnů po nahlášení a nový vývoj je implementován v krátkém časovém horizontu. Nové funkce mohou být testovány ihned po vývoji a nasazeny uživatelům, kdykoli je jejich kvalita dostatečně dobrá pro koncového uživatele. Není třeba čekat na oficiální vydání softwaru. Užíváme si svobody, že můžeme ovlivňovat projekt a instalovat software na libovolný počet počítačů, aniž bychom museli řešit správu licencí. Těšíme se na budoucí spolupráci s komunitou QGIS a našimi komerčními podporovateli v zájmu rozvoje projektu QGIS.
## Autor
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Do tohoto článku přispěl v dubnu 2011 Dr. Andreas Neumann. Pracuje jako koordinátor GIS ve švýcarském městě Uster.
