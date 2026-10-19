# Edit the local user groups

This page is for anyone who looks after the QGIS local user groups. It shows you how to add, change or remove a group.

Two things make up a group, and a pull request that adds or removes one touches both:

| | |
|---|---|
| The entry | One block in [`data/user_groups/groups.json`](../data/user_groups/groups.json) |
| The logo | One file at `static/img/user-groups/<id>.webp` |

Everything else is worked out for you after the merge: the country name, the continent, the point on the map, and the data the [list](https://qgis.org/community/groups/list/) and the [map](https://qgis.org/community/groups/map/) read. **Never edit `static/data/user_groups/user_groups.json`, and never run a build to update it.** A workflow does that on its own once your change is merged.

There are two ways to work. Doing it on your computer is easier, because both files land in one commit. The GitHub website works too and needs nothing installed, but your change arrives in two commits and you have to put the second one on the same branch.

## Add a group

### On your computer

1. Fork the repository, clone it, and make a branch: `git switch -c add-qgis-ke`.
2. Choose the group's id. It is `qgis-` and the country code in lower case, for example `qgis-ke`. It names the logo file and the group's link on the site, so pick it before anything else and do not change it later.
3. Prepare the logo. Resize it so the longest side is 256 pixels or less, and save it as WebP under 200 KB. SVG is not accepted, because an SVG file can carry code. With no image editor, open [Squoosh](https://squoosh.app), drag the logo in, choose **WebP** on the right, tick **Resize**, set the longest side to 256, then download.
4. Save it as `static/img/user-groups/qgis-ke.webp`, using the id from step 2.
5. Open `data/user_groups/groups.json`. Copy an existing group from its `{` to its `}`, paste it after the last one, and put a comma between them. Change the fields, as the table below explains.

   ```json
   {
     "id": "qgis-ke",
     "name": "QGIS Kenya",
     "country": "KE",
     "website": "https://qgis.or.ke",
     "year": 2017,
     "contacts": ["Benard Mitto"],
     "removed": null
   }
   ```

6. Check your work: `pip install -r REQUIREMENTS.txt`, then `python scripts/update_user_groups.py --check`. It reports anything wrong in plain words. This is optional, because the same check runs on your pull request.
7. Commit both files together and open the pull request.

### On the GitHub website

The website commits one file at a time, so this takes two commits. The first makes your branch, and **the second has to go on that same branch**, otherwise you end up with two separate pull requests and the check fails on each.

1. Choose the id and prepare the logo as in steps 2 to 4 above, so you have a file named `qgis-ke.webp`.
2. Open [`data/user_groups/groups.json`](https://github.com/qgis/QGIS-Website/blob/main/data/user_groups/groups.json) and select the pencil icon. GitHub forks the repository for you if you need it.
3. Add your entry, using the example above.
4. Select **Commit changes**. In the dialog choose **Create a new branch for this commit and start a pull request**, name the branch something like `add-qgis-ke`, and select **Propose changes**. Then select **Create pull request**.
5. Now add the logo to that same branch. At the top of the repository, open the branch menu, which reads **main**, and pick `add-qgis-ke`. Check the menu now shows your branch name before going on.
6. Open the `static` folder, then `img`, then `user-groups`. Select **Add file**, then **Upload files**, and drag your WebP in.
7. Select **Commit changes**, and this time choose **Commit directly to the `add-qgis-ke` branch**. Do not create another branch.

Your logo joins the pull request you already opened. Check it is there under **Files changed**: you should see both the entry and the image.

## Change a group

Everything here works the same way on your computer or on the website. On the website you are editing files on `main`, so the first change you commit creates a branch, and any further change goes on that branch, as in steps 5 to 7 above.

- **Details, such as the website or a contact:** edit the group's block in `data/user_groups/groups.json`.
- **The logo:** upload the new image over the old one, keeping the same file name. On the website, open `static/img/user-groups`, select **Add file**, then **Upload files**, and drop in a file with the same name.
- **A group that has stopped:** set `"removed"` to the year it stopped, for example `"removed": 2025`. Keep the entry and keep the logo. The group leaves the map and stays on the list for readers who tick **Include groups that are no longer active**.

Do not change a group's `id`. Links to the group and the name of its logo file both use it.

## Remove a group

Removing is for an entry added by mistake. A group that has simply stopped keeps its history, so use `"removed"` above instead.

Delete both parts, in one pull request:

1. Delete the group's block from `data/user_groups/groups.json`, including the comma that separated it from the next one.
2. Delete `static/img/user-groups/<id>.webp`. On the website, open the file and select the bin icon.

If you forget the logo, the check fails with `no group has this id`, which is the reminder to delete it.

## Fields

| Field | Required | Example | What it is |
|---|---|---|---|
| `id` | Yes | `"qgis-ke"` | `qgis-` and the country code in lower case. Names the logo file and the group's link. Never change it once the group is on the site. |
| `name` | Yes | `"QGIS Kenya"` | The group's own name. |
| `country` | Yes | `"KE"` | The two letter country code in capitals ([find a code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). Use `null` for a worldwide group. |
| `year` | Yes | `2017` | The year the group was registered. A number, without quotes. |
| `contacts` | Yes | `["Benard Mitto"]` | One or more names, in square brackets. |
| `website` | No | `"https://qgis.or.ke"` | The full link to the group's website. |
| `removed` | No | `2025` | The year the group stopped. `null` while it is active. |
| `country_name` | No | `"USA"` | Only if the country name we show is wrong for your group. |

A group with no logo file shows the QGIS logo instead, so you can add the entry first and the logo later.

## What happens after you open the pull request

1. A check called **Check user groups** runs. For a first pull request, a maintainer approves the run first.
2. If something is wrong, the check fails. Select **Details**, then **Summary**, to read what to fix, for example "the country must be a two letter code in capitals".
3. When it passes, the summary lists each change. Your logo appears under **Files changed**, exactly as it will look on the site.
4. A maintainer reviews and merges your pull request.
5. A workflow then regenerates the list and map data, commits it, and the website updates within a few minutes. Nothing for you to do.

## For maintainers

| File | Edited by | Purpose |
|---|---|---|
| `data/user_groups/groups.json` | People | The source: one small entry per group |
| `static/img/user-groups/<id>.webp` | People | One logo per group, added in the pull request. Checked, never rewritten |
| `static/data/user_groups/user_groups.json` | Workflow | GeoJSON read by the list, map and landing page. Published at `/data/user_groups/user_groups.json` for anyone to reuse |
| `data/user_groups/countries.json` | Workflow | Country outlines, names, continents and label points from Natural Earth (public domain). Embedded in the map page, not published as a file |

| Workflow | Runs on | Does |
|---|---|---|
| `.github/workflows/check-user-groups.yml` | Pull requests touching the files above | `python scripts/update_user_groups.py --check`. Read only token, no secrets, writes nothing, makes no network request. |
| `.github/workflows/update-user-groups.yml` | Pushes to `main` touching the files above, or by hand | `python scripts/update_user_groups.py`, commits the result, then starts the Pages deploy. |

The generated files are rebuilt only on `main`, never in a pull request. That is on purpose: a contributor should never have to run the script or commit generated data. Nothing in the test suite compares `groups.json` with the generated GeoJSON, because on a pull request they are out of step by design.

Direct pushes to `main` take the same build path. If the source file is invalid, the build fails without committing, and its summary says why.

Other projects can reuse the groups: [`https://qgis.org/data/user_groups/user_groups.json`](https://qgis.org/data/user_groups/user_groups.json) is a GeoJSON FeatureCollection with one point per group, plus the name, country, continent, website, year, contacts, status and logo path.

Everything for the user groups lives in this repository, not in the theme submodule. Files at the same path as a theme file override it, so changing them never needs a theme pull request.

| Path | What it is |
|---|---|
| `layouts/shortcodes/user-groups-list.html`, `user-groups-stats.html`, `user-groups-map.html` | The list, the landing page counts and the map |
| `layouts/partials/user-group-*.html`, `user-groups-data.html`, `user-groups-edit-button.html` | Cards, table rows, flag, data loading and the "Suggest a change" button |
| `assets/js/user-groups-map.js`, `assets/js/globe-flat-map.js` | The map, and the globe and Equal Earth flat map base it shares with the contributors map |
| `assets/sass/user-groups.sass`, `assets/sass/maps.sass` | Styles for the user groups pages, and the shared map styles |
| `layouts/shortcodes/contributors-map.html`, `assets/js/contributors-map.js`, `assets/js/contributors-filter.js` | Override the theme files of the same name: the contributors map on the shared map base, and the list filter both lists use |

To run it yourself from the project root:

1. Run `pip install -r REQUIREMENTS.txt`.
2. Run `python scripts/update_user_groups.py --check` to validate, or `python scripts/update_user_groups.py` to build.
3. Run `pytest test/test_update_user_groups.py`.

A group's map point is its country's label point from Natural Earth, a point inside the main landmass. Groups in the same country share it, and the map shows their logos side by side.

Both flat maps, user groups and contributors, use the Equal Earth projection, so countries keep their true relative size. It lives in `equalEarthProjection()` in `assets/js/globe-flat-map.js`, with no extra library.
