import { test as base, expect } from "@playwright/test";
import { HomePage } from "./fixtures/home-page";
import { Sidebar } from "./fixtures/sidebar";
import { QgisResourcesPage } from "./fixtures/qgis-resources-page";

type ProductPageFixtures = {
  homePage: HomePage;
  sidebar: Sidebar;
  qgisResourcesPage: QgisResourcesPage;
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

  test('Installation guide', async ({ page }) => {
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Installation guide' })).toBeVisible();
    await page.locator('#sidebar').getByRole('link', { name: 'Installation guide' }).click();
    await expect(page.getByText('QGIS Installers ¶ How to')).toBeVisible();
    await expect(page.locator('#qgis-installers')).toContainText('QGIS Installers');
    await expect(page.getByText('How to obtain QGIS?')).toBeVisible();
    await expect(page.getByText('QGIS is available on Windows')).toBeVisible();
    await expect(page.getByText('We recommend installing the')).toBeVisible();
    await expect(page.getByText('To evaluate the upcoming')).toBeVisible();
    await expect(page.getByText('In the feature frozen phase')).toBeVisible();
    await expect(page.locator('p').filter({ hasText: 'To evaluate the upcoming' }).getByRole('link')).toBeVisible();
    await expect(page.getByRole('link', { name: 'Release schedule' })).toBeVisible();
    await expect(page.locator('#windows')).toContainText('Windows');
    await expect(page.getByText('There are two options for')).toBeVisible();
    await expect(page.locator('#standalone-installers')).toContainText('Standalone installers');
    await expect(page.getByText('For beginners the easiest way')).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release', exact: true }).first()).toBeVisible();
    await expect(page.getByRole('row', { name: 'Release Version Package', exact: true }).getByRole('cell').nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Package' }).first()).toBeVisible();
    await expect(page.getByRole('link', { name: 'The main installers page' })).toBeVisible();
    await expect(page.locator('#osgeo4w-installer')).toContainText('OSGeo4W installer');
    await expect(page.getByText('More advanced QGIS users')).toBeVisible();
    await expect(page.getByText('The OSGeo4W repository')).toBeVisible();
    await expect(page.getByText('Download OSGeo4W Installer')).toBeVisible();
    await expect(page.getByRole('link', { name: 'OSGeo4W Installer' })).toBeVisible();
    await expect(page.getByText('Choose Express Install and')).toBeVisible();
    await expect(page.getByText('The packages listed in the')).toBeVisible();
    await expect(page.locator('#linux')).toContainText('Linux');
    await expect(page.getByText('Most linux distributions')).toBeVisible();
    await expect(page.getByText('Below you find instructions')).toBeVisible();
    await expect(page.locator('#debianubuntu')).toContainText('Debian/Ubuntu');
    await expect(page.getByText('Note ¶ In the section')).toBeVisible();
    await expect(page.getByText('Note ¶ Although you see ‘')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo apt install gnupg' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo mkdir -m755 -p /etc/apt/' }).first()).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'Types: deb deb-src URIs: https://qgis.org/debian Suites: your-distributions-' })).toBeVisible();
    await expect(page.getByText('Note ¶ Suites in above lines')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo apt update' }).first()).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo apt install qgis qgis-' }).first()).toBeVisible();
    await expect(page.getByText('Note ¶ Add qgis-server to')).toBeVisible();
    await expect(page.locator('#repositories')).toContainText('Repositories');
    await expect(page.getByText('To have newer versions, you')).toBeVisible();
    await expect(page.getByText('Our main repository contains')).toBeVisible();
    await expect(page.getByText('For Ubuntu we also used to')).toBeVisible();
    await expect(page.getByRole('link', { name: 'ubuntugis', exact: true })).toBeVisible();
    await expect(page.getByRole('link', { name: 'ubuntugis documentation' })).toBeVisible();
    await expect(page.getByText('Note ¶ The release packages')).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release', exact: true }).nth(4)).toBeVisible();
    await expect(page.getByRole('row', { name: 'Release Version Description' }).getByRole('cell').nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Description' }).nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Repository' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Latest Release' }).nth(2)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release with ubuntugis-' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release for Debian and Ubuntu' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'https://qgis.org/debian https' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'https://qgis.org/ubuntugis', exact: true })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Nightly build of upcoming' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'https://qgis.org/debian-nightly-release https://qgis.org/ubuntu-nightly-release' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Nightly build of upcoming' }).nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'https://qgis.org/ubuntugis-nightly-release' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Long Term Release Repository' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release for Debian and Ubuntu' }).nth(2)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'https://qgis.org/debian-ltr' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Release with ubuntugis-' }).nth(2)).toBeVisible();
    await expect(page.locator('#available-codenames')).toContainText('Supported distribution versions:');
    await expect(page.getByRole('cell', { name: 'Distribution' }).first()).toBeVisible();
    await expect(page.getByRole('row', { name: 'Distribution Version Codename' }).getByRole('cell').nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Codename' })).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Also available based on' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'wget https://download.qgis.' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: './qgis-archive-keyring.gpg -------------------------- pub rsa4096 2022-08-08 [' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo mkdir -m755 -p /etc/apt/' }).nth(1)).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo mkdir -m755 -p /etc/apt/' }).nth(2)).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'Types: deb deb-src URIs: *' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo apt update sudo apt install qgis qgis-plugin-grass' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo apt update sudo apt install qgis-server --no-install-recommends --no-' })).toBeVisible();
    await expect(page.getByText('Note ¶ Please remove all the')).toBeVisible();
    await expect(page.locator('#fedora')).toContainText('Fedora');
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf install qgis python3-qgis qgis-grass qgis-server' })).toBeVisible();
    await expect(page.locator('#qgis-stable')).toContainText('QGIS stable');
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf copr enable dani/qgis' }).first()).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf install qgis python3' }).nth(1)).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf install qgis-server' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Distribution' }).nth(1)).toBeVisible();
    await expect(page.locator('table').filter({ hasText: 'Distribution Version QGIS version GRASS GIS version Fedora' }).locator('th').nth(1)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'QGIS version' }).first()).toBeVisible();
    await expect(page.getByRole('cell', { name: 'GRASS GIS version' }).first()).toBeVisible();
    await expect(page.getByText('More information are').first()).toBeVisible();
    await expect(page.locator('#qgis-ltr-long-term-release')).toContainText('QGIS LTR (Long Term Release)');
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf copr enable dani/qgis-ltr' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf install qgis python3' }).nth(2)).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo dnf install qgis-server' }).nth(1)).toBeVisible();
    await expect(page.getByText('More information are').nth(1)).toBeVisible();
    await expect(page.getByRole('link', { name: 'https://copr.fedorainfracloud.org/coprs/dani/qgis-ltr/' })).toBeVisible();
    await expect(page.locator('#suse--opensuse')).toContainText('SUSE / openSUSE');
    await expect(page.getByRole('cell', { name: 'Distribution' }).nth(3)).toBeVisible();
    await expect(page.getByRole('cell', { name: 'Repository' }).nth(2)).toBeVisible();
    await expect(page.locator('#mandriva')).toContainText('Mandriva');
    await expect(page.locator('pre').filter({ hasText: 'urpmi qgis-python qgis-grass' })).toBeVisible();
    await expect(page.locator('#slackware')).toContainText('Slackware');
    await expect(page.getByText('Packages on https://')).toBeVisible();
    await expect(page.locator('#arch-linux')).toContainText('Arch Linux');
    await expect(page.getByText('Arch Linux is available in')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'pacman -S qgis' })).toBeVisible();
    await expect(page.locator('#qgis-ltr')).toContainText('QGIS LTR');
    await expect(page.locator('pre').filter({ hasText: 'yaourt -S qgis-ltr' })).toBeVisible();
    await expect(page.locator('#qgis-testing')).toContainText('QGIS testing');
    await expect(page.getByText('yaourt -S qgis-git')).toBeVisible();
    await expect(page.getByText('For bugs and other behaviour').nth(1)).toBeVisible();
    await expect(page.locator('#flatpak')).toContainText('Flatpak');
    await expect(page.getByText('For general Linux Flatpak')).toBeVisible();
    await expect(page.getByText('QGIS on Flathub: https://')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'flatpak install --from https' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'flatpak run org.qgis.qgis' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'flatpak update' })).toBeVisible();
    await expect(page.getByText('Flathub files: https://github')).toBeVisible();
    await expect(page.locator('#spack')).toContainText('Spack');
    await expect(page.getByText('General info on installing')).toBeVisible();
    await expect(page.getByText('QGIS package file on Spack:')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'spack install qgis' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'spack load qgis' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'spack env create myenv spack' })).toBeVisible();
    await expect(page.getByText('Spack related issues should')).toBeVisible();
    await expect(page.locator('#mac-os-x--macos')).toContainText('Mac OS X / macOS');
    await expect(page.getByText('Official All-in-one, signed')).toBeVisible();
    await expect(page.locator('#qgis-nightly-release')).toContainText('QGIS nightly release');
    await expect(page.locator('#macports')).toContainText('MacPorts');
    await expect(page.getByText('The package management system')).toBeVisible();
    await expect(page.getByText('Installing MacPorts and updating it and the ports are made with the Terminal.')).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo port info qgis3' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo port install qgis3 +grass' })).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'sudo port selfupdate sudo' })).toBeVisible();
    await expect(page.getByText('Note ¶ Concurrent')).toBeVisible();
    await expect(page.locator('#old-releases')).toContainText('Old releases');
    await expect(page.getByText('Previous releases of the official installer can be downloaded from https://qgis')).toBeVisible();
    await expect(page.getByText('Previous releases of the kyngchaos installer can be downloaded from https://www')).toBeVisible();
    await expect(page.locator('#freebsd')).toContainText('FreeBSD');
    await expect(page.locator('#qgis-stable-4')).toContainText('QGIS stable');
    await expect(page.locator('pre').filter({ hasText: 'pkg install qgis' }).first()).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'cd /usr/ports/graphics/qgis make install clean' })).toBeVisible();
    await expect(page.locator('#qgis-ltr-1')).toContainText('QGIS LTR');
    await expect(page.locator('span').filter({ hasText: 'pkg install qgis-ltr' }).first()).toBeVisible();
    await expect(page.locator('pre').filter({ hasText: 'cd /usr/ports/graphics/qgis-' })).toBeVisible();
    await expect(page.locator('#openbsd')).toContainText('OpenBSD');
    await expect(page.locator('pre').filter({ hasText: 'pkg_add qgis' })).toBeVisible();
    await expect(page.getByText('See: - https://openbsd.app/?')).toBeVisible();
    await expect(page.locator('#android')).toContainText('Android');
    await expect(page.getByText('An old and deprecated not')).toBeVisible();
    await expect(page.getByRole('link', { name: 'https://play.google.com/store' })).toBeVisible();
    await expect(page.getByText('Warning ¶ There is currently')).toBeVisible();
    await expect(page.locator('#qgis-testing-warning')).toContainText('QGIS Testing warning');
    await expect(page.getByText('Warning ¶ QGIS testing')).toBeVisible();
    await expect(page.locator('#installing-from-source')).toContainText('Installing from Source');
    await expect(page.getByText('Refer to INSTALL on how to')).toBeVisible();
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Documentation' })).toBeVisible();
  });

  test('Releases', async ({ page }) => {
    await expect(page.locator('#sidebar').getByRole('link', { name: 'Releases', exact: true })).toBeVisible();
    await expect(page.locator('#sidebar div').filter({ hasText: 'Releases' }).locator('span')).toBeVisible();
    await page.locator('#sidebar').getByRole('link', { name: 'Releases', exact: true }).click();
    await expect(page.locator('#list-of-releases')).toContainText('List of Releases');
    await expect(page.getByText('Previous releases of QGIS are')).toBeVisible();
    await expect(page.getByText('More older releases are')).toBeVisible();
    await expect(page.getByText('Plugins for QGIS are also')).toBeVisible();
    await expect(page.locator('#tests')).toContainText('Tests');
    await expect(page.getByText('Both QGIS and QGIS server are')).toBeVisible();
    await expect(page.getByText('From build tests (github')).toBeVisible();
    await expect(page.getByText('See Unit testing')).toBeVisible();
    await expect(page.getByText('See OGC conformance testing')).toBeVisible();
    await expect(page.getByText('Recent tests output can be')).toBeVisible();
    await expect(page.getByRole('link', { name: 'List of releases' })).toBeVisible();
    await expect(page.getByRole('link', { name: 'Tests' })).toBeVisible();
    await page.getByRole('link', { name: 'Tests' }).click();
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
