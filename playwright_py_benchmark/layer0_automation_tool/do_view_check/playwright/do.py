from .dvc import DoViewCheck

class Do(DoViewCheck):
    def navigate(url: str):
        """
        """
        Do.page.goto(url)
    
    def click(locator: str, index = 0):
        """
        """
        Do.page.locator(locator + f' >> nth={index}').click()