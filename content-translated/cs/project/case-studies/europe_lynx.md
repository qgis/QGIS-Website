---
HasBanner: false
archived: true
date: 2015-02-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/europe_lynx1.png
title: Analýza stanovišť rysa v jižních Karpatech
type: case-study

---
{{<content-start >}}
# Analýza stanovišť rysa v jižních Karpatech
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2015</span>
</p>

Případová studie na podporu základních znalostí modelování stanovišť volně žijících živočichů pro studenty na základě dat z otevřených zdrojů.
## Úvod
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Metodika
Všechna shromážděná data byla zpracována pomocí QGIS 2.6 a 2.8, promítnuta do ETRS89 / ETRS-LAEA a uložena podle směrnice INSPIRE, aby splňovala normy EU. Byl definován celkový **diskrétní váhový index**, který byl aplikován na všechna vstupní data.

<figure>
<img src="../images/europe_lynx1.png" alt="europe_lynx1.png" />
<figcaption>Figure 1: Workflow - Lynx habitat expert model</figcaption>
</figure>

**Popis pracovního postupu**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Poznámka: Třídy půdního pokryvu byly seskupeny podle možného výskytu rysa a lidské činnosti. Ačkoli jsou technicky staršího původu, informace týkající se hodnot lesních porostů byly začleněny za účelem indikace zlepšení stavu biotopů a jako obecný příklad pro spojování souborů prostorových dat*.
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
```
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
```
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
```
*Poznámka: Model potenciální přístupnosti  pro lovce udává klesající pravděpodobnost přístupu lovců do oblasti s rostoucí vzdáleností od silnic a rostoucím sklonem*.

<figure>
<img src="../images/europe_lynx2.png" alt="europe_lynx2.png" />
<figcaption>Figure 2, 3 and 4</figcaption>
</figure>

## Závěr
Při pohledu na konečný výstup (obrázek 3) se zdálo, že se podařilo provést věrohodnou první analýzu potenciálních stanovišť, ale co je důležitější, samotné základní modelování se ukázalo být méně obtížné, než se původně očekávalo. Naše rozhodnutí přidat dílčí model pro přístupnost lovců nám umožnilo implementovat další dimenzi z hlediska hodnocení rizik pro stanoviště, kterou lze jednoduše vnořit do již existujícího scénáře a využít ji pro stanovení nutnosti ochrany v rámci aspektů např. rozvoje infrastruktury. Některé zásadní informace o stanovišti, jako je např. struktura lesa (naše nejvyšší vhodnost stanoviště), však nelze získat z dostupných datových souborů a v kombinaci s komplexním chováním druhů je proto třeba výsledek chápat jako základní a neúplný. Dalšími faktory, které nejsou v této fázi implementovány, jsou mortalita na silnicích, drsnost terénu a podrobný výskyt kořisti.

Kromě toho, že je software QGIS volně dostupný a má otevřený zdrojový kód, prošel v posledních letech významným vývojem. Velmi pozitivní zkušenosti jsme učinili s integrací balíčku nástrojů, který umožňuje používat různé nástroje GRASS a SAGA i nezkušeným uživatelům. I přes časté změny mezi různými verzemi se nevyskytly žádné problémy s kompatibilitou a obecná absence administrativních omezení může být silnou výhodou při intuitivní práci se soubory dat. Těšíme se na další vylepšení, zejména pokud jde o integrovaný nástroj pro tvorbu modelů.
## Reference
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (prosinec 2012): Status, management a rozšíření velkých šelem v Evropě. Dokument Evropské komise.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Hodnocení vhodnosti středoevropské krajiny pro reintrodukci rysa ostrovida. Článek Journal of Applied Ecology.
- Salvatori, V. (2004): Salvatori: V. Salvatori: Oblasti ochrany velkých šelem v Karpatech. Doktorská práce.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (březen 2002): Charakteristika a hodnocení vhodnosti nor rysa ostrovida (Lynx lynx). Zpráva KORA č. 12e, diplomová práce.

### Autoři
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe a David Winger jsou studenti čtvrtého semestru bakalářského studijního programu International Forest Ecosystem Management, Anne Gnilke, resp. německé lesnictví, a Henri Hiltunen je výměnný student z Mikkeli University of Applied Sciences ve Finsku. Prof. Mund přednáší GIS a dálkový průzkum Země na HNE Eberswalde od roku 2010 a poskytl projektu vedení a technickou podporu.

Kontaktujte prosím Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de nebo Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de pro další informace.

{{<content-end >}}
