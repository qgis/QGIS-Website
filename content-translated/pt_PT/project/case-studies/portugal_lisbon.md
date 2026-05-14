---
HasBanner: false
archived: true
date: 2012-01-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/portugal_lisbon1.jpg
title: A  utilização do QGIS para Mapear as Áreas Hotspot para a Biodiversidade e
  Serviços de Ecossistema (HABEaS)
type: case-study

---
{{<content-start >}}
# A  utilização do QGIS para Mapear as Áreas Hotspot para a Biodiversidade e Serviços de Ecossistema (HABEaS)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>January 01, 2012</span>
</p>

HABEaS —— Hotspot Areas for Biodiversity and Ecosystem Services is an online geographic information system (WebGIS) that was created by the [Centre for Applied Ecology](http://www.isa.utl.pt/ceabn/content/2/123/homepage) ([Instituto Superior de Agronomia](http://www.isa.utl.pt/home/), Technical University of Lisbon), Worldwide Fund for Nature (WWF) and Faunalia.

O objetivo principal desta plataforma é fornecer acesso gratuito a uma variedade de dados sobre biodiversidade e serviços de ecossistema para Bacia Mediterrânica que foi espalhada por um número variado de entidades públicas e privadas. Presentemente HABEaS WebSIG abrange o Sul de Portugal, mas para fins de 2012/princípios de 2013 será expandida para o Norte de Portugal e também para o Cantão Tuzla na Bósnia Herzegovina. No longo caminho queremos expandir esta ferramenta a toda a Bacia Mediterrânica.

![](../images/portugal_lisbon1.jpg)

Since the main goal of this tool is to promote free and easy access to information on biodiversity and ecosystem services we decided to use only free and open source software, that any person or entity can use regardless of their location or financial constraints. The website where HABEaS WebGIS is hosted on a server that runs Debian Linux and was developed with Drupal CMS. PostgreSQL/PostGIS was used to store the data and QGIS was used to process and analyze the GIS that we obtained from several entities. We used both QGIS\'s native tools but also GRASS GIS and SAGA GIS tools through the GRASS plugin and SEXTANTE Toolbox.

![](../images/portugal_lisbon2.jpg)

A informação geográfica contida no HABEaS também está a ser usado pela WWF para fornecer suporte na identificação de Florestas de Alto Valor de Conservação (FAVC) no sul de POrtugaç, que é um passo importante para os proprietários que querem que as suas florestas  recebam a Certificação Forest Stewardship Council (FSC).

![](../images/portugal_lisbon3.jpg)

Para determinar que valores de conservação ocorre em cada propriedade nós usámos o Modelador SEXTANTE para criar um script que intersecta todos as camadas HABEaS com os limites da propriedade. Usando a mesma ferramenta nós conseguimos também criar um script que automaticamente calcula a quantidade de carbono que atualmente é armazenada em cada propriedade.

![](../images/portugal_lisbon4.jpg)
## Conclusões
 QGIS é de fácil uso e é muito poderoso nas capacidades de geoprocessamento. A integração das ferramentas do GRASS GIS e SAGA GIS através da Caixa de Ferramentas SEXTANTE permite-nos executar um número complexo de análises espaciais e interligá-las usando o Modelador SEXTANTE. Produz facilmente mapas de qualidade alta com o novo Compositor e exporta-os em formato SVG para editar no Inkscape que é um poderoso editor de gráficos vetorial de código aberto. 

In general, our experience with QGIS has been very positive, the software runs smoothly and the community is very active and supportive. Reported bugs are usually resolved shortly after being reported by users and QGIS developers are always willing to listen to "end user\'s" needs and suggestions.
## Sobre o autor:
<figure>
<img src="../images/portugal_lisbonaut.jpg" class="align-left" height="200" alt="portugal_lisbonaut.jpg" />
<figcaption>Filipe Dias</figcaption>
</figure>

Filipe Dias é um doutorando na Centro de Ecologia Aplicada (Instituto Superior de Agronomia, Universidade Técnica de Lisboa) e consultor do Programa Mediterrânico do Fundo Mundial para a Natureza (WWF).

{{<content-end >}}
