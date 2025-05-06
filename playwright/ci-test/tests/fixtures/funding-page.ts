import type { Page, Locator } from "@playwright/test";
import { TextList } from "./interfaces";

export class FundingPage {
    public readonly url: string = "/funding/donate/";
    public readonly pageBody: Locator;
    public readonly submitButton: Locator;
    public readonly currencyInput: Locator;
    public readonly donateButton: Locator;
    public readonly becomeSustainingMemberLink: Locator;
    public readonly sustainingMembershipDiv: Locator;
    public readonly sustainingMembershipSection: Locator;
    public readonly writeTrearurerLink: Locator;
    public readonly openSustainingMembersLink: Locator;
    public readonly textList: TextList[] = [
        {
            page: "Donate",
            texts: [
                "Sustaining Membership",
                "Payrexx Donation",
                "Bank transfer",
                "Paypal Donation",
                "Your support is vital to keep QGIS improving",
                "Enhanced Infrastructure & Development Support",
                "Maintaining Core Infrastructure",
                "Software Development & QA",
                "Community Growth & Engagement",
                "Empowering Our Volunteers",
                "Fostering Collaboration & Knowledge Sharing",
            ],
        },
        {
            page: "Membership",
            texts: [
                "Sustaining membership program",
                "How funds are used",
                "Membership levels",
                "€ 27,000+ ¶ Flagship Member",
                "€ 9,000+ ¶ Large Member",
                "€ 3,000+ ¶ Medium Member",
                "€ 500+ ¶ Small Member",
                "Sustaining membership benefits",
                "Public Acknowledgment ",
                "Enhanced Software Quality",
                "Keep QGIS Ad Free",
                "How become a sustaining member",
                "Initial Contact",
                "Clarification and Invoice Issuance",
                "Payment Verification",
                "Membership Management",
                "Recognition and Promotion",
                "Ongoing Engagement",
                "One-time payments",
                "About ‘earmarked’ funding",
                "Warning",
            ],
        },
    ];
    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.submitButton = this.page.locator("#payrexx-submit-button");
        this.currencyInput = this.page.locator("#payrexx-currency");
        this.donateButton = this.page.getByRole("button", { name: "Donate" });
        this.becomeSustainingMemberLink = this.page.getByRole("link", {
            name: "Become a Sustaining Member",
        });
        this.sustainingMembershipDiv = this.page
            .locator("div")
            .filter({
                hasText:
                    "Sustaining membership program Support the development of QGIS, an essential tool for the global GIS community.",
            })
            .nth(1);
        this.sustainingMembershipSection = this.page
            .locator("section")
            .filter({
                hasText:
                    "Sustaining membership program Support the development of QGIS, an essential tool for the global GIS community.",
            })
            .getByRole("link");
        this.writeTrearurerLink = this.page.getByRole("link", {
            name: "Write to treasurer",
        });
        this.openSustainingMembersLink = this.page.getByRole("link", {
            name: "Open Sustaining Members",
        });
    }
    async goto() {
        await this.page.goto(this.url);
    }
}

export class MembersPage {
    public readonly flagshipHeading: Locator;
    public readonly flagshipArticle: Locator;
    public readonly largeHeading: Locator;
    public readonly largeArticle: Locator;

    constructor(public readonly page: Page) {
        this.flagshipHeading = this.page.getByRole("heading", {
            name: "Flagship",
        });
        this.flagshipArticle = this.page
            .locator("article")
            .filter({ hasText: "Felt" });
        this.largeHeading = this.page.getByRole("heading", { name: "Large" });
        this.largeArticle = this.page
            .locator("article")
            .filter({ hasText: "Land Vorarlberg" });
    }
}

export class PastMembersPage {
    public readonly pageBody: Locator;
    public readonly textList: string[] = ["Past sustaining members"];

    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
    }
}
