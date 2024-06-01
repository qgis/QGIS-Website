---
source: "blog"
title: "OPENGIS.ch blog: The PostgreSQL Connection Service File and Why We Love It"
image: "the-postgresql-connection-service-file-and-why-we-love-it."
date: "2024-05-30"
link: "https://www.opengis.ch/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/"
draft: "true"
showcase: "planet"
---

<p><strong><em>The PostgreSQL Connection Service File <code>pg_service.conf</code> is nothing new. It has existed for quite some time and maybe you have already used it sometimes too. But not only the new QGIS plugin <a href="https://github.com/opengisch/qgis-pg-service-parser-plugin">PG service parser</a> is a reason to write about our love for this file, as well we generally think it’s time to show you how it can be used for really cool things.</em></strong></p>



<h2 class="wp-block-heading"><strong>What is the Connection Service File?</strong></h2>



<p>The Connection Service File allows you to save connection settings for each so-called “service” locally.</p>



<p>So when you have a database called&nbsp;<code>gis</code>&nbsp;on a local PostgreSQL with port&nbsp;<code>5432</code>&nbsp;and username/password is&nbsp;<code>docker</code>/<code>docker</code>&nbsp;you can store this as a service called&nbsp;<code>my-local-gis</code>.</p>



<pre class="wp-block-code"><code># Local GIS Database for Testing purposes
</code></pre>


[my-local-gis]



<p>host=localhost port=5432 dbname=gis user=docker password=docker</p>



<p>This Connection Service File is called&nbsp;<code>pg_service.conf</code>&nbsp;and is by client applications (such as&nbsp;<a href="https://www.postgresql.org/docs/current/app-psql.html">psql</a>&nbsp;or&nbsp;<a href="https://qgis.org/en/site/">QGIS</a>) generally found directly in the user directory. In Windows it is then found in the user’s application directory&nbsp;<code>postgresql.pg_service.conf</code>. And in Linux it is by default located directly in the user’s directory&nbsp;<code>~/.pg_service.conf</code>.&nbsp;</p>



<p>But it doesn’t necessarily have to be there. The file can be anywhere on the system (or on a network drive) as long as you set the environment variable&nbsp;<code>PGSERVICEFILE</code>&nbsp;accordingly:</p>



<pre class="wp-block-code"><code>export PGSERVICEFILE=/home/dave/connectionfiles/pg_service.conf&nbsp;</code></pre>



<p>Once you have done this, the client applications will search there first – and find it.</p>



<p>If the above are not set, there is also another environment variable&nbsp;<code>PGSYSCONFDIR</code>&nbsp;which is a folder which is searched for the file&nbsp;<code>pg_service.conf</code>.</p>



<p>Once you have this, the service name can be used in the client application. That means in&nbsp;<a href="https://www.postgresql.org/docs/current/app-psql.html">psql</a>&nbsp;it would look like this:</p>



<pre class="wp-block-code"><code>~$ psql service=my-local-gis
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>



<p>And in QGIS like this:</p>



<figure class="wp-block-image"><img alt="" class="wp-image-14336" height="310" src="https://i0.wp.com/www.opengis.ch/wp-content/uploads/2024/05/image.png?resize=750%2C182&amp;ssl=1" width="1279" /></figure>



<p>If you then add a layer in QGIS, only the name of the service is written in the project file. Neither the connection parameters nor username/password are saved. In addition to the security aspect, this has various advantages, more on this below.</p>



<p>But you don’t have to pass all of these parameters to a service. If you only pass parts of them (e.g. without the database), then you have to pass them when the connection is called:</p>



<pre class="wp-block-code"><code>$psql "service=my-local-gis dbname=gis"
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>



<p>You can also override parameters. If you have a database&nbsp;<code>gis</code>&nbsp;configured in the service, but you want to connect the database web, you can specify the service and explicit the database:</p>



<pre class="wp-block-code"><code>$psql "service=my-local-gis dbname=web"
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

web=#</code></pre>



<p>Of course the same applies to QGIS.</p>



<p>And regarding the environment variables mentioned, you can also set a standard service.</p>



<pre class="wp-block-code"><code>export PGSERVICE=my-local-gis</code></pre>



<p>Particularly pleasant in daily work with always the same database.</p>



<pre class="wp-block-code"><code>$ psql
psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

gis=#</code></pre>



<h2 class="wp-block-heading"><strong>And why is it particularly cool?</strong></h2>



<p>There are several reasons why such a file is useful:</p>



<ul>
<li>Security: You don’t have to save the connection parameters anywhere in the client files (e.g. QGIS project files). Keep in mind that they are still plain text in the service file.</li>



<li>Decoupling: You can change the connection parameters without having to change the settings in client files (e.g. QGIS project files).</li>



