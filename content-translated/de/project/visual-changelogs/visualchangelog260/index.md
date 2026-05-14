---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: Projekt
sidebar: true
title: Changelog for QGIS 2.6
type: visual-changelog

---
{{<content-start >}}
# Changelog for QGIS 2.6{#changelog26 }
Veröffentlichungsdatum: 2014-10-31

Änderungsprotokoll für die nächste Version von QGIS 2.6.0. Wir haben viele neue Funktionen, Anpassungen und Erweiterungen hinzugefügt um das beliebteste freie Desktop GIS sogar noch funktionsreich und nützlich zu machen.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Wir möchten den Entwickler, Dokumentationsschreibern, Testern und all den vielen dort draussen danken, die freiwillig Zeit und Arbeit beitragen (oder Leute dafür finanzieren).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Zum Schluss wollen wir unseren offiziellen Förderern für ihre unschätzbare finanzielle Unterstützung, die sie dem Projekt angedeihen lassen, danken:
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

QGIS ist Freie Software und Sie sind nicht verpflichtet, etwas dafür zu bezahlen, um es zu nutzen - in der Tat wollen wir Menschen weit und breit dazu ermutigen, es zu nutzen - unabhängig davon, was ihr finanzieller oder sozialer Status ist. Wir glauben, dass die Befähigung der Menschen mit räumlichen Entscheidungshilfe-Werkzeuge umzugehen, in einer besseren Gesellschaft für die gesamte Menschheit resultieren wird.

