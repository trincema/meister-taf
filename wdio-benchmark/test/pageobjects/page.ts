import { $ } from '@wdio/globals';
import { browser } from '@wdio/globals';
import { LoginLocators } from './login/login.locators.js';

/**
* main page object containing all methods, selectors and functionality
* that is shared across all page objects
*/
export class Page {

    /**
    * Opens a sub page of the page
    * @param path path of the sub page (e.g. /path/to/page.html)
    */
    public navigate(url: string) {
        return browser.url(url);
    }

    public setBrowserSize(width: number, height: number) {
        browser.setWindowSize(width, height);
    }

    /**
    * Opens a sub page of the page
    * @param path path of the sub page (e.g. /path/to/page.html)
    */
    public navigateSubpage(path: string) {
        return browser.url(`https://the-internet.herokuapp.com/${path}`)
    }

    /**
     * Generic click element method, which also includes a waiting mechanism to make sure the element
     * exists on the page, enabled and clickable.
     * @param locator Element locator as string, could be a css locator.
     * @param scroll Flag to scroll or not to scroll to the element before click, default to false.
     * @param timeout Timeout to wait for element to be interactable, default being 1 minute.
     */
    public async click(
        locator: string,
        clickable: boolean = true,
        scroll: boolean = true,
        timeout: number = 60
    ): Promise<void> {
        const element = await $(locator);
        await element.waitForExist({ timeout: timeout * 1000 });
        if (scroll) {
            await element.scrollIntoView();
        }
        await element.waitForEnabled({ timeout: timeout * 1000 });
        if (clickable) {
            await element.waitForClickable({ timeout: timeout * 1000 });
        }
        await element.click();
    }

    /**
     * Click specific element from a list of elements all identified by the same given locator.
     *
     */
    public async clickByIndex(locator: string, index: number, clickable: boolean = true, timeout: number = 60): Promise<void> {
        let element = await $$(locator)[index];
        while (element === undefined) {
            await browser.pause(250);
            element = await $$(locator)[index];
        }
        await element.waitForExist({ timeout: timeout * 1000 });
        await element.waitForEnabled({ timeout: timeout * 1000 });
        if (clickable) {
            await element.waitForClickable({ timeout: timeout * 1000 });
        }
        await element.scrollIntoView();
        return element.click();
    }

    /**
     * 
    */
    public async acceptCookies() {
        await this.waitUntilElementIsClickable(LoginLocators.CookieOk);
        await this.click(LoginLocators.CookieOk);
    }

    /**
     * Generic method to wait for an element to be visible in SUT.
     * @param locator Element locator as string, could be a css locator.
     * @param timeout Timeout to wait for element to be visible, default being 1 minute.
     */
    public async waitUntilElementIsVisible(locator: string, timeout: number = 60) {
        const element = await $(locator);
        await element.waitForDisplayed({ timeout: timeout * 1000 });
    }

    /**
     * Wait until page contains a given element.
     */
    public async waitUntilPageContains(element, timeout: number = 60) {
        const elementInstance = await $(element);
        return elementInstance.waitForExist({
            timeout: timeout * 1000
        });
    }

    /**
     * Generic method to wait for an element to be clickable in SUT.
     * @param locator Element locator as string, could be a css locator.
     * @param timeout Timeout to wait for element to be clickable, default being 1 minute.
     */
    public async waitUntilElementIsClickable(locator: string, timeout: number = 60) {
        const element = await $(locator);
        await element.waitForEnabled({ timeout: timeout * 1000 });
        await element.waitForClickable({ timeout: timeout * 1000 });
    }

}

export default new Page();