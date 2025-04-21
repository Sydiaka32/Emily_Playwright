import pytest
from pages.my_applications_page import MyApplicationPage
from pages.all_auctions_page import AllAuctionsPage
from pages.application_page import ApplicationPage
from pages.navigation_page import NavigationPage


@pytest.mark.parametrize('login', ['t3'], indirect=True)
def test_creation_draft_application(published_auction, draft_application, allure_step, login):
    page = login
    all_auctions_page = AllAuctionsPage(page)
    my_applications_page = MyApplicationPage(page)
    application_page = ApplicationPage(page)
    navigation = NavigationPage(page)

    # Now you have:
    # - published_auction: ID of the published auction
    # - draft_application: bid created for that published auction

    # Step 1: Navigate to my applications
    allure_step("Search auction", lambda: navigation.navigate_to_my_applications(), take_screenshot=True)

    page.wait_for_timeout(5000)

    allure_step("Search auction", lambda: my_applications_page.publish_application(draft_application),
                take_screenshot=True)

    page.wait_for_timeout(5000)

    status = my_applications_page.get_application_status(draft_application).text_content()

    assert status == "Чернетка заяви", \
        f"Expected status to be 'Чернетка заяви', but got '{status}'"