{{<table-of-contents >}}
## Allgemein
### Funktion: Projektdateiname in den Eigenschaften
Der volle Pfad der QGIS-Projektdatei wird im Eigenschaftendialog angezeigt.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Funktion: Den letzten Punkt per Rücktaste/Entf-Taste entfernen
Nun können Sie während Sie Flächen oder Entfernungen messen, unerwünschte Stützpunkte aus ihrer Maßlinie mit Rücktaste oder Entfernen-Taste löschen. 

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Funktion: Zusammengehörige Objekte in der Karte aus über ein Beziehungsreferenzbedienelement wählen
### Funktion: Bearbeitungsbedienelemente
Wir haben einige Verbesserungen an den Bearbeitungselementen vorgenommen:
- Neue Bearbeitungselement für Datum/Zeit und das Setzen von Leerdaten
- Filterzeile
- Saubere Behandlung von Nullwerten in Bearbeitungselementen
- Fotobearbeitungselement erhält Nullwerte
- Webbedienelement erhält Nullwerte
- Attributtabelle kann zwischen 0 und NULL unterscheiden
- Suffixunterstützung für Bereichsbearbeitungselement

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Funktion: Wahlweise Nutzung einer Untermenge der Felder eines verknüpften Layers
You can now use just a subset of related fields when creating a vector join.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Funktion: Ausdrucksfeld (virtuelle Felder)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Funktion: Aktionen können nun Icons zugeordnet werden
Wenn eine Benutzeraktion für einen Vektorlayer erzeugt wird, können Sie der Aktion auch ein Icon zuordnen.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Funktion: Zusätzlichen Ausdruckstypen und -optionen
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Funktion: Klassen mit abgestufter oder kategorisierter Darstellung können umgeschaltet werden
Sie können nun die Anzeige bestimmter Klassen in abgestufter oder kategorisierter Darstellung abwählen statt sie zu entfernen.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Funktion: Legendenverbesserungen
Die zweite Phase der Legenden-/Inhaltverszeichnis-Überholung wurde abgeschlossen. Diese enthält:
- API-Bereinigung (für Entwickler)
- Darstellungsgruppen von Kartenlayern im Layerbaum. Dieser neue Werkzeugleistenknopf erlaubt den schnellen Wechsel zwischen Gruppen sichtbarer Layer.
- Möglichkeit Layergruppen aus der Legendenwerkzeugleiste zu verwalten
- The new legend filter option on the legend toolbar will remove legend items for any classes which are not currently in the view extent. This is an awesome improvement as it ensures that your map legend does not contain entries for items not currently in the map view. It is available in the main map legend and in map composer and for WMS layers.
- Rule-based renderer legends can now be displayed in a pseudo-tree

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Datenanbieter
### Funktion: DXF-Exportverbesserungen
- Baumanzeige und Attributwahl zur Layerzuweisung im Dialog
- Unterstützung für Flächenfüllung/SCHRAFFUR
- Texte als MTEXT statt TEXT ausgeben (einschließlich Text, Neigung und Dicke)
- support for RGB colors when there\'s no exact color match
- AutoCAD 2000-DXF (R15) statt R12 nutzen
- R18-Testmethoden entfernt

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Druckzusammenstellung
### Funktion: Kontrolle über Druckzusammenstellungelemente aus Drucken/Exporten auszuschließen
Wir haben ein Kontrollkästchen und einen datendefinierten Knopf zur Steuerung ob ein Objekt bei Druckzusammenstellungsausdrucken/-exporten ausgeschlossen werden soll. Wenn es nicht abgehakt ist, wird es während der Gestaltung angezeigt.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Funktion: Steuerung des Seitendrucks für leere Zusammenstellungsrahmen
Für Tabellen und HTML-Rahmen gibt es nun ein Kontrollkästchen, das steuert, ob die Seite auf der er sich befindet exportiert werden soll, wenn er leer ist.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Funktion: Elementbaumanzeige
The item tree panel in the map composer allows for selection of items, hiding/showing items, toggling lock status of items and double-clicking to edit item id. You can also use drag and drop to reorder items.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Feature: More control over appearance of composer arrow/line items
- Lines can be styled using line symbol style dialog
- Arrow head fill and outline colors can be user defined
- Arrow head outline width can be user defined

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Feature: Data defined control of composer items
Many properties of composer items can now be controlled using data binding. These include:
- Transparency and blend mode.
- Elementdrehung.
- Map scale, extents and rotation.
- Atlasobjektränder
- Elementgröße und -position.
- Seitengröße, Orientierung und Anzahl der Seiten.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Funktion: Zusammenstellungsbilder können als ferne URLs angegeben werden
Bildelement in der Zusammenstellung unterstützen nun ferne URLs als Bildquelle. Diese Quelle kann auch datendefiniert sein.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Funktion: Zusammenstellungstabellenverbesserungen
- Nun kann ein Tabellenkopf und die Schriftfarbe des Inhalts festgelegt werden.
- Tabellen können nun in mehrere Rahmen geteilt werden, was die Verteilung über Spalten oder mehrere Seiten erlaubt.
- Added option show headers on first frame, all frames, or no frames.
- Allow manual control of column widths.
- New options for table source, including current atlas feature and child features from a relation.
- Choice of behaviour for empty tables, include hiding the entire table, showing empty cells, or displaying a set message in the table body.
- Added a checkbox to filter table features to those which intersect the current atlas feature.
- Added checkbox to remove duplicate rows from table.

