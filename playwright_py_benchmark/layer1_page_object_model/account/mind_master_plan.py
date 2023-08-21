from enum import Enum
from ..page import Page
from .mind_meister_plan_locators import MindMeisterPlanLocators

class MindMeisterPlan(Enum):
    Basic = 0,
    Personal = 1,
    Pro = 2,
    Business = 3

class MindMeisterPlanPage(Page):

    def choose_plan(plan: MindMeisterPlan):
        """
        Choose a plan for Mind Meister
        """
        Page.click(MindMeisterPlanLocators.PLAN_CARD_BUTTON, plan)