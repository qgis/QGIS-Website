---
draft: false
sidebar: true
subtitle: ''
title: Segnalazione dei bug
type: page

---
{{<content-start >}}
# Bug, Richieste e Segnalazioni
QGIS è un progetto largamente mantenuto da volontari, ed è il lavoro di un team di sviluppatori, documentatori, traduttori e sostenitori dediti. Nonostante gli sforzi del team di rilasciare QGIS senza bug, ne può rimanere qualcuno. Se scopri un bug o vuoi nuove funzionalità, segnalalo!
## Dove segnalare?
Ogni parte del progetto QGIS ha un luogo dedicato dove i problemi (richieste di funzionalità o bug) possono essere segnalati, gestiti e discussi. A seconda dell'area in cui hai riscontrato il problema, la tabella seguente indica il repository corretto per segnalarlo:
| Posto in cui hai trovato il bug o richiedi una funzionalità per | Posto per segnalare il problema |
| --- | --- |
| Applicazioni (QGIS Desktop, QGIS Server) | https://github.com/qgis/QGIS/issues |
| QGIS Sito web (https://qgis.org) | https://github.com/qgis/QGIS-Website/issues |
| QGIS Documentazione (https://docs.qgis.org) | https://github.com/qgis/QGIS-Documentation/issues |
| C++ API (https://qgis.org/api) | https://github.com/qgis/QGIS/issues |
| PyQGIS API (https://qgis.org/pyqgis) | https://github.com/qgis/QGIS/issues (per i contenuti) e https://github.com/qgis/pyqgis/issues (per la formattazione) |
| QGIS Plugins Website (https://plugins.qgis.org) | https://github.com/qgis/QGIS-Plugins-Website/issues |
| QGIS Hub Website (https://hub.qgis.org) | https://github.com/qgis/QGIS-Hub-Website/issues |
| QGIS Planet Website (https://planet.qgis.org) | https://github.com/qgis/QGIS-Planet-Website/issues |
| QGIS Changelog Website (https://changelog.qgis.org) | https://github.com/kartoza/prj.app/issues |
| QGIS Feed Website (https://feed.qgis.org) | https://github.com/qgis/qgis-feed/issues |
| Plugin esterni | Il repository dell'autore impostato nella descrizione del plugin |

For help and questions, please contact the [Mailing lists]({{< ref "community/organisation/mailinglists" >}}).
## Segnalare problemi su applicazioni QGIS
QGIS applications (QGIS Desktop and QGIS Server) issues are available in [Github](https://github.com/qgis/QGIS/issues). In order to submit or comment a report, you need to register and login.
### Prima di riportare un problema
Before filing an issue, verify that you are running the currently supported versions {{< param "ltrrelease" >}} or {{< param "release" >}} or the development version {{< param "devversion" >}} (see also [Release schedule]({{< ref "resources/roadmap#release-schedule" >}})) and review the currently open issues to make sure that you aren’t creating a duplicate. If you have additional information on an issue, you can add it to the existing ticket. Third party plugins might also cause problems. If you have installed any, you should also verify that the problem is still reproducible without them. Please don’t report multiple unrelated bugs in a single bug report.

When you’re logged in, a `New Issue` button is available. Select it and follow the instructions there.

Before sending the report, please check the formatting of your report by clicking on “Preview”. Please avoid editing existing reports, if not for typos. Better add further comments in any other case.
#### Creazione di una backtrace
Se hai un crash potrebbe essere utile includere una backtrace poiché il bug potrebbe non essere riproducibile su un'altra macchina.

On Linux QGIS automatically tries to use `gdb` to connect to the crashing process to produce a backtrace. But some distributions disable the possiblity to connect debuggers to a running processes. In that case `gdb` only produces a rather useless message like:

QGIS died on signal 11Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf ptrace: Operation not permitted. No thread selected No stack. gdb returned 0 Aborted (core dumped)

In that case you should reenable that option by setting `kernel.yama.ptrace_scope` to 0 in `/etc/sysctl.d/10-ptrace.conf` (or `/etc/sysctl.conf` or some other file in `/etc/sysctl.d/`) and run `sysctl -p` as root. When you reproduce the crash after that, a backtrace will be printed instead.

If you cannot reproduce the crash, there should still be a core dump in the current directory, that can be analysed after the process has already terminated. It’s called `core`, though the filename may include a dot followed by the process id on some systems.

On some distributions the creation of core dumps is also disabled. In the event that you just get `Aborted` instead of `Aborted (core dumped)` when the crash occurs. Then you need to run `ulimit -c unlimited` before starting QGIS. You can also include that in your `.profile`, so that it’s always enabled when you login.

To produce a backtrace from the core file, start `gdb /path/to/the/qgis/binary core`. The binary is usually `/usr/bin/qgis` or `/usr/bin/qgis.bin` on Debian with the GRASS plugin installed. In `gdb` you run `bt` which will produce the backtrace.
#### Log output in Windows
The nightly build in [OSGeo4W](https://trac.osgeo.org/osgeo4w) (package qgis-dev) is built with debugging output, that you can view with [DebugView](https://docs.microsoft.com/en-us/sysinternals/downloads/debugview). If the problem is not easy to reproduce, the output might shed some light about where QGIS crashes.
## Segnalare problemi sul sito web QGIS o sulla documentazione
QGIS project provides an active [web site](https://qgis.org) and a rich [documentation](https://qgis.org/en/docs/index.html). Despite our efforts, if you find an out of date information, a wrong or unclear statement or miss valuable information, please feel free to report it.

Le sorgenti principali di questi documenti sono ospitate e gestite su repository GitHub per cui, per riportare bug o inviare patch, hai bisogno di un account GitHub e di eseguire l'accesso.

To get started, first [Create a GitHub account](https://github.com/join).

In seguito, scegli il repository appropriato:
- https://github.com/qgis/QGIS-Documentation/issues per la documentazione QGIS
- https://github.com/qgis/QGIS-Website/issues per il sito web

Check if the issue you’d like to report is not already entered.

Clicca su **Nuova Segnalazione**, digita un titolo e una descrizione chiara per il tuo problema.

When you’re finished, click **Submit new issue**.

Note

A `Fix me` link is provided at the bottom of any page of the web site to help you directly improve this page and submit pull request.

Questa opzione è anche disponibile nel piè di pagina della documentazione.
## Segnalazione di problemi con i plugin
Most of the plugins in QGIS are published in the official [QGIS Plugins repository](https://plugins.qgis.org/plugins/). Bugs or feature requests relative to them **must** be opened in their respective bug tracking system:
- For any plugin available in QGIS repository, you’ll find in its metadata a link to its bug tracker. Otherwise, consult the plugin documentation to find the address of the relevant bug tracking system or a developer to contact.
  
  If no information is available, please report it to the [Developer mailing-list](https://lists.osgeo.org/mailman/listinfo/qgis-developer).
- For other plugins, we have no means to ensure such information is provided.

## Invio di una Patch ai progetti QGIS
In addition to issue report, you can help to fix issues. Fixing issues is done in GitHub through pull requests. You need to [fork the repository](https://help.github.com/articles/working-with-forks/) you want to contribute to and submit pull requests at:
- https://github.com/qgis/QGIS per applicazioni QGIS Desktop o QGIS Server
- https://github.com/qgis/QGIS-Website per il sito web su https://qgis.org
- https://github.com/qgis/QGIS-Documentation per la documentazione disponibile su https://docs.qgis.org

You can find a few guidelines that will help you to easily get your patches and pull requests into QGIS projects at [Submitting Pull Requests](https://docs.qgis.org/testing/en/docs/developers_guide/git.html#submitting-pull-requests). And more widely, you may need to read the [Development Process](https://docs.qgis.org/testing/en/docs/developers_guide/git.html) chapter.

{{<content-end >}}
