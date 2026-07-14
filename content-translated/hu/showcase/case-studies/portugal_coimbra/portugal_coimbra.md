---
draft: 'true'

---
# Táj meghatározás nyílt forráskódú szoftverek felhasználásával. A LecoS modul
This case study results from the final draft of the Graduate Geographic Information Systems taught by GeoPoint. We proposed to study a landscape using Landscape Ecology plugin (LecoS) in QGIS 2.01 Dufour. The study was conduted in a region of central Portugal, Municipality of Coimbra, with an total area of 31940ha and it has geographic coordinates 40°12\'11.84\" North, 8°24\'37.15\" West. Because the new administrative reorganization this municipality are divided into 18 parishes, which are mostly urban areas (Figure 1).

![Geographic location of the municipality of Coimbra.](./images/portugal_coimbra1.png){.align-left}

A tájak jellemzésének meghatározása a tájmetrika mennyiségi indexeinek felhasználásával készült. Ezen indexek segítségével leírhatóak a tájak strukturális jellemzői, a változások és azok összegfüggéseinek dokumentálása egyes fajok vagy faj csoportok előfordulásában (Turner et al, 2001;. Olsen et al, 2007;. Fidalgo et al. , 2009). Az extrém nagy számú mutatók  számíthatóak így táj, osztály és folt szintekre is (Turner et al, 2001;. Fidalgo et al, 2009.). A számításokban felhasználásra került a Corine Felszínborítás és földhasználat (COS 90 és COS2006) és a saját készítésű felszínborítási térképek. Martin Jung szerint (2012) a Landscape Ecology Statisctics (LecoS) QGIS beépülő modul felhasználásával készültek a tájmutatókat tartalmazó raszter rétegek. Az eredmények CSV formátum is elérhetőek. 
## Módszerek
Landscape metrics was calculated using the Corine Land Cover (CLC) of the years 1990 and 2006. For this purpose it was necessary to transform the coverages in raster format with cell size 50x50 meters. We use r.to.raster tool the Grass Gis module that were present in processing toolbox and the CLC classification level used it´s the first. After transform coverages we calculate the metrics in Landscape Ecology plugin (LecoS) using the graphical modeler (Figure 2).

![Landscape metrics calculated for diferent years (1990 and 2006).](./images/portugal_coimbra3.png){.align-left}

A következők kerültek kiszámításra: a felszínborítási egységek területe, tájarány, élsűrűség, foltok száma, legnagyobb folt területe, legkisebb folt területe, átlagos folt távolság és optimális rácsméret (1. Táblázat). A diverzitás számításokban a Shannon, a Uniformity és Simpson indexeket használtuk fel. 
## Eredmények
From analysis of the landscape metrics calculated it was found that there was an increase in the degree of human disturbance and therefore a greater fragmentation of uses between 1990 and 2006. The number of patches of "Forest Semi Natural areas" and "Agricultural areas" decreased between 1990 and 2006 (Table 1). This metric can give us some indication of ecological processes increasing or decreasing relationships between populations and habitats (Viana and Aranha, 2008). Also of note is the average distance between spots, one measure that allows us to understand the degree of landscape fragmentation, the decline of "Forest and Semi Natural areas" 1990 to 2006 at the expense of increased "Artificial areas" (Table 1).

![Model to calculate landscape metrics in 1990.](./images/portugal_coimbra2.png){.align-left}

From 1990 to 2006 diversity increased, however it is known that this result is directly related to the transfer between land cover, in particular loss of "Agricultural areas" and "Forest and Semi Natural areas". The same happened with uniformity.
## Következtetés
A LecoS beépülő modul felhasználásával megállapíthatók a tájmetrikák, meg kell jegyezni, hogy a vizsgált területen töredezettségi problémákkal szembesültünk a nagy fokú emberi beavatkozásnak köszönhetően. A QGIS szoftver intuitívnak és nagyon praktikusnak bizonyult a tájmetrikák számításában, bármilyen megkötés nélkül. Valóban erős és működőképes szabadalmazott szoftver megoldás. A jövőben szeretnénk a kidolgozott eljárást felhasználni új területeken ahol az invazív fajok okoznak problémát és megfigyelni a viselkedésünket a tájban. 
## Hivatkozások
- Fidalgo, B., R. Salas, et al. (2009). \"Estimation of plant diversity in a forested mosaic landscape: the role of landscape, habitat and patch features.\" Revista Latinoamericana de Recursos Naturales 5 (2): 65-73.
- Viana, Hélder; Aranha, José (2008) - Estudo da alteração da cobertura do solo no Parque Nacional da Peneda Gerês (1995 e 2007). Análise temporal dos padrões espaciais e avaliação quantitativa da estrutura da paisagem. X Encontro de Utilizadores de Sistemas de Informação Geográfica, 14 a 16 de Maio de 2008 -- Oeiras.
- Martin Jung (2012) LecoS - A QGIS plugin to conduct landscape ecology statistics, <http://plugins.qgis.org/plugins/LecoS>.
- Olsen, L., V. Dale, et al. (2007). \"Landscape patterns as indicators of ecological change at Fort Benning, Georgia, USA.\" Landscape and urban planning 79: 137-149.
- Turner, M. G., R. Gardner, et al. (2001). Landscape ecology in theory and practice: pattern and process. New York.

## Szerzők
![André Duarte](./images/portugal_coimbra4.png){.align-left}

Ez a cikk  André Duarte közreműködésével készült 2014. júliusban. A szerző erdész mérnöki diplomával rendelkezik és mester képzést végzett szintén erdészeti területen a Coimbrai Mezőgazdasági Főiskolán. A Geopoint portugál térinformatikai továbbképzési központjában szerzett GIS ismereteket. Jelenleg a Grupo Portucel Soporcel portugál papírgyárban közreműködik.
