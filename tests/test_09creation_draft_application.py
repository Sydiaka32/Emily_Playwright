import pytest
from pages.auction_page import AuctionPage
from pages.all_auctions_page import AllAuctionsPage

@pytest.mark.parametrize('login', ['t3'], indirect=True)
def test_creation_draft_application(published_auction, allure_step, login):
    page = login  # The browser object passed by the fixture
    auction_page = AuctionPage(page)
    all_auctions_page = AllAuctionsPage(page)

    # Step 1 - Search for auction
    allure_step("Search auction", lambda: all_auctions_page.search_auction(published_auction), take_screenshot=True)
    page.wait_for_timeout(6000)

    # Step 2 - Go to details
    allure_step("Go to auction details", lambda: all_auctions_page.goto_details())

    page.wait_for_timeout(6000)

    # Step 3 - Click on apply

    # Step 4 - Select profile + fill in the price

    # Step 5 - Upload documents if needed

    # Step 6 - Save draft
