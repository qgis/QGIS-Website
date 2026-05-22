---
HasBanner: false
draft: false
sidebar: true
title: Aggiungi la tua organizzazione all'elenco dei contributori di QGIS
type: page

---
{{<content-start >}}
# Aggiungi la tua organizzazione all'elenco dei contributori di QGIS
Benvenuto! Se la tua organizzazione contribuisce a QGIS, può essere inserita nella nostra [pagina dei contributori](/community/contributors/). Segui questi semplici passaggi:
____
## Fase 1: Prepara i dati della tua organizzazione
### Che cosa ti serve:
- ✅ Nome della tua organizzazione, slogan e URL del sito web
- ✅ Breve descrizione del tuo coinvolgimento in QGIS
- ✅ Nomi utente GitHub dei membri del team che contribuiscono a QGIS
- ✅ Logo della tua organizzazione (in formato PNG o SVG, ottimizzato per il web)

____
## Fase 2: Compila il modello
Copia questo modello e personalizzalo con i dati della tua organizzazione:
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
### Guida pratica:
| Campo | Descrizione | Esempio |
| --- | --- | --- |
| **nome** | Denominazione completa della tua organizzazione | `"Kartoza"` |
| **sottotitolo** | Breve slogan o motto | "Mappare il futuro" |
| **immagine** | Nome file del logo (aggiungi a `static/img/contributors/`) | `"img/contributors/kartoza-logo.png"` |
| **larghezza** | Larghezza visualizzazione logo | `"200px"` (lasciare così com'è) |
| **url** | Il tuo sito web | `"https://kartoza.com"` |
| **descrizione** | Breve descrizione (2-3 frasi) | `"Kartoza offre soluzioni GIS open source..."` |
| **membri** | Nomi utente GitHub dei membri del tuo team | Vedi sotto |
| **contributi** | Lascia così com'è: aggiornamento automatico da script | Conserva gli zeri e i valori nulli |

### Spiegazione dell'array dei membri:
- **nome utente**: nome utente GitHub (deve corrispondere esattamente)
- **author_names**: Full name as it appears in Git commits. `"Jean Luc"` or `"Jean Luc,Jean Lucas"` for multiple names.
- **from**: Date when this person started contributing for your org (YYYY-MM-DD)
- **to**: Leave as `null` if still active, or add end date (YYYY-MM-DD)

💡 **Tip:** You can add multiple members—just duplicate the member object for each person.
____
## Step 3: Submit via GitHub Pull Request
### Option A: Use GitHub's Web Editor (Easiest)
1. **Clicca qui per modificare direttamente il file:** [Modifica organizations.json](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - GitHub will automatically fork the repository for you
2. **Scroll to the bottom** of the file
3. **Add a comma** after the last `}` of the previous entry
4. **Paste your organization entry** (from Step 2)
5. **Clicca su "Salva modifiche"** e inserisci una descrizione del tipo: *"Aggiungi [Nome della tua organizzazione] ai contributori"*
6. **Create a Pull Request** by clicking the green button

### Option B: Fork and Clone (For Advanced Users)
1. Fork the [QGIS-Website repository](https://github.com/qgis/QGIS-Website/)
2. Clone your fork locally
3. Aggiungi la tua voce al file `data/contributors/organizations.json`
4. Aggiungi il tuo logo nella cartella `static/img/contributors/` (ottimizza le dimensioni del file!)
5. Commit and push your changes
6. [Open a Pull Request](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **Important:** Make sure your JSON is valid! Use a [JSON validator](https://jsonlint.com/) if needed.
____
## Step 4: Add Your Logo
Carica il tuo logo nella cartella `static/img/contributors/`:
- **Formato:** PNG o SVG
- **Size:** Optimize for web (aim for under 100KB)
- **Dimensions:** Width around 400-600px works well
- **Naming:** Use lowercase and hyphens (e.g., `acme-geospatial.png`)

____
## Step 5: Review & Approval
✨ Once you submit your Pull Request:
1. The QGIS website team will review your submission
2. We may ask for minor adjustments
3. Una volta approvata e aggiunta, la tua organizzazione apparirà nella [pagina dei contributori](/community/contributors/)!

____
Thank you for contributing to QGIS! 🎉

{{<content-end >}}
