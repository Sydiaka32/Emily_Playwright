import pytest

from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_create_copy(navigate_to_my_auctions, get_auction_id, allure_step, login):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    allure_step("Switch to published tab", lambda: my_auctions_page.switch_to_published(), take_screenshot=True)

    # Step 1: Retrieve the original auction ID using the fixture
    original_auction_id = allure_step("Retrieve the original auction id", lambda: get_auction_id(), take_screenshot=False)

    # Step 2: Click the copy option to create a new auction
    allure_step("Copy option", lambda: my_auctions_page.copy_option(), take_screenshot=True)
    page.wait_for_timeout(1500)
    allure_step("Submit copy popup", lambda: my_auctions_page.copy_popup_yes(), take_screenshot=True)
    page.wait_for_timeout(3000)

    # Step 3: Save the draft of the copied auction
    allure_step("Save draft", lambda: auction_page.save_changes(), take_screenshot=False)

    # Step 4: Wait and retrieve the copied auction ID using the fixture
    page.wait_for_timeout(3000)
    copied_auction_id = allure_step("Retrieve id of copied auction", lambda: get_auction_id(), take_screenshot=False)

    # Step 5: Compare IDs to ensure they are different
    assert original_auction_id != copied_auction_id, \
        f"Copied auction has the same ID as the original! {original_auction_id} == {copied_auction_id}"