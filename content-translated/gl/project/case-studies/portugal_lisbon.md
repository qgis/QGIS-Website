---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: proxecto
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: Usando QGIS para mapear áreas importantes para os servizos de biodiversidade
  e ecosistema (HABEaS).
type: case-study

---
{{<content-start >}}
# Usando QGIS para mapear áreas importantes para os servizos de biodiversidade e ecosistema (HABEaS).
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

A finalidade desta plataforma é fornecer acceso libre a unha ampla variedade de datos sobre servizos para a biodiversidade e os ecosistemas da cunca mediterránea que se atopaban espallados a través de varias institucións tanto públicas coma privadas. No presente HABEas WebGIS cobre o Sur de Portugal pero para finais do 2012/comezos do 2013 será expandido ó Norte de Portugal e tamén o Cantón de Tuzla en Bosnia e Herzegovina. No longo prazo queremos ampliar a ferramenta á totalidade da cunca mediterránea.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

A información xeográfica contida en HABEaS tamén foi empregada por WWF para fornecer suporte para a identificación de Bosques de Alto Valor de Conservación (HCVF polas súas siglas en inglés) no Sur de Portugal, o cal é un paso obrigatorio para os terratenentes que desexan que os seus bosques reciban a Certificación do Consello de Bosques (FSC polas súas siglas en inglés).

![](../images/portugal_lisbon3.jpg)

Para determinar os valores de conservación de cada propiedade usamos SEXTANTE Modeller para crear unha secuencia de comandos que intersecte tódalas capas de HABEaS coas fronteiras da propiedade. Usando esa mesma ferramenta fomos tamén capaces de crear unha secuencia de comandos que calcule automáticamente a cantidade de carbono contida actualmente en cada propiedade.

![](../images/portugal_lisbon4.jpg)
## Conclusións
QGIS é sinxelo de usar e ten unhas capacidades de xeoproceso moi poderosas. A integración das ferramentas GRASS GIS e SAGA GIS permitíronnos realizar varias análises espaciais complexas e de canalizalas usando SEXTANTE Modeller. Tamén foi moi sinxelo producir mapas de alta calidade co novo Print Composer e exportalos a formato SVG para una posterior edición con Inkscape, que é un poderoso editor de gráficos vectorias de código aberto.

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Autor
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias é un estudante de doutorado no Centro de Ecoloxía Aplicada (Instituto Superior de Agronomia, Universidade Técnica de Lisboa) e consultor para o Programa Mediterráneo do Fondo Mundial da Natureza (WWF)

{{<content-end >}}
