import { test, expect } from '@playwright/test';

let url = '/';

test('download page', async ({ page }) => {
  await page.goto(url);
  await page.locator('section').filter({ hasText: 'Free and open source Spatial' }).getByRole('link').click();
  await expect(page.getByText('Before download starts ¶ QGIS')).toBeVisible();
  // the following options are one-time payments and are hidden by default
  await expect(page.getByText('$ 10.00').first()).toBeHidden();
  await expect(page.getByText('$ 20.00').first()).toBeHidden();
  await expect(page.getByText('$ 50.00').first()).toBeHidden();
  await expect(page.getByText('$ 100.00').first()).toBeHidden();
  await expect(page.getByText('$ 250.00').first()).toBeHidden();
  await expect(page.locator('#submit-button')).toBeVisible();
  await expect(page.getByRole('link', { name: 'Other methods, more info' })).toBeVisible();
  await expect(page.locator('#currency')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Skip it and go to download' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Product' })).toBeVisible();
  await expect(page.locator('#sidebar div').filter({ hasText: 'Product' }).locator('span')).toBeVisible();
  await page.locator('#sidebar div').filter({ hasText: 'Product' }).locator('span').click();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Overview' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Case studies' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Plugins' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Visual Changelogs' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Community' })).toBeVisible();
  await expect(page.locator('#sidebar div').filter({ hasText: 'Community' }).locator('span')).toBeVisible();
  await page.locator('#sidebar div').filter({ hasText: 'Community' }).locator('span').click();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Get involved' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Become a certified member' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'QGIS Foundation' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Project Organisation' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Members Blogs' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Funding' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Download' })).toBeVisible();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'Resources', exact: true })).toBeVisible();
  await expect(page.locator('#sidebar div').filter({ hasText: 'Resources' }).locator('span')).toBeVisible();
  await page.locator('#sidebar div').filter({ hasText: 'Resources' }).locator('span').click();
  await expect(page.locator('#sidebar').getByRole('link', { name: 'QGIS resources' })).toBeVisible();
  await page.getByRole('button', { name: 'Skip it and go to download' }).click();
  await expect(page.getByRole('heading', { name: 'Download QGIS for your' })).toBeVisible();
  await page.getByRole('heading', { name: 'Other platforms' }).click();
  await expect(page.getByRole('heading', { name: 'Other platforms' })).toBeVisible();
});
