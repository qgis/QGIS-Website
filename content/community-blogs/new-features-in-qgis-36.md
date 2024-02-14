---
source: "blog"
title: "Lutra Consulting: New point clouds and mesh features in QGIS 3.36"
image: "new-features-in-qgis-36."
date: "2024-02-05"
link: "https://lutraconsulting.co.uk/blog/2024/02/05/new-features-in-qgis-36/"
draft: "true"
showcase: "planet"
---

<p>QGIS 3.36 is round the corner and as usual, there will be several new exciting features with the new release. Below is the list of features our team has added to the new release. This was made possible by generous funding from clients.</p>

<h1 id="render-point-clouds-as-a-surface-in-2d-map-views">Render point clouds as a surface in 2D map views</h1>

<p>Point clouds are rendered as individual points by default. Depending on the zoom level and density of the points, you might not be able to get a full picture of the map.</p>

<p>Rendering points as surface enables you to have a better understanding of the data before trying to do any analysis or processing. This has been possible in 3D map views for a couple of QGIS releases, now we have added the functionality also in 2D map views.</p>

<p>The feature generates a surface using triangulation on-the-fly from the points using the same symbology. Below you can see the difference between a point cloud rendered as individual points and rendered as a surface:</p>

<center>
  <p><img title="Point clouds as surface" src="https://lutraconsulting.co.uk/img/posts/pc_as_surface_2d.gif" alt="Point clouds as surface" /></p>
  <sub>Point clouds as individual points vs. as a TIN surface</sub>
</center>

<p>The good news is that rendering as a surface also works well with global map shading, allowing users to get a nice hillshade:</p>

<center>
  <p><img title="Point clouds as surface with hillshade" src="https://lutraconsulting.co.uk/img/posts/pc_as_surface_2d_hillshade.png" alt="Point clouds as surface with hillshade with hillshade" /></p>
  <sub>Point clouds as surface with hillshade</sub>
</center>

<p>To enable this feature, you need to check the option for <strong>Render as a Surface (Triangulate)</strong> under the <strong>Layer Styling</strong> panel.</p>

<center>
  <p><img title="Setting to display point clouds as surface" src="https://lutraconsulting.co.uk/img/posts/pc_as_surface_style.png" alt="Point clouds styling panel" /></p>
  <sub>Settings to display point clouds as surface</sub>
</center>

<p><strong>Pro-tip</strong>: if the on-the-fly rendering as a surface takes too long to render, try increasing the Maximum error: for example 0.6 mm instead of the default 0.3 mm.</p>

<h1 id="flexible-styling-of-classes">Flexible styling of classes</h1>

<p>Previously, point cloud data visualisation in QGIS was limited to rendering all points with a uniform size and opacity. This made it difficult to differentiate between different point classes and highlight specific features of interest. To address this issue, we have introduced a new feature that allows users to customise the point size and opacity for each point cloud data class. This provides a flexible way for visualising point cloud data, allowing users to highlight specific point classes, e.g. by increasing the point size.</p>

<center>
  <p><img title="Assigning size and opacity to each point cloud class" src="https://lutraconsulting.co.uk/img/posts/pc_size_opacity_panel.png" alt="Assigning size and opacity to each point cloud class" /></p>
  <sub>Assigning size and opacity to each point cloud class</sub>
</center>

<center>
  <p><img title="Point clouds with different sizes and opacity levels" src="https://lutraconsulting.co.uk/img/posts/pc_size_opacity.png" alt="Point clouds with different sizes and opacity levels" /></p>
  <sub>Point clouds with different sizes and opacity levels</sub>
</center>

<h1 id="set-3d-map-view-extent-in-2d-map">Set 3D map view extent in 2D map</h1>

