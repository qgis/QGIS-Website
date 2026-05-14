---
HasBanner: false
archived: true
date: 2011-04-01
draft: false
featured: false
section: proiect
sidebar: true
thumbnail: images/suisse_uster1.png
title: Utilizarea QGIS pentru infrastructura de date spațiale a orașului Uster
type: case-study

---
{{<content-start >}}
# Utilizarea QGIS pentru infrastructura de date spațiale a orașului Uster
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>April 01, 2011</span>
</p>

Orașul Uster folosește QGIS din 2007. Încurajată de decizia cantonului Solothurn de a utiliza QGIS ca un înlocuitor pentru ArcView, Uster a decis să facă, de asemenea, o încercare. Orașul s-a alăturat efortului de dezvoltare a cererii QGIS, sugerând și testând noi caracteristici și susținând financiar dezvoltarea. În schimb Uster a obținut o platformă GIS desktop, independentă, în evoluție rapidă, și o soluție WebGIS susținută de o comunitate mondială de utilizatori și dezvoltatori.

![](../images/suisse_uster1.png)

Postgis/PostgreSQL servește ca depozit central de date geografice. Alte baze de date și surse de date sunt replicate în PostgreSQL, la intervale regulate, folosind instrumente ca OGR și FME. La început QGIS a fost folosit în principal pentru vizualizare. Primul utilizator QGIS a fost un agricultor care a avut sarcina de a superviza declarațiile făcute de către fermierii locali pentru primirea subvențiilor agricole. Mai târziu, QGIS a fost introdus ca editor de date și platformă de publicare a hărților, datorită îmbunătățirii instrumentelor de editare și editorului de hărți. Împreună cu alți utilizatori QGIS elvețieni (Solothurn, Thun și CDE (Universitatea din Berna)) coordonăm și sponsorizăm evoluția acestor instrumente, cum ar fi unele îmbunătățiri în simbolizare, etichetare automată, manipulare a atributelor și formelor.

![](../images/suisse_uster2.png)

Administrația orașului folosește, de asemenea, aplicații GIS comerciale: Autodesk Topobase, pentru captura și editarea datelor infrastructurii cadastrale și a apelor reziduale, și GE Smallworld pentru gestionarea rețelelor de gaze, apă și electricitate. Totuși, acestea sunt sisteme expert în folosința personalului special instruit. Toate celelalte proiecte GIS și vizualizarea tuturor datelor sunt asigurate de QGIS.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](../images/suisse_uster3.png)

Astăzi, QGIS este utilizat pentru următoarele proiecte GIS:
- vizualizarea datelor apelor uzate, integrarea baze de date suplimentare și accesul direct la clipurile video ale canalelor și la protocoalele de inspecție
- vizualizarea și editarea pentru monitorizare și planificare a mediului urban și a apelor uzate și sistemelor hidrologice (germană: Genereller Entwässerungsplan)
- vizualizarea datelor cadastrale subterane (rețele de electricitate, ape uzate, apă, gaz și, mai târziu, de telecomunicații) (germană: Leitungskataster)
- vizualizarea datelor cadastrale
- vizualizarea și editarea inventarului comunal al siturilor naturale protejate
- vizualizarea și editarea datelor de planificare urbană și regională
- vizualizarea și editarea datelor infrastructurii rutiere
- vizualizarea statisticilor generate direct din baza de date a rezidenților actuali și din trecut
- proiectarea și vizualizarea planificării energetice (alimentarea cu gaze a regiunilor, utilizarea căldurii din apele uzate, energia geotermală apropiată de suprafață, centralele termice de cartier, etc.)

Alte proiecte suplimentare sunt, în prezent, în curs de dezvoltare.

![](../images/suisse_uster4.png)

În 2007 nu era foarte clar la ce ritm s-ar fi dezvoltat QGIS în continuare și cum vor evolua asistența comunitară și comercială. Astăzi se poate afirma că viteza de dezvoltare și îmbunătățirile aduse de comunitatea QGIS au depășit așteptările noastre. Suportul comunitar și comercial al companiilor Sourcepole și Norbit este excelent. Există o comunicare directă cu dezvoltatorii, fără a fi ținuți la distanță de managementul de produs sau de echipa de vânzări. Dezvoltatorii din aceste două societăți sunt, de asemenea, și dezvoltatori ai proiectului QGIS și au cunoștințe excelente despre codul de bază.

Erorile sunt adesea remediate în termen de ore sau zile după raportare și noile evoluții sunt puse în aplicare într-un interval de timp scurt. Noile caracteristici pot fi testate imediat după dezvoltare, iar lansarea către utilizatori are loc ori de câte ori calitatea este destul de bună pentru utilizatorul final. Nu este nevoie să așteptați pentru versiunile oficiale. Ne bucurăm de libertatea de a fi în măsură să influențăm proiectul și de a instala softul pe oricât de multe calculatoare ne place, fără a avea de a face cu managementul licențelor. Așteptăm cu nerăbdare colaborarea viitoare cu comunitatea QGIS și cu suportul nostru comercial, pentru a merge înainte cu proiectul QGIS.
## Autor
<figure>
<img src="../images/suisse_usteraut.jpg" class="align-left" height="200" alt="suisse_usteraut.jpg" />
<figcaption>Andreas Neumann</figcaption>
</figure>

Acest articol a fost transmis în aprilie 2011 de către Dr. Andreas Neumann. El este coordonator GIS în orașul Uster, Elveția.

{{<content-end >}}
