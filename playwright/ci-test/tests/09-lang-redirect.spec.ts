import { test, expect } from "@playwright/test";

// NOTE: We use test.use({ locale }) rather than Object.defineProperty(navigator, 'languages')
// because Playwright's Chromium does not reliably allow overriding navigator.languages via
// Object.defineProperty — failures are swallowed by try/catch, leaving the headless browser's
// default "en-US" locale in place and preventing any redirect from firing.

test.describe("Language redirect & threshold", () => {

    test.describe("redirects to /nl/ for nl locale when coverage >= threshold", () => {
        test.use({ locale: "nl-NL" });

        test("redirects to /nl/ for nl locale when coverage >= threshold", async ({ page }) => {
            await page.goto("/?langredirdebug=1");
            // NL coverage is 100% which is >= 35% threshold
            await expect.poll(() => page.url(), { timeout: 3000 }).toContain("/nl/");
        });
    });

    test.describe("does not redirect for de locale when coverage < threshold", () => {
        test.use({ locale: "de-DE" });

        test("does not redirect for de locale when coverage < threshold", async ({ page, baseURL }) => {
            await page.goto("/?langredirdebug=1");
            // DE coverage is ~23% which is below the 35% threshold
            await expect.poll(() => page.url(), { timeout: 1000 }).toBe(`${baseURL}/?langredirdebug=1`);
        });
    });
});

test.describe("Debug logging flag", () => {
    // Use a locale below the threshold (DE ~23%) so no redirect occurs and the
    // test stays on the navigated URL. RO was used previously but its coverage
    // (~57%) is now above the 35% threshold, which would trigger a redirect.
    test.use({ locale: "de-DE" });

    test("no debug logs without query param", async ({ page, baseURL }) => {
        const logs: string[] = [];
        page.on("console", (msg) => {
            const t = msg.text();
            if (t.includes("[lang-redirect]")) logs.push(t);
        });
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
        await page.goto("/?langredirdebug=1");
        await page.waitForTimeout(500);
        expect(logs.length).toBeGreaterThan(0);
    });
});
