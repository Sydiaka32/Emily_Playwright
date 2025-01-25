from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_publish_draft():
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

        # Step 3: Publish draft
        my_auctions_page.publish_option()

        # Handle popup and updating time
        page.wait_for_timeout(3000)

        # Refresh the current page
        page.reload()

        # Handle popup and updating time
        page.wait_for_timeout(3000)
        navigation_page.close_notification_if_exists()

        # Step 14: Compare edited title
        assert my_auctions_page.get_card_published_status() == "Прийняття заяв на участь", f"Expected title to be 'Прийняття заяв на участь', but got '{my_auctions_page.get_card_published_status()}'"
        page.locator(my_auctions_locators.AUCTION_CARD_PUBLISHED).screenshot(path="screenshotpublished.png")

        # Close the browser after the test
        browser.close()


# Run the test
if __name__ == "__main__":
    test_publish_draft()
