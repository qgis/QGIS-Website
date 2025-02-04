---
source: "blog"
title: "ItOpen: Building QGIS on Windows 10 with Qt Creator"
image: "building-qgis-on-windows-10-with-qt-creator."
date: "2025-02-03"
link: "https://www.itopen.it/building-qgis-on-windows-10-with-qt-creator/"
draft: "true"
showcase: "planet"
---

<p class="lead clearfix">Just a few additional notes about how to build latest QGIS 3 master on Win 10 64 bits, the base document is: <a href="https://github.com/qgis/QGIS/blob/master/INSTALL">INSTALL</a></p>



<ul class="wp-block-list"><li>follow the instructions in the INSTALL document</li><li>install visual studio code (you&#8217;ll need the &#8220;Visual C++&#8221; compiler tools) fromÂ <a href="http://download.microsoft.com/download/D/2/3/D23F4D0F-BA2D-4600-8725-6CCECEA05196/vs_community_ENU.exe">http://download.microsoft.com/download/D/2/3/D23F4D0F-BA2D-4600-8725-6CCECEA05196/vs_community_ENU.exe</a></li><li>install the Windows 10 SDK (you are looking for debugger tools) from <a href="https://developer.microsoft.com/en-US/windows/downloads/windows-10-sdk">https://developer.microsoft.com/en-US/windows/downloads/windows-10-sdk</a></li><li>install Qt Creator (the IDE only: no Qt sources or pre-built binaries)</li><li>git clone QGIS and create a build dir</li><li>configure Qt Creator kit as in the following pictures</li></ul>



<ul class="wp-block-gallery columns-3 is-cropped wp-block-gallery-1 is-layout-flex wp-block-gallery-is-layout-flex"><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-1926" height="546" src="https://www.itopen.it/wp-content/uploads/2018/12/kists-debugger-800x546.png" width="800" /></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-1927" height="689" src="https://www.itopen.it/wp-content/uploads/2018/12/kists-kit-800x689.png" width="800" /></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-1928" height="545" src="https://www.itopen.it/wp-content/uploads/2018/12/kits-cmake-800x545.png" width="800" /></figure></li><li class="blocks-gallery-item"><figure><img alt="" class="wp-image-1929" height="546" src="https://www.itopen.it/wp-content/uploads/2018/12/kits-qmake-800x546.png" width="800" /></figure></li></ul>



<p>The environent configuration of the kit is:</p>



<pre class="wp-code-highlight prettyprint">&lt;code&gt;PATH=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE\CommonExtensions\Microsoft\TestWindow;C:\Program Files (x86)\MSBuild\14.0\bin\amd64;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\amd64;C:\WINDOWS\Microsoft.NET\Framework64\v4.0.30319;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\VCPackages;C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\IDE;C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools;C:\Program Files (x86)\HTML Help Workshop;C:\Program Files (x86)\Microsoft Visual Studio 14.0\Team Tools\Performance Tools\x64;C:\Program Files (x86)\Microsoft Visual Studio 14.0\Team Tools\Performance Tools;C:\Program Files (x86)\Windows Kits\8.1\bin\x64;C:\Program Files (x86)\Windows Kits\8.1\bin\x86;C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.6.1 Tools\x64\;C:\OSGEO4~1\apps\qt5\bin;C:\OSGEO4~1\apps\Python37;C:\OSGEO4~1\apps\Python37\Scripts;C:\OSGEO4~1\bin;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\system32\WBem;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;C:\Program Files\CMake\bin;c:\cygwin64\bin;C:\OSGeo4W64\apps\Python37\Scripts
PYTHONHOME=C:\OSGEO4~1\apps\Python37
QT_QPA_PLATFORM_PLUGIN_PATH=C:\OSGeo4W64\apps\Qt5\plugins
VCARCH=amd64
VCINSTALLDIR=C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\
VISUALSTUDIOVERSION=14.0
VS110COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 11.0\Common7\Tools\
VS120COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\
VS140COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\
VSINSTALLDIR=C:\Program Files (x86)\Microsoft Visual Studio 14.0\
WINDIR=C:\WINDOWS
WINDOWSLIBPATH=C:\Program Files (x86)\Windows Kits\8.1\References\CommonConfiguration\Neutral
WINDOWSSDKDIR=C:\Program Files (x86)\Windows Kits\8.1\
WINDOWSSDKLIBVERSION=winv6.3\
WINDOWSSDKVERSION=\
WINDOWSSDK_EXECUTABLEPATH_X64=C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.6.1 Tools\x64\
WINDOWSSDK_EXECUTABLEPATH_X86=C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.6.1 Tools\&lt;/code&gt;</pre>



<p>Note: I&#8217;m not really sure if all those variables are necessary, but that worked for me.</p>
