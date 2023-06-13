---
source: "blog"
title: "OPENGIS.ch blog: QField 2.8: Boosting field work through external sensors"
image: "qfield-2-8-boosting-field-work-through-external-sensors."
date: "2023-05-27"
link: "https://www.opengis.ch/2023/05/30/qfield-2-8-boosting-field-work-through-external-sensors/"
draft: "true"
showcase: "planet"
---

<p>The latest version of QField is out, featuring as its main new feature sensor handling alongside the usual round of user experience and stability improvements. We simply can’t wait to see the sensor uses you will come up with!</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13777" data-permalink="https://www.opengis.ch/2023/05/30/qfield-2-8-boosting-field-work-through-external-sensors/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?fit=925%2C596&amp;ssl=1" data-orig-size="925,596" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?fit=300%2C193&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?fit=750%2C483&amp;ssl=1" decoding="async" loading="lazy" width="750" height="483" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?resize=750%2C483&#038;ssl=1" alt="" class="wp-image-13777" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?w=925&amp;ssl=1 925w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?resize=300%2C193&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/05/238116107-1792bb88-9fdb-41e7-9716-7fd65f8837ce.png?resize=768%2C495&amp;ssl=1 768w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<h2 class="wp-block-heading"><strong>The main highlight: sensors</strong></h2>



<p>QField 2.8 ships with <strong>out-of-the-box handling of external sensor streams</strong> over TCP, UDP, and serial port. The functionality allows for data captured through instruments – such as geiger counter, decibel sensor, CO detector, etc. &#8211; to be visualized and manipulated within QField itself.</p>



<p>Things get really interesting when sensor data is utilized as default values alongside positioning during the digitizing of features. You are always one tap away from adding a point locked onto your current position with spatially paired sensor readings saved as point attribute(s).</p>



<p>Not wowed yet? Try pairing sensor readings with QField’s tracking capability! <img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f609.png" alt="😉" class="wp-smiley" style="height: 1em; max-height: 1em;" /> Head over <a href="https://docs.qfield.org/how-to/sensors/" data-type="URL" data-id="https://docs.qfield.org/how-to/sensors/">QField’s documentation on this</a> as well as <a href="https://docs.qgis.org/testing/en/docs/user_manual/introduction/qgis_configuration.html#sensors-properties" data-type="URL" data-id="https://docs.qgis.org/testing/en/docs/user_manual/introduction/qgis_configuration.html#sensors-properties">QGIS&#8217; section on sensor management</a> to know more.</p>



<p>The development of this feature involved the addition of a sensor framework in upstream QGIS which will be available by the end of this coming June as part of the 3.32 release. This is a great example of the synergy between QField and its big brother QGIS, whereas development of new functionality often benefits the broader QGIS community. Big thanks to <a href="https://sevenson.com/" data-type="URL" data-id="https://sevenson.com/">Sevenson Environmental Services</a> for sponsoring this exciting capability.</p>



<h2 class="wp-block-heading"><strong>Notable improvements</strong></h2>



<p>A couple of refinements during this development cycle are worth mentioning. If you ever wished for QField to <strong>directly open a selected project or reloading the last session on app launch</strong>, you’ll be happy to know this is now possible.</p>



<p>For heavy users of value relations in their feature forms, QField is now a tiny bit more clever when displaying string searches against long lists, placing hits that begin with the matched string first as well as visually highlighting matches within the result list itself.</p>



<p>Finally, feature lists throughout QField are now sorted. By default, it will sort by the display field or expression defined for each vector layer, unless an advanced sorting has been defined in a given vector layer’s attribute table. It makes browsing through lists feel that much more natural.</p>
