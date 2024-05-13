---
source: "blog"
title: "OPENGIS.ch blog: QGIS DXF Export enhancements"
image: "qgis-dxf-export-enhancements."
date: "2024-05-09"
link: "https://www.opengis.ch/2024/05/13/qgis-dxf-export-enhancements/"
draft: "true"
showcase: "planet"
---

<p>At OPENGIS.CH, we&#8217;ve been working lately on improving the <strong>DXF Export</strong> QGIS functionality for the upcoming release 3.38. In the meantime, we&#8217;ve also added nice UX enhancements for making it easier and much more powerful to use!</p>



<p>Let&#8217;s see a short review.</p>



<h3 class="wp-block-heading">DXF Export app dialog and processing algorithm harmonized</h3>



<p>You can use either the <a href="https://docs.qgis.org/latest/en/docs/user_manual/managing_data_source/create_layers.html#creating-new-dxf-files" rel="noreferrer noopener" target="_blank">app dialog</a> or the <a href="https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/vectorgeneral.html#export-layers-to-dxf" rel="noreferrer noopener" target="_blank">processing algorithm</a>, both of them offer you equivalent functionality. They are now completely harmonized!</p>



<h3 class="wp-block-heading">Export settings can now be exported to an XML file</h3>



<p>You can now have multiple settings per project available in XML, making it possible to reuse them in your workflows or share them with colleagues.</p>



<figure class="wp-block-video wp-block-embed is-type-video is-provider-videopress"><div class="wp-block-embed__wrapper">

</div><figcaption>Load DXF settings from XML.</figcaption></figure>



<h3 class="wp-block-heading">All settings are now well remembered between dialog sessions</h3>



<p>QGIS users told us there were some dialog options that were not remembered between QGIS sessions and had to be reconfigured each time. That&#8217;s no longer the case, making it easier to reuse previous choices.</p>



<h3 class="wp-block-heading">&#8220;Output layer attribute&#8221; column is now always visible in the DXF Export layer tree</h3>



<p>We&#8217;ve made sure that you won&#8217;t miss it anymore.</p>



<figure class="wp-block-image size-full"><img alt="DXF Export, output layer attribute" class="wp-image-14294" height="750" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/04/output_layer_attribute.png?resize=732%2C750&#038;ssl=1" width="732" /></figure>



<h3 class="wp-block-heading">Possibility to export only the current map selection</h3>



<p>Filter features to be exported via layer selection, and even combine this filter with the existing <em>map extent</em> one.</p>



<figure class="wp-block-image size-full is-resized"><img alt="DXF Export algorithm, use only selected features" class="wp-image-14296" height="602" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/04/use_only_selected_features_alg.png?resize=750%2C602&#038;ssl=1" style="width: 840px; height: auto;" width="750" /></figure>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14297" height="750" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/04/use_only_selected_features_app.png?resize=732%2C750&#038;ssl=1" width="732" /></figure>



<h3 class="wp-block-heading">Empty layers are no longer exported to DXF</h3>



<p>When applying spatial filters like feature selection and map extent, you might end up with empty layers to be exported. Well, those won&#8217;t be exported anymore, producing cleaner DXF output files for you.</p>



<h3 class="wp-block-heading">Possibility to override the export name of individual layers</h3>



<p>It&#8217;s often the case where your layer names are not clean and tidy to be displayed. From now on, you can easily specify how your output DXF layers should be named, without altering your original project layers.</p>



<figure class="wp-block-video wp-block-embed is-type-video is-provider-videopress"><div class="wp-block-embed__wrapper">

</div><figcaption>Override output layer names for DXF export.</figcaption></figure>



<p>We&#8217;ve also fixed some minor UX bugs and annoyances that were present when exporting layers to DXF format, so that we can enjoy using it. Happy DXF exporting!</p>



<p>We would like to thank the Swiss QGIS user group for giving us the possibility to improve the important DXF part of QGIS <img alt="🚀" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f680.png" style="height: 1em;" /><img alt="🚀" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f680.png" style="height: 1em;" /><img alt="🚀" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f680.png" style="height: 1em;" /></p>
