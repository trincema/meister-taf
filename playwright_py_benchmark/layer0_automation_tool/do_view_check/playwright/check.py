from playwright.sync_api import expect
from .dvc import DoViewCheck

class Check(DoViewCheck):
    
    def visibility(locator: str, timeout = 60) -> None:
        """_summary_
        Assert that the element is visible within specified timeout.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 60.
        """
        expect(Check.page.locator(locator)).to_be_visible(timeout=timeout * 1000)
    
    def text(locator: str, expectedText: str, timeout = 60) -> None:
        """_summary_

        Args:
            locator (str): _description_
            expectedText (str): _description_
            timeout (int, optional): _description_. Defaults to 60.
        """
        expect(Check.page.locator(locator)).to_contain_text(expected=expectedText, timeout=timeout * 1000)