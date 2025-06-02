import pytest

from pages.user.auction_page import AuctionPage
from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.navigation_page import NavigationPage


@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_create_copy(created_auction, get_auction_id, allure_step, login):
    page = login
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)
    original_auction_id = created_auction

    # Step 1: Navigate to my auctions
    allure_step("Navigate to my auctions", lambda: navigation_page.navigate_to_my_auctions(), take_screenshot=False)
    allure_step("Switch to published tab", lambda: my_auctions_page.switch_to_published(), take_screenshot=True)

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