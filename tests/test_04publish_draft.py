from pages.my_auctions_page import MyAuctionsPage
from pages.navigation_page import NavigationPage


def test_publish_draft(navigate_to_my_auctions):
    page = navigate_to_my_auctions  # The browser object passed by the fixture
    my_auctions_page = MyAuctionsPage(page)
    navigation_page = NavigationPage(page)

    # Step 1: Publish draft
    my_auctions_page.publish_option()

    # Handle updating time
    page.wait_for_timeout(1500)

    # Refresh the current page
    page.reload()

    # Handle popup and updating time
    page.wait_for_timeout(3000)
    navigation_page.close_notification_if_exists()

    # Step 2: Compare edited title
    assert my_auctions_page.get_card_published_status() == "Прийняття заяв на участь", \
        (f"Expected title to be 'Прийняття заяв на участь', "
         f"but got '{my_auctions_page.get_card_published_status()}'")

