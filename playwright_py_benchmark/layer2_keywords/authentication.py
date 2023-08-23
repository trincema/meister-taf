from ..layer0_automation_tool.playwright.check import Check
from ..layer0_automation_tool.playwright.wait import Wait
from ..layer1_page_object_model.popup.popup_page import PopupPage
from ..layer1_page_object_model.popup.popup_page import PopupLocators
from ..layer1_page_object_model.login.login_page import LoginPage
from ..layer1_page_object_model.login.login_locators import LoginLocators
import time

class AuthenticationKeywords:
    class Login:
        
        def wait_until_ready() -> None:
            """_summary_
            """
            Wait.visibility(LoginLocators.USERNAME_FIELD)
            Wait.visibility(LoginLocators.PASSWORD_FIELD)
            Wait.visibility(LoginLocators.SUBMIT_BUTTON)
            Wait.visibility(PopupLocators.ACCELP_ALL)
            Wait.visibility(PopupLocators.CUSTOMIZE)
            
        def login(username: str, password: str, crawler_enabled = True) -> None:
            """
            Perform login with given credentials.
            """
            LoginPage.input_username(username)
            if crawler_enabled: time.sleep(2)
            LoginPage.input_password(password)
            if crawler_enabled: time.sleep(2)
            LoginPage.submit()
        
        def check_error_message(expectedMessage: str, timeout = 30) -> None:
            """_summary_
            Args:
                expectedMessage (str): _description_
            """
            Check.text(LoginLocators.ERROR_MESSAGE, expectedMessage, timeout)