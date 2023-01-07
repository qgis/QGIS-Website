---
source: "blog"
title: "OPENGIS.ch blog: QGIS Relations, their Widgets and the Plugins of them"
image: "qgis-relations-their-widgets-and-the-plugins-of-them."
date: "2022-11-28"
link: "https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/"
draft: "true"
showcase: "planet"
---

<p><em><strong>This blog post is about QGIS relations and how they are edited in the attribute form with widgets in general, as well as some plugins that override the relations editor widget to improve usability and solve specific use cases. The start is quite basic. If you are already a relation hero, then <a href="#plugins" data-type="internal" data-id="#plugins">jump directly to the plugins</a>.</strong></em></p>



<h2 id="qgis-relations">QGIS Relations in General</h2>



<p>Let&#8217;s have a look at a simple example data model. We have four entities: Building, Apartment, Address and Owner. In UML it looks like this:</p>



<figure class="wp-block-image size-large"><img data-attachment-id="13466" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/erm/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?fit=1893%2C873&amp;ssl=1" data-orig-size="1893,873" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="erm" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?fit=300%2C138&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?fit=750%2C346&amp;ssl=1" loading="lazy" width="750" height="346" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=750%2C346&#038;ssl=1" alt="" class="wp-image-13466" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=1024%2C472&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=300%2C138&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=768%2C354&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=469%2C216&amp;ssl=1 469w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?resize=1536%2C708&amp;ssl=1 1536w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/erm.png?w=1893&amp;ssl=1 1893w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<ul><li>A building can have none or multiple apartments, but an apartment must to be related to a building. This black box on the left describes the relation strength as a composition. An apartment cannot exist without a building. When a building is demolished, all apartments of it are demolished as well.</li><li>An apartment needs to be owned by at least one owner. An owner can own none or more apartments. This is a many-to-many relation and this means, it will be normalized by adding a linking (join) table in between.</li><li>A building can have an address (only one &#8211; no multiple entrances in this example). An address can refer to one building. <br>Why not making one single table on a one-to-one relation? To ensure their existence independently: When a building is demolished, the address should persist until the new building is constructed.</li></ul>



<h3 id="creating-relations-in-qgis">Creating Relations in QGIS</h3>



<p>In QGIS we have now five layers. The four entities and the linking table called &#8220;Apartment_Owner&#8221;.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13467" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/layers/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?fit=878%2C397&amp;ssl=1" data-orig-size="878,397" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="layers" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?fit=300%2C136&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?fit=750%2C339&amp;ssl=1" loading="lazy" width="750" height="339" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?resize=750%2C339&#038;ssl=1" alt="" class="wp-image-13467" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?w=878&amp;ssl=1 878w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?resize=300%2C136&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?resize=768%2C347&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?resize=500%2C226&amp;ssl=1 500w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/layers.png?resize=469%2C212&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>Open&nbsp;<em>Project &gt; Properties&#8230; &gt; Relations</em></p>



<p>With&nbsp;<em>Discover Relations</em>&nbsp;the possible relations are detected from the existing layers according to their foreign keys in the database. In this example no CASCADE is defined in the database what means that the relations strength is always &#8220;Association&#8221;.</p>



<h4 id="where-would-composition-make-sense">Where would &#8220;Composition&#8221; make sense?</h4>



<p>Of course in the relation &#8220;Apartment&#8221; to &#8220;Building&#8221;, to ensure that when a feature of &#8220;Building&#8221; is deleted, the children (&#8220;Apartment&#8221;) are deleted as well, because they cannot exist without a building. Also a&nbsp;<em>duplication</em>&nbsp;of a feature of &#8220;Building&#8221; would duplicate the children (&#8220;Apartment&#8221;) as well.</p>



<p>But as well on the linking (join) table &#8220;Apartment_Owner&#8221; and its relation to &#8220;Apartment&#8221; and &#8220;Owner&#8221; a composition would make sense. Because when a feature of &#8220;Apartment&#8221; or &#8220;Owner&#8221; is deleted, the entry in the linking table should be deleted as well. Because this connection does not exist anymore and otherwise this would lead to orphan entries in the linking table.</p>



<h3 id="walk-through-the-widgets">Walk through the widgets</h3>



<p>To demonstrate the relation widgets&nbsp;<em>Relation Editor</em>,&nbsp;<em>Relation Reference</em>&nbsp;and&nbsp;<em>Value Relation</em>&nbsp;we make a walk through the digitizing process.</p>



<h4 id="relation-editor">Relation Editor</h4>



