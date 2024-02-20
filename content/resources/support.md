---
type: "page"
title: "Support"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start  >}}

# Support

## FAQ

Here we collect answers to question which come up very often.

We will start of with this one page, maybe restructure it into sections, or
even more pages if needed

### User

{{< spoiler title="Downloading issues" >}}

If you are trying to download QGIS and nothing seems to happen, please consult the download manager of your browser.
It can usually be found as an icon (based on arrow, stop-watch or pie-chart) at the top-right corner of your browser window.
Click on the icon to see the download progress or cancel the download. The normal procedure with downloads in the
browser is such, that it first asks you where to save the file (with a file browser dialogue) and then you have to wait
until the download is finished. Because QGIS install packages, depending on the operating system, can be rather large
you have to be patient. The download size can be anywhere between several hundred megabytes to sometimes more than
one gigabyte (in case of MS Windows MSI packages). Depending on your download speed and the QGIS server load, downloads
can take from several minutes up to several hours.
{{< /spoiler >}}

{{< spoiler title="I have to donate in order to download QGIS" >}}
This is a misconception that we hear from time to time, but it is not true. Donating to QGIS is optional.
After downloading QGIS, there is a message appearing, reminding that you can optionally donate to QGIS. However, you can press
"Close this message" and continue downloading without any problem. We want QGIS to be accessible to anyone, no matter
how your financial situation might be. If you are a first-time QGIS user, we recommend that you download, install and test
QGIS first and find out if the software is useful for the tasks you want to solve. Only if you like QGIS and it
substantially helps with your business, tasks or processes, you should think about donating towards QGIS or
supporting it as a sustaining member.
{{< /spoiler >}}

{{< spoiler title="How to ask a QGIS question?" mode="html" >}}
If you are going to ask QGIS related question via the [mailing lists]({{< ref "community/organisation/mailinglists" >}}),
please provide enough information to help others easily understand what your problem is.
Without a clear and precise question, it is very hard to answer for anybody or
takes just too much time because the answer will be a question to you etc etc.
You may provide information such as:

* preferably a descriptive title for your email
* which QGIS version you used at that moment (exact)
* what are you expecting to get
* if applicable, what have you tried and the result you got
* if your question is about something broken, you may also provide:

  * what exactly is the error (if possible: screendump, stacktrace, copy of error text)
  * which Operating System and version
  * how you installed it (osgeo4w? standalone-installer? own build?)
  * at what time did it break (reinstall, new install, system update, project changes)

Keep in mind that the more precise is your question, the quicker and more
accurate can be the answer.

