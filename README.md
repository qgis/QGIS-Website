# QGIS Hugo Website

![Screenshot](./img/hugo-preview.png)

By Tim Sutton and QGIS Contributors.

## Project Status

[![E2E Tests](https://github.com/qgis/QGIS-Hugo/actions/workflows/e2e.yml/badge.svg)](https://github.com/qgis/QGIS-Hugo/actions/workflows/e2e.yml)
[![Deploy Hugo site to Pages](https://github.com/qgis/QGIS-Hugo/actions/workflows/hugo.yml/badge.svg)](https://github.com/qgis/QGIS-Hugo/actions/workflows/hugo.yml)
![Website Status](https://img.shields.io/website-up-down-green-red/http/qgis.github.io/QGIS-Hugo.svg)
![License](https://img.shields.io/github/license/qgis/QGIS-Hugo.svg)

![](https://img.shields.io/github/issues/qgis/QGIS-Hugo.svg)
![](https://img.shields.io/github/issues-closed/qgis/QGIS-Hugo.svg)
![](https://img.shields.io/github/issues-pr/qgis/QGIS-Hugo.svg)
![](https://img.shields.io/github/issues-pr-closed/qgis/QGIS-Hugo.svg)


Project stars:
![Stars](https://starchart.cc/qgis/QGIS-Hugo.svg)

## 🏃Before you start

This web site is a static site built using [Hugo](https://gohugo.io/).

![Hugo Logo](./img/hugo-logo.png) and using the [hugo bulma blocks theme](https://github.com/kartoza/hugo-bulma-blocks-theme).

## 🛒 Getting the Code

development
```
git clone https://github.com/qgis/QGIS-Hugo.git
cd QGIS-Hugo
```


## 🧑💻 Development

First install hugo for your local machine:

**📝 Note:** we need to install the 'extended' hugo version which includes a SASS compiler. If you don't install the extended version you will get errors like this when compiling:

```
ERROR 2022/12/11 07:33:37 Rebuild failed: TOCSS: failed to transform 
"css/style.scss" (text/x-scss). Check your Hugo installation; you need 
the extended version to build SCSS/SASS.: this feature is not available 
in your current Hugo version, see https://goo.gl/YMrWcn for more information
```

You can find the extended version in the [releases page](https://github.com/gohugoio/hugo/releases).

![Download](./img/hugo-download.png)



### 🐧 Linux: 

Download the deb above and then do 

``sudo dpkg -i hugo_extended_0.107.0_linux-amd64.deb``

### 🪟 Windows: 

[Follow these notes](https://gohugo.io/installation/windows/)

### 🍏 macOS: 

[Follow these notes](https://gohugo.io/installation/macos/)

## ⚙️ Setting up VSCode

If you are using VSCode, I recommend the following extensions:

* Hugo Language and Syntax Support
* Color Highlight

Clone the repo:

```
git clone https://github.com/qgis/qgis-hugo.git
```

Run the site:

Press ```Ctl-Shift-D``` then choose the following runner:

'Run dev using locally installed Hugo'

the click the green triangle next to  the runner to start it.

Once the site is running, you can open it at:

<http://localhost:1313>

The site will automatically refresh any page you have open if you edit it and save your work. Magical eh?

## Running End to End (e2e) Tests

Test files are located in ```test/e2e```.

You need to have these extras installed:

```
pip install pytest pytest-base-url playwright
```

These tests exist to make sure code changes to this repository do not break how the site currently functions.
They are intended to run on each commit to verify the site is working in expected order.

Read more on testing [here](https://github.com/qgis/QGIS-Hugo/blob/main/playwright/ci-test/README.md).

### Running as github action

There is a github action that will run the tests automatically on PR submission, merge.

See ```.github/workflows/playwright-e2e.yml```

## Content Harvesting

You can harvest data from various feeds using the fetch_feeds.py script. By default
flickr harvesting is disabled in this script so run it manually and review the content
to see if it is suitable for publication on our site.

```bash
./fetch_feeds.py --flickr=yes
```

This script is run nightly as a github action (see .github/workflows/update-feeds.yml).

## Search Functionality 
The search functionality uses both [FuseJS](https://fusejs.io/) and [MarkJS](https://markjs.io/).

The search functionality code is based on this [Blog Post](https://makewithhugo.com/add-search-to-a-hugo-site/) and [GitHub Gist](https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae) by [Eddie Webb](https://twitter.com/eddturtle).

Content folders need to be excluded from search, by making them [headless bundles](https://gohugo.io/content-management/page-bundles/#headless-bundle) - which we have done for the sustaining member and flagship user folders in content/. To make other content folders which are not rendered and included in search results, add an ```index.md``` file with the following content: ```headless = true```.

## Referencing URLs in templates

The site needs to work in production, where the links of the site are all below the root URL, and in staging, where the site is deployed to GitHub pages in a subpath. To ensure both deployment strategies work, please use the following method of constructing URLs in templates.

```html
<a class="button is-primary" href="{{ "donate/" | absURL }}">
```

**Note:** We do not use a leading slash, only an ending slash.

## 📁 File naming conventions

* Separate words in file names with hyphens e.g. windows-download.md
* Avoid abbreviations in the words of your files
* Write file names in lower case only
* No spaces in file names

## 🤝 Contributing to this project

We welcome your contributions! All contributors are expected to sign a contributor license agreement (CLA) which you can see [here](https://gist.github.com/timlinux/cc20c0b8860648da977a261d46b170d4). This process is automatically enabled when you create your first pull request via https://cla-assistant.io/.

[![CLA assistant](https://cla-assistant.io/readme/badge/qgis/QGIS-Hugo)](https://cla-assistant.io/qgis/QGIS-Hugo)

## 💮 Changing the templates

| Page type       | Path                                     |
| --------------- | ---------------------------------------- |
| Landing Page    | themes/qgis/layouts/index.html           |
| Top Level Pages | themes/qgis/layouts/_default/single.html |

## 🏠 Editing the landing (home) page

The ``content/_index.md`` is the content for the landing page. Just edit whatever you like there. The blocks shortcodes are described below.

## 📃 Adding a top level page

### Create the content

Content pages are stored in the ``content`` folder. The top level documents there will be rendered with the top level page theming.

For example to add an about page, create ``content/about.md``

The page will be accessible then at /about/

### 🖼️ Referencing Images and Media

Place images and media in ```static/img```. Everything in ```static``` is referenced
from the top level of the site e.g.  ```static/img/foo.png``` would be referenced in
markdown as ```/img/foo.png```.

## 📦 Blocks Shortcodes

The site uses a number of shortcodes to create reusable blocks of content. These are defined in the ```themes/hugo-bulma-blocks-theme/layouts/shortcodes/``` folder.

<!-- 3rd level header with icon with title Reusable header web component -->
### Reusable header web component

TODO

### Sidebar

Sidebar is implemented in themes/hugo-bulma-blocks-theme/layouts/partials/sidebar.html

Items are retrieved from config.toml under `[menu]` section. `weight` parameter defines the order of the item.

To enable sidebar on the content page, use the following template:

```
---
type: "page"
...
sidebar: true
---
{{< content-start  >}}

... add content here ...

{{< content-end  >}}
```

### LT/LTR release variables

Script for parsing release schedule from the google spreadsheet is scripts/update-schedule.py. It creates data/conf.json with variables that can be used later in md/html.

Example usage in md:

```
Here you will simply install the latest stable QGIS ({{< param "version" >}}.x {{< param "codename" >}}) 
```

To include param as link, use `param-link` shortcode: it correctly renders as md link, and not as plain text

```
Electronic document: {{< param-link "userguidecite" >}}
```

Example usage in HTML:

to use params inside shortcode or partial, use wrapper:

```
{{ with index .Site.Data.conf }}
...
<a
	class="button is-primary1 mb-3"
	href="{{ .ltr_msi }}"
	onclick="thanks(this)"
	download
>Long Term Version for Windows ({{ .ltrversion }} {{ .ltrnote }})</a>

{{ end }}
```

## URL mapping from old site structure

This table represents required redirects from old URL structure to the new one:
https://docs.google.com/spreadsheets/d/12Oo761Zwgj4iLeJxdrg8I31rGzsB95z5M1PpW9pYma8/edit?usp=sharing

## Stripe donations

main donation page: [https://qgis.github.io/QGIS-Hugo/funding/donate/](https://qgis.github.io/QGIS-Hugo/funding/donate/)

Stripe widget can be included to any page with the shortcode `{{<stripe-widget>}}`

Payment options are implemented with [Payment Links](https://docs.stripe.com/no-code/payment-links). Values and links can be updated in data/stripe_products.yml

## Auto-checking for broken links

```
docker run --rm dcycle/broken-link-checker:3 https://qgis.github.io/QGIS-Hugo > broken_links.csv
```

Crawls the site and reports all 404
