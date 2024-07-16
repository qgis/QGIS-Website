import { test as base, expect } from "@playwright/test";
import { Sidebar } from "./fixtures/sidebar";
import { ArchivePage } from "./fixtures/archive-page";

type ResourcesPageFixtures = {
    sidebar: Sidebar;
    archivePage: ArchivePage;
};

const test = base.extend<ResourcesPageFixtures>({
    sidebar: async ({ page }, use) => {
        const sidebar = new Sidebar(page);
        await use(sidebar);
    },
    archivePage: async ({ page }, use) => {
        const archivePage = new ArchivePage(page);
        await use(archivePage);
    },
});

test.describe("Archive pages", () => {
    test.beforeEach(async ({ archivePage }) => {
        // Go to the resources url before each test.
        await archivePage.goto();
    });

    test("Archive", async ({ page, sidebar, archivePage }) => {
        await expect(sidebar.archiveLink).toBeVisible();
        await sidebar.archiveLink.click();

        for (const text of archivePage.textList) {
            await expect(archivePage.pageBody).toContainText(text);
        }
        await expect(archivePage.archiveHeading).toBeVisible();
        await expect(archivePage.downloadLink).toBeVisible();
        await expect(archivePage.macOsReleaseLink).toBeVisible();
        await expect(archivePage.osgeoDownloadLink).toBeVisible();
        await expect(archivePage.pluginsLink).toBeVisible();
    });
});
