## `param` Shortcode

The `param` shortcode is used to retrieve and display a specific parameter from data/conf.json. This file is in sync with QGIS release schedule and contains variables related to roadmap.

### Parameters

- `name`: The name of the configuration parameter to retrieve.

### Example Usage

```
the latest stable QGIS ({{< param "version" >}}.x {{< param "codename" >}}) 
```

^ will be rendered as `the latest stable QGIS (3.36.x Maidenhead)`

### Additional Notes
Make sure that the parameter you are trying to access exists in the data/conf.json.
This shortcode is useful for displaying dynamic content that is defined in the site's configuration and needs to be consistent across multiple pages.

The shortcode is rendered as plain text. To automatically generate a clickeble link, use `param-link`

Also see notes about automation of LT/LTR variables in the root README
