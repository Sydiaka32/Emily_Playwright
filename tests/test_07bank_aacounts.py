from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


def test_bank_accounts(navigate_to_my_auctions, allure_step):
    page = navigate_to_my_auctions

    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    # Step 1: Navigate to "New Auction" page
    my_auctions_page.navigate_to_new_auction()

    # Step 2: Fill in all required fields

    # Select organiser
    auction_page.select_organiser()

    # Select procedure
    auction_page.select_procedure()

    # Extra step: Wait and Close telegram popup
    navigation_page.close_telegram_popup()

    # Fill in Basic block
    auction_page.fill_basic_info_block()

    # Fill in Details block
    auction_page.fill_detail_lot_description_block()

    # Fill in Lot info block
    auction_page.select_classifier()
    auction_page.fill_lot_info_block()
    auction_page.point_map()

    # Wait for 4 seconds
    page.wait_for_timeout(4000)

    auction_page.add_bank_account()

    auction_page.add_registration_fee()

    auction_page.add_bank_account()

    auction_page.add_other()

    auction_page.add_bank_account()

    auction_page.add_payment()

    auction_page.add_bank_account()

    auction_page.add_guarantee()

    # Upload document
    auction_page.upload_document()

    # Step 3: Save draft
    auction_page.save_draft()

    page.wait_for_timeout(3000)


