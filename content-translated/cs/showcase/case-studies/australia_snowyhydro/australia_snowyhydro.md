---
draft: 'true'

---
# Použití sady nástrojů pro zpracování k automatizaci klasifikace sněhu
Společnost Snowy Hydro Limited (SHL) je špičkový výrobce elektřiny se sídlem ve Sněžných horách v Novém Jižním Walesu v Austrálii. Přestože společnost Snowy Hydro Limited vlastní řadu výrobních zařízení po celé zemi, je nejznámější díky péči o ikonický prvek australské infrastruktury, vodní elektrárnu Snowy Mountains Hydro Electric Scheme.

Vodní elektrárna Snowy Mountains Hydro Electric Scheme, jejíž provoz je možný díky sezónním sněhovým srážkám ve vysokohorské oblasti Nového Jižního Walesu. Voda z jarního tání sněhu se využívá k výrobě elektřiny, která pokrývá špičkovou poptávku na národním trhu s elektřinou, a zároveň odvádí vodu do sušších vnitrozemských oblastí jihovýchodní Austrálie pro zavlažování a zemědělství.

Klasifikace sněhové pokrývky v zimních měsících umožňuje SHL sledovat životní cyklus zasněžené oblasti, archivovat oblasti pokrytí pro historické záznamy a poskytovat statistiky pokrytí týmu hydrografické služby pro předpovědi vydatnosti a zásob vody.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Pozadí
Každý rok v zimních měsících (od 1. června do 31. října) získává SHL co nejvíce snímků bez oblačnosti z družice MODIS Terra (EOS AM). Tyto snímky jsou poté vloženy do algoritmu známého jako Normalizovaný diferenční sněhový index (NDSI), který se používá k označení oblastí, kde se vyskytuje sníh. Ačkoli tento algoritmus není jedinečný pro žádný konkrétní snímač, přístroj MODIS byl vybrán kvůli dostatečnému prostorovému rozlišení a dennímu pokrytí oblasti projektu (mapa 1.1 Zasněžené povodí).
## Cíl
Cílem tohoto projektu je automatizovat pracovní postup NDSI jako model v sadě nástrojů pro zpracování QGIS. Požadovaným výstupem je vektorový polygon zobrazující rozsah sněhové pokrývky v povodí Snowy Water spolu s atributem popisujícím celkovou pokrytou plochu v kilometrech čtverečních.
## Metoda
Samotný algoritmus NDSI je poměrně jednoduchý (viz níže ve vzorci 1.1 - Normalizovaný diferenční sněhový index (NDSI)) a následné kroky potřebné k extrakci sněhové pokrývky ve vektorovém formátu se také dobře hodí pro model zpracovatelského toolboxu.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

Tento algoritmus NDSI vrátí výsledky v rozmezí -1 až 1, přičemž prahovou hodnotou pro sníh jsou obvykle hodnoty vyšší než 0,4. Příklad výstupu NDSI je uveden níže (Mapa 1.3 - výstup NDSI) spolu s přirozeným barevným snímkem (Mapa 1.2 - MODIS true color) pro 13. červenec 2014. Jak je vidět z těchto snímků, výstup NDSI velmi dobře rozlišuje zasněžené oblasti od jiných typů zemského pokryvu a mraků. Může však nesprávně klasifikovat části velkých vodních ploch jako sníh, což je způsobeno tím, že voda má absorpční vlastnosti v blízké infračervené části spektra. Tato vlastnost NDSI naznačuje potřebu začlenit do modelu v určité fázi masku vody.

![Map 1.2 - MODIS true colour](./images/australia_snowyhydro2.jpg){.align-left width="300px"}

![Map 1.3 - NDSI output](./images/australia_snowyhydro3.jpg){.align-center width="300px"}

![Map 1.4 - Recoded \"Snow\" vs \"Non snow\"](./images/australia_snowyhydro4.jpg){.align-left width="300px"}

The NDSI output is created with some very simple band map by using the GRASS module \"r.mapcalculator\". Once the NDSI grid was available the NDSI threshold of 0.4 needed to be applied and this would result in a boolean grid depicting \"Snow\" and \"Non snow\" areas. To get that classification another GRASS module \"r.recode\" was used and produced the result shown above in Map 1.4 Recoded 'Snow' vs 'Non Snow'.

The recoded grid was then converted to a vector polygon dataset and the snow covered areas were extracted (shown below, Map 1.5 - Extracted snow). The snow covered areas were then clipped to the Snowy Water Catchment (shown below, Map - 1.6 Snow inside the SWC), then the large water bodies are masked out (shown below, Map 1.7 - Final snow covered area), and finally the area statistics for the snow covered area is generated.

![Map 1.5 - Extracted Snow](./images/australia_snowyhydro5.jpg){.align-left width="300px"}

![Map 1.6 - Snow inside the SWC](./images/australia_snowyhydro6.jpg){.align-center width="300px"}

![Map 1.7 - Final snow covered area](./images/australia_snowyhydro7.jpg){.align-left width="300px"}

The output from the model is a vector polygon showing the snow covered area within the Snowy Water Catchment. The attributes of the polygon include the area covered by the snow and the percentage of the catchment that is covered. The model in its entirety can be seen below in \"Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model\".

![Image 1.1 - Normalised Difference Snow Index (NDSI) QGIS processing toolbox model](./images/australia_snowyhydro.png){.align-center width="600px"}
## Výsledky / závěr
Sada nástrojů pro zpracování QGIS představuje výkonný způsob, jak automatizovat pracovní postup, jako je tato klasifikace sněhu. Výše uvedený model úspěšně automatizuje proces klasifikace sněhu a poskytuje datovou sadu GIS, kterou lze použít pro vizualizaci a vstup do dalších statistických aplikací. Úspěšně odstraňuje subjektivní chyby uživatele spojené s předchozími metodami používanými SHL a zároveň poskytuje opakovatelný a konzistentní nástroj pro klasifikaci. Některé sezónní výsledky si můžete prohlédnout zde.
### Autor
Andrew Jeffrey je analytik GIS ve společnosti Snowy Hydro Limited se sídlem v Coomě v Novém Jižním Walesu v Austrálii. V roce 2004 absolvoval bakalářské studium (Bsc) na Charles Sturt University ve Wagga Wagga v oboru prostorové informační systémy. Během svého působení ve společnosti Snowy Hydro Limited měl možnost poskytovat prostorovou podporu zajímavým projektům, jako je experiment Cloud Seeding, a každodennímu provozu v rámci organizace.
