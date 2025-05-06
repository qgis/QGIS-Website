import type { Page, Locator } from "@playwright/test";
import { TextList } from "./interfaces";

export class CommunityPage {
    private readonly url: string = "/community/involve/";
    public readonly pageBody: Locator;
    public readonly participateSupportLink: Locator;
    public readonly reportBugsLink: Locator;
    public readonly qgisDocumentationLink: Locator;
    public readonly translateQGISLink: Locator;
    public readonly developPluginLink: Locator;
    public readonly developQGISCoreLink: Locator;
    public readonly sustainDonateLink: Locator;
    public readonly submitButton: Locator;
    public readonly otherMethodsInfoLink: Locator;
    public readonly currencyInput: Locator;
    public readonly workflowCertificationImg: Locator;
    public readonly charterLink: Locator;
    public readonly annualGeneralMeetingsLink: Locator;
    public readonly annualReportsLink: Locator;
    public readonly financeLink: Locator;
    public readonly infrastructureLink: Locator;
    public readonly brandGuidelinesLink: Locator;
    public readonly contributorCreditsLink: Locator;
    public readonly committeeResolutionsLink: Locator;
    public readonly meetingsLink: Locator;
    public readonly goToMeetingsFirstLink: Locator;
    public readonly goToMeetingsNthLink: Locator;
    public readonly mailingListsLink: Locator;
    public readonly qgisUsersListLink: Locator;
    public readonly qgisDevelopersListLink: Locator;
    public readonly qgisCommunityTeamLink: Locator;
    public readonly qgisTranslationsLink: Locator;
    public readonly qgisProjectSteeringLink: Locator;
    public readonly qgisWebClientLink: Locator;

    public readonly textList: TextList[] = [
        {
            page: "Get involved",
            texts: [
                "Ways of Contributing",
                "Participate in Support Channels",
                "Report Bugs",
                "QGIS Documentation",
                "Translate QGIS",
                "Develop a Plugin",
                "Develop QGIS Core",
                "Sustain & Donate",
            ],
        },
        {
            page: "Become a QGIS certified training organisation",
            texts: [
                "Become a QGIS certified training organisation",
                "certification@qgis.org",
                "Certification Process",
                "Requirements",
                "Application",
            ],
        },
        {
            page: "QGIS Foundation",
            texts: [
                "QGIS Foundation",
                "Annual General Meetings",
                "Annual Reports",
                "Finance",
                "QGIS.org Charter",
            ],
        },
        {
            page: "Charter",
            texts: [
                "Charter of the QGIS.ORG Association",
                "Legal status of QGIS.ORG",
                "Definitions",
                "Goals of QGIS.ORG",
                "QGIS.ORG Legal entities",
                "General Meeting",
                "Types of voting members",
                "Composition, appointment and role of voting members",
                "Election and eligibility of QGIS User Group voting members",
                "Election and eligibility of QGIS Community voting members",
                "Honorable members",
                "Voting member terms",
                "Sustaining Members",
                "The board",
                "Election of board members",
                "Terms of members of the board",
                "Composition of the board",
                "Board and PSC Member remuneration",
                "Replacement of Board Members",
                "The Project Steering Committee (PSC)",
                "Election of PSC members",
                "Terms of members of the PSC",
                "Honorary PSC members",
                "Administration of QGIS.ORG",
                "10 Financial arrangements",
            ],
        },
        {
            page: "Annual General Meetings",
            texts: [
                "Annual General Meetings",
                "QGIS AGM Minutes 2023",
                "QGIS AGM Minutes 2022",
                "QGIS AGM Minutes 2021",
                "QGIS AGM Minutes 2020",
                "QGIS AGM Minutes 2019",
                "QGIS AGM Minutes 2018",
                "QGIS AGM Minutes 2017",
            ],
        },
        {
            page: "Annual Reports",
            texts: [
                "Annual Reports",
                "QGIS Annual Report 2022",
                "QGIS Annual Report 2021",
                "QGIS Annual Report 2020",
                "QGIS Annual Report 2019",
                "QGIS Annual Report 2018",
                "QGIS Annual Report 2017",
                "QGIS Annual Report 2016",
            ],
        },
        {
            page: "Finance",
            texts: [
                "Finance",
                "Budget 2023",
                "Financial report 2022",
                "Financial auditing report 2022",
                "Budget 2022",
                "Financial report 2021",
                "Financial auditing report 2021",
                "Budget 2021",
                "Financial report 2020",
                "Financial auditing report 2020",
                "Budget 2020",
                "Financial report 2019",
                "Financial auditing report 2019",
                "Budget 2019",
                "Financial report 2018",
                "Financial auditing report 2018",
                "Budget 2018",
                "Financial report 2018",
                "Financial auditing report 2018",
                "Budget 2018",
                "Financial report 2017",
                "Financial auditing report 2017",
                "Budget 2017",
                "Financial report 2016",
                "Budget 2016",
                "Financial report 2015",
                "Budget 2015",
                "Financial report 2014",
            ],
        },
        {
            page: "Project Organisation",
            texts: [
                "Who’s Who",
                "Board",
                "Project Steering Committee",
                "Honorary PSC Members",
                "Former PSC Members",
                "Voting members",
                "Honorable Voting Members",
                "Country Voting Members",
                "Community Voting Members",
                "Release Management",
                "Packaging Team",
                "Testing Team",
                "Security Team",
                "Community Resources",
                "Translation",
                "Press Material + Translation",
                "TEAM",
            ],
        },
        {
            page: "Infrastructure",
            texts: [
                "Infrastructure",
                "Domains",
                "Main server",
                "Documentation and website",
                "Github management",
                "Flickr Groups",
                "Mastodon",
                "Facebook",
                "Finance",
                "IRC",
                "Planet feeds",
                "OLD Wiki and Redmine",
            ],
        },
        {
            page: "Brand Guidelines",
            texts: [
                "QGIS Trademark and brand guidelines",
                "Country User Groups",
                "Examples of use that do not require permission",
                "Examples of use requiring permission",
                "Prohibited Trademark uses",
                "Examples of unacceptable uses",
                "If in doubt, find out!",
                "Report abuse",
                "Frequently Asked Questions",
            ],
        },
        {
            page: "Contributor Credits",
            texts: ["Contributor Credits", "psc@qgis.org"],
        },
        {
            page: "Meetings",
            texts: ["Meetings", "Developer Meetings", "Users Meetings"],
        },
        {
            page: "Mailing Lists",
            texts: [
                "Mailing Lists",
                "QGIS Users list",
                "QGIS Developers list",
                "QGIS Community team",
                "QGIS Translations",
                "QGIS Project Steering Committee (PSC) list",
                "QGIS Web Client 2",
            ],
        },
    ];

    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");

