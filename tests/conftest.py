import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage


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


@pytest.fixture
def capture_api_values(sync_page, get_auction_id):
    captured_values = {}

    # Define the callback function to capture API responses
    def capture_api_response(response):
        if "api/v1.0/auctions/" in response.url:
            if response.status == 200:
                data = response.json()
                captured_values["previousAuctionId"] = data.get("previousProzorroAuctionId")
                captured_values["discount"] = data.get("specificData", {}).get("discount")

    # Listen for responses
    sync_page.on("response", capture_api_response)

    # Return the dictionary of captured values
    return captured_values


@pytest.fixture
def create_draft_auction(navigate_to_my_auctions, allure_step):
    """Fixture to create a draft auction and return auction details."""
    page = navigate_to_my_auctions

    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    # Auction creation steps
    allure_step("Navigate to 'New Auction' page", my_auctions_page.navigate_to_new_auction, take_screenshot=False)
    allure_step("Select organiser", auction_page.select_organiser, take_screenshot=False)
    allure_step("Select procedure", auction_page.select_procedure, take_screenshot=False)
    allure_step("Close Telegram popup", navigation_page.close_telegram_popup, take_screenshot=False)
    allure_step("Fill in Basic info block", auction_page.fill_basic_info_block, take_screenshot=True)
    allure_step("Fill in Details block", auction_page.fill_detail_lot_description_block, take_screenshot=True)
    allure_step("Select classifier", auction_page.select_classifier, take_screenshot=True)
    allure_step("Fill in Lot info block", auction_page.fill_lot_info_block, take_screenshot=False)
    allure_step("Point map", auction_page.point_map, take_screenshot=True)

    # Avoid hardcoded waits — wait for elements instead
    auction_page.wait_for_upload_ready()

    allure_step("Upload document", auction_page.upload_document, take_screenshot=False)
    allure_step("Save draft", auction_page.save_draft, take_screenshot=False)

    auction_page.wait_for_draft_saved()

    # Return auction details for further assertions in tests
    return {
        "title": my_auctions_page.get_card_title(),
        "procedure": my_auctions_page.get_card_procedure(),
        "status": my_auctions_page.get_card_status()
    }
