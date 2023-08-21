from playwright.sync_api import Page
from ...test_data.login_data import LoginData
from ....layer0_automation_tool.do_view_check.playwright.dvc import DoViewCheck
from ....layer0_automation_tool.do_view_check.playwright.check import Check
from ....layer1_page_object_model.page import Page
from ....layer1_page_object_model.login.login_page import LoginPage
from ....layer1_page_object_model.login.login_locators import LoginLocators
from ....layer1_page_object_model.profile.me_locators import MeLocators
from ....layer2_keywords.popup import Popup
from ....layer2_keywords.authentication import AuthenticationKeywords

import time

crawler_enabled = True

def test_invalid_credentials(page: Page):
    """
    Test case:
        1. Navigate to login page
        2. Enter invalid email and password
        3. Click 'Log in' button
        4. Check that the error message 'Sorry, these credentials are invalid.' appears on screen
    """
    DoViewCheck.page = page
    LoginPage.open_browser(LoginData.MIND_MEISTER_URL)
    LoginPage.input_username(LoginData.INVALID_USERNAME)
    if crawler_enabled: time.sleep(2)
    LoginPage.input_password(LoginData.INVALID_PASSWORD)
    if crawler_enabled: time.sleep(2)
    LoginPage.submit()
    AuthenticationKeywords.Login.check_error_message(LoginData.INVALID_CREDENTIALS_MESSAGE, 10)

def test_valid_credentials(page: Page):
    """
    Test case:
        1. Navigate to login page
        2. Enter valid credentials and click Submit
        3. Check that Profile page is successfuly reached
    """
    DoViewCheck.page = page
    LoginPage.open_browser(LoginData.MIND_MEISTER_URL)
    
    Popup.Cookies.close_accept_all()
    AuthenticationKeywords.Login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD, crawler_enabled)
    Check.visibility(MeLocators.USER_NAME)