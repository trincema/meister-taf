# Given a user is on the login page
# When the user enters their username and password and clicks the login button
# Then the user should be directed to the home page.

*** Settings ***
Resource               ../layer2_keywords/login_keywords.resource

*** Variables ***
${VALID_USERNAME}      emanuel.trinc@yahoo.com
${VALID_PASSWORD}      Meister12345678

# Feature
# As a: MindMeister user on the login page
# I want to: Be able to login with username and password
# Such that: I should see MindMeister profile page
# -------------------------------------------------------
# In order: Login to the Meister apps
# As a: Meister user
# I want to: login with username and password

*** Test Cases ***
# Test Scenarios
User can Login to MindMeister
    Given I am on the MindMeister login page
    When I login with username "${VALID_USERNAME}" and password "${VALID_PASSWORD}"
    Then I should see the MindMeister profile page
    [Teardown]    Close All Browsers

User can login to MeisterTask
    Given I am on the MeisterTask login page
    When I login with username "${VALID_USERNAME}" and password "${VALID_PASSWORD}"
    Then I should see the MeisterTask Home page
    [Teardown]    Close All Browsers