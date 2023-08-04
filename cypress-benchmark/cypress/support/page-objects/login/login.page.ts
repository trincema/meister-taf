//Inside your google-search.page.ts file. This is pageobject file.
/// <reference types="cypress" />

import { LoginLocators } from "./login.locators";

import Do from "../../do-view-check-wait/do";
import Check from "../../do-view-check-wait/check";
import Wait from "../../do-view-check-wait/wait";

export class LoginPage {

    /**
     * Waiting until Login page is ready to be interacted with.
    */
    public waitUntilPageReady(timeout = 60): void {
        Wait.elementToBePresent(LoginLocators.UsernameField, timeout);
        Wait.elementToBePresent(LoginLocators.PasswordField, timeout);
        Wait.elementToBePresent(LoginLocators.Submit, timeout);
    }

    /**
     * Login to the Meister page.
    */
    public login(username: string, password: string): void {
        Do.inputValue(LoginLocators.UsernameField, username);
        Do.inputValue(LoginLocators.PasswordField, password);
        Do.click(LoginLocators.Submit);
    }

    public logout(): void {

    }

    public acceptCookies() {
        Do.click(LoginLocators.CookieOk);
        Wait.elementToBeAbsent(LoginLocators.CookieOk);
    }

}

export default new LoginPage();