---
source: "blog"
title: "anitagraser.com: PyQGIS Jupyter notebooks on Windows using Conda"
image: "pyqgis-jupyter-notebooks-on-windows-using-conda."
date: "2023-01-21"
link: "https://anitagraser.com/2023/01/21/pyqgis-jupyter-notebooks-on-windows-using-conda/"
draft: "true"
showcase: "planet"
---

<p>The <a href="https://anaconda.org/conda-forge/qgis">QGIS conda packages</a> have been around for a while. One of their use cases, for example, is to <a href="https://gisunchained.wordpress.com/2019/05/29/using-qgis-from-conda/">allow Linux users to easily install multiple versions of QGIS</a>.</p>



<p>Similarly, we&#8217;ve seen posts on using <a href="https://lerryws.xyz/posts/PyQGIS-in-Jupyter-Notebook">PyQGIS in Jupyter notebooks</a>. However, I find the setup with *.bat files rather tricky.</p>



<p>This post presents a way to set up a conda environment with QGIS that is ready to be used in Jupyter notebooks. </p>



<p>The first steps are to create a new environment and install QGIS. I use mamba for the installation step because it is faster than conda but you can use conda as well:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: powershell; title: ; notranslate">
(base) PS C:\Users\anita&gt; conda create -n qgis python=3.9
(base) PS C:\Users\anita&gt; conda activate qgis
(qgis) PS C:\Users\anita&gt; mamba install -c conda-forge qgis=3.28.2 
(qgis) PS C:\Users\anita&gt; qgis
</pre></div>


<p>If we now try to import the qgis module in Python, we get an error:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: powershell; title: ; notranslate">
(qgis) PS C:\Users\anita&gt; python
Python 3.9.15 | packaged by conda-forge | (main, Nov 22 2022, 08:41:22) &#91;MSC v.1929 64 bit (AMD64)] on win32
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; import qgis
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'qgis'
</pre></div>


<p>To fix this error, we need to get the paths from the Python console inside QGIS:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: python; title: ; notranslate">
import sys
sys.path
&#91;'H:/miniconda3/envs/qgis/Library/./python', 'C:/Users/anita/AppData/Roaming/QGIS/QGIS3\\profiles\\default/python', ... ]
</pre></div>


<figure class="wp-block-image size-large"><img data-attachment-id="8345" data-permalink="https://anitagraser.com/2023/01/21/pyqgis-jupyter-notebooks-on-windows-using-conda/pyqgis-path/" data-orig-file="https://underdark.files.wordpress.com/2023/01/pyqgis-path.png" data-orig-size="708,283" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="pyqgis-path" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/01/pyqgis-path.png?w=300" data-large-file="https://underdark.files.wordpress.com/2023/01/pyqgis-path.png?w=545" src="https://underdark.files.wordpress.com/2023/01/pyqgis-path.png?w=708" alt="" class="wp-image-8345" srcset="https://underdark.files.wordpress.com/2023/01/pyqgis-path.png 708w, https://underdark.files.wordpress.com/2023/01/pyqgis-path.png?w=150 150w, https://underdark.files.wordpress.com/2023/01/pyqgis-path.png?w=300 300w" sizes="(max-width: 708px) 100vw, 708px" /></figure>



<p>This list of paths can be configured as the defaults for our qgis environment using conda develop: </p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: powershell; title: ; notranslate">
(qgis) PS C:\Users\anita&gt; conda activate base
(base) PS C:\Users\anita&gt; mamba install conda-build -c conda-forge
(base) PS C:\Users\anita&gt; conda develop -n qgis &#91;list of paths from qgis python console] 
</pre></div>


<p>With this setup, the import should now work without errors:</p>


<div class="wp-block-syntaxhighlighter-code "><pre class="brush: powershell; title: ; notranslate">
(base) PS C:\Users\anita&gt; conda activate qgis
(qgis) PS C:\Users\anita&gt; python
Python 3.9.15 | packaged by conda-forge | (main, Nov 22 2022, 08:41:22) &#91;MSC v.1929 64 bit (AMD64)] on win32
Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
&gt;&gt;&gt; import qgis
</pre></div>


<p>The example Jupyter notebook covers running a QGIS Processing algorithm and visualizing the results in the notebook using GeoPandas:</p>



<figure class="wp-block-image size-large"><a href="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png"><img data-attachment-id="8331" data-permalink="https://anitagraser.com/2023/01/21/pyqgis-jupyter-notebooks-on-windows-using-conda/vscode-pyqgis/" data-orig-file="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png" data-orig-size="969,1440" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="vscode-pyqgis" data-image-description="" data-image-caption="" data-medium-file="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=202" data-large-file="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=545" src="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=689" alt="" class="wp-image-8331" srcset="https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=689 689w, https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=101 101w, https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=202 202w, https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png?w=768 768w, https://underdark.files.wordpress.com/2023/01/vscode-pyqgis.png 969w" sizes="(max-width: 689px) 100vw, 689px" /></a></figure>



<p>Head over to Github to find the full instructions: <a href="https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/hello-world.ipynb">https://github.com/anitagraser/QGIS-resources/blob/master/qgis3/notebooks/hello-world.ipynb</a></p>
