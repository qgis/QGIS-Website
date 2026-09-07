import type { Page, Locator } from "@playwright/test";

/**
 * The site-wide footer. Groups mirror the primary navigation, so a link that
 * disappears here is usually a sign a whole content section has gone missing.
 */
export class Footer {
    public readonly root: Locator;

    /** Footer links that must resolve to a real page (not a 404). */
    public static readonly links: { label: string; href: string }[] = [
        { label: "OSGeo Projects", href: "/projects" },
        { label: "Community Projects", href: "/projects/community" },
        { label: "Incubation", href: "/about/incubation" },
        { label: "OSGeoLive", href: "/initiatives/osgeolive" },
        { label: "Get Started", href: "/community/getting-started" },
        { label: "Local Chapters", href: "/local-chapters" },
        { label: "Mailing Lists", href: "/community/mailing-lists" },
        { label: "Code of Conduct", href: "/community/code-of-conduct" },
        { label: "Service Providers", href: "/service-providers" },
        { label: "FOSS4G", href: "/initiatives/foss4g" },
        { label: "Geo for All", href: "/initiatives/geo-for-all" },
        { label: "Google Summer of Code", href: "/initiatives/gsoc" },
        { label: "Events", href: "/events" },
        { label: "About OSGeo", href: "/about" },
    ];

    constructor(public readonly page: Page) {
        this.root = page.locator("footer").first();
    }

    link(label: string): Locator {
        return this.root.getByRole("link", { name: label, exact: true }).first();
    }
}
