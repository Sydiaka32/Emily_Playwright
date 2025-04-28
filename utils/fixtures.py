import pytest
from playwright.sync_api import sync_playwright
from pages.user.login_page import LoginPage
from pages.user.navigation_page import NavigationPage


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
