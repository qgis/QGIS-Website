---
HasBanner: false
archived: true
date: 2016-03-01
draft: false
featured: false
section: projekt
sidebar: true
thumbnail: images/uruguay_mides1.png
title: Využití QGIS na uruguayském ministerstvu sociálního rozvoje (MIDES)
type: case-study

---
{{<content-start >}}
# Využití QGIS na uruguayském ministerstvu sociálního rozvoje (MIDES)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>March 01, 2016</span>
</p>

## Úvod
The Ministry of Social Development of Uruguay ([MIDES,](http://www.mides.gub.uy/innovaportal/v/4376/3/innova.front/mision) , for its acronym in Spanish) is responsible for the national social policies. MIDES is also accountable for the coordination -at both sectoral and territorial levels- articulation, monitoring, supervision and evaluation of plans, programs and projects, within the areas of its competence, aiming at the consolidation of a progressive redistributive social policy.

The National Division of Evaluation and Monitoring ([DINEM](http://dinem.mides.gub.uy/innovaportal/v/25948/11/innova.front/mision-y-cometidos) ) is a section of MIDES that oversees the monitoring and evaluation of plans, programs, actions, devices and social projects through the national territory. DINEM also produces and manages necessary information to improve their design and implementation.

The [Department of Geography of DINEM](http://dinem.mides.gub.uy/innovaportal/v/25507/11/innova.front/departamento-de-geografia) is responsible for the production, management and analysis of geographical information,
## QGIS na katedře geografie DINEM
Ever since the consolidation of the Department of Geography in 2012, we have tried to incorporate open source software to fulfill our duties. In particular, the management of an extensive field work, consisting in the annual implementation of approximately 40,000 visits to socially vulnerable households throughout the country. The objective was to conform a thorough georeferenced database of target households, in order to improve social policies implementation. Particularly, data was collected to enhance the scope of monetary transfer programs ([\"Asignaciones Familiares -- Plan de Equidad\"](https://www.bps.gub.uy/3540/plan-de-equidad.html) and [\"Tarjeta Uruguay Social\"](http://www.mides.gub.uy/innovaportal/v/55480/3/innova.front/tarjeta-uruguay-social-tus)). The survey form applied contemplates social, housing, and environmental aspects.

Logistické zajištění této terénní práce zahrnovalo použití statistických balíků pro správu vytvořené databáze a intenzivní využívání GIS pro organizaci terénních výjezdů a georeferencování odlehčených dat.

<figure>
<img src="../images/uruguay_mides1.png" class="align-center" alt="uruguay_mides1.png" />
<figcaption>QGIS at work: identifying houses on informal settlements to implement fieldwork</figcaption>
</figure>

Ačkoli byl při zahájení pracovního procesu implementován proprietární software, vývoj samotných úkolů si postupně vyžádal jeho převedení na software s otevřeným zdrojovým kódem. Jak se proces jako celek stával více elektronizovaným - zahrnoval engine pracovních postupů a geoprostorovou databázi PostGIS -, licenční požadavky a výhody, které nabízejí možnosti svobodného a otevřeného softwaru (FOSS), nás přiměly ke změně. Tímto způsobem, jak se projekt QGIS zdokonaloval (méně chyb a více funkcí), jsme byli schopni uspokojit naše potřeby pomocí QGIS. Nástroje spojené s PostGIS umožnily pracovní skupině rychle koordinovat úkoly potřebné k životaschopnosti každodenních terénních výjezdů spolu s následnými analytickými úkoly na stejných datech, která terénní práce vytvořila, krátce poté, co byla odlehčena a digitalizována.

<figure>
<img src="../images/uruguay_mides2.png" class="align-center" alt="uruguay_mides2.png" />
<figcaption>QGIS at work: Montevideo, Uruguay’s capital and most populated city, overlayed with PostGIS layer showing to-do visits (mostly composed of socially vulnerable households, in the outskirts of the city)</figcaption>
</figure>

In addition to information management and field work implementation, we constantly use QGIS typical geospatial tools to produce tematic cartography, and in spatial analysis tasks. This last, as much about the data that the fieldwork generates, as with other ministry programs information, and frequently even to aid interinstitutional projects. With [\"qgis2web\"](https://plugins.qgis.org/plugins/qgis2web/) we were able to produce interactive maps, which have become the main way to communicate the results of such investigations. They allow human resources within other programs and agencies to easily and effectively manage higher amounts of information than with a collection of static maps, even when these resources are not used to reading spatial data.
## Závěr
QGIS se stal základním softwarem katedry geografie DINEM. Představuje vynikající výkon pro práci s těžkými soubory a pro interakci s PostGIS a s naším workflow enginem. To nám umožňuje vynikající správu geografických dat, což také umožňuje tvorbu podkladových map a tematických kartografií špičkové kvality.

At the same time, extra features that are incorporated through plugins are of great value to us. For instance, the possibility of exporting \"leaflet\" map viewers, as well as incorporating high resolution satellite imagery directly into the GIS work area through "OpenLayers" to manually vectorize information, among others.

This variety of options is precisely what has allowed us to develop the specific and at the same time very different technical solutions that programs and agencies have been needing through past years.As mentioned in this article, we can state that QGIS meets the necessary requirements to be used in public administration as desktop GIS software. Also it has been a cornerstone in helping this institution to set up a web map, offering general population much information about social issues ([SIG MIDES](https://mapas.mides.gub.uy/), OpenLayers based WEB GIS developed by the IT division).
## Autoři
Guillermo D\'Angelo - Head of the Geography Department (DINEM-MIDES, Uruguay). Degree in Geography.

Richard Detomasi - poradce v sekci prostorových analýz na katedře geografie (DINEM-MIDES, Uruguay). Doktorand v oboru sociálních věd, populační studia. Magistr současných studií Latinské Ameriky. Titul v oboru antropologických věd.

Martín Hahn - poradce v sekci prostorových analýz na katedře geografie (DINEM-MIDES, Uruguay). V současné době studuje bakalářský obor geografie.

Přestože tento článek napsali tři výše uvedení, na procesu, který je v něm popsán, se podílelo více než sto lidí, takže tato práce patří především jim.

Contact: <mapas@mides.gub.uy>

{{<content-end >}}
