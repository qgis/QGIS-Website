---
draft: 'true'

---
# Folosirea setului de instrumente de procesare la automatizarea clasificării zăpezii
Snowy Hydro Limited (SHL) este un generator de vârf, de energie electrică din Snowy Mountains din New South Wales, Australia. În ciuda deținerii unei varietăți de active de producție în întreaga țară, Snowy Hidro Limited este cel mai bine cunoscută pentru custodia unui activ iconic al infrastructurii australiene, Snowy Mountains Hydro Electric Scheme.

Snowy Mountains Hydro Electric Scheme este posibilă datorită căderilor de zăpadă de sezon, din regiunea alpină New South Wales. Apa provenită din topirea de primăvară a zăpezii, este utilizată pentru a genera energie electrică dedicată acoperirii cererii de vârf de pe piața națională de energie electrică, în timp ce, de asemenea, servește și la asigurarea apei în zonele interioare uscate, din Sud-Estul Australiei, la irigații și agricultură.

Clasificarea acoperirii cu zăpadă de-a lungul lunilor de iarnă permite SHL să monitorizeze ciclul de viață al zonei acoperite de zăpadă, arhivarea zonelor de acoperire pentru înregistrări istorice, și furnizarea statisticilor de acoperire pentru echipa de prognoze hidrografice a randamentului apei și a capacității de depozitare.

![Map 1.1 Snowy Water Catchment Map](images/australia_snowyhydro1.jpg){.align-center height="43400px"}
## Fundal
În fiecare an, în lunile de iarnă (de la 01 iunie la 31 octombrie) SHL obține cât mai multe imagini posibil, gratuite, ale norilor, de la satelitul MODIS Terra (EOS AM). Aceste imagini sunt apoi prelucrate de către un algoritm cunoscut sub numele de indexul de zăpadă cu diferența normalizată (NDSI), care este folosit pentru a indica zonele în care zăpada este prezentă. În timp ce acest algoritm nu este unic pentru un senzor anume, instrumentul MODIS a fost ales datorită rezoluției spațiale adecvate și acoperirii zilnice a ariei proiectului (Harta 1.1 Captarea de Apă provenind din topire).
## Scopul
Scopul acestui proiect este de a automatiza fluxul de lucru NDSI ca un model, folosind trusa instrumentelor de procesare QGIS. Ieșirea necesară este un poligon vectorial care arată măsura în care zăpada acoperă bazinul de captare a apelor Snowy, împreună cu atributele care descriu suprafața totală acoperită, în kilometri pătrați.
## Metoda
Algoritmul NDSI în sine este destul de simplu (arătat mai jos, în Formula 1.1 - Indexul de zăpadă cu diferență normalizată (NDSI)), precum și pașii următori, necesari pentru a extrage stratul de zăpadă într-un format vectorial, de asemenea, se pretează bine la un model de instrumente de procesare.

![Formula 1.1 - Normalised Difference Snow Index (NDSI)](./images/australia_snowyhydro8.png)

Acest algoritm NDSI va returna rezultatele între -1 și 1, cu un prag de zăpadă având de obicei valori mai mari de 0,4. Un exemplu de ieșire NDSI este prezentată mai jos (Harta 1.3 - ieșirea NDSI), alături de o imagine în culori naturale (Harta 1.2 - culori reale MODIS) pentru 13 iulie 2014. După cum se vede din aceste imagini ieșirea NDSI este foarte bună la deosebirea zonele acoperite de zăpadă față de alte tipuri de terenuri acoperite și nori. Se pot clasifica eronat porțiuni ale corpurilor de apă mari ca zăpada, cauzate de apa având caracteristici de absorbție în partea infraroșie a spectrului. Această caracteristică a NDSi indică necesitatea de a încorpora, la un moment dat, o mască de apă în model.

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
## Rezultate/Concluzii
Trusa de instrumente de procesare din QGIS reprezintă un mod puternic de a automatiza un flux de lucru, cum ar fi această clasificare de zăpadă. Modelul prezentat mai sus automatizează cu succes procesul de clasificare a zăpezii, și oferă un set de date GIS care pot fi utilizate pentru vizualizarea și introducerea în aplicații statistice ulterioare. Se elimină cu succes erorile de utilizare subiective, asociate cu metodele anterioare folosite de SHL, oferind în același timp un instrument de clasificare repetabil și coerent. Unele rezultate de sezon pot fi vizualizate aici.
### Autor
Andrew Jeffrey este un analist GIS la Snowy Hydro Limited cu sediul în Cooma NSW, Australia. A absolvit Universitatea Charles Sturt din Wagga Wagga cu un Bachelor of Science (BSC) în sisteme informatice spațiale în 2004. În același timp, la Snowy Hidro Limited el a fost în măsură să ofere sprijin spațial zi de zi în cadrul organizației și în proiecte interesante, cum ar fi experimentul Cloud Seeding.
