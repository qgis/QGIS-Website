---
type: "page"
title: "FAQ"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start  >}}

# FAQ

Here we collect answers to question that come up very often.



## User questions

### Downloading issues

If you are trying to download QGIS and nothing seems to happen, please consult the download manager of your browser.
It can usually be found as an icon (based on arrow, stop-watch or pie-chart) at the top-right corner of your browser window.
Click on the icon to see the download progress or cancel the download. The normal procedure with downloads in the
browser is such, that it first asks you where to save the file (with a file browser dialogue) and then you have to wait
until the download is finished. Because QGIS install packages can be rather large, depending on the operating system, you have to be patient.
The download size can be anywhere between several hundred megabytes to sometimes more than
one gigabyte (in case of MS Windows MSI packages). Depending on your download speed and the QGIS server load, downloads
can take from several minutes up to several hours.

### Do I have to donate in order to download QGIS?

This is a misconception that we hear from time to time, but it is not true. Donating to QGIS is optional.
After downloading QGIS, there is a message appearing, reminding that you can optionally donate to QGIS. However, you can press
"Close this message" and continue downloading without any problem. We want QGIS to be accessible to anyone, no matter
how your financial situation might be. If you are a first-time QGIS user, we recommend that you download, install and test
QGIS first and find out if the software is useful for the tasks you want to solve. Only if you like QGIS and it
substantially helps with your business, tasks or processes, you should think about donating towards QGIS or
supporting it as a sustaining member.

### How to ask a QGIS question?

If you are going to ask a QGIS related question via the [mailing lists]({{< ref "community/organisation/mailinglists" >}}),
please provide enough information to help others easily understand what your problem is.
Without a clear and precise question, it is very hard for anybody to answer, or it
just takes too much time because the answer will be a question to you etc etc.
You may provide information such as:

- preferably a descriptive title for your email
- which QGIS version you used at that moment (exact)
- what are you expecting to get
- if applicable, what have you tried and the result you got
- if your question is about something broken, you may also provide:

  - what exactly is the error (if possible: screendump, stacktrace, copy of error text)
  - which Operating System and version
  - how you installed it (osgeo4w? standalone-installer? own build?)
  - at what time did it break (reinstall, new install, system update, project changes)

Keep in mind that the more precise your question is, the quicker and more
accurate the answer can be.

{{< rich-box-start icon="💁" layoutClass="tips" mode="html">}}
{{< rich-content-start themeClass="coloring-1" >}}
##### Note
In case of a broken function, you may give a look at [QGIS issue tracker](https://github.com/qgis/QGIS/issues) before mailing to the list. More information at [bug-reporting]({{< ref "resources/support/bug-reporting" >}}).
{{< rich-content-end >}}
{{< rich-box-end >}}

### How are QGIS release names selected?

After a successful developer meeting in Zurich (Switzerland), we decided that
the next release should be related to it. Since then, all releases have been named
after locations of our developer meetings. 

### Can I open ECW files with QGIS?

Yes you can... BUT depending on your Operating System, it is more or less difficult.

**Windows**: If you are under Windows and are using the OSGeo4w installer, it is included.

**MacOs**: If you are using macOS, you can download the DMG file from [QGIS Downloads](https://qgis.org/download/). This file is built using the [QGIS-Mac-Packager](https://github.com/qgis/QGIS-Mac-Packager) repository, which includes the necessary ECW driver.

**Linux**: By default, most Linux distributions do not include ECW support for QGIS. However, you can find discussions and solutions for adding this support on various resources for guidance. 

For Ubuntu for example, you can check out the following thread:
- [Github - GDAL: How open ECW Maps in QGIS 3.22](https://github.com/OSGeo/gdal/issues/8239)
- [Reddit - QGIS: Problem loading ECW file in Ubuntu (Linux)](https://www.reddit.com/r/QGIS/comments/icw98f/problem_loading_ecw_file_in_ubuntu_linux/?rdt=54968)
- [GIS Stack Exchange: Installing QGIS with ECW support on ubuntu 20.04](https://gis.stackexchange.com/questions/429214/installing-qgis-with-ecw-support-on-ubuntu-20-04/434980#434980).

### How can I get a VPAT / HECVAT / other US compliance form or information? 

Please get in touch with the US User group. They are looking into these topics. 
More info and contact details: https://www.qgis-us.org



## Developer questions

### Can I compile QGIS myself?

Yes, compiling QGIS from source is possible whatever OS you use (Windows, macOS,
Linux). Please read [Building QGIS from source](https://github.com/qgis/QGIS/blob/master/INSTALL.md)



## Citation information

### How to cite QGIS?

If you need to cite QGIS in your work or for an assignment, please use the citation style that would be most helpful:


**Cite the QGIS project in general**


QGIS.org, {{< param "yeartag" >}}. QGIS Geographic Information System. QGIS Association. http://www.qgis.org


**Cite the QGIS Developers Manual**


QGIS.org, {{< param "yeartag" >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Developers Manual. QGIS Association. 
Electronic document: {{< param-link "devcite" >}}


**Cite the QGIS Installation Guide**


QGIS.org, {{< param "yeartag" >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System Installation Guide. QGIS Association. 
Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md


**Cite the QGIS User Guide**


QGIS.org, {{< param "yeartag" >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System User Guide. QGIS Association. 
Electronic document: {{< param-link "userguidecite" >}}

**Cite the QGIS Server Documentation**

QGIS.org, {{< param "yeartag" >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. 
Electronic document: {{< param-link "servercite" >}}


**Cite the QGIS API Documentation**

QGIS.org, {{< param "yeartag" >}}. QGIS {{< param "ltrversion" >}}. Geographic Information System API Documentation. QGIS Association. 
Electronic document: {{< param-link "apicite" >}}

**Preferred format:** [BibTeX](https://en.wikipedia.org/wiki/BibTeX)

Example BibTeX entry:

```
      @Manual{QGIS_software,
        title = {QGIS Geographic Information System},
        author = {{QGIS Development Team}},
        organization = {QGIS Association},
        year = {{{< param "yeartag" >}}},
        url = {https://www.qgis.org},
      }
```

### I created a map with QGIS, do I have to mention QGIS?

There is no requirement to mention QGIS for maps produced with it.
It is of course really welcome if you would like to add a note saying that the map was produced with QGIS.
"Made with QGIS" or "Map created using the Free and Open Source QGIS" are good examples of such a note.

{{< rich-box-start icon="✋" layoutClass="tips" >}}
{{< rich-content-start themeClass="coloring-1" >}}
##### Note

Do not say ©QGIS as QGIS does not hold copyrights on your work.
{{< rich-content-end >}}
{{< rich-box-end >}}



{{< content-end >}}
