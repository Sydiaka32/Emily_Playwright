from playwright.sync_api import Page
from locators.admin.applications_locators import ApplicationLocatorsAdmin


class ApplicationPageAdmin:
    def __init__(self, page: Page):
        self.page = page

    def search_bid(self, bid_id):
        """Fills the search field with the given bid_id and submits the search."""

        # Locate the search input field using the locator
        search_input = self.page.locator(ApplicationLocatorsAdmin.SEARCH_FIELD)
        search_input.fill(str(bid_id))

        # Trigger search — assuming pressing Enter triggers it
        search_input.press("Enter")

    def goto_bid_details(self):
        """Fills the search field with the given bid_id and submits the search."""

        # Locate the search input field using the locator
        self.page.get_by_role("link", name=ApplicationLocatorsAdmin.APPLICATION_DETAILS_BUTTON).click()

    def get_confirmed_status(self, bid_id: str) -> str:
        """Get first status ('Підтверджена заява') for specific application"""
        # Anchor to bid ID first
        status = self.page.get_by_role("heading", name=ApplicationLocatorsAdmin.BID_STATUS).nth(1)
        return status.inner_text()

    def get_activated_status(self, bid_id: str) -> str:
        """Get second status ('Активовано') for specific application"""
        # Use verification status label as anchor
        status = self.page.locator("h6").filter(has_text=ApplicationLocatorsAdmin.VERIFIED_STATUS).get_by_role("heading")
        return status.inner_text()