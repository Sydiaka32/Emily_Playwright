import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage


@pytest.fixture(scope="function")
def sync_page():
    """Main sync Playwright page fixture"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.fixture
def login(sync_page):
    """Login fixture using sync page"""
    login_page = LoginPage(sync_page)
    login_page.login_t1()
    return sync_page


@pytest.fixture
def navigate_to_my_auctions(login):
    """Navigation fixture using sync page"""
    navigation_page = NavigationPage(login)
    navigation_page.navigate_to_my_auctions()
    return login


@pytest.fixture
def get_auction_id(navigate_to_my_auctions):
    """Auction ID retrieval fixture"""

    def _get_auction_id():
        my_auctions_page = MyAuctionsPage(navigate_to_my_auctions)

        with navigate_to_my_auctions.expect_popup() as new_tab:
            my_auctions_page.retrieve_auction_id()

        auction_details_page = new_tab.value
        auction_id = auction_details_page.url.split("/")[-1]
        auction_details_page.close()

        return auction_id

    return _get_auction_id


@pytest.fixture
def allure_step(sync_page):
    def _step(name, action, take_screenshot=True):
        with allure.step(name):
            result = action()
            if take_screenshot:
                allure.attach(sync_page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)
            return result
    return _step

