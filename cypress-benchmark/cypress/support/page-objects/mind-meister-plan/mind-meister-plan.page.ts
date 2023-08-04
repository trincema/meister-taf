import { MindMeisterPlan } from "./mind-meister-plan";
import { MindMeisterLocatorsLocators } from "./mind-meister-plan.locators";

import Do from "../../do-view-check-wait/do";

export class MindMeisterPlanPage {

    public choosePlan(plan: MindMeisterPlan): void {
        Do.click(MindMeisterLocatorsLocators.ChooseProfileButton);
    }

    public chooseBasicPlan(plan: MindMeisterPlan): void {
        Do.clickByIndex(MindMeisterLocatorsLocators.ChooseProfileButton, MindMeisterPlan.Basic);
    }

    public choosePersonalPlan(plan: MindMeisterPlan): void {
        Do.clickByIndex(MindMeisterLocatorsLocators.ChooseProfileButton, MindMeisterPlan.Personal);
    }

    public chooseProPlan(plan: MindMeisterPlan): void {
        Do.clickByIndex(MindMeisterLocatorsLocators.ChooseProfileButton, MindMeisterPlan.Pro);
    }

    public chooseBusinessPlan(plan: MindMeisterPlan): void {
        Do.clickByIndex(MindMeisterLocatorsLocators.ChooseProfileButton, MindMeisterPlan.Business);
    }
}

export default new MindMeisterPlanPage();