<li>Multi-User: You can save the file on a network drive. As long as the environment variable of the local systems points to this file, all users can access the database with the same parameters.</li>



<li>Diversity: You can use the same project file to access different databases with the same structure if only the name of the service remains the same.</li>
</ul>



<p>For the last reason, here are three use cases.</p>



<h3 class="wp-block-heading"><strong>Support-Case</strong></h3>



<p>Someone reports a problem in QGIS on a specific case with their database. Since the problem cannot be reproduced, they send us a DB dump of a schema and a QGIS project file. The layers in the QGIS project file are linked to a service. Now we can restore the dump on our local database and access it with our own, but same named, service. The problem can be reproduced.</p>



<h3 class="wp-block-heading"><strong>INTERLIS</strong></h3>



<p>With INTERLIS the structure of a database schema is precisely specified. If e.g. the canton has built the physical database for it and configured a supernice QGIS project, they can provide the project file to a company without also providing the database structure. The company can build the schema based on the INTERLIS model on its own PostgreSQL database and access it using its own service with the same name.</p>



<h3 class="wp-block-heading"><strong>Test/Prod Switching</strong></h3>



<p>You can access a test and a production database with the same QGIS project if you have set the environment variable for the connection service file accordingly per&nbsp;<a href="https://docs.qgis.org/3.34/de/docs/user_manual/introduction/qgis_configuration.html#user-profiles">QGIS profile</a>.</p>



<p>You create two connection service files.</p>



<p>The one to the test database<code>&nbsp;/home/dave/connectionfiles/test/pg_service.conf</code>:</p>



<pre class="wp-block-code"><code>&#91;my-local-gis]
host=localhost
port=54322
dbname=gis-test</code></pre>



<p>And the one for the production database&nbsp;<code>/home/dave/connectionfiles/prod/pg_service.conf</code>:</p>



<pre class="wp-block-code"><code>&#91;my-local-gis]
host=localhost
port=54322
dbname=gis-productive</code></pre>



<p>In QGIS you create two profiles “Test” and “Prod”:</p>



<figure class="wp-block-image"><img alt="" src="https://lh7-us.googleusercontent.com/P5tG5kloX-sTGLtJjItVhTwQzGjhMugMEhgkUTfUfO4jblPxurVHGRdRcMkH2BGLyMrAPNZtOdaRO5OzeMvxR4CUC38gY23c9uGjXPn_65qSRRddeohzlDU4bQdPlbg5q9yGozwMjzuz9GeP-CTCPN8" /></figure>



