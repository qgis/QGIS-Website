import type { Page, Locator } from "@playwright/test";

/**
 * The site-wide Bulma navbar rendered by the theme's header partial.
 */
export class Header {
    public readonly navbar: Locator;
    public readonly brand: Locator;
    public readonly brandLogo: Locator;
    public readonly burger: Locator;
    public readonly menu: Locator;

    /** Top-level nav entries, in the order the theme renders them. */
    public static readonly topLevelItems: string[] = [
        "Projects",
        "Initiatives",
        "Community",
        "About",
        "News",
    ];

    constructor(public readonly page: Page) {
        this.navbar = page.locator("nav.navbar");
        this.brand = this.navbar.locator(".navbar-brand");
        this.brandLogo = this.brand.locator("img").first();
        this.burger = this.navbar.locator(".navbar-burger");
        this.menu = this.navbar.locator(".navbar-menu");
    }

    /** A top-level navbar link by its visible label. */
    navLink(label: string): Locator {
        return this.navbar.getByRole("link", { name: label, exact: true }).first();
    }
}
