---
draft: 'true'

---
# Modelo de geoprocessamento no QGIS para simplificar o primeiro nível de análise de microzoneamento sísmico
The Institute of Environmental Geology and Geoengineering (IGAG) of the National Research Council (CNR) is located in Rome, in the Area of Research \"Roma 1\". It was founded in 2002 by regrouping five former research Institutes and Centers that had been active for more than 40 years in their field of expertise. IGAG covers a wide range of scientific topics in the field of Earth sciences, mainly focusing towards the study of:
- Geoquímica ambiental e remediação de solos e águas contaminadas.
- Depósitos minerais e processamento mineral, incluindo o tratamento de águas residuais.
- Geologia de engenharia e segurança na escavação de rochas.
- Evolução geológica recente;
- Mitigação de riscos naturais
- Geoarqueologia e arqueometria 
- Geologia Marinha
- Geomática, análise SIG e desenvolvimento.

O estudo de microzoneamento sísmico de nível 1 da área de Pietramontecorvino (Apúlia, sul da Itália, localizada ao longo da cordilheira dos Apeninos Centro-Sul) faz parte de um projeto, em colaboração com a Basin Authority of Apulia (Puglia AdB) e o Departamento de Geologia e Geofísica (DGG) da Universidade de Bari, visando o microzoneamento sísmico de 63 municípios da região de Foggia. A atividade foi promovida pelo Departamento de Proteção Civil da Itália (DPC) e financiada pelo Comitê Interministerial do Planejamento Econômico (CIPE nº 20/2004).
## Ferramenta de  geoprocessamento no QGIS para primeiro nível de estudos de microzoneamento sísmico.
O microzoneamento sísmico avalia o risco sísmico na escala local e tem o propósito de identificar áreas do território caracterizadas pelo comportamento sísmico homogêneo. O primeiro nível de microzoneamento sísmico tem como objetivo definir as propriedades litológicas e a geometria das unidades geológicas que caracterizam essas porções do território (microzonas).

A observação dos danos causados por um terremoto geralmente apresentam variações em escala local, causadas não apenas pelas estruturas geológicas, mas também pela diferente qualidade e tipos nas estruturas de construções, resultando em diferentes riscos sísmicos.

O microzoneamento sísmico avalia o risco sísmico local, através da identificação de áreas caracterizadas por um comportamento sísmico homogêneo. 

The Guidelines and Criteria for Seismic microzoning 2008 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>) provide standards for seismic microzoning studies on Italian territory; they distinguish three levels of increasing depth (from 1 to 3).

O primeiro nível do microzoneamento sísmico consiste na criação de 3 mapas temáticos: 
1. Mapa de pesquisa contendo as pesquisas para estudos de microzonação sísmica;
2. Mapa geolitológico, obtido por meio de mapas geológicos e geomorfológicos de escala detalhada integrando dados existentes de litologia, estratigrafia e geotecnia relacionados aos estudos;
3. Mapa de microzoneamento sísmico de nível 1 (o produto principal do microzoneamento de nível 1), identificando as microzonas em três categorias de riscos locais:
   - Zonas estáveis;
   - Zonas estáveis propensas à amplificação do solo;
   - Zonas instáveis.

O objetivo deste trabalho é contribuir para a criação de uma metodologia para o processamento de dados topográficos, geológicos, geofísicos e geotécnicos visando a elaboração de mapas de microzoneamento sísmico de nível 1, através do uso de ferramentas de código aberto.

A ferramenta Graphical Modeler integrada na última versão do QGIS (2.8.1) foi usada para a criação de um modelo de geoprocessamento simples. Esta ferramenta é útil para automatizar uma das análises frequentemente realizadas para a criação de mapas de microzoneamento sísmico de nível 1, em particular para identificar zonas instáveis como feições de polígonos.

O modelo faz uso de diferentes softwares de código aberto e bibliotecas (GRASS, GDAL, QGIS), demonstrando a utilidade do QGIS como uma interface simplificada e unificada para ferramentas GFOSS (Geospatial Free e Open Source Software) heterogêneas (Fig. 1).

![(Fig. 1) Screenshot from the geoprocessing model.](./images/italy_igag1.png){.align-right}

O modelo recebe como entrada (Fig. 2):
- Um shapefile de curvas de nível que contenha um campo com valores de elevação;
- The name of the field containing elevation values;
- A resolução do raster desejado em metros para o MDE e Declividade (padrão 10);
- Um shapefile de polígono do qual serão extraídas feições intersectando áreas com declividade maior que 15 graus;
- O nome da camada de polígono resultante.

![(Fig. 2) Model input form (left) and execution log (right).](./images/italy_igag2.png){.align-right}

