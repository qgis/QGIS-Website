---
draft: 'true'

---
# Analyse von Luchs-Habitaten in den südlichen Karpaten
Eine auf quelloffenen Daten basierende Fallstudie für Studierende zur Verbreitung von Basiswissen über die Modellierung von Wildtierhabitaten.
## Einführung
Challenged with the task of GIS based modeling for the first time, a working group of undergraduate forestry students of the University for Sustainable Development Eberswalde (HNEE) conducted literature research for habitat suitability and behavior of the Eurasian Lynx (*Lynx lynx*). In the module 'Applied GIS in Natural Resource Management', under the guidance of Prof. Mund, the students quickly discovered the subject's complexity, especially within regard to the adaptability of species to changing environments. With limited research published in English about lynx habitat on the Romanian side, we continued the project based on only freely available data sets and open-source software, aiming to establish conceptual knowledge of habitat modeling, strengthening skills on widely applied QGIS tools and to create a **basic expert model** in the process.
## Methodik
Alle gesammelten Daten wurden mit QGIS 2.6 und 2.8 verarbeitet, in ETRS89 / ETRS-LAEA projiziert und gemäß der INSPIRE-Richtlinie gespeichert, um den EU-Standards zu entsprechen. Ein allgemeiner **diskreter Index von Gewichtung** wurde definiert und auf alle Eingabedaten angewendet.

![Figure 1: Workflow - Lynx habitat expert model](./images/europe_lynx1.png)

**Arbeitsablaufbeschreibung**
- Area of Interest \[Step I -- II\]: Based on selected national park areas and adding a 10 kilometer buffer, a minimum bounding box \[α\] was created and clipped with the outline of the river Danube (derived from Corine Land Cover 2006). Further clipping tools \[β\] were applied to all additional data as an initial preparation step (Figure 2)
- Land Cover Suitability Model \[Step IX\]: \[γ\] Input III and IV were transformed into shape files using the inbuilt #Polygonize function. Corine Landcover (2006) data was reclassified using the field calculator to group land use classes and assign respective index values. Similar processing was applied to Hansen Forestcover data (2000), extracting only areas of cover equal or higher 75 %. Sub-model IX was produced by using the functions #Merge Shapes to combine III with IV and #Rasterize

*Anmerkung: Die Bodenbedeckungsklassen wurden nach dem möglichen Vorkommen von Luchsen und menschlichen Aktivitäten gruppiert. Obwohl sie technisch gesehen älteren Ursprungs sind, wurden Informationen über Waldbedeckungswerte integriert, um eine Verbesserung des Lebensraums anzuzeigen und als ein allgemeines Beispiel für die Verknüpfung räumlicher Datensätze*.
- Habitat Suitability Model \[Step X\]: \[δ\] An Elevation Suitability Index was derived from the AsterDEM 2.0 \[VI\] and together with a Population Density Index \[V\] was integrated into the final habitat suitability model (Figure 3) by using the #Raster calculator

```

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
    
*Note:Defining forest (\>= 75 % cover) as best suitable and using the elevation data to reduce index values above assumed tree line is conceptually related to habitat of deer as the main prey*
- Potential Hunter Accessibility Model \[Step XI\]: Applying the #Terrain analysis tool \[ε\], a slope layer was extracted from the DEM data and combined \[η\] with a road distance layer, which was produced by processing rasterized OSM road data within the #Proximity function and index values assigned using #Reclassify grid values

```

```
    .
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
    
- Conservation Value Model \[Step XII\]: Is the result of the #Raster calculator function: (Figure 4)

```

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
    
*Hinweis: Das Modell für die Erreichbarkeit von Jägern gibt an, dass die Wahrscheinlichkeit, dass Jäger das Gebiet erreichen, mit zunehmender Entfernung zu Straßen und zunehmender Neigung abnimmt*.

![Figure 2, 3 and 4](./images/europe_lynx2.png)
## Conclusion
Betrachtet man das Endergebnis (Abbildung 3), so scheint eine plausible erste potenzielle Habitatanalyse gelungen zu sein, aber noch wichtiger ist, dass sich die grundlegende Modellierung selbst als weniger schwierig erwies als ursprünglich erwartet. Unsere Entscheidung, ein Submodell für die Erreichbarkeit von Jägern hinzuzufügen, ermöglichte es uns, eine weitere Dimension in Bezug auf die Bewertung des Lebensraumrisikos zu implementieren, die einfach in das bereits bestehende Szenario eingebettet und zur Bestimmung des Schutzbedarfs z. B. unter dem Aspekt der Infrastrukturentwicklung verwendet werden kann. Einige entscheidende Lebensrauminformationen, wie z.B. die Waldstruktur (unsere höchste Lebensraumeignung), können jedoch aus den verfügbaren Datensätzen nicht abgeleitet werden und in Kombination mit dem komplexen Artenverhalten muss das Ergebnis daher als grundlegend und unvollständig verstanden werden. Weitere Faktoren, die in diesem Stadium nicht berücksichtigt wurden, sind die Straßenmortalität, die Geländerauigkeit und das detaillierte Vorkommen von Beutetieren.

Neben seinem Open-Source-Charakter, der frei verfügbar ist, wurde die QGIS-Software in den letzten Jahren stark weiterentwickelt. Wir haben sehr positive Erfahrungen mit der Integration des Werkzeugkastens gemacht, der die Verwendung verschiedener GRASS- und SAGA-Werkzeuge auch für unerfahrene Benutzer ermöglicht. Trotz des häufigen Wechsels zwischen verschiedenen Versionen traten keine Kompatibilitätsprobleme auf, und die generelle Abwesenheit von administrativen Beschränkungen kann ein großer Vorteil sein, wenn man intuitiv mit Datensätzen arbeitet. Wir freuen uns auf weitere Verbesserungen, insbesondere im Hinblick auf den integrierten Model Builder.
## Referenzen
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (Dezember 2012): Status, Management und Verbreitung von Großraubtieren in Europa. Dokument Europäische Kommission.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Bewertung der Eignung mitteleuropäischer Landschaften für die Wiederansiedlung des Eurasischen Luchses. Artikel Journal of Applied Ecology.
- Salvatori, V. (2004): Schutzgebiete für Großraubtiere in den Karpaten. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (März 2002): Charakterisierung und Bewertung der Eignung von Luchshöhlen des Eurasischen Luchses (Lynx lynx). KORA-Bericht Nr. 12e, Diplomarbeit.

### Authors
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe und David Winger sind Studierende im vierten Semester des Studiengangs International Forest Ecosystem Management B.Sc., Anne Gnilke bzw. German Forestry und Henri Hiltunen ist Austauschstudent der Mikkeli University of Applied Sciences, Finnland. Prof. Mund ist seit 2010 Dozent für GIS und Fernerkundung an der HNE Eberswalde und hat das Projekt fachlich begleitet und unterstützt.

Bitte wenden Sie sich an Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, oder Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de für weitere Informationen.
