from playwright.sync_api import Page
from config.settings import ConfigParser
from locators.admin.login_locators import LoginLocatorsAdmin


class LoginPageAdmin:
    def __init__(self, page: Page):
        self.page = page

        # Accessing the credentials and URL from ConfigParser class
        self.password = ConfigParser.password_ad
        self.username_ad = ConfigParser.email_ad
        self.admin_url = ConfigParser.admin_login_url


    def login_ad(self):
        """Performs login action on the admin login page"""

        # Navigate to the admin login page
        self.page.goto(self.admin_url)

        # Fill in the email and password fields using locators and credentials
        self.page.locator(LoginLocatorsAdmin.EMAIL_INPUT).fill(self.username_ad)
        self.page.locator(LoginLocatorsAdmin.PASSWORD_INPUT).fill(self.password)

        # Click the login/submit button
        self.page.locator(LoginLocatorsAdmin.SUBMIT_BUTTON).click()