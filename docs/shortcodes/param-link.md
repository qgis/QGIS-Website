## `param-link` Shortcode

The `param-link` is different from `param` in a way that it applies `| markdownify` to its content. So the plain-text links will be rendered as clickable `<a>` tags

### Parameters

- `name`: The name of the configuration parameter to retrieve.

### Example Usage

```
Electronic document: {{< param-link "userguidecite" >}}
```

^ will be rendered like `Electronic document: [https://docs.qgis.org/3.34/en/docs/developers_guide/index.html](https://docs.qgis.org/3.34/en/docs/developers_guide/index.html)`

### Additional Notes
Make sure that the parameter you are trying to access exists in the data/conf.json.

Also see notes about automation of LT/LTR variables in the root README
