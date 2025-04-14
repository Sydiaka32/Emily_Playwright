import re
from playwright.sync_api import Page, expect
from locators.auction_locators import (OrganiserBlock, BasicInfoBlock, DetailLotDescriptionBlock,
                                                           LotInfoBlock, DocumentsBlock, SubmitionBlock, BankAccounts)
from pathlib import Path
from pages.my_auctions_page import MyAuctionsPage



class AuctionPage:
    def __init__(self, page: Page):
        self.page = page

    def select_organiser(self):
        self.page.get_by_label("", exact=True).click()
        self.page.locator(OrganiserBlock.ORGANISER_OPTION).click()

    def select_procedure(self):
        self.page.locator(BasicInfoBlock.AUCTION_TYPE).click()
        self.page.get_by_role("option", name=BasicInfoBlock.BSE_OPTION).click()
        # self.page.locator(BasicInfoBlock.BSE_OPTION).click()

    def fill_basic_info_block(self):
        self.page.get_by_placeholder(BasicInfoBlock.AUCTION_TITLE).first.fill('Auction')
        self.page.get_by_placeholder("Введіть номер лотa").click()
        self.page.get_by_placeholder("Введіть номер лотa").fill("1")
        self.page.locator(BasicInfoBlock.DESCRIPTION).first.fill('Description')

    def fill_detail_lot_description_block(self):
        self.page.locator(DetailLotDescriptionBlock.INITIAL_AMOUNT).fill("1200")
        self.page.locator(DetailLotDescriptionBlock.MIN_STEP).fill('1.4')

    def select_classifier(self):
        self.page.get_by_placeholder(LotInfoBlock.CLASSIFIER).click()
        (self.page.get_by_role("treeitem", name=LotInfoBlock.SELECT_CLASSIFIER).
         get_by_role(LotInfoBlock.CHECKBOX_CLASSIFIER).check())
        self.page.get_by_role("button", name=LotInfoBlock.SUBMIT_CLASSIFIER).click()

    def select_perishable_classifier(self):
        self.page.get_by_placeholder(LotInfoBlock.CLASSIFIER).click()
        (self.page.get_by_role("treeitem", name=LotInfoBlock.SELECT_PERISHABLE).
         get_by_role(LotInfoBlock.CHECKBOX_CLASSIFIER).check())
        self.page.get_by_role("button", name=LotInfoBlock.SUBMIT_CLASSIFIER).click()

    def fill_lot_info_block(self):
        self.page.locator(LotInfoBlock.LOT_QUANTITY).fill('4')
        self.page.get_by_label("", exact=True).first.click()
        # self.page.locator(LotInfoBlock.MEASURE_UNIT).click()
        self.page.locator(LotInfoBlock.MEASURE_UNIT_OPTION).click()
        self.page.locator(LotInfoBlock.DETAILED_LOT_DESCRIPTION).first.fill('dsecription')
        #self.page.locator("div:nth-child(9) > div > .MuiFormControl-root > .MuiInputBase-root > .MuiInputBase-input").fill('0500000000')
        self.page.locator(LotInfoBlock.COATUU).fill('0500000000')

    def point_map(self):
        self.page.get_by_role("button", name=LotInfoBlock.OPEN_MAP).click()
        self.page.locator("div").filter(has_text=re.compile(r"^\+− Leaflet \| © OpenStreetMap contributors$")).nth(1).click()

    def get_coordinates(self):
        # Locate the element that contains the coordinates
        coordinates_field = self.page.locator("div:nth-child(8) > div > .MuiFormControl-root > .MuiInputBase-root > .MuiInputBase-input")  # Replace with the actual selector

        # Get the value or text content from the coordinates field
        coordinates_value = coordinates_field.input_value()  # For input fields or text-based values
        # coordinates_value = coordinates_field.text_content()  # If it's a non-input element (like a div or span)

        return coordinates_value

    def upload_document(self):
        # Get path relative to project root
        base_path = Path(__file__).resolve().parent.parent.parent  # Adjust based on your structure
        document_path = base_path / "Emily_Playwright" / "utils" / "attachments" / "Test_PDF.pdf"

        if not document_path.exists():
            raise FileNotFoundError(f"Test document missing at: {document_path}")

        # Use the file path with Playwright
        file_input = self.page.locator(DocumentsBlock.DOCUMENT_UPLOAD)
        file_input.set_input_files(str(document_path))

    def publish(self):
        self.page.get_by_role("button", name=SubmitionBlock.PUBLISH).click()

    def save_draft(self):
        self.page.get_by_role("button", name=SubmitionBlock.SAVE_DRAFT).click()

    def edit_title(self):
        self.page.get_by_placeholder(BasicInfoBlock.AUCTION_TITLE).first.fill('AuctionEditedForDeletion')

    def save_changes(self):
        self.page.get_by_role("button", name=SubmitionBlock.SAVE_CHANGES).click()

    def get_previous_id(self):
        value = self.page.locator(BasicInfoBlock.PREVIOUS_AUCTION_ID)
        return value.input_value()

    def enable_discount(self):
        self.page.get_by_label(DetailLotDescriptionBlock.DISCOUNT_TOGGLE).check()
        self.page.locator(DetailLotDescriptionBlock.DISCOUNT_FIELD).fill("2.0")

    def get_discount_value(self):
        discount_input = self.page.locator(DetailLotDescriptionBlock.DISCOUNT_INPUT_VALUE)
        return discount_input.input_value()

    def add_registration_fee(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.REGISTRATION_FEE_OPTION).click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_other(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.OTHER_OPTION).click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_payment(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.PAYMENT_OPTION).click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_guarantee(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.GUARANTEE_OPTION).click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_registration_fee_usd(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.REGISTRATION_FEE_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="USD").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_other_usd(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.OTHER_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="USD").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_payment_usd(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.PAYMENT_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="USD").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_guarantee_usd(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.GUARANTEE_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="USD").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_registration_fee_eur(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.REGISTRATION_FEE_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="EUR").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_other_eur(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.OTHER_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="EUR").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_payment_eur(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.PAYMENT_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="EUR").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_guarantee_eur(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self.page.get_by_role("option", name=BankAccounts.GUARANTEE_OPTION).click()
        self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
        self.page.get_by_role("option", name="EUR").click()
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def add_bank_account(self, account_type, currency=None):
        """Adds a bank account with the given type and optional currency."""
        self.page.locator(BankAccounts.ADD_BANK_ACCOUNT).first.click()  # Click 'Add Bank Account'

        # Select bank account type
        self.page.get_by_label("", exact=True).nth(1).click()

        # Map account_type to the correct locator
        account_type_mapping = {
            BankAccounts.REGISTRATION_FEE_OPTION: BankAccounts.REGISTRATION_FEE_OPTION,
            BankAccounts.OTHER_OPTION: BankAccounts.OTHER_OPTION,
            BankAccounts.PAYMENT_OPTION: BankAccounts.PAYMENT_OPTION,
            BankAccounts.GUARANTEE_OPTION: BankAccounts.GUARANTEE_OPTION,
        }

        # Select the corresponding option
        if account_type in account_type_mapping:
            self.page.get_by_role("option", name=account_type_mapping[account_type]).click()
        else:
            raise ValueError(f"Invalid account type: {account_type}")

        # Select currency if provided
        if currency:
            self.page.locator(BankAccounts.CURRENCY_DROPDOWN).click()
            self.page.get_by_role("option", name=currency).click()

        # Click 'Fill from Profile' button
        self.page.locator(BankAccounts.FILL_FROM_PROFILE_BUTTON).click()

    def wait_for_upload_ready(self):
        """Waits until the upload document button is enabled (or any suitable condition)."""
        upload_button = self.page.locator(DocumentsBlock.DOCUMENT_UPLOAD)
        expect(upload_button).to_be_enabled(timeout=5000)

    def wait_for_draft_saved(self):
        """Waits at least 4 seconds, then ensures the user is redirected to 'my-auctions' page."""
        # Wait for 4 seconds to handle slow document uploads or backend delays
        self.page.wait_for_timeout(4000)

        # After the wait, ensure the URL redirects to the 'my-auctions' page
        self.page.wait_for_url("**/my-auctions", timeout=10000)

