# QGIS Hugo Website

By Tim Sutton and QGIS Contributors.

Read [this article](https://cloudcannon.com/blog/the-ultimate-guide-to-hugo-sections/) on templates if you are looking to understand how templates work.

This theme uses the Bulma CSS framework,

## Installation

Navigate to your development directory

```
git clone https://github.com/qgis/qgis-hugo.git
```

## Development

First install hugo for your local machine:

Linux: ``sudo apt install hugo``

Windows: [Follow these notes](https://gohugo.io/installation/windows/)

MacOS: [Follow these notes](https://gohugo.io/installation/macos/)

If you are using VSCode, I recommend the following extensions:

* Hugo Language and Syntax Support

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

## Changing the templates

Page type | Path
----------|---------------
Landing Page | themes/qgis/layouts/index.html
Top Level Pages | themes/qgis/layouts/_default/single.html

## Editing the landing page

The ``content/_index.md`` is the content for the landing page. Just edit whatever you like there. The blocks shortcodes are described below.

## Adding a top level page

Content pages are stored in the ``content`` folder. The top level documents there will be rendered with the top level page theming.

For example to add an about page, create ``content/about.md``

The page will be accessible then at /about/

## Modifying the menu

The menu is implemented in ```themes/qgis/layouts/partials/menu.html```.

## Working with blocks

The different types of blocks we use are defined in ```themes/qgis/layouts/shortcodes```. The main shortcodes you will use are the ones starting with ```block```. To use a block, simply add it to your markdown as per this example:

```
{{< block-title-left
    title="Block with more content"
    subtitle="Unleash your creativity and experience first class cartographic design capabiliities and design great maps for digital and print. "
    text-color="white"
    background-color="teal"
>}}
```

If you want to include markdown content inside the block you can do it as inner content like this:

```
{{< block-title-left
    title="Block with more content"
    subtitle="Unleash your creativity and experience first class cartographic design capabilities and design great maps for digital and print. "
    text-color="white"
    background-color="teal"
>}}
More details khdkjhksj dhjfhs dkj hsfdjkh fsd
{{< /block-title-left >}}
```

The options for a block are:

Name | Description
-----|-------------
title | Title for the block
subtitle | Subtitled for the block
text-color | Use a CSS colour e.g. white or #FFFFFF
background-color | Use a CSS colour e.g. white or #FFFFFF
image | Place your images into static/img and then references it like this "/img/some-image.png"

## Customising CSS

Put your customizations in ```themes/qgis/assets/css/custom.css```.

We use a hugo minification and combining  workflow - see the header layout in ´´´themes/qgis/layouts/partials/header.html´´´.

## Custom
