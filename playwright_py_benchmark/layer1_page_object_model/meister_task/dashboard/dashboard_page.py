from enum import Enum
from ...page import Page
from ....layer0_automation_tool.playwright.dvc import By

class DashboardLocators:
    HEADER_ADD_TASK = 'div[data-test-id="header-button-add-task-right"]'
    DASHBOARD = 'a[href="/app/dashboard"]'
    AGENDA = 'a[href="/app/agenda"]'

class TaskNavItem(Enum):
    Dashboard = 0,
    Agenda = 1,
    Reports = 2,
    Projects = 3

class TaskDashboardPage(Page):

    def add_task() -> None:
        """_summary_
        """
        Page.click(DashboardLocators.HEADER_ADD_TASK)
    
    def navigate(nav_item: TaskNavItem) -> None:
        """_summary_

        Args:
            nav_item (TaskNavItem): _description_
        """
        match nav_item:
            case TaskNavItem.Dashboard:
                Page.click(DashboardLocators.DASHBOARD)
            case TaskNavItem.Agenda:
                Page.click(DashboardLocators.AGENDA)
    
    def open_task(task_name: str) -> None:
        """_summary_

        Args:
            task_name (str): _description_
        """
        Page.click(task_name, By.Text)