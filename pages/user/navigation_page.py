from playwright.sync_api import Page
from locators.user.account_locators import AccountLocators
from config.settings import ConfigParser


class NavigationPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_my_auctions(self):
        """
        Navigates to the 'My Auctions' section via the personal account button and auctions tab.
        """
        self.page.locator(AccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.page.locator(AccountLocators.MY_AUCTIONS_TAB).click()

    def close_telegram_popup(self):
        """
        Closes the Telegram popup by clicking on the close icon.
        """
        self.page.locator("div").filter(has_text="У нас з'явився універсальний").nth(1).click()
        self.page.get_by_role("button").click()

    def close_notification(self):
        """
        Closes the visible notification alert by clicking the close icon.
        """
        self.page.locator("#notistack-snackbar").get_by_role("alert")
        self.page.locator(".jss764 > .MuiSvgIcon-root > path").click()

    def close_notification_if_exists(self):
        """
        Closes the notification if it exists by clicking the 'CloseIcon' test ID element.
        """
        self.page.get_by_test_id("CloseIcon").nth(1).click()

    def navigate_to_home(self):
        """
        Navigates to the home page after login using the base URL from config,
        loading the auctions page filtered by active tendering status.
        """
        home_url = f"{ConfigParser.base_url}/auctions?size=5&status=ACTIVE_TENDERING&procedureType=all"
        self.page.goto(home_url)
        self.page.wait_for_load_state("domcontentloaded")

    def navigate_to_my_applications(self):
        """
        Navigates to the 'My Applications' section via the personal account button and applications tab.
        """
        self.page.locator(AccountLocators.PERSONAL_ACCOUNT_BUTTON).click()
        self.page.locator(AccountLocators.MY_APPLICATIONS_TAB).click()