        this.participateSupportLink = this.page.getByRole("link", {
            name: "Participate in Support",
        });
        this.reportBugsLink = this.page.getByRole("link", {
            name: "Report Bugs",
        });
        this.qgisDocumentationLink = this.page.getByRole("link", {
            name: "QGIS Documentation",
            exact: true,
        });
        this.translateQGISLink = this.page.getByRole("link", {
            name: "Translate QGIS",
            exact: true,
        });
        this.developPluginLink = this.page.getByRole("link", {
            name: "Develop a Plugin",
        });
        this.developQGISCoreLink = this.page.getByRole("link", {
            name: "Develop QGIS Core",
        });
        this.sustainDonateLink = this.page.getByRole("link", {
            name: "Sustain & Donate",
        });
        this.submitButton = this.page.locator("#submit-button");
        this.otherMethodsInfoLink = this.page.getByRole("link", {
            name: "Other methods, more info",
        });
        this.currencyInput = this.page.locator("#payrexx-currency");
        this.workflowCertificationImg = this.page.getByRole("img", {
            name: "Workflow Certification",
        });
        this.charterLink = this.page.getByRole("link", { name: "Charter" });
        this.annualGeneralMeetingsLink = this.page.getByRole("link", {
            name: "Annual General Meetings",
        });
        this.annualReportsLink = this.page.getByRole("link", {
            name: "Annual Reports",
        });
        this.financeLink = this.page.getByRole("link", { name: "Finance" });
        this.infrastructureLink = this.page.getByRole("link", {
            name: "Infrastructure",
        });
        this.brandGuidelinesLink = this.page.getByRole("link", {
            name: "Brand Guidelines",
        });
        this.contributorCreditsLink = this.page.getByRole("link", {
            name: "Contributor Credits",
        });
        this.meetingsLink = this.page
            .getByRole("link", {
                name: "Meetings",
                exact: true,
            })
            .first();
        (this.goToMeetingsFirstLink = this.page
            .getByRole("link", { name: "Go to meetings" })
            .first()),
            (this.goToMeetingsNthLink = this.page
                .getByRole("link", { name: "Go to meetings" })
                .nth(1));
        this.mailingListsLink = this.page.getByRole("link", {
            name: "Mailing Lists",
        });
        this.qgisUsersListLink = this.page.getByRole("link", {
            name: "QGIS Users list http://lists.",
        });
        this.qgisDevelopersListLink = this.page.getByRole("link", {
            name: "QGIS Developers list http://",
        });
        this.qgisCommunityTeamLink = this.page.getByRole("link", {
            name: "QGIS Community team http://",
        });
        this.qgisTranslationsLink = this.page.getByRole("link", {
            name: "QGIS Translations http://",
        });
        this.qgisProjectSteeringLink = this.page.getByRole("link", {
            name: "QGIS Project Steering",
        });
        this.qgisWebClientLink = this.page.getByRole("link", {
            name: "QGIS Web Client 2 http://",
        });
    }
    async goto() {
        await this.page.goto(this.url);
    }
}
