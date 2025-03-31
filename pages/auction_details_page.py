import re
from playwright.sync_api import Page, expect
from locators.auction_details_locators import AuctionDetailsLocators


class AuctionDetailsPage:
    def __init__(self, page: Page):
        self.page = page


    def get_discount_value(self):
        # Locate the discount label to ensure it's loaded
        discount_label = self.page.get_by_text("Розмір знижки від попереднього аукціону, %")

        # Scroll to the label to ensure visibility
        discount_label.scroll_into_view_if_needed()

        # Wait for label to be visible (with adjusted timeout)
        discount_label.wait_for(state="visible", timeout=15000)  # 15 seconds

        # Now target the value element with parent-child locator
        discount_value = self.page.locator(
            'css=div.MuiGrid-container:has(h6:has-text("Розмір знижки"))'
            ' >> div.MuiGrid-grid-md-true >> h6'
        )

        # Scroll again to value (if needed)
        discount_value.scroll_into_view_if_needed()

        # Get text content safely
        return discount_value.text_content().strip()

    def expand_details(self):
        self.page.get_by_role('button', name=AuctionDetailsLocators.DETAIL_INFO_ACORDEON).click()

    def get_previous_id_value(self):
        previous_id_locator = self.page.locator(AuctionDetailsLocators.PREVIOUS_AUCTION_ID)
        displayed_value = previous_id_locator.inner_text()
        return displayed_value

    def apply_for_auction(self):
        # Replace with the locator for the procedure field in the card
        self.page.get_by_role("button", name="Взяти участь").click()

    def click_participate_button(self):
        self.page.get_by_role("button", name="Взяти участь").click()

    def select_profile(self, profile_id: str):
        self.page.get_by_role("combobox", name="Не визначено").click()
        self.page.get_by_role("option", name=profile_id).click()

    def set_bid_price(self, price: str):
        price_field = self.page.get_by_role("textbox", name="Не визначено")
        price_field.click()
        price_field.fill(price)

    def click_continue(self):
        self.page.get_by_role("button", name="Продовжити").click()

    def accept_privacy_policy(self):
        self.page.get_by_role("checkbox", name="Даю згоду на обробку персональних даних...").check()

    def accept_regulations(self):
        self.page.get_by_role("checkbox", name="Ознайомлений з Регламентом...").check()

    def submit_application(self):
        self.page.get_by_role("button", name="Опублікувати").click()

    def verify_draft_price(self, expected_price: str):
        expect(self.page.get_by_text(expected_price)).to_be_visible()

    def verify_application_status(self, expected_status: str):
        expect(self.page.get_by_text(expected_status)).to_be_visible()

    def verify_organization_name(self, expected_name: str):
        expect(self.page.get_by_role("heading", name=expected_name).first).to_be_visible()