<p>Effectively navigating and visualising large-scale 3D datasets can be challenging on PCs with limited resources. To address this issue, we introduced a new feature that allows users to interactively limit the 3D scene, enabling them to focus on specific areas of interest. This new feature, conveniently accessible from the toolbar, eliminates the need for tedious manual entry of coordinates for bounding boxes. Instead, users can simply drag and draw a box around the desired area, instantly restricting the 3D scene to that specific extent. This interactive approach significantly enhances the user experience and streamlines the process of exploring and analysing 3D data:</p>

<center>
  <p><img title="Interactive selection of 3D map scene from 2D map" src="https://lutraconsulting.co.uk/img/posts/3d_map_bbox_interactive.png" alt="Interactive selection of 3D map scene from 2D map" /></p>
  <sub>Interactive selection of 3D map scene from 2D map</sub>
</center>

<h1 id="python-api-for-3d-views">Python API for 3D views</h1>

<p>Creating and viewing 3D maps in QGIS with the correct camera location and angle, scene tilt, light, and other parameters can be a time-consuming and error-prone process. This is because it requires users to manually adjust these settings, often through trial and error. However, with the introduction of the new 3D map view API in QGIS, Python plugins can now automate this process, making it much easier, consistent and more efficient to create high-quality 3D maps that are visually appealing and informative.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># List all open 3D map canvases
</span><span class="n">iface</span><span class="p">.</span><span class="n">mapCanvases3D</span><span class="p">()</span>
<span class="c1"># [&lt;qgis._3d.Qgs3DMapCanvas object at 0x7f23491b5e10&gt;]
</span><span class="n">canvas</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">mapCanvases3D</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>
</code></pre></div></div>
<p>Now let’s try something more complicated:</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Let's change some settings!
</span><span class="n">ms</span> <span class="o">=</span> <span class="n">canvas</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">()</span>
<span class="n">ms</span><span class="p">.</span><span class="n">setEyeDomeLightingEnabled</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
<span class="n">ms</span><span class="p">.</span><span class="n">setBackgroundColor</span><span class="p">(</span><span class="n">QColor</span><span class="p">(</span><span class="s">'beige'</span><span class="p">))</span>
<span class="n">ms</span><span class="p">.</span><span class="n">setTerrainMapTheme</span><span class="p">(</span><span class="s">'dtm'</span><span class="p">)</span>
<span class="n">ms</span><span class="p">.</span><span class="n">setFieldOfView</span><span class="p">(</span><span class="mi">110</span><span class="p">)</span>

