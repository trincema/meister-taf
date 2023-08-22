from ...page import Page
from ....layer0_automation_tool.playwright.do import ClickMissfire

class AddTaskDialogLocators:
    TASK_TITLE_INPUT = 'input[data-test-id="dialog-task-adder-name-input"]'
    CREATE_TASK_BUTTON = 'div[data-test-id="task-adder-dialog-submit"]'

class AddTaskDialog(Page):
    
    def input_task_title(task_title: str) -> None:
        """Summary: 
        Input the given 'task_title' parameter into 'Task title' input field.
        Args:
            task_title (str): The name of the new task
        """
        Page.input_value(AddTaskDialogLocators.TASK_TITLE_INPUT, task_title)
    
    def create_task() -> None:
        """
        Click 'Create Task' button.
        """
        Page.click(AddTaskDialogLocators.CREATE_TASK_BUTTON, ClickMissfire.WAIT_FOR_INVISIBLE)