from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text)
