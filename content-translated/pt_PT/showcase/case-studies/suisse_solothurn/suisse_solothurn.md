---
draft: 'true'

---
# O QGIS no conjunto de FOSSGIS governamentais do Cantão de Solothurn na Suíça
![](./images/suisse_solothurn1.png){.align-left}

O Cantão de Solothurn fornece serviços e infraestrutura a 250,000 cidadãos. No ano de 2001 o Estado Parlamentar decidiu migrar do Windows para Linux. As motivações foram a independência de um vendedor particular, e encorajar a iniciativa livra e reduzir custos de licenças. Como resultado o desenvolvimento do departamento SO!GIS no Cantão do Solothurn começou a entregar requerimentos SIG a mais de 3500 empregados com a estratégia FOSSGIS.

O primeiro passo que tomámos foi a introdução do UMN MapServer e a criação do SO!MAP cliente que oferece uma forma fácil de usar um WebSIG cliente para mais de 3500 empregados. O segundo passo foi a migração de toda a informação geoespacial das shapefiles para um motor de base de dados espacial PostGIS. A introdução foi muito bem sucedida, mas faltava um desktop SIG fácil de usar. 

Depois de uma avaliação de diferentes Desktop SIG nós decidimos usar o QGIS em conjunto com o GRASS, substituindo o ESRI ArcInfo e o ArcView3 em 2006.

A decisão foi conduzida pelos seguintes aspetos:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Organização do Projeto OSGeo
- Tradução do GUI em língua alemã
- Documentação escrita em língua alemã
- Um programador ativo (Marco Hugentobler) perto de Solothurn na Suíça.
- Nós podemos contratar o  Marco Hugentobler para implementar elementos perdidos /em falta como a Digitalização e a composição de mapas.
- Desenvolvimento da Aplicação e Módulo com Python
- Crescente comunidade de utilizadores
- Comunidade de programadores muito ativa
- Independência de um único sistema operativo

## Onde usamos o QGIS
Em contraste com os mapas interativos do UMN MapServer, o desktop SIG oferece uma vista flexível sobre a informação geoespacial de Solothurn. O Desktop SIG QGIS está em uso em mais de 50 utilizadores para o seu trabalho diário. Mas muito deles não são especialistas SIG. Eles querem visualizar e/ou capturar informação geoespacial com uma interface de utilizador intuitiva. 

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA! contém um inventário humanamente legível para os modelos de dados e dos utilizadores não espcialistas em SIG que é capaz de usar esta base de dado para descobrir a informação que necessitam.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusões
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Sobre o autor:
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

Este artigo foi contribuído em Maio de 2009 pelo Dr. Horst Düster. Ele é coordenador SIG no Departamento de Geoinformação no Cantão de Solothurn, Suíça.
