---
source: "blog"
title: "Mergin Maps: [Changelog] 🔏 New Editor permission: safe and secure project collaboration"
image: "new-editor-permission-safe-and-secure-project-collaboration?utm_source=qgis."
date: "2024-06-20"
link: "https://wishlist.merginmaps.com/changelog/new-editor-permission-safe-and-secure-project-collaboration?utm_source=qgis"
draft: "true"
showcase: "planet"
---

<p>We are introducing a new type of workspace role and project permission called "<strong><u>Editor</u></strong>". Editors in your workspace will be able to <u>work on your projects without the risk of breaking your GeoPackage layers and QGIS project files.</u></p><p><strong>How does it work?</strong></p><p>✅ Editors can:</p><ul>
<li><p>Add, update, and delete features in your projects</p></li>
<li><p>Use the mobile app and the QGIS plugin</p></li>
<li><p>Add new files, except for QGIS project files</p></li>
<li><p>Edit files, except for QGIS project files and GeoPackages (without changing the layer schema)</p></li>
<li><p>Remove files, except for QGIS project files and GeoPackages</p></li>
</ul><p>⛔️ Editors cannot:</p><ul>
<li><p>Manipulate QGIS project files, including changing symbology, adding/removing layers, or updating forms. Any changes to a QGIS project file will not be synchronized and will be overridden if the server version of the QGIS project file changes.</p></li>
<li><p>Remove GeoPackages</p></li>
<li><p>Make changes in GeoPackages that would result in creating conflicted copies, such as adding new columns or layers</p></li>
</ul><p><strong>Who is this new permission type suitable for?</strong></p><p>This permission type is ideal for surveyors and others who need to add data without manipulating layer schemas and QGIS project settings.</p><p><strong>Next steps</strong></p><p>Please upgrade your QGIS plugin to the latest version and head to our dashboard</p><p></p><p>Editor permission is available on Cloud and Enterprise edition servers.</p><hr /><p>Read more details in the <a href="https://merginmaps.com/blog/introducing-editor-permissions---our-most-requested-feature" rel="noopener noreferrer nofollow" target="_blank">blog post</a> or in <a href="https://merginmaps.com/docs/manage/permissions/" rel="noopener noreferrer nofollow" target="_blank">our documentation</a>.</p>
