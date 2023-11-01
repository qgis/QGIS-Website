---
source: "blog"
title: "Markus Neteler: GRASS GIS 8.3.0 released"
image: "grass-gis-8-3-0-released."
date: "2023-10-17"
link: "https://courses.neteler.org/grass-gis-8-3-0-released/"
draft: "true"
showcase: "planet"
---

<h3 id="What’s_new_in_a_nutshell" >Section 1. What’s new in a nutshell</h3>
<p>The GRASS GIS 8.3.0 release provides more than <strong>360 changes</strong> compared to the 8.2 branch. This new minor release brings in <strong>many fixes and improvements</strong> in GRASS GIS modules and the graphical user interface (GUI) which now has the <strong>single window layout by default</strong>. Some of the most relevant changes include: support for <strong>parallelization</strong> in three raster modules, new options added to several temporal modules, and substantial clean-up of <code>g.extension</code>, the module that allows the installation of add-ons. The GUI also received a lot of attention with many fixes and items reorganised. We have also adopted the Clang format and indented most of the C code accordingly. A lot of effort was put into cleaning up the C/C++ code to fix almost all compiler warnings.</p>
<p>Translations have been moved from Transifex to <a class="ext" title="Weblate" href="https://weblate.osgeo.org/projects/grass-gis/" target="_blank" rel="noopener">Weblate</a>, which automatically creates pull requests with the translated chunks. We’d like to <strong>thank the translators of all languages</strong> for their long term support!</p>
<p><a class="int" href="https://grass.osgeo.org/images/news/grass83_news_screenshot.png"> <img decoding="async" class="alignright" title="GRASS GIS 8.3" src="https://grass.osgeo.org/images/news/grass83_news_screenshot.png" alt="GRASS GIS 8.3" width="60%" /> </a></p>
<p>Also, docker images have been updated and moved from the mundialis to the OSGeo organization at <a class="ext" title="https://hub.docker.com/r/osgeo/grass-gis/" href="https://hub.docker.com/r/osgeo/grass-gis/" target="_blank" rel="noopener">https://hub.docker.com/r/osgeo/grass-gis/</a>.</p>
<p>We have carried out quite some work in the GitHub Actions: we added support for “pre-commit” in order to reduce unnecessary runs of the automated checks, there were notable improvements in the code checking section and we have activated renovatebot to automatically maintain GitHub Actions.</p>
<p>Last but not least, we have significantly improved the automated release creation to reduce maintainer workload and we have gained nine new contributors! Welcome all!!</p>
<h3 id="Full_list_of_changes_and_contributors" >Section 2. Full list of changes and contributors</h3>
<p>For all 360+ changes, see our detailed announcement with the full list of features and bugs fixed at <a class="ext" title="GitHub / Releases / 8.3.0" href="https://github.com/OSGeo/grass/releases/tag/8.3.0" target="_blank" rel="noopener">GitHub / Releases / 8.3.0</a>.</p>
<p>Thank you all contributors!!</p>
<h3 id="Download_and_test!" >Section 3. Download and test!</h3>
<h4 id="Binaries/Installers_download" >1) Binaries/Installers download</h4>
<ul>
<li>Windows
<ul>
<li><a class="int" href="https://grass.osgeo.org/grass83/binary/mswindows/native/WinGRASS-8.3.0-1-Setup.exe">64bit standalone installer</a></li>
</ul>
</li>
<li>macOS
<ul>
<li><a class="ext broken_link" title="Official Application Bundle" href="https://cmbarton.github.io/grass-mac/_pages/download-grass/" target="_blank" rel="noopener">Official Application Bundle</a></li>
</ul>
</li>
<li>Linux
<ul>
<li><a class="ext" title="Debian" href="https://tracker.debian.org/pkg/grass" target="_blank" rel="noopener">Debian</a></li>
<li><a class="ext" title="Ubuntu" href="https://launchpad.net/~ubuntugis/+archive/ubuntu/ubuntugis-unstable" target="_blank" rel="noopener">Ubuntu</a></li>
<li><a class="ext" title="Fedora/Centos/EPEL" href="https://src.fedoraproject.org/rpms/grass" target="_blank" rel="noopener">Fedora/Centos/EPEL</a></li>
<li><a class="ext" title="Gentoo" href="https://packages.gentoo.org/packages/sci-geosciences/grass" target="_blank" rel="noopener">Gentoo</a></li>
</ul>
</li>
</ul>
<p>Further binary packages for other platforms and distributions will follow shortly, please check at <a class="int" href="https://grass.osgeo.org/download/index.html">software downloads</a>.</p>
<h4 id="Source_code_download" >2) Source code download</h4>
<ul>
<li><a class="int" href="https://grass.osgeo.org/grass83/source/">https://grass.osgeo.org/grass83/source/</a></li>
<li><a class="int" href="https://grass.osgeo.org/grass83/source/grass-8.3.0.tar.gz">https://grass.osgeo.org/grass83/source/grass-8.3.0.tar.gz</a></li>
<li><a class="ext" title="From GitHub" href="https://github.com/OSGeo/grass/releases/tag/8.3.0" target="_blank" rel="noopener">From GitHub</a></li>
</ul>
<p>First time users may explore the <a class="int" href="https://grass.osgeo.org/learn/"><strong>first steps tutorial</strong></a> after installation.</p>
<p><strong>About GRASS GIS</strong></p>
<p>The Geographic Resources Analysis Support System (<a class="int" href="https://grass.osgeo.org/">https://grass.osgeo.org/</a>), commonly referred to as GRASS GIS, is an Open Source Geographic Information System providing powerful raster, vector and <a class="int" href="https://grass.osgeo.org/learn/overview/">geospatial processing capabilities</a>. It can be used either as a stand-alone application, as backend for other software packages such as QGIS and R, or in the cloud. It is distributed freely under the terms of the GNU General Public License (GPL). GRASS GIS is a founding member of the Open Source Geospatial Foundation (OSGeo).</p>
<p><em>The GRASS Dev Team</em></p>
<p>The post <a href="https://courses.neteler.org/grass-gis-8-3-0-released/">GRASS GIS 8.3.0 released</a> appeared first on <a href="https://courses.neteler.org">GFOSS Blog | GRASS GIS and OSGeo News</a>.</p>
