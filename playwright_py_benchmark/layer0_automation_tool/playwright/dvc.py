from enum import Enum
from playwright.sync_api import Page, Locator

class By(Enum):
    Locator = 0,
    Text = 1
    
class DoViewCheck:
    page: Page = None
    
    def locate_element(by: By, locator: str, timeout=30) -> Locator:
        """Summary:
        Locate and return the element by given locator and locator method By.
        Args:
            by (By): _description_
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.

        Returns:
            Locator: _description_
        """
        match by:
            case By.Locator:
                element: Locator = DoViewCheck.page.locator(locator)
                return element
            case By.Text:
                element: Locator = DoViewCheck.page.get_by_text(locator)
                return element