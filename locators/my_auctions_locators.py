class MyAuctionsLocators:
    CARD_TITLE = '(//div[contains(@class, "MuiGrid-container")]//h4)[1]'
    CARD_PROCEDURE = '(//div[contains(@class, "MuiGrid-container")]//h5[contains(@class, "MuiTypography-h5")])[1]'
    CARD_STATUS = '(//div[contains(@class, "MuiGrid-container")]//p)[1]'
    AUCTION_CARD = '(//div[contains(@class, "MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-isbt42")])[2]'
    MORE_OPTIONS = "//button[.//*[@data-testid='MoreVertIcon']]"
    EDIT_OPTION = "Редагувати"
    DELETE_OPTION = "Видалити"
    PUBLISH_OPTION = "Опублікувати"
    DETAILS_BUTTON = "Детальніше"
    PUBLISHED_TAB = "Опубліковані"

    # Published
    AUCTION_CARD_PUBLISHED = '(//*[@id="tabpanel-/my-auctions"]/div/div[2]/div/div)[1]'
    PUBLISHED_CARD_TITLE = "Auction"
    PUBLISHED_CARD_PROCEDURE = "Продаж на англійському аукціоні"
    PUBLISHED_CARD_STATUS = "Прийняття заяв на участь"

    COPY = "Створити копію"
    PUBLISH_COPY_BASED = "Створити копію процедури на основі існуючої"
    ORDER_NUMBER_FIELD = "Черговість лоту"
    SUBMIT_POPUP = "ТАК"







