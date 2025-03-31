from playwright.sync_api import Page
from locators.account_locators import AccountLocators
from locators.all_auctions_locators import AllAuctionsLocators
from pages.auction_details_page import AuctionDetailsPage  # Create this if needed


class AllAuctionsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_new_auction(self):
        self.page.locator(AccountLocators.NEW_AUCTION).click()

    def search_auction(self, prozorro_id: str):
        # self.page.locator(AllAuctionsLocators.SEARCH_FIELD).fill(prozorro_id)
        self.page.get_by_role("textbox", name=AllAuctionsLocators.SEARCH_FIELD).fill(prozorro_id)
        self.page.get_by_role("button", name=AllAuctionsLocators.SEARCH_BUTTON).first.click()

    def goto_details(self) -> AuctionDetailsPage:
        """Open auction details in new tab and return the new page object"""
        with self.page.expect_popup() as popup_info:
            # Use more specific locator matching your structure
            self.page.get_by_role("main").get_by_role(
                "link",
                name=AllAuctionsLocators.DETAILS_BUTTON
            ).click()

        new_page = popup_info.value
        new_page.wait_for_load_state()  # Ensure new page loads completely
        return AuctionDetailsPage(new_page)  # Return page object for new tab
