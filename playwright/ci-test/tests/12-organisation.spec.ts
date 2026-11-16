import { test, expect, Page } from "@playwright/test";

/**
 * Project organisation: each role list is a set of cards built from data/organisation/*.json.
 */

const lists = [
    ["board", "members"],
    ["psc", "members"],
    ["psc", "honorary"],
    ["psc", "former"],
    ["voting_members", "honorable"],
    ["voting_members", "community"],
    ["voting_members", "osgeo"],
    ["release_team", "manager"],
    ["release_team", "packaging"],
    ["release_team", "testing"],
    ["community_team", "leaders"],
    ["community_team", "translation"],
    ["community_team", "press"],
];

const cards = (page: Page, group: string, list: string) =>
    page.locator(`.organisation-members[data-group="${group}"][data-list="${list}"] [role="listitem"]`);

test.describe("Project organisation", () => {
    test.beforeEach(async ({ page }) => {
        await page.goto("/community/organisation/");
    });

    test("keeps the section anchors", async ({ page }) => {
        const ids = [
            "board",
            "project-steering-committee",
            "honorary-psc-members",
            "former-psc-members",
            "voting-members",
            "community-voting-members",
            "release-management",
            "packaging-team",
            "testing-team",
            "community-resources",
            "translation",
        ];
        for (const id of ids) {
            await expect(page.locator(`:is(h2, h3)#${id}`)).toBeAttached();
        }
    });

    test("shows every role list as cards", async ({ page }) => {
        await expect(page.locator(".organisation-members")).toHaveCount(lists.length);
        for (const [group, list] of lists) {
            expect(await cards(page, group, list).count()).toBeGreaterThan(0);
        }
        // The old bullet lists are gone
        await expect(page.getByText("Added 2017")).toHaveCount(0);
    });

    test("cards show role badges, dates and pictures", async ({ page }) => {
        const chair = cards(page, "board", "members").first();
        await expect(chair.locator(".tag.is-primary3")).toBeVisible();
        await expect(chair).toContainText("Since");

        // Ended roles are muted
        await expect(page.locator('.organisation-members[data-list="former"] .tag.is-primary3')).toHaveCount(0);

        // Without a GitHub account the card shows initials
        const osgeo = cards(page, "voting_members", "osgeo").first();
        await expect(osgeo.locator("img")).toHaveCount(0);
        await expect(osgeo.locator(".avatar")).toHaveText("MS");

        // Honorary members keep their contributor style
        await expect(page.locator('.organisation-members[data-list="honorary"] .honorary-member')).toHaveCount(2);
    });

    test("a person can appear in more than one section", async ({ page }) => {
        expect(await page.getByText("Marco Bernasocchi", { exact: true }).count()).toBeGreaterThan(1);
    });
});
