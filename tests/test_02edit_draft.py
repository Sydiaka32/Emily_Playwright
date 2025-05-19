import pytest

from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.auction_page import AuctionPage
from pages.user.navigation_page import NavigationPage


@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_edit_draft(created_auction, allure_step, login):
    page = login
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation = NavigationPage(page)

    # Step 1: Navigate to my auctions
    allure_step("Navigate to my auctions", lambda: navigation.navigate_to_my_auctions(), take_screenshot=False)

    # Step 2: Switch tab to drafts
    allure_step("Switch tab to drafts", lambda: my_auctions_page.switch_to_drafts(), take_screenshot=False)

    # Step 3: Open Edit mode
    allure_step("Open Edit mode", lambda: my_auctions_page.edit_mode(), take_screenshot=False)

    # Step 4: Edit title
    allure_step("Edit title", lambda: auction_page.edit_title(), take_screenshot=True)

    page.wait_for_timeout(1000)

    # Step 5: Save changes
    allure_step("Save changes", lambda: auction_page.save_changes(), take_screenshot=False)

    # Handle updating time
    page.wait_for_timeout(2000)

    # Step 6: Compare edited entities
    assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", \
        f"Expected title to be 'Auction', but got '{my_auctions_page.get_card_title()}'"
