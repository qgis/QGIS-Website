---
HasBanner: false
Reviewed: 1 June 2024
Reviewer: Tim Sutton
draft: false
sidebar: true
title: Groupes d'utilisateurs
type: page

---
{{<content-start >}}
# Groupes d'utilisateurs
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
## Objectifs d'un groupe d'utilisateurs
* Organisation des rencontres utilisateurs
* Coordination du développement, en mettant l'accent sur les normes et les exigences régionales et nationales
* Diffusion d'informations sur QGIS : réunions, articles dans des revues spécialisées en SIG, publications sur QGIS dans les réseaux sociaux, forums de discussion sur les SIG, etc.
* Collecte d'études de cas des usages locaux de QGIS
* Parrainage : les groupes d'utilisateurs locaux sont encouragés à percevoir des cotisations annuelles raisonnables (en fonction du pays). Les fonds ainsi collectés peuvent servir à financer le développement de fonctionnalités pertinentes, à contribuer à la correction de bogues ou à faire un don au projet international QGIS.
* Mise en place de groupes d’intérêt, par ex. enquête, planification urbaine, client/serveur web, etc.
* Initialisation/coordination des modules de l'application, par ex. enquête, planification urbaine, client/serveur web, etc.
* Élire un représentant pour occuper la fonction de [membre votant de QGIS]({{< ref "/community/organisation#voting-members" >}})

## Propositions et recommandations générales
* les groupes d'utilisateurs locaux doivent rester indépendants des fournisseurs et des entreprises
* mettre en place des structures démocratiques pour le comité de pilotage local, afin de permettre le vote et la prise de décisions importantes
* restez transparents, surtout en ce qui concerne les cotisations et la manière dont vous les utilisez
* informer le projet international de temps en temps sur les activités locales

## Organisation
Selon votre pays, il est possible de créer une entité juridique de plus petite taille, par exemple une association ou une organisation à but non lucratif. En fonction de la législation locale, une telle entité implique que vous vous réunissiez au moins une fois par an (assemblée générale), que vous publiiez un rapport annuel et que vous mettiez le rapport financier à la disposition de vos membres. Souvent, cela implique également la rédaction de statuts.

Statuts du groupe suisse des utilisateurs QGIS pour exemple:
* Allemand (master) : [https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf](https://www.qgis.ch/assets/pdf/StatutenderQGISAnwendergruppeSchweiz.pdf)
* Français (translation) : [https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf](https://www.qgis.ch/assets/pdf/StatutsdugroupedutilisateursQGISSuisse.pdf)

Formulaires de demande d'adhésion :
* Allemand : [https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf](https://www.qgis.ch/assets/pdf/QGIS%20Usergruppe%20Beitrittserklaerung.pdf)
* French: [https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf](https://www.qgis.ch/assets/pdf/QGIS%20groupe%20d%20utilisateurs%20Suisse%20declaration%20d%20adhesion.pdf)

Vous pouvez vous référer à ces statuts et formulaires d'adhésion et les adapter selon les besoins à votre situation locale.
## Noms de domaine nationaux qgis.xx
User groups can register their local country domains, e.g. qgis.ch or qgis.uk. If the domain is already taken by another organization, company or person, please negotiate if you can transfer the owner to the local QGIS user group. The QGIS international project has registered [QGIS as a trademark](../organisation/guidelines), which should help you during your negotiations.
## Site web
Le site web de votre groupe d'utilisateurs local doit servir à publier tout contenu relatif aux informations et à la gestion du groupe. Il peut s'agir, par exemple, des réunions d'utilisateurs, d'études de cas, de documents partagés, de forums de discussion, etc. Les documents publics doivent être accessibles sans obligation de connexion (par exemple, ne pas exiger des personnes intéressées qu'elles soient membres d'un réseau social tel que Facebook ou Google+). L'utilisation des réseaux sociaux est recommandée, mais ne doit pas constituer le seul canal d'information. Des flux RSS doivent être mis à disposition sur le site web du groupe d'utilisateurs QGIS.

Bonne chance pour la mise en place de votre groupe d'utilisateurs local ! Merci d'en informer l'équipe internationale de QGIS en vous inscrivant à la liste de diffusion de la communauté QGIS et en nous tenant au courant de l'avancement de votre projet. N'hésitez pas à nous poser des questions concernant la création et la gestion de votre groupe d'utilisateurs local.
## Kit de démarrage
### Hébergement de sous-domaines QGIS.org
User groups are encouraged to use the official QGIS.org branding and host the user group's website on a QGIS.org subdomain (e.g., `sweden.qgis.org`), you can utilize the provided template repository at [https://github.com/qgis/QGIS-User-Group-Website](https://github.com/qgis/QGIS-User-Group-Website). This option ensures consistency with the main QGIS website design. Please carefully read and follow the setup instructions provided in the repository.
### Accès à la soumission d'articles pour le fil d'actualités QGIS
Les groupes d'utilisateurs locaux peuvent demander à accéder au [système de fil d'actualités QGIS](https://feed.qgis.org), qui vous permet de soumettre des actualités (telles que des événements, des campagnes de financement participatif, des rencontres ou des annonces) qui apparaîtront dans la section Actualités de QGIS une fois approuvées par les modérateurs. C'est un excellent moyen de faire connaître les activités de votre groupe à la communauté mondiale de QGIS.
### Modèle pour le domaine national qgis.xx
If you do not wish to use the QGIS.org subdomain hosting you can design your website using the template provided at [https://github.com/qgis/qgis-template.github.io](https://github.com/qgis/qgis-template.github.io) or create your own from scratch.

{{<content-end >}}
