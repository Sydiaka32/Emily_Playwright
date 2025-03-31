from playwright.sync_api import Page
from locators.account_locators import AccountLocators
from config.settings import ConfigParser


class NavigationPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_my_auctions(self):
        self.page.locator(AccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.page.locator(AccountLocators.MY_AUCTIONS_TAB).click()

    def close_telegram_popup(self):
        self.page.locator("div").filter(has_text="У нас з'явився універсальний").nth(1).click()
        self.page.get_by_role("button").click()

    def close_notification(self):
        self.page.locator("#notistack-snackbar").get_by_role("alert")
        self.page.locator(".jss764 > .MuiSvgIcon-root > path").click()

    def close_notification_if_exists(self):
        # Use nth() to select the last element in the matched list
        # element = self.page.locator("//*[local-name()='svg' and contains(@class, 'MuiSvgIcon-root') and @viewBox='0 0 24 24'][./*[local-name()='path' and @d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z']]").nth(
        #     -1)
        # element.click()
        self.page.get_by_test_id("CloseIcon").nth(1).click()

    def navigate_to_home(self):
        """Navigates to the home page after login, using the configured base URL."""
        home_url = f"{ConfigParser.base_url}/auctions?size=5&status=ACTIVE_TENDERING&procedureType=all"
        self.page.goto(home_url)
        self.page.wait_for_load_state("domcontentloaded")






