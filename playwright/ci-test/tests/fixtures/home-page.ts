import type { Page, Locator } from "@playwright/test";

/**
 * The OSGeo landing page: hero headline, the four data-driven hero stats and
 * the main content sections.
 */
export class HomePage {
    public readonly url: string = "/";
    public readonly hero: Locator;
    public readonly headline: Locator;
    public readonly headlineWords: Locator;
    public readonly statCards: Locator;
    public readonly statNumbers: Locator;
    public readonly statLabels: Locator;

    /**
     * Hero stat labels. The numbers themselves are derived from data/*.yaml at
     * build time, so the tests assert on shape rather than exact values.
     */
    public static readonly statLabels: string[] = [
        "Open Source Projects",
        "Devices Worldwide",
        "Years Powering Maps",
        "Users Globally",
    ];

    /** Section headings that make up the page narrative. */
    public static readonly sectionHeadings: string[] = [
        "Invisible Infrastructure, Global Impact",
        "The Software Behind the Maps",
        "Global Initiatives",
        "Join Our Global Community",
        "Be Part of Something Bigger",
    ];

    constructor(public readonly page: Page) {
        this.hero = page.locator(".osgeo-hero");
        this.headline = page.locator("h1.hero-headline");
        this.headlineWords = this.headline.locator(".headline-word");
        this.statCards = page.locator(".hero-stat-card");
        this.statNumbers = page.locator(".hero-stat-card .stat-number");
        this.statLabels = page.locator(".hero-stat-card .stat-label");
    }

    async goto(): Promise<void> {
        await this.page.goto(this.url);
    }
}
