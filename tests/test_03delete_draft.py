import pytest

from config.settings import ConfigParser
from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.navigation_page import NavigationPage


@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_delete_draft(created_auction, allure_step, login):
    page = login
    my_auctions_page = MyAuctionsPage(page)
    config_parser = ConfigParser()
    navigation = NavigationPage(page)

    auction_id = created_auction

    # Step 1: Navigate to my auctions
    allure_step("Navigate to my auctions", lambda: navigation.navigate_to_my_auctions(), take_screenshot=False)

    # Step 2: Switch tab to drafts
    allure_step("Switch tab to drafts", lambda: my_auctions_page.switch_to_drafts(), take_screenshot=False)

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



