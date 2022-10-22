QGIS Hugo Theme
========

Modifications by Tim Sutton and QGIS Contributors.

This is a fork of the [purehugo project](http://dplesca.github.io/purehugo/) (thanks!)

Hugo theme based on [purecss](http://purecss.io/) from Yahoo. The theme is based on [the purecss blog layout example](http://purecss.io/layouts/blog/), is responsive and has a few more features: pagination (if enabled), responsive images (through a shortcode), disqus comments and even a mini-asset-pipeline using gulp. If you end up using it, I'd love to see what you do with it so please give me a shout on [twitter](https://twitter.com/dragos_plesca).

### Installation

Navigate to your Hugo site's theme folder

```
cd themes
git clone https://github.com/dplesca/purehugo.git
```

### Config file

The config file for the demo site looks like this:

```toml
baseurl = "http://qgis.org"
languageCode = "en-us"
title = "QGIS.ORG"
theme = "qgis"
Paginate = 10
disqusShortname = "xxxx"

[params]
  twitterName = "qgis"
  githubName = "qgis"
  stackOverflowId = "###"
  linkedinName = "qgis"
  description = "QGIS Website Theme"
```

Notice the configuration necessary for disqus comments (just setting the disqusShortname); the twitter, github, stack overflow and linkedin handlers (for the site footer); the site description and enabling social links reporting.

### Responsive Images

For responsive images you could use the built-in responsive image shortcode (without the `/**/` characters):  

```
{{%/* img-responsive "http://example.com/image.jpg" */%}}
```

### Hide Share Options

If you would like to hide the share options in the single post view, you can add this option in the `params` section of your config file.

```toml
[params]
  # ... other options ...
  hideShareOptions = true
```

### Hide footer icons text Options

If you would like to hide the text next to the icons on the footer, you can add this option in the `params` section of your config file.

```toml
[params]
  # ... other options ...
  hideFooterIconText = true
```

### Screenshot

![Screenshot](https://i.imgur.com/Dsj41Rz.png)
