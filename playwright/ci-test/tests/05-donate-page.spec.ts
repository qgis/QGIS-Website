import { test, expect } from '@playwright/test';

let url = '/';

test('donate page', async ({ page }) => {
  await page.goto(url);
  await page.locator('section').filter({ hasText: 'Free and open source Spatial' }).getByRole('link').click();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Funding' })).toBeVisible();
  await page.locator('#sidebar').getByRole('link', { name: 'Funding' }).click();
  await expect(page.getByText('QGIS is developed by a team')).toBeVisible();
  await expect(page.getByText('We rely on sponsorships and')).toBeVisible();
  await expect(page.getByText('Donations to QGIS are tax-')).toBeVisible();
  await expect(page.getByText('We use the stripe')).toBeVisible();
  // the following options are one-time payments and are hidden by default
  await expect(page.getByText('$ 10.00').first()).toBeHidden();
  await expect(page.getByText('$ 20.00').first()).toBeHidden();
  await expect(page.getByText('$ 50.00').first()).toBeHidden();
  await expect(page.getByText('$ 100.00').first()).toBeHidden();
  await expect(page.getByText('$ 250.00').first()).toBeHidden();
  await expect(page.locator('#submit-button')).toBeVisible();
  await expect(page.locator('#currency')).toBeVisible();
  await expect(page.getByText('Bank transfer ¶ Use the')).toBeVisible();
  await expect(page.getByText('Account name: QGIS.ORG')).toBeVisible();
  await expect(page.getByText('You can use Paypal')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Donate' })).toBeVisible();
});