Quando iniciado, o modelo executa as seguintes operações: 
- A ferramenta GRASS v.to.rast.attribute converte as linhas de contorno de elevação para raster, tomando o shapefile do contorno, o nome do campo z e a resolução do raster como entrada;
- A ferramenta GRASS r.surf.contour gera o modelo de elevação tomando como entrada o arquivo de saída raster temporário do passo anterior e a resolução do raster;
- The GDAL tool "gdaldem" generates the slope expressed as degrees from the elevation model;
- A ferramenta GRASS r.mapcalculator é usada para gerar um raster de 1 bit identificando áreas com declividade maior que 15 graus (este valor está codificado nas diretrizes de microzoneamento, e por isso é fixo), usando a expressão:

if(A\>15,1,null())

onde A é o raster temporário de declividade gerado pelo gdaldem;
- The GDAL tool "gdal_polygonize" converts the 1 bit raster to polygons;
- The QGIS tool "Intersection" is used to overlay the areas with slope greater than 15 degrees with the chosen intersection layer.

O resultado é uma camada de polígono com áreas propensas à instabilidade devido a um valor de declividade superior a 15 graus, extraído automaticamente de um mapa temático, como uma camada de polígono de deslizamento de terra (Fig. 3) ou um mapa litológico.

![(Fig. 3) The model output (in red) shows highly unstable areas extracted from a landslides layer (orange).](./images/italy_igag3.png){.align-right}
## Conclusões
This work clearly demonstrates that open source GIS tools like QGIS, GRASS, GDAL/OGR, can successfully be used for spatial analysis and data processing aimed at first level seismic microzonation studies. In this example work, QGIS has been used as a simplified and unified interface for different high quality GFOSS tools; the Graphical Modeler allows to intuitively construct geoprocessing models that can be easily shared as portable and cross-platform tools that doesn\'t require expensive software licenses. The tool leverages the QGIS modeling capabilities to graphically chain different algorithms, defining input and output parameters and leaving to the software the task of managing intermediate data output. The use of GRASS algorithms does not require defining and using a GRASS database and mapset, greatly simplifying the design of the model. Future developments include the creation of a package of tools and models, based on open source software, that can be used to simplify and speed up spatial analysis tasks necessary for seismic microzonation studies.
## Referências
- G. Baldassarre; Gallicchio, S.; Giannandrea, P. & Tropeano, M.: \"Relazione Finale Geolitologica per la microzonazione sismica di livello 1dei Comuni della Provincia di Foggia Dipartimento di Geologia e Geofisica dell\'Università di Bari, 2011\"
- Cavinato,G.P.; Cavuoto, G.; Coltella, M.; Cosentino, G.; Paolucci, E.; Peronace, E. & Simionato, M.: \"Studio di fattibilità per il monitoraggio e la messa in sicurezza delle aree urbane a rischio di stabilità statica e vulnerabilità strutturale del Comune e della Provincia di Foggia -CIPE 20/2004 Consiglio Nazionale delle Ricerche - Istituto di Geologia Ambientale e Geoingegneria, 2013, 526\"
- Contributi per l\'aggiornamento degli \"Indirizzi e criteri per la microzonazione sismica \" 2008. Ingegneria sismica, Pàtron Editore Bologna, 2011 (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB28083>)
- Gruppo di lavoro MS, 2008. Indirizzi e criteri per la microzonazione sismica. Conferenza delle Regioni e delle Province autonome - Dipartimento della protezione civile, Roma, 3 vol. e Dvd, Presidenza del Consiglio dei Ministri, Dipartimento di Protezione Civile, 2008, 424. (<http://www.protezionecivile.gov.it/jcms/it/view_pub.wp?contentId=PUB1137>)

## Autores
Este artigo foi uma contribuição de março de 2015 entre Giusseppe Consentino e Francesco Pennica (www.igag.cnr.it).

![Giuseppe Cosentino](./images/guiseppe_cosentino.png){.align-left height="200px"}

Giuseppe Cosentino \<<g.cosentino@igag.cnr.it>\> is geologist and technologist specializied in Geographic Information Systems for the management of geological and engineering hazards. Currently working in the field of seismic microzonation and environmental characterization of the lands in contaminated sites. Areas of interest: geological and environmental hazards, cartography, structural geology, explorative drillings.

![Francesco Pennica](./images/francesco_pennica.png){.align-left height="200px"}

Francesco Pennica provides GIS and WebGIS software development and data management: GeoServer, MapServer, ArcGIS Server, GeoNetwork OGC standard based webgis services, Java, HTML, CSS, Javascript, Python, PHP languages and frameworks, WebGIS front-end development with OpenLayers, ExtJS, GeoExt, JQuery, GWT, Ext-GWT, Google Maps API SQL, geodatabase management, PostgreSQL, PostGIS, GIS desktop software based analysis and scripting (ArcGIS, GRASS, GFOSS tools), Software configuration and management in Linux and Windows based servers and desktops.
