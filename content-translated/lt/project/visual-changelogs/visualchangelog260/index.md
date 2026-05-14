---
HasBanner: false
draft: false
releaseDate: '2014-10-31'
section: projektą
sidebar: true
title: QGIS 2.6 pakeitimai
type: visual-changelog

---
{{<content-start >}}
# QGIS 2.6 pakeitimai{#changelog26 }
Laidos data: 2014-10-31

QGIS 2.6.0 pakeitimų žurnalas. Mes pridėjome daug naujų savybių, pataisymų ir patobulinimų, kad populiariausia atvira darbastalio GIS taptų dar funkcionalesne ir naudingesne.

Whenever new features are added to software they introduce the possibility of new bugs - if you encounter any problems with this release, please file a ticket [on the QGIS Bug Tracker](http://hub.qgis.org).

Norime padėkoti programuotojams, dokumentuotojams, testuotojams ir dar būriui kitų žmonių, kurie savo noru aukojo savo laiką ir pastangas (arba finansavo tuo užsiimančius žmones).

From the QGIS community we hope you enjoy this release! If you wish to donate time, money or otherwise get involved in making QGIS more awesome, please wander along to [qgis.org](https://qgis.org) and lend a hand!

Na ir pagaliau norėtume padėkoti savo rėmėjams už neįkainojamą finansinę paramą šiam projektui:
- **GOLD Sponsor: Asia Air Survey, Japan** <http://www.asiaairsurvey.com/>
- SILVER Sponsor: [Sourcepole AG, Switzerland](http://www.sourcepole.com/)
- SILVER Sponsor: [State of Vorarlberg, Austria](http://www.vorarlberg.at/)
- BRONZE Sponsor: [Lutra Consulting, UK](http://www.lutraconsulting.co.uk/)
- BRONZE Sponsor: [www.molitec.it, Italy](http://www.molitec.it/)
- BRONZE Sponsor: [www.argusoft.de, Germany](http://www.argusoft.de)
- BRONZE Sponsor: [www.openrunner.com, France](http://www.openrunner.com)
- BRONZE Sponsor: [GKG Kassel,(Dr.-Ing. Claas Leiner), Germany](http://www.eschenlaub.de/)

A current list of donors who have made financial contributions large and small to the project can be seen on our [donors list](https://qgis.org/en/site/about/sponsorship.html#list-of-donors). If you would like to become an official project sponsor, please visit [our sponsorship page](https://qgis.org/en/site/about/sponsorship.html#sponsorship) for details. Sponsoring QGIS helps us to fund our six monthly developer meetings, maintain project infrastructure and fund bug fixing efforts.

If you enjoy using QGIS, please consider making a donation to support the project - either [financial](https://qgis.org/en/site/getinvolved/donations.html) or of [your time and skills](https://qgis.org/en/site/getinvolved/index.html)! Lastly we would like to also take a moment to encourage you to fund a [special campaign](http://blog.vitu.ch/10102014-1046/crowdfunding-initiative-automated-testing) by one of our QGIS developers to get a working test suite for QGIS so that we can improve out quality assurance process and deliver you the best possible releases.

QGIS yra atvira programinė įranga ir jums jokiu būdu neprivalu mokėti norint ją naudoti. Priešingai, mes norime skatinti kiek galima daugiau žmonių naudoti ją nepriklausomai nuo jūsų finansinio ar visuomeninio statuso - mes tikime, kad duodant žmonėms įrankius, teikiančius galimybę daryti erdvinius sprendimus, galima sukurti geresnę visos žmonijos visuomenę.

{{<table-of-contents >}}
## Bendra
### Savybė: projekto failo pavadinimas savybėse
Dabar projekto savybių dialoge galite matyti pilną QGIS projekto failo kelią.

![](images/entries/8662dc4a69298f603dd9038d1199ab16fd25f786.webp)
### Savybė: galimybė išimti paskutinį tašką matavimo metu paspaudus del ar backspace mygtuką
Dabar kai matuojate plotus ir atstumus, jūs galite išimti iš skaičiavimo paskutines nereikalingas viršūnes paspaudę delete arba backspace mygtuką.

![](images/entries/ed471908937cb068e2f004e7b3311f2bdf307042.webp)
### Savybė: pažymėti susijusį geobjektą drobėje iš ryšių valdiklio
### Savybė: redaktoriaus valdikliai
Mes padarėme keletą redaktoriaus valdiklių patobulinimų:
- naujas datos/laiko keitimo valdiklis, kuriame galima nurodyti tuščią datą
- filtro eilutės keitimas
- tinkamas NULL interpretavimas keitimo valdikliuose
- foto valdiklis išlaiko NULL reikšmę
- tinklo valdiklis išlaiko NULL reikšmę
- atributų lentelė gali atskirti 0 nuo NULL
- intervalo valdiklis palaiko priešdėlį

![](images/entries/78fd27b2cf736f37bdf97694a5018f29c609c6cb.webp)
### Savybė: pasirinktinai naudoti tik poaibį prijungto sluoksnio laukų
Kurdami vektorių junginį dabar galite naudoti tik poaibį susijusių laukų.

![](images/entries/14023cf2ee768960d9c4a43da6e2a1624d10b3c3.webp)
### Savybė: išraiškų laukai (virtualūs laukai)
Sometimes you want to have an attribute that is calculated and that is always \'fresh\' - reflecting the current state of the feature properties. Now you can add virtual fields to your table which are based on an expression.

![](images/entries/5fe53ad54b8d0cf8b7a22b90e733a421bb929506.webp)
### Savybė: veiksmai dabar gali turėti susijusią piktogramą
Kuriant savo vektorinio sluoksnio veiksmą, jūs dabar galite nurodyti ir piktogramą, kuri bus naudojama su veiksmu.

![](images/entries/e7bd5b306e3a72cc111a81f86a053b42679aa2f8.webp)
### Savybė: papildomi išraiškų tipai ir parinktys
- Allow using `+` for string concatenation.
- New keyword: `attribute( feature, attribute_name )` - gets the specified attribute from a feature.
- New keyword: `$currentfeature` - returns the current feature.
- New keyword: `$atlasfeature` - returns the atlas feature.
- New keyword: `getFeature` - gets a matching feature from a layer.

![](images/entries/e2e079bec87be65ccc97055251fc2544be91aaab.webp)
### Savybė: klasės su graduotai ir kategorizuotais braižymais gali būti įjungtos/išjungtos
Dabar galite nuspręsti išjungti kai kurias klases graduotuose ir kategorizuotuose braižymuose jų visiškai neišimdami.

![](images/entries/84d11c6d978775d92f6a1902092795735d1f32b3.webp)
### Savybė: legendos patobulinimai
Baigta legendos / turinio perdarymo antra fazė. Įgyvendinta:
- API valymas (programuotojams)
- Žemėlapio sluoksnių matomumo grupės sluoksnių medyje. Šis naujas įrankinės mygtukas leidžia greitus pakeitimus tarp grupių sluoksnių, kurie turi būti matomi.
- Galimybė valdyti sluoksnių grupes per legendos įrankinę
- Naujas legendos įrankinės filtro mygtukas išims legendos elementus visų klasių, kuriuos šiuo metu nėra matomumo ribose. Tai puikus patobulinimas, nes tai užtikrina, kad žemėlapio legendoje nėra įrašų tų elementų, kurie realiai nesimato žemėlapyje. Šis mygtukas veikia tiek pagrindinio žemėlapio legendoje, tiek žemėlapio kūrėjyje, tiek WMS sluoksniuose.
- Nuo taisyklių priklausomų sluoksnių legenda gali būti rodoma pseudo-medžiu

![](images/entries/363048a7d08ac76d35463abbef514c65031922e7.webp)
## Duomenų tiekėjai
### Savybė: DXF eksporto patobulinimai
- medžio peržiūra ir atributų parinkimas dialoge sluoksnio priskyrimui
- užpildytų poligonų/HATCH palaikymas
- laikyti tekstą kaip MTEXT, o ne TEXT (t.y. įskaitant šriftą ir storį)
- support for RGB colors when there\'s no exact color match
- naudoti AutoCAD 2000 DXF (R15), o ne R12
- išimti R18 bandomus metodus

![](images/entries/4f615505e3fd6ec0b619278e42ecc5a3e79ac827.webp)
## Žemėlapio maketas
### Savybė: spausdinimo kūrėjo elementų slėpimas spausdinant/eksportuojant
Mes pridėjom varnelę ir priklausymo nuo duomenų mygtuką, kurie leidžia valdyti, ar elementas bus praleidžiamas spausdinant ar eksportuojant. Jei elementas nepažymėtas, jis bus matomas tik kūrimo metu.

![](images/entries/f334447d13ee49a6c4c5cb4322e3f12824643416.webp)
### Savybė: tuščių kūrėjo rėmų puslapių spausdinimų valdymas
Lentelėms ir HTML rėmams pridėta varnelė, kuri nurodo, ar turi būti eksportuojamas puslapis, kuris yra tuščiame rėme.

![](images/entries/1500ba6abdf5b314c760ebfc63e460731dcc5110.webp)
### Savybė: elementų medžio skiltis
Žemėlapio kūrėjo elementų medžio skiltyje elementus galima pažymėti, slėpti/rodyti, keisti užrakinimo būseną, o paspaudus du kartus - keisti elemento identifikatorių. Taip pat galite pakeisti elementų tvarką juos pertempdami.

![](images/entries/52b70bdf87d21a13c00798458bab6347dddd7910.webp)
### Savybė: daugiau kūrėjo rodyklių/linijų išvaizdos valdymo
- Linijų stilius gali būti keičiamas naudojant linijų simbolių dialogą
- Galima keisti rodyklės galvutės užpildymo ir krašto spalvas
- Galima keisti rodyklės galvutės krašto plotį

![](images/entries/49757b3cc09839edb8af38f1cb1317458f279110.webp)
### Savybė: pagal duomenis valdomi kūrėjo elementai
Daugelį kūrėjo elementų savybių dabar galima valdyti naudojant duomenų susiejimą. Įskaitant ir šias savybes:
- Permatomumą ir suliejimo režimą.
- Elemento pasukimą
- Žemėlapio mastelį, apimtis ir pasukimą
- Atlaso geoobjekto paraštes.
- Elemento dydį ir poziciją.
- Puslapio dydį, orientaciją ir puslapių skaičių.

![](images/entries/9f321489cd9c90eb4d66e577680fc5467756e58e.webp)
### Savybė: kūrėjo piešinius galima nurodyti kaip nutolusius URL
Žemėlapio kūrėjo piešinių elementai dabar palaiko nutolusius url kaip piešinių šaltinius. Šaltinis taipogi gali būti nustatomas pagal duomenis.

![](images/entries/05cd7008c231df3b3af874753b840669a605cb0f.webp)
### Savybė: kūrėjo lentelių patobulinimai
- Dabar galite keisti lentelės antraštės ir turinio teksto spalvas.
- Lenteles galima dalinti tarp kelių rėmų, leidžiant turiniui pasiskirstyti per skirtingų puslapių stulpelius.
- Pridėta parinktis antraštes rodyti pirmame rėme, visuose rėmuose arba nerodyti jokiuose rėmuose.
- Galima rankiniu būdu valdyti stulpelių pločius.
- Naujos lentelės šaltinio parinktys, įskaitant dabartinį atlaso geoobjektą ir vaikiniai geoobjektai pagal ryšį.
- Tuščių lentelių elgsenos pasirinkimas, įskaitant visos lentelės paslėpimą, tuščių langelių rodymą arba nurodyto teksto rodymą lentelės viduje.
- Pridėta varnelė filtruoti lentelės geoobjektus iki tų, kurie kertasi su dabartiniu atlaso geoobjektu.
- Pridėta varnelė pasikartojančių lentelės eilučių pašalinimui.

Pastebėtina, kad lentelės jau sukurtuose projektuose automatiškai nėra konvertuojamos į naują lentelių formatą, kuris palaiko šias savybes. Kad atsirastų nauji nustatymai, lentelės turi būti iš naujo įkeltos į kūrėją.

![](images/entries/9ccb75b2110daf0c95a3fba31ac18144c1345f0e.webp)
### Savybė: kūrėjo patobulinimai
Žemėlapio kūrėjas (naudojamas spausdinamų žemėlapių ruošimui) gavo eilę patobulinimą 2.6 QGIS versijoje.
- Dabar galite pakeisti mastelio juostos antrinę pildymo spalvą
- Paišant linijas/rodykles ir laikant nuspaudus shift klavišą, bus braižomos tik horizontalios, vertikalios ar 45 laipsniai pakreiptos linijos
- Paišant kitus naujus elementus ir laikant nuspaudus shift, bus paišomi kvadratai, laikant alt elementas bus paišomas nuo centro
- Dešinys paspaudimas daugiau nerakina elementų, nuo šiol tai valdoma per naują elementų skydelį. Užrakintų elementu daugiau nebegalima pažymėti kūrėjo drobėje taip leidžiant sąveikauti su žemiau esančiais elementais.
- Laikant alt ir spaudžiant kursoriaus klavišus, elementai bus perkeliami per 1 tašką
- Removed the destructive \'Load from template\' menu item, replace with a new non-destructive \'Add items from template\' action

![](images/entries/a7267ed637121bc9be70c5fa0afd2a63f9790bc7.webp)
### Savybė: pagerintas elementų pritraukimas
Pritraukimo ribos dabar nurodomos taškais, o tai leidžia tiksliau perkelti ir keisti elementų dydį padidinus. Grupėje esantys elementai daugiau nebenaudojami automatinio pritraukimo linijoms.

![](images/entries/8e43479380c28942345f3d9500dd956bd13f43e8.webp)
### Savybė: kelios žemėlapio elemento peržiūros
Sometimes it is useful to be able to show more than one overview frame for a map frame. For example if you want to show where your map is in local, regional and global context, using multiple overview maps can help you to achieve this. As of QGIS 2.6 you can now achieve this by assigning as many maps as you like to the \'overview\' role in your composition.

![](images/entries/88b55cc5f5e7cfb62486fe3b4867b7133ae66953.webp)
### Savybė: HTML elementų patobulinimai
Kūrėjo HTML elementui pridėtos kelios naujos parinktys:
- Galimybė rankomis įvesti HTML šaltinį
- Prieš paišant HTML turinį gali būti įvertintos QGIS išraiškos, esančios HTML šaltinyje
- Nuo duomenų priklausantis URL HTML šaltiniui
- Galima kurti naudotojo stilius, kurie permuštų HTML stilius

![](images/entries/7ed388f0c775b738648b2bd6eb6be0a75fa5816a.webp)
### Savybė: kūrėjo žemėlapio tinklelio patobulinimai
- Dabar galite turėti kelis tinklelius su skirtingomis savybėmis.
- Galit kombinuoti perprojektuotus tinklelius su ilg/plat tinkleliais.
- Galite naudoti standartinės QGIS simbologijos tinklelių linijas ir pan.
- Atsirado naujas tinklelio stilius - tik rėmas/anotacijos. Parinkus šį stilių bus nupaišytas tik rėmas ir anotacijos, nebus jokių tinklelio linijų ar kitų žymėjimų žemėlapyje.
- Dabar yra parinktis, valdanti kurioje žemėlapio elementu pusėje yra paišomas rėmas.
- Atsirado nauji rėmų brūkšniukų stiliai, tokie kaip vidiniai brūkšniukai, išoriniai brūkšniukai ir vidiniai brūkšniukai kartu su išoriniais.
- Patobulintos tinklelio anotacijos, pavyzdžiui atsirado daug naujų anotacijų formatų.
- Tinklelio anotacijoms dabar naudojami tipografiškai teisingi pirminiai ir dvigubi pirminiai simboliai.

![](images/entries/eeb61d7da3d3f95283b1bb47545cbdff9cc334ae.webp)
## Apdorojimas
### Savybė: internetinis modelių ir scenarijų rinkinys
Modeliai ir scenarijai gali būti atsiųsti iš internetinio rinkinio bei įdiegti tiesiogiai iš apdorojimo sąsajos. Rinkinys bus plečiamas naujais scenarijais ir modeliais, kuriuos pateiks Apdorojimo naudotojai.

![](images/entries/23e357ca0e559a33a7872206b306c0b1fbdb4b7d.webp)
### Savybė: naujas modeliuotojo įgyvendinimas
Modeliuotojas buvo perrašytas. Dabar jis turi papildomą funkcionalumą, tokį kaip įdėti modeliai be gylio apribojimo. Modeliai dabar saugomi kaip JSON failai. Išlaikytas suderinamumas su ankstesnėmis versijomis, taigi vis dar galite naudoti visus modelius. Dabar galite pertempti elementus iš įvesties ir algoritmų į modeliuotojo grafą.

![](images/entries/72bb8beaf97133424d1e68da67ae6fe79ea6faf6.webp)
## Programavimas
### Savybė: QGIS valdiklių API pakeitimai
In order to normalise the naming of QGIS widgets, some minor API changes have been made. Almost all edit widgets were renamed by adding \"Wrapper\" at the end of their names. In particular this concerns:
- QgsCheckboxWidget -\> QgsCheckboxWidgetWrapper
- QgsClassificationWidget -\> QgsClassificationWidgetWrapper
- QgsColorWidget -\> QgsColorWidgetWrapper
- QgsEnumerationWidget -\> QgsEnumerationWidgetWrapper
- QgsFilenameWidget -\> QgsFilenameWidgetWrapper
- QgsHiddenWidget -\> QgsHiddenWidgetWrapper
- QgsPhotoWidget -\> QgsPhotoWidgetWrapper
- QgsRangeWidget -\> QgsRangeWidgetWrapper
- QgsTexteditWidget -\> QgsTexteditWrapper
- QgsUniquevalueWidget -\> QgsUniquevalueWidgetWrapper
- QgsUuidWidget -\> QgsUuidWidgetWrapper
- QgsValuemapWidget -\> QgsValuemapWidgetWrapper
- QgsValuerelationWidget -\> QgsValuerelationWidgetWrapper
- QgsWebviewWidget -\> QgsWebviewWidgetWrapper

## QGIS Serveris
### Savybė: paieškos su GetFeatureInfo užklausa patobulinimai
<https://github.com/qgis/QGIS/commit/8888c5f0c0e0ffdf23453a20addf6abaf125845d>
### Savybė: pridėtas GetFeatureInfo geometrijos atributų tikslumo nustatymas
## Simbologija
### Savybė: geresnis atsitiktinių spalvų parinkimas
Mes patobulinome atsitiktinės spalvos algoritmą klasifikuotame braižyme taip, kad parenkamos spalvos vizualiai labiau skirtųsi viena nuo kitos.

![](images/entries/ec29c9d6eb23d01b4dbbae32a6e20fe0b1f48198.webp)
### Savybė: simbologijos naudotojo sąsajos patobulinimai
- Kur įmanoma, simbolių sluoksnio savybės išlaikomos keičiant simbolių sluoksnio tipą.
- Formos išdeginimo ir gradiento spalvos rampoms pridėti keitimo mygtukai.
- Automatinis etikečių ir gretimų intervalų ribų atnaujinimas.
- Persijungiant į pagal taisykles veikiantį braižymą, klasės automatiškai konvertuojamos iš kategorizuojamų į graduojamas klases.
- Graduoto braižymo etiketėms pridėti vienetai ir skaitmenų po kablelio skaičius.
- Pagerinta GUI reakcija po pakeitimų spalvų rampoje, atvirkštinėje spalvų rampoje ir kitose parinktyse.
- Išlaikyti simbolį persijungiant tarp paprasto, graduoto, kategorizuoto ir kitų braižymų.
- Pagerintos StdDev skaičiavimo režimo etiketės

![](images/entries/08305d5131c28c45b400662267ff0d174ef9c8ce.webp)
## Naudotojo sąsaja
### Savybė: sintaksės išskyrimas kodo redaktoriuose
Python'o scenarijų redaktoriuje, išraiškų kūrėjyje, filtrų languose, kūrėjo HTML ir CSS redaktoriuose.

![](images/entries/54b470a064d65d6d65aa66a8feece43ba8cbf6c4.webp)
### Savybė: spalvų paletės
Dabar galite kurti savas spalvų paletes naudojimui QGIS.
- Sava naudotojo globali spalvų paletė (parinkčių dialoge).
- Projekto spalvų paletė (projekto savybių dialoge).
- Spalvos rodomos spalvų mygtuko meniu ir naujos spalvos parinkimo dialoge.
- Galite importuoti/eksportuoti spalvas į GPL paletės failą.

![](images/entries/a156f408d7a87fc930095c8fd68e9fba0fc0a817.webp)
### Savybė: naujas spalvos parinkimo dialogas
Atsirado naujas savas QGIS spalvos parinkimo dialogas. Tarp savybių yra:
: - Atspalvio, sotumo, reikšmės, raudonos, žalios ir mėlynos spalvos komponentų slankikliai.
  - Alfa slankiklis.
  - Galimybė kopijuoti/įkelti html spalvų kodus (daugybe įmanomų formatų)
  - Prieš/po spalvos peržiūra su alfa peržiūra.
  - Interaktyvus 2D spalvų rampos valdiklis.
  - Atspalvio ratuko/trikampio valdiklis.
  - Keičiamos spalvų paletės, įskaitant galimybę kurti naujas paletes ir importuoti/eksportuoti spalvas į GPL paletės failą.
  - Gyvai veikiantys spalvų pavyzdžiai su galimybe bandyti nustatytą spindulį (priklausomai nuo OS palaikymo).
  - Leidžia sąveiką su kitomis programomis spalvų pertempimu (priklausomai nuo OS palaikymo).
  - Galimybė išjungti dialogą ir vietoje jo naudoti paprastą dialogą.

![](images/entries/7189c0fe2d1ff3fdc63c531a02f74b5d32b70bfd.webp)
### Savybė: vieno geoobjekto parinkimo įrankis sulietas su parinkimu stačiakampiu
Mes suliejome vienetinio parinkimo įrankį su parinkimu stačiakampiu. Jei norite parinkti vieną geoobjektą, tiesiog įjunkite stačiakampio įrankį ir tada vieną kartą spauskite ant geoobjekto (o ne tempkite, kaip paišant stačiakampį).

![](images/entries/f8a68fcdfcaa59e6162185acb5c92edb9145c881.webp)
### Savybė: sluoksnio pridėjimo į žemėlapio drobę elgsena
In many of QGIS\' dialogs that generate a new layer, the \'Add layer to map canvas\' checkbox is now checked by default so that the new layer automatically gets added to the map.

![](images/entries/f36f5912d2422a439d67b1a743fe81588e709dfb.webp)
### Savybė: pridėti piktogramų dydžiai 48 ir 64
Naudojantiems QGIS lietimui jautriuose įrenginiuose (arba jei jūs tiesiog mėgstate dideles, gremėzdiškas piktogramas), jūs galite padidinti piktogramų dydį iki 64 x 64 taškų!

![](images/entries/3be3f51da2f54a8395f054f757f9fae1948a6103.webp)
### Savybė: nauji spalvų mygtukai
This is probably one of the most useful new features in QGIS 2.6 -especially if you are involved a lot in cartography work. The colour button used everywhere in QGIS has been enhanced, with drop down menus, colour swatches, default colours, etc. Click on the drop down item to the right of the colour button to see the quick options. Click on the button to the left of the colour widget to see a standard colour chooser dialog.

![](images/entries/54c211513bc86d00a5bce01a17476481937e0fbe.webp)
### Savybė: identifikavimo įrankio kontekstinis meniu
Naudodami identifikavimo įrankį dabar galite spausti ant drobės dešiniu mygtuku, kad panaudotumėte identifikavimo įrankį kontekstiniame režime. Pasirodančiame meniu galite nurodyti, kurių tipų geoobjektus norite identifikuoti (jei norite - galite ir visų tipų objektus).

![](images/entries/c395c2ce4964826458a721a8a3f89cb7dc2853b5.webp)

{{<content-end >}}
