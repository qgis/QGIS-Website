---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS a GRASS při mapování nebezpečí požárů v místních samosprávách
type: case-study

---
{{<content-start >}}
# QGIS a GRASS při mapování nebezpečí požárů v místních samosprávách
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Úvod
Regionální rada Southern Downs (SDRC) je malá až středně velká místní samospráva v jihovýchodním Queenslandu v Austrálii. Region rady, především jeho jižní část, trpí velkými požáry buše. Požáry buše jsou skutečným a aktuálním problémem pro obyvatele a vlastníky pozemků v regionu Southern Downs a mají za následek ztráty na životech a majetku.

Tento projekt umožní radě a obyvatelům regionu lépe si uvědomit rizika a umožní lepší rozhodování v budoucnu.

![](../images/australia_queens1.jpg)
## Projekt
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

Projekt GIS byl rozdělen do 6 hlavních kroků.
- Hodnocení a mapování svahů
- Hodnocení a mapování prvků
- Hodnocení a mapování vegetace
- Kombinace skóre pro určení závažnosti nebezpečí požáru křoví
- Ověřování v terénu a kvalitativní hodnocení
- Hotové mapy

## Použití QGIS a GRASS
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

Zásuvný modul QGIS GRASS byl použit k importu pětimetrových vrstevnic celé oblasti do GRASSu, které byly následně převedeny do rastrové vrstevnicové mapy pomocí r.surf.contour. Z rastrové obrysové mapy byla poté pomocí r.slope.aspect vygenerována mapa sklonů a aspektů. Kategoriím byly přiřazeny různé rozsahy sklonu a aspektu a bylo jim přiděleno riziko ohrožení. Vegetačním oblastem byly rovněž přiřazeny různé hodnoty rizika. Všechny výsledné rastrové mapy byly poté zkombinovány pomocí mapcalc a bylo jim přiřazeno konečné skóre nebezpečí. Skóre rizika se pak rozdělilo do tří hlavních kategorií: vysoké; střední a nízké.

Poslední částí procesu bylo ověření v terénu prostřednictvím venkovských hasičských sborů. Po procesu ověření byly v QGIS vytištěny konečné mapy pro prezentaci.

Vzhledem k tomu, že všechny příkazy systému GRASS lze spustit z příkazového řádku, byly všechny příkazy potřebné k vytvoření map nebezpečí požárů křovin zaznamenány pro účely dokumentace a pro případ, že by bylo třeba mapy někdy v budoucnu přegenerovat.
## Závěr
Celkově QGIS spolu s pluginem GRASS poskytl radě, která provádí vlastní mapování nebezpečí požárů křovin, skvělé zkušenosti a skvělý konečný výsledek. Zásuvný modul GRASS poskytuje velmi snadno použitelné rozhraní pro GRASS prostřednictvím QGIS. Vzhledem k tomu, že QGIS dokáže nativně otevřít rastrový formát GRASS, je integrace velmi bezproblémová a mapy lze vytvářet snadno.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Reference
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Autor
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Do tohoto článku přispěl v lednu 2011 Nathan Woodrow. Nathan je pracovníkem GIS v regionální radě Southern Downs a studuje na University of Souther Queensland obor prostorové vědy.

{{<content-end >}}
