from enum import Enum
from playwright.sync_api import Page

class By(Enum):
    Locator = 0,
    Text = 1
    
class DoViewCheck:
    page: Page = None