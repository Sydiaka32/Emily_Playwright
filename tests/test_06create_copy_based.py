from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_details_page import AuctionDetailsPage


def test_create_copy(navigate_to_my_auctions, get_auction_id, allure_step):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    auction_details_page = AuctionDetailsPage(page)

    allure_step("Switch to published", my_auctions_page.switch_to_published(), take_screenshot=True)

    # Step 1: Retrieve the original auction ID using the fixture
    original_auction_id = allure_step("Retrieve original auction id", get_auction_id(), take_screenshot=False)

    # Step 2: Click the copy option to create a new auction
    allure_step("Copy based option", my_auctions_page.copy_based_option(), take_screenshot=True)
    page.wait_for_timeout(1500)
    allure_step("Submit copy based popup", my_auctions_page.copy_popup_yes(), take_screenshot=True)
    page.wait_for_timeout(3000)

    previous_id = allure_step("Get previous auction id", auction_page.get_previous_id(), take_screenshot=True)

    assert original_auction_id == previous_id, \
        f"Previous auction id is not the same as the original! {original_auction_id} != {previous_id}"

    allure_step("Enable discount", auction_page.enable_discount(), take_screenshot=True)

    # Step 3: Save the draft of the copied auction
    allure_step("Save draft", auction_page.save_changes(), take_screenshot=False)

    page.wait_for_timeout(3000)

    allure_step("Publish option", my_auctions_page.publish_option(), take_screenshot=True)

    page.wait_for_timeout(3000)

    allure_step("Go to auction details", my_auctions_page.goto_auction_details(), take_screenshot=True)

    page.wait_for_timeout(6000)

    # Step 4: Verify information on auction details

    # check discount
    # discount_value = auction_details_page.get_discount_value()
    # assert discount_value == '2', \
    #     f"Discount is not the same as entered one! {discount_value} != '2'"

    # check id of previous auction
    auction_details_page.expand_details()
    previous_id_value = auction_details_page.get_previous_id_value()
    assert previous_id_value == previous_id, \
        f"Ids do not match! {previous_id_value} != {previous_id}"

