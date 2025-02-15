from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


def test_edit_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)

    # Step 1: Go to edit mode of draft and edit entities
    my_auctions_page.edit_mode()
    auction_page.edit_title()
    page.wait_for_timeout(1000)
    auction_page.save_changes()

    # Handle updating time
    page.wait_for_timeout(2000)

    # Step 2: Compare edited entities
    assert my_auctions_page.get_card_title() == "AuctionEditedForDeletion", \
        f"Expected title to be 'Auction', but got '{MyAuctionsPage.get_card_title()}'"
