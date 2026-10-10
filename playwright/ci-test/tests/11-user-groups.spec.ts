import { test, expect, Page } from "@playwright/test";

/**
 * Local user groups: landing page, list and map.
 *
 * All three pages show data built from data/user_groups/groups.json. The list reuses the
 * contributors filter script (search, continent filters, grid and table,
 * URL state) and the map reuses the shared globe/flat map base class.
 */

const visibleCards = (page: Page) =>
    page.locator(".contributor-card-column:visible");

test.describe("Local user groups", () => {
    test("landing page links to the list and the map", async ({ page }) => {
        await page.goto("/community/groups/");
        await expect(page.getByRole("heading", { name: "Goals of a user group" })).toBeVisible();
        await expect(page.locator('a[href="/community/groups/list/"]').first()).toBeVisible();
        await expect(page.locator('a[href="/community/groups/map/"]').first()).toBeVisible();
        // The old year by year list is gone
        await expect(page.getByText("Registered 2016 or earlier")).toHaveCount(0);
    });

    test("list searches, filters and remembers its state", async ({ page }) => {
        await page.goto("/community/groups/list/");
        const total = await visibleCards(page).count();
        expect(total).toBeGreaterThan(30);
        await expect(page.locator("#stats-total")).toHaveText(String(total));

        // Search by country and by contact name
        await page.fill("#contributor-search", "mex");
        await expect(visibleCards(page)).toHaveCount(2);
        await page.fill("#contributor-search", "ghetta");
        await expect(visibleCards(page)).toHaveCount(1);
        await page.fill("#contributor-search", "zzzz");
        await expect(page.locator(".contributors-no-results")).toBeVisible();
        await page.fill("#contributor-search", "");

        // Continent filter
        await page.click(".filter-button[data-thematic='africa']");
        await expect(page).toHaveURL(/filters=africa/);
        const africa = await visibleCards(page).count();
        expect(africa).toBeGreaterThan(0);
        expect(africa).toBeLessThan(total);
        await page.click("#reset-filters");

        // Inactive groups are hidden until asked for
        await page.check("#include-inactive");
        await expect(page).toHaveURL(/inactive=1/);
        expect(await visibleCards(page).count()).toBeGreaterThan(total);

        // Table view, sorted by country by default
        await page.click("#view-table-btn");
        await expect(page.locator("#contributors-table-view")).toBeVisible();
        const countries = await page
            .locator("#contributors-table-body tr:visible")
            .evaluateAll((rows) => rows.map((r) => (r as HTMLElement).dataset.country || ""));
        const sorted = [...countries].sort((a, b) => a.localeCompare(b));
        expect(countries).toEqual(sorted);
        await expect(page).not.toHaveURL(/sort=/);

        // State survives a reload
        await page.reload();
        await expect(page.locator("#include-inactive")).toBeChecked();
        await expect(page.locator("#contributors-table-view")).toBeVisible();
    });

    test("map shows logos and opens a group from the URL", async ({ page }) => {
        const errors: string[] = [];
        page.on("pageerror", (e) => errors.push(e.message));

        await page.goto("/community/groups/map/?view=flat&group=qgis-ch");
        await expect(page.locator(".user-groups-map .loading-spinner")).toBeHidden();
        await expect(page.locator("#flat-map-view .user-group-marker").first()).toBeAttached();

        const popup = page.locator("#user-group-popup");
        await expect(popup).toBeVisible();
        await expect(page.locator("#user-group-popup-title")).toContainText("Switzerland");
        await expect(popup).toContainText("Since 2015");

        await page.keyboard.press("Escape");
        await expect(popup).toBeHidden();
        await expect(page).not.toHaveURL(/group=/);

        // A country with two groups lists both
        await page.goto("/community/groups/map/?view=flat&country=MX");
        await expect(page.locator(".user-group-entry")).toHaveCount(2);

        expect(errors).toEqual([]);
    });

    test("both maps open on the flat map", async ({ page }) => {
        for (const path of ["/community/groups/map/", "/community/contributors/map/"]) {
            await page.goto(path);
            await expect(page.locator("#flat-map-view")).toBeVisible();
            await expect(page.locator("#globe-view")).toBeHidden();
            await expect(page.locator("#flat-view-btn")).toHaveAttribute("aria-pressed", "true");
        }
        await page.click("#globe-view-btn");
        await expect(page.locator("#globe-view")).toBeVisible();
        await expect(page).toHaveURL(/view=globe/);
    });

    test("contributors map still works with the shared map base", async ({ page }) => {
        const errors: string[] = [];
        page.on("pageerror", (e) => errors.push(e.message));

        await page.goto("/community/contributors/map/?view=flat");
        await expect(page.locator(".loading-spinner")).toBeHidden();
        await expect(page.locator("#flat-map-view .ol-overlay-container").first()).toBeAttached();
        await page.uncheck("#filter-supporting");
        await expect(page).toHaveURL(/showSupporting=false/);

        expect(errors).toEqual([]);
    });
});
