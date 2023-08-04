import Do from "../../do-view-check-wait/do";
import Check from "../../do-view-check-wait/check";
import Wait from "../../do-view-check-wait/wait";
import { DashboardLocators } from "./dashboard.locators";

export class DashboardPage {
    /**
     * 
    */
    public backToMindMeister() {
        Do.click(DashboardLocators.BackToMindMeister);
    }
}

export default new DashboardPage();