<p>And you set the environment variable for each profile&nbsp;<code>PGSERVICEFILE</code>&nbsp;which should be used (in the menu&nbsp;<em>Settings &gt; Options…</em>&nbsp;and there under&nbsp;<em>System</em>&nbsp;scroll down to&nbsp;<em>Environment</em></p>



<figure class="wp-block-image"><img alt="image" src="https://lh7-us.googleusercontent.com/BZQzdWMsz1dbNf43syK1wkViu_uiOjitDu3a2wnJw7NElQ-OyvVwc26BR2y9rIW7ol_ocLGPOeRhfsjliIj9yWhUYqColQnwIpGfwVcMX2kPtFebDymTlFJjmbxDehH9QJ2MshLFu5TaULQfgOW-VZk" /></figure>



<p>or</p>



<figure class="wp-block-image"><img alt="image" src="https://lh7-us.googleusercontent.com/1KSjiGIKgFBxD13G7FYB_6wz6BRt2XbYmNJVdsgoCzptjN9K6PoR-Q5Ttxxnf6XAKXLYjWFL6PacuroU6klaW0EZJZtPDGVkLHPYQYUA1kACMMmJz7TZkQpGp-yvRaAaqN0j3sYJsZTXT2EXQACtdIc" /></figure>



<p>If you now use the service&nbsp;<code>my-local-gis</code>&nbsp;in a QGIS layer, it connects the database&nbsp;<code>prod</code>&nbsp;in the “Prod” profile and the database&nbsp;<code>test</code>&nbsp;in the “Test” profile.</p>



<h2 class="wp-block-heading"><strong>The authentication configuration</strong></h2>



<p>Let’s have a look at the authentication. If you have the connection service file on a network drive and make it available to several users, you may not want everyone to access it with the same login. Or you generally don’t want any user information in this file. This can be elegantly combined with the authentication configuration in QGIS.</p>



<p>If you want to make a QGIS project file available to multiple users, you create the layers with a service. This service contains all connection parameters except the login information.</p>



<p>This login information is transferred using QGIS authentication.</p>



<figure class="wp-block-image"><img alt="image" src="https://lh7-us.googleusercontent.com/RGByDYJr2czDGs4XKQD6SzCbsgiM318UdYav1m0z9fzX9_vQcFNjnZ5zqqg2X5hQ6HnJhwNGuszKYPpVSE5L53mxrpSTlLhGw5J8TAOB43IhTXFJlfII3ICPmX9ztbEOlR-TpJrlW5jfOy42-Dbx_Os" /></figure>



<p>You also configure this authentication per QGIS profile we mentioned above. This is done via Menu&nbsp;<em>Settings &gt; Options…</em>&nbsp;and there under&nbsp;<em>Authentication</em>:</p>



<figure class="wp-block-image"><img alt="image" src="https://lh7-us.googleusercontent.com/nnQe3fm9iMDFxG5QCxV_kpeBKjiUUefXx5B0dcNvMF7v0ObW_5051hXBBldC_CKSTrNPblJzwDo0zK2aQBKyz9ZM_27wIPtOY1i7srhpJLMr84VHWevuy4F1hj93ZjzJXbAKlt80gw0HuHtHaqcuigQ" /></figure>



<p>(or directly where you create the PostgreSQL connection)</p>



<p>If you add such a layer, the service and the ID of the authentication configuration are saved in the QGIS project file. This is in this case&nbsp;<code>mylogin</code>. Of course this name must be communicated to the other users so that they can also set&nbsp; the ID for their login to&nbsp;<code>mylogin</code>.</p>



<p>Of course, you can use multiple authentication configurations per profile.</p>



<h2 class="wp-block-heading"><strong>QGIS Plugin</strong></h2>



<p>And yes, there is now a great plugin to configure these services directly in QGIS. This means you no longer have to deal with text-based INI files. It’s called&nbsp;<a href="https://github.com/opengisch/qgis-pg-service-parser-plugin">PG service parser</a>:</p>



<figure class="wp-block-image"><img alt="image" src="https://lh7-us.googleusercontent.com/3JNSq_fmD2g33fLls2FGklpoCRo-M4Pyuts7z4dP56wKK7_tRj3hGyakJSQHTHBxWyQNkBfJQggaPl_InrOdY58b-6GN8eGBH9oOgJYLkq6XMApgGBrboR_FQ5dZwJZFiBpZZ4_oBg2_BTNUAGiuPkk" /></figure>



<p>It finds the connection service file according to the mentioned environment variables&nbsp;<code>PGSERVICEFILE</code>&nbsp;or&nbsp;<code>PGSYSCONFDIR</code>&nbsp;or at its default location.</p>



<p>As well it’s super easy to create new services by duplicating existing ones.</p>



<figure class="wp-block-image"><img alt="" src="https://lh7-us.googleusercontent.com/FvLhRVplNNN5EGo8OYmED9L786WKZOxxBZy98wVnJq6vywqo_Ny2wHQaKUbcMMaiyEVTD8BNKAeD0kAY_4HgmJ39NvEF9z20PPlbwPNIgVFRXwNQTYn5KgGOzJ8iUGJ4PnY7l1y0rNzOTrdOqMtbcNY" /></figure>



<h3 class="wp-block-heading">And for the Devs</h3>



<p>And what would a blog post be without some geek food? The back end of this plugin is published on&nbsp;<a href="https://pypi.org/project/pgserviceparser/">PYPI</a>&nbsp;and can be easily installed with&nbsp;<code>pip install pgserviceparser&nbsp;</code>and then be used in Python.</p>



<p>For example to list all the service names.&nbsp;</p>



<pre class="wp-block-code"><code>&gt;&gt;&gt; import pgserviceparser
&gt;&gt;&gt; pgserviceparser.service_names()
&#91;'my-local-gis', 'another-local-gis', 'opengisch-demo-pg']</code></pre>



<p>Optionally you can pass a config file path. Otherwise it gets it by the mentioned mechanism.</p>



<p>Or to receive the configuration from the given service name as a dict.</p>



<pre class="wp-block-code"><code>&gt;&gt;&gt; pgserviceparser.service_config('my-local-gis')
{'host': 'localhost', 'port': '54322', 'dbname': 'gis', 'user': 'docker', 'password': 'docker'}</code></pre>



<p>There are some more functions. Check them out here on&nbsp;<a href="https://github.com/opengisch/pgserviceparser">GitHub</a>&nbsp;or in the&nbsp;<a href="https://opengisch.github.io/pgserviceparser/">documentation</a>.</p>



<h2 class="wp-block-heading">Well then</h2>



<p>We hope you share our enthusiasm for this beautiful file – at least after reading this blog post. And if not – feel free to tell us why you don’t in the comments <img alt="🙂" class="wp-smiley" src="https://s.w.org/images/core/emoji/15.0.3/72x72/1f642.png" style="height: 1em;" /></p>
