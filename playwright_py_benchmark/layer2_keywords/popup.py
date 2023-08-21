from ..layer1_page_object_model.popup.popup_page import PopupPage

class Popup:
    class Cookies:
        def close_accept_all():
            """
            Close 'Accept All' dialog.
            """
            PopupPage.Cookies.accept_all()