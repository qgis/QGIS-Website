---
source: "blog"
title: "OPENGIS.ch blog: QField background tracking"
image: "qfield-background-tracking."
date: "2023-06-29"
link: "https://www.opengis.ch/2023/06/29/qfield-background-tracking/"
draft: "true"
showcase: "planet"
---

<p>Years ago, the QField community and its users showed their love for their favourite field app by supporting a successful crowdfunding to improve camera handling.</p>



<p>Since then, OPENGIS.ch has continued to lead the development of QField with the regular support of sponsors. We couldn’t be prouder of the progress we have made, with plenty of new features added in every major release. This includes major improvements to positioning including location tracking, integration of external GNSS receivers through not only Bluetooth but TCP/UDP and serial port connections, accuracy indicator and constraints, and most recently sensors reading to list a few.</p>



<p>We are now calling for the community to help further better QField and unlock an important milestone: <strong>background location tracking service</strong>.</p>



<div class="wp-block-buttons is-horizontal is-content-justification-center is-layout-flex wp-container-1">
<div class="wp-block-button"><a class="wp-block-button__link has-text-align-center wp-element-button" href="#pledge-now">Pledge now</a></div>
</div>



<p></p>



<figure class="wp-block-image size-large"><img data-attachment-id="13823" data-permalink="https://www.opengis.ch/2023/06/29/qfield-background-tracking/woman-traveler-explorer-with-backpack-hiking-to-the-top-of-the-mountain-adventure-weekend/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?fit=1920%2C1280&amp;ssl=1" data-orig-size="1920,1280" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;Shi  - stock.adobe.com&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;Woman traveler explorer with backpack hiking to the top of the mountain. Adventure weekend concept.&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;Woman traveler explorer with backpack hiking to the top of the mountain. Adventure weekend.&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="Woman traveler explorer with backpack hiking to the top of the mountain. Adventure weekend." data-image-description="" data-image-caption="&lt;p&gt;Woman traveler explorer with backpack hiking to the top of the mountain. Adventure weekend concept.&lt;/p&gt;
" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?fit=300%2C200&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?fit=750%2C500&amp;ssl=1" decoding="async" loading="lazy" width="750" height="500" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=750%2C500&#038;ssl=1" alt="" class="wp-image-13823" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=1024%2C683&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=300%2C200&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=768%2C512&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=1536%2C1024&amp;ssl=1 1536w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?resize=360%2C240&amp;ssl=1 360w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/06/gps-tracking.jpeg?w=1920&amp;ssl=1 1920w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<h2 class="wp-block-heading">Main goal: background location tracking on Android – 25&#8217;000€</h2>



<p>Currently, QField requires users to keep their devices’ screen on and have the app in the foreground to keep track of the device’s positioning location. On mobile devices, this can drain batteries faster than many would want to, in environments where charging options are limited.</p>



<p>This crowdfunding aims at removing this constraint and <strong>allow QField &#8211; via a background service &#8211; to constantly keep tracking location</strong> even while the device is suspended (i.e., when the screen is turned off / locked).&nbsp;</p>



<p>To achieve this, a significant amount of work is required as the positioning framework on Android will need to be relocated to a dedicated background service. Recent work we’ve done adding a background service to synchronize captured image attachments in <a href="https://qfield.cloud/">QFieldCloud projects</a> armed us with the assurances that we can achieve our goal while giving us an appreciation of the large amount of work needed.</p>



<h3 class="wp-block-heading"><em>Some of the benefits</em></h3>



<p>Running out of battery is the nightmare of most field surveyors. By moving location tracking to a background service, users will be able to <strong>considerably improve their battery life</strong> and keep focusing on their tasks.</p>



<p>Furthermore, while OPENGIS.ch ninjas remain busy squashing reported QField crashes all year long, there will always be unexpected scenarios leading to abrupt app shut down such as third party apps, system running out of battery, etc. To address this, the background service framework will also <strong>act as a safeguard to avoid location data loss</strong> when QField unexpectedly shuts down and offer users means to recover that data upon re-opening QField.</p>



<h2 class="wp-block-heading">Stretch goal 1: background navigation audio feedback 5&#8217;000€</h2>



<p>The second stretch goal builds onto QField’s nice fly-to-point navigation system. If the QField community meets this threshold, a new <strong>background navigation audio feedback informing users in the field of their proximity to their target </strong>will be implemented.&nbsp;</p>



<p>The audio feedback will use text-to-speech technology to state the distance to target in meters for a given time or distance interval.</p>



<h2 class="wp-block-heading">Stretch goal 2: iOS 15&#8217;000€</h2>



<p>The main goal will cover the Android implementation only. Due to being a very low level work we will have to replicate the work for each platform we support. If we reach stretch goal 2 we will also implement this for iOS.</p>



<h1 id="pledge-now" class="wp-block-themeisle-blocks-advanced-heading pledge-now">Pledge now:</h1>



<iframe loading="lazy" class="clickup-embed clickup-dynamic-height" src="https://forms.clickup.com/2192114/f/22wqj-26041/KCQACZWJ84G4MJJ2XR" onwheel="" width="100%" height="100%" style="background: transparent; border: 1px solid #ccc;"></iframe><script async src="https://app-cdn.clickup.com/assets/js/forms-embed/v1.js"></script>



<p>In case you do not see the embedded form you can open it directly <a href="https://forms.clickup.com/2192114/f/22wqj-26041/KCQACZWJ84G4MJJ2XR">here</a>.</p>



<p>Thanks for supporting our crowdfunding and keep an eye on our blog for updates on the status.</p>



<p></p>
