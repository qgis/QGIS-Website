import type { Page, Locator } from "@playwright/test";

/** A plain content page, identified by its path, <title> and <h1>. */
export interface ContentPageSpec {
    path: string;
    title: string;
    heading: string;
}

/**
 * Generic page object for the many straightforward content pages, so each one
 * does not need a bespoke fixture.
 */
export class ContentPage {
    constructor(
        public readonly page: Page,
        public readonly spec: ContentPageSpec,
    ) {}

    async goto(): Promise<void> {
        await this.page.goto(this.spec.path);
    }

    get heading(): Locator {
        return this.page.getByRole("heading", { name: this.spec.heading, level: 1 }).first();
    }

    get body(): Locator {
        return this.page.locator("body");
    }
}

/**
 * The content pages covered by the smoke suite. Titles and headings are taken
 * from the rendered site; a mismatch means content or a layout has moved.
 */
export const contentPages: ContentPageSpec[] = [
    { path: "/about/", title: "About OSGeo", heading: "About OSGeo - OSGeo" },
    { path: "/community/", title: "Community - OSGeo", heading: "Community - OSGeo" },
    { path: "/initiatives/", title: "Initiatives - OSGeo", heading: "Initiatives - OSGeo" },
    { path: "/local-chapters/", title: "Local Chapters", heading: "Local Chapters" },
    { path: "/service-providers/", title: "Service Providers", heading: "Service Providers" },
    { path: "/news/", title: "News & Announcements", heading: "News & Announcements" },
];
