from playwright.sync_api import Page
from config.settings import ConfigParser
from locators.user.login_locations import LoginLocators


class LoginPage:
    def __init__(self, page: Page):

        self.page = page

        # Accessing the credentials and URL from ConfigParser class
        self.username_t1 = ConfigParser.email_t1  # Using email_t1 from settings.py
        self.password = ConfigParser.password_user  # Using password_user from settings.py
        self.url = ConfigParser.user_login_url  # Using user_login_url from settings.py
        self.username_t3 = ConfigParser.email_t3
        self.username_mv = ConfigParser.email_mv
        self.username_ad = ConfigParser.email_ad
        self.admin_url = ConfigParser.admin_login_url

    def login_t1(self):
        """
        Logs in as user T1 by navigating to user login URL,
        filling the email and password fields, and submitting the form.
        """
        self.page.goto(self.url)

        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_t1)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_t3(self):
        """
        Logs in as user T3 by navigating to user login URL,
        filling the email and password fields, and submitting the form.
        """
        self.page.goto(self.url)

        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_t3)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_mv(self):
        """
        Logs in as user MV by navigating to user login URL,
        filling the email and password fields, and submitting the form.
        """
        self.page.goto(self.url)

        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_mv)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_ad(self):
        """Navigates to the admin login URL."""
        self.page.goto(self.admin_url)
