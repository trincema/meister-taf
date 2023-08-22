from ...page import Page

class TaskDetailsLocators:
    DIALOG = 'div[data-test-id="dialog-TaskDialog"]'
    PIN_TO_AGENDA_BTN = 'div[data-test-id="dialog-TaskDialog"] div[data-test-id="icon-text-button-right"]'
    PIN_TO_FOCUS_BTN = 'div[data-test-group="list-item"] > div[class="kr-view"]'
    CLOSE_DIALOG_BTN = 'div[data-test-id="button-close-right"]'

class TaskDetailsDialog(Page):
    
    def pin_to_agenda() -> None:
        """Summary:
        Click 'Pin to Agenda' button to pin the current task to the Agenda.
        """
        Page.click_by_index(TaskDetailsLocators.PIN_TO_AGENDA_BTN)
    
    def pin_to_focus():
        """_summary_
        """
        Page.click(TaskDetailsLocators.PIN_TO_FOCUS_BTN)
    
    def close_dialog():
        """_summary_
        """
        Page.click(TaskDetailsLocators.CLOSE_DIALOG_BTN)