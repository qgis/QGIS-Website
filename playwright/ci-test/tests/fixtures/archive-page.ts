import type { Page, Locator } from "@playwright/test";

export class ArchivePage {
    private readonly url: string = "/archive/";
    public readonly pageBody: Locator;
    public readonly textList: string[] = [
        "Archive"
    ];
    public readonly listOfArchive: Locator;
    public readonly archiveHeading: Locator;
    public readonly downloadLink: Locator;
    public readonly macOsReleaseLink: Locator;
    public readonly osgeoDownloadLink: Locator;
    public readonly pluginsLink: Locator;
    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.archiveHeading = this.page.getByRole('heading', { name: 'Archive' });
        this.downloadLink = this.page.getByRole('link', { name: 'QGIS.org hosted downloads' });
        this.macOsReleaseLink = this.page.getByRole('link', { name: 'Older releases for macOS / OS' });
        this.osgeoDownloadLink = this.page.getByRole('link', { name: 'OSGeo hosted downloads' });
        this.pluginsLink = this.page.getByRole('link', { name: 'at plugins.qgis.org' });
    }
    async goto() {
        await this.page.goto(this.url);
    }
}
