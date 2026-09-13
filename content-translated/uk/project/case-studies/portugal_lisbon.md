---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: проект
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: Картографування у QGIS для потреб сервісу біорізноманіття та екології (HABEaS)
type: case-study

---
{{<content-start >}}
# Картографування у QGIS для потреб сервісу біорізноманіття та екології (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

Основною задачею цієї платформи є надання вільного доступу до широкого спектру даних з питань біорізноманіття та екології Середземноморського басейну, які раніше були розкидані по різних приватних та публічних установах. На сьогодні HABEaS охоплює південь Португалії, але протягом 2012/на початку 2013 вона буде розширена до північної Португалії та кантону Тулза у Боснії та Герцеговині. У довгостроковій перспективі ми хочемо розширити цей інструмент на весь середземноморський басейн.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

Просторові дані, зібрані у HABEaS, також використовуються Всесвітнім фондом дикої природи для ідентифікації лісів з високою природоохоронною цінністю (High Conservation Value Forests, HCVF) на півдні Португалії, що є необхідним для власників, які хочуть отримати сертифікат Forest Stewardship Council (FSC).

![](../images/portugal_lisbon3.jpg)

Щоб визначити яке значення для збереження мають ділянки ми використовували редактор моделей плаґіна SEXTANTE, щоб створити модель, яка розраховує перетин всіх шарів HABEaS з межами ділянки. За допомогою цього ж інструмента ми також можемо розрахувати кількість вугілля, яке зберігається на кожній ділянці.

![](../images/portugal_lisbon4.jpg)
## Підсумки
QGIS проста у використанні та має потужні аналітичні можливості. Інтеграція з GRASS GIS та SAGA за допомогою плаґіна SEXTANTE дозволила нам виконати складні аналізи та об'єднати їх за допомогою редактора моделей. Також у QGIS дуже просто створювати високоякісні друковані карти та експортувати їх у формат SVG для подальшої обробки у потужному графічному редакторі Inkscape.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Автор
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias є аспірантом Центру прикладної екології (Instituto Superior de Agronomia, Університет Лісабона) та консультантом середземноморської програми Всесвітнього фонду охорони дикої природи (WWF).

{{<content-end >}}
