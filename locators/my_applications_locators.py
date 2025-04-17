class MyApplicationLocators:
    APPLICATION_CARD = "(//div[contains(@class, 'MuiPaper-elevation1')][1])[2]"
    APPLICATION_DETAILS = "//button[contains(@class, 'MuiButton-root') and normalize-space()='Переглянути заяву']"
    PROFILE_INFO = ("//h6[contains(@class, 'MuiTypography-subtitle1') and"
                    " normalize-space()='62 | Юридична особа - резидент | Aphrodite']")
    PRICE_INFO = "//h6[contains(@class, 'MuiTypography-subtitle1') and contains(normalize-space(), '500.00 грн')]"
    STATUS_INFO = "//h6[contains(@class, 'MuiTypography-subtitle1') and normalize-space()='Неопублікована заява']"









