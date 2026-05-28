---
draft: 'true'

---
# Analyse voor woonomgeving van Lynx in de zuidelijke Karpaten
Een praktijkvoorbeeld om het basisbegrip te promoten voor het modelleren van woonomgevingen voor wilde dieren, voor studenten, gebaseerd op gegevens van open source.
## Introductie
Uitgedaagd door de taak om voor de eerste keer op GIS gebaseerd te modelleren, voerde een werkgroep van studenten bosbouw aan de University for Sustainable Development Eberswalde (HNEE) literatuuronderzoek uit naar de geschiktheid van de woonomgeving en het gedrag van de Euraziatische Lynx (*Lynx lynx*). In de module ‘Applied GIS in Natural Resource Management’, onder begeleiding van Prof. Mund, ontdekten de studenten al snel de complexiteit van het onderwerp, speciaal met betrekking tot de aanpassing van de soort aan wijzigende omgevingen. Met beperkt onderzoek dat is gepubliceerd in het Engels over de woonomgeving van de lynx habitat aan de Roemeense kant, zetten we het project voort, gebaseerd op alleen vrij beschikbare gegevenssets en open-source software. Met als doel de conceptuele kennis voor het modelleren van woonomgevingen neer te zetten, het versterken van de vaardigheden met breed toegepaste gereedschappen voor QGIS en om in het proces een **basis expertmodel** te maken.
## Methodologie
Alle verzamelde gegevens werden verwerkt met QGIS 2.6 en 2.8, geprojecteerd in ETRS89 / ETRS-LAEA en opgeslagen conform de richtlijn van INSPIRE om te voldoen aan de standaarden van de EU. Een overall **discrete index of weights** werd gedefinieerd en toegepast op alle ingevoerde gegevens.

![Afbeelding 1: Werkstroom - Lynx woonomgeving expertmodel](./images/europe_lynx1.png)

**Beschrijving werkstroom**
- Gebied van interesse \[Stap I – II\]: gebaseerd op geselecteerde gebieden van nationale parken en een buffer van 10 kilometer toegevoegd, er werd een minimaal begrenzingsvak \[α\] gemaakt en afgesneden op de omtrek van de rivier Donau (afgeleid van Corine Land Cover 2006). Verdere gereedschappen voor afsnijden \[β\] werden toegepast op alle aanvullende gegevens als een initieel voorbereidende stap (Afbeelding 2)
- Land Cover Suitability Model \[Stap IX\]: \[γ\] Invoer III en IV werden getransformeerd in shapefiles met behulp van de ingebouwde functie #Polygoniseren. Gegevens van Corine Landcover (2006) werden opnieuw geclassificeerd met behulp van veldberekening om klassen van landgebruik te groeperen en respectievelijke waarden voor de index toe te kennen. Soortgelijke verwerking werd toegepast op gegevens van Hansen Forestcover data (2000), waarbij alleen gebieden werden uitgenomen met een bedekking van 75% of hoger. Sub-model IX werd geproduceerd met behulp van de functies #Merge Shapes om III met IV te combineren en te #Rasteriseren

*Opmerking: Klassen van landbedekking werden gegroepeerd op mogelijk voorkomen van de lynx en menselijke activiteiten. Hoewel technisch van oudere herkomst, werd informatie, gerelateerd om waarden van bosbedekking, geïntegreerd om de verbetering in de habitat aan te kunnen geven en als een algemeen voorbeeld voor het samenvoegen van ruimtelijke gegevenssets*
- Habitat Suitability Model \[Stap X\]: \[δ\] Een Elevation Suitability Index werd afgeleid uit de AsterDEM 2.0 \[VI\] en werd samen met een Population Density Index \[V\] geïntegreerd in het uiteindelijke model voor geschiktheid van habitat (Afbeelding 3) door de #Rasterberekening te gebruiken

```

```
    Cover Suitability Model * Population Density Index * Elevation Suitability Index
    
*Opmerking: Definiëren van bos (\>= 75% bedekking) als best geschikt en gebruiken van de hoogtegegevens om waarden van index boven de aangenomen boomgrens is conceptueel gerelateerd aan de habitat van het hert als belangrijkste prooi*
- Potential Hunter Accessibility Model \[Stap XI\]: Met toepassing van het gereedschap #Terreinanalyse \[ε\], werd een hellingslaag uitgenomen uit de gegevens van de DEM en gecombineerd \[η\] met een laag met wegafstanden, die werd geproduceerd door gerasteriseerde OSM-weggegevens te verwerken met de functie #Proximity en indexwaarden werden toegekend met behulp van rasterwaarden #Reclassify

