import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.my_auctions_page import MyAuctionsPage
from pages.auction_page import AuctionPage

@pytest.fixture(scope="function")
def browser():
    """Set up and tear down a browser instance."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page  # Provide the page object to tests
        browser.close()

@pytest.fixture
def login(browser):
    """Log in to the website."""
    login_page = LoginPage(browser)
    login_page.login_t1()
    return browser  # Pass the logged-in page object

@pytest.fixture
def navigate_to_my_auctions(login):
    """Navigate to 'My Auctions' page."""
    navigation_page = NavigationPage(login)
    navigation_page.navigate_to_my_auctions()
    return login  # Pass the browser with 'My Auctions' loaded

@pytest.fixture
def get_auction_id(navigate_to_my_auctions):
    """Fixture to open an auction in a new tab, retrieve its ID, and close the tab."""
    def _get_auction_id():
        # Initialize MyAuctionsPage with the page object
        my_auctions_page = MyAuctionsPage(navigate_to_my_auctions)

        # Open the auction in a new tab
        with navigate_to_my_auctions.expect_popup() as new_tab:
            my_auctions_page.retrieve_auction_id()  # Call the method to open the auction
        auction_details_page = new_tab.value  # Get the new tab reference

        # Extract the auction ID from the URL
        auction_id = auction_details_page.url.split("/")[-1]

        # Close the auction details tab
        auction_details_page.close()

        return auction_id
    return _get_auction_id

