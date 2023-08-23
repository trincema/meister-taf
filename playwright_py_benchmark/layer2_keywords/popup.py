from ..layer0_automation_tool.playwright.wait import Wait
from ..layer1_page_object_model.popup.popup_page import PopupPage
from ..layer1_page_object_model.popup.popup_locators import PopupLocators

class PopupKeywords:
    class Cookies:
        def close_accept_all():
            """
            Close 'Accept All' dialog.
            """
            PopupPage.Cookies.accept_all()
            Wait.invisibility(PopupLocators.ACCELP_ALL)
            Wait.removal(PopupLocators.ACCELP_ALL)