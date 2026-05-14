---
HasBanner: false
draft: false
releaseDate: '2014-06-27'
section: proiect
sidebar: true
title: Jurnalul schimbărilor pentru QGIS 2.4
type: visual-changelog

---
{{<content-start >}}
# Jurnalul schimbărilor pentru QGIS 2.4{#changelog24 }
Data lansării: 2014-06-27

Jurnalul schimbărilor pentru versiunea QGIS 2.4.0. În această versiune, accentul a fost pus foarte mult pe cizelare și performanță - s-au adăugat multe caracteristici noi, reglaje și îmbunătățiri, pentru a face interfața cu utilizatorul mai consistentă și pentru a-i conferi un aspect profesional (și, sperăm, mai ușor de utilizat). Compozitorul (folosit pentru crearea de hărți gata de imprimare), a înglobat foarte multă muncă, în scopul transformării sale într-o platformă viabilă dedicată obținerii unor rezultate cartografice deosebite.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Dorim să le mulțumim dezvoltatorilor, tester-ilor, autorilor documentațiilor și tuturor acelor persoane care, în mod voluntar, au consumat timp și efort (sau au finanțat alte persoane în acest scop).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

În fine, am dori să mulțumim sponsorilor noștri oficiali pentru sprijinul financiar de neprețuit, pe care l-au oferit acestui proiect:
- GOLD Sponsor: [Asia Air Survey, Japan](http://www.asiaairsurvey.com/)
- SILVER Sponsor: [G.A.I.A. mbH, Germany](http://www.gaia-mbh.de/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [www.eschenlaub.de, Germany](http://www.eschenlaub.de)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors).

If you would like to make a donation or sponsor our project, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. QGIS is Free software and you are under no obligation to do so. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

{{<table-of-contents >}}
## Generalități
### Feature: Generate band name with NetCDF EXTRA_DIM
NetCDF furnizează informații suplimentare dimensionale. Informațiile furnizează metadate pe fiecare bandă. Aceste metadate pot fi utilizate pentru a explica numele fiecărei benzi. De exemplu, benzile unui fișier NetCDF reprezintă temperatura la o anumită adâncime. Pentru utilizator, este mai ușor să selecteze o bandă cu informații detaliate, decât să extragă doar numărul benzii.

![image1](images/entries/becafd815f152b53503b33048beb8bc95cdfdaf6.webp)
### Funcționalitate: Aplicarea unei scări și a unui decalaj asupra datelor raster
În unele surse de date raster, datele sunt stocate ca întregi, având o scară și un decalaj în metadate. Scara și decalajul pot fi utilizate pentru a obține datele corecte. QGIS le aplică rasterului obținut pentru a furniza utilizatorilor informațiile corecte pentru legendă, histogramă și identificatorul de entități.

![image2](images/entries/9ec1681e4318f92a886405cf8215ec98068cf8ba.webp)
### Funcționalitate: Bară pentru calcule rapide, în tabelul de atribute
Există o nouă facilitate pentru cei care lucrează cu câmpuri calculate în tabelele cu atribute vectoriale. Noua bară de calcul rapid vă permite actualizarea rapidă și ușoară a valorilor dintr-o coloană a tabelului de atribute.

![image3](images/entries/386f372e4b7be45426a62005813c8d58a9a2cb43.webp)
### Funcționalitate: Previzualizarea culorilor în compozitor și pe suprafața hărții
A really innovative feature that has been added to 2.4 is support for grayscale and colour blindness previews. This allows you to visualise how people with colour blindness will perceive your cartography and map layout, or how your map will look if it\'s printed in grayscale. You can read more about this new feature [here](http://nyalldawson.net/2014/05/colour-blindness-and-grayscale-previews-in-qgis-2-4/).

![image4](images/entries/d3d6193f1a37c8201c9be786ef798c5419eb4c79.webp)
### Funcționalitate: Fișiere QLR QGIS Layer
Added support for QGIS Layer Definition files or simply QLR (see <http://nathanw.net/2014/03/12/qgis-qlr/>). QLR file is a file that points to the data, contains all the styling, and other information. You can then just add this file and it will do all the other magic for you. QLR makes it easy to add same layer to multiple map documents, inheriting all of the properties which have been set and works with any layer supported in QGIS, expect special plugin layers.
### Funcționalitate: Noi funcții pentru expresii
Noi funcții sunt disponibile în constructorul de expresii.
- casetă de încadrare (limite)
- bounding box width & height (bounds_width/bounds_height)
-  coordonatele min/max x/y (xmin/xmax/ymin/ymax)
- noua funcție wordwrap care returnează un șir cu un număr maxim/minim de caractere per linie

![image5](images/entries/b8f4b0adf2c8f7ba8303f5aa6df8d2294a0b4c7b.webp)
### Funcționalitate: Copy, paste și drag and drop pentru culori
You can now copy, paste, drag and drop colours between any colour input widget in QGIS. See this [article](http://nyalldawson.net/2014/05/colour-shortcuts-in-qgis-2-4/) for more information on how this new feature works. Hex color codes and rgb strings can also be pasted on to colour buttons to allow importing colours from outside of QGIS.

![image6](images/entries/d2e1cdce5ed643c88f1630fa36b667e53ec8e4de.webp)
### Funcționalitate: Randarea multifir
This is one feature we simply cannot do justice to with a screenshot -QGIS now supports multi-threaded rendering! What this means is that when drawing the map, QGIS will split the drawing work between all of the cores in your CPU, making the process more efficient and responsive. By **responsive** we mean that you no longer need to wait for the map view to update before you can pan or zoom again. Also the map display updates incrementally allowing you to see if the map is positioned correctly early on in the drawing process. Take a look at [this article](http://www.lutraconsulting.co.uk/casestudies/qgis-multi-threaded-rendering) for a more detailed overview of the multi-threaded rendering system. You will find some options in the QGIS settings dialog that allow you to manage the behaviour of multi-threaded rendering.

![image7](images/entries/ebcacf7c2623f7ea3e87c929d77bfe4113c75549.webp)
## Etichetare
### Funcționalitate: Etichetarea multiplă a unei entități
Long lines (such as contour lines or roads) can now be repeatedly labeled at regular intervals. One can choose between mm and map units for specifying the repetition interval. At the time of the release there is still an issue with \"merge connected lines to avoid duplicate\" setting.

![image8](images/entries/4b996cdf33f0d18a5266e6b6053ab88d4dca9372.webp)
## Compozitorul de Hărți
### Funcționalitate: Îmbunătățiri aduse elementelor de imagine din compozitor
The image item in composer is now \'atlas friendly\' - you can use an **expression to define which image** should be shown for each atlas page. You can also now set the **resize mode** (zoom, clip, stretch etc.) for the image in relation to its frame size and dimensions. You can also specify the placement of the image relative to its frame using the new **placement** item property.

![image9](images/entries/59c029be33ba4cbdf7fb48879350e699cf5f9897.webp)
### Funcționalitate: Scări predefinite pentru atlasul cu hărți
When working with atlas map items, you can now specify a predefined scale mode for the map. It will use the best fitting option from the list of predefined scales in you your project properties settings (see Project -\> Project Properties -\> General -\> Project Scales to configure these predefined scales).

![image10](images/entries/45aa708b7c1ba7dd42bd71e3ee293349262853f7.webp)
### Funcționalitate: Tabele de atribute îmbunătățite, în compozitor
S-au adus o serie de îmbunătățiri la abilitatea de afișare a tabelelor, în ferestrele compozitorului:
- S-a adăugat suport pentru reordonarea coloanelor dintr-un tabel
- S-a adăugat suport pentru coloanele create pe baza unei expresii
- You can now set the alignment of individual table columns, and also specify the alignment for the table\'s header cells
- Conținutul unui tabel poate fi filtrat printr-o expresie

![image11](images/entries/e39937a4b6533c14856b12d4a1064425eac52a31.webp)
### Funcționalitate: Îmbunătățiri generale aduse compozitorului
O serie de îmbunătățiri fac viața mai ușoară în compozitorul de hărți, în timpul compunerii unei hărți:
- S-a adăugat un buton pentru a vedea granițele entităților de pe suportul hărții principale
- Abilitatea de a exporta imaginile SVG din compozitor, cu straturi
- Setarea stilului pentru capătul și îmbinarea liniilor, în cazul scării
- Suport pentru stabilirea stilului de îmbinare a liniilor, în cazul cadrelor

![image12](images/entries/cff24f3259e286e405ca13c94fcf5e19dbe98c64.webp)
### Funcționalitate: Îmbunătățiri ale cadrelor HTML
Cadrele HTML din compozitor au fost îmbunătățite. Există un nou buton de **adăugare cadru** care poate fi folosit pentru a crea manual mai multe cadre înlănțuite. S-a îmbunătățit, de asemenea, logica întreruperilor de pagină, scăzând probabilitatea de obținere a unei întreruperi care să treacă prin mijlocul liniilor de text, atunci când se paginează cadrele HTML.

![image13](images/entries/792d6c3cfc682d2132caec8b6be0ce30c855e39f.webp)
## Plugin-urile
### Funcționalitate: MetaSearch Catalogue Client Plugin
Metasearch este un plug-in QGIS pentru interacțiunea cu serviciile de catalogare metadate, suportând standardul Serviciului de Catalogare OGC pentru Web (CSW). Acest plug-in oferă o abordare ușoară și intuitivă, împreună cu o interfață prietenoasă, pentru căutarea în cataloagele de metadate din QGIS, acum făcând parte în mod implicit din nucleul de bază al QGIS.

![image14](images/entries/a80155cfd652a9e83c5f2564e371357a92ae115f.webp)
## Simbologie
### Funcționalitate: Umplere de tip shapeburst
We have a great new render in QGIS 2.4. The shapeburst renderer will allow you to fill polygons with a gradient extending from the line edge towards the polygon interior. You can read more about **shapeburst** [here](http://nyalldawson.net/2014/06/shapeburst-fill-styles-in-qgis-2-4/?utm_source=rss&utm_medium=rss&utm_campaign=shapeburst-fill-styles-in-qgis-2-4).

![image15](images/entries/1d85daf70119e7a58d5ef18ae5a0ac2daf18ff4f.webp)
### Funcționalitate: Opțiunea de decalare a plasamentului marcajelor de tip linie
When using a marker line along a line or polygon edge, you can now specify an **offset** so that the marker line starts a set distance from the beginning of the line. If a marker line is set to \"first vertex\" or \"last vertex\" mode, than this offset will control how far along the line from the vertex the marker is placed.

![image16](images/entries/884f1735cee30abc7024f6fc21756b8609770173.webp)
### Funcționalitate: Nou render, de tip Poligon Inversat
Un nou render a fost adăugat pentru entitățile de tip poligon, permițând stilizarea porțiunii **exterioare** a poligoanelor. Acest lucru poate fi util pentru evidențierea unor zone, sau pentru crearea de măști cartografice. Atunci când se utilizează cu noul stil, de tip shapeburst, puteți obține un rezultat similar cu cel din imaginea de mai jos.

**Observație:** Noua versiune a plugin-ului vă ajută să creați cu ușurință straturi de măști din selecția curentă, să etichetați entități doar în acele zone, și să generați o mască automată în Atlas.

![image17](images/entries/b58dd06d363524d112de7a40748f599730c4276e.webp)
### Funcționalitate: Salvarea și recuperarea stilurilor, folosind straturile Spatialite
In the previous version was possible to save style with postgres layers, now will be possible for Spatialite layers too. This functions allow to embed different styles inside a spatialite container simplifying sharing data and their presentation. A video tutorial of this funcionality can be found here <http://pvanb.wordpress.com/2014/05/15/saving-layer-styles-to-your-spatialite-database/>

![image18](images/entries/b52c9d3fab8a6281c0e8869702328521a2445994.webp)

{{<content-end >}}
