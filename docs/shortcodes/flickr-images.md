## Flickr Images Shortcode

![flickr.png](img/flickr.png)

The flickr-images shortcode allows you to display images fetched from content/flickr-images directory, with customizable parameters to control the showcase type, quantity, and layout.

### Parameters

- **showcase:** (Optional) Specifies the type of showcase to display. Can get `map` or `screenshot` values. Defaults to an empty string.
- **quantity:** (Optional) Specifies the maximum number of images to display. Defaults to "100".
- **columns:** (Optional) Specifies the layout of the images. If set to `gallery`, it displays 2 images on the first row and 3 images on the second row. If set to a numeric value (e.g., `6` for half-width), it determines **how many columns you want out of 12** on the available width.

### Example Usage

To use the flickr-images shortcode, include the desired parameters within the shortcode tag as follows:

```html
{{< flickr-images showcase="showcase-type" quantity="100" columns="gallery" >}}
```
This will fetch images from Flickr based on the specified showcase type, limiting the display to 100 images and arranging them in a gallery layout.

### Additional Notes
- Ensure that the "showcase" parameter matches the desired showcase type configured in your Flickr images collection.
- Adjust the "quantity" parameter as needed to limit the number of images displayed.
- Customize the "columns" parameter to control the layout of the images, either as a gallery or based on specific column widths.


