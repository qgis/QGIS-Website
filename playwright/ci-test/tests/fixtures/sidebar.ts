import type { Page, Locator } from "@playwright/test";

export class Sidebar {
    public readonly sidebar: Locator;
    public readonly productLink: Locator;
    public readonly overviewLink: Locator;
    public readonly caseStudiesLink: Locator;
    public readonly pluginsLink: Locator;
    public readonly visualChangelogsLink: Locator;
    public readonly communityLink: Locator;
    public readonly getInvolvedLink: Locator;
    public readonly becomeCertifiedMemberLink: Locator;
    public readonly qgisFoundationLink: Locator;
    public readonly projectOrganisationLink: Locator;
    public readonly membersBlogsLink: Locator;
    public readonly fundingLink: Locator;
    public readonly downloadLink: Locator;
    public readonly resourcesLink: Locator;
    public readonly qgisResourcesLink: Locator;

    constructor(public readonly page: Page) {
        this.sidebar = this.page.locator("#sidebar");
        this.productLink = this.sidebar.getByRole("link", {
            name: "Product",
        });
        this.overviewLink = this.sidebar.getByRole("link", {
            name: "Overview",
        });
        this.caseStudiesLink = this.sidebar.getByRole("link", {
            name: "Case studies",
        });
        this.pluginsLink = this.sidebar.getByRole("link", {
            name: "Plugins",
        });
        this.visualChangelogsLink = this.sidebar.getByRole("link", {
            name: "Visual Changelogs",
        });
        this.communityLink = this.sidebar.getByRole("link", {
            name: "Community",
        });
        this.getInvolvedLink = this.sidebar.getByRole("link", {
            name: "Get involved",
        });
        this.becomeCertifiedMemberLink = this.sidebar.getByRole("link", {
            name: "Become a certified member",
        });
        this.qgisFoundationLink = this.sidebar.getByRole("link", {
            name: "QGIS Foundation",
        });
        this.projectOrganisationLink = this.sidebar.getByRole("link", {
            name: "Project Organisation",
        });
        this.membersBlogsLink = this.sidebar.getByRole("link", {
            name: "Members Blogs",
        });
        this.fundingLink = this.sidebar.getByRole("link", {
            name: "Funding",
        });
        this.downloadLink = this.sidebar.getByRole("link", {
            name: "Download",
        });
        this.resourcesLink = this.sidebar.getByRole("link", {
            name: "Resources",
            exact: true,
        });
        this.qgisResourcesLink = this.sidebar.getByRole("link", {
            name: "QGIS resources",
        });
    }
}
