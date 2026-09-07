import { test as base, expect } from "@playwright/test";
import { Header } from "./fixtures/header";
import { Footer } from "./fixtures/footer";
import { HomePage } from "./fixtures/home-page";

type HomePageFixtures = {
    header: Header;
    footer: Footer;
    homePage: HomePage;
};

const test = base.extend<HomePageFixtures>({
    header: async ({ page }, use) => await use(new Header(page)),
    footer: async ({ page }, use) => await use(new Footer(page)),
    homePage: async ({ page }, use) => await use(new HomePage(page)),
});

test.describe("Home page", () => {
    test.beforeEach(async ({ homePage }) => {
        await homePage.goto();
    });

    test("has the OSGeo title", async ({ page }) => {
        await expect(page).toHaveTitle(/OSGeo - Open Source Geospatial Foundation/);
    });

    test("shows the hero headline", async ({ homePage }) => {
        await expect(homePage.hero).toBeVisible();
        await expect(homePage.headline).toBeVisible();
        await expect(homePage.headlineWords).toHaveCount(2);
        await expect(homePage.headline).toContainText("Powering the");
        await expect(homePage.headline).toContainText("World's Maps");
    });

    test("renders the four data-driven hero stats", async ({ homePage }) => {
        await expect(homePage.statCards).toHaveCount(4);
        await expect(homePage.statLabels).toHaveText(HomePage.statLabels);

        // The project count comes from data/projects.yaml, so assert its shape
        // rather than a value that changes whenever a project is added.
        await expect(homePage.statNumbers.first()).toHaveText(/^\d+\+$/);
    });

    test("shows each main content section", async ({ page }) => {
        for (const heading of HomePage.sectionHeadings) {
            await expect(
                page.getByRole("heading", { name: heading, level: 2 }),
            ).toBeVisible();
        }
    });

    test("shows the OSGeo logo in the navbar", async ({ header }) => {
        await expect(header.navbar).toBeVisible();
        await expect(header.brandLogo).toBeVisible();
        await expect(header.brandLogo).toHaveAttribute("alt", "OSGeo");
        await expect(header.brandLogo).toHaveAttribute("src", /osgeo-logo\.svg$/);
    });

    test("has a footer", async ({ footer }) => {
        await expect(footer.root).toBeVisible();
    });
});
