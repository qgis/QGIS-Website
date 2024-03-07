import { test as base, expect } from "@playwright/test";
import { CommunityPage } from "./fixtures/community-page";
import { HomePage } from "./fixtures/home-page";
import { Sidebar } from "./fixtures/sidebar";

type ProductPageFixtures = {
    homePage: HomePage;
    sidebar: Sidebar;
    communityPage: CommunityPage;
};

const test = base.extend<ProductPageFixtures>({
    homePage: async ({ page }, use) => {
        const homePage = new HomePage(page);
        await use(homePage);
    },
    sidebar: async ({ page }, use) => {
        const sidebar = new Sidebar(page);
        await use(sidebar);
    },
    communityPage: async ({ page }, use) => {
        const communityPage = new CommunityPage(page);
        await use(communityPage);
    },
});

test("Community page", async ({ homePage, sidebar, communityPage }) => {
    await homePage.goto();
    await homePage.downloadLink.click();
    await expect(sidebar.communityLink).toBeVisible();
    await sidebar.communityLink.click();
    await expect(sidebar.getInvolvedLink).toBeVisible();
    await sidebar.getInvolvedLink.click();

    let getInvolvedTexts = communityPage.textList.find(
        (item) => item.page == "Get involved",
    )?.texts;

    if (getInvolvedTexts) {
        for (const item of getInvolvedTexts) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }
    await expect(communityPage.participateSupportLink).toBeVisible();
    await expect(communityPage.reportBugsLink).toBeVisible();
    await expect(communityPage.qgisDocumentationLink).toBeVisible();
    await expect(communityPage.translateQGISLink).toBeVisible();
    await expect(communityPage.developPluginLink).toBeVisible();
    await expect(communityPage.developQGISCoreLink).toBeVisible();
    await expect(communityPage.sustainDonateLink).toBeVisible();
    await expect(communityPage.becomeSustainingMemberLink).toBeVisible();
    await expect(communityPage.oneTimeDonationLink).toBeVisible();
    await expect(communityPage.submitButton).toBeVisible();
    await expect(communityPage.otherMethodsInfoLink).toBeVisible();
    await expect(communityPage.currencyInput).toBeVisible();

    await expect(sidebar.becomeCertifiedMemberLink).toBeVisible();
    await sidebar.becomeCertifiedMemberLink.click();

    let becomeCertifiedTexts = communityPage.textList.find(
        (item) => item.page == "Become a certified member",
    )?.texts;

    if (becomeCertifiedTexts) {
        for (const item of becomeCertifiedTexts) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.workflowCertificationImg).toBeVisible();

    await expect(sidebar.qgisFoundationLink).toBeVisible();
    await sidebar.qgisFoundationLink.click();

    let qgisFoundationText = communityPage.textList.find(
        (item) => item.page == "QGIS Foundation",
    )?.texts;

    if (qgisFoundationText) {
        for (const item of qgisFoundationText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.charterLink).toBeVisible();
    await expect(communityPage.annualGeneralMeetingsLink).toBeVisible();
    await expect(communityPage.annualReportsLink).toBeVisible();
    await expect(communityPage.financeLink).toBeVisible();

    await communityPage.charterLink.click();

    let charterText = communityPage.textList.find(
        (item) => item.page == "Charter",
    )?.texts;

    if (charterText) {
        for (const item of charterText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await communityPage.annualGeneralMeetingsLink.click();

    let annualGeneralMeetingsText = communityPage.textList.find(
        (item) => item.page == "Annual General Meetings",
    )?.texts;

    if (annualGeneralMeetingsText) {
        for (const item of annualGeneralMeetingsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await communityPage.annualReportsLink.click();
    let annualReportsText = communityPage.textList.find(
        (item) => item.page == "Annual Reports",
    )?.texts;

    if (annualReportsText) {
        for (const item of annualReportsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await communityPage.financeLink.click();
    let financeText = communityPage.textList.find(
        (item) => item.page == "Finance",
    )?.texts;

    if (financeText) {
        for (const item of financeText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(sidebar.projectOrganisationLink).toBeVisible();
    await sidebar.projectOrganisationLink.click();
    let projectOrganisationText = communityPage.textList.find(
        (item) => item.page == "Project Organisation",
    )?.texts;

    if (projectOrganisationText) {
        for (const item of projectOrganisationText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.infrastructureLink).toBeVisible();
    await communityPage.infrastructureLink.click();
    let infrastructureText = communityPage.textList.find(
        (item) => item.page == "Infrastructure",
    )?.texts;

    if (infrastructureText) {
        for (const item of infrastructureText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.brandGuidelinesLink).toBeVisible();
    await communityPage.brandGuidelinesLink.click();
    let brandGuidelinesText = communityPage.textList.find(
        (item) => item.page == "Brand Guidelines",
    )?.texts;

    if (brandGuidelinesText) {
        for (const item of brandGuidelinesText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.contributorCreditsLink).toBeVisible();
    await communityPage.contributorCreditsLink.click();
    let contributorCreditsText = communityPage.textList.find(
        (item) => item.page == "Contributor Credits",
    )?.texts;

    if (contributorCreditsText) {
        for (const item of contributorCreditsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.committeeResolutionsLink).toBeVisible();
    await communityPage.committeeResolutionsLink.click();

    let committeeResolutionsText = communityPage.textList.find(
        (item) => item.page == "Committee Resolutions",
    )?.texts;

    if (committeeResolutionsText) {
        for (const item of committeeResolutionsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.meetingsLink).toBeVisible();
    await communityPage.meetingsLink.click();

    let meetingsText = communityPage.textList.find(
        (item) => item.page == "Meetings",
    )?.texts;

    if (meetingsText) {
        for (const item of meetingsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.goToMeetingsFirstLink).toBeVisible();
    await expect(communityPage.goToMeetingsNthLink).toBeVisible();

    await expect(communityPage.mailingListsLink).toBeVisible();
    await communityPage.mailingListsLink.click();

    let mailingListsText = communityPage.textList.find(
        (item) => item.page == "Mailing Lists",
    )?.texts;

    if (mailingListsText) {
        for (const item of mailingListsText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.qgisUsersListLink).toBeVisible();
    await expect(communityPage.qgisDevelopersListLink).toBeVisible();
    await expect(communityPage.qgisCommunityTeamLink).toBeVisible();
    await expect(communityPage.qgisTranslationsLink).toBeVisible();
    await expect(communityPage.qgisProjectSteeringLink).toBeVisible();
    await expect(communityPage.qgisWebClientLink).toBeVisible();

    await expect(sidebar.fundingLink).toBeVisible();
    await sidebar.fundingLink.click();
    await expect(sidebar.membershipLink).toBeVisible();
    await sidebar.membershipLink.click();

    let membershipText = communityPage.textList.find(
        (item) => item.page == "Membership",
    )?.texts;

    if (membershipText) {
        for (const item of membershipText) {
            await expect(communityPage.pageBody).toContainText(item);
        }
    }

    await expect(communityPage.becomeSustainingMemberLink).toBeVisible();
    await expect(communityPage.sustainingMembershipDiv).toBeVisible();
    await expect(communityPage.sustainingMembershipSection).toBeVisible();
    await expect(communityPage.writeTrearurerLink).toBeVisible();
    await expect(communityPage.openSustainingMembersLink).toBeVisible();
    // TODO: why Members are not visible?
    // await expect(page.locator('#sidebar').getByRole('link', { name: 'Members' })).toBeVisible();
    // await page.locator('#sidebar').getByRole('link', { name: 'Members' }).click();
    // await expect(page.getByRole('heading', { name: 'Flagship' })).toBeVisible();
    // await expect(page.locator('article').filter({ hasText: 'Felt 2023-01-01 - 2024-02-' })).toBeVisible();
    // await expect(page.getByRole('heading', { name: 'Large' })).toBeVisible();
    // await expect(page.locator('article').filter({ hasText: 'Land Vorarlberg 2023-03-01 -' })).toBeVisible();
    // await expect(page.locator('#sidebar').getByRole('link', { name: 'Past Members' })).toBeVisible();
    // await page.locator('#sidebar').getByRole('link', { name: 'Past Members' }).click();
    // await expect(page.getByText('Past sustaining members ¶ Cheslatta Carrier nation 2021-11-19 - 2023-01-31')).toBeVisible();
});
