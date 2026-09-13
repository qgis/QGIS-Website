---
draft: 'true'

---
# Amurum forest reserve habitat and avifauna mapping with QGIS in Nigeria
Amurum forest reserve is located near the city of Jos, Plateau state, Nigeria. It was established in conjunction with the initiation of the A.P. Leventis Ornithological Research Institute (APLORI) for the purpose of natural conservation, education and research. APLORI is hosted by the Department of Zoology at the University of Jos. Yearly a group of approximately eight highly motivated students from all over Nigeria obtain training in conservation biology, statistics (with R) and as of 2011 GIS as well. During two weeks in December 2011 we studied basic GIS concepts and applied those with QGIS for various conservation purposes. In this article we describe the way in which we used QGIS to map the habitats and its determinants of Amurum reserve and how the basic habitat maps were used to obtain strata for the purpose of efficiently determining the spatial distribution of the avifauna including the biodiversity.

![Training Group](./images/nigeria_jos1.jpg){.align-right}
## 고도 , 음역기복, 경사, 서식지 정보의 공간 데이터 가시화
1) Mapping elevation and groundtruthing: We downloaded (free) elevation data originating from the NASA Shuttle Radar Topographic Mission (SRTM) for the area in which Amurum is located. (Information about the global elevation data set can be found here: <http://www.cgiar-csi.org/data/elevation/item/45-srtm-90m-digital-elevation-database-v41>).
2) Gdal 툴을 이용하여  원본 데이터 셋에 대한 레이어 병합 및 비교적 소규모 지역에서의 레스터 정보를 추출하였습니다.  또한 우리는 수집한 다양한 위치의 고도 데이터는 GPS로 부터 취득 하였습니다.
3) 그리고 레이다 영상의 고도정보를 GPS에서 수집된 고도정보와 비교검토 하여 일치 시키는 작업을 하였습니다.
이과정을 통하여 만들어진 지형모델을 Gdal Tools릉 이용하여 해당지역의 음영기복  및 경사도를 공간연산하였습니다. 이러한 다양한 일련의 작업들은 생태학적 관점에서 시사하는 바가 크다고 할 수 있으며
그이유는  서식지의 지형형태에 대한 강한 연관성을 보여주기 때문입니다.

![QGIS screenshot](./images/nigeria_jos2.jpg){.align-right}
4) 우리는 보다 시각적으로 우수한 지도를 개발하려는 목표 때문에 고해상도 맵으로 부터 취득된 고도 기복도(클리핑 처리된)를 공간 보간 작업을 하였습니다. 우리는 GdalTOOLS 기능 중 Warp tool 기능을 사용하였습니다. 
그리고 보다 부드럽고 매끄러운 등고선을 취득하기 위하여 CONTOUR TOOL을 이용하였습니다.
5) 대상지 구역으로 부터의 좌표 획득은  GPS 기기로부터 실측 자료자료로 부터 얻었졌다. 경유지와 경유 궤적은 GPS 도구를 사용하여 간단하게 얻어올 수 있었다. 취득된 경유지와 궤적을 토대로 폴리곤 셰이프 파일을 생성하였다. 생성된 파일의경유궤적정보는 실제 측정치와 유사한 형태대로 지도상에 도시 된다.
6) 우리는  오픈레이어스 플러그인의 구글영상지도를 사용하여 빠르고 정확하게 Amurum 지역의 서식지 지도를 제작할 수 있습니다. 서식지는 세가지 형태로 구분 될 수 있었습니다. 정의된 지역은사바나 기후지역, 열대림지역, 암석돌출 지역 으로 구분될 수 있었습니다.우리 는 구글영상 이미지를 기본으로 세가지 형태의 서식지를 폴리곤으로 분류하여 편집기능을 이용하요 폴리곤을그릴 수 있었다. 스냅핑 옵션 설정을 통하여 단알 폴리곤들을 구축 하였다.

## 새의 분포와 다양성 을 지도화
서식지 주제도들은 일반적으로 위치가 불규칙하게 나타나게 되어 있습니다. 특정한 지역내의  산개 되어 있는 서식지 정보들을 특정한 형태 의 비율로 구성하여 표면정보로 표현하는 방법으로 분석 할 수 있었습니다.(분류계통화)

![Training Group](./images/nigeria_jos3.jpg){.align-right}

The random points in fTools were used for this purpose. All the locations were visited during two mornings by four groups of students (2 per group) giving a total of 38 random locations dispersed throughout the reserve. The observation data were entered in a spreadsheet and analyzed using R. In addition, the Shannon-Wiener diversity index was calculated using R. After merging the location file with the resulting observation data it was exported as a csv file which was loaded into QGIS using the "Add delimited text layer" tool. On the basis of the above mentioned layers a map was constructed presenting some of the most important landscape features and avian diversity of the Amurum reserve.
## 결론
Overall, the course was a great success. We - a group of students with no previous GIS experience \-\-- enjoyed working with QGIS a lot. Within just two weeks time we were able to develop an extremely useful map of the reserve. Amongst others, the extents of the various habitats were determined which allows for stratification and thus for better estimates of abundances of various kinds of organisms. Basically we are now able to do better ecological research using QGIS as an open source platform.

![QGIS map: Diversity of Amurum Forest Reserve](./images/nigeria_jos4.png){.align-right}
## 저자
참여한 Abengowe Elmond Chiadikaobi, Adeyanju Temidayo Esther, Akiemen Nerioya, Albert Malangale Tauje, Azi Abok Joel, Echude Daniel, Eelke Folmer, Nwaogu Chima Josiah, Onoja Joseph Daniel, Yadok Biplang 에게 행운이 함께하기를
