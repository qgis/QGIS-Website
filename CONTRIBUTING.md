# ✨ Contributing to QGIS-Website

Thank you for considering contributing to QGIS Website!
We welcome contributions of all kinds, including bug fixes, feature requests,
documentation improvements, and more. Please follow the guidelines below to
ensure a smooth contribution process.


![-----------------------------------------------------](./img/green-gradient.png)

## 🏃Before you start

This web site is a static site built using [Hugo](https://gohugo.io/).

![Hugo Logo](./img/hugo-logo.png) and using the [hugo bulma blocks theme](https://github.com/kartoza/hugo-bulma-blocks-theme).


![-----------------------------------------------------](./img/green-gradient.png)

## 🛒 Getting the Code

```
git clone https://github.com/qgis/QGIS-Website.git
cd QGIS-Website
```


![-----------------------------------------------------](./img/green-gradient.png)

## 🧑💻 Development

For Nix based development environment, please skip directly to the [Nix](#nix) section.

First install hugo for your local machine:

**📝 Note:** we need to install the 'extended' hugo version which includes a SASS compiler. If you don't install the extended version you will get errors like this when compiling:

```
ERROR 2022/12/11 07:33:37 Rebuild failed: TOCSS: failed to transform 
"css/style.scss" (text/x-scss). Check your Hugo installation; you need 
the extended version to build SCSS/SASS.: this feature is not available 
in your current Hugo version, see https://goo.gl/YMrWcn for more information
```

Currently, the website requires Hugo with a minimum version of `v0.139.0`. Ensure you have a compatible version installed to avoid any build issues.

You can find the extended version `v0.139.0` [here](https://github.com/gohugoio/hugo/releases/tag/v0.139.0).

![Download](./img/hugo-download.png)

### 🐧 Linux: 

Download the latest version and then do 

``sudo dpkg -i hugo_extended_<latest>_linux-amd64.deb``

**📝 Note:** if your system has another version of Hugo, no need to mess up with docker, snap, nix. Just extract the binaries somewhere with `dpkg -x` .
Example, assuming that you use a dedicated directory for your local binaries :

```sh
mkdir -p ~/apps/hugo_139/
wget https://github.com/gohugoio/hugo/releases/download/v0.139.0/hugo_extended_0.139.3_linux-amd64.deb --output-document ~/apps/hugo_128/hugo_extended_0.139.3_linux-amd64.deb 
dpkg -x hugo_extended_0.139.3_linux-amd64.deb
~/apps/hugo_128/usr/local/bin/hugo server  
```

### 🪟 Windows

[Follow these notes](https://gohugo.io/installation/windows/#prebuilt-binaries)

### 🍏 macOS: 

[Follow these notes](https://gohugo.io/installation/macos/#prebuilt-binaries)

### Nix

Run the following command on this project root folder:

```sh
nix-shell # It will install all the dependecies
hugo server # To run the local server
```


![-----------------------------------------------------](./img/green-gradient.png)

## ⚙️ Setting up VSCode

If you are using VSCode, I recommend the following extensions:

* Hugo Language and Syntax Support
* Color Highlight

Clone the repo:

```
git clone https://github.com/qgis/QGIS-Website.git
```

Run the site:

Press ```Ctl-Shift-D``` then choose the following runner:

'Run dev using locally installed Hugo'

the click the green triangle next to  the runner to start it.

Once the site is running, you can open it at:

<http://localhost:1313>

The site will automatically refresh any page you have open if you edit it and save your work. Magical eh?


![-----------------------------------------------------](./img/green-gradient.png)

## Run in other IDEs

Use an appropriate Hugo plugin for your IDE, or run Hugo från the command line:

```shell
hugo server
```

You can then visit the hot-reloaded site in your browser at `http://localhost:1313/`


![-----------------------------------------------------](./img/green-gradient.png)

## Running Playwright End to End (e2e) Tests

Test files are located in ```playwright/ci-test/tests```.

These tests exist to make sure code changes to this repository do not break how the site currently functions.
They are intended to run on each commit to verify the site is working in the expected order.

### Run tests with VSCode

**Requirements:** NodeJS v18+

1. **Install playwright:** If you haven't already installed Playwright, you can do so by running the following commands in `playwright/ci-test` directory.

```bash
cd playwright/ci-test
npm install
```

2. **Install playwright browsers:**

```bash
npx playwright install --with-deps chromium
```

3. **Install the extension [Playwright Test for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright)**: This extension provides a seamless integration of Playwright testing into VSCode.

![Screenshot](./img/vs_code_playwright_extension.png)

4. **Open the Testing Tab:** In VSCode, click on the Testing icon in the Activity Bar on the side of the window. This will open the Testing tab.

5. **Run Playwright Tests from the Testing Tab:**
- In the Testing tab, you should see your Playwright tests listed. If not, ensure the browser is checked under Playwright > Project menu.
- Click on the refresh button in the Testing tab to reload the tests.
- You can run individual tests by clicking the play button next to the test name.
- You can also run all tests by clicking the play button at the top of the Testing tab.

![Screenshot](./img/vs_code_testing_tab.png)

6. **Debugging Tests:**

- You can debug individual tests by clicking the debug icon (a small bug with a play button) next to the test name.
- Make sure to set breakpoints in your test files before running the debugger.

### Run tests with CLI

By default, this will run in `headless` mode just as it is in CI.

```bash
./run-tests.sh
```

**NOTE:** To run it in `UI` mode, add the `--ui` tag to the script.

```bash
$PLAYWRIGHT \
    test \
    --ui \
    --project chromium
```

Read more on testing [here](https://github.com/qgis/QGIS-Website/blob/main/playwright/ci-test/README.md).

### Running as github action

There is a github action that will run the tests automatically on PR submission, merge.

See ```.github/workflows/playwright-e2e.yml```


![-----------------------------------------------------](./img/green-gradient.png)

## 🤖 Automated Content and Manual Edit Guidelines

**⚠️ IMPORTANT:** Several parts of this website are automatically generated and should **NOT** be edited manually. Manual edits to these files will be overwritten by automation scripts.

### 🚫 Do NOT Edit These Files/Folders Manually

| File/Folder Path | Updated By Script | How to Update Instead |
|------------------|-------------------|----------------------|
| `data/donors.json` | `update_donors.py`, `update_donors_from_file.py` | Use donation scripts or provide donor text files |
| `data/feed.json` | `fetch_feeds.py` | Update the data from https://feed.qgis.org |
| `config/commit.toml` | `get_commit_hash.sh` | Automatically updated on deployment |
| `content/funders/` | `fetch_feeds.py` | Update the data from https://members.qgis.org |
| `content/flickr-images/` | `fetch_feeds.py` | Content imported from Flickr feeds |
| `content/hub-maps/` | `hub_maps_harvest.py` | Update the data from https://maps.qgis.org |
| `content/funding/donate/github-sponsors.md` | GitHub Actions (`update-gh-sponsors.yml`) | ⚠️ **PARTIAL**: Only content outside `<!-- sponsors -->` comments can be edited |

### ✅ How to Properly Update Automated Content

#### 💰 Donors Information
- **Manual donors:** Use `scripts/update_donors_from_file.py <donor_file.txt>`
- **Stripe donors:** Run `scripts/update_donors.py` (requires Stripe API access). Runs nightly via GitHub Actions
- **File format:** Plain text files with donor names

#### 📋 Visual Changelogs
- **Source:** changelog.qgis.org
- **Script:** `scripts/changelog_harvest.py`
- **Manual run:** `./scripts/changelog_harvest.py --version X.XX --release DD.MM.YYYY`
- **Updates after harvesting:** It is allowed to update the content of `content/project/visual-changelogs` with a PR but only when the harvest from https://changelog.qgis.org is done.

#### 🏢 Sustaining Members & News
- **Script:** `fetch_feeds.py`
- **Sources:** External feeds and APIs
- **Schedule:** Runs nightly via GitHub Actions

#### 🗺️ Maps Showcase
- **Source:** maps.qgis.org
- **Script:** `scripts/hub_maps_harvest.py`
- **Schedule:** Runs twice daily via GitHub Actions

#### 💖 GitHub Sponsors
- **Source:** GitHub Sponsors API
- **Workflow:** `.github/workflows/update-gh-sponsors.yml`
- **Schedule:** Runs twice daily via GitHub Actions
- **File:** `content/funding/donate/github-sponsors.md`
- **⚠️ Important:** Only edit content **outside** the `<!-- sponsors -->` comment blocks. The sponsor list between these comments is automatically generated and will be overwritten.

#### 🏢 Commercial Support
- **Validation:** Link checking and cleanup
- **Workflow:** `.github/workflows/check-commercial-support-links.yml`
- **Schedule:** Runs weekly (Sundays) via GitHub Actions

### 🔄 Automation Schedule

| Content Type | Frequency | Method |
|--------------|-----------|--------|
| GitHub Sponsors | Twice daily (midnight & noon UTC) | `.github/workflows/update-gh-sponsors.yml` |
| Stripe Donors | Twice daily (midnight & noon UTC) | `.github/workflows/update-donors.yml` |
| News feeds & Sustaining members | Twice daily (midnight & noon UTC) | `.github/workflows/update-feeds.yml` |
| Hub Maps | Twice daily (midnight & noon UTC) | `.github/workflows/update-feeds.yml` |
| Commercial Support Links | Weekly (Sunday midnight UTC) | `.github/workflows/check-commercial-support-links.yml` |
| Version info | On deployment | Build process |
| Visual Changelogs | Manual/As needed | Local script execution (`changelog_harvest.py`) |

### 🛡️ Protected Content Guidelines

1. **Check file headers:** Auto-generated files contain warning comments
2. **Use scripts:** Always use designated scripts for updates
3. **Verify sources:** Ensure external data sources are accessible
4. **Test locally:** Run scripts locally before committing
5. **Monitor automation:** Check GitHub Actions for feed updates

![-----------------------------------------------------](./img/green-gradient.png)

## Content Harvesting

You can harvest data from various feeds using the fetch_feeds.py script. By default
flickr harvesting is disabled in this script so run it manually and review the content
to see if it is suitable for publication on our site.

```bash
./fetch_feeds.py
```

Flickr parsing creates new files and md pages with param `draft: true`. It can be changed to `false` after manual verification. The script will not overwrite the changes. Pictures with `draft: false` will appear on /project/overview/maps/ and /project/overview/screenshots/.

This script is run nightly as a github action (see .github/workflows/update-feeds.yml).


![-----------------------------------------------------](./img/green-gradient.png)

## Search Functionality 
The search functionality uses both [FuseJS](https://fusejs.io/) and [MarkJS](https://markjs.io/).

The search functionality code is based on this [Blog Post](https://makewithhugo.com/add-search-to-a-hugo-site/) and [GitHub Gist](https://gist.github.com/eddiewebb/735feb48f50f0ddd65ae5606a1cb41ae) by [Eddie Webb](https://twitter.com/eddturtle).

Content folders need to be excluded from search, by making them [headless bundles](https://gohugo.io/content-management/page-bundles/#headless-bundle) - which we have done for the sustaining member and flagship user folders in content/. To make other content folders which are not rendered and included in search results, add an ```index.md``` file with the following content: ```headless = true```.


![-----------------------------------------------------](./img/green-gradient.png)

## Referencing URLs in templates

The site needs to work in production, where the links of the site are all below the root URL, and in staging, where the site is deployed to GitHub pages in a subpath. To ensure both deployment strategies work, please use the following method of constructing URLs in templates.

```html
<a class="button is-primary" href="{{ "donate/" | absURL }}">
```

**Note:** We do not use a leading slash, only an ending slash.


![-----------------------------------------------------](./img/green-gradient.png)

## Styles (SASS/CSS)

SASS for most components is stored in themes/hugo-bulma-blocks-theme/assets/sass/bulma/components/

Some common styles are places in themes/hugo-bulma-blocks-theme/assets/sass/style.sass - this file is compiled as hugo template, hence has access to config.toml variables and hugo macroses

Also some bulma theme overrides are placed in themes/hugo-bulma-blocks-theme/assets/css/custom.css


![-----------------------------------------------------](./img/green-gradient.png)

## 📁 File naming conventions

* Separate words in file names with hyphens e.g. windows-download.md
* Avoid abbreviations in the words of your files
* Write file names in lower case only
* No spaces in file names


![-----------------------------------------------------](./img/green-gradient.png)

## 🤝 Contributing to this project

We welcome your contributions! All contributors are expected to sign a contributor license agreement (CLA) which you can see [here](https://gist.github.com/timlinux/cc20c0b8860648da977a261d46b170d4). This process is automatically enabled when you create your first pull request via https://cla-assistant.io/.

[![CLA assistant](https://cla-assistant.io/readme/badge/qgis/QGIS-Website)](https://cla-assistant.io/qgis/QGIS-Website)


![-----------------------------------------------------](./img/green-gradient.png)

## 💮 Changing the templates

| Page type       | Path                                     |
| --------------- | ---------------------------------------- |
| Landing Page    | themes/qgis/layouts/index.html           |
| Top Level Pages | themes/qgis/layouts/_default/single.html |


![-----------------------------------------------------](./img/green-gradient.png)

## 🏠 Editing the landing (home) page

The layout of the landing page is themes/hugo-bulma-blocks-theme/layouts/index.html: the main page has many diverse blocks, that are not used anywhere else, hence its content is mostly in the partials.

The ``content/_index.md`` contains the front matter of the page and the contents for the `feature` shortcodes. Just edit whatever you like there. The blocks shortcodes are described [here](https://github.com/qgis/QGIS-Website/blob/main/docs/shortcodes.md)


![-----------------------------------------------------](./img/green-gradient.png)

## 📃 Adding a top level page

### Create the content

Content pages are stored in the ``content`` folder. The top level documents there will be rendered with the top level page theming.

For example to add an about page, create ``content/about.md``

The page will be accessible then at /about/

### 🖼️ Referencing Images and Media

Place images and media in ```static/img```. Everything in ```static``` is referenced
from the top level of the site e.g.  ```static/img/foo.png``` would be referenced in
markdown as ```/img/foo.png```.


![-----------------------------------------------------](./img/green-gradient.png)

## 📦 Blocks Shortcodes

The site uses a number of shortcodes to create reusable blocks of content. These are defined in the ```themes/hugo-bulma-blocks-theme/layouts/shortcodes/``` folder.

The shortcodes with screenshots are described [here](https://github.com/qgis/QGIS-Website/blob/main/docs/shortcodes.md)

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

Script for harvesting the visualchangelog from changelog.qgis.org is scripts/changelog_harvest.py. It will create/update a visual-changelogs at content/project/visual-changelogs based on the data at data/conf.json.

Usage:
```
$ ./scripts/changelog_harvest.py

# For a specific version
$ ./scripts/changelog_harvest.py --version 3.34 --release 21.06.2024

# Resizing the images for existing changelog
$ ./scripts/changelog_harvest.py --version 3.34 --release 21.06.2024 --use_existing
```

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

Example usage as shortcode param:

tricky part: shortcodes can't be used as other shortcodes' params. So you need to make replacement in the outer shortcode: "tabs.html" make a replacement of `|ltrversion|` and `|version|` to the values from config.

```
{{< tabs tab1="QGIS |ltrversion|" tab2="QGIS |version|" tab3="QGIS testing (>|ltrversion|)" tab4="Archived releases">}}
```

![-----------------------------------------------------](./img/green-gradient.png)

## URL mapping from old site structure

This table represents required redirects from old URL structure to the new one:
https://docs.google.com/spreadsheets/d/12Oo761Zwgj4iLeJxdrg8I31rGzsB95z5M1PpW9pYma8/edit?usp=sharing

Notes:

- it will be more convenient to store all redirects in same file (nginx conf or else)
- hugo aliases not recommended: they work, but don't support regex. also hard to maintain: redirects are spread across content files
- use regexps to redirect from all langs
- use regexps to map between similar stuff (case studies, visual changelog) - example rewrite rules below

Bulk redirects can be done like

```
map $url $new_url {
  ...
    ^/[A-Za-z-]+/site/about/case_studies/(.*).html /project/case-studies/$1/;
    ^/[A-Za-z-]+/site/forusers/visualchangelog(.*)/index.html /project/visual-changelogs/visualchangelog$1/;
  ^/[A-Za-z-]+/site/forusers/usergroups.html /community/organisation/groups/;
  ...
}
```

See [nginx map tutorial](https://gauravswaroop.medium.com/nginx-bulk-url-redirect-with-map-47c2cd6ad50a) and [examples with regex capture](https://dzone.com/articles/about-using-regexp-in-nginx-map)


![-----------------------------------------------------](./img/green-gradient.png)


## TODO: Payrexx Donation

![-----------------------------------------------------](./img/green-gradient.png)
## Stripe donations

main donation page: [https://qgis.github.io/QGIS-Website/funding/donate/](https://qgis.github.io/QGIS-Website/funding/donate/)

Stripe widget can be included to any page with the shortcode `{{<stripe-widget>}}`

Payment options are implemented with [Payment Links](https://docs.stripe.com/no-code/payment-links). Values and links can be updated in [data/stripe_products.yml](https://github.com/qgis/QGIS-Website/blob/main/data/stripe_products.yml)

**Note**: payment links also support recurring donations (subscriptions) - products with recurrent payments should be created for that matter

### Donors update from a static file
The Donors list stored in data/donors.json can be updated from one or multiple
static txt file using the script `script/update_donors_from_file.py`:

```sh
python scripts/update_donors_from_file.py <path_to_donors.txt> <path_to_donors2.txt> ...
```

### Donors scraping

Is not ported yet. Donors are stored in data/donors.json. [adddonor.pl](https://github.com/qgis/QGIS-Website/blob/master/scripts/adddonor.pl) and related scripts & webhooks should be adapted to the new format

![-----------------------------------------------------](./img/green-gradient.png)

## Auto-checking for broken links

```
docker run --rm dcycle/broken-link-checker:3 https://qgis.github.io/QGIS-Website > broken_links.csv
```

Crawls the site and reports all 404. Full run takes apout 10 mins

