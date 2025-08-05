from playwright.sync_api import Page
from locators.admin.application_details_locators import ApplicationDetailsLocatorsAdmin


class ApplicationDetailsPageAdmin:
    def __init__(self, page: Page):
        self.page = page

    def activate_option(self):
        """Clicks the 'Activate Application' button on the application details page."""

        # Click the 'Activate Application' button using its locator
        self.page.get_by_role("button", name=ApplicationDetailsLocatorsAdmin.ACTIVATE_BUTTON).click()
