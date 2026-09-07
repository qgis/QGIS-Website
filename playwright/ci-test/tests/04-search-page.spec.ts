import { test as base, expect } from "@playwright/test";
import { SearchPage } from "./fixtures/search-page";

const test = base.extend<{ searchPage: SearchPage }>({
    searchPage: async ({ page }, use) => await use(new SearchPage(page)),
});

test.describe("Search", () => {
    test("renders the search page", async ({ searchPage }) => {
        await searchPage.goto();
        await expect(searchPage.heading).toBeVisible();
        await expect(searchPage.input).toBeVisible();
        await expect(searchPage.results).toBeAttached();
    });

    test("the search index is published as JSON", async ({ page }) => {
        // The client-side search reads the home page's JSON output format;
        // if that stops being generated, search silently returns nothing.
        const response = await page.request.get("/index.json");
        expect(response.status()).toBe(200);
        const body = await response.json();
        expect(Array.isArray(body) ? body.length : Object.keys(body).length).toBeGreaterThan(0);
    });

    test("echoes the ?q= parameter back to the reader", async ({ searchPage }) => {
        await searchPage.goto("osgeolive");
        await expect(searchPage.queryDisplay).toHaveText("osgeolive");
    });
});
