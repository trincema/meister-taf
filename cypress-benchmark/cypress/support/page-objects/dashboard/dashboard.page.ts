import Do from "../../do-view-check-wait/do";
import View from "../../do-view-check-wait/view";
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

    public getNavItemText(): string {
        return View.getText(DashboardLocators.NavItem);
    }
}

export default new DashboardPage();