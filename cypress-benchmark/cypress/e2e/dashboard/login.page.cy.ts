//This is spec file, inside your google-search.spec.ts
import { LoginLocators } from "../../support/page-objects/login/login.locators";

import LoginPage from "../../support/page-objects/login/login.page";
import Do from "../../support/do-view-check-wait/do";
import Check from "../../support/do-view-check-wait/check";
import Wait from "../../support/do-view-check-wait/wait";
import dashboardPage from "../../support/page-objects/dashboard/dashboard.page";
import mindMeisterPlanPage from "../../support/page-objects/mind-meister-plan/mind-meister-plan.page";

describe('Meister login page', () => {
    it('Should login', () => {
        cy.visit('https://accounts.meister.co/login');
        cy.viewport(1366, 768);

        LoginPage.waitUntilPageReady()
        LoginPage.acceptCookies();
        LoginPage.login('emanuel.trinc@yahoo.com', 'Meister12345678');
        dashboardPage.backToMindMeister();
        mindMeisterPlanPage.chooseBasicPlan();
        
        cy.origin('https://www.mindmeister.com', () => {
            const check = Cypress.require("../../support/do-view-check-wait/check");
            const Check = new check.Check();
            const dashboardLocators = Cypress.require("../../support/page-objects/dashboard/dashboard.locators");
            Check.haveText(dashboardLocators.DashboardLocators.NavItem, 'My Maps');
        });
    });
});