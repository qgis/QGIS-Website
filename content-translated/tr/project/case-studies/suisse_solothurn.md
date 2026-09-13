---
HasBanner: false
archived: true
date: 2009-05-01
draft: false
featured: false
section: proje
sidebar: true
thumbnail: images/suisse_solothurn1.png
title: QGIS  İsviçre'nin Canton Solothurn resmi FOSGIS alanında yer alır
type: case-study

---
{{<content-start >}}
# QGIS  İsviçre'nin Canton Solothurn resmi FOSGIS alanında yer alır
<p class="is-size-6 is-italic has-text-weight-medium">
  <span class="icon">
    <i class="fas fa-calendar-alt"></i>
  </span>
  <span>May 01, 2009</span>
</p>

![](../images/suisse_solothurn1.png)

 Solothurn Canton 250,000 Solothurn vatandaşına altyapı ve hizmet sağlamaktadır. 2001 yılında Devlet Parlamentosu Windowstan Linux a geçme kararı aldı. Bu karardaki etken tek özel bir üreticiden bağımsız, lisans masraflarını azaltmak ve ücretsiz teşebbüsü teşvik etmekti. Sonucunda SO!GIS Solothurn Canton bölümü 3500 den fazla işverene FOSSGIS stratejisi olarak GIS dağıtımına başladı. 

The first step we took was the introduction of UMN MapServer and the creation of a SO!MAP client that offers an easy to use WebGIS client for all the 3500 employees. The second step was the migration of all our geospatial data from Shapefiles to the PostGIS spatial database engine. The introduction was very successful, but an easy to use desktop GIS was lacking.

Farklı CBS masaüstü programının değerlendirilmesinden sonra ESRI ArcInfo ve ArcView3  ün kullanımı 2006 yılnda QGIS ve GRASS birliklte kullanılacak şekilde bırakılmıştır.

Karar aşağıdaki beklentileri karşılamalı:
- Due to our use of desktop GIS in a Linux Terminal Server environment, Java wasn\'t an option.
- OSGeo Pfoje-Yapısı
- GUI Almancaya çevrilmiştir
- Dokümentasyon Almanca yazılmıştır
- Aktif geliştirici (Marco Hugentobler) İsviçre Solothurn da bulunmaktadır.
- Marco Hugentobler ile Harita birleştirme ve Sayısallaştırma gibi kayıp / eksik özelliklerin geliştirilmesi için anlaşıldı.
- Pytonla Eklenti ve Uygulama geliştirme
- Gelişen kullanıcı topluluğu 
- Çok aktif geliştirme toplupuğu
- Tek bir işletim sisteminden bağımsızlık

## QGIS ı nerde kullanırız
In contrast to the interactive maps served by UMN MapServer, the desktop GIS has to offer a flexible view at the geospatial data of Solothurn. QGIS Desktop GIS is in use by more than 50 users for their daily work. But many of them are not GIS experts. They want to visualize and/or capture geospatial data with an intuitive user interface.

One of the most important Desktop GIS issues is the question: \"How do I get the information from the PostGIS geodata repository I need?\". Since our end users are unfamiliar with data models and the underlying structures of our spatial database, offering the users a raw connection to the PostGIS DB was not an option. We have a metadata database that stores the descriptions of all production data called \'SO!DATA\'.

SO!DATA contains a human readable inventory of the data models and the non-GIS-Expert user is able to use this database to discover the information they need.

<figure>
<img src="../images/suisse_solothurn2.png" class="align-right" alt="suisse_solothurn2.png" />
<figcaption>"SO!GIS Layer" plugin developed at the Canton of Solothurn</figcaption>
</figure>

To remove the need for end users to interact directly with PostGIS connections and table selection dialogs, a plugin has been developed in python. The plugin is called \"SO!GIS Layer\" (see Figure 1). The plugin connects to the SO!GIS PostGIS repository, gets the information of all published geospatial data layers from SO!DATA and offers the user a GUI to find the data layers they need. With this infrastructure in place, our users are happy —— they can prepare for geoprocessing, editing and map composing in an individual way.

<figure>
<img src="../images/suisse_solothurn3.png" class="align-right" alt="suisse_solothurn3.png" />
<figcaption>"SO!GIS Suche" plugin developed at the Canton of Solothurn</figcaption>
</figure>

Another required QGIS plugin we created is called \'SO!GIS Suche\'. This provides the possibility to search for locations like townships, addresses or cadastral parcels (see Figure 2). As a result the user is able to navigate very easily to an area of interest.

At the moment many other plugins are under development. These will support data manipulation, analysis or mapping for different projects. Our in-development plugins cover topics such as nature reserves, soil conservation, cadastral data verification, crisis management, abandoned sites and so on.
## Sonuç
Today we can say that using QGIS was the right decision for us. QGIS offers most of the features requested by our users. The Canton of Solothurn subcontracts the creation of features that QGIS lacks to commercial support providers. With PyQgis and PyQt there are excellent options for easy in-house application development based on QGIS. One huge benefit is the unlimited number of installations. Everyone who needs to use QGIS can use it without any limitations. To push the development of QGIS the Canton of Solothurn has invested approximately \$30,000 into QGIS every year since 2007. This is much more efficient and target-oriented than the payment of support into the black box of our former software provider. Apart from using FOSSGIS, the Canton of Solothurn also provides public geodata free of charge via the SO!ONLINE web portal.
## Yazar
<figure>
<img src="../images/suisse_solothurnaut.jpg" class="align-left" height="200" alt="suisse_solothurnaut.jpg" />
<figcaption>Horst Düster</figcaption>
</figure>

Bu makale Mayıs 2009 yılında Dr.Horst Düster in katkılarıyıla oluşturulmuştur. Kendisi Canton Solothurn da  Geoinformasyon bölümünde CBS koordinatördür.

{{<content-end >}}