<p>First we create a &#8220;Building&#8221; and call it &#8220;Garden Tower&#8221;. Then we add some &#8220;Apartments&#8221;.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13468" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/relationeditor/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?fit=1017%2C512&amp;ssl=1" data-orig-size="1017,512" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="relationeditor" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?fit=300%2C151&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?fit=750%2C378&amp;ssl=1" loading="lazy" width="750" height="378" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?resize=750%2C378&#038;ssl=1" alt="" class="wp-image-13468" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?w=1017&amp;ssl=1 1017w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?resize=300%2C151&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?resize=768%2C387&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor.png?resize=469%2C236&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>The &#8220;Apartments&#8221; are created in the widget called&nbsp;Relation Editor. This shows us a list (similar to the <em>QGIS Attribute Table</em>) of all children (&#8220;Apartment&#8221;) referencing to this &#8220;Building&#8221;. We have here activated the possibilities to&nbsp;<em>add</em>,&nbsp;<em>delete</em>&nbsp;and&nbsp;<em>duplicate</em>&nbsp;child-features.</p>



<p>In the widget settings (<em>Right-click on the layer &gt; Properties&#8230; &gt; Attribute Form</em>) we see that there are other possibilities to&nbsp;<em>link</em>&nbsp;and&nbsp;<em>unlink</em>&nbsp;child-features as well as&nbsp;<em>zoom</em>&nbsp;to the current child-feature (what only would make sense when they have a geometry).</p>



<figure class="wp-block-image size-large"><img data-attachment-id="13469" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/relationeditor_settings/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?fit=1077%2C473&amp;ssl=1" data-orig-size="1077,473" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="relationeditor_settings" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?fit=300%2C132&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?fit=750%2C330&amp;ssl=1" loading="lazy" width="750" height="330" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?resize=750%2C330&#038;ssl=1" alt="" class="wp-image-13469" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?resize=1024%2C450&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?resize=300%2C132&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?resize=768%2C337&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?resize=469%2C206&amp;ssl=1 469w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_settings.png?w=1077&amp;ssl=1 1077w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>As well we can set here the cardinality. This will become interesting when we go to the &#8220;Owner&#8221; to &#8220;Apartment&#8221; relation. But let&#8217;s first have a look at the opposite of what we just did.</p>



<h4 id="relation-reference">Relation Reference</h4>



<p>When we open now a feature of &#8220;Apartment&#8221;, we see that we have a drop down to select the &#8220;Building&#8221; to reference to.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13470" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/relationreference/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?fit=720%2C113&amp;ssl=1" data-orig-size="720,113" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="relationreference" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?fit=300%2C47&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?fit=720%2C113&amp;ssl=1" loading="lazy" width="720" height="113" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?resize=720%2C113&#038;ssl=1" alt="" class="wp-image-13470" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?w=720&amp;ssl=1 720w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?resize=300%2C47&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationreference.png?resize=469%2C74&amp;ssl=1 469w" sizes="(max-width: 720px) 100vw, 720px" data-recalc-dims="1" /></figure>



<p>On the right of this drop down we can see some buttons. Those are for the following functionalities (from left to right):</p>



<ul><li>Open the form of the current parent feature (in our case the &#8220;Building&#8221; feature called &#8220;Garden Tower&#8221;)</li><li>Add a new feature on the parent layer (in our case &#8220;Building&#8221;)</li><li>Highlight the parent layer (in our case &#8220;Building&#8221;) on the map</li><li>Select the parent feature (in our case &#8220;Building&#8221;) on the map to reference it</li></ul>



<p>In the settings (<em>Right-click on the layer &gt; Properties&#8230; &gt; Attribute Form</em>) we see that we choose the configured relation to connect the child (&#8220;Apartment&#8221;) to the parent (&#8220;Building&#8221;). This won&#8217;t be needed with the widget&nbsp;<em>Value Relation</em>.</p>



<h4 id="value-relation">Value Relation</h4>



<p>The&nbsp;<em>Value Relation</em>&nbsp;does not require a relation at all. We simply choose the &#8220;parent&#8221; layer (&#8220;Building&#8221;) its primary key as the key (&#8220;t_id&#8221;) and a descriptive field as the value (&#8220;Description&#8221;).</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13471" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/valuerelation_settings/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?fit=808%2C162&amp;ssl=1" data-orig-size="808,162" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="valuerelation_settings" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?fit=300%2C60&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?fit=750%2C150&amp;ssl=1" loading="lazy" width="750" height="150" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?resize=750%2C150&#038;ssl=1" alt="" class="wp-image-13471" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?w=808&amp;ssl=1 808w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?resize=300%2C60&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?resize=768%2C154&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation_settings.png?resize=469%2C94&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>The result shows us a drop down as well to select the parent.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13472" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/valuerelation/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?fit=720%2C103&amp;ssl=1" data-orig-size="720,103" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="valuerelation" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?fit=300%2C43&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?fit=720%2C103&amp;ssl=1" loading="lazy" width="720" height="103" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?resize=720%2C103&#038;ssl=1" alt="" class="wp-image-13472" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?w=720&amp;ssl=1 720w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?resize=300%2C43&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/valuerelation.png?resize=469%2C67&amp;ssl=1 469w" sizes="(max-width: 720px) 100vw, 720px" data-recalc-dims="1" /></figure>



<p>It is much easier to configure, but you can see the limitations. There are no such functionalities to control the parent feature like&nbsp;<em>add</em>,&nbsp;<em>identify on map</em>&nbsp;etc. As well you need to be careful to fulfill the foreign key constraint (you have to choose the correct field to link with). All this is given, when you build a&nbsp;<em>Relation Reference</em>&nbsp;on an existing relation.</p>



<h4 id="many-to-many-relations">Many-to-Many Relations</h4>



<p>Now we link some &#8220;Owner&#8221; to our &#8220;Apartment&#8221;. We could create new ones like we did it for the &#8220;Apartment&#8221; in &#8220;Building&#8221; or we can&nbsp;<em>link</em>&nbsp;existing ones. For linking we choose the yellow link-button on the top of the&nbsp;<em>Relation Editor</em>.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13473" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/linking_dialog/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?fit=857%2C318&amp;ssl=1" data-orig-size="857,318" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="linking_dialog" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?fit=300%2C111&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?fit=750%2C278&amp;ssl=1" loading="lazy" width="750" height="278" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?resize=750%2C278&#038;ssl=1" alt="" class="wp-image-13473" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?w=857&amp;ssl=1 857w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?resize=300%2C111&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?resize=768%2C285&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/linking_dialog.png?resize=469%2C174&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>This dialog looks similar to the&nbsp;<em>Relation Editor</em>&nbsp;widget. You have just to select the &#8220;Owner&#8221; you want to link to the &#8220;Apartment&#8221; by checking the yellow box. It&#8217;s a very powerful tool, but people are often confused about the load of functionality here and the selection that can be difficult to get used to (yellow boxes vs. blue index selection). For this case we extended the&nbsp;<em>Relation Editor</em>&nbsp;widget with a <a href="#linkingrelationeditor" data-type="internal" data-id="#linkingrelationeditor">plugin</a>.</p>



<p>Anyway after that we linked our features of the layer &#8220;Owner&#8221;.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13474" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/relationeditor_many/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?fit=816%2C202&amp;ssl=1" data-orig-size="816,202" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="relationeditor_many" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?fit=300%2C74&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?fit=750%2C186&amp;ssl=1" loading="lazy" width="750" height="186" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?resize=750%2C186&#038;ssl=1" alt="" class="wp-image-13474" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?w=816&amp;ssl=1 816w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?resize=300%2C74&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?resize=768%2C190&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/relationeditor_many.png?resize=469%2C116&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>Have you seen the linking table in between? Well, me neither. It&#8217;s completely invisible for the end user. This because of the cardinality setting I mentioned already. When we choose the linked table &#8220;Owner&#8221; instead of &#8220;Many to one relation&#8221;, then we can create and link the other parent (&#8220;Owner&#8221;) directly.</p>



<h4 id="one-to-one-relation">One-to-One Relation</h4>



<p>A one-to-one relation like we have here between &#8220;Building&#8221; and &#8220;Address&#8221; is created in the database more or less like a normal one-to-many relation. This means one of the tables (in our case &#8220;Address&#8221;) has a foreign key pointing to the parent table (&#8220;Building&#8221;). There are tricks to fulfill the one-to-one maximum cardinality (like e.g. by setting a UNIQUE constraint on this foreign key column) but still in the QGIS user interface it looks like a one-to-many relation. It&#8217;s displayed in a normal&nbsp;<em>Relation Editor</em>&nbsp;widget.</p>



<p>Solutions could be so called &#8220;Joins&#8221;. Go to the settings (<em>Right-click on the layer &gt; Properties&#8230; &gt; Joins</em>)</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13475" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/joins_settings/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?fit=855%2C301&amp;ssl=1" data-orig-size="855,301" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="joins_settings" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?fit=300%2C106&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?fit=750%2C264&amp;ssl=1" loading="lazy" width="750" height="264" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?resize=750%2C264&#038;ssl=1" alt="" class="wp-image-13475" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?w=855&amp;ssl=1 855w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?resize=300%2C106&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?resize=768%2C270&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins_settings.png?resize=469%2C165&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>Here you can join a layer of your choice and add the fields of this other layer (in our case &#8220;Address&#8221;) to your current feature form (of &#8220;Building&#8221;). So it appears to the user that it&#8217;s the same table containing fields of &#8220;Building&#8221; and &#8220;Address&#8221;.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13476" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/joins/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?fit=1002%2C296&amp;ssl=1" data-orig-size="1002,296" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="joins" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?fit=300%2C89&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?fit=750%2C222&amp;ssl=1" loading="lazy" width="750" height="222" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?resize=750%2C222&#038;ssl=1" alt="" class="wp-image-13476" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?w=1002&amp;ssl=1 1002w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?resize=300%2C89&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?resize=768%2C227&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/joins.png?resize=469%2C139&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>Negative point about those joins are, that they are fault prone. You have to be careful with default values (e.g. on primary keys) of the joined layer. You cannot expect a fully reliable feature form like you have it in the&nbsp;<em>Relation Editor</em>. Here as well, we extended the&nbsp;<em>Relation Editor</em>&nbsp;widget with a <a href="#linkingrelationeditor" data-type="internal" data-id="#linkingrelationeditor">plugin</a>.</p>



<h2 id="plugins">Plugins for Relation Editor Widgets</h2>



<p>Since QGIS 3.18 the base class of the <em>Relation Editor Widgets </em>became abstract, what opened the possibility to use it in PyQGIS and derive it to super nice widgets handling specific use cases and improving the usability.</p>



<h3 id="linkingrelationeditor">Linking Relation Editor Widget</h3>



<p>As mentioned before, the QGIS stock dialog to link children is full of features but it can be overwhelming and difficult to use. Mostly because of the two selection possibilities in the list. A blue selection is for the currently displayed feature, and a yellow checkbox selection is for the features to be actually linked.</p>



<p>In collaboration with the Model Baker Group we wanted to improve the situation. But as we where unsure how the end solution should look like, so we decided to experiment in a plugin. The result is a<em> link manger dialog,</em> in which features can be <em>linked</em> and <em>unlinked</em> by moving them left and right. The effective link is created or destroyed when the dialog is accepted.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13461" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/peek-2022-11-25-13-59/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-13-59.gif?fit=804%2C445&amp;ssl=1" data-orig-size="804,445" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Peek-2022-11-25-13-59" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-13-59.gif?fit=300%2C166&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-13-59.gif?fit=750%2C415&amp;ssl=1" loading="lazy" width="750" height="415" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-13-59.gif?resize=750%2C415&#038;ssl=1" alt="" class="wp-image-13461" data-recalc-dims="1"/></figure>



<p>Find more information on the repository <a rel="noreferrer noopener" href="https://github.com/opengisch/qgis-linking-relation-editor" target="_blank">https://github.com/opengisch/qgis-linking-relation-editor</a></p>



<h3>Ordered Relation Editor Widget</h3>



<p>Sometimes the order of the children play a role on the project, and you want to have them displayed following that. For that there is the <em>Ordered Relation Editor Widget</em>. You can configure a field in the children to be used to order them. In the given example the field <em>Floor</em> was used to order <em>Apartments</em>. Reordering the fields by Drag&amp;Drop would change the value of the configured field. Display name and optionally a path to an icon to be shown on the list can be configured by expression in the <em>Attribute Form</em> tab in the layer properties (<em>Right-click on the layer &gt; Properties&#8230; &gt; Attribute Form</em>).</p>



<figure class="wp-block-image size-large"><img data-attachment-id="13478" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/peek-2022-11-25-14-08-1/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?fit=1174%2C570&amp;ssl=1" data-orig-size="1174,570" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Peek-2022-11-25-14-08-1" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?fit=300%2C146&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?fit=750%2C364&amp;ssl=1" loading="lazy" width="750" height="364" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?resize=750%2C364&#038;ssl=1" alt="" class="wp-image-13478" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?resize=1024%2C497&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?resize=300%2C146&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?resize=768%2C373&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-25-14-08-1.gif?resize=469%2C228&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /><figcaption>Find more information on the repository <a rel="noreferrer noopener" href="https://github.com/opengisch/qgis-ordered-relation-editor" target="_blank">https://github.com/opengisch/qgis-ordered-relation-editor</a></figcaption></figure>



<h3>Document Management System Widgets</h3>



<p>Often in QGIS projects there is the need to deal with external documents. This could be for example pictures, documentations or reports about some features. To support that we added two new tables in the project:</p>



<ul><li><strong>Documents</strong> each document is represented by a row in this table. The table has following fields:<ul><li><strong>id</strong></li></ul><ul><li><strong>path</strong> is the filename of the document.</li></ul></li><li><strong>DocumentsFeatures</strong> this is a linking (join) table and permits to link a document with one or more features in more layers. The table has following fields:<ul><li><strong>id</strong></li><li><strong>document_id</strong> id of the document.</li><li><strong>feature_id</strong> id of the feature.</li><li><strong>feature_layer</strong> layer of the feature.</li></ul></li></ul>



<p>Thanks to a QGIS feature named <em><a href="https://www.qgis.org/en/site/forusers/visualchangelog318/index.html?highlight=polymorph#id48">Polymorphic Relations</a></em> we can link a document with features of multiple layers. The polymorphic relation can evaluate an expression to decide in which table will be the feature to link. Here a screenshot of the relation configuration:</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13484" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/image-3-5/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?fit=916%2C116&amp;ssl=1" data-orig-size="916,116" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="image-3" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?fit=300%2C38&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?fit=750%2C95&amp;ssl=1" loading="lazy" width="750" height="95" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?resize=750%2C95&#038;ssl=1" alt="" class="wp-image-13484" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?w=916&amp;ssl=1 916w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?resize=300%2C38&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?resize=768%2C97&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/image-3.png?resize=469%2C59&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>After this configuration in the layers &#8220;Apartment&#8221; and &#8220;Building&#8221; it will be possible to link children from the &#8220;Documents&#8221; table. The document management plugin provides two widgets to simplify the handling of the relation. In the feature side widget the documents are displayed as a grid or list. If possible a preview of the contend is shown and you can add new documents via Drag&amp;Drop from the system file manager. <em>Double-click</em> on a document will open it in the default system viewer.</p>



<figure class="wp-block-image size-large"><img data-attachment-id="13488" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/peek-2022-11-27-15-25/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?fit=1174%2C570&amp;ssl=1" data-orig-size="1174,570" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Peek-2022-11-27-15-25" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?fit=300%2C146&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?fit=750%2C364&amp;ssl=1" loading="lazy" width="750" height="364" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?resize=750%2C364&#038;ssl=1" alt="" class="wp-image-13488" srcset="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?resize=1024%2C497&amp;ssl=1 1024w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?resize=300%2C146&amp;ssl=1 300w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?resize=768%2C373&amp;ssl=1 768w, https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-25.gif?resize=469%2C228&amp;ssl=1 469w" sizes="(max-width: 750px) 100vw, 750px" data-recalc-dims="1" /></figure>



<p>The second widget is meant to be used in the <em>Feature Form</em> of the &#8220;Documents&#8221; table, and it permits to handy see, for each document, with which feature from which layer it is linked.</p>



<figure class="wp-block-image size-full"><img data-attachment-id="13491" data-permalink="https://www.opengis.ch/2022/11/29/qgis-relations-their-widgets-and-the-plugins-of-them/peek-2022-11-27-15-30-1/" data-orig-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-30-1.gif?fit=836%2C511&amp;ssl=1" data-orig-size="836,511" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Peek-2022-11-27-15-30-1" data-image-description="" data-image-caption="" data-medium-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-30-1.gif?fit=300%2C183&amp;ssl=1" data-large-file="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-30-1.gif?fit=750%2C458&amp;ssl=1" loading="lazy" width="750" height="458" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2022/11/Peek-2022-11-27-15-30-1.gif?resize=750%2C458&#038;ssl=1" alt="" class="wp-image-13491" data-recalc-dims="1"/></figure>



<p>Find more information on the repository <a rel="noreferrer noopener" href="https://github.com/opengisch/qgis-document-management-system-plugin" target="_blank">https://github.com/opengisch/qgis-document-management-system-plugin</a></p>



<h2>That&#8217;s it</h2>



<p>Well then. We hope that all the beginners reading this article received some light on QGIS Relations and all the advanced user some inspiration on the immense possibilities you have with QGIS <img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f642.png" alt="🙂" class="wp-smiley" style="height: 1em; max-height: 1em;" /></p>
