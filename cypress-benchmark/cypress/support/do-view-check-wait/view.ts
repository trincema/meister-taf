/**
 * View: encapsulate all generic web-page query methods
*/
export class View {
    public getText(locator: string): string {
        const text = cy.get(locator).innerText;
        return text;
    }
}

export default new View();