import { expect } from '@wdio/globals'
import LoginPage from '../pageobjects/login/login.page.js'
import ProfilePage from '../pageobjects/profile/profile.page.js';
import MindMeisterPlanPage from '../pageobjects/plans/mind-meister-plan.page.js';

describe('My Login application', () => {
    it('should login with valid credentials', async () => {
        await LoginPage.open();
        await LoginPage.waitUntilReady();

        await LoginPage.login('emanuel.trinc@yahoo.com', 'Meister12345678');
        await ProfilePage.backToMindMeister();
        await MindMeisterPlanPage.chooseBasicPlan();
        await LoginPage.sleep(100000);
    })
})
