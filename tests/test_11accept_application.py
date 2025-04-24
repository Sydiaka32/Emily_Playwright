import pytest
from pages.my_applications_page import MyApplicationPage
from pages.all_auctions_page import AllAuctionsPage
from pages.application_page import ApplicationPage
from pages.navigation_page import NavigationPage


@pytest.mark.parametrize('login', ['admin'], indirect=True)
def test_accept_application(published_auction, draft_application, published_application, allure_step, login):
    page = login
    all_auctions_page = AllAuctionsPage(page)
    my_applications_page = MyApplicationPage(page)
    application_page = ApplicationPage(page)
    navigation = NavigationPage(page)

    # Pre-Conditions: create auction -> create application for it -> publish application

    # Step 1: Login to admin as admin

    # Step 2: Go to applications

    # Step 3: Search for exact application by id?

    # Step 4: Go to application details

    # Step 5: Click on activate

    # Step 6: Go to user as participant

    # Step 7: Go to my-applications

    # Step 8: Verify status



