from playwright.sync_api import Page
from ...test_data.login_data import LoginData
from ....layer0_automation_tool.playwright.dvc import DoViewCheck
from ....layer1_page_object_model.page import Page
from ....layer1_page_object_model.login.login_page import LoginPage
from ....layer2_keywords.popup import PopupKeywords
from ....layer2_keywords.authentication import AuthenticationKeywords
from ....layer2_keywords.profile import Profile

import time

crawler_enabled = True

def test_invalid_credentials(page: Page, assert_snapshot):
    """
    Test case:
        1. Navigate to login page
        2. Enter invalid email and password
        3. Click 'Log in' button
        4. Check that the error message 'Sorry, these credentials are invalid.' appears on screen
    """
    DoViewCheck.page = page
    page.set_viewport_size({ "width": 1920, "height": 1080 })   # 1080p
    LoginPage.open_browser(LoginData.MIND_MEISTER_URL)
    AuthenticationKeywords.Login.wait_until_ready()
    #assert_snapshot(DoViewCheck.page.screenshot())
    PopupKeywords.Cookies.close_accept_all()
    
    LoginPage.input_username(LoginData.INVALID_USERNAME)
    if crawler_enabled: time.sleep(2)
    LoginPage.input_password(LoginData.INVALID_PASSWORD)
    if crawler_enabled: time.sleep(2)
    LoginPage.submit()
    AuthenticationKeywords.Login.check_error_message(LoginData.INVALID_CREDENTIALS_MESSAGE, 10)

def test_valid_credentials(page: Page, assert_snapshot):
    """
    Test case:
        1. Navigate to login page
        2. Enter valid credentials and click Submit
        3. Check that Profile page is successfuly reached
    """
    DoViewCheck.page = page
    page.set_viewport_size({ "width": 1920, "height": 1080 })   # 1080p
    LoginPage.open_browser(LoginData.MIND_MEISTER_URL)
    AuthenticationKeywords.Login.wait_until_ready()
    
    PopupKeywords.Cookies.close_accept_all()
    AuthenticationKeywords.Login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD, crawler_enabled)
    Profile.Me.wait_until_ready()
    #assert_snapshot(DoViewCheck.page.screenshot())