import { expect } from '@wdio/globals'
import LoginPage from '../pageobjects/login/login.page.js'
import ProfilePage from '../pageobjects/profile/profile.page.js';
import MindMeisterPlanPage from '../pageobjects/plans/mind-meister-plan.page.js';

class LoginKeywords {
    public static login(u: string, p: string) {

    }
}

enum LoginData {
    VALID_USERNAME = 'emanuel.trinc@yahoo.com',
    VALID_PASSWORD = 'Meister12345678'
}

describe('Login', () => {
    it('should login with valid credentials', async () => {
        LoginPage.open();
        LoginPage.waitUntilReady();

        LoginKeywords.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD);
        ProfilePage.backToMindMeister();
        MindMeisterPlanPage.chooseBasicPlan();
        
        LoginPage.logout();
    })
})
