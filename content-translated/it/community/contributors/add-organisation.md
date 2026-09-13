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
## Fase 1: prepara i dati della tua organizzazione
### Che cosa ti serve:
- ✅ Nome della tua organizzazione, slogan e URL del sito web
- ✅ Breve descrizione del tuo coinvolgimento in QGIS
- ✅ Nomi utente GitHub dei membri del team che contribuiscono a QGIS
- ✅ Logo della tua organizzazione (in formato PNG o SVG, ottimizzato per il web)

____
## Fase 2: compila il modello
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
- **author_names**: nome completo così come appare nei commit Git. `"Jean Luc"` o `"Jean Luc,Jean Lucas"` in caso di nomi multipli.
- **da**: data in cui questa persona ha iniziato a collaborare con la tua organizzazione (AAAA-MM-GG)
- **a**: Lasciare `null` se ancora attivo, oppure inserire la data di fine (AAAA-MM-GG)

💡 **Suggerimento:** puoi aggiungere più membri: basta duplicare l'oggetto "membro" per ogni persona.
____
## Fase 3: invia tramite pull request su GitHub
### Opzione A: Utilizza l'editor web di GitHub (il metodo più semplice)
1. **Clicca qui per modificare direttamente il file:** [Modifica organizations.json](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - GitHub creerà automaticamente un fork del repository per te
2. **Scorri fino alla fine** del file
3. **Aggiungi una virgola** dopo l'ultima `}` della riga precedente
4. **Inserisci i dati della tua organizzazione** (dal Passaggio 2)
5. **Clicca su "Salva modifiche"** e inserisci una descrizione del tipo: *"Aggiungi [Nome della tua organizzazione] ai contributori"*
6. **Crea una Pull Request** cliccando sul pulsante verde

### Opzione B: Fork e Clona (per utenti esperti)
1. Crea un fork del [repository del sito web di QGIS](https://github.com/qgis/QGIS-Website/)
2. Clona il tuo fork in locale
3. Aggiungi la tua voce al file `data/contributors/organizations.json`
4. Aggiungi il tuo logo nella cartella `static/img/contributors/` (ottimizza le dimensioni del file!)
5. Salva e invia le modifiche
6. [Apri una pull request](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **Importante:** assicurati che il tuo JSON sia valido! Se necessario, usa un [validatore JSON](https://jsonlint.com/).
____
## Fase 4: aggiungi il tuo logo
Carica il tuo logo nella cartella `static/img/contributors/`:
- **Formato:** PNG o SVG
- **Dimensioni:** ottimizza per il web (cerca di non superare 100 kB)
- **Dimensioni:** una larghezza compresa tra circa 400 e 600 px è l'ideale
- **Denominazione:** utilizzare lettere minuscole e trattini (ad es., `acme-geospatial.png`)

____
## Fase 5: revisione e approvazione
✨ Una volta inviata la tua Pull Request:
1. Il team del sito web di QGIS esaminerà il tuo contributo
2. Potremmo richiedere alcune piccole modifiche
3. Una volta approvata e aggiunta, la tua organizzazione apparirà nella [pagina dei contributori](/community/contributors/)!

____
Grazie per il tuo contributo a QGIS! 🎉

{{<content-end >}}
