from playwright.sync_api import Page
from locators.user.account_locators import AccountLocators
from locators.user.my_auctions_locators import MyAuctionsLocators


class MyAuctionsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_new_auction(self):
        self.page.locator(AccountLocators.NEW_AUCTION).click()

    def get_card_title(self):
        # Replace with the locator for the title field in the card
        return self.page.locator(MyAuctionsLocators.CARD_TITLE).inner_text()

    def get_card_title_locator(self):
        return self.page.locator(MyAuctionsLocators.CARD_TITLE)

    def get_card_procedure(self):
        # Replace with the locator for the procedure field in the card
        return self.page.locator(MyAuctionsLocators.CARD_PROCEDURE).inner_text()

    def get_card_status(self):
        # Replace with the locator for the status field in the card
        return self.page.locator(MyAuctionsLocators.CARD_STATUS).inner_text()

    def edit_mode(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.EDIT_OPTION).click()

    def delete_option(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.DELETE_OPTION).click()

    def publish_option(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.PUBLISH_OPTION).click()

    def get_card_published_title(self):
        # Replace with the locator for the title field in the card
        return self.page.get_by_role("link", name=MyAuctionsLocators.PUBLISHED_CARD_TITLE).first.inner_text()

    def get_card_published_status(self):
        # Replace with the locator for the procedure field in the card
        return self.page.get_by_text(MyAuctionsLocators.PUBLISHED_CARD_STATUS).first.inner_text()

    def get_card_published_procedure(self):
        # Replace with the locator for the status field in the card
        return self.page.get_by_role("heading", name=MyAuctionsLocators.PUBLISHED_CARD_PROCEDURE).first.inner_text()

    def copy_option(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.COPY).nth(0).click()
        self.page.get_by_placeholder(MyAuctionsLocators.ORDER_NUMBER_FIELD).fill("1")
        self.page.locator(MyAuctionsLocators.TIME_FIELD).fill("2359")

    def copy_based_option(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.PUBLISH_COPY_BASED).click()
        self.page.get_by_placeholder(MyAuctionsLocators.ORDER_NUMBER_FIELD).fill("2")
        self.page.locator(MyAuctionsLocators.TIME_FIELD).fill("2359")

    def copy_popup_yes(self):
        self.page.get_by_role("button", name=MyAuctionsLocators.SUBMIT_POPUP).click()

    def retrieve_auction_id(self):
        self.page.get_by_role("link", name=MyAuctionsLocators.DETAILS_BUTTON).first.click()
        # self.page.auction_url = page.url

    def switch_to_published(self):
        self.page.get_by_role("tab", name=MyAuctionsLocators.PUBLISHED_TAB).click()

    def goto_auction_details(self):
        self.page.get_by_role("link", name=MyAuctionsLocators.DETAILS_BUTTON).first.click()

    def switch_to_drafts(self):
        self.page.locator(MyAuctionsLocators.DRAFTS_TAB).click()

    def search_auction(self, auction_id):
        # self.page.locator(AllAuctionsLocators.SEARCH_FIELD).fill(prozorro_id)
        self.page.locator(MyAuctionsLocators.SEARCH_FIELD).fill(str(auction_id))
        self.page.get_by_role("button", name=MyAuctionsLocators.SEARCH_BUTTON).first.click()





