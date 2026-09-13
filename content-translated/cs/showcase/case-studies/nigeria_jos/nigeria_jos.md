---
draft: 'true'

---
# Mapování biotopů a avifauny lesní rezervace Amurum v Nigérii pomocí QGIS
Lesní rezervace Amurum se nachází nedaleko města Jos ve státě Plateau v Nigérii. Byla založena z podnětu Ornitologického výzkumného ústavu A. P. Leventise (APLORI) za účelem ochrany přírody, vzdělávání a výzkumu. APLORI hostí katedra zoologie na univerzitě v Josu. Každoročně zde skupina přibližně osmi vysoce motivovaných studentů z celé Nigérie získává vzdělání v ochranářské biologii, statistice (pomocí R) a od roku 2011 také v GIS. Během dvou týdnů v prosinci 2011 jsme studovali základní koncepty GIS a ty jsme pak aplikovali pomocí QGIS pro různé ochranářské účely. V tomto článku popisujeme způsob, jakým jsme pomocí QGIS mapovali biotopy a jejich determinanty v rezervaci Amurum a jak byly základní mapy biotopů použity k získání vrstevnic pro účely efektivního určení prostorového rozložení avifauny včetně biodiverzity.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## Mapování nadmořské výšky, stínu kopců, svahu a stanovišť
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) Nástroje GdalTools byly použity ke sloučení původních datových sad a k oříznutí menší oblasti obsahující rezervu tak, aby rastrové datové sady zůstaly relativně malé. Pomocí GPS jsme zjišťovali nadmořské výšky na různých místech rezervace.
3) Celkově lze říci, že nadmořské výšky ze souboru dat SRTM dobře odpovídaly nadmořským výškám zjištěným pomocí gps. K výpočtu kopců a svahů pro danou oblast byly použity modely terénu v nástroji GdalTools. Tyto proměnné jsou důležité z ekologického hlediska, protože silně souvisejí s typem stanoviště.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) Protože jsme chtěli vytvořit dobře vypadající mapu, interpolovali jsme původní (oříznutou) výškovou mapu, abychom získali mapu s vyšším rozlišením. Použili jsme nástroj warp v nástroji GdalTools. Pomocí nástroje contour jsme získali hladké obrysové linie.
5) Souřadnice hranice rezervace byly získány chůzí po hranicích rezervace pomocí GPS. Body cesty a stopy uložené v GPS byly plynule importovány pomocí GPS Tools. Importované waypointy a stopy byly použity ke konstrukci polygonového shapefile. Podobným způsobem byly zmapovány stopy uvnitř rezervace.
6) Pomocí satelitního snímku Google, který jsme dostali do pracovního prostoru pomocí pluginu Openlayers, jsme mohli rychle a přesně sestavit mapu stanoviště Amurum. Rezervace má tři typy odlišných stanovišť: Savana, galerijní les a skalní výchoz. Na základě satelitního snímku jsme pomocí editoru nakreslili polygony vymezující tato tři stanoviště. Správné nastavení možností přichycení umožnilo vytvořit nepřekrývající se polygony.

## Mapování rozšíření a rozmanitosti ptáků
Mapy stanovišť byly použity k vygenerování náhodných lokalit. Plocha jednotlivých typů stanovišť byla použita k vygenerování počtu lokalit úměrného ploše jednotlivých typů stanovišť (stratifikace).

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## Závěr
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## Autoři
Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang Godwill
