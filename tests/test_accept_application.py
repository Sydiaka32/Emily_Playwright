import pytest

from pages.admin.application_details_page import ApplicationDetailsPageAdmin
from pages.admin.applications_page import ApplicationPageAdmin
from pages.admin.navigation_page import NavigationPageAdmin


@pytest.mark.parametrize('login', ['admin'], indirect=True)
def test_accept_application(published_auction, draft_application, published_application, allure_step, login):
    page = login
    navigation_admin = NavigationPageAdmin(page)
    applications_page_admin = ApplicationPageAdmin(page)
    application_details_page = ApplicationDetailsPageAdmin(page)

    bid_id = draft_application

    # Pre-Conditions: create auction -> create application for it -> publish application
    # Implemented with fixtures

    # Step 1: Login to admin as admin
    # Implemented with fixtures
    # Step 2: Go to applications
    allure_step("Go to Applications page", lambda: navigation_admin.navigate_to_applications(), take_screenshot=True)



    # Step 3: Search for exact application by id?
    allure_step("Search for the exact bid", lambda: applications_page_admin.search_bid(bid_id=bid_id),
                take_screenshot=True)



    # Step 4: Go to application details
    allure_step("Go to bid details", lambda: applications_page_admin.goto_bid_details(),
                take_screenshot=True)

    page.wait_for_timeout(3000)

    # Step 5: Click on activate
    allure_step("Go to bid details", lambda: application_details_page.activate_option(),
                take_screenshot=True)

    page.wait_for_timeout(3000)

    # Step 6: Verify status
    bid_status = applications_page_admin.get_confirmed_status(bid_id)
    verification_status = applications_page_admin.get_activated_status(bid_id)

    assert bid_status == "Підтверджена заява", \
        f"Expected status to be 'Підтверджена заява', but got '{bid_status}'"

    assert verification_status == "Активовано", \
        f"Expected status to be 'Активовано', but got '{verification_status}'"



