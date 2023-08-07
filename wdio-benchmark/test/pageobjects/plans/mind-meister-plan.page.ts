import { Page } from "../page.js";
import { MindMeisterPlan } from "./mind-meister-plan.js";
import { MindMeisterLocators } from "./mind-meister-plan.locators.js";

export class MindMeisterPlanPage extends Page {

    public async choosePlan(plan: MindMeisterPlan) {
        await super.click(MindMeisterLocators.ChooseProfileButton);
    }

    public async chooseBasicPlan() {
        await super.clickByIndex(MindMeisterLocators.ChooseProfileButton, MindMeisterPlan.Basic);
    }

    public async choosePersonalPlan() {
        await super.clickByIndex(MindMeisterLocators.ChooseProfileButton, MindMeisterPlan.Personal);
    }

    public async chooseProPlan() {
        await super.clickByIndex(MindMeisterLocators.ChooseProfileButton, MindMeisterPlan.Pro);
    }

    public async chooseBusinessPlan() {
        await super.clickByIndex(MindMeisterLocators.ChooseProfileButton, MindMeisterPlan.Business);
    }

    public async waitForPageReady() {
        await super.waitUntilElementIsClickable(MindMeisterLocators.ChooseProfileButton);
    }
}

export default new MindMeisterPlanPage();