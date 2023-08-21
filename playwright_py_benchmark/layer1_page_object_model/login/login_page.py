from playwright.sync_api import Page
from .login_locators import LoginLocators
from ..page import Page

class LoginPage(Page):
    
    def input_username(username: str):
        """
        """
        LoginPage.page.locator(LoginLocators.USERNAME_FIELD).fill(username)
    
    def input_password(password: str):
        """
        """
        LoginPage.page.locator(LoginLocators.PASSWORD_FIELD).fill(password)
    
    def submit():
        """
        """
        LoginPage.page.locator(LoginLocators.SUBMIT_BUTTON).click()
    