from playwright.sync_api import Page
from locators.account_locators import AccountLocators
from locators.all_auctions_locators import AllAuctionsLocators
from locators.my_auctions_locators import MyAuctionsLocators


class ApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def select_profile(self):
        # Replace with the locator for the status field in the card
        self.page.get_by_label("Не визначено").get_by_text("Не визначено").click()
        self.page.get_by_role("option", name="62").click()

    def fill_price(self):
        self.page.get_by_role("textbox", name="Не визначено").fill("1500")

    def continue_option(self):
        self.page.get_by_role("button", name="Продовжити").click()

    def confirmation_checks(self):
        self.page.get_by_role("checkbox", name="Даю згоду на обробку персональних даних та "
                                               "приймаю умови Політики конфіденційнос").check()
        self.page.get_by_role("checkbox", name="Ознайомлений з Регламентом роботи "
                                               "системи електронних торгів").check()

    def save_draft_application(self):
        self.page.get_by_role("button", name="Зберегти чернетку").click()









