---
draft: 'true'

---
# Apdorojimo įrankinės naudojimas sniego klasifikavimo automatizavimui
Snowy Hydro Limited (SHL) - tai piko elektros generatorius, esantis Snowy Mountains, New South Wales, Australijoje. Nepaisant to, kad Snowy Hydro Limited turi daug įvairių generatorių visoje šalyje, ji geriausiai žinoma už žymų Australijos infrastruktūros gabalą - Sniego kalnų hidroelektrinių schemą.

Sniego kalnų hirdoelektrinių schemai veikti leidžia sezoninis snygis Naujojo Pietų Velso alpių regione. Pavasarinio sniego vanduo naudojamas piko elektros generavimui nacionalinėse elektros rinkose, tuo pačiu vandenį nukreipiant į sausesnes Pietrytinės Australijos vietas drėkinimui ir žemdirbystei.

Sniego dangos klasifikavimas žiemos mėnesių metu leidžia SHL stebėti sniegu padengtų plotų gyvavimo ciklą, archyvuoti padengimo istorinius įrašus, teikti padengimo statistiką hidrografijos paslaugos komandai vandens gavimo ir saugojimo prognozėms.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Bendra informacija
Kiekvienų metų žiemos mėnesiais (nuo birželio 1-os iki spalio 31-os) SHL gauna kiek galima daugiau vaizdų be debesų iš MODIS Terra (EOS AM) palydovo. Šie vaizdai pateikiami algoritmui, žinomam kaip Normalizuotas Sniego Skirtumo Indeksas (NDSI), kuris naudojamas aptinkant plotus su sniegu. Nors šis algoritmas nėra unikalus ar pririštas prie kokio nors konkretaus jutiklio, MODIS buvo pasirinktas dėl savo tinkamos erdvinės raiškos ir kasdieninio projekto ploto padengimo (Žemėlapis 1.1 Sniego vandens baseinai).
## Tikslas
Šio projekto tikslas yra automatizuoti NDSI procesus kaip QGIS apdorojimo įrankinės modelį. Reikiama išvestis yra vektorinis poligonas, rodantis sniegu padengtą plotą Sniego vandens baseine, kartu su atributais, aprašančiais visą padengtą plotą kvadratiniais kilometrais.
## Metodas
Pats NDSI algoritmas yra gan paprastas (rodomas žemiau Formulėje 1.1 - Normalizuotas Sniego Skirtumo Indeksas (NDSI)), o tolimesni reikiami žingsniai ištraukia sniego padengimą vektoriniu formatu, kuris taip pat puikiai tinka apdorojimo įrankinės modeliui.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

NDSI algoritmas grąžina rezultatus tarp -1 ir 1, sniego ribinė reikšmė paprastai būna didesnė už 0,4. Žemiau pateikiamas NDSI išvesties pavyzdys (Žemėlapis 1.3 - NDSI išvestis), kartu su natūralių spalvų vaizdu (Žemėlapis 1.2 MODIS tikros spalvos) 2014 liepos 13. Kaip matome šiuose rezultatuose, NDSI išvestis labai gerai atskiria plotus padengtus sniegu nuo kitų dangos tipų ir debesų. Kaip ten bebūtų, jis gali neteisingai klasifikuoti didelius vandens telkinius kaip sniegą, kadangi vanduo turi panašias absorbavimo charakteristikas spektre artimam infraraudonajam. Ši NDSI charakteristika rodo poreikį įtraukti vandens šabloną kažkuriame modelio etape.

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
## Rezultatai/Išvados
QGIS apdorojimo įrankinė yra galingas būdas automatizuoti procesus, tokius kaip sniego klasifikavimas. Aukščiau vaizduojamas modelis sėkmingai automatizuoja sniego klasifikavimo procesą ir sukuria GIS duomenų aibę, kurią galima naudoti vaizdavimui ir kaip įvestį tolimesniems statistiniams taikymams. Jis sėkmingai pašalina subjektyvias naudotojo klaidas, susijusias su ankstesniais SHL naudotais metodais, ir tuo pačiu teikia pakartojamą ir pastovų klasifikavimo įrankį. Čia galima matyti kai kuriuos sezoninius rezultatus.
### Autorius
Andrew Jeffrey yra Snowy Hydro Limited, Cooma NSW, Australia GIS analitikas. Jis baigė Wagga Wagga Charles Sturt Universiteto mokslų bakalaurą (Bsc), o 2004 Erdvinių informacinių sistemų magistrą. Snowy Hydro Limited jis teikia erdvinę paramą įspūdingiems projektams, tokiems kaip Debesų sėjimo eksperimentui ir kasdieniams darbams organizacijoje.
