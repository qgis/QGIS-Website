---
HasBanner: false
archived: false
date: 2015-01-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/portugal_pinhel1.jpg
title: QGIS a mapování rizika lesních požárů v Portugalsku
type: case-study

---
{{<content-start >}}
# QGIS a mapování rizika lesních požárů v Portugalsku
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2015</span>
</p>

Portugalsko bylo postiženo rozsáhlými požáry, které způsobily obrovské ztráty, a to nejen ekologické, ale i hospodářské a sociální. Aby tomuto riziku čelila, rozhodla se portugalská vláda před několika lety prostřednictvím Národního úřadu pro lesy (AFN) vytvořit technické úřady přidělené místním samosprávám, které musí kromě jiných dovedností připravit obecní plány ochrany před lesními požáry a operativní reakce.

In order to support the elaboration of these documents, the AFN provided technical guides with a methodology for calculating and mapping the Forest Fire Hazard and Risk. Moreover, tutorials have been offered to follow this methodology, using Proprietary Software. However, the acquisition and licensing costs of that software are unaffordable for most of the smaller local administrations and so, it was decided to create and make available a guide with a methodology for developing Hazard and Risk cartography using only Free and Open Source Software \[<http://goo.gl/TSv2E>\].

Bylo navrženo použít následující sadu softwaru: QGIS, GRASS GIS, gvSIG a knihovny GDAL/OGR. Tato příručka popisuje všechny úkoly geoprocessingu nezbytné pro vypracování plánů ochrany lesů před požáry a operační zásah podle metodiky AFN. Velká část úloh byla vypracována v QGIS a prostorová analýza v rastrovém modelu byla vypracována v GRASS. gvSIG byl použit pro síťovou analýzu se svým rozšířením Network Analysis a knihovny GDAL/OGR byly použity pro transformace mezi souřadnicovými referenčními systémy.

Po rozsáhlém souboru testů metodiky a třech letech reálného používání při přípravě operačního plánu obce Pinhel lze říci, že navržené alternativy umožňují s mnoha výhodami nahradit proprietární software, který se obvykle používá k provádění tohoto úkolu. Ověření výsledků ukazuje, že navzdory relativní jednoduchosti koncepčního modelu je jeho vypovídací schopnost poměrně dobrá a že implementace modelu v Open Source Software nijak negativně nenarušuje výsledky, spíše naopak.
> ![](../images/portugal_pinhel1.jpg)

<figure>
<img src="../images/portugal_pinhel2.jpg" class="align-right" alt="portugal_pinhel2.jpg" />
<figcaption>Forest Fire Hazard and Risk Maps of Pinhel, implemented with Open Source Software.</figcaption>
</figure>

Ve druhé fázi se pokusili tento proces urychlit a pomocí modelů vytvořili pracovní postup, který provádí širokou sadu úkolů téměř bez zásahu člověka. Tato druhá fáze spočívala v podstatě v automatizaci celého postupu popsaného v praktické příručce, která byla výsledkem první fáze. Taková automatizace by mohla znamenat zkrácení několika hodin intenzivní práce technika, který hodlá každoročně vypracovávat Plány obrany lesa, na pouhých několik minut, při nichž se lidský zásah omezuje na výběr vstupních údajů a určení místa, kde hodláme uchovávat výstupní údaje.

<figure>
<img src="../images/portugal_pinhel3.png" class="align-right" alt="portugal_pinhel3.png" />
<figcaption>Interface of the Sextante Model to calculate the Probability of the Forest Fire Hazard.</figcaption>
</figure>

In furtherance of this second phase, we used the Python version of Sextante software, that works integrated into QGIS and adds a broad set of independent applications (GRASS GIS, SAGA GIS, OTB, R, GDAL/OGR, Pymorph, LASTools, Python scrips, etc..) in a single interface, providing a huge geoprocessing toolbox to QGIS users. Besides the integration of these applications in QGIS, Sextante has a tool for creating models, taking advantage of the modules offered by any of those softwares which aggregates. So, we\'ve created a model to automate the process of producing Forest Fire Hazard and Risk maps, using GRASS, SAGA, fTools and MMQGIS tools.

<figure>
<img src="../images/portugal_pinhel4.png" class="align-right" alt="portugal_pinhel4.png" />
<figcaption>Part of the model developed for automation of the production of cartography for Forest Fire Hazard and Risk.</figcaption>
</figure>

The results obtained so far are very promising, as already can be automatically achieved the creation of the Hazard and Risk Maps \[2\]. Taking into account that the Python version of Sextante is still very recent and is in heavy construction, there are some problems that must be corrected so that the models may be completed, which certainly will happen very soon, given the momentum that Sextante project presents. As future work, we intend to apply, also automatically, the symbology to the results as well as provide the final layouts in QGIS Composer, ready for export and/or print. Upon completion of the second phase and the realization of a sufficient set of tests that can validate the results obtained, it is our intention to provide the model free and openly.
## Závěry
Zkoumané alternativy se ukázaly jako nesmírně kvalitní a umožňovaly všechny operace doporučené v technických příručkách státní správy lesů, a to v mnoha ohledech efektivněji než s proprietárním softwarem. Z hlediska snadnosti použití bylo zjištěno, že tento typ softwaru není v žádném případě složitější než proprietární software, vyžaduje pouze větší technické znalosti o implementovaných modelech a algoritmech, které však umožňují vyšší míru volnosti, což umožňuje zkoumat a dolaďovat modely pro každou konkrétní situaci. Po několika letech testování a používání v obci Pinhel je proces tvorby kartografie nebezpečí a rizika lesních požárů s využitím výhradně softwaru s otevřeným zdrojovým kódem plně konsolidován.

Skutečnost, že software s otevřeným zdrojovým kódem je založen na standardech a podporuje většinu otevřených datových formátů, umožňuje úplnou interoperabilitu mezi softwary, což uživateli umožňuje vybrat si v každém okamžiku ten nejvhodnější. Přestože náš návrh směřuje ke konkrétní sadě softwaru, nic nebrání tomu, aby byl nahrazen některou z existujících alternativ v široké škále návrhů svobodného a otevřeného softwaru pro geoprostorový průmysl. QGIS se však stále více prezentuje jako nejkomplexnější, nejstabilnější a nejsnadněji použitelné řešení FOSS4G, jehož projekt je dynamičtější, s rychlým odstraňováním chyb a s téměř každodenní implementací nových zásuvných modulů, které přidávají specifické funkce do nejrůznějších oblastí činností.
## Autor
<figure>
<img src="../images/portugal_pinhelaut.png" class="align-left" height="200" alt="portugal_pinhelaut.png" />
<figcaption>Pedro Venâncio</figcaption>
</figure>

Pedro Venâncio Bc. v oboru geologie, postgraduální studium svobodného softwaru a Mgr. v oboru geografických informačních systémů. Působil jako výzkumný pracovník v Centru pro geofyziku na univerzitě v Coimbře, v Národní laboratoři pro stavební inženýrství a v současné době je zodpovědný za službu kartografie a geografických informačních systémů na magistrátu města Pinhel.

{{<content-end >}}
