QGIS Hugo Website
===============

By Tim Sutton and QGIS Contributors.

Read [this article](https://cloudcannon.com/blog/the-ultimate-guide-to-hugo-sections/) on templates if you are looking to understand how templates work.

This theme uses the Bulma CSS framework,

### Installation

Navigate to your development directory

```
git clone https://github.com/qgis/qgis-hugo.git
```

# Development

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

Press Ctl-Shift-D then choose the following runner:

'Run dev using locally installed Hugo'

the click the green triangle next to  the runner to start it.

# Changing the templates

Page type | Path
----------|---------------
Landing Page | themes/qgis/layouts/index.html
Top Level Pages | themes/qgis/layouts/_default/single.html

# Editing the landing page

The ``content/_index.md`` is the content for the landing page. Just edit whatever you like there. The blocks shortcodes are described below.

# Adding a top level page

Content pages are stored in the ``content`` folder. The top level documents there will be rendered with the top level page theming.

For example to add an about page, create ``content/about.md``

The page will be accessible then at /about/
