---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS în fruntea aplicațiilor FOSSGIS guvernamentale din Cantonul Solothurn,
  Elveția
type: case-study

---
{{<content-start >}}
# QGIS în fruntea aplicațiilor FOSSGIS guvernamentale din Cantonul Solothurn, Elveția
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

Cantonul Solothurn oferă servicii și infrastructură pentru cei 250.000 de locuitori. În anul 2001, Parlamentul de Stat a decis să migreze de la Windows la Linux. Motivațiile au fost independența față de un singur furnizor, încurajarea liberei inițiative și reducea costurilor de licență. Ca urmare, departamentul SO!GIS din Cantonul Solothurn și-a formulat cerințele GIS pentru cei peste 3500 de angajați, într-o strategie FOSSGIS.

Primul pas a fost introducerea UMN MapServer și crearea clientului SO!MAP, care oferă un acces WebGIS facil pentru toți cei 3500 de angajați. Al doilea pas a fost migrarea tuturor datelor noastre geospațiale din fișiere shape în motorul de baze de date spațiale PostGIS. Deși migrarea a avut un mare succes, lipsea, totuși, o aplicație desktop GIS ușor de utilizat.

După o evaluare a diferitelor aplicațiilor GIS Desktop am decis să utilizăm QGIS în conjuncție cu GRASS, înlocuind ESRI ArcInfo și ArcView3 în anul 2006.

Decizia a fost determinată de următoarele aspecte:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Înființarea proiectului OSGeo
- Intefață grafică tradusă în limba germană
- Documentație scrisă în limba germană
- Un dezvoltator activ (Marco Hugentobler) în apropiere de Solothurn, Elveția.
- Am fi putut contracta la Marco Hugentobler implementarea facilităților lipsă/mai puțin dezvoltate cum erau digitizarea și compunerea hărților.
- Dezvoltare de aplicații și plugin-uri cu Python
- Comunitatea de utilizatori în creștere
- Comunitatea de dezvoltatori foarte activă
- Independența față de un singur sistem de operare

## Unde folosim QGIS
Spre deosebire de hărțile interactive deservite de UMN MapServer, GIS desktop oferă o imagine flexibilă datelor geospațiale din Solothurn. QGIS Desktop GIS este utilizat de mai mult de 50 de utilizatori în munca lor de zi cu zi. Dar mulți dintre ei nu sunt experți GIS. Ei doresc să vizualizeze și/sau să înregistreze date geospațiale, printr-o interfață intuitivă. 

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

Aceasta cuprinde un inventar de modele de date, inteligibil pentru utilizatorul care nu este expert în GIS, dându-i posibilitatea să caute aici informațiile de care are nevoie.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Concluzii
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Autor
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Acest articol a fost transmis în mai 2009 de către Dr. Horst Düster. El este coordonatorul GIS la Departamentul de Geoinformații din cantonul Solothurn, Elveția.

{{<content-end >}}
