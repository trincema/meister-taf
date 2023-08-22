from playwright.sync_api import expect
from .dvc import DoViewCheck
from .dvc import By

class Check(DoViewCheck):
    
    def visibility(locator: str, by=By.Locator, index=0, timeout = 60) -> None:
        """_summary_

        Args:
            locator (str): _description_
            by (_type_, optional): _description_. Defaults to By.Locator.
            index (int, optional): _description_. Defaults to 0.
            timeout (int, optional): _description_. Defaults to 60.
        """
        match by:
            case By.Locator:
                expect(Check.page.locator(locator).all()[index]).to_be_visible(timeout=timeout * 1000)
            case By.Text:
                expect(Check.page.get_by_text(locator).all()[index]).to_be_visible(timeout=timeout * 1000)
    
    def invisibility(locator: str, timeout = 60) -> None:
        """_summary_
        Assert that the element is visible within specified timeout.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 60.
        """
        expect(Check.page.locator(locator)).to_be_hidden(timeout=timeout * 1000)
    
    def text(locator: str, expectedText: str, timeout = 60) -> None:
        """_summary_

        Args:
            locator (str): _description_
            expectedText (str): _description_
            timeout (int, optional): _description_. Defaults to 60.
        """
        expect(Check.page.locator(locator)).to_contain_text(expected=expectedText, timeout=timeout * 1000)
    