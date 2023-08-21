import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://accounts.meister.co/login');
  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle("Log In | Meister");

  const username = await page.$('input[id="login_email_login"]');
  await username.fill('emanuel.trinc@yahoo.com');
  const pass = await page.$('input[id="login_email_password"]');
  await pass.fill('Meister12345678');
  const acceptAll = await page.$('a[id="cb-btn-ok"]');
  await acceptAll.click();
  const submit = await page.$('input[id="btn_signin"]');
  await submit.click();
  
  //const email = await page.$('input[name="email"]');
  //await email.fill('myemail');
  //await expect(page).toHaveURL('https://accounts.meister.co/password_reset');
  //const submit = await page.$('input[id="btn_signin"]');
  //await submit.click();
  //await submit.click();
  //await page.waitForURL("https://accounts.meister.co/");
  
});
