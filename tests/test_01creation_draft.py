from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from locators.my_auctions_locators import MyAuctionsLocators


def test_creation_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)  # Missing instantiation fixed here

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

    # Wait for 4 seconds
    page.wait_for_timeout(4000)

    # Step 9: Upload document
    auction_page.upload_document()

    # Step 10: Save draft
    auction_page.save_draft()

    # Wait for 20 seconds
    page.wait_for_timeout(20000)
    navigation_page.close_telegram_popup()

    page.wait_for_timeout(3000)  # Wait for 3 seconds before checking
    navigation_page.close_notification_if_exists()

    page.wait_for_timeout(3000)
    # Step 12: Compare the data with expected values
    assert my_auctions_page.get_card_title() == "Auction", f"Expected title to be 'Auction', but got '{my_auctions_page.get_card_title()}'"
    assert my_auctions_page.get_card_procedure() == "Продаж на англійському аукціоні", f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{my_auctions_page.get_card_procedure()}'"
    assert my_auctions_page.get_card_status() == "Чернетка", f"Expected status to be 'Чернетка', but got '{my_auctions_page.get_card_status()}'"

    my_auctions_locators = MyAuctionsLocators()
    page.locator(my_auctions_locators.AUCTION_CARD).screenshot(path="screenshot.png")
