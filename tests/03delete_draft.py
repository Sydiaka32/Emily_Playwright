from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_delete_draft():
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

        # Step: get auction_id
        page.on("response", my_auctions_page.handle_response)

        # Step 3: Delete draft
        my_auctions_page.delete_option()

        # Handle popup and updating time
        page.wait_for_timeout(3000)

        # Step: ensure that auction deleted
        # Step 3: Verify that the auction is no longer in the list
        page.on("response", my_auctions_page.verify_deletion)

        # Wait for a response that contains the updated list after deletion
        page.wait_for_timeout(3000)

        # Close the browser after the test
        browser.close()


# Run the test
if __name__ == "__main__":
    test_delete_draft()
