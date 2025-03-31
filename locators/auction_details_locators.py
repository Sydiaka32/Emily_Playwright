class AuctionDetailsLocators:
    DISCOUNT_VALUE = ('//div[contains(@class, "MuiGrid-container") and .//h6[contains(text(), '
                      '"Розмір знижки від попереднього аукціону")]]/div[contains(@class, "MuiGrid-grid-md-true")]/h6')
    DETAIL_INFO_ACORDEON = "Детальна інформація"
    PREVIOUS_AUCTION_ID = ('//div[contains(@class, "MuiGrid-container") and '
                           './/h6[contains(text(), "Ідентифікатор попереднього аукціону")]]'
                           '/div[contains(@class, "MuiGrid-grid-md-true")]//a')

    PARTICIPATE_BTN = "Взяти участь"
    PROFILE_SELECT = "Не визначено"
    PRICE_FIELD = "Не визначено"
    CONTINUE_BTN = "Продовжити"
    PUBLISH_BTN = "Опублікувати"








