---
HasBanner: false
date: '2020-02-23'
description: Met het QGIS Grant Programme 2019 waren we in staat zes aanvragen te
  ondersteunen die erop waren gericht om het project QGIS te verbeteren…
draft: false
link: https://blog.qgis.org/2020/02/23/reports-from-the-winning-grant-proposals-2019/
sidebar: true
title: Rapporten van de winnende aanvragen voor financiële steun 2019

---
{{<content-start >}}

<p>Met het <a href="http://blog.qgis.org/2019/06/30/qgis-grant-programme-2019-results/">QGIS Grant Programme 2019</a> waren we in staat zes aanvragen te ondersteunen die erop waren gericht om het project QGIS te verbeteren, inclusief software, infrastructuur en documentatie. Hier zijn de rapporten over het werk dat binnen de individuele projecten is uitgevoerd:</p>
<ol>
<li><strong>Profileren en optimaliseren van de QGIS vector renderingcode (Nyall Dawson)<br />
</strong>We voerden diepteonderzoek uit naar &#8220;hot spots&#8221; van de code en inefficiënties in de QGIS renderingcode met een aantal programma's voor het profileren van code. Dat werk resulteerde in <a href="https://lists.osgeo.org/pipermail/qgis-psc/2019-December/007960.html">vele optimalisaties </a>in de vector renderingcode en in andere delen van QGIS (zoals bepaalde algoritmes van Processing). Deze optimalisaties werden beschikbaar gemaakt in de uitgave QGIS 3.10.0.</li>
<li><strong>&#8220;Herbalanceren&#8221; van het programma voor labelen en repareren van enkele slechte keuzes voor automatisch plaatsen van labels (Nyall Dawson)</strong><br />
We hebben eerst een aantal eenheidstesten ontworpen die een bereik aan verschillende situaties voor het plaatsen van labels bedekten en hebben toen die testen gebruikt als een richtlijn voor het opnieuw programmeren van het programma voor de labels. Labels zullen nu nooit worden geplaatst bovenop objecten van een laag met een hoger gewicht voor obstakels, wat de complexiteiten en problemen vermijdt die in de oude benadering aanwezig waren. Om te voorkomen dat bestaande projecten worden beschadigd, wordt de nieuwe labellogica alleen gebruikt voor nieuw gemaakte projecten in QGIS 3.12 en later. (Bestaande projecten kunnen worden geüpgraded via het dialoogvenster voor de labelinstellingen van het project.)</li>
<li><strong>Hergebruiken van bronfunctionaliteit om mogelijkheden van DB manager te verschaffen (Alessandro Pasotti &amp; Nyall Dawson)</strong><br />
We hebben een nieuwe QGIS core-API ontwikkeld, volledig gericht op Python, die het mogelijk maakt om opgeslagen verbindingen naar bronnen van verscheidene gegevensproviders te beheren op een uniforme en consistente manier. Dit is onderdeel van een grotere inspanning om een <a href="https://www.itopen.it/qgis-abstract-connections-api/">nieuwe verbindingen-API</a>te bouwen.</li>
<li><strong>Verbeteringen aan cache voor snappen (Hugo Mercier)</strong><br />
Snappen is cruciaal voor het bewerken van georuimtelijke objecten. Snappen gaat er correct van uit dat QGIS in zijn geheugen een geïndexeerde cache heeft van de geometrieën om aan te snappen. En die cache te onderhouden als gegevens worden aangepast, soms  door een andere gebruiker of databaselogica, kan een echte uitdaging zijn. Dat is precies wat <a href="https://lists.osgeo.org/pipermail/qgis-psc/2020-January/008126.html">dit werk</a> aanpakt. Deze mogelijkheid is samengevoegd in QGIS 3.12.</li>
<li><strong>Problemen in grotere 3D-scenes gerepareerd (Martin Dobias)</strong><br />
We werkten aan<a href="https://lists.osgeo.org/pipermail/qgis-psc/2020-January/008158.html"> twee problemen binnen 3D-kaartweergaven</a>. De eerste was dat kaarttegels alleen werden voorbereid met een enkele CPU-core &#8211; dit is nu gerepareerd en we kunnen meerdere CPU's gebruiken om tegels van 3D-scenes sneller te laden. Het andere (en grotere) probleem was dat gegevens uit vectorlagen (als ze de 3D-renderer hebben toegewezen gekregen) al in een keer werden voorbereid voor de gehele laag in de hoofdthread. Dat resulteerde in het mogelijk lang bevriezen van de gehele gebruikersinterface als gegevens werden geladen. Dit is nu ook opgelost en gegevens uit vectorlagen worden geladen in kleinere tegels in achtergrondthreads (en met meerdere CPU-cores). Als resultaat daarvan is de algemene gebruikerservaring nu veel soepeler.</li>
<li><strong>Open documentatie-issues voor pull requests (Matthias Kuhn en Denis Rouzaud)</strong><br />
Een documentatie-bot is <a href="https://lists.osgeo.org/pipermail/qgis-psc/2020-January/008095.html">nu live</a> en maakt automatisch een issue in de opslagplaats voor de documentatie voor samengevoegde PR.</li>
</ol>
<p>Dank aan iedereen die heeft deelgenomen en deze ronde van grants een groot succes maakte, en dank aan al onze sponsoren en donoren die dit initiatief mogelijk maakten!</p>

<p><a href="https://blog.qgis.org/2020/02/23/reports-from-the-winning-grant-proposals-2019/" target="_blank" rel="noopener noreferrer">Bekijk de originele post op blog.qgis.org ↗</a></p>

{{<content-end >}}
