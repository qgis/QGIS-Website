---
source: "blog"
title: "OPENGIS.ch blog: QField 3.3 “Darién”: It is just the beginning"
image: "qfield-3-3-darien-it-is-just-the-beginning."
date: "2024-06-11"
link: "https://www.opengis.ch/2024/06/11/qfield-3-3-darien-it-is-just-the-beginning/"
draft: "true"
showcase: "planet"
---

<p>QField 3.3 has been released, and with it, we are proud to introduce a brand new plugin framework that empowers users to customize and add completely new functionalities to their favourite field application. That’s on top of a bunch of new features and improvements added during this development cycle. What preceded this moment was just the beginning!</p>



<h2 class="wp-block-heading">Main highlights</h2>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14432" height="467" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/33splash.png?resize=750%2C467&#038;ssl=1" width="750" /></figure>



<p>One of the biggest feature additions of this version is a brand new drawing tool that allows users to sketch out important details over captured photos or annotate drawing templates. This was a highly requested feature, which we are delighted to bring to all supported platforms (Android, iOS, Windows, macOS, and, of course, Linux) with the financial support of the <a href="http://qgis.ch">Swiss QGIS user group</a>.</p>



<p>Also landing in this version is support for <strong>copying and pasting vector features into and from the clipboard</strong>. This comes in handy in multiple ways, from providing a quick and easy way to transfer attributes from one feature to another through matching field names to pasting the details of a captured feature in the field into a third-party messenger, word editing, or email application. Copying and pasting features can be done through the feature form’s menu as well as long pressed over the map canvas. If copy pasting ain’t your style, a new feature-to-feature attributes transfer shortcut has also been added to the feature form’s menu.</p>



<figure class="wp-block-gallery has-nested-images columns-default is-cropped wp-block-gallery-1 is-layout-flex wp-block-gallery-is-layout-flex">
<figure class="wp-block-image size-large"><img alt="" class="wp-image-14433" height="386" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/transfer_attributes.png?resize=750%2C386&#038;ssl=1" width="750" /></figure>
</figure>



<p>The feature form continues to gain more functionalities; in this version, the feature form’s value map editor widget has gained a <strong>new toggle button interface</strong> that can help fasten data entry. The interface replaces the traditional combo box with a series of toggle buttons, lowering the number of taps required to pick a value. If you enjoy this as much as we do, send a virtual thanks to Deutsches Archäologisches Institut, which sponsored this feature.</p>



<p>Other improvements in the feature form include support for <strong>value relation item grouping</strong> and respect for<strong> the vector layer attributes’ &#8220;reuse last entered value&#8221; setting</strong>.</p>



<figure class="wp-block-gallery has-nested-images columns-default is-cropped wp-block-gallery-2 is-layout-flex wp-block-gallery-is-layout-flex">
<figure class="wp-block-image size-large"><img alt="" class="wp-image-14434" height="386" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/value_map_buttons.png?resize=750%2C386&#038;ssl=1" width="750" /></figure>
</figure>



<p>Finally, additional features that are sure to please include support for <strong>image decoration overlay</strong>, a new interface to <strong>hop through cameras </strong>(front, back, and external devices) for the ‘non-native’ camera<strong>, </strong>the possibility to<strong> disable the 3-finger map rotation gesture</strong>, <a href="https://github.com/opengisch/QField/releases/tag/v3.3.0">and much more</a>.</p>



<h2 class="wp-block-heading"><strong>User experience improvements</strong></h2>



<p>Long-time users of QField will notice the new version <strong>restyling of the information panels such as GNSS positioning, navigation, elevation profile, and sensor data</strong>. The information is now presented as an overlay sitting on top of the map canvas, which increases the map canvas&#8217; visibility while also achieving better focus and clarity on the provided details. While revisiting these information panels, we’ve made sure all details, including altitude and distance to destination, respect user-configured project distance unit type.</p>



<p>The dashboard’s legend has also received some attention. You can now <strong>toggle the visibility of any layer via a quick tap on a new eye icon sitting in the legend tree</strong> itself. Similarly, legend groups can be expanded and collapsed directly for the tree. This also permits you to show or hide layers while digitizing a feature, something which was not possible until now. The development of these improvements was supported by <a href="https://www.gispo.fi/">Gispo</a> and sponsored by the <a href="https://www.maanmittauslaitos.fi/en">National Land Survey of Finland</a>.</p>



<h2 class="wp-block-heading"><strong>Plugin framework</strong></h2>



<p>Last but far away from least, QField 3.3 introduces a brand new plugin framework using Qt’s powerful QML and JavaScript engine. With a few lines of code, plugins can be written to tweak QField’s behaviour and add breathtaking capabilities. Two types of plugins are possible: app-wide plugins as well as project-scoped plugins. To ensure maximum ease of deployment, we have enabled project plugin distribution through <a href="https://qfield.cloud" rel="noreferrer noopener" target="_blank">QFieldCloud</a>!</p>



<figure class="wp-block-image size-full"><img alt="" class="wp-image-14445" height="386" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/06/plugin_manager.png?resize=750%2C386&#038;ssl=1" width="750" /></figure>



<p>We will write a dedicated post later this week explaining all the details of how QField plugins can radically change your field (and business) workflows by allowing you to be even more efficient in the field.</p>



<p>Users interested in authoring plugins or better understanding the framework, can already visit the <a href="https://docs.qfield.org/how-to/plugins/" rel="noreferrer noopener" target="_blank">dedicated documentation page</a> and a <a href="https://github.com/opengisch/qfield-weather-forecast">sample plugin implementation</a> sporting a weather forecast integration.</p>
