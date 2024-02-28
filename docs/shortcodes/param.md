## `param` Shortcode

The `param` shortcode is used to retrieve and display a specific configuration parameter from the site's data files.

### Parameters

- `name`: The name of the configuration parameter to retrieve.

### Example Usage

To use the `param` shortcode, you need to pass the name of the configuration parameter as an argument. For example, if you want to retrieve the `email` parameter from the site's configuration:

```html
{{< param "email" >}}
```

This will output the value of the email parameter from the site's configuration data.

### Additional Notes
The configuration parameters are typically stored in the data directory of your Hugo site, in a file named conf.toml, conf.yaml, or conf.json.
Make sure that the parameter you are trying to access exists in the site's configuration data files.
This shortcode is useful for displaying dynamic content that is defined in the site's configuration and needs to be consistent across multiple pages.