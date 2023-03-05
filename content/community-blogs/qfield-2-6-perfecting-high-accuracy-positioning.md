---
source: "blog"
title: "OPENGIS.ch blog: QField 2.6: perfecting high-accuracy positioning"
image: "qfield-2-6-perfecting-high-accuracy-positioning."
date: "2023-01-23"
link: "https://www.opengis.ch/2023/01/26/qfield-2-6-perfecting-high-accuracy-positioning/"
draft: "true"
showcase: "planet"
---

<p>It’s only been a few weeks into the new year, but we’ve got great news for you: a brand new QField 2.6 “Geeky Gecko <img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f98e.png" alt="🦎" class="wp-smiley" style="height: 1em; max-height: 1em;" />” has been released with a focus on positioning improvements, including Bluetooth support for Windows. And with that, we are delighted to remove the ‘beta’ status from QField for Windows.</p>



<h2>New positioning features</h2>



<figure class="wp-block-image size-full"><img data-attachment-id="13566" data-permalink="https://www.opengis.ch/2023/01/26/qfield-2-6-perfecting-high-accuracy-positioning/26_cover/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?fit=800%2C501&amp;ssl=1" data-orig-size="800,501" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="26_cover" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?fit=300%2C188&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?fit=750%2C470&amp;ssl=1" width="750" height="470" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?resize=750%2C470&#038;ssl=1" alt="" class="wp-image-13566" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?w=800&amp;ssl=1 800w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?resize=300%2C188&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?resize=768%2C481&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2023/01/26_cover.png?resize=422%2C264&amp;ssl=1 422w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p><strong>Let’s open with a bang: QField 2.6 now supports NMEA streaming from external GNSS devices over TCP, UDP, and serial ports, in addition to preexisting Bluetooth connectivity. </strong>This new functionality means that QField is now compatible with a much larger range of GNSS devices out there.</p>



<p>These new receivers unlock NTRIP-driven centimetre accuracy for devices that use the Bluetooth connection to a manufacturer&#8217;s application to connect to NTRIP servers. In this scenario, QField could not initiate a Bluetooth connection since it was already taken. With the new TCP and UDP receivers &#8211; provided the manufacturer’s application offers NMEA streaming over either of those Internet protocols &#8211; QField can connect and consume high-accuracy positioning.</p>



<p>The presence of a serial port receiver provides support for external GNSS devices using Bluetooth on Windows via the virtual serial port created by the operating system. The lack of Bluetooth support on Windows was a long-wanted enhancement from QField users on that platform and was the last blocker for the ‘beta’ status to go away.</p>



<p><strong>In addition, QField 2.6 allows users to pick from half a dozen metrics a value to attach to the measure (M) dimension of geometries being digitized when locked to the current position. </strong>This functionality is available to both users digitizing and the positioning tracker. The measurement values available as of 2.6 are timestamp, ground speed, bearing, horizontal accuracy and vertical accuracy, as well as PDOP, HDOP and VDOP values.</p>



<h2>Growing Continuous Integration (CI) testing framework now covers positioning</h2>



<p>Starting with version 2.6, <strong>QField ships with increased quality assurances</strong> thanks to the addition of tests covering positioning functionalities in its growing CI framework.</p>



<p>Practically speaking, this means that every single line of QField code changed is now being tested against positioning-related regression, significantly decreasing the risks of shipping a new version of QField with broken functionality in the area of antenna height, vertical grid shift, and ellipsoidal height adjustments.</p>



<p>We would like to commend <a rel="noreferrer noopener" href="https://www.bahn.com/en" data-type="URL" data-id="https://www.bahn.com/en" target="_blank">Deutsche Bahn</a> for funding the required work here. This could not have come in soon enough as more and more people are opting for QField and relying on it for their crucial day-to-day fieldwork.</p>
