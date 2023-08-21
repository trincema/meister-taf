from enum import Enum
from ...page import Page
from .sidenav_locators import SidenavLocators

class Sidenav(Enum):
    MyApps = 0,
    Recents = 1,
    Favourites = 2,
    Public = 3,
    Trash = 4

class SidenavPage(Page):

    def navigate(sidenav: Sidenav):
        """
        Navigate to the given item on the left navbar.
        """
        Page.click(SidenavLocators.SIDENAV_ITEM, sidenav)