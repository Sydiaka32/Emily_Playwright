import pytest
from pages.user.my_applications_page import MyApplicationPage
from pages.user.all_auctions_page import AllAuctionsPage
from pages.user.application_page import ApplicationPage


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

    application_page = ApplicationPage(auction_details_page.page)

    page.wait_for_timeout(3000)

    # Step 3 - Apply for participation
    allure_step("Initiate application process", lambda: auction_details_page.apply_for_auction(), take_screenshot=False)

    # Step 4 - Select profile and set price
    allure_step("Set bid parameters", lambda: application_page.select_profile(), take_screenshot=False)

    allure_step("Set bid parameters", lambda: application_page.fill_price(), take_screenshot=False)

    allure_step("Set bid parameters", lambda: application_page.continue_option(), take_screenshot=False)

    # Step 5 - Handle agreements
    allure_step("Accept terms and conditions", lambda: application_page.confirmation_checks(), take_screenshot=False)

    # Step 6 - Submit application
    allure_step("Submit draft application", lambda: application_page.save_draft_application(), take_screenshot=False)

    page.wait_for_timeout(5000)
    current_page = application_page.page
    print("Redirected to URL:", current_page.url)

    my_applications_page = MyApplicationPage(current_page)

    allure_step("Open application details", lambda: my_applications_page.open_application_details(), take_screenshot=False)


    # Step 7 - Assert values directly
    assert my_applications_page.get_app_status() == "Неопублікована заява", \
        f"Expected status to be 'Неопублікована заява', but got '{my_applications_page.get_app_status()}'"

    assert "500" in my_applications_page.get_app_price(), \
        f"Price should contain '500', got '{my_applications_page.get_app_price()}'"

    assert my_applications_page.get_app_profile() == "62 | Юридична особа - резидент | Aphrodite", \
        (f"Expected profile to be '62 | Юридична особа - резидент | Aphrodite', "
         f"but got '{my_applications_page.get_app_profile()}'")


