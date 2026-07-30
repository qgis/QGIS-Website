import { test, expect, Page } from "@playwright/test";

/**
 * Search regression tests.
 *
 * The search index is built per page section (see the theme's
 * layouts/_default/index.json) so that results deep-link to the heading that
 * matched. These tests pin the behaviour that used to be broken:
 *   - a multi-word query finding an answer buried far down a long page
 *   - results linking to the section anchor rather than the page top
 *   - the index not containing duplicate entries
 */

const CITE_ANCHOR = "/resources/support/faq/#how-to-cite-qgis";

type IndexEntry = {
    title: string;
    page: string;
    contents: string;
    permalink: string;
};

async function fetchIndex(page: Page): Promise<IndexEntry[]> {
    const response = await page.request.get("/index.json");
    expect(response.ok()).toBeTruthy();
    return (await response.json()) as IndexEntry[];
}

async function search(page: Page, query: string) {
    await page.goto(`/search/?q=${encodeURIComponent(query)}`);
    await expect(page.locator(".search-loading")).toBeHidden();
    return page.locator("#search-results a.search-item");
}

test.describe("Search", () => {
    test("index is built per section, without duplicates", async ({ page }) => {
        const entries = await fetchIndex(page);
        expect(entries.length).toBeGreaterThan(0);

        // A page's .Scratch survives `hugo server` rebuilds, so an accumulating
        // index would silently emit each entry several times.
        const permalinks = entries.map((entry) => entry.permalink);
        expect(new Set(permalinks).size).toBe(permalinks.length);

        // Every entry carries the page it came from, used as result context.
        expect(entries.filter((entry) => !entry.page)).toHaveLength(0);

        // Sections are addressable by anchor.
        const anchored = entries.filter((entry) => entry.permalink.includes("#"));
        expect(anchored.length).toBeGreaterThan(0);

        const cite = entries.find((entry) => entry.permalink.endsWith(CITE_ANCHOR));
        expect(cite).toBeDefined();
        expect(cite!.title).toContain("cite QGIS");
        expect(cite!.page).toBe("FAQ");
        // The section holds only its own text, not the whole FAQ page.
        expect(cite!.contents).toContain("cite QGIS in your work");
        expect(cite!.contents).not.toContain("How to ask a QGIS question");
    });

    test('"How to cite QGIS" links straight to the FAQ section', async ({ page }) => {
        const results = await search(page, "How to cite QGIS");
        await expect(results.first()).toHaveAttribute("href", new RegExp(`${CITE_ANCHOR}$`));
    });

    test("a re-worded query still finds the section", async ({ page }) => {
        // Fuse matches the query as one contiguous phrase, so this phrasing only
        // works via the every-token fallback in search.js.
        const results = await search(page, "how do I cite qgis");
        await expect(results.first()).toHaveAttribute("href", new RegExp(`${CITE_ANCHOR}$`));
    });

    test("headings shared by many pages are distinguishable", async ({ page }) => {
        // "Programmability" is a heading on every visual changelog, so results
        // must name the page each section belongs to.
        const results = await search(page, "programmability");
        const count = await results.count();
        expect(count).toBeGreaterThan(1);

        const contexts = await results.locator(".list-item-context").allInnerTexts();
        expect(new Set(contexts).size).toBeGreaterThan(1);
    });

    test("matched terms are highlighted", async ({ page }) => {
        const results = await search(page, "How to cite QGIS");
        await expect(results.first().locator("mark").first()).toBeVisible();
    });

    test("a query with no match reports no results", async ({ page }) => {
        await page.goto("/search/?q=xyzzynotathing");
        await expect(page.locator(".search-results-empty")).toBeVisible();
        await expect(page.locator("#search-results a.search-item")).toHaveCount(0);
    });
});
