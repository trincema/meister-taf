from enum import Enum
from .dvc import DoViewCheck
from .dvc import By
from .check import Check

class ClickMissfire(Enum):
    NONE = 0,
    WAIT_FOR_INVISIBLE = 1,
    

class Do(DoViewCheck):
    def navigate(url: str):
        """
        """
        Do.page.goto(url)
    
    def click(locator: str, by=By.Locator, issue=ClickMissfire.NONE, timeout=30):
        """_summary_

        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        Do.click_by(by, locator)
        if issue == ClickMissfire.WAIT_FOR_INVISIBLE:
            while True:
                try:
                    Check.invisibility(locator, 5)
                    break
                except:
                    Do.click_by(by, locator)
    
    def click_by(by: By, locator: str, timeout=30) -> None:
        """_summary_

        Args:
            by (By): _description_
            locator (str): _description_
        """
        match by:
            case By.Locator:
                Do.page.locator(locator).click(timeout=timeout * 1000)
            case By.Text:
                Do.page.get_by_text(locator).all()[0].click(timeout=timeout * 1000)
    
    def click_by_index(locator: str, index = 0, timeout=30):
        """_summary_

        Args:
            locator (str): _description_
            index (int, optional): _description_. Defaults to 0.
            timeout (int, optional): _description_. Defaults to 30.
        """
        Do.page.locator(locator + f' >> nth={index}').click(timeout=timeout * 1000)
    
    def click_with_parent(parent_locator: str, element_locator: str, timeout=30):
        """_summary_

        Args:
            parent_locator (str): _description_
            element_locator (strtimeout, optional): _description_. Defaults to 30.
        """
        Do.page.locator(parent_locator).locator(element_locator).click(timeout=timeout * 1000)
    
    def input_value(locator: str, value: str, timeout=30):
        """_summary_

        Args:
            locator (str): _description_
            value (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        Do.page.locator(locator).fill(value, timeout=timeout * 1000)