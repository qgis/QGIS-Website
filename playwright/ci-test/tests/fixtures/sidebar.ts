import type { Page, Locator } from "@playwright/test";

export class Sidebar {
    public readonly sidebar: Locator;
    public readonly productLinkInSidebar: Locator;
    public readonly overviewLinkInSidebar: Locator;
    public readonly caseStudiesLinkInSidebar: Locator;
    public readonly pluginsLinkInSidebar: Locator;
    public readonly visualChangelogsLinkInSidebar: Locator;
    public readonly communityLinkInSidebar: Locator;
    public readonly getInvolvedLinkInSidebar: Locator;
    public readonly becomeCertifiedMemberLinkInSidebar: Locator;
    public readonly qgisFoundationLinkInSidebar: Locator;
    public readonly projectOrganisationLinkInSidebar: Locator;
    public readonly membersBlogsLinkInSidebar: Locator;
    public readonly fundingLinkInSidebar: Locator;
    public readonly downloadLinkInSidebar: Locator;
    public readonly resourcesLinkInSidebar: Locator;
    public readonly qgisResourcesLinkInSidebar: Locator;

    constructor(public readonly page: Page) {
        this.sidebar = this.page.locator("#sidebar");
        this.productLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Product",
        });
        this.overviewLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Overview",
        });
        this.caseStudiesLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Case studies",
        });
        this.pluginsLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Plugins",
        });
        this.visualChangelogsLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Visual Changelogs",
        });
        this.communityLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Community",
        });
        this.getInvolvedLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Get involved",
        });
        this.becomeCertifiedMemberLinkInSidebar = this.sidebar.getByRole(
            "link",
            { name: "Become a certified member" },
        );
        this.qgisFoundationLinkInSidebar = this.sidebar.getByRole("link", {
            name: "QGIS Foundation",
        });
        this.projectOrganisationLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Project Organisation",
        });
        this.membersBlogsLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Members Blogs",
        });
        this.fundingLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Funding",
        });
        this.downloadLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Download",
        });
        this.resourcesLinkInSidebar = this.sidebar.getByRole("link", {
            name: "Resources",
            exact: true,
        });
        this.qgisResourcesLinkInSidebar = this.sidebar.getByRole("link", {
            name: "QGIS resources",
        });
    }
}
