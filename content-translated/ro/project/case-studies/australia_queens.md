---
HasBanner: false
archived: true
date: 2011-01-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/australia_queens1.jpg
title: QGIS și GRASS, în Cartografierea de către Guvernele Locale a Pericolelor de
  aprindere a vegetației
type: case-study

---
{{<content-start >}}
# QGIS și GRASS, în Cartografierea de către Guvernele Locale a Pericolelor de aprindere a vegetației
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2011</span>
</p>

## Introducere
Southern Downs (SDRC) este o administrație locală de dimensiuni mici și mijlocii, în sud-estul Queensland, Australia. Consiliul Regional, în special în partea de sud, suferă de incendii majore. Aprinderea vegetației este o preocupare reală, permanentă pentru locuitorii și proprietarii de terenuri din regiunea Southern Downs, care a dus la pierderea de vieți și bunuri.

Acest proiect va permite Consiliului și oamenilor din regiune să conștientizeze riscurile, pentru mai bunele decizii viitoare.

![](../images/australia_queens1.jpg)
## Proiectul
As bushfire is not only a problem for SDRC but also for the whole of Queensland, the state government requires that each local government identifies the bushfire hazard in their area via the State Planning Policy 1/03 Mitigating the Adverse Impacts of Flood, Bushfire and Landslide \[1\]. This kind of job would normally be done using consultants but was instead done by the council itself using a combination of QGIS and GRASS.

Partea GIS a proiectului a fost împărțită în 6 etape principale
- Evaluarea pantelor și cartografierea
- Evaluarea aspectului și cartografierea
- Evaluarea vegetației și cartografierea
- Combinarea scorurilor pentru a identifica gradul de severitate a pericolului incendiilor de vegetație
- Verificarea terenului și evaluarea calitativă
- Hărți Finale

## Folosirea QGIS și GRASS
![](../images/australia_queens2.jpg)

QGIS, using the GRASS plugin, was selected as it provided the tools needed to complete the job and the interaction between QGIS and GRASS made it easy to process the raster maps and present them in a meaningful way to users. SDRC uses MapInfo for its main GIS system, however MapInfo's addons were not as powerful as GRASS GIS for raster processing.

Plugin-ul GRASS QGIS a fost folosit pentru a importa curbele de nivel de 5 metri din întreaga regiune în GRASS, care au fost apoi convertite într-o hartă de curbe de nivel raster folosind r.surf.contour. Panta și aspectul hărții au fost apoi generate folosind r.slope.aspect pe curbele de nivel din harta raster. Diverselor pante li s-au atribuit categorii, variind ca aspect și având un diferit scor de risc. Zonelor de vegetație li s-au acordat, de asemenea, scoruri de risc diferite. Toate hărțile raster rezultate au fost apoi combinate cu mapcalc, rezultând un scor final de risc. Scorurile de risc au fost apoi împărțite în trei categorii principale: mare, mediu și scăzut.

Partea finală a procesului a fost verificarea în teren, prin intermediul serviciului de pompieri din mediul rural. După procesul de revizuire, QGIS a fost folosit pentru a imprima hărțile finale de prezentare. 

Deoarece toate comenzile GRASS pot fi rulate din linia de comandă, toate comenzile care au fost necesare pentru a genera hărțile de risc au fost înregistrate, în scopul documentării și pentru cazul în care hărțile vor trebui regenerate.
## Concluzii
QGIS, împreună cu plugin-ul GRASS, a oferit o mare experiență și un câștig deosebit pentru Consiliu, care și-a făcut propria cartografiere. Plugin-ul GRASS oferă o interfață ușor de utilizat pentru GRASS, prin QGIS. Deoarece QGIS este capabil de a deschide formate raster native GRASS, integrarea este foarte ușoară, hărțile făcându-se cu ușurință.

The project won an encouragement award at the Queensland Planning Institute of Australia state planning awards in 2010 \[2\]
## Referințe
- \[1\] <http://www.emergency.qld.gov.au/publications/spp/>
- \[2\] <http://digital.crowtherblayne.com.au/default.aspx?xml=crowther_pia.xml>

## Autor
<figure>
<img src="../images/australia_queensaut.jpg" class="align-left" height="200" alt="australia_queensaut.jpg" />
<figcaption>Nathan Woodrow</figcaption>
</figure>

Acest articol a fost transmis în ianuarie 2011 de către Nathan Woodrow. Nathan este un ofițer GIS la Southern Downs Regional Council și studiază Științele Spațiale la Universitatea din Southern Queensland

{{<content-end >}}