{{< rich-box icon="💁" layoutClass="tips" >}}
{{< rich-content themeClass="coloring-1" >}}
##### Note
In case of a broken function, you may give a look at [QGIS issue tracker](https://github.com/qgis/QGIS/issues) before mailing to the list. More information at [bug-reporting](../../resources/support/bug-reporting).
{{< /rich-content >}}
{{< /rich-box >}}
{{< /spoiler >}}

{{< spoiler title="How are QGIS release names selected?" >}}
After a successful developer meeting in Zurich (Switzerland), we decided that
the next release should be related to it. Since then, all releases have been named
after locations of our developer meetings. 
{{< /spoiler >}}

{{< spoiler title="How to cite QGIS?" >}}

To cite QGIS in your piece of work, or for an assignment, please use citation type that can be more helpful:


**Cite the QGIS project in general**


QGIS.org, |yeartag|. QGIS Geographic Information System. QGIS Association. http://www.qgis.org


**Cite the QGIS Developers Manual**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System Developers Manual. QGIS Association. 
Electronic document: |devcite|


**Cite the QGIS Installation Guide**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System Installation Guide. QGIS Association. 
Electronic document: https://github.com/qgis/QGIS/blob/master/INSTALL.md


**Cite the QGIS User Guide**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System User Guide. QGIS Association. 
Electronic document: |userguidecite|

**Cite the QGIS Server Documentation**

QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System API Documentation. QGIS Association. 
Electronic document: |servercite|


**Cite the QGIS API Documentation**


QGIS.org, |yeartag|. QGIS |ltrversion|. Geographic Information System API Documentation. QGIS Association. 
Electronic document: |apicite|





**Preferred format:** [BibTeX](https://en.wikipedia.org/wiki/BibTeX)


Example BibTeX entry:

```
      @Manual{QGIS_software,
        title = {QGIS Geographic Information System},
        author = {{QGIS Development Team}},
        organization = {QGIS Association},
        year = {|yeartag|},
        url = {https://www.qgis.org},
      }
```
{{< /spoiler >}}

{{< spoiler title="I created a map with QGIS, do I have to mention QGIS?" mode="html" >}}
There is no requirement to mention QGIS for maps produced with it.
It is of course really welcome if would like to add a note saying that the map was produced with QGIS.
"Made with QGIS" or "Map created using the Free and Open Source QGIS" are good examples of such a note.

{{< rich-box icon="💁" layoutClass="tips" >}}
{{< rich-content themeClass="coloring-1" >}}
##### Note

Do not say ©QGIS as QGIS does not hold copyrights on your work.
{{< /rich-content >}}
{{< /rich-box >}}
{{< /spoiler >}}

{{< spoiler title="Can I open ECW files with QGIS?" >}}
Yes you can... BUT depending on your Operating System, it is more or less difficult.

If you are under Windows and are using the OSGeo4w installer, it is included.

If you are using macOS, you can find the ECW plugin and install instructions at
https://www.kyngchaos.com/software/frameworks

For other instructions, eg look here: https://www.faunalia.eu/en/blog/2019-05-21_ecw_support

{{< /spoiler >}}

### Development

{{< spoiler title="Can I compile QGIS myself?" >}}

Yes, compiling QGIS from source is possible whatever OS you use (Windows, OS X,
Linux). Please read [Building QGIS from source](https://github.com/qgis/QGIS/blob/master/INSTALL.md)


{{< /spoiler >}}

## Mailing Lists

QGIS has a bunch of mailing lists. See [Mailing lists]({{< ref "community/organisation/mailinglists" >}}) for the different available lists.

If you are going to ask questions please read this: [How to ask a QGIS question?](https://qgis.org/en/site/getinvolved/faq/index.html#how-to-ask-a-qgis-question).

## StackExchange

On [http://gis.stackexchange.com](http://gis.stackexchange.com) you can ask QGIS questions also. If you use the tag `qgis` you’ll see all QGIS related questions and answers: [http://gis.stackexchange.com/?tags=qgis](http://gis.stackexchange.com/?tags=qgis)

## Communication channels

### Telegram

There is a lot of user and community related chat (english spoken) on the Telegram channel you can join here: [https://t.me/joinchat/Aq2V5RPoxYYhXqUPoxRWPQ](https://t.me/joinchat/Aq2V5RPoxYYhXqUPoxRWPQ)

To join: install Telegram on your phone, register and join via link above.

There is also a web version (https://web.telegram.org) which you can join in the browser (after you joined telegram via your phone(number)).

### Matrix / IRC

Matrix (https://matrix.org) is a project for decentralised chat. QGIS has a room accessible by the **#qgis:osgeo.org** alias (among others) which bridges to the libera.chat **#qgis** IRC channel.

To use Matrix: create an account (at matrix.org is easiest, but if you have an OSGeo account you can also [use your OSGeo id as matrix id](https://wiki.osgeo.org/wiki/Matrix#Connecting_to_the_OSGeo_Matrix_Homeserver)), install a client (Elements is easiest, but see [https://matrix.org/docs/projects/try-matrix-now/#clients](https://matrix.org/docs/projects/try-matrix-now/#clients) for more), OR point your browser to [https://matrix.to/#/#qgis:osgeo.org](https://matrix.to/#/#qgis:osgeo.org)

To use IRC: install an IRC client and connect to [irc://irc.libera.chat/#qgis](irc://irc.libera.chat/#qgis) or point your browser to [https://web.libera.chat/?channels=#qgis](https://web.libera.chat/?channels=#qgis)

### Facebook

For Facebook users, an english-speaking global community group for QGIS users can be found at [https://www.facebook.com/groups/qgiscommunityofficialvirtualgroup](https://www.facebook.com/groups/qgiscommunityofficialvirtualgroup)

## User Groups

Local QGIS user groups are a great place to meet other users.

See [User Groups](../../community/organisation/groups/) to read about it.

## Website

The website should be used to publish any material in relation to the information and management of the user group. Examples include the user meetings, case study, shared material, discussion boards, etc. Public material should be available without login requirements (e.g. do not require interested people to be a member of a social media network like Facebook or Google+). Usage of social media is recommended but should not be the only channel of information. RSS feeds should be made available at the Website of the QGIS user group.

Good luck with the organization of your local user group. Please inform the international QGIS team by registering at the QGIS community list and reporting about your progress. Please do not hesitate to ask questions regarding the establishment and maintenance of your local user group.

{{< script src="js/spoiler.js" >}}

{{< content-end >}}
