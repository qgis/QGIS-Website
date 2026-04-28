---
Reviewed: 4 June 2024
Reviewer: Tim Sutton
draft: false
selected_language: en
sidebar: true
subtitle: ''
title: QGIS ресурси
type: page

---
{{<content-start >}}
# Resources
{{< rich-box-start icon="🖖" layoutClass="tips">}} {{< rich-content-start themeClass="coloring-1" >}}
#### Проблеми с инсталацията?
If you are looking for information on installing QGIS on all available platforms, we have prepared a comprehensive guide for you:

[Ръководство за монтаж]({{< ref "/resources/installation-guide/index.md" >}})

{{< rich-content-end >}} {{< rich-box-end >}}
## Документация
QGIS has a lot of documentation. All of the core documentation (user manual, developer handbooks etc.) is available in English. Some documents such as the user guide are also available in other languages.

You will find documentation for every QGIS Long Term Release (LTR) on the respective documentation website.

[Включете се]({{< ref "/community/involve" >}}) и ни помогнете да напишем по-добра документация.

{{<language-select >}}

<!--{{< tabs tab1="QGIS |ltrversion|" tab2="QGIS |version|" tab3="QGIS testing (>|version|)" tab4="Archived releases" tab5="Data protection">}} -->

{{<tabs tab1="QGIS |алтернативна версия|" tab2="QGIS тестване (>|ltrversion|)" tab3="Архивирани издания" tab4="Защита на данните" >}}

{{< tab-content-start tab="1" >}} **For users (QGIS {{< param "ltrversion" >}}):**

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/user_manual" layoutClass="inline-block link-with-language" listTitle="Ръководство за монтаж — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/training_manual" layoutClass="inline-block link-with-language" listTitle="Ръководство за QGIS обучение — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/gentle_gis_introduction" layoutClass="inline-block link-with-language" listTitle="Кратко въведение в ГИС — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/server_manual" layoutClass="inline-block link-with-language" listTitle="Ръководство за сървъра — <lang>" >}}

**За автори на документация (QGIS {{< параметър "LTR Версия" >}}):**

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/documentation_guidelines" layoutClass="inline-block link-with-language" listTitle="Указания за документация — <lang>" >}}

**За разработчици (QGIS {{< параметър "LTR версия" >}}):**

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/<lang>/docs/pyqgis_developer_cookbook" layoutClass="inline-block link-with-language" listTitle="PyQGIS готварска книга (за плъгини и скриптове) — <lang>" >}}

{{<rich-list listLink="https://qgis.org/pyqgis/|ltrversion|/" layoutClass="inline-block" listTitle="PyQGIS - Документация на QGIS Python API" >}}

{{<rich-list listLink="https://qgis.org/api/|ltrversion|/" layoutClass="inline-block" listTitle="Документация за C++ API" >}}

{{<rich-list listLink="https://github.com/qgis/QGIS/blob/release-|ltrversion|/INSTALL.md" layoutClass="inline-block" listTitle="Изграждане на QGIS от изходния код" >}}

**За изтегляне (QGIS {{< параметър "LTR версия" >}}):**

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/pdf" layoutClass="inline-block" listTitle="PDF файл с ръководствата" >}}

{{<rich-list listLink="https://docs.qgis.org/|ltrversion|/zip" layoutClass="inline-block" listTitle="HTML zip файл с ръководствата" >}}

{{<tab-content-end >}}

<!--{{< tab-content-start tab="2" >}}
**For users (QGIS {{< param "version" >}}):**

