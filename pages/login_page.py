from playwright.sync_api import Page
from config.settings import ConfigParser
from locators.login_locations import LoginLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Accessing the credentials and URL from ConfigParser class
        self.username = ConfigParser.email_t1  # Using email_t1 from settings.py
        self.password = ConfigParser.password_user  # Using password_user from settings.py
        self.url = ConfigParser.user_login_url  # Using user_login_url from settings.py

    def login(self):
        # Use the username, password, and URL from the config file
        self.page.goto(self.url)

        # Use the locators from the LoginLocators class
        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()

