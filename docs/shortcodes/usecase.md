## `usecase` Shortcode

The `usecase` shortcode is designed to create a rich list item that links to a case study. It includes a thumbnail image, a title, and a short description.

### Parameters

- `thumbnail`: The filename of the thumbnail image to display. The image should be located in the `/product/case-studies/` directory.
- `title`: The title of the case study.
- `description`: A brief description of the case study.

### Example Usage

To use the `usecase` shortcode, you need to pass the `thumbnail`, `title`, and `description` parameters like so:

```html
{{< usecase thumbnail="image.jpg" title="Case Study Title" description="A short description of the case study." >}}
```
This will generate a rich list item with an image, title, and description that links to the specified case study.

### Additional Notes
Ensure that the thumbnail image exists in the specified directory and is accessible.
The title and description should be concise and relevant to the content of the case study they link to.
This shortcode is typically used within a loop to display multiple case studies.