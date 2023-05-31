---
source: "blog"
title: "North Road: SLYR Update — June 2023"
image: "slyr-update-june-2023."
date: "2023-05-30"
link: "https://north-road.com/2023/05/31/slyr-update-june-2023/"
draft: "true"
showcase: "planet"
---

<div>Welcome back, SLYR enthusiasts! We&#8217;re thrilled to share the latest updates and enhancements for our <a href="https://north-road.com/slyr/">SLYR ESRI to QGIS Compatibility Suite</a> that will dramatically streamline the use of ESRI documents within QGIS (and vice versa!). Our team has been hard at work, expanding the capabilities of SLYR to ensure seamless compatibility between the latest QGIS and ArcGIS releases. We&#8217;ve also got some exciting news for users of the Community Edition of SLYR! Let&#8217;s dive right in and explore the exciting new features that have been added to SLYR since our <a href="https://north-road.com/2022/11/04/slyr-update-november-2022/">previous update</a>&#8230;</div>
<div>
<h2>Converting Raster Layers in Geodatabases</h2>
<p>We&#8217;re pleased to announce that SLYR now offers support for converting raster layers within Geodatabases. With this update, users can effortlessly migrate their raster data from ESRI&#8217;s Geodatabases to QGIS, enabling more efficient data management and analysis.</p>
<p>This enhancement is only possible thanks to <a href="https://gdal.org/drivers/raster/openfilegdb.html">work in the fantastic GDAL library</a> which underpins QGIS&#8217; raster data support. Please ensure that you have the latest version of QGIS (3.30.3 or 3.28.7 at a minimum) to make the most of this feature.</p>
</div>
<h2>Annotation and Graphic Layer Improvements</h2>
<h3>Text Annotations along Curves</h3>
<p>For those working with curved annotations, we&#8217;ve got you covered! SLYR now supports the conversion of text annotations along curves in QGIS. With this enhancement, you&#8217;ll get accurate conversion of any curved text and text-along-line annotations from MXD and APRX documents. This has been a long-requested feature which we can now introduce thanks to enhancements coming in QGIS 3.32.</p>
<h3>ArcGIS Pro Graphics Layer Support</h3>
<p>SLYR now supports the conversion of ArcGIS Pro graphics layers, converting all graphic elements to their QGIS &#8220;Annotation Layer&#8221; equivalents. If you&#8217;ve spent hours carefully designing cartographic markup on your maps, you can be sure that SLYR will allow you to re-use this work within QGIS!</p>
<p><img decoding="async" loading="lazy" class="size-full wp-image-212544 aligncenter" src="https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47.png" alt="Curved text graphic conversion" width="802" height="579" srcset="https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47.png 802w, https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47-300x217.png 300w, https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47-768x554.png 768w, https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47-230x166.png 230w, https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47-350x253.png 350w, https://north-road.com/wp-content/uploads/2023/05/Screenshot-from-2023-05-30-11-31-47-480x347.png 480w" sizes="(max-width: 802px) 100vw, 802px" /></p>
<h2>Enhanced Page Layout Support</h2>
<div>
<p>We&#8217;ve further improved the results of converting ArcGIS Pro page layouts to QGIS print layouts, with dozens of refinements to the conversion results. The highlights here include:</p>
<ul>
<li>Support for converting measured grids and graticules to QGIS map grids</li>
<li>Enhanced dynamic text conversions:  Now, when migrating your projects, you can expect a smoother transition for dynamic text ensuring your layouts correctly show generated metadata and text correctly</li>
<li>Support for north arrows, grouped elements, legends and table frames.</li>
</ul>
<p>Rest assured that your carefully crafted map layouts will retain their visual appeal and functionality when transitioning to QGIS!</p>
</div>
<h2>Improved QGIS to ArcGIS Pro Conversions</h2>
<div>
<h3>SVG Marker Exports and Symbology Size</h3>
<p>SLYR has introduced initial support for exporting SVG markers from QGIS to ArcGIS Pro formats. SVG graphics are a component of QGIS&#8217; cartography, and are frequently used to create custom marker symbols. Unfortunately, ArcGIS Pro doesn&#8217;t have any native support for SVG graphics for marker symbols, instead relying on a one-off conversion from SVG to multiple separate marker graphics whenever an SVG is imported into ArcGIS Pro. Accordingly, we&#8217;ve implemented a similar logic in SLYR in order to convert SVG graphics to ArcGIS Pro marker graphics transparently whenever QGIS symbology is exported to ArcGIS. This enhancement allows for a seamless transfer of symbology from QGIS, ensuring that your converted maps retain their visual integrity.</p>
<p>Furthermore, the update includes support for exporting QGIS symbology sizes based on &#8220;map unit&#8221; measurements to ArcGIS Pro, resulting in ArcGIS Pro symbology which more accurately matches the original QGIS versions.</p>
<h3>Rule-Based Renderer Conversion</h3>
<p>The &#8220;Rule Based Renderer&#8221; is QGIS&#8217; ultimate powerhouse for advanced layer styling. It&#8217;s extremely flexible, thanks to its support for nested rules and filtering using QGIS expressions. However, this flexibility comes with a cost &#8212; there&#8217;s just no way to reproduce the same results within ArcGIS Pro&#8217;s symbology options! Newer SLYR releases will now attempt to work around this by implementing basic conversion of QGIS rule-based renderers to ArcGIS Pro layers with &#8220;display filters&#8221; attached. This allows us to convert some basic rule-based configuration to ArcGIS Pro formats.</p>
<p>There&#8217;s some limitations to be aware of:</p>
<ol>
<li>Only &#8220;flat&#8221; rule structures can be converted. It&#8217;s not possible to convert a nested rule structure into something representable by ArcGIS Pro.</li>
<li>While the QGIS expression language is very rich and offers hundreds of functions for use in expressions, only basic QGIS filter expressions can be converted to ArcGIS Pro rules.</li>
</ol>
<div>
<h3>Improved Conversion of Raster and Mesh Layers</h3>
<p>Based on user feedback, we&#8217;ve made significant improvements to the conversion of QGIS rasters and mesh layers to ArcGIS Pro formats. Expect enhanced accuracy when migrating these types of data, ensuring a closer match between your QGIS projects and their ArcGIS Pro equivalents.</p>
</div>
</div>
<h2>New tools</h2>
<p>The latest SLYR release introduces some brand new tools for automating your conversion workflows:</p>
<div>
<h3>Convert LYR/LYRX Files Directly to SLD</h3>
<p>To facilitate interoperability, SLYR has introduced algorithms that directly convert ESRI LYR or LYRX files to the &#8220;SLD&#8221; format (Styled Layer Descriptor). This feature simplifies the process of sharing and utilizing symbology between different GIS software, allowing for direct conversion of ESRI symbology for use in Geoserver or Mapserver.</p>
</div>
<div>
<h3>Convert File Geodatabases to Geopackage</h3>
<p>We&#8217;re thrilled to introduce a powerful new tool in SLYR that enables a comprehensive conversion of a File Geodatabase to the Geopackage format. With this feature, you can seamlessly migrate your data from ESRI&#8217;s File Geodatabase format to the versatile and widely supported GeoPackage format. As well as the raw data conversion, this tool also ensures the conversion of field domains and other advanced Geodatabase functionality to their GeoPackage equivalent, preserving valuable metadata and maintaining data integrity throughout the transition. (Please note that this tool requires QGIS version 3.28 or later.)</p>
</div>
<p>&nbsp;</p>
<p>All these exciting additions to SLYR are available today to SLYR license holders. If you&#8217;re after one-click, accurate conversion of projects from ESRI to QGIS, <a href="https://north-road.com/contact/">contact us</a> to discuss your licensing needs.</p>
<p>As described on our <a href="https://north-road.com/slyr/#pledge">SLYR page</a>, we also provide some of the conversion tools for free use via the SLYR &#8220;Community Edition&#8221;. We&#8217;re proud to announce that we&#8217;ve just hit the next milestone in the Community Edition funding, and will now be releasing all of SLYR&#8217;s support for raster LYR files to the community edition! This complements the existing support for vector LYR files and ESRI style files available in the community edition. For more details on the differences between the licensed and community editions, see our <a href="https://north-road.com/slyr/#features">product comparison</a>.</p>
<div data-animation="no-animation" data-icons-animation="no-animation" data-overlay="" data-change-size="" data-button-size="0.7" style="font-size:0.7em!important;display:none;" class="supsystic-social-sharing supsystic-social-sharing-package-flat supsystic-social-sharing-hide-on-homepage supsystic-social-sharing-spacing supsystic-social-sharing-content supsystic-social-sharing-content-align-left" data-text=""><a data-networks="[]" class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter twitter" target="_blank" title="Twitter" href="https://twitter.com/share?url=https%3A%2F%2Fnorth-road.com%2F2023%2F05%2F31%2Fslyr-update-june-2023%2F&text=SLYR+Update+%E2%80%94+June+2023" data-main-href="https://twitter.com/share?url={url}&text={title}" data-nid="2" data-name="" data-pid="1" data-post-id="212540" data-url="https://north-road.com/wp-admin/admin-ajax.php" rel="nofollow" data-mailto=""><i class="fa-ssbs fa-ssbs-fw fa-ssbs-twitter"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a data-networks="[]" class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter linkedin" target="_blank" title="Linkedin" href="https://www.linkedin.com/shareArticle?mini=true&title=SLYR+Update+%E2%80%94+June+2023&url=https%3A%2F%2Fnorth-road.com%2F2023%2F05%2F31%2Fslyr-update-june-2023%2F" data-main-href="https://www.linkedin.com/shareArticle?mini=true&title={title}&url={url}" data-nid="13" data-name="" data-pid="1" data-post-id="212540" data-url="https://north-road.com/wp-admin/admin-ajax.php" rel="nofollow" data-mailto=""><i class="fa-ssbs fa-ssbs-fw fa-ssbs-linkedin"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a><a data-networks="[]" class="social-sharing-button sharer-flat sharer-flat-1 counter-standard without-counter facebook" target="_blank" title="Facebook" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fnorth-road.com%2F2023%2F05%2F31%2Fslyr-update-june-2023%2F" data-main-href="http://www.facebook.com/sharer.php?u={url}" data-nid="1" data-name="" data-pid="1" data-post-id="212540" data-url="https://north-road.com/wp-admin/admin-ajax.php" rel="nofollow" data-mailto=""><i class="fa-ssbs fa-ssbs-fw fa-ssbs-facebook"></i><div class="counter-wrap standard"><span class="counter">0</span></div></a></div>
