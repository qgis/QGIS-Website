## `roadmap` Shortcode

![](img/roadmap.png)

The `roadmap` shortcode is used to create a visual representation of a project's roadmap, including various phases such as initial release, point releases, packaging, and availability of installers. It also includes a JavaScript countdown functionality for each phase.

### Parameters

- No parameters are directly passed to this shortcode. Instead, it uses predefined IDs to manage the roadmap and countdown elements.

### Example Usage

The `roadmap` shortcode is typically used as a standalone element and does not require parameters to be passed. It is structured with `steps-segment` and `steps-content` classes to define each phase of the roadmap.

```html
{{< roadmap >}}
```

This will generate a roadmap with the phases and countdown timers as defined in the HTML structure.

### JavaScript Functionality
The roadmap includes a JavaScript countdown timer for each phase. The countdown is initialized with a deadline, and the initializeClock function updates the days, hours, minutes, and seconds for each phase until the deadline is reached.

### Additional Notes
The roadmap is divided into segments, each with a steps-marker and steps-content to describe the phase.
Tooltips (help-tip) provide additional information about each phase.
The JavaScript code for the countdown timer should be included at the bottom of the HTML file where the roadmap is used.
The IDs point-release, freeze, and package are used to initialize the countdown timers for the respective phases.