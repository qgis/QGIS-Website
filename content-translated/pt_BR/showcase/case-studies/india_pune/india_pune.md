---
draft: 'true'

---
# O uso da consola python para preparar um mapa offline a partir de um WMS (transferência de mosaicos)
Este estudo explica como preparar mapas off-line a partir de WMS / WFS ou qualquer mapa carregado na vista do mapa do QGIS  baixando os tiles com a ajuda de um script no console de python. O script também gera um mosaico de todas as peças para posterior utilização.

Acessar mapas raster / vetor através do serviço de mapeamento Web service (WMS) é muito comum e eficiente. Ele tem várias vantagens, tais como segurança, estilos centralizados e flexíveis mapa. Um exemplo são os mapas do Google, Yahoo, Bing, MODIS, Landsat, mapas publicados pela NASA, NRSC (Índia). A desvantagem / limitação de WMS é que funciona via internet ou intranet. Pode não ser possível obter conexão com a internet sempre, especialmente no campo durante o levantamento. Também WMS funciona lento, em comparação com qualquer formato de imagem off-line, como GeoTiff, jpg, img etc.
## Utilização do QGIS
QGIS provides a tool to connect/access any WMS service. WMS connection is based on simple URL and once connection is established map can be seen on QGIS mapview. If we save the map of visible extent from QGIS mapview as jpg (File \> Save as Image) it creates world file which has the geographic coordinate information of particular region E.g. sample.jpg is the map and sample.jpgw have the coordinates. That means the downloaded image is georeferenced. We can download tiles in grid format manually and use later offline. Manual downloading is possible if the area is very small or low resolution images are fine.

![QGIS with WMS tiles](./images/india_pune1.png){.align-left}
## Terminal Python
A short script was written in "Python Console" with help available on QGIS official website in PyQGIS Developer Cookbook. Script consists of basically 4 components as following,
1. Coordenadas X,Y (canto superior esquerdo e canto inferior direito) do primeiro mosaico
2. Tamanho do mosaico a ser transferido (ex.: 0.001 X 0.001 graus)
3. Número de mosaicos a transferir (cálculo baseado na extensão total do mapa e no tamanho do mosaico)
4. Caminho de saída para armazenar os ficheiros/mosaicos de saída

The script works in two simple for loops first which defines the extent of map in QGIS map view and run row/columns. Once the map extent is set then map is loaded in QGIS. The delay of 3 seconds (depends on internet connection) was introduced before saving map as jpg in user defined directory. Once the script is executed all the tiles created in directory can be directly loaded in QGIS or single mosaic is prepared from Raster \> Miscellaneous \> Merge or Build Virtual Raster (Catalog). Both tools generates mosaic but basic difference in Merge creates an image independent of tiles whereas Virtual raster generates a link in all individual tiles (tiles are required).

![Python script and directory where tiles are stored](./images/india_pune2.png){.align-left}

O método tem uma limitação, quando altera o mapa no servidor acabará por se refletir offline (mapa transferido). Neste caso o usuário tem de repetir o processo e gerar um novo mapa offline. A segunda limitação é a que o mapa criado será um formato de imagem; não pode ser usado para mapas temáticos ou classificação de imagens. Com alguns esforços extra alguns mapas de uso do solo podem ser convertidos em vector sem perda de dados.
## Âmbito
O mosaico gerado é uma imagem pura mesmo se for transferida a partir de uma mapa temático (7-8 cores). Usando uma ferramenta avançada como a reclassificação, camada/banda guardada no raster pode ser convertida num vector poligonal. O WMS tem vários pedidos tais como, getcapabilities, getmap, getfeatureinfo, etc. Os polígonos podem ser recuperados usando a informação do atributo getfeatureinfo. O script pode ser convertido num módulo para que qualquer pessoa sem conhecimentos de programação possam usar o script.
## Conclusão
A experiência em cima mostra que o QGIS pode ser usado num nível avançado. Com conhecimentos básicos de programação qualquer um pode escrever pequenos scripts ou um módulo para melhorar a qualidade do trabalho e poupar tempo. Dentro do QGIS, aceda a um repositório de módulos que é desenvolvido pelo mundo é o melhor para o QGIS. O Livro de Programador PyQGIS é um recurso muito bom para escrever um script e para processar dados raster mais facilmente com ajuda das ferramentas GDAL.
## Autores
Este artigo foi contribuído em Maio 2014 pelo Prashant Kadgi, que vive em Pune (Índia) e actualmente trabalha como consultor na GIS APP Consultancy Services. Desde 2009, ele usa SIG & DR em projectos NRM, floresta, e-governance e software em diferentes regiões da Índia e do mundo. 
- Contact: <kadgiprashant@gmail.com>
- Website www.gisappco.com (em construção)
