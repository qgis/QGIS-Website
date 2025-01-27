---
source: "blog"
title: "anitagraser.com: LLM-based spatial analysis assistants for QGIS"
image: "llm-based-spatial-analysis-assistants-for-qgis."
date: "2024-10-06"
link: "https://anitagraser.com/2024/10/06/llm-based-spatial-analysis-assistants-for-qgis/"
draft: "true"
showcase: "planet"
---

<p>After the initial ChatGPT hype in 2023 (when we saw the first LLM-backed QGIS plugins, e.g. <a href="https://plugins.qgis.org/plugins/QChatGPT/">QChatGPT</a> and <a href="https://plugins.qgis.org/plugins/qgpt_agent_release/">QGPT Agent</a>), there has been a notable slump in new development. As far as I can tell, none of the early plugins are actively maintained anymore. They were nice tech demos but with limited utility. </p>



<p>However, in the last month, I saw two new approaches for combining LLMs with QGIS that I want to share in this post: </p>



<h2 class="wp-block-heading">IntelliGeo plugin: generating PyQGIS scripts or graphical models</h2>



<p>At the QGIS User Conference in Bratislava, I had the pleasure to attend the <a href="https://talks.osgeo.org/qgis-uc2024/talk/DNHKHQ/">&#8220;Large Language Models and GIS&#8221; workshop</a> presented by <a href="https://talks.osgeo.org/qgis-uc2024/speaker/UHP88B/">Gustavo Garcia</a> and <a href="https://talks.osgeo.org/qgis-uc2024/speaker/XV3E98/">Zehao Lu</a> from the the University of Twente. There, they presented the <a href="https://github.com/MahdiFarnaghi/intelli_geo/releases/tag/v0.0.1">IntelliGeo Plugin</a> which enables the automatic generation of PyQGIS scripts and graphical models. </p>



<p>The workshop was packed. After we installed all dependencies and the plugin, it was exciting to test the graphical model generation capabilities. During the workshop, we used OpenAI&#8217;s API but the readme also mentions support for Cohere.</p>



<p>I was surprised to learn that even simple graphical models are actually pretty large files. This makes it very challenging to generate and/or modify models because they take up a big part of the LLM&#8217;s context window. Therefore, I expect that the PyQGIS script generation will be easier to achieve. But, of course, model generation would be even more impressive and useful since models are easier to edit for most users than code. </p>



<figure class="wp-block-image size-large"><a href="https://github.com/MahdiFarnaghi/intelli_geo/blob/main/.github/IMAGES/Screenshot%20from%202024-09-19%2014-29-26.png"><img alt="" class="wp-image-9242" height="586" src="https://anitagraser.com/wp-content/uploads/2024/10/image-1.png?w=1024" width="1024" /></a><figcaption class="wp-element-caption">Image source: <a href="https://github.com/MahdiFarnaghi/intelli_geo/blob/main/.github/IMAGES/Screenshot%20from%202024-09-19%2014-29-26.png">https://github.com/MahdiFarnaghi/intelli_geo</a></figcaption></figure>



<h2 class="wp-block-heading">ChatGeoAI: chat with PyQGIS</h2>



<p>ChatGeoAI is an approach presented in <a href="https://doi.org/10.3390/ijgi13100348">Mansourian, A.; Oucheikh, R. (2024). ChatGeoAI: Enabling Geospatial Analysis for Public through Natural Language, with Large Language Models. <em>ISPRS Int. J. Geo-Inf.</em>, <em>13</em>, 348.</a>  </p>



<p>It uses a fine-tuned Llama 2 model in combination with spaCy for entity recognition and WorldKG ontology to write PyQGIS code that can perform a variety of different geospatial analysis tasks on OpenStreetMap data.  </p>



<p>The paper is very interesting, describing the LLM fine-tuning, integration with QGIS, and evaluation of the generated code using different metrics. However, as far as I can tell, the tool is not publicly available and, therefore, cannot be tested. </p>



<figure class="wp-block-image size-large"><a href="https://www.mdpi.com/2220-9964/13/10/348"><img alt="" class="wp-image-9240" height="587" src="https://anitagraser.com/wp-content/uploads/2024/10/image.png?w=1024" width="1024" /></a><figcaption class="wp-element-caption">Image source: <a href="https://www.mdpi.com/2220-9964/13/10/348">https://www.mdpi.com/2220-9964/13/10/348</a></figcaption></figure>



<p>Are you aware of more examples that integrate QGIS with LLMs? Please share them in the comments below. I&#8217;d love to hear about them. </p>
