---
source: "blog"
title: "Lutra Consulting: View and track changes in QGIS"
image: "mergin-maps-local-changes."
date: "2022-11-09"
link: "https://lutraconsulting.co.uk/blog/2022/11/08/mergin-maps-local-changes/"
draft: "true"
showcase: "planet"
---

<p>With the recent changes to the <a href="https://merginmaps.com">Mergin Maps</a> plugin for QGIS, you can visualise the local changes before synchronising your data.</p>

<!-- more -->

<p>Have you ever been in the situation when, after making a lot of changes in your Mergin Maps project, you hesitate to press Sync button because you are not sure that all required changes are made or afraid that some unwanted edits were introduced? Or maybe you need to review the work done and see what actually have changed between two versions? If the answer to any of these questions is “yes” then you will like the changes visualisation functionality we introduced in the 2022.4 version of the <a href="https://merginmaps.com">Mergin Maps</a> plugin for QGIS.</p>

<p>Changes visualisation functionality comes handy in two use-cases: revising local changes made in the Mergin Maps project before syncing them with the server and getting a list of changes between two versions of the project. Let’s take a closer look at this feature.</p>

<h2 id="local-changes-visualisation">Local changes visualisation</h2>
<p>While working with Mergin Maps project, the user can at any time revise their current changes made locally. First, make sure that all your layer’s edits are saved (committed) as currently viewing of the unsaved changes is not supported. Then right-click on any vector layer and select “Show Local Changes” entry in the context menu.</p>

<center>
<img width="400" src="https://lutraconsulting.co.uk/img/posts/local_changes_context_menu.png" alt="Accessing local changes from context menu" />
<p><em>Accessing local changes from context menu</em></p>
</center>

<p>This will open the Changes Viewer dialog. Each vector layer with local changes has its own tab in the Changes Viewer dialog, the name of the tab matches the layer name and also contains information about the number of changes in this specific layer.
Local changes are shown on the map and in the tabular form, to distinguish different types of edits a following color codes are used: inserts (new features) are green, edits orange and deletions red. It is possible to enlarge or reduce the size of the map and table by dragging the splitter between them, splitter position is applied to all tabs and will be saved and reused on the further dialog calls.</p>

<center>
<img width="400" src="https://lutraconsulting.co.uk/img/posts/local_changes_window.png" alt="Features added, deleted and modified in map and tabular views" />
<p><em>Features added, deleted and modified in map and tabular views</em></p>
</center>

<p>Map canvas in the Changes Viewer dialog supports basic operations like panning as well as zooming in and out. By default, all project layers are shown on the map to provide better context, but it is possible to toggle their visibility by unchecking the “Toggle Project Layers” button in the toolbar above the map. When this button is unchecked, only changes from the current vector layer are shown.</p>

<p>If, after some panning/zooming, you need to return to the extent where all changes are visible — press “Zoom Full” button. Also, it is possible to select a specific feature(s) in the table below map and zoom to them by clicking the “Zoom To Selection” button.
Finally, changes can be added as a new memory layer to the current project. To do so, click “Add to project” button and choose one of the options: add changes from the current layer or add all changes from all layers. For each changed layer, a new memory layer will be added to the current project. These changes layers will preserve the same color coding for features and attribute table as used in the Changes Viewer dialog. Please note, that these layers should be manually removed from the project before the sync, unless it is your intention to make them a part of your Mergin Maps project.
Another way to revise local changes is to open Changes Viewer from the Project Status dialog by clicking “View Changes” button.</p>

<h2 id="mergin-maps-processing-tools">Mergin Maps Processing tools</h2>

<p>Sometimes one may want to export local changes as a vector layer and save that file for further usage. Of course, this can be done with the help of Changes Viewer dialog, but it is time-consuming, especially when the Mergin Maps project has many layers or if there is a need to check local changes in several projects. To cover this use-case, we also provide “Extract local changes” tool. This tool is a part of the Mergin Maps QGIS plugin and can be found under the “Mergin Maps” group in the Processing Toolbox.</p>

<center>
<img width="400" src="https://lutraconsulting.co.uk/img/posts/local_changes_toolbox.png" alt="Mergin Maps Processing tools to create changeset" />
<p><em>Mergin Maps Processing tools to create changeset</em></p>
</center>

<p>In the tool dialog you need to specify a directory with your Mergin Maps project, select a layer of interest either choosing from available layer or selecting a GeoPackage file in the project directory and layer in this file.</p>

<center>
<img width="400" src="https://lutraconsulting.co.uk/img/posts/local_changes_processing_tool.png" alt="Processing tool to extract local changes" />
<p><em>Processing tool to extract local changes</em></p>
</center>

<p>An output layer containing local changes will be created as a temporary or regular layer and added to the current project. This layer will have the same styling (both for features and attribute table) as the layers produced by Changes Viewer dialog.</p>

<center>
<img width="400" src="https://lutraconsulting.co.uk/img/posts/local_changes_results.png" alt="Result of the local change processing tool" />
<p><em>Result of the local change processing tool</em></p>
</center>

<p>The “Create diff” tool comes handy when you need to revise the changes between two versions of the layer in the Mergin Maps project. This tool is also a part of the Mergin Maps QGIS plugin, and it is implemented as a Processing algorithm. The “Create diff” tool can be found under the “Mergin Maps” group in the Processing Toolbox.</p>

<p>The tool dialog is quite similar to the “Extract local changes” tool dialog. Fill in input values: directory of your Mergin Maps project, layer of interest, start and end version numbers. Finally, specify location of the output vector layer or leave the field empty if you want it as a temporary layer in your current project. After clicking “Run” the tool will query the server for information and generate a vector layer containing all changes made between specified layer versions. For example, if some field value was changed in one version and then the same field was changed again in another version, then only the last change will be shown in the output changes file.</p>

<p>This feature is an another step in our ongoing efforts to create an easy-to-use tool for collaborative data collection and data management. If you need help or want to share your experience with Mergin Maps QGIS plugin, please join us in the community chatroom, and we will be happy to hear your thoughts.</p>
