from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage


def test_create_copy(navigate_to_my_auctions, get_auction_id):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    my_auctions_page.switch_to_published()

    # Step 1: Retrieve the original auction ID using the fixture
    original_auction_id = get_auction_id()

    # Step 2: Click the copy option to create a new auction
    my_auctions_page.copy_option()
    page.wait_for_timeout(1500)
    my_auctions_page.copy_popup_yes()
    page.wait_for_timeout(3000)

    # Step 3: Save the draft of the copied auction
    auction_page.save_changes()

    # Step 4: Wait and retrieve the copied auction ID using the fixture
    page.wait_for_timeout(3000)
    copied_auction_id = get_auction_id()

    # Step 5: Compare IDs to ensure they are different
    assert original_auction_id != copied_auction_id, \
        f"Copied auction has the same ID as the original! {original_auction_id} == {copied_auction_id}"