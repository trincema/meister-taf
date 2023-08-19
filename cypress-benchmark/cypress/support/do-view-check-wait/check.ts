/**
 * Check: encapsulate all generic web-page assert methods
*/
export class Check {
    /**
     * Assert that a certain number of elements are present on the page.
     * @param locator The locator of the elements to query.
     * @param expectedLength The expected length of elements.
     * @param timeout The timeout to get the elements, default to 30s.
    */
    public haveLength(locator: string, expectedLength: number, timeout = 30): void {
        cy.get(locator, {timeout: timeout * 1000}).should('have.length', expectedLength);
    }

    /**
     * Assert that a certain number of elements are present on the page.
     * @param locator The locator of the elements to query.
     * @param expectedText The expected text of the given element.
     * @param index (Optional) The index of the element, default 0
     * @param timeout (Optional) The timeout to get the elements, default to 30s.
    */
    public haveText(locator: string, expectedText: string, index: number = 0, timeout = 30): void {
        cy.get(locator, {timeout: timeout * 1000}).eq(index).should('have.text', expectedText);
    }

    /**
     * Assert that a certain element is visible.
     * @param locator The locator of the elements to query.
     * @param timeout The timeout to get the elements, default to 30s
    */
    public visible(locator: string, timeout = 30) {
        cy.get(locator, { timeout: timeout * 1000 }).should('be.visible');
    }
}

export default new Check();