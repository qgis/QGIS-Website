import type { Page, Locator } from "@playwright/test";

export class Sidebar {
    public readonly sidebar: Locator;
    public readonly projectLink: Locator;
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
    public readonly documentationLink: Locator;
    public readonly membershipLink: Locator;
    public readonly installationGuideLink: Locator;
    public readonly archiveLink: Locator;
    public readonly roadmapLink: Locator;
    public readonly reportsLink: Locator;
    public readonly booksLink: Locator;
    public readonly supportLink: Locator;
    public readonly membersLink: Locator;
    public readonly pastMembersLink: Locator;
    public readonly windowsLink: Locator;
    public readonly linuxLink: Locator;
    public readonly macOSLink: Locator;
    public readonly freeBSDLink: Locator;
    public readonly openBSDLink: Locator;
    public readonly qgisTestingWarningLink: Locator;
    public readonly installingFromSourceLink: Locator;

    constructor(public readonly page: Page) {
        this.sidebar = this.page.locator("#sidebar");
        this.projectLink = this.sidebar.getByRole("link", {
            name: "Project",
            exact: true,
        });
        this.overviewLink = this.sidebar.getByRole("link", {
            name: "Overview",
        });
        this.caseStudiesLink = this.sidebar.getByRole("link", {
            name: "Case studies",
        });
        this.pluginsLink = this.sidebar.getByRole("link", {
            name: "Plugins",
            exact: true
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
            name: "Certification Programme",
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
        this.documentationLink = this.sidebar.getByRole("link", {
            name: "Documentation",
        });

        this.membershipLink = this.sidebar.getByRole("link", {
            name: "Membership",
        });
        this.installationGuideLink = this.sidebar.getByRole("link", {
            name: "Installation guide",
        });

        this.windowsLink = this.sidebar.getByRole("link", {
            name: "Windows",
        });

        this.linuxLink = this.sidebar.getByRole("link", {
            name: "Linux",
            exact: true,
        });

        this.macOSLink = this.sidebar.getByRole("link", {
            name: "Mac OS X / macOS",
        });

        this.freeBSDLink = this.sidebar.getByRole("link", {
            name: "FreeBSD",
        });

        this.openBSDLink = this.sidebar.getByRole("link", {
            name: "OpenBSD",
        });

        this.qgisTestingWarningLink = this.sidebar.getByRole("link", {
            name: "QGIS Testing Warning",
        });

        this.installingFromSourceLink = this.sidebar.getByRole("link", {
            name: "Installing from Source",
        });
        
        this.archiveLink = this.sidebar.getByRole("link", {
            name: "Archive",
            exact: true,
        });

        this.roadmapLink = this.sidebar.getByRole("link", {
            name: "Roadmap",
            exact: true,
        });

        this.reportsLink = this.sidebar.getByRole("link", {
            name: "Reports",
            exact: true,
        });

        this.booksLink = this.sidebar.getByRole("link", {
            name: "Books",
            exact: true,
        });

        this.supportLink = this.sidebar.getByRole("link", {
            name: "Contact and Support",
            exact: true,
        });

        this.membersLink = this.sidebar.getByRole("link", {
            name: "Members",
            exact: true,
        });

        this.pastMembersLink = this.sidebar.getByRole("link", {
            name: "Past Members",
            exact: true,
        });
    }
}
