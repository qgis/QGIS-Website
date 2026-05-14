---
draft: 'true'

---
# QGIS naudojimas FTTH/GPON tinklo planavimui Europos Skaitmeninio Plano įgyvendinimui
## Problemos apibrėžimas
Per paskutinius kelis metus daugelis ES šalių pradėjo vykdyti programas, Europos Skaitmeninės Iniciatyvos (EAC), 2010 metais vystytos Europos Komisijoje, įgyvendinimui. Pagal jos gaires, iki 2020 metų kiekvienas Europos Sąjungos pilietis privalo turėti prieigą prie 30 Mbps Interneto ir bent pusė jų turi turėti prieigą, ne lėtesnę už 100 Mbps.

Lenkija yra viena iš šalių, kur diegiamos šitos gairės. Naudodamos Europos Sąjungos lėšas daug vietinių operatorių gali konkuruoti su dideliais telekomunikacijų teikėjais didelio greičio plačiajuosčio ryšio paslaugose. Deja, finansavimo prašymui reikia daug darbo, norit paruošti reikiamą dokumentaciją, įskaitant, be kitų dalykų, planuojamų FTTH (laidas iki namų) tinklų konceptualius žemėlapius.

Dar daugiau, šiuo metu nėra GIS IT įrankių, padedančių potencialiems naudos gavėjams ruošiant dokumentaciją. Problema yra dar sudėtingesnė dėl fakto, kad tokia programinė įranga turėtų leisti kurti dokumentaciją pagal konkrečias programos gaires (pvz. reikalavimas prijungti mokymo įstaigas).

Kadangi mes turime didelę patirtį telekomunikacijos pramonėje, įmonės, duodančios paraišką ES finansavimui, prašė mūsų sukurti programinę įrangą, palaikančią FTTH tinklų koncepcinių žemėlapių kūrimą. Sukurtos programinės įrangos sukurti produktai turėjo stipriai pagreitinti paraiškų paruošimo procesą.
## Sprendimo aprašymas
Dėl didelio programinės įrangos populiarumo, plataus prieinamumo, atvirumo ir plačių funkcinių galimybių, atrodė natūralu pasirinkti QGIS, kaip mūsų sprendimo bazinę platformą.

Pagal Europos Tarybos FFTH gaires, ypač svarbu visų pirma paruošti planą, kuriame būtų tiek techniniai aspektai (kablių vietos, dalinimai, galai), tiek ekonominis aspektas (paklausa), paruošti pagal realius adresų taškų duomenis. Pastatų struktūra ir pastatų vystymo tankis sprendžia GPON (Gigabit Passive Optical Network) tinklo dizainą. Norint turėti galimybę efektyviai planuoti tinklo topologiją, reikia be kitų dalykų turėti ir:
- prieigą prie GIS duomenų,
- GIS duomenų apdorojimo automatizavimą,
- tinklo optimizavimo algoritmų taikymą,
- GPON tinklo inžinerinių taisyklių taikymą.

Visi šie elementai buvo sujungti QGIS platformoje. Žemiau yra trumpas aprašymas, kaip mes įgyvendinome projektą ir kokiu funkciniai elementai buvo įtraukti kuriant vieną sprendimą.

Kad pasiektume mūsų tikslą, mums reikėjo kelių funkcinių komponentų, neskaitant standartinės GIS platformos:
- GRASS - vektorinių ir tinklo algoritmų rinkinio,
- QGIS priedų - OpenLayers, QuickOSM, Scipy Point Clustering, WorkContextTracer (mūsų priedas),
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - vietinės duomenų bazės įvesties ir išvesties duomenų saugojimui.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](./images/poland_ffth/toolbox.png){.align-left}

Siekiant išvengti situacijos, kai tolimesnių analizių rezultatai susipainioja, mes teikiame priedą WorkContextTraces, kuris grupuoja mūsų darbą taip vadinamuose darbo kontekstuose.

![](./images/poland_ffth/workorder.png){.align-left}

Tinklų algoritmai, kurie remiasi GRASS teikiamomis funkcijomis, buvo praturtinti pridedant telekomunikacijų scenarijus. Mes pridėjome paklausos spiečių koncepciją, kuri leidžia naudoti tiek K-means, tiek ir hierarchinius metodus paklausos taškų agregavimui.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

