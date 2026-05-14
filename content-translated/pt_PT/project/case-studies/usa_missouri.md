---
HasBanner: false
archived: true
date: 2013-02-01
draft: false
featured: false
section: projeto
sidebar: true
thumbnail: images/usa_missouri1.png
title: Mapas QGIS Históricos de Registos de Herpetofauna (no Missouri, EUA)
type: case-study

---
{{<content-start >}}
# Mapas QGIS Históricos de Registos de Herpetofauna (no Missouri, EUA)
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>February 01, 2013</span>
</p>

The Missouri Herpetological Atlas Project (MOHAP) was initiated in 1997 as a result of the desire to obtain and easily update detailed distribution maps for Missouri (United States of America) amphibians and reptiles. A database was established to store all valid localities, including records published in historical literature sources and specimens vouchered from museums. From the database, a series of maps can be produced representing both locality records and \"county records\" for each species.

MOHAP hosts a web site at <http://atlas.moherp.org/> that describes the project in detail and displays a variety of static maps, all produced by QGIS. An atlas, published as a downloadable PDF, is released periodically as a gratis publication in the spirit of open access to scientific research (Daniel, R.E. and B.S. Edmond. 2012. Atlas of Missouri Amphibians and Reptiles for 2011. \<<http://atlas.moherp.org/pubs/atlas11.pdf>\>). Published maps are used by field biologists, land managers, and others to better understand species\' distributions in Missouri.

As of February 2013, the MOHAP database contained 31,495 entries representing the specimens housed in 34 museum collections and cited in 32 historical literature sources; 5,118 documented county records; 6,884 unique localities; and 12,866 unique species / locality combinations. The state\'s herpetofauna consists of 113 species.
## Gerar e Exportar Mapas Estáticos
O processo de criação de mapas com o QGIS começa com os dados guardados em várias tabelas do PostgreSQL, ativadas espacialmente com PostGIS. Porque os mapas são estáticos e finalmente destinados tanto para a Web ou um atlas impresso, estes são gerados automaticamente para cada espécie, utilizando um módulo QGIS Python personalizado (Figuras 1,2).

<figure>
<img src="../images/usa_missouri1.png" class="align-right" alt="usa_missouri1.png" />
<figcaption>Custom map generation and export user interface, maps are generated and exported in a batch process.</figcaption>
</figure>

The final species maps have a clean and professional appearance (Figure 3). To better understand species\' distributions, a series of base maps are also created and labelled (Figure 4). Because of the way styles are managed within each data layer, the base map layers can also be incorporated into a set of species maps with little extra effort.

<figure>
<img src="../images/usa_missouri2.png" class="align-right" alt="usa_missouri2.png" />
<figcaption>Maps are displayed as static images.</figcaption>
</figure>

<figure>
<img src="../images/usa_missouri3.png" class="align-right" alt="usa_missouri3.png" />
<figcaption>Labelled Level III Ecoregion map for Missouri and surrounding states.</figcaption>
</figure>

## Conclusões
No início do projeto MOHAP, várias ferramentas comerciais e proprietárias foram usadas ​​para armazenar e processar dados e produzir mapas para publicação. A partir de 2007, começámos a mover todos os aspetos do projeto para software de código aberto. O QGIS, junto com PHP, PostgreSQL, PostGIS, Python, e ReportLab, formam o eixo de código aberto para MOHAP, permitindo efetivamente que o projeto e todos os dados existirem livre de embaraços de software proprietário.

O QGIS contém suporte nativo para o PostGIS e uma arquitetura de módulos Python, que foram fundamentais na criação do mapa geração automatizada e exportação. A documentação da API extensa foi utilizada juntamente com o livro de programador de módulos para criar exatamente o que precisávamos para a automatização. O apoio da comunidade também é muito bom e inclui uma grande variedade de módulos construídos e compartilhados prontos para usar. 

Apesar de usarmos o QGIS numa pequena forma e específica, as suas capacidades e extensibilidade usando Python é mais do que suficiente para lidar com projetos maiores e mais complexos.
## Sobre o autor:
<figure>
<img src="../images/usa_missouriaut.jpg" class="align-left" height="200" alt="usa_missouriaut.jpg" />
<figcaption>Brian Edmond</figcaption>
</figure>

This article was contributed by Brian Edmond in February 2013. He is a Senior Systems Analyst in Computer Services at Missouri State University. He holds a BS in Wildlife Biology from the University of Missouri and has spent his career in the intergrade zone between biology and technology.

{{<content-end >}}
