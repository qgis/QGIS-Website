---
source: "blog"
title: "Markus Neteler: Translating Open Source Software with Weblate: A GRASS GIS Case Study"
image: "translating-with-weblate."
date: "2023-11-14"
link: "https://neteler.org/blog/translating-with-weblate/"
draft: "true"
showcase: "planet"
---

<p>Open source software projects thrive on the contributions of the community, not only for the code, but also for making the software accessible to a global audience. One of the critical aspects of this accessibility is the localization or translation of the software&#8217;s messages and interfaces. In this context, Weblate (<a href="https://weblate.org/">https://weblate.org/</a>) has proven to be a powerful tool for managing these translations, especially for projects such as GRASS GIS, which is part of <a href="https://www.osgeo.org/">OSGeo</a> (Open Source Geospatial Foundation).</p>
<p><a href="https://neteler.org/wp-content/uploads/2023/11/weblate_logo.png"><img decoding="async" class="alignleft size-medium wp-image-2268" src="https://neteler.org/wp-content/uploads/2023/11/weblate_logo-300x102.png" alt="Weblate software logo" width="300" height="102" srcset="https://neteler.org/wp-content/uploads/2023/11/weblate_logo-300x102.png 300w, https://neteler.org/wp-content/uploads/2023/11/weblate_logo-150x51.png 150w, https://neteler.org/wp-content/uploads/2023/11/weblate_logo.png 410w" sizes="(max-width: 300px) 100vw, 300px" /></a><a href="https://neteler.org/wp-content/uploads/2023/11/grass_gis_logo_nobg_220_250.png"><img fetchpriority="high" decoding="async" class="alignleft size-full wp-image-2269" src="https://neteler.org/wp-content/uploads/2023/11/grass_gis_logo_nobg_220_250.png" alt="GRASS GIS logo" width="220" height="250" srcset="https://neteler.org/wp-content/uploads/2023/11/grass_gis_logo_nobg_220_250.png 220w, https://neteler.org/wp-content/uploads/2023/11/grass_gis_logo_nobg_220_250-132x150.png 132w" sizes="(max-width: 220px) 100vw, 220px" /></a></p>
<h2>What is Weblate?</h2>
<p><a href="https://weblate.org/">Weblate</a> is an open source translation management system designed to simplify the translation process of software projects. It provides an intuitive web interface that allows translators to work without deep technical knowledge. This ease of use combined with robust integration capabilities makes Weblate a popular choice for open source projects.</p>
<h2>GRASS GIS and Localization</h2>
<p>GRASS GIS (<a href="https://grass.osgeo.org/">https://grass.osgeo.org/</a>), a software suite for managing and analyzing geospatial data, is used worldwide and therefore needs to be available in many languages. The project uses Weblate, hosted by OSGeo, to manage and facilitate its translation work (see <a href="https://weblate.osgeo.org/projects/grass-gis/">OSGeo-Weblate</a> portal).</p>
<h2>Marking messages for translation</h2>
<p>Before translation work can begin, the messages to be translated must be marked for translation in the GRASS GIS source code. This is done with the gettext macro <em>_(&#8220;&#8230;&#8221;)</em>. <a href="https://www.gnu.org/software/gettext/">GNU gettext</a> is a GNU library for the internationalization of software. Here is a simplified overview of the process:</p>
<ol>
<li>Identify the strings to be translated: The developers identify the strings in the source code that need to be translated. These are usually user messages, while debug messages are not marked for translation.</li>
<li>Use the gettext macro: The identified strings are packed into a gettext macro. For example, a string <em>&#8220;Welcome to GRASS GIS&#8221;</em> in the source code would be changed to <em>_(&#8220;Welcome to GRASS GIS&#8221;)</em>. This change indicates that the string should be used for translation.</li>
<li>Extraction and template generation: Tools such as xgettext are used to extract these marked strings from the source code and create a POT (Portable Object Template) file. This file is used as a template for all translations. In the GRASS GIS project the template language is English.</li>
</ol>
<p>There are three template files in the GRASS GIS project: one with the graphical user interface (GUI) messages, one with the library functions (libs) and one with the modules (mods).</p>
<h2>Connecting the software project to Weblate</h2>
<p>While the POT files could be transferred to Weblate manually, we chose the automated option. The OSGeo Weblate instance is directly connected to the GRASS GIS project via git (GitHub) using the <a href="https://docs.weblate.org/en/latest/vcs.html">Weblate version control integration</a>.</p>
<p>How it works in practice:</p>
<ol>
<li>Developer makes a commit to the <a href="https://github.com/OSGeo/grass">GRASS GIS repo on GitHub</a></li>
<li>A GitHub webhook makes a call to <a href="https://weblate.osgeo.org">weblate.osgeo.org</a> – note that it has it&#8217;s own <a href="https://github.com/osgeoweblate/grass/tree/weblate-grass-gis-grasslibs">local git repo</a> for GRASS GIS, as it does for other OSGeo projects, with translations being managed in this Weblate instance. This local git repo is updated when the webhook is fired.</li>
<li>As messages are translated in OSGeo-Weblate, they are eventually pushed to the Weblate Github fork of GRASS GIS (the push frequency is set to 24 hours by default, i.e., new translations are collected over a day), and Weblate then triggers a pull request to the main <a href="https://github.com/OSGeo/grass">GRASS GIS repo on GitHub</a>.</li>
</ol>
<p>For technical background on the OSGeo Weblate installation, see the related <a href="https://wiki.osgeo.org/wiki/SAC:Weblate">OSGeo-SAC Weblate page</a>.</p>
<h2>Translation process in Weblate</h2>
<p>Here is how the typical translation process looks like:</p>
<ul>
<li>Translator registration: Registration (via <a href="https://www.osgeo.org/community/getting-started-osgeo/osgeo_userid/">OSGeo-ID</a>) and login to the <a href="https://weblate.osgeo.org/projects/grass-gis/">Weblate instance</a>.</li>
<li>Language selection: Select the language to be translated. If a language does not exist yet, it can be added with the approval of the project managers.</li>
<li>Translation interface: Weblate provides an easy-to-use web interface where translators can view the original texts and enter their translations. If activated, machine translation can also be used here (DeepL, Google Translate, etc.). The Weblate translation memory helps to quickly translate identical and similar sentences.</li>
</ul>
<div id="attachment_2271" style="width: 635px" class="wp-caption aligncenter"><a href="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo.png"><img decoding="async" aria-describedby="caption-attachment-2271" class="wp-image-2271 size-large" src="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-1024x589.png" alt="GRASS GIS messages in Weblate" width="625" height="359" srcset="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-1024x589.png 1024w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-300x173.png 300w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-150x86.png 150w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-768x442.png 768w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-1536x884.png 1536w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo-624x359.png 624w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo.png 1917w" sizes="(max-width: 625px) 100vw, 625px" /></a><p id="caption-attachment-2271" class="wp-caption-text">GRASS GIS messages in Weblate</p></div>
<ul>
<li>Together we are better: translators can discuss translations, resolve conflicts and suggest improvements. Weblate also offers quality checks to ensure consistency and accuracy. Translations in different languages can be compared in tabular form.</li>
</ul>
<div id="attachment_2272" style="width: 635px" class="wp-caption alignleft"><a href="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison.png"><img decoding="async" aria-describedby="caption-attachment-2272" class="size-large wp-image-2272" src="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-1024x591.png" alt="Message translation comparison in Weblate (GRASS GIS project example)" width="625" height="361" srcset="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-1024x591.png 1024w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-300x173.png 300w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-150x87.png 150w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-768x443.png 768w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-1536x886.png 1536w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison-624x360.png 624w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_osgeo_msg_comparison.png 1916w" sizes="(max-width: 625px) 100vw, 625px" /></a><p id="caption-attachment-2272" class="wp-caption-text">Message translation comparison in Weblate (GRASS GIS project example)</p></div>
<ul>
<li>Integration with source code: Once translations are completed and checked, they are written back into the GRASS GIS source code (see above). Weblate supports automatic synchronization with source code repositories.</li>
<li>Continuous updates: As the source code evolves, new strings can be marked for translation and Weblate is automatically updated to reflect these changes.</li>
</ul>
<div id="attachment_2273" style="width: 635px" class="wp-caption alignleft"><a href="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github.png"><img decoding="async" aria-describedby="caption-attachment-2273" class="size-large wp-image-2273" src="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-1024x590.png" alt="Pull request with new translations opened by Weblate in GRASS GIS Github repository" width="625" height="360" srcset="https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-1024x590.png 1024w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-300x173.png 300w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-150x86.png 150w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-768x442.png 768w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-1536x885.png 1536w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github-624x359.png 624w, https://neteler.org/wp-content/uploads/2023/11/weblate_grass_github.png 1918w" sizes="(max-width: 625px) 100vw, 625px" /></a><p id="caption-attachment-2273" class="wp-caption-text">Pull request with new translations opened by Weblate in GRASS GIS Github repository</p></div>
<h2>Benefits for the GRASS GIS project</h2>
<p>By using Weblate, GRASS GIS benefits from the following <strong>advantages</strong>:</p>
<ul>
<li>Streamlined translation workflow: The process from tagging strings to integrating translations is efficient and manageable.</li>
<li>Community engagement: Weblate&#8217;s ease of use encourages more community members to participate in the translation process.</li>
<li>Quality and Consistency: Weblate ensures high quality translations through integrated quality checks and collaboration tools.</li>
<li>Up-to-date localization: Continuous synchronization with the source code repository ensures that translations are always up-to-date.</li>
</ul>
<h2>Conclusion</h2>
<p>The integration of Weblate into the GRASS GIS development workflow underlines the importance of localization in open source software. By using tools such as gettext for message tagging and Weblate for translation management, GRASS GIS ensures that it remains <a href="https://grass.osgeo.org/download/">accessible and usable for a global community</a>, embodying the true spirit of open source software.</p>
<h2>Thanks</h2>
<p>Thanks to <a href="https://wiki.osgeo.org/wiki/User:Robe">Regina Obe from OSGeo-SAC</a> for her support in setting up and maintaining the OSGeo-Weblate instance and for her explanations of how things work in terms of Weblate/GitHub server communication.</p>
<p>The post <a href="https://neteler.org/blog/translating-with-weblate/">Translating Open Source Software with Weblate: A GRASS GIS Case Study</a> appeared first on <a href="https://neteler.org">Markus Neteler | Geospatial Analysis | Remote sensing | GRASS GIS</a>.</p>
