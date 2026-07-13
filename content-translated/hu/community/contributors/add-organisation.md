---
HasBanner: false
draft: false
sidebar: true
title: Adja hozzá szervezetét a QGIS közreműködői közé
type: page

---
{{<content-start >}}
# Adja hozzá szervezetét a QGIS közreműködői közé
Üdvözöljük! Ha szervezete hozzájárul a QGIS fejlesztéséhez, akkor felkerülhet a [hozzájárulók oldalára](/community/contributors/). Kövesse az alábbi egyszerű lépéseket:
____
## 1. lépés: Adja meg a szervezet adatait
### Amire szüksége lesz:
- ✅ A szervezet neve, szlogenje és weboldalának URL-címe
- ✅ A QGIS-ben betöltött szerepének rövid leírása
- ✅ A QGIS-hez hozzájáruló csapattagok GitHub-felhasználónevei
- ✅ A szervezeted logója (PNG vagy SVG formátumban, webes használatra optimalizálva)

____
## 2. lépés: Töltse ki a sablont
Másolja át ezt a sablont, és töltse ki a szervezetére vonatkozó adatokkal:
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
### Útmutató a mezőkhöz
| Mező | Leírás | Példa |
| --- | --- | --- |
| **name** | A szervezet teljes neve | `"Kartoza"` |
| **subtitle** | Rövid szlogen vagy mottó | `„A jövő feltérképezése”` |
| **image** | A logó fájlneve (helyezze el a `static/img/contributors/` mappába) | `"img/contributors/kartoza-logo.png"` |
| **width** | A logó megjelenítési szélessége | `"200px"` (maradjon így) |
| **url** | Az ön weboldala | `"https://kartoza.com"` |
| **description** | Rövid leírás (2–3 mondat) | `"A Kartoza nyílt forráskódú GIS-megoldásokat kínál..."` |
| **members** | A csapattagok GitHub-felhasználónevei | Lásd alább |
| **contributions** | Hagyja így – a szkriptek automatikusan frissítik | A nullák és a null értékek megőrzése |

### A Members tömb bemutatása:
- **username**: GitHub-felhasználónév (pontosan meg kell egyeznie)
- **author_names**: A Git-commitekben szereplő teljes név. Több név esetén `"Jean Luc"` vagy `"Jean Luc,Jean Lucas"`.
- **from**: Az a dátum, amikor a személy elkezdett közreműködni a szervezetben (ÉÉÉÉ-HH-NN)
- **to**: Ha még aktív, hagyja `null`-ként, vagy adja meg a végdátumot (ÉÉÉÉ-HH-NN)

💡 **Tipp:** Több tagot is hozzáadhat – ehhez egyszerűen másolja le a members objektumot minden egyes személy számára.
____
## 3. lépés: Beküldés GitHub pull requesten keresztül
### A. lehetőség: Használja a GitHub webes szerkesztőjét (legegyszerűbb)
1. **Kattintson ide a fájl közvetlen szerkesztéséhez:** [Szerkessze az organizations.json fájlt](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - A GitHub automatikusan létrehozza a tároló másolatát az Ön számára
2. **Görgessen a fájl aljára**
3. **Illesszen be egy vesszőt** az előző bejegyzés utolsó `}` jele után
4. **Illessze be a szervezet adatait** (a 2. lépésből)
5. **Kattintson a „Változtatások mentése” gombra**, és írja be a következő leírást: *"Add [szervezet neve] to contributors"*
6. **Készítsen pull requestet** a zöld gombra kattintva

### B. lehetőség: Forkolás és klónozás (haladó felhasználóknak)
1. Készítsen forkot a [QGIS-weboldal tárolójáról](https://github.com/qgis/QGIS-Website/)
2. Klónozza a forkot a gépére
3. Adja hozzá a bejegyzését a `data/contributors/organizations.json` fájlhoz
4. Adja hozzá a logóját a `static/img/contributors/` mappához (optimalizálja a fájl méretét!)
5. Commitolja a módosításokat, majd pusholja
6. [Nyisson egy pull requestet](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **Fontos:** Győződjön meg róla, hogy a JSON-fájl érvényes! Szükség esetén használjon [JSON-érvényesítőt](https://jsonlint.com/).
____
## 4. lépés: Logó hozzáadása
Töltse fel a logóját a `static/img/contributors/` mappába:
- **Format:** PNG or SVG
- **Size:** Optimize for web (aim for under 100KB)
- **Dimensions:** Width around 400-600px works well
- **Naming:** Use lowercase and hyphens (e.g., `acme-geospatial.png`)

____
## Step 5: Review & Approval
✨ Once you submit your Pull Request:
1. The QGIS website team will review your submission
2. We may ask for minor adjustments
3. Once approved and merged, your organization will appear on the [contributors page](/community/contributors/)!

____
Thank you for contributing to QGIS! 🎉

{{<content-end >}}
