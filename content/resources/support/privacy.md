---
type: "page"
title: "Privacy Policy"
subtitle: ""
draft: false
sidebar: true
---

{{< content-start>}}

# Our Privacy Policy

## QGIS Feed and Analytics Dashboard
The **QGIS Feed Analytics Dashboard** ([https://analytics.qgis.org](https://analytics.qgis.org)) collects minimal, non-identifiable usage data to help improve the QGIS project. When QGIS checks for news updates from the [QGIS Feed Website](https://feed.qgis.org), the following information is recorded:

- **Date of request** (rounded to the nearest day)
- **QGIS version** in use
- **User's country** (determined from the IP address, which is immediately discarded)
- **Operating system platform**

No persistent or personally identifiable information is stored or shared. The IP address is used only to determine the country and is not retained. Data is aggregated hourly into summary tables by date, country, QGIS version, and platform. This helps the QGIS team understand usage patterns and prioritize development efforts.

**Participation is optional:** Users can disable the news feed feature in QGIS at any time.

For questions or concerns, please contact the QGIS Project Steering Committee at [info@qgis.org](mailto:info@qgis.org).

## QGIS Plugins Analytics
The QGIS Plugins Analytics service ([https://plugins-analytics.qgis.org](https://plugins-analytics.qgis.org)) collects minimal, non-identifiable data whenever a plugin is downloaded from the QGIS Plugins Manager or the [QGIS Plugins Website](https://plugins.qgis.org). The following information is recorded:

- **Date of download** (rounded to the nearest day)
- **Plugin version** downloaded
- **User's country** (determined from the IP address, which is immediately discarded)

No persistent or personally identifiable information is stored or shared. The IP address is used only to determine the country and is not retained.

- **Download activity** has been recorded since **16 July 2024**
- **Per-country statistics** have been collected since **30 May 2024**

Plugin popularity is calculated using the formula:

```
downloads * (1 + (rating_score / (rating_votes + 0.01) / 3))
```

This data helps the QGIS team understand plugin usage and improve the plugin ecosystem.

For any questions or concerns, please contact the QGIS Project Steering Committee at [info@qgis.org](mailto:info@qgis.org).


{{< content-end >}}