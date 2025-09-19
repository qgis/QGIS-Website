import { test, expect } from "@playwright/test";

async function mockLocale(page, codes: string[]) {
    // Ensure our navigator locale overrides are present before any site scripts run
    await page.addInitScript((langs) => {
        try {
            Object.defineProperty(navigator, "languages", {
                get: () => langs,
                configurable: true,
            });
            Object.defineProperty(navigator, "language", {
                get: () => langs[0] || "en-US",
                configurable: true,
            });
        } catch (e) {
            // ignore
        }
    }, codes);
}

test.describe("Language redirect & threshold", () => {
    test("redirects to /nl/ for nl locale when coverage >= threshold", async ({ page }) => {
        await mockLocale(page, ["nl-NL", "nl"]);
        await page.goto("/?langredirdebug=1");
        // Should redirect to NL (coverage 100% in data/tx_coverage.json)
        await expect.poll(() => page.url(), { timeout: 3000 }).toContain("/nl/");
    });

    test("does not redirect for ro locale when coverage < threshold", async ({ page, baseURL }) => {
        await mockLocale(page, ["ro-RO", "ro"]);
        await page.goto("/?langredirdebug=1");
        // Should remain at root because RO coverage ~57% < default threshold 80
        await expect.poll(() => page.url(), { timeout: 1000 }).toBe(`${baseURL}/?langredirdebug=1`);
    });
});

test.describe("Debug logging flag", () => {
    test("no debug logs without query param", async ({ page, baseURL }) => {
        const logs: string[] = [];
        page.on("console", (msg) => {
            const t = msg.text();
            if (t.includes("[lang-redirect]")) logs.push(t);
        });
        // Use ro to avoid redirect and keep single page
        await mockLocale(page, ["ro-RO", "ro"]);
        await page.goto("/");
        await page.waitForTimeout(500);
        expect(logs.length).toBe(0);
        // Remains at root
        await expect.poll(() => page.url(), { timeout: 1000 }).toBe(`${baseURL}/`);
    });

    test("debug logs appear with ?langredirdebug=1", async ({ page }) => {
        const logs: string[] = [];
        page.on("console", (msg) => {
            const t = msg.text();
            if (t.includes("[lang-redirect]")) logs.push(t);
        });
        await mockLocale(page, ["ro-RO", "ro"]);
        await page.goto("/?langredirdebug=1");
        await page.waitForTimeout(500);
        expect(logs.length).toBeGreaterThan(0);
    });
});


