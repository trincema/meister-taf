*** Settings ***
Library                SeleniumLibrary
Resource               ../layer1_page_object_model/login_page.resource

*** Variables ***
${MIND_MEISTER_URL}    https://accounts.meister.co/login
${MEISTER_TASK_URL}    https://www.meistertask.com/app/dashboard
${PROFILE_USER_NAME}   css=h2[id="current-user-name"]

*** Keywords ***
I am on the MindMeister login page
    Log To Console                     I am on the MindMeister login page
    Open browser                       ${MIND_MEISTER_URL}         headlesschrome
    Wait Until Element Is Visible      ${SUBMIT_BUTTON}            timeout=30s
    Set Window Size                    1920    1080

I am on the MeisterTask login page
    Log To Console                     I am on the MeisterTask login page
    Open Browser                       ${MEISTER_TASK_URL}          headlesschrome
    Wait Until Element Is Visible      ${SUBMIT_BUTTON}             timeout=30s
    Set Window Size                    1920    1080

I login to MindMeister with username "${username}" and password "${password}"
    Log To Console    I login to MindMeister with username "${username}" and password "${password}"
    Set username      ${username}
    Sleep             2s
    Set password      ${password}
    Sleep             2s
    Submit

I should see the MindMeister profile page
    Log To Console                    I should see the MindMeister profile page
    Wait Until Element Is Visible     ${PROFILE_USER_NAME}           timeout=30s