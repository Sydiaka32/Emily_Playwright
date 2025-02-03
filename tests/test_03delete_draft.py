from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_delete_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    login_page = LoginPage(page)
    navigation_page = NavigationPage(page)
    my_auctions_page = MyAuctionsPage(page)

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


