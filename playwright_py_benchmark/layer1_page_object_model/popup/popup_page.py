from playwright.sync_api import Page
from playwright_py_benchmark.layer1_page_object_model.page import Page
from ..page import Page
from .popup_locators import PopupLocators

class PopupPage(Page):

    class Cookies:
        def accept_all():
            """
            Click 'Accept All' button dialog.
            """
            PopupPage.page.locator(PopupLocators.ACCELP_ALL).click()
        
        def customize():
            """
            Click 'Customize' button.
            """
            PopupPage.page.locator(PopupLocators.CUSTOMIZE).click()
