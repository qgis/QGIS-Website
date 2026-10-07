# Edit the local user groups

This page is for anyone who looks after the QGIS local user groups. It shows you how to add, change or retire a group using only the GitHub website. You need a GitHub account, and nothing to install.

Everything on the [list](https://qgis.org/community/groups/list/) and the [map](https://qgis.org/community/groups/map/) comes from one file: [`data/user_groups/groups.json`](../data/user_groups/groups.json). You edit that file. A workflow does the rest: it finds the country name and continent, places the group on the map, and downloads, checks and converts the logo.

## Add a group

1. Open [`data/user_groups/groups.json` on GitHub](https://github.com/qgis/QGIS-Website/blob/main/data/user_groups/groups.json).
2. Select the pencil icon to edit the file. GitHub makes a copy for you if you need one.
3. Copy an existing group, from its `{` to its `}`, and paste it after the last group.
4. Add a comma between the previous group's `}` and your new `{`.
5. Change the fields, as the table below explains. Leave out `id` for a new group.
6. Select **Commit changes**, then **Propose changes**, then **Create pull request**.

Here is a complete new group:

```json
{
  "name": "QGIS Kenya",
  "country": "KE",
  "website": "https://qgis.or.ke",
  "year": 2017,
  "contacts": ["Benard Mitto"],
  "logo_url": "https://qgis.or.ke/images/qgiskenya_logo.png",
  "removed": null
}
```

## Change or retire a group

1. Open the file and select the pencil icon, as above.
2. Find the group and change what you need.
3. To retire a group, set `removed` to the year it stopped, for example `"removed": 2025`. The group leaves the map and stays on the list for readers who ask to see inactive groups.
4. Propose the change and open the pull request.

Do not change a group's `id`. Links to the group and its logo use it.

## Fields

| Field | Required | Example | What it is |
|---|---|---|---|
| `name` | Yes | `"QGIS Kenya"` | The group's own name. |
| `country` | Yes | `"KE"` | The two letter country code in capitals ([find a code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). Use `null` for a worldwide group. |
| `year` | Yes | `2017` | The year the group was registered. A number, without quotes. |
| `contacts` | Yes | `["Benard Mitto"]` | One or more names, in square brackets. |
| `website` | No | `"https://qgis.or.ke"` | The full link to the group's website. |
| `logo_url` | No | `"https://qgis.or.ke/logo.png"` | A link to the logo image itself, not to a web page. |
| `removed` | No | `2025` | The year the group stopped. `null` while it is active. |
| `id` | No | `"qgis-kenya"` | Made from the name when you leave it out. Existing groups keep theirs. |
| `country_name` | No | `"USA"` | Only if the country name we show is wrong for your group. |

## Logos

A logo can be a PNG, JPEG, GIF or WebP image, at least 16 pixels wide and high, and under 5 MB. SVG is not accepted, because an SVG file can carry code.

You have two ways to give a logo:

* **A link.** Put the link to the image in `logo_url`. To get it, right click the logo on the group's website and choose to copy the image address.
* **A file.** Upload the image to the [`user-groups-logos`](../user-groups-logos/) folder in the same pull request, named after the group's id, for example `qgis-kenya.png`. A file wins over a link.

We resize every logo to 256 pixels and save it as WebP. When a group has no logo, the QGIS logo is shown.

## What happens after you open the pull request

1. A check called **Check user groups** runs. For a first pull request, a maintainer approves it first.
2. If something is wrong, the check fails. Select **Details**, then **Summary**, to read what to fix, for example "the country must be a two letter code in capitals".
3. When it passes, the summary lists each change. Download **user-group-logo-previews** at the bottom of the summary to see the logos exactly as they will appear.
4. A maintainer reviews and merges your pull request.
5. A workflow builds the data, commits it and updates the website within a few minutes.

If a logo link stops working later, the group keeps its current logo.

## For maintainers

| File | Edited by | Purpose |
|---|---|---|
| `data/user_groups/groups.json` | People | The source: one small entry per group |
| `user-groups-logos/<id>.<ext>` | People | Uploaded logos, removed once converted |
| `static/data/user_groups/user_groups.json` | Workflow | GeoJSON read by the list, map and landing page. Published at `/data/user_groups/user_groups.json` for anyone to reuse |
| `data/user_groups/logos.json` | Workflow | The link each logo was downloaded from, so an unchanged logo is not downloaded again. Not published |
| `data/user_groups/countries.json` | Workflow | Country outlines, names, continents and label points from Natural Earth (public domain). Embedded in the map page, not published as a file |
| `static/img/user-groups/<id>.webp` | Workflow | Converted logos |

| Workflow | Runs on | Does |
|---|---|---|
| `.github/workflows/check-user-groups.yml` | Pull requests touching the files above | `python scripts/update_user_groups.py --check`. Read only token, no secrets, writes nothing. |
| `.github/workflows/update-user-groups.yml` | Pushes to `main` touching the files above, or by hand | `python scripts/update_user_groups.py`, commits the result, then starts the Pages deploy. |

Other projects can reuse the groups: [`https://qgis.org/data/user_groups/user_groups.json`](https://qgis.org/data/user_groups/user_groups.json) is a GeoJSON FeatureCollection with one point per group, plus the name, country, continent, website, year, contacts, status and logo path.

Direct pushes to `main` take the same build path. If the source file is invalid, the build fails without committing, and its summary says why.

To run it yourself from the project root:

1. Run `pip install -r REQUIREMENTS.txt`.
2. Run `python scripts/update_user_groups.py --check` to validate, or `python scripts/update_user_groups.py` to build.
3. Run `pytest test/test_update_user_groups.py`.

A group's map point is its country's label point from Natural Earth, a point inside the main landmass. Groups in the same country share it, and the map shows their logos side by side.

Both flat maps, user groups and contributors, use the Equal Earth projection, so countries keep their true relative size. It lives in `equalEarthProjection()` in the theme's `assets/js/globe-flat-map.js`, with no extra library.
