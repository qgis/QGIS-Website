# Edit the project organisation page

This page is for anyone who keeps the [project organisation page](https://qgis.org/community/organisation/) up to date. It shows you how to add a person to a section, change a role and end one.

The page text lives in [`content/community/organisation.md`](../content/community/organisation.md). The people live in [`data/organisation/`](../data/organisation/), with one file per group. Each file holds the lists that the page shows as cards.

| File | Lists | Section on the page |
|---|---|---|
| `board.json` | `members` | Board |
| `psc.json` | `members`, `honorary`, `former` | Project Steering Committee, Honorary PSC Members, Former PSC Members |
| `voting_members.json` | `honorable`, `community`, `osgeo` | Honorable, Community and OSGeo Voting Members |
| `release_team.json` | `manager`, `packaging`, `testing` | Release Management, Packaging Team, Testing Team |
| `community_team.json` | `leaders`, `translation`, `press` | Community Resources, Translation, Press Material |

The page shows each list with one line, for example `{{< organisation-members group="psc" list="former" >}}`. A person with roles in several sections has an entry in each of those lists.

## How the badges work

Every card shows the section's badge first, in green. The person's roles follow, with one badge for each role and its dates.

In the voting member lists, a member with a known date has one `Voting member` role with that date. A member with no known date has no `roles`, and the card shows only the section badge.

```json
"community": {
  "badge": "Community voting member",
  "people": [
    { "name": "Martin Dobias", "github": "wonder-sk", "country": "Slovakia" },
    { "name": "Lova Andriarimalala", "github": "Xpirix", "country": "Madagascar", "roles": [{ "role": "Voting member", "since": "2026" }] }
  ]
}
```

| List field | What to write |
|---|---|
| `badge` | The section name, shown first on every card in the list |
| `people` | The people in the list, in the order of their cards |

## Add a person to a section

1. Open the file for the group, for example `data/organisation/release_team.json`.
2. Find the list for the section, for example `testing`.
3. Add an entry to its `people`, at the place where you want the card to appear.

   ```json
   { "name": "Lova Andriarimalala", "github": "Xpirix", "roles": [{ "role": "Windows", "since": "2026" }] }
   ```

| Field | What to write |
|---|---|
| `name` | The full name, as the person writes it. This field is required. |
| `github` | The GitHub login. The card links to the profile and shows its picture. Leave it out if the person has no account. |
| `avatar` | A picture under `static/`, for example `img/contributors/supporting/tim_sutton.png`. It replaces the GitHub picture. |
| `country` | The country in English, for example `Portugal`. The community voting members use it. |
| `roles` | One badge per role, after the section badge. Each role has a `role` text and can have a `since` and an `until`, for example `"since": "9.2013"`. Keep the role text to two or three words so it fits on the badge, and put anything longer in `note`. |
| `note` | One short line above the badges, for example `Suspended while serving as a PSC member`. |

With no `github` and no `avatar`, the card shows the person's initials. People listed in `data/contributors/honorary_members.json` get their crown or star on every card, as on the contributors page.

## End a role

Add `until` to the role, for example `"until": "2026"`. The badge turns grey and shows the dates.

When someone leaves the PSC, move their entry from the `members` list to the `former` list in `psc.json`, and add `until` to each role.

## Check your change

1. Run `hugo server` from the project root.
2. Open http://localhost:1313/community/organisation/ and find the card.
3. Run the tests for this page: `cd playwright/ci-test && npx playwright test tests/12-organisation.spec.ts`.

If the page asks for a list that is not in the file, or a list with no `people`, the build stops. The error names the file and the list.
