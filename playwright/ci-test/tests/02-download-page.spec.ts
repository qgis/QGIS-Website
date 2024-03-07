import { test as base, expect } from "@playwright/test";
import { Sidebar } from "./fixtures/sidebar";
import { DownloadPage } from "./fixtures/download-page";
import { HomePage } from "./fixtures/home-page";

let url = "/";

type DownloadPageFixtures = {
    homePage: HomePage;
    sidebar: Sidebar;
    downloadPage: DownloadPage;
};

const test = base.extend<DownloadPageFixtures>({
    homePage: async ({ page }, use) => {
        const homePage = new HomePage(page);
        await use(homePage);
    },
    sidebar: async ({ page }, use) => {
        const sidebar = new Sidebar(page);
        await use(sidebar);
    },
    downloadPage: async ({ page }, use) => {
        const downloadPage = new DownloadPage(page);
        await use(downloadPage);
    },
});

test("Download page", async ({ homePage, sidebar, downloadPage }) => {
    await homePage.goto();
    await homePage.downloadLink.click();
    await expect(downloadPage.beforeDownloadText).toBeVisible();
    await expect(downloadPage.oneTimePaymentText).toBeVisible();
    await expect(downloadPage.submitButton).toBeVisible();
    await expect(downloadPage.otherMethodsLink).toBeVisible();
    await expect(downloadPage.currencyInput).toBeVisible();
    await expect(downloadPage.skipDownloadButton).toBeVisible();
    await expect(sidebar.productLinkInSidebar).toBeVisible();
    await expect(sidebar.overviewLinkInSidebar).toBeVisible();
    await expect(sidebar.caseStudiesLinkInSidebar).toBeVisible();
    await expect(sidebar.pluginsLinkInSidebar).toBeVisible();
    await expect(sidebar.visualChangelogsLinkInSidebar).toBeVisible();
    await expect(sidebar.communityLinkInSidebar).toBeVisible();
    await expect(sidebar.getInvolvedLinkInSidebar).toBeVisible();
    await expect(sidebar.becomeCertifiedMemberLinkInSidebar).toBeVisible();
    await expect(sidebar.qgisFoundationLinkInSidebar).toBeVisible();
    await expect(sidebar.projectOrganisationLinkInSidebar).toBeVisible();
    await expect(sidebar.membersBlogsLinkInSidebar).toBeVisible();
    await expect(sidebar.fundingLinkInSidebar).toBeVisible();
    await expect(sidebar.downloadLinkInSidebar).toBeVisible();
    await expect(sidebar.resourcesLinkInSidebar).toBeVisible();
    await expect(sidebar.qgisResourcesLinkInSidebar).toBeVisible();
    await downloadPage.skipDownloadButton.click();
    await expect(downloadPage.beforeDownloadHeading).toBeVisible();
    await downloadPage.otherPlatformsHeading.click();
    await expect(downloadPage.otherPlatformsHeading).toBeVisible();
});
