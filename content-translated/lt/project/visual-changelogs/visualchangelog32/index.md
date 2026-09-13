---
HasBanner: false
draft: false
releaseDate: '2018-06-22'
section: projektą
sidebar: true
title: QGIS 3.2 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 3.2 pakeitimai{#changelog32 }
![image1](images/projects/8f04d904f903b8bff930e6c968fe46928e6cc012.png)

Laidos data: 2018-06-22

The greatest QGIS release ever! QGIS 3.2 brings a massive list of new changes - the highlights of which we will try to cover here. As always can we remind you that QGIS is an open source project and if you are able to, consider supporting our work through [donations]({{< ref "/funding/donate.md" >}}), [sustaining memberships]({{< ref "/funding/membership.md" >}}) or contributions to the code documentation, web site and so on.

**Ačiū**

We would like to thank the developers, documenters, testers and all the many folks out there who volunteer their time and effort (or fund people to do so). From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

QGIS is supported by donors and sustaining members. A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list]({{< ref "/funding/donate.md" >}}). If you would like to become an official sustaining member, please visit [our sustaining members page]({{< ref "/funding/membership.md" >}}) for details. Supporting QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts. A complete list of current sustaining members is provided below - our very great thank you to all of our supporters!

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## QGIS 3.2 versijos rėmėjai
A special thanks to all our [sustaining members, sponsors and donors]({{< ref "/funding/membership.md" >}}) for helping us to make this release possible!
## Bendra
### Savybė: naujas suspaustas projekto failo formatas .qgz dabar yra numatytasis formatas
3.0 versijoje QGZ buvo pridėtas kaip pasirinktinis formatas. Šį formatą padarius numatytuoju palengvės kelias pereinant prie talpos, galinčios įtraukti resursus, tokius kaip SVG, vietinę duomenų kopiją GPKG, spalvų rampas, priedus ir scenarijus.

![image29](images/entries/15e0d291ccc9722a61ed5d2611d3ac4c0eef3685.png.400x300_q85_crop.webp)

