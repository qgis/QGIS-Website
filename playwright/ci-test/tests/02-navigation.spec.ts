import { test as base, expect } from "@playwright/test";
import { Header } from "./fixtures/header";
import { Footer } from "./fixtures/footer";

type NavFixtures = { header: Header; footer: Footer };

const test = base.extend<NavFixtures>({
    header: async ({ page }, use) => await use(new Header(page)),
    footer: async ({ page }, use) => await use(new Footer(page)),
});

test.describe("Site navigation", () => {
    test.beforeEach(async ({ page }) => {
        await page.goto("/");
    });

    test("shows every top-level nav entry", async ({ header }) => {
        for (const label of Header.topLevelItems) {
            await expect(header.navLink(label)).toBeVisible();
        }
    });

    test("navigates to the projects section from the navbar", async ({ header, page }) => {
        await header.navLink("Projects").click();
        await expect(page).toHaveURL(/\/projects\/?$/);
        await expect(page.getByRole("heading", { name: "OSGeo Projects", level: 1 })).toBeVisible();
    });

    test("exposes a burger menu for small viewports", async ({ header, page }) => {
        await page.setViewportSize({ width: 500, height: 900 });
        await expect(header.burger).toBeVisible();
    });

    // Every footer link should reach a real page. This is the cheapest guard
    // against a content section being renamed or removed.
    for (const { label, href } of Footer.links) {
        test(`footer link "${label}" resolves`, async ({ footer, page }) => {
            const link = footer.link(label);
            await expect(link).toHaveAttribute("href", new RegExp(`${href}/?$`));

            const target = await link.getAttribute("href");
            const response = await page.request.get(target!);
            expect(response.status(), `${label} -> ${target}`).toBe(200);
        });
    }
});
