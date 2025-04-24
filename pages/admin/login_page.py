from playwright.sync_api import Page
from config.settings import ConfigParser
from locators.login_locations import LoginLocators


class LoginPageAdmin:
    def __init__(self, page: Page):
        self.page = page

        # Accessing the credentials and URL from ConfigParser class
        self.password = ConfigParser.password_user
        self.username_ad = ConfigParser.email_ad
        self.admin_url = ConfigParser.admin_login_url


    def login_ad(self):
        # Use the username, password, and URL from the config file
        self.page.goto(self.admin_url)

        # Use the locators from the LoginLocators class
        self.page.locator(LoginLocators.EMAIL_INPUT).fill(self.username_ad)
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(self.password)
        self.page.locator(LoginLocators.SUBMIT_BUTTON).click()