{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/user_manual"  layoutClass="inline-block link-with-language" listTitle="Desktop User Guide — <lang>" >}}
 
{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/training_manual"  layoutClass="inline-block link-with-language" listTitle="QGIS Training manual — <lang>">}}

{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/gentle_gis_introduction"  layoutClass="inline-block link-with-language" listTitle="Gentle Intro to GIS — <lang>" >}}

{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/server_manual"  layoutClass="inline-block link-with-language" listTitle="Ръководство за сървъра — <lang>" >}}


**За автори на документация (QGIS {{< param "версия" >}}):**

{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/documentation_guidelines"  layoutClass="inline-block link-with-language" listTitle="Указания за документация — <lang>">}}


**For developers (QGIS {{< param "версия" >}}):**

{{< rich-list listLink="https://docs.qgis.org/|version|/<lang>/docs/pyqgis_developer_cookbook"  layoutClass="inline-block link-with-language" listTitle="PyQGIS готварска книга (за плъгини и скриптове) — <lang>">}}

{{< rich-list listLink="https://qgis.org/pyqgis/|version|/"  layoutClass="inline-block" listTitle="PyQGIS - QGIS Python Api documentation" >}}


{{< rich-list listLink="https://qgis.org/api/|version|/"  layoutClass="inline-block" listTitle="C++ API документация" >}}

{{< rich-list listLink="https://github.com/qgis/QGIS/blob/release-|version|/INSTALL.md"  layoutClass="inline-block" listTitle="Изграждане на QGIS от изходния код" >}}

**За изтегляне (QGIS {{< param "версия" >}}):**

{{< rich-list listLink="https://docs.qgis.org/|version|/pdf"  layoutClass="inline-block" listTitle="PDF файл с ръководствата" >}}

{{< rich-list listLink="https://docs.qgis.org/|version|/zip"  layoutClass="inline-block" listTitle="HTML zip файл с ръководствата" >}}

{{< tab-content-end >}} -->

{{<tab-content-start tab="2" >}}

We are still updating (not translating yet) the documentation for releases newer than QGIS {{< param "ltrversion" >}}. We call this version 'QGIS Testing' and the documentation can be found here:

**За потребители (тестване на QGIS):**

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/user_manual" layoutClass="inline-block link-with-language" listTitle="Ръководство за потребителя на настолни компютри" >}}

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/training_manual" layoutClass="inline-block link-with-language" listTitle="QGIS Ръководство за обучение" >}}

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/gentle_gis_introduction" layoutClass="inline-block link-with-language" listTitle="Кратко въведение в ГИС" >}}

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/server_manual" layoutClass="inline-block link-with-language" listTitle="Ръководство/Наръчник за сървъра" >}}

**За автори на документация (тестване на QGIS):**

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/documentation_guidelines" layoutClass="inline-block link-with-language" listTitle="Документация - указания" >}}

**За разработчици (тестване на QGIS):**

{{<rich-list listLink="https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook" layoutClass="inline-block link-with-language" listTitle="PyQGIS cookbook (за добавки и скриптове)" >}}

{{<rich-list listLink="https://qgis.org/api/" layoutClass="inline-block" listTitle="Документация за C++ API" >}}

{{<rich-list listLink="https://qgis.org/pyqgis/" layoutClass="inline-block" listTitle="PyQGIS - Документация на QGIS Python API" >}}

{{<rich-list listLink="https://github.com/qgis/QGIS/blob/master/INSTALL.md" layoutClass="inline-block" listTitle="Изграждане на QGIS от изходния код" >}}

**За изтегляне (тестване на QGIS):**

{{<rich-list listLink="https://docs.qgis.org/testing/pdf" layoutClass="inline-block" listTitle="PDF файл с ръководствата" >}}

{{<rich-list listLink="https://docs.qgis.org/testing/zip" layoutClass="inline-block" listTitle="HTML zip файл с ръководствата" >}}

{{<tab-content-end >}}

{{<tab-content-start tab="3" >}}

{{<rich-list listLink="https://docs.qgis.org/3.40/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.40 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.34/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.34 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.28/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.28 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.22/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.22 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.16/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.16 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.10/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.10 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/3.4/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 3.4 — <lang>" >}}

{{<rich-list listLink="https://docs.qgis.org/2.18/<lang>" layoutClass="inline-block link-with-language" listTitle="Документация за QGIS 2.18 — <lang>" >}}

{{<tab-content-end >}}

{{<tab-content-start tab="4" >}}

In line with GDPR and related data protection regulations, we provide the following documentation:

{{<rich-list listLink="https://docs.qgis.org/latest/en/docs/user_manual/appendices/qgis_desktop_network_connections.html" layoutClass="inline-block" listTitle="Мрежови връзки на приложението QGIS" >}}

{{<tab-content-end >}}

{{< rich-box-start >}} {{< rich-content-start themeClass="coloring-6">}}
## Поддръжка
Общността на QGIS предлага множество отлични уебсайтове с форуми за поддръжка.

{{<button class="is-primary6" link="resources/support" text="Преглед на опциите за поддръжка" >}}

{{< rich-content-end >}} {{< rich-box-end >}}

{{<content-end >}}
