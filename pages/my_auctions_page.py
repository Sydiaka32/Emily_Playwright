from playwright.sync_api import Page
from locators.account_locators import AccountLocators
from locators.my_auctions_locators import MyAuctionsLocators


class MyAuctionsPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_new_auction(self):
        self.page.locator(AccountLocators.NEW_AUCTION).click()

    def get_card_title(self):
        # Replace with the locator for the title field in the card
        return self.page.locator(MyAuctionsLocators.CARD_TITLE).inner_text()

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

    def get_latest_auction_id(self, response):
        """Fetch the latest auction ID via an API request."""
        url = "https://qa.ualand.utest.pro/api/v1.0/auctions/search/created/short?page=0&size=5&sort=id%2Cdesc"
        response = self.api_context.get(url)
        if response.ok:
            try:
                json_data = response.json()
                if json_data and isinstance(json_data, list):
                    auction_id = json_data[0].get("id")
                    if auction_id:
                        print(f"Extracted Auction ID: {auction_id}")
                        return auction_id
                    else:
                        print("No 'id' field found in the first auction item.")
                else:
                    print("Response JSON is empty or not a list.")
            except Exception as e:
                print(f"Error parsing response JSON: {e}")
        else:
            print(f"Failed to fetch auctions. HTTP Status: {response.status}")
        return None

    def verify_deletion(self, response):
        """Verify that the auction is no longer in the response"""
        # Match the exact URL or part of the URL
        if "auctions/search/created/short" in response.url and response.status == 200:
            json_data = response.json()
            # Check if the auction ID is no longer in the list
            auction_deleted = all(item["id"] != self.auction_id for item in json_data)
            assert auction_deleted, f"Auction with ID {self.auction_id} was not deleted."
            print("Auction successfully deleted")

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

    def publish_copy(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.PUBLISH_COPY).click()

    def copy_popup(self):
        self.page.get_by_placeholder(MyAuctionsLocators.ORDER_NUMBER_FIELD).fill("1")
        self.page.get_by_role("button", name=MyAuctionsLocators.SUBMIT_POPUP)

    def publish_copy_based(self):
        self.page.locator(MyAuctionsLocators.MORE_OPTIONS).first.click()
        self.page.get_by_role("button", name=MyAuctionsLocators.PUBLISH_COPY_BASED).click()

    def retrieve_auction_id(self):
        self.page.get_by_role("link", name=MyAuctionsLocators.DETAILS_BUTTON).first.click()
        # self.page.auction_url = page.url




