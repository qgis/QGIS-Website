import type { Page, Locator } from "@playwright/test";

export class FaqPage {
    public readonly pageBody: Locator;
    public readonly textList: string[] = [
        "FAQ",
        "User",
        "Downloading issues",
        "I have to donate in order to download QGIS",
        "How to ask a QGIS question?",
        "How are QGIS release names selected?",
        "How to cite QGIS?",
        "Cite the QGIS project in general",
        "I created a map with QGIS, do I have to mention QGIS?",
        "Can I open ECW files with QGIS?",
        "Development",
        "Can I compile QGIS myself?",
        "QGIS.org, %%Y. QGIS Geographic Information System. QGIS Association.",
        "Cite the QGIS Developers",
        "Geographic Information System Developers Manual. QGIS Association.",
        "Cite the QGIS Installation",
        "Geographic Information System Installation Guide. QGIS Association.",
        "Geographic Information System User Guide. QGIS Association.",
        "Cite the QGIS Server",
        "Geographic Information System API Documentation. QGIS Association.",
        "Cite the QGIS API",
        "Geographic Information System API Documentation. QGIS Association.",
        "Preferred format: BibTeX",
    ];
    public readonly faqLink: Locator;
    public readonly qgisIssueTrackerLink: Locator;
    public readonly bugReportingLink: Locator;
    public readonly qgisWebsiteLink: Locator;
    public readonly qgisGitHubLink: Locator;
    public readonly citeQGISUserGuide: Locator;
    public readonly bibTexPre: Locator;
    public readonly patternsPre: Locator;
    public readonly buildingQGISFromSourceLink: Locator;
    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.faqLink = this.page.getByRole("link", { name: "FAQ" });
        this.qgisIssueTrackerLink = this.page.getByRole("link", {
            name: "QGIS issue tracker",
        });
        this.bugReportingLink = this.page.getByRole("link", {
            name: "bug-reporting",
        });
        this.qgisWebsiteLink = this.page.getByRole("link", {
            name: "http://www.qgis.org",
        });
        this.qgisGitHubLink = this.page.getByRole("link", {
            name: "https://github.com/qgis/QGIS/",
        });
        this.citeQGISUserGuide = this.page
            .locator("p")
            .filter({ hasText: "Cite the QGIS User Guide" });
        this.bibTexPre = this.page.locator("pre").filter(
            { hasText: "title = {QGIS Geographic Information System}" }
        );
        this.patternsPre = this.page.locator("pre").filter(
            { hasText: "title = {The QGIS project: Spatial without compromise}" }
        );
        this.buildingQGISFromSourceLink = this.page.getByRole("link", {
            name: "Building QGIS from source",
        });
    }
}