This feature was developed by [OSLANDIA - Paul Blottiere](https://github.com/pblottiere)
### Savybė: lauko reikšmių filtravimas Užklausų kūrime
Kuriant naują išraiškų filtrą užklausų kūrime, dabar galite filtruoti laiko reikšmes peržiūrėjimo skydelyje

![image30](images/entries/731d930d07ca6d35f6bff727ef94a6322fcf21d0.gif.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Savybė: PILNO ekrano žemėlapis spaudžiant Ctrl+Shift+Tab
Greta Ctrl+Tab dabar galite spausti Ctrl+Shift+Tab, kuris jums parodys žemėlapį ir TIK žemėlapį, jokių įrankinių ar mygtukų (net be lango pavadinimo, kartu su F11). Puikiai tinka Pilno ekrano žemėlapio projektavimui per projektorių dideliuose ekranuose. Galite keisti mastelį ir stumdyti! (Paremta Mathieu Pellerin darbu)

![image31](images/entries/e05bfa8d423465a0ec6697fac1d21dfeee177aea.png.400x300_q85_crop.webp)

Šią savybę sukūrė Richard Duivenvoorde
## Žemėlapio įrankiai
### Savybė: žemėlapio paprastinimo įrankis dabar taip pat gali ir glotninti geoobjektus
The Simplify Features map tool has been renamed to \"Simplify/Smooth Features\", and now supports interactive smoothing of features.

![image2](images/entries/eca7851f8710661b929a99722afd28707f5926b3.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: identifikavimo įrankis su papildomomis parinktimis
Nauji patobulinimai dabar leidžia naudoti panašius įrankius į pažymėjimo, norint identifikuoti kelis geoobjektus.

Šią savybę finansavo Leicestershire County Council and East Hampshire District Council

This feature was developed by [Martin Dobias and Viktor Sklencar](https://www.lutraconsulting.co.uk)
### Savybė: taipogi įrašyti ir išplėstų/suskleistų narių būseną žemėlapio temose
Kiekviena žemėlapio tema taip pat įrašo kurie sluoksniai, grupės ir legendos elementai yra išplėsti, kad parinkus žemėlapio temą būtų atstatytos išplėstos/suskleistos būsenos.

![image3](images/entries/0cfc7d80448436d67a4b1e92773e66eda5900a57.PNG.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Feature: Auto \"Zoom to Selection\" mode for new map views
Naujo žemėlapio peržiūra gali būti sukonfigūruota taip, kad automatiškai priartintų dabartinį pažymėjimą. Gali būti kombinuojama su skirtingomis žemėlapio temomis kaip šiame pavyzdyje.

![image4](images/entries/17848d809ce5a999115619ace229b6f07dba272a.PNG.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Savybė: paprastinimo metodo pasirinkimas žemėlapio paprastinimo įrankyje
This allows different techniques to be used for simplification in the interactive simplify map tool, including the more cartographically pleasing \"Visvalingam\" simplification algorithm.

![image5](images/entries/085ad891fdc2b416a89603a6962544d165f2cef1.PNG.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: pridėti priartinimą į susijusių geoobjektų formas
Pažymėjus vieną ar daugiau įrašų susijusioje lentelėje, geoobjekto atributų subformoje atsiranda naujas mygtukas. Mygtukas priartina žemėlapyje geoobjektus, jei jie turi geometrijas.

![image6](images/entries/697d671bf6227445e10f9c899c0740b4225c1e7f.PNG.400x300_q85_crop.webp)

Šią savybę sukūrė Jürgen Fischer
### Savybė: kerteziniai plotai/ilgiai/perimetrai identifikavimo rezultatuose
QGIS 3.2 identifikavimo rezultatų skydelyje dabar rodome ir elipsoidinius, ir kartezinius plotus, ilgius ir perimetrus atskirai. Matant du skirtingus matavimus leidžia naudotojams geriau suprasti galimas problemas ploto ir atstumo skaičiavimuose, kylančias dėl neteisingo projekcijos ar elipsoido pasirinkimo.

![image7](images/entries/28e185f928be7d08fd2971828a1daed53c224394.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Išraiškos
### Savybė: naujos išraiškų funkcijos
- color_grayscale_average()
- color_mix_rgb()
- flip_coordinates()
- wedge_buffer()
- tapered_buffer()
- buffer_by_m()

Nauji kintamieji:
- \@project_home
- \@project_author
- \@project_abstract
- \@project_creation_date
- \@project_identifier
- \@project_keywords

Šią savybę sukūrė Mathieu Pellerin, Nyall Dawson
### Savybė: labiau padedantis išraiškų kūrėjas
Išraiškų kūrėjas dabar leidžia lengviau kurti išraiškas su QGIS!
- Kūrėjas dabar rodo nuo duomenų priklausančių reikšmių aprašymą, įskaitant ir reikšmių galimą intervalą iš išraiškos
- Ctrl+paspaudus funkcijos pavadinimą bus automatiškai atidaryta dabartinės išraiškos pagalba
- Dabar rodo išraiškų dalių indikatorių su klaidomis
- Rodo pilną klaidų pranešimų sąrašą, gautą nagrinėjant išraišką

![image8](images/entries/a296b411a0950f6bbd9af3c3cffec90b509b6e78.png.400x300_q85_crop.webp)

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
## Naudotojo sąsaja
### Savybė: sluoksnių skydelis: filtruotų žemėlapių sluoksnių indikatoriai
The main window\'s layer tree view (ToC) gets support for indicators that are shown when a vector layer has a filter applied. This makes it easier for users to understand that they are looking at a subset of all data. Clicking the indicator\'s icon brings up query builder.

Pridėtas mini-karkasas papildomų piktogramų rodymui sluoksnių medyje, greta sluoksnių ir grupių pavadinimų. Pelės užvedimo tekstas gali būti susietas su indikatoriais, kad suteiktų papildomą indikatorių kontekstą. Papildomai, signalas siunčiamas naudotojui paspaudus indikatorius ir gali būti nustatomi savo veiksmai. Mintis yra ateityje naudoti indikatorius subtiliam pranešimui apie skirtingą informaciją, pavyzdžiui:
- žemėlapio sluoksnis su netinkamomis geometrijomis
- žemėlapio sluoksnis su su momentinio perprojektavimo klaidomis
- žemėlapio sluoksnis turi trūkstamą duomenų šaltinį
- žemėlapio sluoksnis su netinkama CRS

![image9](images/entries/ff2206aa7147ca68357ea4e3a1354bc231fb49cc.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Savybė: galimybė keisti atradėjo filtrų priešdėlius
Prefixes of locator filters can now be customized under the application settings in the \"Locator\" tab

![image10](images/entries/d45b0ff62c8013eed8171c3bc42c9cdacc7dac10.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Savybė: atvėrimas vektoriaus ir rastro, saugomo HTTP(S), FTP ar debesų paslaugose
In 3.2, the data source manager\'s vector and raster panels have been updated to simplify opening of vector and raster datasets stored on HTTP(S), FTP, or cloud services. Basic HTTP(S) authentication support included.

![image11](images/entries/06e06201fb4db385ae14d6932353ce0b0b035e83.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: greitas skaičiuotuvas paieškos juostoje
QGIS 3.2 allows evaluation of simple expressions (well, actually ANY QGIS expression\... so you could use aggregates and the like if you really wanted!) by entering \"= \" followed by an expression into the locator bar. If a valid expression is entered, users are given an option to copy the result to the clipboard.

E.g. entering \"= 10/3\" shows a locator entry \"Copy \'3.3333333\' to clipboard\".

![image12](images/entries/873ea8846c5f2f2cea56e8d4602bb41ac0567d7d.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: klavišų kombinacijos skydelių perjungimui
Ctrl+{nr} klavišų kombinacija

This feature was funded by [Technology One](https://www.technologyonecorp.com/)

This feature was developed by [Nathan Woodrow](https://nathanw.net/)
### Savybė: žymelių paieška
Leidžia ieškoti erdvinių žymelių. Du kartus paspaudus ant paieškos rezultatų, žymelės vieta bus priartinta.

Short video: <https://www.youtube.com/watch?v=ymW4TU8QWy4>

The new filter presents itself with a prefix of \"b\" and with tr( \"Spatial bookmarks\" ) as displayname.

Šią savybę sukūrė Klavs Pihlkjær
### Savybė: projekto uždarymo ir atšaukimo veiksmai
Two new actions have been added to the \"Project\" menu
- \"Close\": Closes the active project, returning the QGIS window to the \"Recent Projects\" list
- \"Revert\": Restores the active project to the last saved state, discarding all unsaved changes

![image13](images/entries/3801ee06f51aa6517fd1c4a5de5eafffd4114f71.png.400x300_q85_crop.webp)

Šią savybę sukūrė Nathan Woodrow, Nyall Dawson
### Savybė: neįrašytų pakeitimų indikatorius pavadinimo juostoje
QGIS 3.2 now follows the standard UI approach of indicating that the current project has unsaved changes by adding a \"\*\" prefix to the project name in the application title bar. This makes it easy to see if you have unsaved changes at a single glance!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: konfigūruojamas žemėlapių patarimų rodymo uždelsimas
Šią savybę sukūrė jdugge
### Savybė: perkelti sluoksnį ar grupę į sluoksnių skydelio viršų
Perkelia pažymėtą sluoksnį(-ius) ar grupę(-es) į sluoksnių skydelio viršų.

Šią savybę sukūrė Mie Winstrup
### Savybė: mygtukas kopijuoti statistikos skydelio turinį į iškarpinę
It is now possible to copy the statistics panel\'s output table into the clipboard.

![image14](images/entries/0d1f4be90052251c05a1fc351dd099aaa92c65f7.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: paieškos nustatymų, parinkčių ir projekto savybių puslapiai iš atradėjo lauko
Short video: <https://www.youtube.com/watch?v=duB2YekUmV0>

The new filter presents itself with a prefix of \"s\" and with tr( \"Settings\" ) as displayname.

Šią savybę sukūrė Klavs Pihlkjær
### Savybė: įlietų sluoksnių ir grupių indikatoriai
Embedded project layers and groups are now flagged by a handy \"embedded\" indicator, making it immediately clear to users which layers and groups have been embedded inside a project.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Simbologija
### Savybė: gražesnės naujų sluoksnių spalvos
The \"random\" colors assigned to new map layers are no longer \"random\" but instead randomly selected from a preset palette of \"visually pleasing\" colors. Say goodbye to ugly baby puke green layers!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Braižymas
### Savybė: patobulinta žemėlapio autoriaus teisių dekoracija
- Autorių teisių tekste palaikomos išraiškos.
- Patobulintos teksto formatavimo parinktys, įskaitant šešėlius, kontūrus, fonus ir t.t.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: galima keisti pagrindinio lango mastelio juostos šrifto dydį ir šeimą
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: savo SVG kelias ir dydis šiaurės rodyklės dekoracijai
This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
## Duomenų valdymas
### Savybė: atnaujinti materializuotą rodinį
Naršyklėje paspaudus dešinį pelės mygtuką ant materializuoto rodinio (angl. view) dabar galima jį atnaujinti.

![image15](images/entries/125ee6837700d992fb8b6452ab1b346ba96c5cce.png.400x300_q85_crop.webp)

This feature was developed by [Etienne Trimaille](https://github.com/Gustry)
### Savybė: Z ir M palaikymas redaguojant neprisijungus
Keitimas neprisijungus dabar palaiko ir sluoksnius su Z ir M koordinatėmis.

This feature was funded by [Oester Messtechnik](https://messtechnik.ch/)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Savybė: QGIS projektų metaduomenys
Tęsiant metaduomenų darbą, pradėtą QGIS 3.0, 3.2 dabar palaiko QGIS projektų metaduomenis. Tai leidžia projekto savybėse laikyti detalius metaduomenis, įskaitant santraukas, raktažodžius, kontaktinę informaciją, nuorodą ir t.t.

![image16](images/entries/eb1394b46bf05e8a9b6be480cac4382c2f22a865.png.400x300_q85_crop.webp)

Šią savybę finansavo Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) ERIKUS projekto rėmuose

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com) and [Faunalia](https://www.faunalia.eu)
## Formos ir valdikliai
### Savybė: kelių stulpelių išdėstymas kelių reikšmių pažymėjimų ryšio valdiklyje
Reikšmių ryšių valdiklis su įjungta galimybe žymėti daugiau nei vieną objektą dabar palaiko kelis stulpelius. Taip galima geriau išnaudoti horizontalią ekrano erdvę.

![image17](images/entries/5fb9e551ed835b45161f3a2e9a94320dc50d5b97.gif.400x300_q85_crop.webp)

This feature was funded by [Grundbuch- und Vermessungsamt des Kanton Zug](https://www.zg.ch/behoerden/direktion-des-innern/grundbuch-und-vermessungsamt/gis-fachstelle)

This feature was developed by [David Signer, OPENGIS.ch](https://opengis.ch)
### Savybė: leisti naudoti URL savo atributų formoms (UI failas)
UI failas bus atsisiųstas pirmą kartą panaudojus sesijoje. Taip galima lengvai platinti klientams atnaujintus UI failus.

This feature was funded by [SIRS](http://www.sirs-fr.com)

This feature was developed by [Denis Rouzaud, OPENGIS.ch](https://opengis.ch)
### Savybė: detalizacijos (kaskadinės) formos
QGIS 3.2 introduces drill-down (cascading) form support, where the values available in one field depend on the values of other fields. This feature allows users to create "value-relation" expressions based on the current value of another field in the same form. When the user modifies a field's value, the choices available in all related fields are filtered to match the new value -- allowing a hierarchical filtering strategy (drill-down, or cascading) inside a form.

![image18](images/entries/5990ff168d5b6b41176de4fa487964b97c32fafc.gif.400x300_q85_crop.webp)

Šią savybę finansavo Grant Boxer, NaturalGIS, Tudor Bărăscu, NotioGIS, République et canton de Neuchâtel, Arpa Piemonte, Nelson Silva, QGIS Danish User Group, Bo Victor Thomsen and Lene Fischer, North River Geographic

This feature was developed by [Alessandro Pasotti (North Road)](https://north-road.com)
## Sluoksnių legenda
### Savybė: pasirinktinis tekstas virš vektorinių sluoksnių simbolių
Ši savybė leidžia naudotojams pridėti papildomą informaciją prie simbolių legendoje.

![image19](images/entries/2e1e6a3c4b154c35642096a4c2235c2b2d706200.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Savybė: kopijuoti ir įkelti Grupes/Sluoksnius iš vieno QGIS projekto į kitą.
Leidžiama kopijuoti ir įkelti grupes arba sluoksnius iš vieno projekto į kitą.

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
## Žemėlapio maketas
### Savybė: nuo duomenų priklausantis lentelės šaltinis atributų lentelės elementams
When an attribute table is set to a \"Layer features\" source, this new feature allows the underlying vector layer from which to source features to be data defined.

(Visi esami lentelės atributai (stulpelių nustatymai) paliekami tokie, kaip yra, taigi nustačius sluoksniui nuo duomenų priklausomą lentelę su kitokiais laukais, gausime tuščius stulpelius lentelėje)

This feature was funded by [Kartoza/InaSAFE](http://kartoza.com/en/)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: projekto duomenys įdedami į išdėstymo eksportus
Įrašant spausdinimo išdėstymą į SVG, PDF ar nuotraukas dabar į sukurtą failą įtrauks ir projekto metaduomenis. Skirtingų metaduomenų elementų palaikymas priklauso nuo konkretaus eksporto formato.

Šią savybę finansavo Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) ERIKUS projekto rėmuose

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: geresnis mastelio juostos teksto formatavimas
QGIS 3.2 suteikia visą diapazoną teksto formatavimo parinkčių, kurias galite naudoti mastelio juostos tekstui, pvz. buferius, šešėlius ir fono formas.

Neperskaitomas mastelio juostos tekstas liko praeityje!

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Apdorojimas
### Feature: Improved \'Join by attribute table\' algorithm
The \'Join by attribute table\' algorithm has been upgraded to support one-to-many joins (i.e. create separate features for each matching feature) as well as an option to discard records which could not be joined. Additionally, an optional prefix for joined fields can now be specified.

![image20](images/entries/93dd2a52ae3ed2b7a3842f6379d033fabc7932fe.png.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin, Nyall Dawson](http://www.imhere-asia.com/)
### Savybė: įkelti scenarijų iš šablono
Nauja parinktis įkelti apdorojimo scenarijus iš savo šablono

![image21](images/entries/fce801da5d7b82a1038f19d603d64046e6a399a0.gif.400x300_q85_crop.webp)

This feature was developed by [Matteo Ghetta (Faunalia)](http://www.faunalia.eu/)
### Savybė: geoobjektų filtro algoritmas apdorojimo modeliams
Apdorojimo modeliuotojui pridėtas naujas geoobjektų filtravimo algoritmas. Leidžia filtruoti šaltinio geoobjektus naudojant išraiškas ir siųsti atitinkančius geoobjektus į skirtingas išvestis kaip galutinius produktus arba skirtingai algoritmų eilei tolimesniam apdorojimui.

Read this [blog post for more information](http://www.opengis.ch/2018/05/28/how-to-filter-features-in-qgis-using-the-graphical-processing-modeler/).

![image22](images/entries/3b1e5e0d5b1874d2e3f0cbb8070eb82dedd89a4e.png.400x300_q85_crop.webp)

This feature was funded by [QGIS User Group Switzerland](https://qgis.ch)

This feature was developed by [Matthias Kuhn, OPENGIS.ch](https://opengis.ch)
### Savybė: zoninė histograma
Šis naujas algoritmas prideda laukus, rodančius kiekvienos unikalios rastro sluoksnio reikšmės, esančios poligonais apibrėžtose zonose, skaičių.

![image23](images/entries/577c3ed7ed7875d51e968a135bfd532f97d692c8.jpg.400x300_q85_crop.webp)

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: Sąjungos, skirtumo ir persidengimo algoritmai migruoti į C++
QGIS savas geoapdorojimo algoritmas buvo migruotas iš Python'o į C++. Be greitaveikos pagerinimo, šiuo pakeitimu buvo išspręsti ir keli riktai.

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Feature: \'Project points (cartesian)\' algorithm
Šis naujas Apdorojimo algoritmas projektuoja taškus iš įvesties taškų sluoksnio nustatytu atstumu ir kryptimi (azimutu). Palaiko dinaminius parametrus atstumui ir krypčiai, taigi atstumas ir kryptis gali būti paimti iš laukų reikšmių ar išraiškų.

This feature was funded by [Nyall Dawson (North Road)](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: daugiau algoritmų gavo dinamines parametrų reikšmes
QGIS 3.2 extends the work begun in 3.0 to allow \"dynamic\" parameters for selected Processing algorithms. Dynamic parameters allow users to use expressions or field values to specify the value of a parameter while the algorithm executes, so e.g. the buffer size can be dynamically calculated for each individual feature buffered.

Nuo 3.2 šie algoritmai palaiko dinaminius parametrus:
- Trinti sykles
- Išimti pasikartojančias viršūnes
- Paprastinti
- Glotninti
- Pritraukti prie tinklelio
- Subpadalinti
- Transekcija
- Versti

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: kelių žiedų buferio (pastovaus atstumo) algoritmas
This new algorithm computes multi-ring (\'donuts\') buffer for all the features in an input layer, using a fixed or dynamic distance and rings number.

Šią savybę sukūrė Alex Bruy
### Feature: New \"segmentize\" algorithms
QGIS 3.2 į Apdorojimą buvo pridėti du nauji algoritmai kreivių geometrijos segmentavimui.

\"Segmentize by maximum distance\": The segmentization is performed by specifying the maximum allowed offset distance between the original curve and the segmentized representation.

\"Segmentize by maximum angle\": The segmentization is performed by specifying the maximum allowed radius angle between vertices on the straightened geometry (e.g the angle of the arc created from the original arc center to consective output vertices on the linearized geometry).

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: parinktis kurti taškus visose poligono dalyse
The \"Centroid\" and \"Point on surface\" algorithms have a new option to create points for every individual part of input geometries.

This feature was developed by [Mathieu Pellerin](http://www.imhere-asia.com/)
### Savybė: geometrijų pavertimo algoritmas
This new algorithm allows rotation of features by a set angle. The rotation can occur around a preset point or each individual feature\'s centroid.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Line sinuosity in \"Add Geometry Attributes\"
The \"Add Geometry Attributes\" algorithm now calculates line sinuosity and straight distance for line layers.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: importuoti nuotraukas su geo žymomis
In QGIS 3.2 a new \"Import geotagged photos\" algorithm has been added to Processing. It allows selection of a folder which it will scan for jpg files which have been geotagged and creates a PointZ layer with the result, with attributes for photo path, altitude, direction and timestamp.

Galima pasirinkti skenuoti rekursyviai ir pasirinktinai galite kurti lentelę su nuotraukomis, kurios buvo neperskaitomos arba neturėjo geožymų.

Šis algoritmas automatiškai nustato išeities lentelę, kad ji naudotų išorinių resursų valdiklį susietų nuotraukų rodymui atributų formoje.

![image24](images/entries/399ace1f3d437044b9fb478afb820372195b79d8.png.400x300_q85_crop.webp)

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: x/y koordinačių sukeitimo vietomis algoritmas
Algoritmas sukeičia X ir Y koordinates vietomis įvesties geometrijose. Gali būti naudojamas taisyti geometrijas, kurios netyčia turi supainiotas ilgumos ir platumos vietas.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Feature: Sort order option for \"Add Incremental Field\"
Šis pakeitimas leidžia naudotojams pasirinktinai nurodyti rikiavimo tvarką priskiriant reikšmes didėjančio lauko pridėjimo algoritme. Anksčiau reikšmės buvo visada pridedamos naudojant pradinę geoobjekto tvarką. Po šio pakeitimo naudotojai gali valdyti tvarką, kuria geoobjektams priskiriamos reikšmės.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: atstumo parametro vienetų indikatorius
When an algorithm uses a \"distance\" type parameter, the units will now be shown next to the parameter. This avoids the confusion when running algorithms which use distances where the unit depends on a layer or CRS parameter - e.g. the distance parameter in the buffer algorithm gives the distance in layer units\... so now in QGIS 3.2 we show those units directly within the dialog. Hopefully this leads to less user confusion and accidental \"1000 degree buffers\"!

Papildomai - jei vienetai nurodyti laipsniais, greta parametro rodoma nedidelė įspėjimo piktograma. Užvedus pelę ant šios piktogramos naudotojui patariama perprojektuoti duomenis į tinkamą projektuotą vietinę koordinačių sistemą.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: algoritmų žurnalą galima įrašyti/valyti/kopijuoti
Algoritmų vykdymo dialoge buvo pridėti nauji mygtukai, kurie leidžia naudotojui įrašyti dabartinį žurnalą (į tekstinį ar HTML failą), kopijuoti žurnalo turinį į iškarpinę arba išvalyti žurnalą.

Šią savybę finansavo SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: pleišto buferio algoritmas
Šis naujas algoritmas sukuria pleišto formos buferius iš įvesties taškų.

Azimuto parametras suteikia kampą (laipnsniais) pleišto viduriui nuo taško. Buferio plotis (laipsniais) nurodomas pločio parametru. Pastebėtina, kad pleištas tęsis iki pusės kampinio pločio pagal azimuto kryptį. Išorinis buferio spindulys nurodomas išoriniu spinduliu ir pasirinktinai gali būti nurodytas vidinis spindulys.

Algoritmas palaiko dinaminius parametrus azimutui, pločiui ir spinduliui.

Pradinė šio algoritmo išvestis yra kreivinio poligono geometrija, bet ją galima automatiškai segmentuoti į poligonus priklausomai nuo išvesties formato.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: kintamo pločio buferiai
Buvo pridėtas naujas apdorojimo algoritmas, kuriantis kintančio pločio buferius, įskaitant ir smailius buferius (su nurodytu pradžios ir pabaigos diametru) ir kintamo pločio buferius iš linijos m reikšmės.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: rastro perklasifikavimo algoritmai
Du nauji QGIS rastro perklasifikavimo algoritmai buvo pridėti į Apdorojimą. Juos paprasta naudoti, nors jie greiti ir stabilūs, veikia su BET KOKIU rastro sluoksnio tipu, kokį tik palaiko QGIS!
- Perklasifikavimas pagal sluoksnį: perklasifikuoja rastrą naudojant diapazonus, nurodytus per min/maks/reikšmės laukus vektorinėje lentelėje.
- Perklasifikavimas pagal lentelę: perklasifikuoja rastrą naudojatn fiksuotą lentelę, įvestą naudotojo algoritmo dialoge.

Šią savybę finansavo SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: sąjungos algoritmas su vienu sluoksniu
The union algorithm can be now run with just a single input layer in order to resolve any overlaps among the layer\'s features. For example, if an area is covered by three features, that area will be cut out from those features and three new features will be added, copying attributes of the original features.

![image25](images/entries/a32fa9ccc63bd3f91e6696ee8f9aef32f61b4691.png.400x300_q85_crop.webp)

This feature was funded by [InaSAFE DFAT](https://www.dfat.gov.au/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)
## Programos ir projekto parinktys
### Savybė: privalomi projekto sluoksniai
Privalomų sluoksnių negalima išimti iš projekto. Taip pridedamas papildomas saugumas projekto naudotojams, kad jie neišims sluoksnių, kurie jiems pasirodė nereikalingi (pvz. naudojamų jungtims, ryšiams ir išraiškoms).

![image26](images/entries/b65c47d1a41ab4a7ad545696b4985ebd7edb9f75.png.400x300_q85_crop.webp)

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
### Savybė: projektų įrašymas ir skaitymas iš PostgreSQL duombazės
Users can now save their projects within a PostgreSQL database. Project can be saved in menu **Projects \> Save To \> PostgreSQL** and loaded using menu **Projects \> Load From \> PostgreSQL**. Projects saved in database can be loaded also through the browser dock (projects show up under the schema where they were saved, together with other layers).

Saving/loading QGIS projects must be explicitly enabled in PostgreSQL connection settings: there is a new option \"Allow saving/loading QGIS projects in the database\" which is disabled by default.

New API has been introduced that allows creation of custom project storage implementations (may be used by plugins). Related QEP: <https://github.com/qgis/QGIS-Enhancement-Proposals/issues/118>

This feature was funded by [Arpa Piemonte (Dipartimento Tematico Geologia e Dissesto) within ERIKUS project](https://www.arpa.piemonte.it/)

This feature was developed by [Martin Dobias, Peter Petrik (Lutra Consulting)](https://www.lutraconsulting.co.uk) and [Faunalia](https://www.faunalia.eu)
## Naršyklė
### Savybė: įrašyti/įkelti XYZ kaladėlių jungtis
Iš naršyklės skydelio, XYZ kaladėlių įrašus galima eksportuoti/importuoti į/iš XML failo.

![image27](images/entries/678a1f4686de353f4a04fc83877e27c18d2fca7d.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Savybė: galima rankiniu būdu nurodyti projekto namų kelią
This new feature in QGIS 3.2 allows the project home path (which is used by the browser to create the \'Project Home\' item) to be set by users for a project, instead of always matching the location where the project is saved.

This allows users to set the project home to a folder which contains data and other content, and is especially useful for organisations where QGIS projects are not stored in the root folder of a organisational \'project\'.

Projekto namų aplankas taipogi gali būti santykinis aplankas, tokiu atveju jis bus skaičiuojamas nuo projekto įrašymo vietos.

The path can be set through the Project Properties dialog, or by right-clicking on the Project Home browser item and selecting \'Set Project Home\'.

![image28](images/entries/db297eb148a7d62dd58aab40dca32ee91d148831.png.400x300_q85_crop.webp)

Šią savybę finansavo SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Duomenų tiekėjai
### Savybė: tinklelio sluoksnių palaikymas
Buvo atlikti pradiniai darbai palaikymui tinklelių sluoksnių, kurie gali rodyti duomenis ant struktūrinio ar nestruktūrinio tinklelio (gardelės) greta rastro ar vektorinio sluoksnio. Tai vis dar vykstantis darbas, kuris turėtų būti baigtas QGIS 3.4. Kol kas buvo sukurta nauja biblioteka MDAL, skirta skirtingų tinkleliai paremtų duomenų palaikymui ir yra naujas API, o naudotojo sąsaja dar nepadaryta.

Daugiau informacijos rasite:

<https://github.com/qgis/QGIS-Enhancement-Proposals/issues/119>

and

<https://github.com/lutraconsulting/MDAL>

![image32](images/entries/91c7bf725bc4afecc9efbeaedc8e98ad153b73b4.png.400x300_q85_crop.webp)

This feature was developed by [Peter Petrik and Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk)
### Savybė: automatiškai nustatyti numatytąjį stilių ArcGIS Feature Server sluoksniams
Kai sluoksniai į QGIS 3.2 įkeliami iš Geoobjektų Serverio, jie automatiškai turės tokį patį stilių, kaip buvo nurodyta tame sluoksnyje serveryje, atitinkant sluoksnio išvaizdą, kai jis įkeliamas į ArcGIS.

Šią savybę finansavo SMEC/SJ

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: greitesnės Oracle užklausos
Kai kurios Oracle sluoksnių operacijos stipriai pagreitėjo, pavyzdžiui nuo raidžių dydžio nepriklausantis geoobjektų atitikimas.

This feature was funded by [North Road](https://north-road.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: riboti Oracle duombazės jungties lentelių sąrašą iš anksto nurodytoje schemoje
Šis pakeitimas leidžia Oracle duombazės jungtyje nurodyti schemą. Jei nurodyta, bus rodomos tik lentelės iš schemos.

Previously the option existed to restrict the scan to tables which belong to the user, but this option does not support the use case where a connection must access tables from a different user, and the default \"scan everything\" setting is too expensive (since it often takes multiple minutes to perform, especially when geometryless tables are shown).

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
### Savybė: tik skaitymo palaikymas kreivinėms Oracle geometrijoms
Anksčiau šios geometrijos buvo tyliai išmetamos.

This feature was funded by [Open Spatial](http://www.openspatial.com)

This feature was developed by [Nyall Dawson (North Road)](https://north-road.com)
## Priedai
### Savybė: DB tvarkyklėje pridėta užklausų istorija
3.2 galima saugoti SQL užklausas. Užklausų istoriją galima rasti DB tvarkyklės priedo SQL lango kortelėje.

![image33](images/entries/9c6074aaf1e989c460833535788d0b396a677e34.png.400x300_q85_crop.webp)

This feature was developed by [Salvatore Larosa](https://github.com/slarosa)
### Savybė: DB tvarkyklės SQL vykdymas fone
Šią savybę sukūrė Paul Blottiere
## 3D savybės
### Savybė: 3D poligonai: pasirinktinai generuoti tolimas sienas
Kartais duomenų rinkiniai su 3D poligonais neturi tinkamos viršūnių rikiavimo tvarkos (pagal ar prieš laikrodžio rodyklę) ir dėl to 3D rodinyje gaunami ne patys geriausi rezultatai: arba kai kurių poligonų (sienų) trūksta - arba kai kurių poligonų šešėliai braižomi neteisingai. Su įjungta nauja parinktimi **Pridėti tolimas sienas**, teseliatorius sugeneruos trikampius abiem kryptimis (priekio ir fono), dėl ko stipriai pagerėja tokių duomenų rinkinių braižymo kokybė.

The only downside when using this option is that more graphical memory is used (double amount of vertex data). Make sure to set culling mode to \"Back\" when using this option, otherwise there would be no visible difference as the scene would still render polygons with incorrect shading.

Šioje nuotraukoje matomi laisvai prieinamas Prahos 3D pastatų duomenų rinkinys.

![image34](images/entries/875e423e7a857a509812da6f46d468486fb7fd99.png.400x300_q85_crop.webp)

This feature was developed by [Martin Dobias (Lutra Consulting)](https://www.lutraconsulting.co.uk/)

{{<content-end >}}
