import type { Page, Locator } from "@playwright/test";

export class DownloadPage {
    public readonly url: string = "/";
    public readonly beforeDownloadText: Locator;
    public readonly oneTimePaymentText: Locator;
    public readonly tenEurosButton: Locator;
    public readonly twentyEurosButton: Locator;
    public readonly fiftyEurosButton: Locator;
    public readonly hundredEurosButton: Locator;
    public readonly twoFiftyEurosButton: Locator;
    public readonly submitButton: Locator;
    public readonly otherMethodsLink: Locator;
    public readonly currencyInput: Locator;
    public readonly skipDownloadButton: Locator;
    public readonly beforeDownloadHeading: Locator;
    public readonly otherPlatformsHeading: Locator;

    constructor(public readonly page: Page) {
        this.beforeDownloadText = this.page.getByText(
            "Before download starts ¶ QGIS",
        );
        this.oneTimePaymentText = this.page.getByText(
            "One-Time Payment € 10.00 € 20",
        );
        this.tenEurosButton = this.page.getByText("$ 10.00");
        this.twentyEurosButton = this.page.getByText("$ 20.00");
        this.fiftyEurosButton = this.page.getByText("$ 50.00");
        this.hundredEurosButton = this.page.getByText("$ 100.00");
        this.twoFiftyEurosButton = this.page.getByText("$ 250.00");
        this.submitButton = this.page.locator("#submit-button");
        this.otherMethodsLink = this.page.getByRole("link", {
            name: "Other methods, more info",
        });
        this.currencyInput = this.page.locator("#currency");
        this.skipDownloadButton = this.page.getByRole("button", {
            name: "Skip it and go to download",
        });
        this.beforeDownloadHeading = this.page.getByRole("heading", {
            name: "Download QGIS for your",
        });
        this.otherPlatformsHeading = this.page.getByRole("heading", {
            name: "Other platforms",
        });
    }
}
