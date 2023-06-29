---
source: "blog"
title: "OPENGIS.ch blog: Unterstützung für WMTS im QGIS Swiss Locator"
image: "unterstutzung-fur-wmts-in-qgis-swiss-locator."
date: "2023-06-13"
link: "https://www.opengis.ch/2023/06/13/unterstutzung-fur-wmts-in-qgis-swiss-locator/"
draft: "true"
showcase: "planet"
---

<figure class="wp-block-image size-full"><img data-attachment-id="13791" data-permalink="https://www.opengis.ch/2023/06/13/unterstutzung-fur-wmts-in-qgis-swiss-locator/unnamed/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?fit=512%2C341&amp;ssl=1" data-orig-size="512,341" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="unnamed" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?fit=300%2C200&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?fit=512%2C341&amp;ssl=1" decoding="async" loading="lazy" width="512" height="341" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?resize=512%2C341&#038;ssl=1" alt="" class="wp-image-13791" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?w=512&amp;ssl=1 512w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?resize=300%2C200&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/unnamed.png?resize=360%2C240&amp;ssl=1 360w" sizes="(max-width: 512px) 100vw, 512px" data-recalc-dims="1" /></figure>



<p>Das <strong>QGIS swiss locator Plugin</strong> erleichtert in der Schweiz vielen Anwendern das Leben dadurch, dass es die umfangreichen Geodaten von <strong><a href="https://www.swisstopo.ch/" data-type="URL" data-id="https://www.swisstopo.ch/">swisstopo</a></strong> und <strong><a href="https://opendata.swiss" data-type="URL" data-id="https://opendata.swiss">opendata.swiss</a></strong> zugänglich macht. Darunter ein breites Angebot an GIS Layern, aber auch Objektinformationen und eine Ortsnamensuche.</p>



<p>Dank eines Förderprojektes der Anwendergruppe Schweiz durfte OPENGIS.ch ihr Plugin um eine zusätzliche Funktionalität erweitern. Dieses Mal mit der Integration von WMTS als Datenquelle, eine ziemlich coole Sache. Doch <strong>was ist eigentlich der Unterschied zwischen WMS und WMTS</strong>?</p>



<h2 class="wp-block-heading">WMS vs. WMTS</h2>



<p>Zuerst zu den Gemeinsamkeiten: Beide Protokolle – WMS und WMTS – sind dazu geeignet, Kartenbilder von einem Server zu einem Client zu übertragen. Dabei werden <strong>Rasterdaten</strong>, also Pixel, übertragen. Ausserdem werden dabei gerenderte Bilder übertragen, also keine Rohdaten. Diese sind dadurch für die Präsentation geeignet, im Browser, im Desktop GIS oder für einen PDF Export.</p>



<p>Der Unterschied liegt im T. Das T steht für “Tiled”, oder auf Deutsch “gekachelt”. Bei einem WMS (ohne Kachelung) können beliebige Bildausschnitte angefragt werden. Bei einem WMTS werden die Daten in einem genau vordefinierten Gitternetz &#8212; als Kacheln &#8212; ausgeliefert.&nbsp;</p>



<p>Der Hauptvorteil von WMTS liegt in dieser Standardisierung auf einem Gitternetz. Dadurch <strong>können diese Kacheln zwischengespeichert (also gecached) werden</strong>. Dies kann auf dem Server geschehen, der bereits alle Kacheln vorberechnen kann und bei einer Anfrage direkt eine Datei zurückschicken kann, ohne ein Bild neu berechnen zu müssen. Es erlaubt aber auch ein clientseitiges Caching, das heisst der Browser – oder im Fall von Swiss Locator QGIS – kann jede Kachel einfach wiederverwenden, ganz ohne den Server nochmals zu kontaktieren. Dadurch kann die Reaktionszeit enorm gesteigert werden und flott mit Applikationen gearbeitet werden.</p>



<p>Warum also noch WMS verwenden?</p>



<p>Auch das hat natürlich seine Vorteile. Der WMS kann optimierte Bilder ausliefern für genau eine Abfrage. Er kann Beispielsweise alle Beschriftungen optimal platzieren, so dass diese nicht am Kartenrand abgeschnitten sind, bei Kacheln mit den vielen Rändern ist das schwieriger. Ein WMS kann auch verschiedene abgefragte Layer mit Effekten kombinieren, Blending-Modi sind eine mächtige Möglichkeit, um visuell ansprechende Karten zu erzeugen. Weiter kann ein WMS auch in beliebigen Auflösungen arbeiten (DPI), was dazu führt, dass Schriften und Symbole auf jedem Display in einer angenehmen Grösse angezeigt werden, währenddem das Kartenbild selber scharf bleibt. Dasselbe gilt natürlich auch für einen PDF Export.</p>



<p>Ein WMS hat zudem auch die Eigenschaft, dass im Normalfall kein Caching geschieht. Bei einer dahinterliegenden Datenbank wird immer der aktuelle Datenstand ausgeliefert. Das kann auch gewünscht sein, zum Beispiel soll nicht zufälligerweise noch der AV-Datensatz von gestern ausgeliefert werden.</p>



<p>Dies bedingt jedoch immer, dass der Server das auch entsprechend umsetzt. Bei den von swisstopo via map.geo.admin.ch publizierten Karten ist die Schriftgrösse auch bei WMS fix ins Kartenbild integriert und kann nicht vom Server noch angepasst werden.</p>



<p>Im Falle von QGIS Swiss Locator geht es oft darum, Hintergrundkarten zu laden, z.B. Orthofotos oder Landeskarten zur Orientierung. Daneben natürlich oft auch auch weitere Daten, von eher statischer Natur. In diesem Szenario kommen die Vorteile von WMTS bestmöglich zum tragen. Und deshalb <strong>möchten wir der QGIS Anwendergruppe Schweiz im Namen von allen Schweizer QGIS Anwender dafür danken, diese Umsetzung ermöglicht zu haben</strong>!</p>



<p>Der QGIS Swiss Locator ist das schweizer Taschenmesser von QGIS. Fehlt dir ein Werkzeug, das du gerne integrieren würdest? Schreib uns einen Kommentar!</p>
