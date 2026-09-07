import { test as base, expect } from "@playwright/test";
import { ProjectsPage } from "./fixtures/projects-page";

const test = base.extend<{ projectsPage: ProjectsPage }>({
    projectsPage: async ({ page }, use) => await use(new ProjectsPage(page)),
});

test.describe("Projects gallery", () => {
    test.beforeEach(async ({ projectsPage }) => {
        await projectsPage.goto();
    });

    test("lists the projects from data/projects.yaml", async ({ projectsPage }) => {
        await expect(projectsPage.heading).toBeVisible();
        // Guard against the data file failing to load and rendering an empty grid.
        expect(await projectsPage.cards.count()).toBeGreaterThan(20);
    });

    test("offers a filter button for every category", async ({ projectsPage }) => {
        await expect(projectsPage.filterButton("all")).toBeVisible();
        for (const category of ProjectsPage.categories) {
            await expect(projectsPage.filterButton(category)).toBeVisible();
        }
    });

    test("every card carries the metadata the filters rely on", async ({ projectsPage }) => {
        const count = await projectsPage.cards.count();
        for (let i = 0; i < count; i++) {
            const card = projectsPage.cards.nth(i);
            await expect(card).toHaveAttribute("data-category", /.+/);
            await expect(card).toHaveAttribute("data-status", /.+/);
            await expect(card).toHaveAttribute("data-name", /.+/);
        }
    });

    test("filtering by category narrows the visible cards", async ({ projectsPage }) => {
        const total = await projectsPage.visibleCardCount();
        expect(total).toBeGreaterThan(0);

        await projectsPage.filterButton("desktop").click();
        const desktopExpected = await projectsPage.cardsInCategory("desktop").count();
        expect(desktopExpected).toBeGreaterThan(0);

        await expect
            .poll(() => projectsPage.visibleCardCount())
            .toBe(desktopExpected);

        // ...and resetting to "all" brings them back.
        await projectsPage.filterButton("all").click();
        await expect.poll(() => projectsPage.visibleCardCount()).toBe(total);
    });

    test("opens an individual project page", async ({ projectsPage, page }) => {
        await projectsPage.cardsInCategory("desktop").first().click();
        await expect(page).toHaveURL(/\/projects\/[a-z0-9-]+\/?$/);
        await expect(page.locator("h1").first()).toBeVisible();
    });
});
