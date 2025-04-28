import pytest

from pages.user.auction_page import AuctionPage
from pages.user.my_auctions_page import MyAuctionsPage

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_create_copy_based(navigate_to_my_auctions, get_auction_id, allure_step, capture_api_values, login):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    allure_step("Switch to published", lambda: my_auctions_page.switch_to_published(), take_screenshot=True)

    # Step 1: Retrieve the original auction ID using the fixture
    original_auction_id = allure_step("Retrieve original auction id", lambda: get_auction_id(), take_screenshot=False)

    # Step 2: Click the copy option to create a new auction
    allure_step("Copy based option", lambda: my_auctions_page.copy_based_option(), take_screenshot=True)
    page.wait_for_timeout(1500)
    allure_step("Submit copy based popup", lambda: my_auctions_page.copy_popup_yes(), take_screenshot=True)
    page.wait_for_timeout(3000)

    # Capture previousAuctionId
    previous_id = allure_step("Get previous auction id", lambda: auction_page.get_previous_id(), take_screenshot=True)

    assert original_auction_id == previous_id, \
        f"Previous auction id is not the same as the original! {original_auction_id} != {previous_id}"

    # Enable discount and capture the value
    allure_step("Enable discount", lambda: auction_page.enable_discount(), take_screenshot=True)
    discount_value = allure_step("Get discount value", lambda: auction_page.get_discount_value(), take_screenshot=True)

    # Step 3: Save the draft of the copied auction
    allure_step("Save draft", lambda: auction_page.save_changes(), take_screenshot=False)

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

    # Now make assertions using the captured values
    assert captured_values.get("previousAuctionId") == previous_id, \
        f"API PreviousAuctionId does not match! Expected {previous_id}, got {captured_values.get('previousAuctionId')}"

    assert float(captured_values.get("discount")) == float(discount_value), \
        f"API Discount does not match! Expected {discount_value}, got {captured_values.get('discount')}"

    assert captured_values.get("isPerishable") == 'true', \
        f"API Discount does not match! Expected 'isPerishable', got {captured_values.get('isPerishable')}"
