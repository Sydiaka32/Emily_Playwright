import pytest

from pages.my_auctions_page import MyAuctionsPage
from pages.navigation_page import NavigationPage

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_publish_draft(navigate_to_my_auctions, allure_step, login):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    navigation_page = NavigationPage(page)

    # Step 1: Publish draft
    allure_step("Publish draft", lambda: my_auctions_page.publish_option(), take_screenshot=True)

    # Handle updating time
    page.wait_for_timeout(1500)

    # Refresh the current page
    allure_step("Refresh current page", lambda: page.reload(), take_screenshot=False)

    # Handle popup and updating time
    page.wait_for_timeout(3000)
    navigation_page.close_notification_if_exists()

    card_status = allure_step("Get auction status", lambda: my_auctions_page.get_card_published_status(), take_screenshot=True)

    # Step 2: Compare edited title
    assert card_status == "Прийняття заяв на участь", \
        (f"Expected title to be 'Прийняття заяв на участь', "
         f"but got '{card_status}'")

