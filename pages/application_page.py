from playwright.sync_api import Page
from locators.application_locators import ApplicationLocators


class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def select_profile(self):
        combobox = self.page.locator(ApplicationLocators.PROFILE_SELECT)
        combobox.wait_for()
        combobox.scroll_into_view_if_needed()
        combobox.click()
        self.page.locator(ApplicationLocators.APHRODITE_OPTION).click()

    def fill_price(self):
        self.page.locator(ApplicationLocators.PRICE_FIELD).fill("1500")

    def continue_option(self):
        self.page.locator(ApplicationLocators.CONTINUE_BUTTON).click()

    def confirmation_checks(self):
        self.page.locator(ApplicationLocators.PRIVASY_POLISY_CHECK).nth(0).click()
        self.page.locator(ApplicationLocators.REGULATIONS_CHECK).nth(1).click()

    def save_draft_application(self):
        self.page.locator(ApplicationLocators.SAVE_DRAFT_BUTTON).click()



