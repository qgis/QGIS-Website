---
HasBanner: false
draft: false
sidebar: true
title: Roteiro
type: page

---
{{<content-start >}}
# Roteiro
{{<roadmap >}}

{{<button class="is-primary1 is-rounded" link="https://qgis.org/schedule.ics" text="Subscribe to the roadmap iCalendar" >}}

Releases and development of QGIS follow a timebased schedule (roadmap).
- Os números pares da versão (2.18, 3.2 etc) são versões de lançamento.
- Os números ímpares da versão (2.99, 3.1 etc) são versões de desenvolvimento.

Um novo lançamento acontecerá a cada quatro meses. Nos primeiros três meses, novos desenvolvimentos estão ocorrendo. No último mês antes de um lançamento, um congelamento de recursos é invocado e o último mês é usado para testes, correção de bugs, tradução e preparações de lançamento. Quando o lançamento acontece, uma ramificação com um número de liberação par é criada e a ramificação mestre avança para a próxima versão ímpar. Após o lançamento, é feito um chamado para empacotamento.

Sempre a cada terceiro lançamento (iniciando na versão 2.8), teremos uma versão de longo tempo de lançamento (LTR) que será mantida até a próxima edição LTR.
## Fase de desenvolvimento
Na fase de desenvolvimento, os desenvolvedores trabalham para adicionar novos recursos para o próximo lançamento. Os primeiros usuários podem usar as compilações noturnas que temos para todas as principais plataformas para ver o progresso do desenvolvimento, fazer testes preliminares e fornecer relatórios de bugs e suas opiniões para ajudar no desenvolvimento.
## Congelamento de atualizações
In the feature freeze phase, new features are not allowed in anymore and the focus of everyone moves from enhancing QGIS to stabilizing it. This also turns the nightly builds effectively into [prereleases](#qgis-prereleases).

**Users** should start extensive testing of these prereleases in their environment to verify that there are no issues, they wouldn’t want to see in the upcoming release. All such issues should be reported (see [Bugs, Features and Issues]({{< ref "resources/support/bug-reporting" >}})). Everything that goes unnoticed, will also end up in the next release. Only in case of serious problems backports to a latest release will occur. Therefore testing of the prereleases and reporting issues is very important.

In the feature freeze, **developers** monitor the bugtracker and start working on fixing the reported issues and update the **visual changelog** with the features they added.

With the start of the feature freeze, the translation files will be updated so that **translators** can start their work. Note that this might be an incremental process as although the features are frozen, bug fixes might still introduce translation string changes.

Two weeks before the release, a hard freeze is initiated after which only fixes to severe problems and regressions introduced after the feature freeze are allowed in.

O gerente de lançamento anuncia isso em paralisar feição.
## Lançamento
On major and minor release dates, the release branch is created and the release is tagged and tar balls are prepared. Point releases are just tagged and tar balls are created.

Os empacotadores são notificados de que a embalagem pode começar.

Uma vez que alguns pacotes estejam disponíveis, o lançamento pode ser anunciado e o site é atualizado de acordo.
## Calendário de lançamento
The schedule is aligned to produce roughly the same dates for each year given our four monthly releases with LTRs entering the LTR repo in late february.

Beginning after 2.12 the development phase is always 12 weeks and the freeze phase is at least 5 weeks. Remainders are used to extend the freeze phase of LTR releases.

Point releases will happen every month on the latest release branch, if there are backports. Beginning with the 3.28 release, point releases are only done with new latest releases.

In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn’t replace the previous LTR in the LTR repositories. This happens as soon as a new LR is released.

This schedule is also available as [“iCalendar”](https://qgis.org/schedule.ics).
### Agenda
{{<csv-table file="csv/schedule.csv" >}}
### Event legend
| Abbreviation | Descrição |
| --- | --- |
| LTR | Lançamento a longo prazo, começo da nova fase de desenvolvimento |
| LR | Lançamento regular, começar de novo fase de desenvolvimento |
| FF | Congelamento de recursos, o fim da fase de desenvolvimento |
| PR | Lançamento pontual da versão mais recente e ramo LTR |
| EPR | Lançamento de ponto extra |
| <span class="rm-current"> current </span> | <span class="rm-current"> currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} </span> |
| <span class="rm-next"> next </span> | <span class="rm-next"> next releases </span> |

## Localização de pré-lançamentos /nightly builds{#qgis-prereleases }
| Plataforma | Localização |
| --- | --- |
| Windows | [OSGeo4W]({{< ref "resources/installation-guide#online-osgeo4w-installer" >}}) |
| Linux | [Debian/Ubuntu]({{< ref "resources/installation-guide#repositories" >}}) |

{{<content-end >}}
