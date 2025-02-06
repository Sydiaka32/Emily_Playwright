from playwright.sync_api import  sync_playwright

from config.settings import ConfigParser
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_delete_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    config_parser = ConfigParser()

    # Step 2: Click on first auction (opens in new tab)
    with page.expect_popup() as new_tab:
        my_auctions_page.retrieve_auction_id()
    auction_details_page = new_tab.value  # Get the new tab reference

    # Step 3: Extract auction ID from the new tab URL
    auction_url = auction_details_page.url
    auction_id = auction_url.split("/")[-1]  # Extract the ID

    # Step 4: Close auction details tab & return to "My Auctions"
    auction_details_page.close()

    # Step 3: Delete draft
    my_auctions_page.delete_option()

    # Handle popup and updating time
    page.wait_for_timeout(3000)

    # Step 5: Manually try to visit the auction details page
    page.goto(f"{config_parser.base_url}/auctions/{auction_id}")  # Replace with actual URL format
    page.wait_for_timeout(3000)

    # Step 6: Verify redirection
    assert (f"{config_parser.all_auctions_url}"
            in page.url), f"Auction {auction_id} was not deleted, expected redirection!"



