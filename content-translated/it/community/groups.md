---
HasBanner: false
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
title: Gruppi Utenti
type: page

---
{{<content-start >}}
# Gruppi Utenti
Local user groups bring QGIS users together in their own country and language. They run meetings, share know how and help shape QGIS. This page explains how a group works and how to start one.

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## Find a group near you
Search the groups by name, country or continent. Switch between cards and a sortable table.

{{<button class="is-success" link="/community/groups/list/" text="Browse the list" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "groups" "/community/groups/list/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}

{{<rich-box-start layoutClass="has-right rounded" >}}

{{<rich-content-start themeClass="coloring-1" >}}
## See the groups on a map
Every highlighted country has a local group. Select a logo to meet the group.

{{<button class="is-success" link="/community/groups/map/" text="Open the map" >}}

{{<rich-content-end >}}

{{<rich-right-start >}}

{{<user-groups-stats "countries" "/community/groups/map/" >}}

{{<rich-right-end >}}

{{<rich-box-end >}}
## Obiettivi di un gruppo di utenti
* Organizzazione di incontri per gli utenti
* Coordinamento dello sviluppo, con particolare attenzione agli standard e ai requisiti regionali/nazionali
* Diffusione delle informazioni su QGIS: incontri, articoli su riviste specializzate in GIS, informazioni su QGIS nei social media, forum di discussione sul GIS, ecc.
* Raccolta di casi di studio dell'uso locale di QGIS
* Sponsorizzazione: i gruppi di utenti locali sono incoraggiati a raccogliere quote associative annuali ragionevoli (a seconda del Paese). I fondi raccolti possono essere utilizzati per finanziare lo sviluppo di funzionalità rilevanti, aiutare nella correzione di bug o come donazione al progetto internazionale QGIS.
* Costituzione di gruppi di interesse, ad esempio topografia, urbanistica, client server/web, ecc.
* Inizializzazione / coordinamento di moduli applicativi, ad esempio, topografia, urbanistica, client / server web, ecc.
* Eleggere un rappresentante che agisca come [Membro Votante QGIS]({[< ref "/community/organisation#voting-members" >]})

## Presupposti generali/raccomandazioni
* I gruppi di utenti locali dovrebbero rimanere neutrali rispetto a fornitori e aziende
* istituisce strutture democratiche per il consiglio direttivo locale, votando e prendendo decisioni importanti
* rimanere trasparenti, specialmente se avete a che fare con le quote associative e le spese di gestione
* informare di tanto in tanto il progetto internazionale sulle vostre attività locali

## Organizzazione
A seconda del vostro paese, potrebbe essere costituita un'entità giuridica più piccola, ad esempio un'associazione. A seconda della legislazione locale, una tale entità implica che vi riuniate almeno una volta all'anno (assemblea generale), pubblicate un rapporto annuale e mettete il rapporto finanziario a disposizione dei vostri membri. Spesso implica anche la creazione di statuti.

Statuti del gruppo degli utenti svizzeri QGIS come esempio:
* German (master): [https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf](https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf)
* French (traduzione): [https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf](https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf)

Moduli di domanda di adesione:
* German: [https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf](https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf)
* French: [https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf](https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf)

È possibile utilizzare questi statuti e i moduli di domanda di adesione come riferimento, adattandoli alla vostra situazione locale.
## Dominio del paese locale qgis.xx
User groups can register their local country domains, e.g. qgis.ch or qgis.uk. If the domain is already taken by another organization, company or person, please negotiate if you can transfer the owner to the local QGIS user group. The QGIS international project has registered [QGIS as a trademark](../organisation/guidelines), which should help you during your negotiations.
## Sito internet
Il sito web del gruppo locale dovrebbe essere utilizzato per pubblicare qualsiasi materiale relativo alle informazioni e alla gestione del gruppo utenti. Per esempio, le riunioni degli utenti, i casi di studio, materiale condiviso, forum di discussione, ecc. Il materiale pubblico dovrebbe essere reso disponibile senza requisiti di accesso (ad esempio, non richiedere alle persone interessate di essere un membro di un social network come Facebook o Google+). L'utilizzo dei social network è consigliato ma non dovrebbe essere l'unico canale di informazione. I feed RSS dovrebbero essere resi disponibili sul sito Web del gruppo di utenti QGIS.

Buona fortuna con l'organizzazione del vostro gruppo locale degli utenti. Si prega di informare il team di QGIS internazionale registrando l'elenco comunità QGIS e fornendo un rapporto sui vostri progressi. Non esitate a chiedere domande riguardanti la creazione e la manutenzione del gruppo locale degli utenti.
## Pacchetto iniziale
### Hosting di sottodominio QGIS.org
User groups are encouraged to use the official QGIS.org branding and host the user group's website on a QGIS.org subdomain (e.g., `sweden.qgis.org`), you can utilize the provided template repository at [https://github.com/qgis/QGIS-User-Group-Website](https://github.com/qgis/QGIS-User-Group-Website). This option ensures consistency with the main QGIS website design. Please carefully read and follow the setup instructions provided in the repository.
### Accesso all'invio di notizie al QGIS News Feed 
I gruppi utenti locali possono richiedere l'accesso al sistema QGIS News Feed, che consente di inviare notizie (come eventi, campagne di crowdfunding, meetup o annunci) che appariranno nella sezione notizie di QGIS una volta approvate dai moderatori. Questo è un ottimo modo per condividere le attività del proprio gruppo con la comunità QGIS globale.
### Modello per il dominio nazionale locale qgis.xx 
If you do not wish to use the QGIS.org subdomain hosting you can design your website using the template provided at [https://github.com/qgis/qgis-template.github.io](https://github.com/qgis/qgis-template.github.io) or create your own from scratch.

{{<content-end >}}
