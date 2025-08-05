import pytest

from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.navigation_page import NavigationPage

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_publish_draft(created_auction, allure_step, login):
    page = login
    my_auctions_page = MyAuctionsPage(page)
    navigation_page = NavigationPage(page)


    # Step 1: Navigate to my auctions
    allure_step("Navigate to my auctions", lambda: navigation_page.navigate_to_my_auctions(), take_screenshot=False)

    # Step 2: Switch tab to drafts
    allure_step("Switch tab to drafts", lambda: my_auctions_page.switch_to_drafts(), take_screenshot=False)

    # Step 3: Publish draft
    allure_step("Publish draft", lambda: my_auctions_page.publish_option(), take_screenshot=True)

    # Handle updating time
    page.wait_for_timeout(1500)

    # Step 4: Refresh page
    allure_step("Refresh current page", lambda: page.reload(), take_screenshot=False)

    # Handle popup and updating time
    page.wait_for_timeout(3000)

    # Step 5: Get auction status
    card_status = allure_step("Get auction status", lambda: my_auctions_page.get_card_published_status(),
                              take_screenshot=True)

    # Step 6: Compare status
    assert "Прийняття заяв на участь" in card_status, \
        f"Expected status to contain 'Прийняття заяв на участь', but got '{card_status}'"

