import { test, expect } from "@playwright/test";
import { ContentPage, contentPages } from "./fixtures/content-page";

test.describe("Content pages", () => {
    for (const spec of contentPages) {
        test(`${spec.path} renders`, async ({ page }) => {
            const contentPage = new ContentPage(page, spec);
            await contentPage.goto();

            await expect(page).toHaveTitle(new RegExp(spec.title.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
            await expect(contentPage.heading).toBeVisible();
            await expect(page.locator("nav.navbar")).toBeVisible();
            await expect(page.locator("footer").first()).toBeVisible();
        });
    }
});

test.describe("Error handling", () => {
    test("serves a branded 404 page", async ({ page }) => {
        // Hugo writes 404.html; a static host serves it for unknown paths.
        await page.goto("/404.html");
        await expect(page).toHaveTitle(/404 Page not found/);
        await expect(
            page.getByRole("heading", { name: "Whoops! Page not found", level: 1 }),
        ).toBeVisible();
        // Regression guard: this page said "Go to QGIS Homepage" after the fork.
        await expect(page.locator("body")).not.toContainText("QGIS Homepage");
        await expect(page.getByRole("link", { name: "Homepage" })).toBeVisible();
    });
});
