import type { Page, Locator } from "@playwright/test";

/**
 * /search/ -- client-side search backed by the home page's JSON output.
 */
export class SearchPage {
    public readonly url: string = "/search/";
    public readonly heading: Locator;
    public readonly input: Locator;
    public readonly results: Locator;
    /** Echoes the ?q= parameter; the input itself is not pre-filled. */
    public readonly queryDisplay: Locator;

    constructor(public readonly page: Page) {
        this.heading = page.getByRole("heading", { name: "Search Results", level: 1 });
        // The navbar renders a search box too; the page's own box is the last one.
        this.input = page.locator("input#search-query").last();
        this.results = page.locator("#search-results");
        this.queryDisplay = page.locator("#search-query-text");
    }

    async goto(query?: string): Promise<void> {
        await this.page.goto(query ? `${this.url}?q=${encodeURIComponent(query)}` : this.url);
    }
}
