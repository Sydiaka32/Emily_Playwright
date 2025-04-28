import pytest

from pages.user.navigation_page import NavigationPage
from pages.user.my_auctions_page import MyAuctionsPage
from pages.user.auction_page import AuctionPage
from locators.user.auction_locators import BankAccounts

@pytest.mark.parametrize('login', ['t1'], indirect=True)
def test_bank_accounts(navigate_to_my_auctions, allure_step, login):
    page = navigate_to_my_auctions

    my_auctions_page = MyAuctionsPage(page)
    auction_page = AuctionPage(page)
    navigation_page = NavigationPage(page)

    allure_step("Navigate to 'New Auction' page", lambda: my_auctions_page.navigate_to_new_auction())

    allure_step("Fill in all required fields", lambda: (
        auction_page.select_organiser(),
        auction_page.select_procedure(),
        navigation_page.close_telegram_popup(),
        auction_page.fill_basic_info_block(),
        auction_page.fill_detail_lot_description_block(),
        auction_page.select_classifier(),
        auction_page.fill_lot_info_block(),
        auction_page.point_map(),
        page.wait_for_timeout(4000),
    ))

    # Define bank accounts and currencies
    bank_accounts = [
        (BankAccounts.REGISTRATION_FEE_OPTION, None),
        (BankAccounts.OTHER_OPTION, None),
        (BankAccounts.PAYMENT_OPTION, None),
        (BankAccounts.GUARANTEE_OPTION, None),
        (BankAccounts.REGISTRATION_FEE_OPTION, "USD"),
        (BankAccounts.OTHER_OPTION, "USD"),
        (BankAccounts.PAYMENT_OPTION, "USD"),
        (BankAccounts.GUARANTEE_OPTION, "USD"),
        (BankAccounts.REGISTRATION_FEE_OPTION, "EUR"),
        (BankAccounts.OTHER_OPTION, "EUR"),
        (BankAccounts.PAYMENT_OPTION, "EUR"),
        (BankAccounts.GUARANTEE_OPTION, "EUR"),
    ]

    # Loop through and add bank accounts dynamically
    for account_type, currency in bank_accounts:
        allure_step(f"Add bank account: {account_type} ({currency if currency else 'UAH'})",
                    lambda: auction_page.add_bank_account(account_type, currency), take_screenshot=True)

    # Upload document
    allure_step("Upload document", lambda: auction_page.upload_document())

    # Step 3: Save draft
    allure_step("Save draft", lambda: auction_page.save_draft())

    page.wait_for_timeout(3000)
