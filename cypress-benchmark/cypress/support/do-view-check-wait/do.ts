import check from "../../support/do-view-check-wait/check";
import wait from "../../support/do-view-check-wait/wait";

/**
 * Do: encapsulate all generic web-page action methods
*/
export class Do {

    /**
     * Input a given value in the text field with the given locator. Supported elements: <input>, <textarea>.
     * @param locator The given element locator.
     * @param value The given value to input in the text field.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public inputValue(locator: string, value: string, timeout = 60): void {
        cy.get(locator, { timeout: timeout * 1000 }).type(value, {force: true});
    }

    /**
     * Click the element with the given locator. Supported elements: <button>, <input>.
     * @param locator The given element locator.
     * @param value The given value to input in the text field.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public click(locator: string, timeout = 60) {
        cy.get(locator, { timeout: timeout * 1000 }).click();
    }

    /**
     * Click the element with the given locator. Supported elements: <button>, <input>.
     * @param locator The given element locator.
     * @param value The given value to input in the text field.
     * @param index The given index of the element to click on.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public clickByIndex(locator: string, index: number, timeout = 60) {
        cy.get(locator, { timeout: timeout * 1000 }).eq(index).click();
    }

}

export default new Do();