import re
from playwright.sync_api import Page, expect
import time


def test_login(page: Page):
    time.sleep(5)
    page.goto("https://accounts.meister.co/login")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Log In | Meister"))

    # Close Accept all
    acceptAllBtn = page.locator('css=a[id="cb-btn-ok"]')
    acceptAllBtn.click()

    # Fill credentials
    usernameField = page.locator('css=input[id="login_email_login"]')
    usernameField.fill('emanuel.trinc@yahoo.com')
    passwordField = page.locator('css=input[id="login_email_password"]')
    passwordField.fill('Meister12345678')
    # Login/Submit
    submit = page.locator('css=input[id="btn_signin"]')
    submit.click()

    # Click back to Mindmeister to go to Mind Meister plan
    backToMindMeister = page.locator('css=a[class="back-to-text"]')
    backToMindMeister.click(timeout=30000)

    # Click Basic Plan to go to Dashboard
    basicPlan = page.locator('css=button[class*="plan-card__button"]')
    basicPlan[0].click()

    navItem = page.locator('css=div[class="kr-text"]')
    navItem.click()

    time.sleep(10000)