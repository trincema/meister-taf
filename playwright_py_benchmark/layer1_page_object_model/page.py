from .page_locators import PageLocators
from ..layer0_automation_tool.playwright.do import Do
from ..layer0_automation_tool.playwright.view import View
from ..layer0_automation_tool.playwright.check import Check

class Page(Do, View, Check):
    def open_browser(url: str):
        """
        """
        Page.navigate(url)

