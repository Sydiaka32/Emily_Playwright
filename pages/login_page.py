from playwright.sync_api import Page
from config.settings import ConfigParser
from locators.login_locations import LoginLocators


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
        # Use the username, password, and URL from the config file
        self.page.goto(self.url)

        # Use the locators from the LoginLocators class
        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_t1)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_t3(self):
        # Use the username, password, and URL from the config file
        self.page.goto(self.url)

        # Use the locators from the LoginLocators class
        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_t3)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_mv(self):
        # Use the username, password, and URL from the config file
        self.page.goto(self.url)

        # Use the locators from the LoginLocators class
        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_mv)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

    def login_ad(self):
        # Use the username, password, and URL from the config file
        self.page.goto(self.admin_url)

        # Use the locators from the LoginLocators class
        # self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_ad)
        # self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        # self.page.locator(LoginLocators.SUBMIT_BUTTON).click()