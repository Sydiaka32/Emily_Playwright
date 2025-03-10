from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


def test_creation_draft(navigate_to_my_auctions, allure_step):
    page = navigate_to_my_auctions

    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    # Using the fixture to reduce redundancy
    allure_step("Navigate to 'New Auction' page", my_auctions_page.navigate_to_new_auction, take_screenshot=False)

    allure_step("Select organiser", auction_page.select_organiser, take_screenshot=False)
    allure_step("Select procedure", auction_page.select_procedure, take_screenshot=False)
    allure_step("Close Telegram popup", navigation_page.close_telegram_popup, take_screenshot=False)
    allure_step("Fill in Basic info block", auction_page.fill_basic_info_block, take_screenshot=True)
    allure_step("Fill in Details block", auction_page.fill_detail_lot_description_block, take_screenshot=True)
    allure_step("Select classifier", auction_page.select_classifier, take_screenshot=True)
    allure_step("Fill in Lot info block", auction_page.fill_lot_info_block, take_screenshot=False)
    allure_step("Point map", auction_page.point_map, take_screenshot=True)

    # Wait for 4 seconds (try to avoid hardcoded waits if possible)
    page.wait_for_timeout(4000)

    allure_step("Upload document", auction_page.upload_document, take_screenshot=False)
    allure_step("Save draft", auction_page.save_draft, take_screenshot=False)

    page.wait_for_timeout(4000)

    # Additional assertions
    card_title = allure_step("Get card title", my_auctions_page.get_card_title, take_screenshot=False)
    card_procedure = allure_step("Get card procedure", my_auctions_page.get_card_procedure, take_screenshot=False)
    card_status = allure_step("Get card status", my_auctions_page.get_card_status, take_screenshot=False)

    assert card_title == "Auction", f"Expected title to be 'Auction', but got '{card_title}'"
    assert card_procedure == 'Продаж на "англійському аукціоні"', \
        f"Expected procedure to be 'Продаж на англійському аукціоні', but got '{card_procedure}'"
    assert card_status == "Чернетка", f"Expected status to be 'Чернетка', but got '{card_status}'"
