class LoginLocators:
    USERNAME_FIELD = 'css=input[id="login_email_login"]'
    PASSWORD_FIELD = 'css=input[id="login_email_password"]'
    SUBMIT_BUTTON = 'css=input[id="btn_signin"]'
    ERROR_MESSAGE = 'css=#site-flash-messages > div.ui-message.error.align-items-start > div:nth-child(2)'