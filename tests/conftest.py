import pytest
import allure
from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage
from utils.api_utils import api_login_organiser, upload_document, create_auction, publish_auction



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
def login(sync_page, request):
    """Login fixture that supports multiple user roles."""
    login_page = LoginPage(sync_page)

    # Take user role from the parametrize decorator (default to t1)
    user_role = request.param if hasattr(request, "param") else "t1"

    # Handle login for different roles
    if user_role == "t1":
        login_page.login_t1()
    elif user_role == "t3":
        login_page.login_t3()
    elif user_role == "mv":
        login_page.login_mv()
    elif user_role == "admin":
        login_page.login_ad()
    else:
        raise ValueError(f"Unsupported user role: {user_role}")

    expect(sync_page.get_by_role("button", name="Особистий кабінет")).to_be_visible(timeout=10000)

    # Ensure navigation to home after login
    navigation_page = NavigationPage(sync_page)
    navigation_page.navigate_to_home()  # Navigate to auctions page after login

    return sync_page


def navigate_to_my_auctions(sync_page):
    """Navigation helper function"""
    navigation_page = NavigationPage(sync_page)
    navigation_page.navigate_to_my_auctions()


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

    # Capture API responses only for the right endpoint
    def capture_api_response(response):
        if "api/v1.0/auctions/" in response.url and response.status == 200:
            data = response.json()
            captured_values["previousAuctionId"] = data.get("previousProzorroAuctionId")
            captured_values["discount"] = data.get("specificData", {}).get("discount")
            captured_values["isPerishable"] = data.get("specificData", {}).get("isPerishable")

            # Debug print for clarity
            print(f"Captured Data: {captured_values}")

    # Hook into page responses
    sync_page.on("response", capture_api_response)

    # Ensure a fresh start for each test
    yield captured_values

    # Clean up listener after test
    sync_page.remove_listener("response", capture_api_response)



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


@pytest.fixture(scope="function")
def published_auction():
    """
    Fixture to log in, upload a document, create an auction, publish it,
    and extract the prozorroId.
    Returns the prozorroId for use in search tests.
    """
    # Step 1: Upload a document
    document_id = upload_document()

    # Step 2: Create the auction using the document_id
    auction_id = create_auction()

    # Step 3: Publish the auction and get the response
    publish_response = publish_auction()

    # Step 4: Extract prozorroId
    prozorro_id = publish_response.get("prozorroId")

    if not prozorro_id:
        raise ValueError("Prozorro ID is missing in the response")

    # Return the prozorroId for use in test cases
    yield prozorro_id
