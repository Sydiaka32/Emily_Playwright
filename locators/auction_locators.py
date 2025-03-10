class OrganiserBlock:
    #ORGANISER = 'label="Exact Label Text"'
    ORGANISER_OPTION = 'role=option[name="SdU"]'


class BasicInfoBlock:
    AUCTION_TYPE = 'text="Оберіть тип процедури"'
    BSE_OPTION = "Продаж на \"англійському аукціоні\""

    #TODO Add more procedures here

    AUCTION_TITLE = "Введіть назву"

    LOT_NUMBER = "Введіть номер лота"
    DESCRIPTION = "div:nth-child(2) > div > .MuiFormControl-root > .MuiInputBase-root > textarea"
    PREVIOUS_AUCTION_ID = 'input[placeholder="LSE000-UA-YYYYMMDD-00000"]'


class DetailLotDescriptionBlock:
    INITIAL_AMOUNT = "input[name=\"specificData\\.initialAmount\"]"
    MIN_STEP = ("div:nth-child(3) > .MuiPaper-root > div:nth-child(4) > div:nth-child(2) > div > "
                ".MuiFormControl-root > .MuiInputBase-root > .MuiInputBase-input")
    DISCOUNT_TOGGLE = "Знижка"
    DISCOUNT_FIELD = "//input[@name='specificData.discount']"
    DISCOUNT_INPUT_VALUE = 'input[name="specificData.discount"]'


class LotInfoBlock:
    CLASSIFIER = "Оберіть основний класифікатор"
    SELECT_CLASSIFIER = "18000000-9"
    CHECKBOX_CLASSIFIER = "checkbox"
    SUBMIT_CLASSIFIER = "Обрати"
    LOT_QUANTITY = "input[name=\"specificData\\.lots\\.0\\.quantity\"]"
    MEASURE_UNIT = "[id=\"mui-component-select-specificData\\.lots\\.0\\.measureUnit\"]"
    MEASURE_UNIT_OPTION = 'role=option[name="роботи"]'
    DETAILED_LOT_DESCRIPTION = "div:nth-child(4) > div > .MuiFormControl-root > .MuiInputBase-root > textarea"
    OPEN_MAP = "Показати карту"

    #CLICK_MAP = page.locator("div").filter(has_text=re.compile(r"^\+− Leaflet \| © OpenStreetMap contributors$")).nth(1)
    COATUU = "div:nth-child(8) > div > .MuiFormControl-root > .MuiInputBase-root > .MuiInputBase-input"


class BankAccounts:
    ADD_BANK_ACCOUNT = ("//div[.//h6[contains(.,'Додати рахунок')]]"
                        "/following-sibling::div//button[.//*[@data-testid='AddCircleOutlineIcon']]")
    FILL_FROM_PROFILE_BUTTON = "Заповнити реквізити з мого профілю"
    REGISTRATION_FEE_OPTION = "Реєстраційний внесок"


class DocumentsBlock:
    DOCUMENT_UPLOAD = 'input[type="file"]'


class SubmitionBlock:
    SAVE_DRAFT = "Зберегти чернетку"
    PUBLISH = "Опублікувати"
    SAVE_CHANGES = "Зберегти зміни"





