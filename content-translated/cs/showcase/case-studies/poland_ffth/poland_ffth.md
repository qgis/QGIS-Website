---
draft: 'true'

---
# Využití QGIS pro plánování sítí FTTH/GPON v souvislosti s implementací Evropské digitální agendy
## Definice problému
V posledních několika letech zahájilo mnoho zemí EU operační programy k provádění Evropské digitální agendy (EAC), kterou Evropská komise vypracovala v roce 2010. Podle jejích pokynů by do roku 2020 měl mít každý občan Evropské unie přístup k internetovému pásmu o rychlosti 30 Mb/s a nejméně polovina z nich bude mít přístup k pásmu ne pomalejšímu než 100 Mb/s.

Polsko je jednou ze zemí, v nichž se agenda realizuje. Díky fondům Evropské unie může mnoho místních operátorů konkurovat velkým poskytovatelům telekomunikačních služeb, pokud jde o vysokorychlostní širokopásmové služby. Bohužel podání žádosti o finanční prostředky vyžaduje velké množství práce nutné k vypracování řádné dokumentace, zahrnující mimo jiné vypracování koncepčních map plánované sítě FTTH (Fiber To The Home).

V současné době navíc nejsou k dispozici žádné IT nástroje založené na GIS, které by potenciálním příjemcům pomohly s přípravou dokumentace. Složitost problému ještě komplikuje skutečnost, že takový software by měl umožnit tvorbu dokumentace v souladu s konkrétními pokyny programu (např. povinnost připojení vzdělávacích institucí).

Vzhledem k tomu, že máme rozsáhlé zkušenosti v telekomunikačním průmyslu, požádaly nás subjekty žádající o finanční prostředky EU o vytvoření softwaru podporujícího vývoj koncepční mapy sítě FTTH. Produkty generované vyvinutým softwarem měly výrazně urychlit proces přípravy žádosti.
## Popis řešení
Vzhledem k vysoké popularitě, široké dostupnosti, otevřenosti softwaru a obrovským funkčním schopnostem bylo přirozené zvolit QGIS jako platformu, která bude sloužit jako základ našeho řešení.

Podle pokynů FTTH Council Europe je zásadní nejprve připravit plán, který zohlední jak technické hledisko (umístění kabelů, spojovacích uzávěrů, rozbočovačů), tak ekonomické hledisko (poptávku) na základě údajů o skutečných adresních bodech. Struktura budovy a hustota zástavby určují technologii návrhu sítě GPON (Gigabit Passive Optical Network). Aby bylo možné efektivně plánovat topologii sítě, je třeba mít mj:
- přístup k datům GIS,
- automatizace zpracování dat GIS,
- použití algoritmů síťové optimalizace,
- uplatnění pravidel síťového inženýrství GPON.

Všechny tyto položky byly propojeny v platformě QGIS. Níže je uveden stručný popis toho, jak jsme projekt realizovali a jaké funkční položky byly začleněny do jednoho řešení.

K dosažení našeho cíle jsme kromě standardní platformy GIS potřebovali několik funkčních komponent:
- GRASS - kolekce vektorových a síťových algoritmů,
- Pluginy QGIS - OpenLayer, QuickOSM, Scipy Point Clustering, WorkContextTracer (náš plugin),
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - místní databáze pro ukládání vstupních a výstupních dat.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](./images/poland_ffth/toolbox.png){.align-left}

Aby se výsledky následných analýz nepomíchaly, poskytli jsme zásuvný modul WorkContextTracer, který seskupuje naši práci do tzv. pracovních kontextů.

![](./images/poland_ffth/workorder.png){.align-left}

Síťové algoritmy založené na grafových funkcích dostupných v systému GRASS byly obohaceny o telekomunikační skripty. Zavedli jsme koncept shlukování poptávek, který umožňuje použít jak K-means, tak hierarchické metody pro agregaci poptávkových bodů.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

Operátoři také potřebovali asociaci mezi vytvořenými uzly sítě a adresními body, aby mohli odhadnout individuální náklady každé větve sítě. Pro splnění tohoto úkolu jsme vytvořili skripty, které tuto operaci provádějí a výsledky ukládají do místní databáze SpatiaLite. Data bylo třeba exportovat do tabulkového procesoru, proto jsme pro splnění tohoto požadavku použili volně dostupnou softwarovou knihovnu.
## Jak uživatelé používali nástroj k vytvoření plánu sítě FTTH/GPON
Uživatel zahájil práci otevřením nového pracovního kontextu a zadáním vstupní vrstvy adresních bodů k analýze. Pomocí standardního rozhraní QGIS mohl uživatel stanovit soubor požadavků na adresní body a nakonec zadat parametry potřebné pro další kroky algoritmu.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

Bez informací o stávající civilní infrastruktuře byla jako směrovací vrstva použita správně filtrovaná silniční síť OpenStreet. Algoritmy Scipy na základě vstupních parametrů shlukovaly adresní body do poptávkových agregátů a označovaly je samostatnou barvou označující jejich přiřazení k určitému shluku.

![](./images/poland_ffth/step1.png){.align-left}

Po seskupení všech adresních bodů uživatel zahájil kroky plánování sítě na vysoké úrovni, přičemž poskytl vrstvy připravené v předchozích krocích a vrstvu s výchozím bodem sítě GPON.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](./images/poland_ffth/step4_results.png){.align-left}

V této fázi již měl uživatel k dispozici všechny informace pro vytvoření technické koncepce sítě FTTx na vysoké úrovni. Poslední částí bylo vygenerování tabulky s datovou zprávou, která zobrazovala všechny vypočtené údaje z několika různých pohledů.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Závěr
Díky využití platformy QGIS a možnostem jejího rozšíření se nám podařilo vyvinout bezplatné open source řešení umožňující telekomunikačním operátorům připravit podklady potřebné pro podání žádosti o spolufinancování v rámci programu EU implementujícího evropskou digitální agendu.

Spojením flexibilních vektorových algoritmů se skripty telekomunikačního inženýrství jsme umožnili praktické využití matematických algoritmů při řešení reálných problémů týkajících se plánování telekomunikačních sítí. Uživatel operuje se srozumitelným rozsahem dat (obec, budova, silnice), zatímco transformace těchto informací do matematického modelu je před uživatelem skryta.

Uživatel získal mnoho užitečných výhod:
- Automatický vývoj plánu sítě GPON na základě veřejně dostupných dat a technických pravidel technologie GPON.
- Možnost přizpůsobit nástroj konkrétním programovým směrnicím EU v dané zemi.
- Velká přesnost výsledků odpovídá skutečným rozměrům.
- Vytvoření údajů potřebných pro podání žádosti o finanční prostředky EU: mapa koncepce sítě, zpráva o uzavření kabelů a spojů s přiřazením obslužných oblastí.
- Možnost přesného stanovení nákladů na výstavbu a odpisy jednotlivých částí sítě s výpočtem nákladů na připojení jednotlivých adresních bodů.
- Možnost upřednostnit adresní místa od nejziskovějších po nerentabilní.
- Možnost vyhodnocovat základní ekonomické ukazatele, jako je ROI, NPV.

## Užitečné odkazy a bibliografie
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Autoři
Řešením je zcela bezplatný nástroj s otevřeným zdrojovým kódem. Je součástí rozsáhlejšího projektu založeného na platformách QGIS a FreeCAD, který je určen pro použití v telekomunikačním průmyslu.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.
