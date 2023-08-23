from .dvc import DoViewCheck

class Wait(DoViewCheck):
    
    def visibility(locator: str, timeout=30) -> None:
        """Summary:
        Wait until the element is visible.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        element = Wait.page.locator(locator)
        element.wait_for(state='visible', timeout=timeout * 1000)
    
    def visibility_by_index(locator: str, index=0, timeout=30) -> None:
        """Summary:
        Wait until the element is visible.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        element = Wait.page.locator(locator + f' >> nth={index}')
        element.wait_for(state='visible', timeout=timeout * 1000)
    
    def invisibility(locator: str, timeout=30) -> None:
        """Summary:
        Wait until the element is visible.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        element = Wait.page.locator(locator)
        element.wait_for(state='hidden', timeout=timeout * 1000)
    
    def removal(locator: str, timeout=30) -> None:
        """Summary:
        Wait until the element is visible.
        Args:
            locator (str): _description_
            timeout (int, optional): _description_. Defaults to 30.
        """
        element = Wait.page.locator(locator)
        element.wait_for(state='detached', timeout=timeout * 1000)