import re
from playwright.sync_api import Page
from locators.auction_locators import (OrganiserBlock, BasicInfoBlock, DetailLotDescriptionBlock,
                                                           LotInfoBlock, DocumentsBlock, SubmitionBlock, BankAccounts)
from pathlib import Path


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
        self.page.get_by_role("treeitem", name=LotInfoBlock.SELECT_CLASSIFIER).get_by_role(LotInfoBlock.CHECKBOX_CLASSIFIER).check()
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
        # Get the absolute path to the PlaywrightFramework directory
        base_path = Path(__file__).resolve().parent.parent  # Move up two levels to PlaywrightFramework
        file_path = base_path / "utils" / "attachments" / "Test_PDF.pdf"

        # Use the file path with Playwright
        file_input = self.page.query_selector(DocumentsBlock.DOCUMENT_UPLOAD)
        file_input.set_input_files(str(file_path))

    # def upload_document(self):
    #     file_input = self.page.query_selector(DocumentsBlock.DOCUMENT_UPLOAD)
    #     # Set the file to upload
    #     file_input.set_input_files(r"C:\Users\User\Desktop\Automation\Selenium\Selenium\PlaywrightFramework\utils"
    #                                r"\attachments\Test_PDF.pdf")

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

    def add_bank_account(self):
        self.page.locator(BankAccounts.ADD_BANK_ACCOUNT).first.click()

    def add_registration_fee(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self. page.get_by_role("option", name=BankAccounts.REGISTRATION_FEE_OPTION).click()
        self.page.get_by_role("button", name=BankAccounts.FILL_FROM_PROFILE_BUTTON).nth(1).click()

    def add_other(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self. page.get_by_role("option", name=BankAccounts.OTHER_OPTION).click()
        self.page.get_by_role("button", name=BankAccounts.FILL_FROM_PROFILE_BUTTON).nth(2).click()

    def add_payment(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self. page.get_by_role("option", name=BankAccounts.PAYMENT_OPTION).click()
        self.page.get_by_role("button", name=BankAccounts.FILL_FROM_PROFILE_BUTTON).nth(3).click()

    def add_guarantee(self):
        self.page.get_by_label("", exact=True).nth(1).click()
        self. page.get_by_role("option", name=BankAccounts.GUARANTEE_OPTION).click()
        self.page.get_by_role("button", name=BankAccounts.FILL_FROM_PROFILE_BUTTON).nth(4).click()


