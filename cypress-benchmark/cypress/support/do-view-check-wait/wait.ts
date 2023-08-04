/**
 * Wait: encapsulate all generic web-page wait methods.
*/
export class Wait {
    /**
     * Sleep for a certain given amount of time, default is 30s.
    */
    public sleep(timeout = 30): void {
        cy.wait(timeout * 1000)
    }

    /**
     * Wait until a certain element is visible on the web page.
     * @param locator The given element locator.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public elementToBeVisible(locator: string, timeout = 60) {
        cy.get(locator, { timeout: timeout * 1000 }).should('be.visible');
    }

    /**
     * Wait until a certain element is present on the web page.
     * @param locator The given element locator.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public elementToBePresent(locator: string, timeout = 30) {
        cy.get(locator, { timeout: timeout * 1000 }).should('exist');
    }

    /**
     * Wait until a certain element is visible on the web page.
     * @param locator The given element locator.
     * @param timeout The timeout to get the element, default to 30s.
    */
    public elementToBeAbsent(locator: string, timeout = 60) {
        cy.get(locator, { timeout: timeout * 1000 }).should('not.exist');
    }
}

export default new Wait()