import { test as base, expect } from "@playwright/test";
import { Header } from "./fixtures/header";
import { HomePage } from "./fixtures/home-page";

type HomePageFixtures = {
    header: Header;
    homePage: HomePage;
};

const test = base.extend<HomePageFixtures>({
    header: async ({ page }, use) => {
        const header = new Header(page);
        await use(header);
    },
    homePage: async ({ page }, use) => {
        const homePage = new HomePage(page);
        await use(homePage);
    },
});

test.describe("Home page", () => {
    test.beforeEach(async ({ header, homePage }) => {
        // Go to the home url before each test.
        await homePage.goto();
    });

    test("Header", async ({ header }) => {
        await expect(header.logoLink).toBeVisible();
        await expect(header.productLink).toBeVisible();
        await header.productLink.hover();
        await expect(header.overviewLink).toBeVisible();
        await expect(header.caseStudiesLink).toBeVisible();
        await expect(header.pluginsLink).toBeVisible();
        await expect(header.visualChangelogLink).toBeVisible();
        await expect(header.communityLink).toBeVisible();
        await header.communityLink.hover();
        await expect(header.getInvolvedLink).toBeVisible();
        await expect(header.certifiedMemberLink).toBeVisible();
        await expect(header.qgisFoundationLink).toBeVisible();
        await expect(header.projectOrganisationLink).toBeVisible();
        await expect(header.membersBlogLink).toBeVisible();
        await expect(header.downloadLink).toBeVisible();
        await expect(header.resourcesLink).toBeVisible();
        await header.resourcesLink.hover();
        await expect(header.qgisResourcesLink).toBeVisible();
        await expect(header.installationGuideLink).toBeVisible();
        await expect(header.documentationLink).toBeVisible();
        await expect(header.releasesLink).toBeVisible();
        await expect(header.roadmapLink).toBeVisible();
        await expect(header.reportsLink).toBeVisible();
        await expect(header.booksLink).toBeVisible();
        await expect(header.supportLink).toBeVisible();
        await expect(header.blogLink).toBeVisible();
        await expect(header.donateLink).toBeVisible();
        await expect(header.searchInput).toBeVisible();
        await expect(header.searchInput).toBeEmpty();
    });

    test("Content", async ({ homePage }) => {
        await expect(homePage.freeOpenSourceSpatialDiv).toBeVisible();
        await expect(homePage.spatialWithoutCompromiseHeading).toBeVisible();
        await expect(homePage.createMapsHeading).toBeVisible();
        await expect(homePage.editLayersHeading).toBeVisible();
        await expect(homePage.processAndAnalyzeHeading).toBeVisible();
        await expect(homePage.shareMapsHeading).toBeVisible();
        await expect(homePage.exploreQGISLink).toBeVisible();
        await expect(homePage.powerOfOpenSourceHeading).toBeVisible();
        await expect(homePage.getInvolvedLink).toBeVisible();
        await expect(homePage.freeAndOpenSourceHeading).toBeVisible();
        await expect(homePage.freeDownloadLink).toBeVisible();
        await expect(homePage.youTubeVideoThumbnailOverlayImage).toBeVisible();
        await expect(homePage.startUsingQGISHeading).toBeVisible();
        await expect(homePage.goToMaterialsLink).toBeVisible();
        await expect(homePage.qgisSupportersHeading).toBeVisible();
        await expect(homePage.addYourLogoHereText).toBeVisible();
        await expect(homePage.silverPartnerText).toBeVisible();
        await expect(homePage.supportersGridDiv).toBeVisible();
        await expect(homePage.createMapsImg).toBeVisible();
        await expect(homePage.editLayersImg).toBeVisible();
        await expect(homePage.processImg).toBeVisible();
        await expect(homePage.shareMapsImg).toBeVisible();
        await expect(homePage.communityImg).toBeVisible();
        await expect(homePage.changeLogVideo).toBeVisible();

        homePage.textList.forEach(async (text) => {
            await expect(homePage.pageBody).toContainText(text);
        });
    });
});

// Footer Locators

// test('Footer', async ({ page }) => {
// await expect(page.locator('.tile > .tile').first()).toBeVisible();
// await expect(page.getByRole('contentinfo')).toBeVisible();
//   await expect(page.getByRole('img', { name: 'Logo' })).toBeVisible();
//   await expect(page.getByRole('link', { name: '' })).toBeVisible();
//   await expect(page.getByRole('link', { name: '' })).toBeVisible();
//   await expect(page.getByRole('link', { name: '' })).toBeVisible();
//   await expect(page.locator('div:nth-child(2) > div:nth-child(2) > a:nth-child(4)').first()).toBeVisible();
//   await expect(page.getByRole('link', { name: '' })).toBeVisible();
//   await expect(page.getByRole('link', { name: '' })).toBeVisible();
// });
