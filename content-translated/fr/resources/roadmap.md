---
HasBanner: false
draft: false
sidebar: true
title: Feuille de route
type: page

---
{{<content-start >}}
# Feuille de route
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Abonnez-vous au calendrier iCalendar de la feuille de route" >}}

Les versions et le développement de QGIS suivent un calendrier (feuille de route).
- Les versions à numéros pairs (2.18, 3.2, etc.) sont des versions stables.
- Les versions à numéros impairs (2.99, 3.1, etc.) sont des versions de développement.

Les sorties se feront tous les quatre mois. Dans les trois premiers mois, les développements nouveaux seront effectués. Ensuite, intervient une phase de gel des nouvelles fonctionnalités permettant de consacrer le dernier mois aux tests, corrections de bugs, traductions et préparations des sorties. Lorsque la date de sortie arrive, une branche avec un numéro pair est créée tandis que la branche master prend le numéro de version impair suivant. S'ensuit un appel à la compilation et le packaging du logiciel pour les différents systèmes d'exploitation.

Toutes les trois publications (en commençant par la 2.8), la version sera maintenue à long terme (LTR) jusqu'à la prochaine publication à long terme.
## Phase de développement
Dans la phase de développement, les développeurs travaillent à l'ajout des nouvelles fonctionnalités de la prochaine version. Les adopteurs précoces peuvent déjà utiliser les versions nightly disponibles sur les plateformes majeures afin de suivre la progression des développements, faire des tests préliminaires et fournir des rapports de bogue et leurs idées pour aider le développement.
## Gel des fonctionnalités
Pendant la phase de gel des fonctionnalités, aucune nouvelle fonctionnalité n'est plus acceptée et l'attention de tous passe de l'amélioration de QGIS à sa stabilisation. Cela transforme également les versions quotidiennes (nightly builds) en [préreleases](#qgis-prereleases).

**Les utilisateurs** sont invités à procéder à des tests approfondis de ces versions préliminaires dans leur environnement afin de s'assurer qu'elles ne contiennent aucun problème qu'ils ne souhaiteraient pas voir apparaître dans la prochaine version. Tous les problèmes de ce type doivent être signalés (voir [Bugs, fonctionnalités et problèmes]({{< ref "resources/support/bug-reporting" >}})). Tout ce qui passe inaperçu se retrouvera également dans la prochaine version. Ce n'est qu'en cas de problèmes graves que des corrections seront réintégrées dans une version plus récente. Il est donc très important de tester les préversions et de signaler les problèmes.

Pendant le gel des fonctionnalités, les **développeurs** surveillent le dépôt de bogues et commencent à travailler à la résolution des problèmes signalés. Ils mettent aussi à jour le "Journal des modifications" avec les nouvelles fonctionnalités.

Avec le démarrage du gel des fonctionnalités sont mis à jour les fichiers de traduction afin que les **traducteurs** puissent démarrer leur travail. Notez que ceci peut induire une procédure en boucle, les résolutions de bogues pouvant induire des modifications dans les textes à traduire.

Un gel total est initié deux semaines avant la sortie, durant lequel ne sont acceptées que les résolutions de problèmes et régressions graves introduits après le gel des fonctionnalités.

Le responsable de publication l'annonce lors du gel des fonctionnalités.
## Sortie
Lors des dates de publication des versions majeures et mineures, la branche de publication est créée, la version est balisée et les archives tar sont préparées. Pour les versions mineures, seules la balise est ajoutée et les archives tar sont créées.

Les compilateurs de logiciels sont notifiés que la compilation peut commencer.

Lorsque des packages sont disponibles la sortie peur être annoncée et le site web est mis à jour.
## Calendrier de sortie
Le calendrier de sortie des versions est organisé de manière à ce qu'elles aient lieu aux mêmes dates chaque année suivant le rythme d'une version tous les quatre mois et une version à long terme LTR à la fin du mois de février.

À partir de la version 2.12, la phase de développement dure toujours 12 semaines et la phase de gel au moins 5 semaines. Le temps restant est utilisé pour prolonger la phase de gel des versions LTR.

Des mises à jour mineures seront publiées chaque mois sur la branche de la dernière version, s'il y a des rétroportages. À partir de la version 3.28, les mises à jour mineures ne seront effectuées qu'avec les nouvelles versions les plus récentes.

Au cours des quatre premiers mois suivant sa publication, une nouvelle version LTR fait également office de version LR actuelle. Au cours de cette phase, la nouvelle version LTR ne remplace pas la version LTR précédente dans les dépôts LTR. Ce remplacement intervient dès la publication d'une nouvelle version LR.

Ce calendrier est également disponible au format [“iCalendar”](https://qgis.org/schedule.ics).
### Programme
{{< csv-table file="csv/schedule.csv" />}}
### Légende des évènements
| Abréviation | Description |
| --- | --- |
| LTR | Version maintenue à long terme, début d'une nouvelle phase de développement |
| LR | Version régulière, début d'une nouvelle phase de développement |
| FF | Gel des fonctionnalités, fin de la phase de développement |
| PR | Version ponctuelle de la dernière version et de la branche LTR |
| EPR | Version ponctuelle supplémentaire |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> suivant </span> | <span class="rm-next"> prochaines releases </span> |

## Localisation des pré-versions / nightly builds{#qgis-prereleases }
| Plateforme | Emplacement |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
