from ..layer1_page_object_model.popup.popup_page import PopupPage
from ..layer1_page_object_model.login.login_page import LoginPage
from ..layer1_page_object_model.profile.me_locators import MeLocators
from ..layer0_automation_tool.playwright.wait import Wait
import time

class Profile:
    class Me:
        def wait_until_ready() -> None:
            """_summary_
            """
            Wait.visibility(MeLocators.USER_NAME)
            Wait.visibility_by_index(MeLocators.ME_NAV_ITEM)
            Wait.visibility(MeLocators.MY_TEAM_NAV_ITEM)
            Wait.visibility(MeLocators.PLANS_NAV_ITEM)
            Wait.visibility(MeLocators.SAVE_CHANGES_BTN)

    class MyTeam:
        class MembersAndGroups:
            pass
        class Settings:
            pass

    class Plans:
        pass