Note that tables in existing projects are not automatically updated to the new table format which supports these features, and tables must be readded to a composition for the new settings to appear.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Funktion: Zusammenstellungsverbesserungen
An der Druckzusammenstellung erhielt eine Anzahl von Verbesserungen in 2.6.
- Sie können nun die sekundäre Füllfarbe von Maßstabsleisten festlegen
- Holding shift while drawing line/arrow items constrains drawing to horizontal, vertical or 45 degree angles
- Holding shift while drawing other new items constrains them to squares, holding alt causes item to be drawn from the center
- Right click no longer locks/unlocks items, this is now handled by the new items panel. Locked items can no longer be selected from the composer canvas, allowing for interaction with items below them.
- Holding alt while pressing cursor keys results in a 1px movement for items
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Feature: Improved item snapping
Snapping thresholds are now set in pixels, allowing for finer movement and resizing of items when zoomed in to a composition. Items within a group are no longer used for auto snap lines.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Feature: Multiple overviews for a map item
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Feature: HTML item improvements
There are a number of useful new options for the HTML composer item:
- Option for manual entry of HTML source
- QGIS expressions within HTML source can be evaluated prior to rendering HTML content
- Data defined URL for HTML source
- Allow for creating a user stylesheet to override HTML styles

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Feature: Composer map grid improvements
- You can now have multiple grids with different properties.
- You can mix reprojected grids and Lat/Long grids.
- You can use standard QGIS symbology grid lines etc.
- There is a new frame/annotations only grid style. Selecting this style causes only the frame and annotations to be drawn, with no grid lines or other markings over the map.
- There are now options for controlling which side of a map item the frame is drawn on.
- There are new tick styles for frames, with inner ticks, outer ticks and both inner and outer tick options.
- We have made improvements to grid annotations, including many new formats for annotations.
- Grid annotations now use the typographically correct prime and double prime symbols for grid annotations.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Verarbeitung
### Feature: On-line collection of models and scripts
Models and scripts can be downloaded from the online collection and installed directly from the Processing interface. The collection will be expanded with new scripts and models provided by Processing users.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Feature: New modeler implementation
The modeler has been rewritten, and now provides extra functionality such as allowing nested models with no depth limit. Models are now stored as JSON files. Backwards compatibility is kept, so all models can still be used. You can also now drag and drop items from the inputs and algorithms onto the modeler graph.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programmability
### Feature: API changes for QGIS widgets
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
### Feature: Enhancements of searching with GetFeatureInfo request
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Feature: Add a precision setting for GetFeatureInfo geometry attributes
## Symbolisierung
### Feature: Better random colour choice
We have improved the random colour algorithm for classified renderer so that the colours generated are more visually distinct from each other.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Feature: Symbology user interface improvements
- Where possible, properties of symbol layer are maintained when changing symbol layer type.
- Added an edit button for shapeburst and gradient color ramps.
- Automatic update of label and neighboring ranges boundaries.
- Classes are automatically converted from categorised and graduated classes when switching to rule based renderer.
- Added units and number of decimal places to graduated renderer labels.
- Improved responsiveness to changes in color ramp, inverted colour ramp, and other options in GUI.
- Retain symbol when switching between simple, graduated, categorized, and other renderers.
- Improved labelling of StdDev calculation mode.

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Benutzerschnittstelle
### Feature: Syntax highlighting code editor
For python script editors, expression builder, filter window, composer HTML and CSS editors

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Feature: Color palettes
You can now define your own custom color palettes for use in QGIS.
- Custom user global color palette (in options dialog).
- Per project color palette (in project properties dialog).
- Colors are shown in color button menus and new color picker dialog.
- You can import/export colors to a GPL palette file.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Feature: New color picker dialog
There is a new custom QGIS color picker dialog. Features include:
: - Sliders for hue, saturation, value, red, green, blue color components.
  - Alpha slider.
  - Option to copy/paste html color codes (in a variety of formats).
  - Before/after color preview, with alpha preview.
  - Interactive 2D color ramp widget.
  - Hue wheel/triangle widget.
  - Editable color palettes, including the ability to create new palettes and import/export colors to a GPL palette file.
  - Live color sampler with option to sample over a set radius (OS support dependant).
  - Supports interaction with other apps via drag and drop of colors (OS support dependant).
  - Option to disable the dialog and use the native picker dialog instead.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Feature: Single select feature tool merged into select by rectangle
We have merged the single selection tool into the rectangle tool. If you want to select a single feature, simply enable the rectangle tool and then single click (rather than dragging a rectangle) a feature.

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Feature: Add layer to map canvas behaviour
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Feature: Add icon size 48 and 64
For those using QGIS on touch devices (or if you just like big, chunky icons), you can now set the icons up to 64 x 64 pixels in size.

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Feature: New colour buttons
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Feature: Context menu for identify tool
When using the identify tool, you can now right click on the canvas to use the identify tool in context mode. In the menu that appears you can define which feature types you wish to identify (all all if you like).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
