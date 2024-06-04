import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://127.0.0.1:1313/');
  await page.getByLabel('main navigation').getByRole('link', { name: 'Releases' }).click();
  await page.getByRole('heading', { name: 'Release Archive ¶' }).click();
  await expect(page.getByRole('heading', { name: 'Release Archive ¶' })).toBeVisible();
  await expect(page.getByRole('link', { name: 'QGIS.org hosted downloads' })).toBeVisible();
  await expect(page.getByRole('link', { name: 'Older releases for macOS / OS' })).toBeVisible();
  await expect(page.getByRole('link', { name: 'OSGeo hosted downloads' })).toBeVisible();
  await expect(page.getByRole('link', { name: 'at plugins.qgis.org' })).toBeVisible();
});