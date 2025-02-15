from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


def test_creation_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
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

    # Upload document
    auction_page.upload_document()

    # Step 3: Save draft
    auction_page.save_draft()

    page.wait_for_timeout(3000)

    # Step 4: Compare the data with expected values
    assert my_auctions_page.get_card_title() == "Auction", \
        f"Expected title to be 'Auction', but got '{my_auctions_page.get_card_title()}'"
    assert my_auctions_page.get_card_procedure() == "Продаж на англійському аукціоні", \
        f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{my_auctions_page.get_card_procedure()}'"
    assert my_auctions_page.get_card_status() == "Чернетка", \
        f"Expected status to be 'Чернетка', but got '{my_auctions_page.get_card_status()}'"
