from playwright.sync_api import Page
from locators.account_locators import AccountLocators
from locators.all_auctions_locators import AllAuctionsLocators
from locators.my_auctions_locators import MyAuctionsLocators


class AllAuctionsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_new_auction(self):
        self.page.locator(AccountLocators.NEW_AUCTION).click()

    def search_auction(self):
        # Replace with the locator for the title field in the card
        self.page.locator(AllAuctionsLocators.SEARCH_FIELD).fill("BSE001-UA-20250324-35676")
        self.page.get_by_role("button", name="Пошук").first.click()

    def goto_details(self):
        self.page.get_by_role("link", name="Детальніше").click()
