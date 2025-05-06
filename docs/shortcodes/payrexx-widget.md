```
{{< payrexx-widget >}}

or 

{{< payrexx-widget otherMethods="true">}}
```

Inserts a donation form integrated with Payrexx. Donate options are controlled by data/payrexx_products.yml

![](img/payrexx-widget.png)

Used inside `rich-right` block:

```
{{< rich-right-start >}}
{{< payrexx-widget otherMethods="true">}}
{{< rich-right-end >}}
```

`otherMethods="true"` inserts the link to /funding/donate/ page

![](img/payrexx-widget-1.png)
