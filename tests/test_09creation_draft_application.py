import pytest
from pages.auction_page import AuctionPage
from pages.all_auctions_page import AllAuctionsPage


@pytest.mark.parametrize('login', ['t3'], indirect=True)
def test_creation_draft_application(published_auction, allure_step, login):
    page = login
    all_auctions_page = AllAuctionsPage(page)
    auction_details_page = None  # Will be initialized after navigation

    # Step 1 - Search for auction
    allure_step("Search auction", all_auctions_page.search_auction(published_auction), take_screenshot=True)


    # Step 2 - Navigate to details (this handles popup)
    allure_step("Go to auction details", auction_details_page = all_auctions_page.goto_details())

    # Step 3 - Apply for participation
    allure_step("Initiate application process", lambda: auction_details_page.click_participate_button())
    #
    # # Step 4 - Select profile and set price
    # allure_step("Set bid parameters", auction_details_page.select_profile("62"),
    #             auction_details_page.set_bid_price("1700"), auction_details_page.click_continue())
    #
    # # Step 5 - Handle agreements
    # allure_step("Accept terms and conditions", auction_details_page.accept_privacy_policy(),
    #             auction_details_page.accept_regulations()
    #
    # # Step 6 - Submit application
    # allure_step("Submit draft application", auction_details_page.submit_application())
    #
    #
    # # Step 7 - Verify draft creation
    # allure_step("Verify draft application details", auction_details_page.verify_draft_price("1700 грн"),
    #             auction_details_page.verify_application_status("Чернетка заяви"),
    #             auction_details_page.verify_organization_name("Aphrodite, UA-EDR"))

