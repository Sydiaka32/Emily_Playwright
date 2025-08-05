from playwright.sync_api import Page
from locators.admin.navigation_locators import NavigationLocatorsAdmin


class NavigationPageAdmin:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_applications(self):
        """Navigates to the Applications tab in the admin panel"""
        self.page.get_by_role("banner").get_by_role("button").first.click()
        self.page.get_by_role("link", name=NavigationLocatorsAdmin.APPLICATIONS_TAB).click()
