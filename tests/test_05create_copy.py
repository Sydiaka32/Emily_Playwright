from config.settings import ConfigParser
from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage


def test_create_copy(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    # Step 1: Click on the first auction (opens in a new tab)
    with page.expect_popup() as new_tab:
        my_auctions_page.retrieve_auction_id()
    auction_details_page = new_tab.value  # Get the new tab reference

    # Step 2: Extract the original auction ID from the URL
    original_auction_id = auction_details_page.url.split("/")[-1]

    # Step 3: Close auction details tab & return to "My Auctions"
    auction_details_page.close()

    # Step 4: Click the copy option to create a new auction
    my_auctions_page.copy_option()

    page.wait_for_timeout(1500)

    my_auctions_page.copy_popup_yes()

    page.wait_for_timeout(3000)

    # Step 5: Save the draft of the copied auction
    auction_page.save_changes()

    # Step 6: Wait and go to the new auction details page
    page.wait_for_timeout(3000)

    # Step 7: Click on the first auction again (assuming it's the copied auction)
    with page.expect_popup() as new_tab:
        my_auctions_page.retrieve_auction_id()
    copied_auction_details_page = new_tab.value

    # Step 8: Extract the copied auction ID from the URL
    copied_auction_id = copied_auction_details_page.url.split("/")[-1]

    # Step 9: Close the copied auction details page
    copied_auction_details_page.close()

    # Step 10: Compare IDs to ensure they are different
    assert original_auction_id != copied_auction_id, \
        f"Copied auction has the same ID as the original! {original_auction_id} == {copied_auction_id}"
