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

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- Les versions à numéros pairs (2.18, 3.2, etc.) sont des versions stables.
- Les versions à numéros impairs (2.99, 3.1, etc.) sont des versions de développement.

Les sorties se feront tous les quatre mois. Dans les trois premiers mois, les développements nouveaux seront effectués. Ensuite, intervient une phase de gel des nouvelles fonctionnalités permettant de consacrer le dernier mois aux tests, corrections de bugs, traductions et préparations des sorties. Lorsque la date de sortie arrive, une branche avec un numéro pair est créée tandis que la branche master prend le numéro de version impair suivant. S'ensuit un appel à la compilation et le packaging du logiciel pour les différents systèmes d'exploitation.

Toutes les trois publications (en commençant par la 2.8), la version sera maintenue à long terme (LTR) jusqu'à la prochaine publication à long terme.
## Phase de développement
Dans la phase de développement, les développeurs travaillent à l'ajout des nouvelles fonctionnalités de la prochaine version. Les adopteurs précoces peuvent déjà utiliser les versions nightly disponibles sur les plateformes majeures afin de suivre la progression des développements, faire des tests préliminaires et fournir des rapports de bogue et leurs idées pour aider le développement.
## Gel des fonctionnalités
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

Pendant le gel des fonctionnalités, les **développeurs** surveillent le dépôt de bogues et commencent à travailler à la résolution des problèmes signalés. Ils mettent aussi à jour le "Journal des modifications" avec les nouvelles fonctionnalités.

Avec le démarrage du gel des fonctionnalités sont mis à jour les fichiers de traduction afin que les **traducteurs** puissent démarrer leur travail. Notez que ceci peut induire une procédure en boucle, les résolutions de bogues pouvant induire des modifications dans les textes à traduire.

Un gel total est initié deux semaines avant la sortie, durant lequel ne sont acceptées que les résolutions de problèmes et régressions graves introduits après le gel des fonctionnalités.

Le responsable de publication l'annonce lors du gel des fonctionnalités.
## Sortie
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Les compilateurs de logiciels sont notifiés que la compilation peut commencer.

Lorsque des packages sont disponibles la sortie peur être annoncée et le site web est mis à jour.
## Calendrier de sortie
Le calendrier de sortie des versions est organisé de manière à ce qu'elles aient lieu aux mêmes dates chaque année suivant le rythme d'une version tous les quatre mois et une version à long terme LTR à la fin du mois de février.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Programme
{{<csv-table file="csv/schedule.csv" >}}
### Légende des évènements
| Abbreviation | Description |
| --- | --- |
| LTR | Version maintenue à long terme, début d'une nouvelle phase de développement |
| LR | Version régulière, début d'une nouvelle phase de développement |
| FF | Gel des fonctionnalités, fin de la phase de développement |
| PR | Version ponctuelle de la dernière version et de la branche LTR |
| EPR | Version ponctuelle supplémentaire |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |

## Localisation des pré-versions / nightly builds{#qgis-prereleases }
| Plateforme | Emplacement |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
