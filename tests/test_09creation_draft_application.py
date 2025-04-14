from multiprocessing import context

import pytest
from pages.my_applications_page import MyApplicationPage
from pages.all_auctions_page import AllAuctionsPage
from pages.application_page import ApplicationPage


@pytest.mark.parametrize('login', ['t3'], indirect=True)
def test_creation_draft_application(published_auction, allure_step, login):
    page = login
    all_auctions_page = AllAuctionsPage(page)
    my_applications_page = MyApplicationPage(page)
    application_page = ApplicationPage(page)
    auction_details_page = None  # Will be initialized after navigation

    # Step 1 - Search for auction
    allure_step("Search auction", lambda: all_auctions_page.search_auction(published_auction), take_screenshot=True)

    # Step 2 - Navigate to details (this handles popup)
    auction_details_page = allure_step("Go to auction details", lambda: all_auctions_page.goto_details(),
                                       take_screenshot=False)

    page.wait_for_timeout(3000)

    # Step 3 - Apply for participation
    allure_step("Initiate application process", lambda: auction_details_page.apply_for_auction(), take_screenshot=False)

    # Step 4 - Select profile and set price
    allure_step("Set bid parameters", application_page.select_profile(), take_screenshot=False)

    allure_step("Set bid parameters", application_page.fill_price(), take_screenshot=False)

    allure_step("Set bid parameters", application_page.continue_option(), take_screenshot=False)

    # Step 5 - Handle agreements
    allure_step("Accept terms and conditions", application_page.confirmation_checks(), take_screenshot=False)

    # Step 6 - Submit application
    allure_step("Submit draft application", application_page.save_draft_application(), take_screenshot=False)

    # Step 7 - Assert values directly
    assert my_applications_page.verify_application_status("Неопублікована заява"), "Application status not correct"
    assert my_applications_page.verify_draft_price("1700 грн"), "Draft price is incorrect"
    assert my_applications_page.verify_organization_name("SdU, UA-EDR"), "Organization name is incorrect"

