import time
from playwright.sync_api import Page
from ...test_data.login_data import LoginData
from ....layer0_automation_tool.playwright.dvc import DoViewCheck
from ....layer0_automation_tool.playwright.check import Check
from ....layer0_automation_tool.playwright.wait import Wait
from ....layer0_automation_tool.playwright.dvc import By
from ....layer1_page_object_model.login.login_page import LoginPage
from ....layer1_page_object_model.meister_task.dashboard.dashboard_page import TaskDashboardPage
from ....layer1_page_object_model.meister_task.dashboard.dashboard_page import TaskNavItem
from ....layer1_page_object_model.meister_task.dashboard.add_task_dialog import AddTaskDialog
from ....layer1_page_object_model.meister_task.dashboard.task_details_dialog import TaskDetailsDialog
from ....layer1_page_object_model.meister_task.agenda.agenda_page import TaskAgendaPage
from ....layer2_keywords.popup import PopupKeywords
from ....layer2_keywords.authentication import AuthenticationKeywords
from ....layer2_keywords.snapshot import SnapshotKeywords

crawler_enabled = True

def test_add_task(page: Page, assert_snapshot):
    """
    Test Scenario:
        1. Login to Meister Task web app
        2. Click header plus button to 'Add Task'
        3. Input a name for the new task
        4. Click 'Create Task' button.
        5. Pin the task to Agenda FOCUS
        6. Close Task Details dialog
        7. Navigate to 'Agenda' tab
        8. Check that the task was successfully pinned
    """
    DoViewCheck.page = page
    page.set_viewport_size({ "width": 1920, "height": 1080 })   # 1080p
    LoginPage.open_browser(LoginData.MEISTER_TASK_URL)
    PopupKeywords.Cookies.close_accept_all()
    
    AuthenticationKeywords.Login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD, crawler_enabled)
    TaskDashboardPage.wait_page_ready()
    SnapshotKeywords.info_snapshot()
    time.sleep(100000)
    
    TaskDashboardPage.add_task()
    AddTaskDialog.input_task_title('Task1')
    AddTaskDialog.create_task()
    TaskDetailsDialog.pin_to_agenda()
    TaskDetailsDialog.pin_to_focus()
    TaskDetailsDialog.close_dialog()
    TaskDashboardPage.navigate(TaskNavItem.Agenda)
    time.sleep(5)
    SnapshotKeywords.assert_snapshot(assert_snapshot)
    Check.visibility('Task1', by=By.Text)
    
    time.sleep(2)
    # TODO - Implement proper checks here

def xtest_delete_task(page: Page):
    """
    Test Scenario:
        1. Login to Meister Task web app
        2. Navigate to 'Agenda' tab
        3. Click on the desired task
        4. Expand ... menu and click 'Delete'
        5. Click confirm
        6. Check that the task has been deleted
    """
    DoViewCheck.page = page
    page.set_viewport_size({ "width": 1920, "height": 1080 })   # 1080p
    LoginPage.open_browser(LoginData.MEISTER_TASK_URL)
    PopupKeywords.Cookies.close_accept_all()
    
    AuthenticationKeywords.Login.login(LoginData.VALID_USERNAME, LoginData.VALID_PASSWORD, crawler_enabled)
    TaskDashboardPage.navigate(TaskNavItem.Agenda)
    Check.visibility('Task1', by=By.Text)
    TaskDashboardPage.open_task('Task1')
    TaskDetailsDialog.open_task_menu()
    TaskDetailsDialog.delete_task()
    Check.visibility('Task1', by=By.Text)
    time.sleep(2)
    # TODO - Implement proper checks here