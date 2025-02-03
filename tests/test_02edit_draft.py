from playwright.sync_api import  sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_edit_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    navigation_page = NavigationPage(page)
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    my_auctions_locators = MyAuctionsLocators()

    # Step 2: Navigate to "My Auctions"
    navigation_page.navigate_to_my_auctions()

    # Step 6.1: Close telegram popup
    navigation_page.close_telegram_popup()

    page.wait_for_timeout(2000)

    # Step 13: Go to edit mode of draft and edit
    my_auctions_page.edit_mode()
    auction_page.edit_title()
    page.wait_for_timeout(1000)
    auction_page.save_changes()

    # Handle popup and updating time
    page.wait_for_timeout(2000)

    # Step 14: Compare edited title
    assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", \
        f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"
