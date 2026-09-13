---
draft: 'true'

---
# Utilizarea QGIS pentru planificarea rețelei FTTH/GPON ca urmare a implementării Agendei Digitale Europene
## Definirea problemei
În ultimii ani, multe țări UE au lansat programe operaționale pentru implementarea Agendei Digitale Europene (EAC), dezvoltate de Comisia Europeană în 2010. Conform orientărilor sale, până în 2020 fiecare cetățean al Uniunii Europene ar trebui să aibă acces la o lățime de bandă de internet de 30 Mbps, iar cel puțin jumătate dintre aceștia vor avea acces la o lățime de bandă nu mai lentă de 100 Mbps.

Polonia este una dintre țările în care Agenda este implementată. Datorită fondurilor Uniunii Europene, mulți operatori locali pot concura cu marii furnizori de telecomunicații, în ceea ce privește serviciile de bandă largă de mare viteză. Din păcate, aplicarea pentru finanțare necesită multă muncă, necesară pentru a întocmi documentația adecvată, inclusiv, printre altele, a dezvoltării hărților conceptuale ale rețelei FTTH (Fiber To The Home) planificate.

Mai mult, în prezent nu există instrumente IT bazate pe GIS care să sprijine potențialii beneficiari în pregătirea documentației. Complexitatea problemei se datorează faptului că un astfel de software ar trebui să permită crearea documentației în conformitate cu liniile directoare specifice programului (de exemplu, obligația de a conecta instituțiile de învățământ).

Deoarece avem o vastă experiență în industria telecomunicațiilor, entitățile care solicită fonduri UE ne-au cerut să creăm software care să sprijine dezvoltarea hărții conceptuale a rețelei FTTH. Produsele generate de software-ul dezvoltat au avut rolul de a accelera semnificativ procesul de pregătire a aplicației.
## Descrierea soluției
Datorită popularității ridicate, disponibilității pe scară largă, deschiderii software-ului și abilităților funcționale imense, a fost firesc să selectăm QGIS ca platformă care să servească drept bază pentru soluția noastră.

Conform liniilor directoare ale FTTH Council Europe, este crucial să se pregătească mai întâi un plan care să ia în considerare atât aspectul tehnic (plasarea cablurilor, îmbinărilor, spliterelor) cât și aspectul economic (cererea) pe baza adreselor reale. Structura clădirilor și densitatea dezvoltării clădirilor determină tehnologia de proiectare a rețelei GPON (Gigabit Passive Optical Network). Pentru a avea capacitatea de planificare eficientă a topologiei rețelei, sunt necesare, printre altele:
- accesul la datele GIS,
- automatizarea procesării datelor GIS,
- aplicarea algoritmilor de optimizare a rețelei,
- aplicarea regulilor de inginerie de rețea GPON.

Toate aceste articole au fost conectate în platforma QGIS. Mai jos este o scurtă descriere a modului în care s-a realizat proiectul și ce elemente funcționale au fost încorporate pentru a crea o singură soluție.

Pentru a ne atinge obiectivul, am avut nevoie de câteva componente funcționale, în afară de platforma GIS standard:
- GRASS - o colecție de algoritmi vectoriali și de rețea,
- QGISPluginuri QGIS - OpenLayer, QuickOSM, Scipy Point Clustering, WorkContextTracer (plugin-ul nostru),
- QGIS modeler -- tool for graphical flow modelling,
- SpatiaLite - o bază de date locală pentru stocarea datelor de intrare și de ieșire.

The entire solution was based on the concept of so called wizards which realize the process of preparing the FTTx network technical concept step by step. Using \'geoprocessing\' modeller, we created models requiring only the necessary input data from operator. Algorithmic complexity was encapsulated within models in the form of designed flow, which use existing QGIS algorithms and calls dedicated scripts.

![](./images/poland_ffth/toolbox.png){.align-left}

Pentru a preveni confundarea rezultatelor analizelor ulterioare, am elaborat un plugin numit WorkContextTracer, care grupează munca noastră în așa-numitele contexte de lucru.

![](./images/poland_ffth/workorder.png){.align-left}

Algoritmii de rețea, bazați pe funcțiile grafice disponibile în GRASS, au fost îmbogățiți prin adăugarea scrípturilor de telecomunicații. Am introdus un concept de grupare a cererii, care permite utilizarea atât a K-means, cât și a metodelor ierarhice de agregare a punctelor cererii.

Geoprocessing scripts with usage of cable routing layer and Djikstra algorithm develops a cable route proposal with optical fiber nodes\' locations.

