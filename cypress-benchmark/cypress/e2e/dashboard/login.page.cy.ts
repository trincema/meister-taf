//This is spec file, inside your google-search.spec.ts
import { LoginLocators } from "../../support/page-objects/login/login.locators";

import LoginPage from "../../support/page-objects/login/login.page";
import Do from "../../support/do-view-check-wait/do";
import Check from "../../support/do-view-check-wait/check";
import Wait from "../../support/do-view-check-wait/wait";

describe('Meister login page', () => {
    it('Should login', () => {
        cy.visit(LoginLocators.Url);
        cy.viewport(1366, 768);

        LoginPage.waitUntilPageReady()
        LoginPage.acceptCookies();
        LoginPage.login('emanuel.trinc@yahoo.com', 'Emi25##1988');
        Wait.sleep(5);
        cy.origin('https://www.mindmeister.co', () => {
            const dashboardPage = Cypress.require("../../support/page-objects/dashboard/dashboard.page");
            const DashboardPage = new dashboardPage.DashboardPage();
            DashboardPage.backToMindMeister();
            cy.origin('https://accounts.meister.co', () => {
                //const mindMeisterPlanPage = Cypress.require("../../support/page-objects/mind-meister-plan/mind-meister-plan.page");
                //mindMeisterPlanPage.MindMeisterPlanPage.chooseBasicPlan();
            });
        });
    });
});