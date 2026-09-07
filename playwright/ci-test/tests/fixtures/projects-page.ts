import type { Page, Locator } from "@playwright/test";

/**
 * /projects/ -- the filterable gallery driven by data/projects.yaml.
 */
export class ProjectsPage {
    public readonly url: string = "/projects/";
    public readonly heading: Locator;
    public readonly cards: Locator;
    public readonly filterButtons: Locator;

    /** Category slugs defined in data/projects.yaml. */
    public static readonly categories: string[] = [
        "catalog",
        "cms",
        "database",
        "desktop",
        "distribution",
        "library",
        "testing",
        "web",
    ];

    constructor(public readonly page: Page) {
        this.heading = page.getByRole("heading", { name: "OSGeo Projects", level: 1 });
        this.cards = page.locator("a.project-card-clean[data-category]");
        this.filterButtons = page.locator("button[data-filter]");
    }

    async goto(): Promise<void> {
        await this.page.goto(this.url);
    }

    filterButton(category: string): Locator {
        return this.page.locator(`button[data-filter="${category}"]`);
    }

    cardsInCategory(category: string): Locator {
        return this.page.locator(`a.project-card-clean[data-category="${category}"]`);
    }

    /** Cards currently visible to the user, i.e. not hidden by a filter. */
    async visibleCardCount(): Promise<number> {
        return await this.cards.locator("visible=true").count();
    }
}
