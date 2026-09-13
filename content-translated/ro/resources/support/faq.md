---
draft: false
sidebar: true
subtitle: ''
title: Întrebări frecvente
type: page

---
{{<content-start >}}
# Întrebări frecvente
Here we collect answers to question that come up very often.
## User questions
### Probleme de descărcare
If you are trying to download QGIS and nothing seems to happen, please consult the download manager of your browser. It can usually be found as an icon (based on arrow, stop-watch or pie-chart) at the top-right corner of your browser window. Click on the icon to see the download progress or cancel the download. The normal procedure with downloads in the browser is such, that it first asks you where to save the file (with a file browser dialogue) and then you have to wait until the download is finished. Because QGIS install packages can be rather large, depending on the operating system, you have to be patient. The download size can be anywhere between several hundred megabytes to sometimes more than one gigabyte (in case of MS Windows MSI packages). Depending on your download speed and the QGIS server load, downloads can take from several minutes up to several hours.
### Do I have to donate in order to download QGIS?
Aceasta este o concepție greșită, pe care o auzim din când în când, și care nu este adevărată. Donarea către QGIS este opțională. După descărcarea QGIS, apare un mesaj care vă reamintește că, opțional, puteți dona către QGIS. Cu toate acestea, puteți apășa pe „Închide acest mesaj”, descărcarea continuând fără nicio problemă. Ne dorim ca oricine să aibă acces la QGIS, indiferent de situația sa financiară. Dacă utilizați QGIS pentru prima dată, vă recomandăm să descărcați, să instalați și să testați mai întâi QGIS, aflând astfel dacă softul este util pentru sarcinile pe care le aveți de rezolvat. Numai dacă vă place QGIS și vă ajută substanțial la afacerea, sarcinile sau procesele dvs., ar trebui să luați în considerare o donație către QGIS sau să deveniți membru susținător.
### Cum se pune o întrebare despre QGIS?
If you are going to ask a QGIS related question via the [mailing lists]({{< ref "community/organisation/mailinglists" >}}), please provide enough information to help others easily understand what your problem is. Without a clear and precise question, it is very hard for anybody to answer, or it just takes too much time because the answer will be a question to you etc etc. You may provide information such as:
- preferabil, un titlu descriptiv pentru mesaj
- versiunea (exactă) de QGIS, care a fost folosită la acel moment
- ce vă așteptați să obțineți
- dacă este cazul, ce ați încercat și ce rezultat ați obținut
- dacă întrebarea dumneavoastră se referă la o defecțiune, puteți transmite, de asemenea:
  - care este eroarea exactă (dacă este posibil: o captură de ecran, jurnalul stivei, mesajul de eroare)
  - which Operating System and version
  - modalitatea instalării (osgeo4w? instalare offline? compilație proprie?)
  - în ce moment a apărut eroarea (reinstalare, instalare nouă, actualizare de sistem, la modificarea proiectului)

Keep in mind that the more precise your question is, the quicker and more accurate the answer can be.