```

```
    .
                          Slopelayer
    Road distance * ( 1 + ----------- )
                             100
    
- Conservation Value Model \[Stap XII\]: Is het resultaat van de functie #Rasterberekening: (Afbeelding 4)

```

```
    (Habitat Suitability Model * Hunter Accessibility Model)
    --------------------------------------------------------
                           2
    
*Opmerking: De Hunter Accessibility Model zal de afnemende waarschijnlijkheid aangeven dat jagers het gebied betreden bij toenemende afstand tot wegen en steilere hellingen*

![Afbeelding 2, 3 en 4](./images/europe_lynx2.png)
## Conclusie
Kijkend naar de uiteindelijke uitvoer (Afbeelding 3) leek een eerste potentiële analyse van de habitat succesvol te zijn, maar meer belangrijk: het basis modelleren zelf bleek achteraf minder moeilijk dan initieel werd verwacht. Onze keuze om een submodel voor toegankelijkheid voor jagers toe te voegen, stelde ons in staat een andere dimensie te implementeren in termen van beoordeling van risico's voor de habitat. Die eenvoudig kan worden genest binnen het reeds bestaande scenario en kan worden gebruikt om benodigde beschermingsmaatregelen te bepalen onder aspecten van bijv. infrastructurele ontwikkeling. Echter, enige cruciale informatie over de habitat, zoals bosstructuur (onze hoogste geschiktheid voor de habitat) kan niet worden afgeleid uit beschikbare gegevenssets en in combinatie met het complexe gedrag van de soort moet het resultaat daarom worden begrepen als basis en niet volledig. Op dit moment nog niet geïmplementeerde aanvullende factoren zijn sterftecijfers op wegen, ruwheid van het terrein en gedetailleerd voorkomen van prooi.

Naast het open source, vrij beschikbare karakter is QGIS software in de afgelopen jaren onderwerp geweest van belangrijke ontwikkelingen. We hebben een erg positieve ervaring gehad met de integratie van de Toolbox, wat het ons mogelijk maakte gebruik te maken van de verscheidene gereedschappen van GRASS en SAGA, zelfs voor onervaren gebruikers. Er traden geen compatibiliteitsproblemen op, ondanks het frequent gebruiken van de verschillende versies. De algemene afwezigheid van administratieve beperkingen kan een krachtig voordeel zijn bij het intuïtief werken met gegevenssets. Wij zien uit naar verdere verbeteringen, speciaal met betrekking tot de geïntegreerde modelbouwer.
## Verwijzingen
- Kaczensky, P., Chapron, G.,von Avrx, M., Huber, D., Andrén, H. & Linnell, J. (December 2012): Status, management and distribution of large carnivores in Europe. Document Europese Commissie.
- Schadt, S., Revilla, E., Wiegand, T., Knauer, F., Kaczensky, P., Breitenmoser, U., Bufka, L., Cerveny, J., Koubek, P., Huber, T., Stanisa, C. & Trepl, L. (2002): Assessing the suitability of central European landscapes for the reintroduction of Eurasian lynx. Article Journal of Applied Ecology.
- Salvatori, V. (2004): Conservation areas for large carnivores in the Carpathian Mountains. PhD Thesis.
- Podgórski, T., Schmidt, K., Kowalczyk, R. & Gulczyñska, A. (2008): Microhabitat selection by Eurasian lynx and its implications for species conservation. Acta Theriologica 53: 97--110.
- Boutros, D. (March 2002): Characterization and assessment of suitability of Eurasian lynx (Lynx lynx) den sites. KORA Report No. 12e, Diploma thesis.

### Auteurs
Angela Dichte, Luca Ehrminger, Silvana Garcia Travesi Reyes, Tobias Hoppe en David Winger zijn studenten in het vierde semester van het studieprogramma International Forest Ecosystem Management B.Sc., Anne Gnilke respectievelijk German Forestry en Henri Hiltunen is een uitwisselingsstudent van de Mikkeli University of Applied Sciences, Finland. Prof. Mund is lector in GIS en Remote Sensing aan de HNE Eberswalde sinds 2010 en verschafte begeleiding en technische ondersteuning aan het project.

Neem, voor meer informatie, contact op met Luca.Ehrminger(at)hnee.de, David.Winger(at)hnee.de, of Prof.Dr.Jan-Peter Mund: Jan-Peter.Mund(at)hnee.de.
