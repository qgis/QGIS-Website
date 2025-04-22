## feature Shortcode

![feature.png](img/feature.png)

The feature shortcode allows you to create visually appealing feature sections with titles, descriptive text, and accompanying images on the main page. 


### Parameters

- **title:** The main title of the feature section.
- **text:** A brief description or overview of the feature.
- **col-title-X:** The title for the Xth column of additional information.
- **col-text-X:** The text content for the Xth column, providing detailed information about the feature.
- **img:** The URL of the image to be displayed alongside the feature.
- **order:** (Optional) Specify the order of the feature section. Use values like `1`, `2`, etc., to determine the layout order.

### Example Usage

To utilize the feature shortcode, include the necessary parameters within the shortcode tag as shown below:

```html
{{< feature
title = "Create maps"
text = "Explore QGIS's exceptional cartographic design features to craft outstanding maps for desktop, mobile, cloud, and print media"
col-title-1 = "Class-leading cartography"
col-text-1 = "Experience QGIS' extensive set of design options to bring"
col-title-2 = "Professional map production"
col-text-2 = "Use the intuitive layout designer to produce high-quality, large-format print maps."
col-title-3 = "Powerful reporting tools"
col-text-3 = "Create atlasses and reports with maps and tabular content."
img = "img/main-create.webp"
order = 1>}}
```

This will generate a feature section with the specified title, description, additional columns of information, and an accompanying image.

### Additional Notes

- Customize the content of each column (`col-title-X` and `col-text-X`) to provide comprehensive details about the feature being highlighted.
- Ensure that the image referenced in the shortcode is accessible and properly sized for display within the feature section.
- Utilize the `order` parameter to control the layout order of the feature sections, especially when multiple feature sections are used within the same page or layout.