Operatoriams taipogi reikėjo ryšių tarp sukurtų tinklo mazgų ir adresų taškų, kad galėtų įvertinti kiekvienos konkrečios tinklo šakos kainą. Kad būtų galima įvykdyti šią užduotį, mes sukūrėme scenarijus, kurie vykdo šį veiksmą įrašant rezultatus į vietinę SpatiaLite duombazę. Duomenis turi būti galima įrašyti į skaičiuoklę, todėl šiam reikalavimui įgyvendinti naudojame atvirą programinės įrangos biblioteką.
## Kaip naudotojai naudojo įrankį, kad sukurtų FTTH/GPON tinklo planą
Naudotojai pradeda darb1 atidarydami nauj1 darbo kontekstą ir nurodydami įvesties adresų taškų sluoksnį, kurį reikia analizuoti. Naudojant standartinę QGIS naudotojo sąsają, naudotojas gali nustatyti aibę reikalavimų adresų taškams ir galu gale pateikti tolimesniems algoritmo žingsniams reikiamus parametrus.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

Neturint informacijos apie esamą civilinę infrastruktūrą, kaip maršrutizavimo sluoksnis buvo naudojamas filtruotas OpenStreetMap kelių tinklas. Scipy algoritmams buvo pateikti įvesties parametrai, adresų taškai sudėti į spiečius paklausos agregatams, pažymint juos atskira spalva, rodančia jų priklausymą konkrečiam spiečiui.

![](./images/poland_ffth/step1.png){.align-left}

Sukūrus visų adresų taškų spiečius, naudotojas pradėjo aukštesnio lygio tinklo planavimo žingsnius, nurodant sluoksnius, paruoštus ankstesniuose žingsniuose ir sluoksnį su GPON tinklo pradiniu tašku.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](./images/poland_ffth/step4_results.png){.align-left}

Šiuo metu naudotojas jau turėjo visas dalis informacijos, iš kurios reikia kurti aukšto lygio FTTx tinklo techninę koncepciją. Paskutinė dalis buvo sukurti duomenų ataskaitą, rodančią visus suskaičiuotus duomenis iš kelių skirtingų perspektyvų.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Išvada
QGIS platformos ir jos priedų galimybių dėka, mes sugebėjome sukurti atviro kodo sprendimą, leidžiantį telekomunikacijų operatoriams paruošti dokumentus, kurių reikia pateikiant paraišką ko-finansavimui ES programai, įgyvendinančiai Europos Skaitmeninį Planą.

Kombinuojant lanksčiu vektorių algoritmus su telekomunikacijų inžinerijos scenarijais mes įgalinome praktinį matematinių algoritmų naudojimą sprendžiant realias problemas, susijusias su telekomunikacijų tinklų planavimu. Naudotojas veikia suprantamoje duomenų apimtyje (savivaldybės, pastatai, keliai), kur šios informacijos transformacija į matematinį modelį yra paslėpta nuo naudotojo.

Naudotojai gavo daug naudos:
- Automatinį GPON tinklo plano kūrimą pagal viešai prieinamus duomenis ir GPON technologijos inžinerines taisykles.
- Galimybę tinkinti įrankį pagal specifines ES programos gaires konkrečioje šalyje.
- Didelį rezultatų tikslumą, atitinkantį realias dimensijas.
- Generavimą duomenų, kurie reikalingi teikiant paraišką ES finansavimui: tinklo koncepcinis žemėlapis, kabelių ir sandūrų uždarymų ataskaita su aptarnavimo zonų priskyrimu.
- Galimybę tiksliai nustatyti kiekvienos tinklo dalies konstrukciją ir nusidėvėjimo kainas, skaičiuojant kiekvieno adresų taško prijungimo kainą.
- Galimybę prioritetizuoti adresų taškus nuo pelningiausių iki nepelningų.
- Galimybę įvertinti bazinius ekonominius indikatorius, tokius kaip ROI, NPV.

## Naudingos nuorodos ir bibliografija
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Autoriai
Sprendimas yra pilnai atviro kodo įrankis. Jis yra dalis didesnio projekto, paremto QGIS ir FreeCAD platformomis, kuris turi tikslą būti naudojamu telekomunikacijos pramonėje.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.