<span class="c1"># Move the camera to look at specific map coordinates in layer's CRS
</span><span class="n">cam</span> <span class="o">=</span> <span class="n">canvas</span><span class="p">.</span><span class="n">cameraController</span><span class="p">()</span>
<span class="n">mapPoint</span> <span class="o">=</span> <span class="n">QgsVector3D</span><span class="p">(</span><span class="o">-</span><span class="mf">498175.92</span><span class="p">,</span> <span class="o">-</span><span class="mf">1205400.58</span><span class="p">,</span> <span class="mi">210</span><span class="p">)</span>
<span class="n">worldPoint</span> <span class="o">=</span> <span class="n">ms</span><span class="p">.</span><span class="n">mapToWorldCoordinates</span><span class="p">(</span><span class="n">mapPoint</span><span class="p">)</span>
<span class="n">cam</span><span class="p">.</span><span class="n">setLookingAtPoint</span><span class="p">(</span><span class="n">worldPoint</span><span class="p">,</span> <span class="mi">60</span><span class="p">,</span> <span class="mi">45</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>

<span class="c1"># Create four new 3D map views
</span><span class="n">c1</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">createNewMapCanvas3D</span><span class="p">(</span><span class="s">'South View'</span><span class="p">)</span>
<span class="n">c2</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">createNewMapCanvas3D</span><span class="p">(</span><span class="s">'West View'</span><span class="p">)</span>
<span class="n">c3</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">createNewMapCanvas3D</span><span class="p">(</span><span class="s">'North View'</span><span class="p">)</span>
<span class="n">c4</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">createNewMapCanvas3D</span><span class="p">(</span><span class="s">'East View'</span><span class="p">)</span>

<span class="c1"># Apply settings to all open 3D map views
</span><span class="k">for</span> <span class="n">canvas</span> <span class="ow">in</span> <span class="n">iface</span><span class="p">.</span><span class="n">mapCanvases3D</span><span class="p">():</span>
	<span class="n">canvas</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">().</span><span class="n">setEyeDomeLightingEnabled</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>

<span class="c1"># Define a camera pose to update the views' cameras
</span><span class="n">pose</span> <span class="o">=</span> <span class="n">QgsCameraPose</span><span class="p">()</span>
<span class="n">pose</span><span class="p">.</span><span class="n">setCenterPoint</span><span class="p">(</span><span class="n">QgsVector3D</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">210</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>  <span class="c1"># This is in 3D world coordinates
</span><span class="n">pose</span><span class="p">.</span><span class="n">setDistanceFromCenterPoint</span><span class="p">(</span><span class="mi">100</span><span class="p">)</span>
<span class="n">pose</span><span class="p">.</span><span class="n">setPitchAngle</span><span class="p">(</span><span class="mi">75</span><span class="p">)</span>  <span class="c1"># Tilt the camera by 75 degrees
</span><span class="n">pose</span><span class="p">.</span><span class="n">setHeadingAngle</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>  <span class="c1"># Looking towards North
</span><span class="n">c1</span><span class="p">.</span><span class="n">cameraController</span><span class="p">().</span><span class="n">setCameraPose</span><span class="p">(</span><span class="n">pose</span><span class="p">)</span>
<span class="n">pose</span><span class="p">.</span><span class="n">setHeadingAngle</span><span class="p">(</span><span class="mi">90</span><span class="p">)</span>  <span class="c1"># Towards East
</span><span class="n">c2</span><span class="p">.</span><span class="n">cameraController</span><span class="p">().</span><span class="n">setCameraPose</span><span class="p">(</span><span class="n">pose</span><span class="p">)</span>
<span class="n">pose</span><span class="p">.</span><span class="n">setHeadingAngle</span><span class="p">(</span><span class="mi">180</span><span class="p">)</span>  <span class="c1"># Towards South
</span><span class="n">c3</span><span class="p">.</span><span class="n">cameraController</span><span class="p">().</span><span class="n">setCameraPose</span><span class="p">(</span><span class="n">pose</span><span class="p">)</span>
<span class="n">pose</span><span class="p">.</span><span class="n">setHeadingAngle</span><span class="p">(</span><span class="mi">270</span><span class="p">)</span>  <span class="c1"># Towards West
</span><span class="n">c4</span><span class="p">.</span><span class="n">cameraController</span><span class="p">().</span><span class="n">setCameraPose</span><span class="p">(</span><span class="n">pose</span><span class="p">)</span>

<span class="c1"># We can set the 3D map views 2D extent to always match the main 2D canvas one
# Our 3D views get updated while zooming/panning the main 2D canvas
</span><span class="n">canvas</span> <span class="o">=</span> <span class="n">iface</span><span class="p">.</span><span class="n">mapCanvas</span><span class="p">()</span>
<span class="n">canvas</span><span class="p">.</span><span class="n">extentsChanged</span><span class="p">.</span><span class="n">connect</span><span class="p">(</span><span class="k">lambda</span> <span class="p">:</span><span class="n">c1</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">().</span><span class="n">setExtent</span><span class="p">(</span><span class="n">canvas</span><span class="p">.</span><span class="n">extent</span><span class="p">()))</span>
<span class="n">canvas</span><span class="p">.</span><span class="n">extentsChanged</span><span class="p">.</span><span class="n">connect</span><span class="p">(</span><span class="k">lambda</span> <span class="p">:</span><span class="n">c2</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">().</span><span class="n">setExtent</span><span class="p">(</span><span class="n">canvas</span><span class="p">.</span><span class="n">extent</span><span class="p">()))</span>
<span class="n">canvas</span><span class="p">.</span><span class="n">extentsChanged</span><span class="p">.</span><span class="n">connect</span><span class="p">(</span><span class="k">lambda</span> <span class="p">:</span><span class="n">c3</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">().</span><span class="n">setExtent</span><span class="p">(</span><span class="n">canvas</span><span class="p">.</span><span class="n">extent</span><span class="p">()))</span>
<span class="n">canvas</span><span class="p">.</span><span class="n">extentsChanged</span><span class="p">.</span><span class="n">connect</span><span class="p">(</span><span class="k">lambda</span> <span class="p">:</span><span class="n">c4</span><span class="p">.</span><span class="n">mapSettings</span><span class="p">().</span><span class="n">setExtent</span><span class="p">(</span><span class="n">canvas</span><span class="p">.</span><span class="n">extent</span><span class="p">()))</span>
</code></pre></div></div>

<center>
  <p><img title="Changing 3D view settings through Python" src="https://lutraconsulting.co.uk/img/posts/3d_scene_change_view.png" alt="Changing 3D view settings through Python" /></p>
  <sub>Changing 3D view settings through Python</sub>
</center>

<h1 id="more-point-clouds-attributes">More point clouds attributes</h1>
<p>LAS/LAZ/COPC point clouds have a <code class="highlighter-rouge">classificationFlags</code> attribute that stores four types of information (Synthetic, Keypoint, Withheld, and Overlap) in a single value. This saves space, but it makes it difficult to use the information for styling or filtering, as you need to write complex expressions.</p>

<p>To make it easier to use, we are following the approach introduced in PDAL 2.6: the <code class="highlighter-rouge">classificationFlags</code> attribute gets replaced with four separate attributes: Synthetic, Keypoint, Withheld, and Overlap. This will make it easier to include these attributes in styling and filtering expressions.</p>

<h1 id="performance-enhancement-for-rendering">Performance enhancement for rendering</h1>
<p>To improve the performance of point cloud rendering in QGIS, we introduced a new caching system to minimise the need for repeated decompression of LAS node data while panning or zooming. This caching mechanism efficiently stores decompressed points for each unique combination of layer URI, node, requested attributes, filter extent, and filter expression. This enables rapid rendering of previously cached nodes, significantly enhancing the overall rendering performance in 2D and 3D maps.</p>

<p>Performance can vary depending on actual data, but on a local sample COPC file, it renders 7 times faster with this change.</p>

<h1 id="labels-for-mesh-layer">Labels for mesh layer</h1>

<p>Viewing mesh data has been possible through styling, plotting or using the Identify tool. But now you can also create labels on mesh surfaces or vertices similar to vector layers.</p>

<p>To display labels for your mesh data, simply open the styling panel and enable labels for:</p>
<ul>
  <li>Labels on Vertices</li>
  <li>Labels on Surfaces</li>
</ul>

<center>
  <p><img title="Label settings for mesh layers" src="https://lutraconsulting.co.uk/img/posts/mesh_label_settings.png" alt="Label settings for mesh layers" /></p>
  <sub>Label settings for mesh layers</sub>
</center>

<p>Below is an example of mesh Z values at vertices (yellow) and mesh areas at cell centre (purple):</p>

<center>
  <p><img title="Example of labels on a mesh layer" src="https://lutraconsulting.co.uk/img/posts/mesh_labels.png" alt="Example of labels on a mesh layer" /></p>
  <sub>Example of labels on a mesh layer</sub>
</center>

<h1 id="want-more-changes-in-qgis">Want more changes in QGIS?</h1>
<p>Do you want to see more improvements and new features in QGIS? Do not hesitate to <a href="mailto:info@lutraconsulting.co.uk">contact us</a> to discuss your requiremnets.</p>
