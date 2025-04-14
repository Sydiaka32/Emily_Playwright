from playwright.sync_api import Page
from locators.application_locators import ApplicationLocators


class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def select_profile(self):
        # Replace with the locator for the status field in the card
        self.page.get_by_label(ApplicationLocators.PROFILE_SELECT).get_by_text(ApplicationLocators.PROFILE_SELECT).click()
        self.page.get_by_role("option", name=ApplicationLocators.APHRODITE_OPTION).click()

    def fill_price(self):
        self.page.get_by_role("textbox", name=ApplicationLocators.PRICE_FIELD).fill("1500")

    def continue_option(self):
        self.page.get_by_role("button", name=ApplicationLocators.CONTINUE_BUTTON).click()

    def confirmation_checks(self):
        self.page.get_by_role("checkbox", name=ApplicationLocators.PERSONAL_DATA_CHECK).check()
        self.page.get_by_role("checkbox", name=ApplicationLocators.FAMILIRIZATION_CHECK).check()

    def save_draft_application(self):
        self.page.get_by_role("button", name=ApplicationLocators.SAVE_DRAFT_BUTTON).click()



