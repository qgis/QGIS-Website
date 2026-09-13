---
type: "page"
title: "Add Your Organization to QGIS Contributors"
draft: false
HasBanner: false
sidebar: true
---

{{< content-start >}}

# Add Your Organization to QGIS Contributors

Welcome! If your organization contributes to QGIS, you can be featured on our [contributors page](/community/contributors/). Follow these simple steps:

---

## Step 1: Prepare Your Organization Details

### What You'll Need:
- ✅ Your organization's name, tagline, and website URL
- ✅ A brief description of your QGIS involvement
- ✅ GitHub usernames of team members who contribute to QGIS
- ✅ Your organization's logo (PNG or SVG, optimized for web)

---

## Step 2: Fill Out the Template

Copy and customize this template with your organization's information:

```
{
  "name": "Your Organization Name",
  "subtitle": "Your tagline or motto",
  "image": "img/contributors/your-logo.png",
  "width": "200px",
  "url": "https://your-website.com",
  "description": "Brief description of your organization and how you contribute to QGIS.",
  "members": [
    {
      "username": "github_username",
      "author_names": "Full Name",
      "from": "2020-01-15",
      "to": null
    }
  ],
  "contributions": {
    "documentation": { "commits": 0, "last_contribution": null },
    "qgis_core": { "commits": 0, "last_contribution": null },
    "web_sites": { "commits": 0, "last_contribution": null }
  }
}
```

### Field Guide:

| Field | Description | Example |
|-------|-------------|---------|
| **name** | Your organization's full name | `"Kartoza"` |
| **subtitle** | Short tagline or motto | `"Mapping the Future"` |
| **image** | Logo filename (add to `static/img/contributors/`) | `"img/contributors/kartoza-logo.png"` |
| **width** | Logo display width | `"200px"` (keep as is) |
| **url** | Your website | `"https://kartoza.com"` |
| **description** | Brief description (2-3 sentences) | `"Kartoza provides open-source GIS solutions..."` |
| **members** | GitHub usernames of your team members | See below |
| **contributions** | Leave as is—auto-updated by scripts | Keep zeros and null values |

### Members Array Explained:
- **username**: GitHub username (must match exactly)
- **author_names**: Full name as it appears in Git commits. `"Jean Luc"` or `"Jean Luc,Jean Lucas"` for multiple names.
- **from**: Date when this person started contributing for your org (YYYY-MM-DD)
- **to**: Leave as `null` if still active, or add end date (YYYY-MM-DD)

💡 **Tip:** You can add multiple members—just duplicate the member object for each person.

---

## Step 3: Submit via GitHub Pull Request

### Option A: Use GitHub's Web Editor (Easiest)

1. **Click here to edit the file directly:** [Edit organizations.json](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - GitHub will automatically fork the repository for you
2. **Scroll to the bottom** of the file
3. **Add a comma** after the last `}` of the previous entry
4. **Paste your organization entry** (from Step 2)
5. **Click "Commit changes"** and provide a description like: *"Add [Your Org Name] to contributors"*
6. **Create a Pull Request** by clicking the green button

### Option B: Fork and Clone (For Advanced Users)

1. Fork the [QGIS-Website repository](https://github.com/qgis/QGIS-Website/)
2. Clone your fork locally
3. Add your entry to `data/contributors/organizations.json`
4. Add your logo to `static/img/contributors/` (optimize file size!)
5. Commit and push your changes
6. [Open a Pull Request](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **Important:** Make sure your JSON is valid! Use a [JSON validator](https://jsonlint.com/) if needed.

---

## Step 4: Add Your Logo

Upload your logo to the `static/img/contributors/` folder:
- **Format:** PNG or SVG
- **Size:** Optimize for web (aim for under 100KB)
- **Dimensions:** Width around 400-600px works well
- **Naming:** Use lowercase and hyphens (e.g., `acme-geospatial.png`)

---

## Step 5: Review & Approval

✨ Once you submit your Pull Request:
1. The QGIS website team will review your submission
2. We may ask for minor adjustments
3. Once approved and merged, your organization will appear on the [contributors page](/community/contributors/)!

---

Thank you for contributing to QGIS! 🎉

{{< content-end >}}