from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_creation_draft():
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

        # Step 3: Navigate to "New Auction" page
        my_auctions_page.navigate_to_new_auction()

        # Step 4: Select organiser
        auction_page.select_organiser()

        # Step 5: Select procedure
        auction_page.select_procedure()

        # Step 6.1: Close telegram popup
        navigation_page.close_telegram_popup()

        # Step 6: Fill in Basic block
        auction_page.fill_basic_info_block()

        # Step 7: Fill in Details
        auction_page.fill_detail_lot_description_block()

        # Step 8: Fill in Lot info
        auction_page.select_classifier()
        auction_page.fill_lot_info_block()
        auction_page.point_map()

        # Wait for  seconds
        page.wait_for_timeout(4000)

        # Step 9: Upload document
        auction_page.upload_document()

        # Step 10: Save draft
        auction_page.save_draft()

        # Wait for  seconds
        page.wait_for_timeout(20000)
        navigation_page.close_telegram_popup()

        page.wait_for_timeout(3000)  # Wait for 1 second before checking
        navigation_page.close_notification_if_exists()

        page.wait_for_timeout(3000)
        # Step 12: Compare the data with expected values
        assert my_auctions_page.get_card_title() == "Auction", f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"
        assert my_auctions_page.get_card_procedure() == "Продаж на англійському аукціоні", (f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{my_auctions_page.get_card_procedure()}'")
        assert my_auctions_page.get_card_status() == "Чернетка", f"Expected status to be 'Чернетка', but got '{my_auctions_page.get_card_status()}'"

        page.locator(my_auctions_locators.AUCTION_CARD).screenshot(path="screenshot.png")

        # Close the browser after the test
        browser.close()


# Run the test
if __name__ == "__main__":
    test_creation_draft()
