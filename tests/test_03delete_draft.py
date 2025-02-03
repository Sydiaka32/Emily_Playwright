from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_delete_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)

    # Step 3: Delete draft
    my_auctions_page.delete_option()

    # Handle popup and updating time
    page.wait_for_timeout(3000)

    assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", \
        f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"



