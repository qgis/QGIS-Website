---
draft: 'true'

---
# Die Nutzung von QGIS in der Geodateninfrastruktur der Stadt Uster
Die Stadt Uster benutzt QGIS seit 2007. Durch die Entscheidung des Kanton Solothurn für die Nutzung von QGIS als Desktop-GIS-Ersatz für ArcView wurde auch in Uster entschieden QGIS auszuprobieren. Die Stadt beteiligte sich an der weiteren Entwicklung der QGIS-Applikation durch die Anregung und den Test neuer Funktionen und durch die finzanzielle Unterstützung der Entwicklung. Im Gegenzug erhält User eine sich schnell entwickelndes, plattformunabhängiges Desktop-GIS- und WebGIS-Lösung, das durch eine weltweite Benutzer- und Entwicklungsgemeinschaft gestützt wird.

![](./images/suisse_uster1.png){.align-right}

PostGIS/PostgreSQL wird als zentrales Geodatenlager verwendet. Andere Datenbanken und Datenquellen werden in regelmäßigen Abständen mit Werkzeugen wie OGR und FME in PostgreSQL repliziert. Zu Beginn wurde QGIS hauptsächlich zur Anzeige verwendet. Der erste QGIS-Benutzer war ein Bauer, der die Erklärungen andere Bauern der Umgebung für landwirtschaftliche Zuschüsse zu überwachen hatte.  Später wurde QGIS auch als Plattform zur Datenbearbeitung und Kartenveröffentlichung eingeführt - dabei wurden auch die Bearbeitungswerkzeuge und die Druckzusammenstellung verbessert. Zusammen mit anderen schweizer QGIS-Benutzer (Solothurn, Thun und CDE (Berner Universität)) koordinieren und sponsorn wir die Verbesserung dieser Werkzeuge und auch einige Verbesserungen bei der datengetriebenen Darstellung, automatische Beschriftung, Attributbehandlung und Formulare.

![](./images/suisse_uster2.png){.align-right}

Die Stadtverwaltung benutzt auch kommerzielle GIS-Software: Autodesk Topobase für die Erfassung und die Bearbeitung von Kataster- und Kanaldaten und GE Smallworld für die Verwaltung von Gas-, Wasser- und Stromnetzen. Dies sind jedoch Fachsysteme, die von speziell ausgebildetem Personal benutzt werden. Alle anderen GIS-Projekte und die Anzeige aller Daten wird von QGIS erledigt.

In the second half of 2010, first tests with QGIS server were carried out. In 2011 we introduced a new WebGIS system based on the QGIS WMS server and GeoExt/OpenLayers as the web client. The main reasons for the decision to use QGIS server were the considerable time savings made possible by re-using the existing QGIS desktop project configurations, rather than having to manage parallel Web project configurations. Additional advantages are the rich set of symbolization and labeling options and the consistent map rendering between the Desktop GIS application and the Web-GIS. The QGIS webclient can be tested and used at <http://gis.uster.ch/>

![](./images/suisse_uster3.png){.align-right}

Heute wird QGIS für folgende GIS-Projekte verwendet:
- Anzeige von Kanaldaten, Integration von zusätzlichen Datenbank und direkter Zugriff auf Kanalvideos und Inspektionsprotokolle.
- Anzeige und Bearbeitung des generellen Entwässerungsplan
- Anzeige  des Leitungskatasters (Kanal-, Wasser-, Gas- und Strom-,  sowie Telekommunikationsnetze).
- Anzeige von Kataster- und Vermessungsdaten
- Anzeige und Bearbeitung des kommunalen Naturschutzinventar
- Anzeige und Bearbeitung von Stadt- und Regionalplanungsdaten
- Anzeige und Bearbeitung von Straßendaten
- Anzeige von direkt aus der Datenbank erzeugten Statistiken zu aktuellen und verzogenen Einwohner.
- Planung und Visualisierung für die Energieplanung (Gasversorgungsgebiete, Wärmenutzung von Abwasser,  oberflächennahe Geothermie, Blockheizkraftwerke, usw.).

Weitere Projekte sind derzeit in der Entwicklung.

![](./images/suisse_uster4.png){.align-right}

2007 war nicht ganz klar in welcher Geschwindigkeit QGIS weiterentwickelt würde und wie sich die Gemeinschaft und die kommerzielle Unterstützung entwickelt würde. Heute kann festgestellt werden, dass die Entwicklungsgeschwindigkeit und die Verbesserungen der QGIS-Gemeinschaft unsere Erwartungen übertroffen haben. Gemeinschaft und kommerzielle Unterstützung der Firmen Sourcepole und norBIT sind hervorragend. Es gibt eine direkte Kommunikation mit den Entwicklern ohne das Sie durch Produktmanagement oder Vertrieb abgeschirmt wären. Die Entwickler dieser beiden Firmen sind auch führende Entwickler des QGIS-Projekt und haben exzellenten Überblick über die Codebasis.

Fehler werden oft innerhalb von Stunden oder Tage nach Meldung behoben und neue Entwicklungen werden in einem kurzen Zeitraum implementiert. Neue Funktionen können unmittelbar nach der Entwicklung getestet und den Benutzers zur Verfügung gestellt werden, sobald die Qualität gut genug für den Endnutzer ist. Es gibt keinen Grund auf offizielle Softwarefreigabe zu warten. Wir schätzen die Möglichkeit das Projekt zu beeinflussen und die Software auf sovielen Computern zu installieren wie wir möchten, ohne uns mit Lizenzverwaltung zu befassen. Wir freuen uns auf die zukünftige Zusammenarbeit mit der QGIS-Gemeinschaft und unseren kommerziellen Unterstützern um das QGIS-Projekt voran zu bringen.
## Autor
![Andreas Neumann](./images/suisse_usteraut.jpg){.align-left height="200px"}

Dieser Artikel wurden Im April 2011 von Dr. Andreas Neumann beigetragen. Er ist GIS-Koordinator bei der Stadt Uster in der Schweiz.
