import { $ } from '@wdio/globals'
import { Page } from '../page.js';
import { LoginLocators } from './login.locators.js';

/**
 * sub page containing specific selectors and methods for a specific page
 */
class LoginPage extends Page {
    /**
     * define selectors using getter methods
     */
    public get inputUsername () {
        return $(LoginLocators.UsernameField);
    }

    public get inputPassword () {
        return $(LoginLocators.PasswordField);
    }

    public get btnSubmit () {
        return $(LoginLocators.Submit);
    }

    /**
     * overwrite specific options to adapt it to page object
     */
    public open() {
        super.navigate(LoginLocators.Url);
        super.setBrowserSize(1920, 1200);
    }

    /**
     * a method to encapsule automation code to interact with the page
     * e.g. to login using username and password
     */
    public async login (username: string, password: string) {
        await this.inputUsername.setValue(username);
        await this.inputPassword.setValue(password);
        await this.btnSubmit.click();
    }

    public async waitUntilReady() {
        await super.waitUntilPageContains(LoginLocators.UsernameField);
        await super.waitUntilPageContains(LoginLocators.PasswordField);
        await super.waitUntilElementIsClickable(LoginLocators.Submit);
        await super.acceptCookies();
    }

    public async sleep(seconds: number) {
        return browser.pause(seconds * 1000);
    }
    
    /**
     * Generic method to pause the current execution a given number of seconds.
     * @param seconds The given number of seconds to pause the current execution.
     */
    public async sleepMilis(milliseconds: number): Promise<void> {
        await browser.pause(milliseconds);
    }
}

export default new LoginPage();
