import pytest

from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.auction_page import AuctionPage


@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_edit_draft(navigate_to_my_auctions, allure_step, login):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    # Step 1: Go to edit mode of draft and edit entities
    allure_step("Open Edit mode", lambda: my_auctions_page.edit_mode(), take_screenshot=False)
    allure_step("Edit title", lambda: auction_page.edit_title(), take_screenshot=True)
    page.wait_for_timeout(1000)
    allure_step("Save changes", lambda: auction_page.save_changes(), take_screenshot=False)

    # Handle updating time
    page.wait_for_timeout(2000)

    # Step 2: Compare edited entities
    assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", \
        f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"
