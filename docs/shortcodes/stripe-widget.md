```
{{< stripe-widget >}}

or 

{{< stripe-widget otherMethods="true">}}
```

Inserts a donation form integrated with Stripe. Donate options are controlled by data/stripe_products.yml

![](img/stripe-widget.png)

Used inside `rich-right` block:

```
{{< rich-right-start >}}
{{< stripe-widget otherMethods="true">}}
{{< rich-right-end >}}
```

`otherMethods="true"` inserts the link to /funding/donate/ page

![](img/stripe-widget-1.png)
