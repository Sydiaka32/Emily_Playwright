from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_edit_draft():
    with sync_playwright() as playwright:
        # Launch the browser and create a new page
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Initialize the LoginPage, NavigationPage, and MyAuctionsPage
        login_page = LoginPage(page)
        navigation_page = NavigationPage(page)
        my_auctions_page = MyAuctionsPage(page)
        auction_page = AuctionPage(page)
        my_auctions_locators = MyAuctionsLocators()

        # Step 1: Log in to the application
        login_page.login()

        # Step 2: Navigate to "My Auctions"
        navigation_page.navigate_to_my_auctions()

        # Step 6.1: Close telegram popup
        navigation_page.close_telegram_popup()

        page.wait_for_timeout(3000)

        # Step 13: Go to edit mode of draft and edit
        my_auctions_page.edit_mode()
        auction_page.edit_title()
        auction_page.save_changes()

        # Handle popup and updating time
        page.wait_for_timeout(3000)

        # Step 14: Compare edited title
        assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"
        page.locator(my_auctions_locators.AUCTION_CARD).screenshot(path="screenshotedited.png")

        # Close the browser after the test
        browser.close()


# Run the test
if __name__ == "__main__":
    test_edit_draft()
