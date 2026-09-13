---
draft: false
sidebar: true
subtitle: ''
title: Privacybeleid
type: page

---
{{<content-start >}}
# Ons privacybeleid
## QGIS Feed en dashboard Analytics
Het **QGIS Feed Analytics Dashboard** ([https://analytics.qgis.org](https://analytics.qgis.org)) verzamelt minimale, niet te identificeren gebruiksgegevens om het project QGIS te helpen verbeteren. Als QGIS op nieuwe updates controleert op de [QGIS Feed website](https://feed.qgis.org), wordt de volgende informatie vastgelegd:
- **Datum van het verzoek** (afgerond naar de dichtstbijzijnde dag)
- **QGIS versie** die gebruikt wordt
- **Land gebruiker** (bepaald uit het IP-adres, dat onmiddellijk wordt genegeerd)
- **Platform besturingssysteem**

Geen persistente of persoonlijk te identificeren informatie wordt opgeslagen of gedeeld. Het IP-adres wordt alleen gebruikt om het land te identificeren en wordt niet behouden. Gegevens worden elk uur samengevoegd in overzichtstabellen voor datum, land, versie van QGIS en platform. Dat helpt het team van QGIS om de gebruikspatronen te begrijpen en inspanningen voor ontwikkeling te prioriteren.

**Deelnemen is optioneel:** Gebruikers kunnen de mogelijkheid voor de news feed in QGIS op elk moment uitschakelen.

Voor vragen of zorgen, neem contact op met het QGIS Project Steering Committee op [info@qgis.org](mailto:info@qgis.org).
## QGIS Plugins dashboard Analytics 
Het **QGIS Plugins Analytics Dashboard** ([https://plugins-analytics.qgis.org](https://plugins-analytics.qgis.org)) verzamelt minimale, niet te identificeren gebruiksgegevens elke keer als een plug-in wordt gedownload vanuit QGIS Plug-ins beheren en installeren of de [website QGIS Plugins](https://plugins.qgis.org). De volgende informatie wordt vastgelegd:
- **Datum downloaden** (afgerond naar de dichtstbijzijnde dag)
- **Versie plug-in** die werd gedownload
- **Land gebruiker** (bepaald uit het IP-adres, dat onmiddellijk wordt genegeerd)

Geen persistente of persoonlijk te identificeren informatie wordt opgeslagen of gedeeld. Het IP-adres wordt alleen gebruikt om het land te identificeren en wordt niet behouden.
- **Downloadactiviteit** wordt vastgelegd vanaf **16 juli 2024**
- **Statistieken per land** zijn verzameld vanaf **30 mei 2024**

Populariteit van de plug-in wordt berekend met de formule:
```
downloads * (1 + (rating_score / (rating_votes + 0.01) / 3))
```
Deze gegevens helpen het team van QGIS het gebruik van plug-ins te begrijpen en het ecosysteem voor plug-ins te verbeteren.

Voor eventuele vragen of zorgen, neem contact op met het QGIS Project Steering Committee op [info@qgis.org](mailto:info@qgis.org).

{{<content-end >}}
