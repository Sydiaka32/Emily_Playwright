from playwright.sync_api import Page
from locators.application_locators import ApplicationLocators


class MyApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_application_status(self, expected_status: str) -> bool:
        """Verify the heading status text of the application."""
        heading = self.page.get_by_role("heading", name=expected_status)
        return heading.is_visible()

    def verify_draft_price(self, expected_price_text: str) -> bool:
        """Verify the presence of the draft price text."""
        return self.page.get_by_text(f"Розмір закритої цінової пропозиції, грн.:{expected_price_text}").is_visible()

    def verify_organization_name(self, expected_org_name: str) -> bool:
        """Verify the organization name in heading."""
        heading = self.page.get_by_role("heading", name=expected_org_name)
        return heading.is_visible()





