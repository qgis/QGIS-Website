import type { Page, Locator } from "@playwright/test";

export class ProjectPage {
    public readonly pageBody: Locator;
    public readonly qgisOverview: Locator;
    public readonly fosQGISLink: Locator;
    public readonly contentTab1Img: Locator;
    public readonly createMapImg: Locator;
    public readonly goToPluginsLink: Locator;
    public readonly internationalConferenceImg: Locator;
    public readonly communityMeetingsLink: Locator;
    public readonly localUserGroupsImg: Locator;
    public readonly localUserGroupsHeading: Locator;
    public readonly localGroupsListLink: Locator;
    public readonly joinTheCommunityLink: Locator;
    public readonly mapsLink: Locator;
    public readonly screenshotsLink: Locator;
    public readonly projectTextList: string[] = [
        "Free and open source",
        "QGIS overview",
        "Giving the power of spatial visualization and decision making tools to everyone",
        "Available on Windows, Mac, Linux",
        "Key features",
        "Create maps",
        "Edit layers",
        "Process and analyze",
        "Share maps",
        "Class-leading cartography",
        "Professional map production",
        "Powerful reporting tools",
        "Level up with community resources",
        "2000+ plugins developed by community",
        "Annual international conference",
        "Local user groups and support providers",
        "Cross platform",
        "QGIS Server",
        "QGIS Desktop",
        "QGIS Web Client",
        "QGIS on mobiles and tablets",
        "Case Studies",
        "Maps showcase",
        "Application screenshots",
    ];

    public readonly mapsTextList: string[] = [
        "QGIS Maps",
    ];

    public readonly screenshotsTextList: string[] = [
        "QGIS Screenshots",
    ];

    public readonly caseStudiesTextList: string[] = [
        "Case Studies",
    ];

    public readonly visualChangelogsTextList: string[] = [
        "Visual Changelogs",
    ];

    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.qgisOverview = this.page.getByRole("heading", {
            name: "QGIS overview",
        });
        this.fosQGISLink = this.page
            .locator("section")
            .filter({ hasText: "Free and open source QGIS" })
            .getByRole("link");
        this.contentTab1Img = this.page
            .locator("#content-tab-1")
            .getByRole("img", { name: "Create map" });
        this.createMapImg = this.page
            .getByRole("img", { name: "Create map" })
            .nth(1);
        this.goToPluginsLink = this.page.getByRole("link", {
            name: "Go to plugins",
        });
        this.internationalConferenceImg = this.page.getByRole("img", {
            name: "International conference",
        });
        this.communityMeetingsLink = this.page.getByRole("link", {
            name: "Community meetings",
        });
        this.localUserGroupsImg = this.page.getByRole("img", {
            name: "Local user groups",
        });
        this.localUserGroupsHeading = this.page.getByRole("heading", {
            name: "Local user groups and support",
        });
        this.localGroupsListLink = this.page.getByRole("link", {
            name: "Local groups list",
        });
        this.joinTheCommunityLink = this.page.getByRole("link", {
            name: "Join the community",
        });
        this.mapsLink = this.page.getByRole("link", {
            name: "Maps",
            exact: true,
        });
        this.screenshotsLink = this.page.getByRole("link", {
            name: "Screenshots",
        }).first();
    }
}
