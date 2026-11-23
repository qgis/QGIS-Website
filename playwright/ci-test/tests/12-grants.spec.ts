import { test, expect } from "@playwright/test";

/**
 * Grant programme list: each post's button opens the original post on the QGIS blog,
 * and the posts get no page of their own on this site.
 */

test.describe("Grant programme", () => {
    test("read more buttons link to the blog posts", async ({ page }) => {
        await page.goto("/community/organisation/grants/");
        const buttons = page.locator(".rich a.button");
        expect(await buttons.count()).toBeGreaterThan(0);

        const hrefs = await buttons.evaluateAll((links) =>
            links.map((link) => link.getAttribute("href")),
        );
        for (const href of hrefs) {
            expect(href).toMatch(/^https:\/\/blog\.qgis\.org\//);
        }
    });

    test("grant posts get no page of their own", async ({ page }) => {
        const response = await page.request.get(
            "/community/organisation/grants/qgis-grant-programme-2026-results/",
        );
        expect(response.status()).toBe(404);
    });
});