{{<rich-box-start icon="💁" layoutClass="tips" mode="html" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
In case of a broken function, you may give a look at [QGIS issue tracker](https://github.com/qgis/QGIS/issues) before mailing to the list. More information at [bug-reporting]({{< ref "resources/support/bug-reporting" >}}).

{{<rich-content-end >}}

{{<rich-box-end >}}
### Criteriile de selectare a numelor pentru versiunile de QGIS?
În urma unei reuniuni a dezvoltatorilor din Zurich (Elveția), s-a decis ca versiunea lansată la acel moment să facă referire la respectivul eveniment. De atunci, toate versiunile poartă numele localităților în care s-au desfășurat întâlnirile dezvoltatorilor.
### QGIS poate deschide fișiere ECW?
ECW is a proprietary file format - please consult their [Licensing Page](https://supportsi.hexagon.com/s/article/License-for-reading-or-writing-ECW-in-third-party-software) to understand how you may use it. Also, please consult the [GDAL documentation](https://gdal.org/en/stable/drivers/raster/ecw.html#creation-options-1) for notes on how to enable licensed features if you have a paid version of ECW. ECW support is not included in all QGIS binary versions and for all platforms by default.

**Platform specific notes:**

***Windows***: If you are using Windows and have downloaded the **offline installers** (provided by the download buttons labelled **Long Term Version for Windows ({{< param "ltrversion" >}} {{< param "ltrnote" >}})** and **Latest Version for Windows ({{< param "version" >}})**), ECW read support is included by default.

If you are using the **OSGeo4W Network Installer**, ECW support is installed by default if you use the express install workflow. If manually selecting components, you need to explicitly enable the `gdal-ecw` package in order to ensure that ECW support is included in your installation.

***macOS***: If you are using macOS, you can download the DMG file from [QGIS Downloads](https://qgis.org/download/). This includes ECW support by default.

***Linux***: By default, the QGIS binaries for most Linux distributions *do not* include default ECW support. However, you can find discussions and solutions for adding this support in various resources for guidance.

For Ubuntu, for example, you can check out the following resources:
- [Github - GDAL: How to open ECW Maps in QGIS 3.22](https://github.com/OSGeo/gdal/issues/8239)
- [Reddit - QGIS: Problem loading ECW file in Ubuntu (Linux)](https://www.reddit.com/r/QGIS/comments/icw98f/problem_loading_ecw_file_in_ubuntu_linux/?rdt=54968)
- [GIS Stack Exchange: Installing QGIS with ECW support on ubuntu 20.04](https://gis.stackexchange.com/questions/429214/installing-qgis-with-ecw-support-on-ubuntu-20-04/434980#434980).

### How can I get a VPAT / HECVAT / other US compliance form or information?
Please get in touch with the US User group. They are looking into these topics. More info and contact details: https://www.qgis-us.org
## Developer questions
### Aș putea compila QGIS?
Yes, compiling QGIS from source is possible whatever OS you use (Windows, macOS, Linux). Please read [Building QGIS from source](https://github.com/qgis/QGIS/blob/master/INSTALL.md)
## Citation information
### Cum se face o referire la QGIS?
If you need to cite QGIS in your work or for an assignment, please use the citation style that would be most helpful:

Here are some choices to cite the overall QGIS software project, a specific QGIS version being used used, or QGIS documentation to allow reproducibility:

**The QGIS project as an evolving software project, independent of a specific software release, by Digital Object Identifier (concept DOI)**

Folosește conceptul [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6139224.svg)](https://doi.org/10.5281/zenodo.6139224) atunci când
- referring to the QGIS software in general (e.g., in introductions or background sections)
- describing workflows where the exact version is not critical
- citing QGIS as a long-term research tool or infrastructure

The concept DOI will always resolve to the latest version of QGIS and provide a stable reference to the software project over time.

**Specific QGIS software releases by Digital Object Identifier (version DOI)**

Each QGIS release since release 3.22.4 (2022) has its own version DOI identifying a precise, archived snapshot of the software (e.g., a specific software release). All version DOI are linked to the concept DOI of the QGIS project.

Please refer to the QGIS Zenodo Landing Page ([QGIS Zenodo Landing Page](https://zenodo.org/search?q=parent.id%3A6139224&f=allversions%3Atrue&l=list&p=1&s=10&sort=version)) for all specific version DOI.
- QGIS 4.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18889261.svg)](https://doi.org/10.5281/zenodo.18889261)
- QGIS 3.44 LTR [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15705458.svg)](https://doi.org/10.5281/zenodo.15705458)

**Citarea, în general, a proiectului QGIS**

QGIS.org, {{< yeartag >}}. QGIS Geographic Information System. QGIS Association. http://www.qgis.org

**Citarea din Manualul Dezvoltatorului QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Developers Manual. QGIS Association. Electronic document: {{< param-link "devcite" >}}

**Citarea din Ghidul de Instalare a QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Installation Guide. QGIS Association. Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md

**Citarea din Manualul Utilizatorului QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System User Guide. QGIS Association. Electronic document: {{< param-link "userguidecite" >}}

**Citarea din Documentația Serverului QGIS**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "servercite" >}}

**Citarea din Documentația QGIS API**

QGIS.org, {{< yeartag >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. Electronic document: {{< param-link "apicite" >}}

**Preferred format:** [BibTeX](https://en.wikipedia.org/wiki/BibTeX)

Exemplu de intrare BibTeX:
```
@Manual{QGIS_software,
  title = {QGIS Geographic Information System},
  author = {{QGIS Development Team}},
  organization = {QGIS Association},
  year = {{{< yeartag >}}},
  url = {https://www.qgis.org},
}
```
**Cite the QGIS paper in Patterns**
```
@article{graser2025,
  title = {The QGIS project: Spatial without compromise},
  journal = {Patterns},
  volume = {6},
  number = {7},
  pages = {101265},
  year = {2025},
  issn = {2666-3899},
  doi = {https://doi.org/10.1016/j.patter.2025.101265},
  url = {https://www.sciencedirect.com/science/article/pii/S2666389925001138},
  author = {Anita Graser and Tim Sutton and Marco Bernasocchi}
}
```
### Am creat o hartă cu QGIS, trebuie să menționez QGIS?
There is no requirement to mention QGIS for maps produced with it. It is of course really welcome if you would like to add a note saying that the map was produced with QGIS. "Made with QGIS" or "Map created using the Free and Open Source QGIS" are good examples of such a note.

{{<rich-box-start icon="✋" layoutClass="tips" >}}

{{<rich-content-start themeClass="coloring-1" >}}
##### Note
Nu folosiți ©QGIS întrucât QGIS nu deține drepturi de autor asupra muncii dvs.

{{<rich-content-end >}}

{{<rich-box-end >}}

{{<content-end >}}
