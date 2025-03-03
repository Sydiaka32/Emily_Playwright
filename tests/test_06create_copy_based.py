from pages.auction_page import AuctionPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_details_page import AuctionDetailsPage


def test_create_copy(navigate_to_my_auctions, get_auction_id):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    auction_details_page = AuctionDetailsPage(page)

    my_auctions_page.switch_to_published()

    # Step 1: Retrieve the original auction ID using the fixture
    original_auction_id = get_auction_id()

    # Step 2: Click the copy option to create a new auction
    my_auctions_page.copy_based_option()
    page.wait_for_timeout(1500)
    my_auctions_page.copy_popup_yes()
    page.wait_for_timeout(3000)

    previous_id = auction_page.get_previous_id()

    assert original_auction_id == previous_id, \
        f"Previous auction id is not the same as the original! {original_auction_id} != {previous_id}"

    auction_page.enable_discount()

    # Step 3: Save the draft of the copied auction
    auction_page.save_changes()

    page.wait_for_timeout(3000)

    my_auctions_page.publish_option()

    page.wait_for_timeout(3000)

    my_auctions_page.goto_auction_details()

    page.wait_for_timeout(6000)

    # Step 4: Verify information on auction details

    # check discount
    # discount_value = auction_details_page.get_discount_value()
    # assert discount_value == '2', \
    #     f"Discount is not the same as entered one! {discount_value} != '2'"

    # check id of previous auction
    auction_details_page.expand_details()
    previous_id_value = auction_details_page.get_previous_id_value()
    assert previous_id_value == previous_id, \
        f"Ids do not match! {previous_id_value} != {previous_id}"

