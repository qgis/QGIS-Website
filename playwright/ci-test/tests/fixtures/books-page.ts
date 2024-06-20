import type { Page, Locator } from "@playwright/test";

export class BooksPage {
    public readonly pageBody: Locator;
    public readonly contactLink: Locator;
    public readonly textList: string[] = [
        "Books",
        "English",
        "Chinese",
        "Dutch",
        "French",
        "Greek",
        "Japanese",
        "Polish",
        "Turkish",
    ];
    constructor(public readonly page: Page) {
        this.pageBody = this.page.locator("body");
        this.contactLink = this.page.getByRole("link", {
            name: "psc@qgis.org",
        });
    }
}
