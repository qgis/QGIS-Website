import type { Page, Locator } from "@playwright/test";

export class QgisResourcesPage {
    private readonly url: string = "/resources/hub/";
    public readonly pageBody: Locator;
    public readonly installationGuideLink: Locator;
    public readonly getInvolvedLink: Locator;
    public readonly tab3Element: Locator;
    public readonly desktopUserGuideLink: Locator;
    public readonly serverGuideLink: Locator;
    public readonly qgisTrainingManualLink: Locator;
    public readonly introductionInGISLink: Locator;
    public readonly documentationGuidelinesLink: Locator;
    public readonly pyQGISCookbookLink: Locator;
    public readonly cPlusPlusAPIDocumentationLink: Locator;
    public readonly pyQGISApiLink: Locator;
    public readonly buildingQGISFromSourceLink: Locator;
    public readonly forDownloadParagraph: Locator;
    public readonly pdfManualsLink: Locator;
    public readonly htmlZipManualsLink: Locator;
    public readonly viewSupportOptionsLink: Locator;
    public readonly dataProtectionLink: Locator;
    public readonly appNetworkConnectionsLink: Locator;
    public readonly textList: string[] = [
        "Resources",
        "🖖 Installation troubles?",
        "Documentation",
        "For users",
        "For documentation writers",
        "For developers",
        "For download",
        "Support",
        "Data protection",
    ];

    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.installationGuideLink = this.page
            .locator("a")
            .filter({ hasText: /^Installation guide$/ });
        this.getInvolvedLink = this.page
            .locator("p")
            .filter({ hasText: "Get involved and help us" })
            .getByRole("link");
        this.tab3Element = this.page.locator("#tab-3");
        this.desktopUserGuideLink = this.page.getByRole("link", {
            name: "Desktop User Guide",
        });
        this.serverGuideLink = this.page.getByRole("link", {
            name: "Server Guide",
        });
        this.qgisTrainingManualLink = this.page.getByRole("link", {
            name: "QGIS Training manual",
        });
        this.introductionInGISLink = this.page.getByRole("link", {
            name: "Gentle Intro to GIS",
        });
        this.documentationGuidelinesLink = this.page.getByRole("link", {
            name: "Documentation Guidelines",
        });
        this.pyQGISCookbookLink = this.page.getByRole("link", {
            name: "PyQGIS cookbook (for plugins",
        });
        this.cPlusPlusAPIDocumentationLink = this.page.getByRole("link", {
            name: "C++ API documentation",
        });
        this.pyQGISApiLink = this.page.getByRole("link", {
            name: "PyQGIS - QGIS Python Api",
        });
        this.buildingQGISFromSourceLink = this.page.getByRole("link", {
            name: "Building QGIS from Source",
        });
        this.forDownloadParagraph = this.page
            .locator("p")
            .filter({ hasText: "For download" })
            .first();
        this.pdfManualsLink = this.page.getByRole("link", {
            name: "PDF of the manuals",
        });
        this.htmlZipManualsLink = this.page.getByRole("link", {
            name: "HTML zip of the manuals",
        });

        this.dataProtectionLink = this.page.getByText(
            'Data protection', 
            { exact: true }
        );
        this.appNetworkConnectionsLink = this.page.getByRole("link", {
            name: "QGIS Application Network Connections",
        });
        this.viewSupportOptionsLink = this.page.getByRole("link", {
            name: "View support options",
        });
    }
    async goto() {
        await this.page.goto(this.url);
    }
}