De asemenea, operatorii aveau nevoie de o asociere între nodurile de rețea create și punctele de adresă, pentru a estima costul individual al fiecărei ramuri de rețea. Pentru a finaliza această sarcină, am creat scrípturi care efectuează această operațiune, stocând rezultatele în baza de date locală SpatiaLite. Datele trebuiau să fie exportabile în foaie de calcul, așa că am folosit biblioteca de software gratuită pentru a îndeplini această cerință.
## Cum au folosit utilizatorii instrumentul, pentru a crea un plan de rețea FTTH/GPON
Utilizatorul a început lucrul prin deschiderea unui nou context de lucru și prin specificarea unui strat de intrare, cu punctele adreselor care urmează a fi analizate. Folosind interfața standard QGIS, utilizatorul putea stabili un set de cerințe pentru punctele adreselor și, în cele din urmă, putea furniza parametrii necesari pentru etapele ulterioare ale algoritmului.

![](./images/poland_ffth/step1_inputlayer.png){.align-left}

Fără a avea informații despre infrastructura civilă existentă, a fost folosită, ca strat de rutare, o rețea de drumuri OpenStreet, filtrată corespunzător. Algoritmii Scipy alimentați cu parametrii de intrare, au grupat punctele de adresă în cereri agregate, marcându-le cu o culoare separată și indicând alocarea lor către un anumit cluster.

![](./images/poland_ffth/step1.png){.align-left}

Având grupate toate punctele de adrese, utilizatorul a inițiat pașii de planificare a rețelei la nivel înalt, furnizând straturile pregătite în pașii anteriori și un strat cu punctul de plecare al rețelei GPON.

![](./images/poland_ffth/step1-2_result.png){.align-left}

Upon the completion of the algorithm, in QGIS there are geometry objects representing planned cables and splice closure locations. Basing on demand data and network topology, an additional information is stored in database such as the length of the cable, its profile, node's serving areas.

![](./images/poland_ffth/step4_results.png){.align-left}

În această etapă, utilizatorul avea deja toate informațiile pentru a dezvolta un concept tehnic de rețea FTTx de nivel înalt. Partea finală a fost generarea foii de calcul a raportului de date, care arată toate datele calculate din diverse perspective.

![](./images/poland_ffth/report_generated.png){.align-left}

![](./images/poland_ffth/report_generated_and_tranformed.png){.align-left}
## Concluzii
Datorită utilizării platformei QGIS, precum și capacităților sale de extindere, am reușit să dezvoltăm o soluție open source gratuită, care permite operatorilor de telecomunicații pregătirea documentelor necesare depunerii cererii de cofinanțare în programul UE de implementare a Agendei Digitale Europene.

Prin combinarea algoritmilor vectoriali flexibili cu scrípturile de inginerie de telecomunicații, am permis utilizarea practică a algoritmilor matematici în rezolvarea problemelor reale, privitoare la planificarea rețelelor de telecomunicații. Utilizatorul operează pe un domeniu de date ușor de înțeles (municipiu, clădire, drum), în timp ce transformarea acestor informații într-un model matematic este ascunsă.

Utilizatorul obține mai multe beneficii:
- Dezvoltarea automată a planului de rețea GPON, pe baza datelor disponibile public și a regulilor de inginerie ale tehnologiei GPON.
- Abilitatea de personalizare a instrumentului, după cerințele specifice ale programului UE dintr-o anumită țară.
- Acuratețea mare a rezultatelor, conform dimensiunilor reale.
- Generarea datelor necesare la aplicarea pentru fonduri UE: hartă conceptuală de rețea, raport de închidere a cablurilor și a îmbinărilor, cu atribuirea zonelor deservite.
- Posibilitatea de a determina cu precizie costurile de construcție și amortizare pentru fiecare parte din rețea, cu calculul costului de conectare a fiecărui punct de adresă.
- Posibilitatea de a prioritiza punctele de adresă, de la cele mai profitabile la cele neprofitabile.
- Posibilitatea de a evalua indicatorii economici de bază precum ROI, NPV.

## Legături utile și bibliografie
- <http://europa.eu/rapid/press-release_MEMO-10-200_en.htm> - information on European Digital Agenda
- <http://www.ftthcouncil.eu/> - FTTH Council Europe website
- <https://www.scipy.org/> - SciPy project website
- <https://ksavinetworkinventory.com/en/download-geospatial-network-inventory-free/>
  - tool download webpage.

## Autori
Soluția este un instrument open source complet gratuit. Face parte dintr-un proiect mai amplu bazat pe platformele QGIS și FreeCAD, care intenționează să fie utilizat în industria telecomunicațiilor.

The author of this QGIS based solution is Softelnet (<https://www.softelnet.com>), a company manufacturing and integrating software for the telecommunications industry for over 15 years.
