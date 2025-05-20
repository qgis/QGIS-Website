## csv-table

Renders an HTML table from a CSV file.

```
{{< csv-table file="csv/schedule.csv" >}}
```

![](img/csv-table.png)

For simple tables, standard Markdown tables should be used:

```markdown
| Abbreviation | Description |
|-------------|-------------|
| LTR | Long term release, begin of new development phase |
| LR | Regular release, begin of new development phase |
| FF | Feature freeze, end of development phase |
| PR | Point release of latest release and LTR branch |
| EPR | Extra Point release |
| :rm-current:current | :rm-current:currently supported releases: {{< param "ltrrelease" >}} and {{< param "release" >}} |
| :rm-next:next | :rm-next:next releases |
```

Note: Hugo shortcode `param` can be used inside markdown tables to substitute dynamic vars: `{{< param "ltrrelease" >}}`

`:rm-next:`, `:rm-current:`, etc. are transformed into CSS classes from themes/hugo-bulma-blocks-theme/assets/sass/bulma/components/roadmap.sass. These are used for styling roadmap tables.
