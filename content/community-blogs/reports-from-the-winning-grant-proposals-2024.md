---
source: "blog"
title: "QGIS Project blog: Reports from the winning grant proposals 2024"
image: "reports-from-the-winning-grant-proposals-2024."
date: "2025-02-07"
link: "https://blog.qgis.org/2025/02/07/reports-from-the-winning-grant-proposals-2024/"
draft: "true"
showcase: "planet"
---

<p>With the <a href="https://blog.qgis.org/2024/05/01/qgis-grant-programme-2024-results/">QGIS Grant Programme 2024</a> (Updates <a href="https://blog.qgis.org/2024/05/08/qgis-grant-programme-2024-update/">#1</a> &amp; <a href="https://blog.qgis.org/2024/06/14/qgis-grant-programme-2024-update-no-2/">#2</a>), we were able to support <a href="https://github.com/qgis/PSC/issues/60">7 enhancement proposals</a> that improve the QGIS project. The following reports summarize the work performed:  </p>



<ol class="wp-block-list">
<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/269">QEP#269 Update older annotation items to new framework</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-August/010304.html">report</a><br />This enhancement introduced new annotation types, improved callout options, and a rich text editor for better formatting. Annotations can now link to a &#8220;visibility layer,&#8221; and older types are automatically upgraded for a cleaner UI. Future improvements may include handling HTML annotations, deprecating the &#8220;Form&#8221; annotation, and refining the user experience.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/289">QEP#289 Authentication system revision (v1.1)</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2025-February/010450.html">report</a><br />This work enhances the authentication framework by automating password synchronization with the system keychain and generating secure default passwords for new profiles. Users now experience a smoother setup with fewer manual steps, while UI tweaks improve password handling and security. These changes provide a more seamless and secure experience for both users and plugin developers.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/291">QEP#291 Mitigate Abusive Tile Fetching on OpenStreetMap (OSM)</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-November/010348.html">report</a> <br />This work enhanced network caching by dynamically adjusting cache size based on available disk space, significantly improving tile storage for most users. New safeguards prevent accidental breaches of OpenStreetMap’s tile usage policy by limiting bulk downloads across various tools and warning users when thresholds are exceeded. Additionally, the default OpenStreetMap XYZ layer now uses a 96DPI tile resolution, reducing unnecessary tile requests and improving print layout exports. These changes help ensure responsible data usage while enhancing performance and usability.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/287">QEP#287 PyQGIS linter warnings</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-December/010400.html">report</a><br />This work enhanced QGIS’s Python integration by contributing upstream, directly to SIP. This approach avoids extra build-time complexity. In addition to static linting, support for deprecation messages was added, now active in QGIS (requires Python-SIP 6.9.0 or later). Due to budget constraints and dependency availability, planned updates to the plugin platform needed to be postponed.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/290">QEP#290 Clean up point cloud index and improve its thread safety</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-December/010402.html">report</a><br />This work enhanced point cloud support by providing shared pointer access to the point cloud index, cleaning up the point cloud index API, unifying local and remote implementations of EPT/COPC providers, and refining hierarchy fetching logic. These updates make point cloud handling more robust and better prepared for future use cases.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/292">QEP#292 Implementing CI Qt6 Windows Builds through vcpkg</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-October/010340.html">report</a><br />This enhancement focused on transitioning QGIS to build with Qt6 using vcpkg, streamlining dependency management and improving the Windows development experience. Continuous integration pipelines now test Qt6 builds, helping identify compatibility issues early. Additional contributions include improved build documentation, enhanced dependency tracking, modernized CMake scripts, and updates to the pull request comment bot. Preliminary work has also begun on macOS support using the same vcpkg system. These efforts lay the groundwork for a smoother Qt6 migration and long-term maintainability.</li>



<li><a href="https://github.com/qgis/QGIS-Enhancement-Proposals/issues/248">QEP#248 Authentication System: allow Database storage for authentication DB</a> &#8212; <a href="https://lists.osgeo.org/pipermail/qgis-psc/2024-October/010325.html">report</a><br />This enhancement introduced a new API for managing authentication credentials in QGIS. While its immediate impact on users is limited, it addresses SQLite scaling issues for QGIS Server in cloud environments and lays the foundation for future enhancements. The update includes an abstraction layer for third-party credential storage, support for multiple prioritized encrypted and unencrypted storage options, and improved access control for authentication assets. Documentation has been updated to reflect these changes.</li>
</ol>



<p>Thank you to everyone who participated and made this round of grants a great success and thank you to all our <a href="https://qgis.org/en/site/about/sustaining_members.html">sustaining members</a> and donors who make this initiative possible!</p>



<p></p>
