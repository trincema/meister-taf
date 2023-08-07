import { Page } from "../page.js";
import { ProfileLocators } from './profile.locators.js';

export class ProfilePage extends Page {
    /**
     * 
    */
    public async backToMindMeister() {
        await super.click(ProfileLocators.BackToMindMeister);
    }
}

export default new ProfilePage();