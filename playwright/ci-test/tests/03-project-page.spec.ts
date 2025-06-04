import { test as base, expect } from "@playwright/test";
import { HomePage } from "./fixtures/home-page";
import { Sidebar } from "./fixtures/sidebar";
import { ProjectPage } from "./fixtures/project-page";

type ProjectPageFixtures = {
    homePage: HomePage;
    sidebar: Sidebar;
    projectPage: ProjectPage;
};

const test = base.extend<ProjectPageFixtures>({
    homePage: async ({ page }, use) => {
        const homePage = new HomePage(page);
        await use(homePage);
    },
    sidebar: async ({ page }, use) => {
        const sidebar = new Sidebar(page);
        await use(sidebar);
    },
    projectPage: async ({ page }, use) => {
        const projectPage = new ProjectPage(page);
        await use(projectPage);
    },
});

test("Project page", async ({ homePage, sidebar, projectPage }) => {
    await homePage.goto();
    await homePage.downloadLink.click();
    await sidebar.aboutLink.click();
    await expect(projectPage.fosQGISLink).toBeVisible();
    await expect(projectPage.qgisOverview).toBeVisible();
    await expect(projectPage.contentTab1Img).toBeVisible();
    await expect(projectPage.createMapImg).toBeVisible();
    await expect(projectPage.goToPluginsLink).toBeVisible();
    await expect(projectPage.internationalConferenceImg).toBeVisible();
    await expect(projectPage.communityMeetingsLink).toBeVisible();
    await expect(projectPage.localUserGroupsImg).toBeVisible();
    await expect(projectPage.localUserGroupsHeading).toBeVisible();
    await expect(projectPage.localGroupsListLink).toBeVisible();
    await expect(projectPage.joinTheCommunityLink).toBeVisible();
    await expect(projectPage.amurumForestLink).toBeVisible();

    for (const text of projectPage.projectTextList) {
        await expect(projectPage.pageBody).toContainText(text);
    }

    await projectPage.mapsLink.click();
    for (const text of projectPage.mapsTextList) {
        await expect(projectPage.pageBody).toContainText(text);
    }

    await expect(projectPage.screenshotsLink).toBeVisible();
    await projectPage.screenshotsLink.click();

    for (const text of projectPage.screenshotsTextList) {
        await expect(projectPage.pageBody).toContainText(text);
    }
    await sidebar.caseStudiesLink.click();

    for (const text of projectPage.caseStudiesTextList) {
        await expect(projectPage.pageBody).toContainText(text);
    }

    await expect(projectPage.amurumForestLink).toBeVisible();
    await expect(sidebar.pluginsLink).toBeVisible();
    await sidebar.visualChangelogsLink.click();

    for (const text of projectPage.visualChangelogsTextList) {
        await expect(projectPage.pageBody).toContainText(text);
    }
});
