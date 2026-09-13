---
draft: 'true'

---
# QGIS na pilha FOSSGIS governamental do Cantão de Solothurn, na Suíça
![](./images/suisse_solothurn1.png){.align-left}

O cantão de Solothurn fornece serviços e infra-estrutura para 250.000 cidadãos Solothurn. No ano de 2001, o Parlamento do Estado decidiu migrar do Windows para o Linux. As motivações eram para ser independente de um fornecedor específico, para incentivar a livre empresa e reduzir os custos de licença. Como resultado o Departamento de SO!SIG Cantão de Solothurn começou a entregar os requisitos de SIG de mais de 3500 funcionários com uma estratégia FOSSGIS.

O primeiro passo que demos foi a introdução da UMN MapServer e da criação de um cliente SO!MAP. Que oferece um cliente WebGIS fácil de usar  para todos os 3500 funcionários. O segundo passo foi a migração de todos os nossos dados geoespaciais de Shapefiles para o banco de dados espacial no PostGIS. A introdução foi muito bem sucedida, mas faltou uma área de trabalho SIG fácil de usar.

Após avaliação de uma área de trabalho SIG diferente, decidimos usar QGIS em conjunto com a GRASS, substituindo ESRI ArcInfo e ArcView3 em 2006.

A decisão foi conduzida pelos seguintes aspectos:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- Organização do Projecto OSGeo
- Tradução do GUI em língua alemã
- Documentação escrita em língua alemã
- Um programador activo (Marco Hugentobler) perto de Solothurn na Suíça.
- Nós podemos contratar o  Marco Hugentobler para implementar elementos perdidos /em falta como a Digitalização e a composição de mapas.
- Desenvolvimento da Aplicação e Módulo em Python
- Crescente comunidade de usuários
- Comunidade de programadores muito activa
- Independência de um único sistema operativo

## Onde usamos o QGIS
Em contraste com os mapas interactivos servidos pelo UMN MapServer , o SIG Desktop tem para oferecer uma visão flexível aos dados geoespaciais de Solothurn. QGIS SIG desktop está em uso por mais de 50 usuários para o trabalho diário. Mas muitos deles não são especialistas em SIG. Eles querem visualizar e / ou capturar dados geoespaciais com uma interface de usuário intuitiva.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA contém um inventário humano legível dos modelos de dados e usários Não-Experiente-SIG tem a facilidade de usar esse banco de dados para descobrir a informação de que necessitam.

![\"SO!GIS Layer\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn2.png){.align-right}

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy \-\-- they can prepare for geoprocessing, editing and map composing in an individual way.

![\"SO!GIS Suche\" plugin developed at the Canton of Solothurn](./images/suisse_solothurn3.png){.align-right}

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Conclusão
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Autor
![Horst Düster](./images/suisse_solothurnaut.jpg){.align-left height="200px"}

Este artigo foi contribuído em Maio de 2009 pelo Dr. Horst Düster. Ele é coordenador SIG no Departamento de Geoinformação no Cantão de Solothurn, Suíça.
