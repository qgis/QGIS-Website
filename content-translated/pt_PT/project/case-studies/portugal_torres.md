---
HasBanner: false
archived: true
date: 2010-11-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/portugal_torres1.jpg
title: QGIS e GRASS aplicados à gestão paleontológica na costa Oeste de Portugal
type: case-study

---
{{<content-start >}}
# QGIS e GRASS aplicados à gestão paleontológica na costa Oeste de Portugal
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>November 01, 2010</span>
</p>

The Associação Leonel Trindade -- Sociedade de História Natural (ALT-SHN) is a non profit institution headquarted in Torres Vedras, Portugal, specialized in paleontology. The institution manages a large fossil collection, mainly from Upper Jurassic. One of the key issues in paleontological management is to assess spatial context of the sites from where the fossils are retrieved -- hundreds of sites representing thousands of different specimens.
## O Projeto
![](../images/portugal_torres1.jpg)

Back in 2008, we came up with the idea of exploring GIS technologies to support the investigation and get a more holistic perspective on the heritage we were dealing. This idea boosted SIGAP Project (GIS applied to paleontology) \[2\]. The project, supported by public and private entities -- mainly the Municipalty, Digiterra.hu and the Army\'s Geographic Institute (IGeoE), aimed three goals:
- Levantamentos de campo com recurso a GPS diferencial de modo a recolher as coordenadas dos sítios;
- Construir um modelo de risco para identificar ameaças ao património paleontológico;
- Montar uma base de dados para gerir toda esta informação e posteriormente iniciar a inventariação da colecção.

## Software utilizado
O QGIS foi a plataforma central de todo projecto. Os dados de campo eram descarregados directamente no QGIS e posteriormente editados e manipulados de modo a obter a informação final. A interface GRASS providenciada pelo QGIS permitiu-nos levar a cabo análises espaciais complexas sobre rasters e assim obter o modelo de risco que necessitávamos para planear futuramente o trabalho de campo. Além disso, QGIS também nos permitiu importar dados de uma base de dados PostGIS e visualizá-los no QGIS.

<figure>
<img src="../images/portugal_torres2.jpg" class="align-right" alt="portugal_torres2.jpg" />
<figcaption>Vector point data editing and visualization</figcaption>
</figure>

The choice for QGIS was also encouraged by the multi platform support. The institution has three distinct facilities, and each of those facilities has different systems — we have Mac, Windows PC and Linux PC, therefore it\'s of extreme importance that we have the freedom to install the software on any machine we want so we don\'t get stuck to a particular computer.

<figure>
<img src="../images/portugal_torres3.jpg" class="align-right" alt="portugal_torres3.jpg" />
<figcaption>Paleontological Risk Map</figcaption>
</figure>

## Conclusões
The overall experience with QGIS can only be rated has being very good and recommendable. From our point of view, the main advantage of QGIS is that it\'s not just a GIS software — it\'s a productivity suite for spatial data. It allowed us to take advantage of other powerful tools within a single work environment. From QGIS you can work with GRASS, with PostGIS, with GPS data, with webservices and with tens of useful plug-ins developed by users worldwide. The user friendly interface is also a big advantage, especially if you have to train first time users has we\'ve done. The easyness of the interface makes production of maps an everyday task and brought people closer to spatial approaches \[3\].
## Referências
- \[1\] www.alt-shn.org (portuguese only)
- \[2\] MANO, André. (2009) -- Sistema de Informação Geográfica Aplicado à Paleontologia. Paleolusitana: Revista de Paleontologia e Paleoecologia, Torres Vedras: Alt-Sociedade de História Natural. ISSN 1647-2756, n.º 1, p. 245-250.
- \[3\] Mano, André. (2010) -- Projecto SIGAP, Trabalho de Projecto apresentado como requisito parcial para a obtenção do grau de Mestre em Ciência e Sistemas de Informação Geográfica. ISEGI -- UNL, Lisboa, 2010

## Sobre o autor:
<figure>
<img src="../images/portugal_torresaut.png" class="align-left" height="200" alt="portugal_torresaut.png" />
<figcaption>André Mano</figcaption>
</figure>

This article was contributed in November 2010 by André Mano. He is responsible for the Geopraphic Department of Associação Leonel Trindade -- Sociedade de História Natural. His area of interest is focused on geotechnology applications to the fields of paleontology, archeology and cultural heritage.

{{<content-end >}}
