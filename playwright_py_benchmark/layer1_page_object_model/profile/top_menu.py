from ..page import Page
from .top_menu_locators import TopMenuLocators

class TopMenu(Page):
    def back_to_mind_meister():
        """
        Click 'Back to MindMeister' to go to 
        """
        TopMenu.click(TopMenuLocators.BACK_TO_MIND_MEISTER)