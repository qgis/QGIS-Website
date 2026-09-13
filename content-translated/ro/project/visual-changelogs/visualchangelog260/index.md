---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.6{#changelog26 }
Data lansării: 2014-10-31

Jurnalul schimbărilor pentru versiunea QGIS 2.6.0. S-au adăugat multe caracteristici noi, reglaje și îmbunătățiri, pentru a face cel mai popular GIS desktop, gratuit cât mai complet și util.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Dorim să le mulțumim dezvoltatorilor, tester-ilor, autorilor documentațiilor și tuturor acelor persoane care, în mod voluntar, au consumat timp și efort (sau au finanțat alte persoane în acest scop).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

În fine, am dori să mulțumim sponsorilor noștri oficiali pentru sprijinul financiar de neprețuit, pe care l-au oferit acestui proiect:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS este un soft gratuit iar dvs. nu aveți obligația de a plăti pentru folosirea lui - de fapt, vrem să încurajăm oamenii de pretutindeni să-l folosească, indiferent de starea financiară sau socială - având convingerea că, oferind utilizatorilor posibilități de decizie spațială, vom obține o societate mai bună.

{{<table-of-contents >}}
## Generalități
### Funcționalitate: Numele fișierului proiectului apare în Proprietăți
De acum, se poate vedea calea completă pentru fișierul proiectului în fereastra de dialog a proprietăților proiectului.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Funcționalitate: Del/Backspace elimină ultimul punct dintr-o măsurătoare
De acum, când măsurați suprafețele sau distanțele, puteți elimina nodurile nedorite de pe linia de măsurare folosind tastele Delete sau Backspace.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Funcționalitate: Selectarea entității corespondente de pe hartă prin intermediul widget-ului de relații
### Funcționalitate: Widget-uri de editare
S-au adus o serie de îmbunătățiri la widget-urile de editare:
- nou widget de editare pentru dată/oră, capabil să afișeze datele nule
- editarea liniei de filtru
- Manipularea corespunzătoare a valorilor NULL de către widget-urile de editare
- Widgetul foto păstrează valoarea NULL
- Widgetul web păstrează valoarea NULL
- Tabelul de atribute poate distinge între 0 și NULL
- Adăugare suport pentru sufix pentru widget-ul gamă

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Funcționalitate: Folosiți în mod opțional doar un subset de câmpuri din stratul alăturat
De acum, pentru crearea unei uniuni vectoriale, se poate utiliza doar un subset de câmpuri conexe.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Funcționalitate: Câmp de expresii (câmpuri virtuale)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Funcționalitate: De acum, acțiunile pot avea asociată o pictogramă
Când creați o acțiune personalizată pentru un strat vectorial, puteți defini acum o pictogramă care să fie utilizată, de asemenea, pentru acțiune.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Funcționalitate: Diverse opțiuni și tipuri de expresii suplimentare
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Funcționalitate: Se pot inversa clasele din cadrul renderelor clasificate pe grade și categorii
De acum, puteți alege să dezactivați anumite clase din renderele organizate pe grade și categorii, fără a le elimina efectiv.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Funcționalitate:  Îmbunătățiri aduse legendei
Cea de-a doua fază de revizuire a legendei / cuprinsului s-a finalizat. Aceasta include:
- Curățare API (pentru dezvoltatori)
- Vizibilitatea grupurilor prezente în arborele straturilor. Acest nou buton al bării de instrumente permite modificarea rapidă a grupurilor de straturi care ar trebui să fie vizibile.
- Abilitatea de a gestiona grupurile cu straturi prin intermediul barei de instrumente a legendei
- Noua opțiune de filtrare, din bara de instrumente a legendei, va elimina elementele legendei pentru orice clase care nu sunt prezente în suprafața vizualizată. Acesta este un avantaj major, deoarece garantează că legenda hărții nu conține intrări pentru elementele care nu sunt prezente, în mod curent, în harta vizualizată. Această opțiune este disponibilă pentru legenda hărții principale, în compozitor și pentru straturile WMS.
- Legendele renderelor bazate pe reguli pot fi afișate într-un pseudo-arbore

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Furnizorii de Date
### Funcționalitate: Îmbunătățiri aduse exportului DXF
- vedere de tip arbore și selecție atribut pentru atribuirea stratului în fereastra de dialog
- posibilitate de umplere a poliguanelor/HAȘURĂ
- reprezentarea textelor ca MTEXT în loc de TEXT (incluzând tipul, înclinația și grosimea fontului)
- support for RGB colors when there\'s no exact color match
- se folosește AutoCAD 2000 DXF (R15) în loc de R12
- eliminarea metodelor de testare R18

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Compozitorul de Hărți
### Funcționalitate: Controlul asupra ascunderii elementelor hărții din compozitor
S-a adăugat o casetă de bifare și un buton definit cu ajutorul datelor, pentru specificarea elementelor care vor fi excluse hărțile compozitorului. Dacă elementul nu este bifat, el va fi vizibil doar la momenul creării compoziției.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Funcționalitate: Control asupra tipăririi paginilor pentru cadrele albe ale compozitorului
Pentru tabelele sau cadrele HTML, o casetă de bifare specifică dacă se va exporta conținutul paginii atunci când cadrul este gol.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Funcționalitate: Panoul arborelui cu elemente
Panoul arborelui cu elemente, din compozitorul de hărți, permite selecția elementelor, ascunderea/afișarea acestora, inversarea stării de blocare a elementelor precum și editarea id-ului  elementului prin efectuarea unui dublu-click pe acesta. Puteți utiliza, de asemenea, drag and drop pentru a reordona elementele.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Funcționalitate: Mai mult control asupra aspectului săgeților/liniilor din compozitor
- Liniile pot fi stilizate folosindu-se dialogul de stilizare a simbolurilor pentru linii
- Utilizatorul poate defini culorile de umplere ale vârfului și a conturului săgeților
- Utilizatorul poate defini dimensiunea conturului săgeților

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Funcționalitate: Control definit cu ajutorul datelor, pentru elementele compozitorului
Multe proprietăți ale elementelor compozitorului pot fi de acum controlate cu ajutorul datelor. Printre acestea sunt incluse:
- Transparența și modul interacțiunii pixelillor.
- Rotaţia elementului.
- Scara, limitele și rotația hărții.
- Geometria marginii atlasului.
- Poziția și mărimea elementului.
- Dimensiunea paginii, orientarea și numărul paginilor.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Funcționalitate: Imaginile compozitorului se pot afla la distanță, fiind specificate ca URL-uri
De acum, elementele de tip imagine din compozitorul de hărți, acceptă URL-uri de la distanță ca sursă pentru imagini. Această sursă poate fi, de asemenea, definită cu ajutorul datelor.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Funcționalitate: Îmbunătățiri aduse tabelelor din Compozitor
- De acum, se pot seta antetul tabelului și culorile fontului conținutului.
- Tabelele pot fi împărțite de-a lungul mai multor cadre, permițând conținutului lor să fie distribuit pe coloane sau pe diferite pagini.
- S-a adăugat opțiunea de a se afișa anteturile în primul cadru, în toate cadrele, sau fără cadre.
- Se permite controlul manual al lățimii coloanelor.
- Noi opțiuni pentru sursa tabelelor, inclusiv pentru atlas și pentru entitățile copil dintr-o relație.
- Stabilirea comportamentului tabelelor goale, incluzând ascunderea întregului tabel, afișarea celulelor goale, sau afișarea unui set de mesaje în interiorul tabelului.
- Adăugarea unei o casete de bifare pentru a filtra acelor entități din tabel care intersectează atlasul curent.
- S-a adăugat o casetă de bifare pentru eliminarea rândurilor duplicate dintr-o tabelă.

Rețineți că tabelele din proiectele existente nu sunt actualizate automat la noul format de tabel care acceptă aceste caracteristici, de aceea tabelele trebuie să fie reinserate într-o compoziție pentru a vedea noile setări.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Funcționalitate: Îmbunătățiri generale aduse compozitorului
Compozitorului de hărți (utilizat pentru a crea hărți imprimabile) i s-au adus o serie de îmbunătățiri în QGIS 2.6.
- De acum, se poate schimba culoarea de umplere secundară pentru scările grafice
- Ținându-se apăsată tasta SHIFT în timp ce se desenează elementele de tip linie/săgeată, constrânge desenarea lor orizontală, verticală sau la un unghi de 45 grade
- Ținându-se apăsată tasta SHIFT, în timp ce se desenează alte noi elemente, vor rezulta pătrate, iar reținându-se ALT ele vor fi desenate dinspre centru
- Clic dreapta nu mai blochează/deblochează elementele, acest lucru fiind gestionat acum de către noul panou de elemente. Articolele blocate nu mai pot fi selectate din canevasul compozitorului, permițându-se interacțiunea cu elementele de sub ele.
- Reținându-se ALT, în timp ce se apasă tastele cursorului, rezultă o deplasare a elementelor cu 1px
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Funcționalitate: Acroșaj îmbunătățit al elementelor
Pragul de acroșare este de acum stabilit în pixeli, pentru a permite o mișcare și o redimensionare mai fină a elementelor, atunci când o compoziție este mărită. Elementele din cadrul unui grup nu mai sunt folosite pentru liniile cu auto-acroșare.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Funcționalitate: Multiple vederi de ansamblu pentru o hartă
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Funcționalitate:  Îmbunătățiri pentru codul HTML din elemente
Există o serie de noi opțiuni utile pentru elementele HTML din compozitor:
- Posibilitatea de specificare manuală a sursei HTML
- Expresiile QGIS din interiorul sursei HTML pot fi evaluate înainte de randarea conținutului HTML
- Definire cu ajutorul datelor pentru URL-ul sursei HTML
- Posibilitate de a crea un stil propriu, care să suprascrie stilurile HTML

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Funcționalitate: Îmbunătățiri aduse grilei hărții din compozitor
- De acum, puteți avea mai multe grile cu proprietăți diferite.
- Puteți mixa grilele reproiectate cu cele Lat/Long.
- Se poate utiliza simbologia QGIS standard pentru linii, grile etc.
- Există noi cadre/adnotări numai de stil grilă. Selectând acest stil, se vor desena doar cadrul și adnotările, fără linii de grilă sau alte marcaje peste hartă.
- Există de acum opțiuni pentru controlul părții unei hărți pe care este desenat un cadru.
- Există noi stiluri pentru cadre, cu opțiuni pentru caneluri interne, externe, sau ambele.
- S-au adus îmbunătățiri la adnotările grilelor, inclusiv mai multe formate noi pentru adnotări.
- Adnotările grilelor folosesc de acum simboluri tipografice prime și duble, corecte.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Procesare
### Funcționalitate: Colecție de modele și scrípturi on-line
Modelele și scrípturile pot fi descărcate și instalate din colecțiile online, direct din interfața de procesare. Colecția va fi extinsă cu noi scrípturi și modele oferite de utilizatorii Processing.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Funcționalitate: Implementarea unui modelator nou
Modelatorul a fost rescris, iar acum oferă funcționalități suplimentare, cum ar fi acceptarea modelelor fără nici o limită de adâncime. Modelele sunt acum stocate ca fișiere JSON. Compatibilitatea este păstrată, astfel încât toate modelele pot fi folosite în continuare. De asemenea, puteți de acum să glisați și să fixați elementele din intrări și algoritmii pe modelatorul grafic.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programabilitate
### Funcționalitate: Schimbări API pentru widget-urile QGIS 
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Server
### Funcționalitate: Îmbunătățiri ale căutării care utilizează cereri GetFeatureInfo
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Funcționalitate: S-a adăugat o setare de precizie pentru atributele geometriei GetFeatureInfo
## Simbologie
### Funcționalitate: Generare mai bună a culorilor aleatorii
S-a îmbunătățit algoritmul de generare a culorilor aleatorii pentru randarea clasificată, astfel încât culorile sunt vizibil mai diferite între ele.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Funcționalitate: Îmbunătățiri aduse interfeței cu utilizatorul
- Acolo unde este posibil, proprietățile stratului simbolului sunt menținute la schimbarea tipului de strat.
- S-a adăugat un buton de editare pentru umplere de tip shapeburst și cu gradienți.
- Actualizarea automată a etichetelor și a intervalelor de vecinătate.
- Clasele sunt convertite automat începând de la clasele organizate pe categorii și pe grade, atunci când se trece la renderul bazat pe reguli.
- S-au adăugat unități și numere cu zecimale la etichetele renderului gradual.
- Reacție îmbunătățită la schimbările gamei de culori, la inversarea ei și la alte opțiuni din GUI.
- Se păstrează simbolul la comutarea între renderele simple, graduale, pe categorii, și altele.
- Etichetare îmbunătățită a modului de calcul StdDev.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Interfața cu Utilizatorul
### Funcționalitate: Evidențierea sintaxei din editorul de cod
Pentru editoarele de scrípturi python, constructorul de expresii, fereastra filtrului, compozitorul HTML și editoarele CSS

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Funcționalitate: Palete de culori
Puteți defini de acum propriile palete de culori, pentru utilizarea în QGIS.
- Posibilitate de personalizare a paletei de culori globale (în opțiunile ferestrei de dialog).
- Paletă de culori per proiect (în fereastra de dialog a proprietăților proiectului).
- Culorile sunt afișate sub formă de meniuri cu butoane colorate și în noua fereastră de dialog a selectorului de culoare.
- Puteți importa/exporta culorile într-un fișier GPL, de tip paletă.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Funcționalitate: Noul dialog al selectorului de culoare
Există un nou dialog personalizat de selectare a culorii în QGIS. Caracteristicile acestuia includ:
: - Butoane glisante pentru nuanță, saturație, valoare, culorile roșu, verde și albastru.
  - Buton glisant pentru transparență.
  - Opțiune de copiere/lipire coduri de culoare html (în diverse formate).
  - Previzualizare culoare înainte/după, cu previzualizare transparență.
  - Widget interactiv, 2D, pentru rampa de culoare.
  - Widget rotund/triunghiular pentru nuanță.
  - S-au introdus palete de culori editabile, inclusiv abilitatea de a crea noi palete, și importul/exportul culorilor către un fișier GPL, de tip paletă.
  - Selectare a culorii în timp real, cu posibilitate de probare pe o rază presetată (în funcție de SO).
  - Suport pentru interacțiunea cu alte aplicații prin intermediul drag and drop pentru culori (în funcție de SO).
  - Opțiunea de a dezactiva fereastra de dialog și de a se folosi fereastra de selectare nativă.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Funcționalitate: Instrumentul de selecție a unei entități singulare a fuzionat cu selectarea după un dreptunghi
Instrumentul de selecție singulară s-a îmbinat cu instrumentul de selecție dreptunghiulară. Dacă se dorește selectarea unui singur element, pur și simplu se activează instrumentul dreptunghiular și apoi se efectuează un singur clic pe entitate (în locul trasării unui dreptunghi).

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Funcționalitate: Comportamentul comenzii de adăugare a unui strat la canevas
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Funcționalitate: S-au adăugat pictograme cu mărimi de 48 și 64
Pentru cei care folosesc QGIS pe dispozitivele cu exran tactil (sau cărora le plac pictogramele mari), de acum se pot seta pictogramele de până la 64 x 64 pixeli.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Funcționalitate: Butoane cu noi culori
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Funcționalitate: Meniu contextual pentru instrumentul de identificare
Când se utilizează instrumentul de identificare, se poate face clic dreapta pe canevas pentru a se utiliza instrumentul de identificare în mod contextual. În meniul care apare, puteți defini ce tipuri de entitate doriți să identificați (sau toate, dacă doriți).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
