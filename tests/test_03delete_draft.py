import pytest

from config.settings import ConfigParser
from pages.my_auctions_page import MyAuctionsPage

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_delete_draft(navigate_to_my_auctions, get_auction_id, allure_step, login):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    config_parser = ConfigParser()

    # Step 1: Retrieve the original auction ID using the fixture
    auction_id = allure_step("Retrieve auction id", lambda: get_auction_id(), take_screenshot=False)

    # Step 2: Delete draft
    allure_step("Delete draft", lambda: my_auctions_page.delete_option(), take_screenshot=False)

    # Handle updating time
    page.wait_for_timeout(3000)

    # Step 3: Manually try to visit the auction details page
    allure_step("Manually try to visit deleted auction",
                lambda: page.goto(f"{config_parser.base_url}/auctions/{auction_id}"), take_screenshot=True)
    page.wait_for_timeout(3000)

    # Step 4: Verify redirection
    assert (f"{config_parser.all_auctions_url}" in page.url), \
        f"Auction {auction_id} was not deleted, expected redirection!"



