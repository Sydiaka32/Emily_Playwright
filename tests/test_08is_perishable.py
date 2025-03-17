from pages.navigation_page import NavigationPage
from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage


def test_is_perishable(navigate_to_my_auctions, get_auction_id, allure_step, capture_api_values):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    # Auction creation steps
    allure_step("Navigate to 'New Auction' page", my_auctions_page.navigate_to_new_auction, take_screenshot=False)
    allure_step("Select organiser", auction_page.select_organiser, take_screenshot=False)
    allure_step("Select procedure", auction_page.select_procedure, take_screenshot=False)
    allure_step("Close Telegram popup", navigation_page.close_telegram_popup, take_screenshot=False)
    allure_step("Fill in Basic info block", auction_page.fill_basic_info_block, take_screenshot=True)
    allure_step("Fill in Details block", auction_page.fill_detail_lot_description_block, take_screenshot=True)
    allure_step("Select classifier", lambda: auction_page.select_perishable_classifier(), take_screenshot=True)
    allure_step("Fill in Lot info block", auction_page.fill_lot_info_block, take_screenshot=False)
    allure_step("Point map", auction_page.point_map, take_screenshot=True)
    # Wait for 4 seconds (try to avoid hardcoded waits if possible)
    page.wait_for_timeout(4000)

    allure_step("Upload document", auction_page.upload_document, take_screenshot=False)
    allure_step("Save draft", auction_page.save_draft, take_screenshot=False)

    page.wait_for_timeout(3000)

    allure_step("Publish option", lambda: my_auctions_page.publish_option(), take_screenshot=True)

    page.wait_for_timeout(3000)

    allure_step("Go to auction details", lambda: my_auctions_page.goto_auction_details(), take_screenshot=True)

    page.wait_for_timeout(6000)

    # Step 4: Intercept API response to verify auction details
    # The fixture will capture and return these values
    captured_values = capture_api_values

    # Add a delay to make sure the API request has been triggered and the response captured
    page.wait_for_timeout(3000)

    assert captured_values.get("isPerishable") == True, \
        f"API Discount does not match! Expected 'isPerishable', got {captured_values.get('isPerishable')}"