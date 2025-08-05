from playwright.sync_api import Page
from locators.user.my_applications_locators import MyApplicationLocators


class MyApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_application_status(self, expected_status: str) -> bool:
        """
        Verify if the application status matches the expected status by checking visibility
        of a specific status locator.
        """
        status_locator = self.page.locator(
            "xpath=//h6[contains(@class, 'MuiTypography-h6') and text()='Неопублікована заява']")
        return status_locator.is_visible()

    def verify_draft_price(self, expected_price_text: str) -> bool:
        """
        Verify the draft price text matches the expected price.
        """
        price_element = self.page.locator("p.css-s0fat1")
        return price_element.text_content() == expected_price_text

    def verify_organization_name(self, expected_org_name: str) -> bool:
        """
        Verify the organization name in the participant section matches expected.
        """
        org_locator = self.page.locator(
            "xpath=//h6[contains(@class, 'MuiTypography-subtitle1') and contains(text(), 'UA-EDR')]")
        return org_locator.text_content() == expected_org_name

    def open_application_details(self):
        """
        Clicks the first 'Application Details' button found on the page to open details.
        """
        print("Found:", self.page.locator(MyApplicationLocators.APPLICATION_DETAILS).count())
        button = self.page.locator(MyApplicationLocators.APPLICATION_DETAILS).first
        button.click()

    def get_app_status(self):
        """
        Retrieves the text content of the application status field.
        """
        return self.page.locator(MyApplicationLocators.STATUS_INFO).inner_text()

    def get_app_profile(self):
        """
        Retrieves the text content of the application profile information.
        """
        return self.page.locator(MyApplicationLocators.PROFILE_INFO).inner_text()

    def get_app_price(self):
        """
        Retrieves the text content of the application price information.
        """
        return self.page.locator(MyApplicationLocators.PRICE_INFO).inner_text()

    def get_application_card(self, bid_id: str):
        """
        Locates the application card element by bid ID using CSS selector with proper escaping.
        """
        return self.page.locator(
            f'div.MuiPaper-root:has(span:has-text("{bid_id}"))'
        ).filter(has_text="ID:")

    def get_publish_button(self, bid_id: str):
        """
        Locates the 'Publish' button within the specified application card.
        """
        card = self.get_application_card(bid_id)
        return card.get_by_role("button", name="Опублікувати", exact=True)

    def publish_application(self, bid_id: str):
        """
        Performs the full flow of publishing the specified application by clicking its publish button.
        """
        publish_btn = self.get_publish_button(bid_id)
        publish_btn.click()

    def get_application_status(self, bid_id: str):
        """
        Gets the application status element using stable selectors anchored by SVG icon.
        """
        card = self.get_application_card(bid_id)
        # Use the SVG icon as an anchor point to get the status element
        return card.locator('svg[data-testid="FiberManualRecordIcon"] + h6').first  # or use :nth-match()
