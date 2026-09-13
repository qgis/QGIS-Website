---
HasBanner: false
draft: false
sidebar: true
title: Voeg uw organisatie toe aan deelnemers aan QGIS
type: page

---
{{<content-start >}}
# Voeg uw organisatie toe aan deelnemers aan QGIS
Welkom! Als uw organisatie bijdraagt aan QGIS, kunt u worden vermeld op onze [pagina met deelnemers](/community/contributors/). Volg deze eenvoudige stappen:
____
## Stap 1: Bereid de details voor uw organisatie voor
### Wat u nodig zult hebben:
- ✅ De naam, tagregel en URL voor de website van uw organisatie
- ✅ Een korte beschrijving van uw betrokkenheid bij QGIS
- ✅ GitHub gebruikersnamen of teamleden die bijdragen aan QGIS
- ✅ Het logo van uw organisatie (PNG of SVG, geoptimaliseerd voor web)

____
## Stap 2: Vul het sjabloon in
Kopieer dit sjabloon en pas het aan met de informatie van uw organisatie:
```
{
  "name": "Your Organization Name",
  "subtitle": "Your tagline or motto",
  "image": "img/contributors/your-logo.png",
  "width": "200px",
  "url": "https://your-website.com",
  "description": "Brief description of your organization and how you contribute to QGIS.",
  "members": [
    {
      "username": "github_username",
      "author_names": "Full Name",
      "from": "2020-01-15",
      "to": null
    }
  ],
  "contributions": {
    "documentation": { "commits": 0, "last_contribution": null },
    "qgis_core": { "commits": 0, "last_contribution": null },
    "web_sites": { "commits": 0, "last_contribution": null }
  }
}
```
### Richtlijnen velden:
| Veld | Beschrijving | Voorbeeld |
| --- | --- | --- |
| **naam** | De volledige naam van uw organisatie | `"Kartoza"` |
| **subtitel** | Korte tagregel of motto | `"De toekomst in kaart brengen"` |
| **afbeelding** | Bestandsnaam logo (toevoegen aan `static/img/contributors/`) | `"img/contributors/kartoza-logo.png"` |
| **breedte** | Breedte voor weergave logo | `"200px"` (behouden zoals het is) |
| **URL** | Uw website | `"https://kartoza.com"` |
| **beschrijving** | Korte beschrijving (2-3 zinnen) | `"Kartoza maakt open-source GIS-oplossingen…"` |
| **leden** | GitHub gebruikersnamen van uw teamleden | Zie hieronder |
| **bijdragen** | Laat dit zoals het is—automatisch bijgewerkt door scripts | Nullen en nulwaarden behouden |

### Uitleg lijst met leden:
- **gebruikersnaam**: GitHub gebruikersnaam (moet exact overeenkomen)
- **autheur_namen**: Volledige naam, zoals die verschijnt in commits van Git. `"Jean Luc"` of `"Jean Luc,Jean Lucas"` voor meerdere namen.
- **vanaf**: Datum wanneer deze persoon begon met het bijdragen voor uw organisatie (JJJJ-MM-DD)
- **tot en met**: Laat als `null` indien nog steeds actief, of voer de einddatum in (JJJJ-MM-DD)

💡 **Tip:** U mag meerdere leden toevoegen—dupliceer gewoon het object lid voor elke persoon.
____
## Stap 3: Indienen via GitHub Pull Request
### Optie A: GitHub's Web Editor gebruiken (gemakkelijkst)
1. **Klik hier om het bestand direct te bewerken:** [Bewerken van organizations.json](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - GitHub zal automatisch de opslagruimte voor u forken
2. **Scroll naar het einde** van het bestand
3. **Voeg een komma toe** na de laaste `}` of het vorige item
4. **Plak het item van uw organisatie** (van Stap 2)
5. **Klik op "Wijzigingen indienen"** en geef een beschrijving op zoals: *"Toevoegen [naam van uw organisatie] aan bijdragers"*
6. **Maak een Pull Request** door op de groene knop te klikken

### Optie B: Forken en klonen (voor gevorderde gebruikers)
1. Fork de [opslagplaats QGIS-Website](https://github.com/qgis/QGIS-Website/)
2. Kloon uw fork lokaal
3. Voeg uw item toe aan `data/contributors/organizations.json`
4. Voeg uw logo toe aan `static/img/contributors/` (optimaliseer de bestandsgrootte!)
5. Commit en push uw wijzigingen
6. [Open een Pull Request](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **Belangrijk:** Zorg ervoor dat uw JSON gevalideerd is! Gebruik indien nodig een [JSON-validator](https://jsonlint.com/).
____
## Stap 4: Voeg uw logo toe
Upload uw logo naar de map `static/img/contributors/`:
- **Indeling:** PNG of SVG
- **Grootte:** Geoptimaliseerd voor web (probeer onder de 100KB te blijven)
- **Afmetingen:** Breedte rond 400-600px werkt goed
- **Naam geven:** gebruik kleine letters en afbreekstreepjes (bijv. `acme-geospatial.png`)

____
## Stap 5: Beoordelen en goedkeuren
✨ Als uw Pull Request is ingediend:
1. Het websiteteam van QGIS zal uw bijdrage beoordelen
2. We zouden kleine aanpassingen kunnen vragen
3. Eenmaal goedgekeurd en gemerged zal uw organisatie verschijnen op de [pagina met bijdragers](/community/contributors/)!

____
Dank u voor uw bijdragen aan QGIS! 🎉

{{<content-end >}}
