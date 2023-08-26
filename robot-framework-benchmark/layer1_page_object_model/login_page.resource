*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${USERNAME_FIELD}    css=input[id="login_email_login"]
${PASSWORD_FIELD}    css=input[id="login_email_password"]
${SUBMIT_BUTTON}     css=input[id="btn_signin"]
${ERROR_MESSAGE}     css=#site-flash-messages > div.ui-message.error.align-items-start > div:nth-child(2)

*** Keywords ***
Set username
    [Arguments]        ${username}
    Wait Until Element Is Visible    ${USERNAME_FIELD}     timeout=30s
    Input Text                       ${USERNAME_FIELD}     ${username}

Set password
    [Arguments]        ${password}
    Wait Until Element Is Visible    ${PASSWORD_FIELD}    timeout=30s
    Input Password                   ${PASSWORD_FIELD}    ${password}

Submit
    Wait Until Element Is Enabled    ${SUBMIT_BUTTON}     timeout=30s
    Click Element                    ${SUBMIT_BUTTON}
