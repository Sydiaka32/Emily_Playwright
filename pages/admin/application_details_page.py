from playwright.sync_api import Page

from locators.admin.application_details_locators import ApplicationDetailsLocatorsAdmin



class ApplicationDetailsPageAdmin:
    def __init__(self, page: Page):
        self.page = page

    def activate_option(self):
        """Fills the search field with the given bid_id and submits the search."""

        # Locate the search input field using the locator
        self.page.get_by_role("button", name=ApplicationDetailsLocatorsAdmin.ACTIVATE_BUTTON).click()

