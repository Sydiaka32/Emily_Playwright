from playwright.sync_api import Page
from locators.application_locators import ApplicationLocators
from locators.my_applications_locators import MyApplicationLocators


class MyApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_application_status(self, expected_status: str) -> bool:
        """Verify the application status using the correct selector"""
        status_locator = self.page.locator(
            "xpath=//h6[contains(@class, 'MuiTypography-h6') and text()='Неопублікована заява']")
        return status_locator.is_visible()

    def verify_draft_price(self, expected_price_text: str) -> bool:
        """Verify the draft price using the actual price element"""
        price_element = self.page.locator("p.css-s0fat1")
        return price_element.text_content() == expected_price_text

    def verify_organization_name(self, expected_org_name: str) -> bool:
        """Verify organization name in the participant section"""
        org_locator = self.page.locator(
            "xpath=//h6[contains(@class, 'MuiTypography-subtitle1') and contains(text(), 'UA-EDR')]")
        return org_locator.text_content() == expected_org_name

    def open_application_details(self):
        print("Found:", self.page.locator(MyApplicationLocators.APPLICATION_DETAILS).count())
        button = self.page.locator(MyApplicationLocators.APPLICATION_DETAILS).first
        button.click()

    def get_app_status(self):
        # Replace with the locator for the title field in the card
        return self.page.locator(MyApplicationLocators.STATUS_INFO).inner_text()

    def get_app_profile(self):
        return self.page.locator(MyApplicationLocators.PROFILE_INFO).inner_text()

    def get_app_price(self):
        # Replace with the locator for the procedure field in the card
        return self.page.locator(MyApplicationLocators.PRICE_INFO).inner_text()

    def get_application_card(self, bid_id: str):
        """Locates the application card by bid ID using proper CSS escaping"""
        return self.page.locator(
            f'div.MuiPaper-root:has(span:has-text("{bid_id}"))'
        ).filter(has_text="ID:")

    def get_publish_button(self, bid_id: str):
        """Locates the publish button within a specific application card"""
        card = self.get_application_card(bid_id)
        return card.get_by_role("button", name="Опублікувати", exact=True)

    def publish_application(self, bid_id: str):
        """Full flow to publish a specific application"""

        publish_btn = self.get_publish_button(bid_id)
        publish_btn.click()

    def get_application_status(self, bid_id: str):
        """Gets the status element using stable selectors"""
        card = self.get_application_card(bid_id)
        # Use the SVG icon as an anchor point
        return card.locator('svg[data-testid="FiberManualRecordIcon"] + h6').first  # or use :nth-match()




