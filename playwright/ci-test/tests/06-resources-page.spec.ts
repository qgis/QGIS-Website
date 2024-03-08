import { test as base, expect } from "@playwright/test";
import { HomePage } from "./fixtures/home-page";
import { Sidebar } from "./fixtures/sidebar";
import { QgisResourcesPage } from "./fixtures/qgis-resources-page";
import { InstallationGuidePage } from "./fixtures/installation-guide-page";
import { ReleasesPage } from "./fixtures/releases-page";

type ProductPageFixtures = {
  homePage: HomePage;
  sidebar: Sidebar;
  qgisResourcesPage: QgisResourcesPage;
  installationGuidePage: InstallationGuidePage;
  releasesPage: ReleasesPage
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
  qgisResourcesPage: async ({ page }, use) => {
      const qgisResourcesPage = new QgisResourcesPage(page);
      await use(qgisResourcesPage);
  },
  installationGuidePage: async ({ page }, use) => {
      const installationGuidePage = new InstallationGuidePage(page);
      await use(installationGuidePage);
  },
  releasesPage: async ({ page }, use) => {
      const releasesPage = new ReleasesPage(page);
      await use(releasesPage);
  },

});


test.describe('Resources pages', () => {
  test.beforeEach(async ({ qgisResourcesPage }) => {
    // Go to the resources url before each test.
    await qgisResourcesPage.goto();
  });

  test('QGIS resources', async ({ sidebar, qgisResourcesPage  }) => {
    await expect(sidebar.resourcesLink).toBeVisible();
    await sidebar.resourcesLink.click();
    await expect(qgisResourcesPage.installationGuideLink).toBeVisible();
    await expect(qgisResourcesPage.getInvolvedLink).toBeVisible();
    await expect(qgisResourcesPage.tab3Element).toBeVisible();
    await expect(qgisResourcesPage.desktopUserGuideLink).toBeVisible();
    await expect(qgisResourcesPage.serverGuideLink).toBeVisible();
    await expect(qgisResourcesPage.qgisTrainingManualLink).toBeVisible();
    await expect(qgisResourcesPage.introductionInGISLink).toBeVisible();
    await expect(qgisResourcesPage.documentationGuidelinesLink).toBeVisible();
    await expect(qgisResourcesPage.pyQGISCookbookLink).toBeVisible();
    await expect(qgisResourcesPage.cPlusPlusAPIDocumentationLink).toBeVisible();
    await expect(qgisResourcesPage.pyQGISApiLink).toBeVisible();
    await expect(qgisResourcesPage.buildingQGISFromSourceLink).toBeVisible();
    await expect(qgisResourcesPage.forDownloadParagraph).toBeVisible();
    await expect(qgisResourcesPage.pdfManualsLink).toBeVisible();
    await expect(qgisResourcesPage.htmlZipManualsLink).toBeVisible();
    await expect(qgisResourcesPage.viewSupportOptionsLink).toBeVisible();

    for (const text of qgisResourcesPage.textList) {
        await expect(qgisResourcesPage.pageBody).toContainText(text);
    }
  });

  test('Installation guide', async ({ sidebar, installationGuidePage }) => {
    await expect(sidebar.installationGuideLink).toBeVisible();
    await sidebar.installationGuideLink.click();
    await expect(installationGuidePage.upcomingEvaluationLink).toBeVisible();
    await expect(installationGuidePage.releaseScheduleLink).toBeVisible();
    await expect(installationGuidePage.releaseCell1).toBeVisible();
    await expect(installationGuidePage.releaseVersionPackageCell).toBeVisible();
    await expect(installationGuidePage.packageCell).toBeVisible();
    await expect(installationGuidePage.mainInstallersPageLink).toBeVisible();
    await expect(installationGuidePage.osgeo4WInstallerLink).toBeVisible();
    await expect(installationGuidePage.aptInstallGnupgPre).toBeVisible();
    await expect(installationGuidePage.aptInstallAptPre).toBeVisible();
    await expect(installationGuidePage.aptUpdatePre).toBeVisible();
    await expect(installationGuidePage.aptInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.ubuntugisLink).toBeVisible();
    await expect(installationGuidePage.ubuntugisDocumentationLink).toBeVisible();
    await expect(installationGuidePage.releaseCell4).toBeVisible();
    await expect(installationGuidePage.releaseVersionDescriptionCell).toBeVisible();
    await expect(installationGuidePage.descriptionCell).toBeVisible();
    await expect(installationGuidePage.repositoryCell).toBeVisible();
    await expect(installationGuidePage.latestReleaseCell).toBeVisible();
    await expect(installationGuidePage.releaseWithUbuntugisCell).toBeVisible();
    await expect(installationGuidePage.releaseDebianUbuntuCell).toBeVisible();
    await expect(installationGuidePage.releaseDebianUbuntuLink).toBeVisible();
    await expect(installationGuidePage.releaseUbuntugisCell).toBeVisible();
    await expect(installationGuidePage.longTermReleaseRepositoryCell).toBeVisible();
    await expect(installationGuidePage.releaseDebianUbuntuCell2).toBeVisible();
    await expect(installationGuidePage.releaseDebianLtrLink).toBeVisible();
    await expect(installationGuidePage.releaseWithUbuntugisCell2).toBeVisible();
    await expect(installationGuidePage.distributionCell).toBeVisible();
    await expect(installationGuidePage.distributionVersionCodenameCell).toBeVisible();
    await expect(installationGuidePage.codenameCell).toBeVisible();
    await expect(installationGuidePage.alsoAvailableBasedOnCell).toBeVisible();
    await expect(installationGuidePage.wgetQgisPre).toBeVisible();
    await expect(installationGuidePage.qgisArchiveKeyringPre).toBeVisible();
    await expect(installationGuidePage.mkdirAptPre1).toBeVisible();
    await expect(installationGuidePage.mkdirAptPre2).toBeVisible();
    await expect(installationGuidePage.aptUpdateInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.aptUpdateInstallQgisServerPre).toBeVisible();
    await expect(installationGuidePage.dnfInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.dnfCoprEnableQgisPre1).toBeVisible();
    await expect(installationGuidePage.dnfInstallQgisPythonPre).toBeVisible();
    await expect(installationGuidePage.dnfInstallQgisServerPre).toBeVisible();
    await expect(installationGuidePage.distributionCell2).toBeVisible();
    await expect(installationGuidePage.distGrassFedora).toBeVisible();
    await expect(installationGuidePage.qgisVersionCell).toBeVisible();
    await expect(installationGuidePage.grassGisVersionCell).toBeVisible();
    await expect(installationGuidePage.dnfCoprEnableQgisPre2).toBeVisible();
    await expect(installationGuidePage.dnfInstallQgisPythonPre2).toBeVisible();
    await expect(installationGuidePage.dnfInstallQgisServerPre2).toBeVisible();
    await expect(installationGuidePage.fedoraCoprLink).toBeVisible();
    await expect(installationGuidePage.distributionCell3).toBeVisible();
    await expect(installationGuidePage.repositoryCell2).toBeVisible();
    await expect(installationGuidePage.urpmiQgisPre).toBeVisible();
    await expect(installationGuidePage.pacmanQgisPre).toBeVisible();
    await expect(installationGuidePage.yaourtQgisLtrPre).toBeVisible();
    await expect(installationGuidePage.flatpakInstallPre).toBeVisible();
    await expect(installationGuidePage.flatpakRunPre).toBeVisible();
    await expect(installationGuidePage.flatpakUpdatePre).toBeVisible();
    await expect(installationGuidePage.spackInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.spackLoadQgisPre).toBeVisible();
    await expect(installationGuidePage.spackEnvCreatePre).toBeVisible();
    await expect(installationGuidePage.portInfoQgis3Pre).toBeVisible();
    await expect(installationGuidePage.portInstallQgis3Pre).toBeVisible();
    await expect(installationGuidePage.portSelfupdatePre).toBeVisible();
    await expect(installationGuidePage.pkgInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.makeInstallQgisPre).toBeVisible();
    await expect(installationGuidePage.pkgInstallQgisLtrSpan).toBeVisible();
    await expect(installationGuidePage.makeInstallQgisLtrPre).toBeVisible();
    await expect(installationGuidePage.pkgAddQgisPre).toBeVisible();
    await expect(installationGuidePage.googlePlayLink).toBeVisible();
    await expect(sidebar.documentationLink).toBeVisible();

    for (const text of installationGuidePage.textList) {
        await expect(installationGuidePage.pageBody).toContainText(text);
    }
  });

  test('Releases', async ({ page, sidebar, releasesPage }) => {
    await expect(sidebar.releasesLink).toBeVisible();
    await sidebar.releasesLink.click();

    for (const text of releasesPage.textList) {
        await expect(releasesPage.pageBody).toContainText(text);
    }
    await expect(releasesPage.listOfReleasesLink).toBeVisible();
    await expect(releasesPage.testsLink).toBeVisible();
    await releasesPage.testsLink.click();
    
  });

  test('Roadmap', async ({ page }) => {
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Roadmap' })).toBeVisible();
    await page.locator('#sidebar').getByRole('link', { name: 'Roadmap' }).click();
    await expect(page.locator('#road-map')).toContainText('Road Map');
    await expect(page.locator('#development-phase')).toContainText('Development phase');
    await expect(page.locator('#feature-freeze')).toContainText('Feature freeze');
    await expect(page.locator('#release')).toContainText('Release');
    await expect(page.locator('#release-schedule')).toContainText('Release schedule');
    await expect(page.locator('#schedule')).toContainText('Schedule');
    await expect(page.getByRole('cell', { name: 'Event' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Latest', exact: true })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Long-Term Repo' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Freeze', exact: true })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Date' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Week #' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Weeks' })).toBeVisible();
    await expect(page.locator('#event-legend')).toContainText('Event legend');
    await expect(page.getByRole('cell', { name: 'Long term release, begin of' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Regular release, begin of new' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Feature freeze, end of' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Point release of latest' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Extra Point release' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'currently supported releases' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'next releases' })).toBeVisible();
    await expect(page.locator('#qgis-prereleases')).toContainText('Location of prereleases / nightly builds');
    await expect(page.getByRole('cell', { name: 'Platform' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Location' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Windows' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'OSGeo4W' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Linux' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Debian/Ubuntu' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'MacOS' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Mac OS' })).toBeVisible();
  });

  test('Reports', async ({ page }) => {
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Reports' })).toBeVisible();
    await expect(page.locator('#sidebar div').filter({ hasText: 'Reports' }).locator('span')).toBeVisible();
    await page.locator('#sidebar').getByRole('link', { name: 'Reports' }).click();
    await expect(page.locator('#daily-reports')).toContainText('Daily Reports');
    await expect(page.locator('#ogc-certification')).toContainText('OGC Certification');
    await expect(page.getByText('QGIS Server').first()).toBeVisible();
    await expect(page.locator('p:nth-child(5) > img')).toBeVisible();
    await expect(page.getByText('In order to keep an eye on')).toBeVisible();
    await expect(page.getByText('WMS').first()).toBeVisible();
    await expect(page.getByText('OGC API Features (aka WFS')).toBeVisible();
    await expect(page.getByText('WFS').first()).toBeVisible();
    await expect(page.getByText('Latest reports')).toBeVisible();
    await expect(page.locator('#performance')).toContainText('Performance');
    await expect(page.getByText('At the moment, two tools are')).toBeVisible();
    await expect(page.getByText('The first one is MS-Perfs')).toBeVisible();
    await expect(page.getByText('The second one is Graffiti,')).toBeVisible();
    await expect(page.getByRole('link', { name: 'OGC Certification' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Performance' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Security' })).toBeVisible();
  });

  test('Books', async ({ page }) => {
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Books' })).toBeVisible();
    await page.locator('#sidebar').getByRole('link', { name: 'Books' }).click();
    await expect(page.getByText('Books ¶ This page lists books')).toBeVisible();
    await expect(page.locator('#books')).toContainText('Books');
    await expect(page.getByText('This page lists books')).toBeVisible();
    await expect(page.getByText('Please write to psc@qgis.org')).toBeVisible();
    await expect(page.getByText('Note: Books order is newest')).toBeVisible();
    await expect(page.getByRole('link', { name: 'psc@qgis.org' })).toBeVisible();
    await expect(page.locator('#english')).toContainText('English');
    await expect(page.locator('#discover-qgis-3x---second-edition')).toContainText('Discover QGIS');
    await expect(page.locator('#qgis-for-hydrological-applications---second-edition')).toContainText('QGIS for Hydrological Applications - Second Edition');
    await expect(page.locator('#land-use-cover-datasets-and-validation-tools-validation-practices-with-qgis')).toContainText('Land Use Cover Datasets and Validation Tools. Validation Practices with QGIS');
    await expect(page.locator('#introduction-to-qgis')).toContainText('Introduction to QGIS');
    await expect(page.locator('#qgis-for-hydrological-applications')).toContainText('QGIS for Hydrological applications');
    await expect(page.locator('#chinese')).toContainText('Chinese');
    await expect(page.locator('#dutch')).toContainText('Dutch');
    await expect(page.locator('#french')).toContainText('French');
    await expect(page.locator('#greek')).toContainText('Greek');
    await expect(page.locator('#japanese')).toContainText('Japanese');
    await expect(page.locator('#polish')).toContainText('Polish');
    await expect(page.locator('#turkish')).toContainText('Turkish');
  });
})
