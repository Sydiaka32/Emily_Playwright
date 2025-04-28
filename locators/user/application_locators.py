class ApplicationLocators:
    SEARCH_FIELD = '//*[@id=":rg:"]'
    PROFILE_SELECT = ("//div[@role='combobox' and contains(@class, 'MuiSelect-select') "
                       "and contains(@class, 'MuiInputBase-input') and .//div[contains(text(), 'Не визначено')]]")
    APHRODITE_OPTION = "//li[@data-value='62']"
    PRICE_FIELD = "//input[@type='text' and @placeholder='Не визначено' and contains(@class, 'MuiOutlinedInput-input')]"
    CONTINUE_BUTTON = "//button[@type='button' and contains(@class, 'MuiButton-containedPrimary') and text()='Продовжити']"
    PRIVASY_POLISY_CHECK = "//div[contains(@class,'MuiFormControl-root')]//input[@type='checkbox']"
    REGULATIONS_CHECK = "//div[contains(@class,'MuiFormControl-root')]//input[@type='checkbox']"
    SAVE_DRAFT_BUTTON = ("//button[contains(@class, 'MuiButton-outlined') and contains(@class, 'MuiButton-colorPrimary') "
                         "and normalize-space()='Зберегти чернетку']")









