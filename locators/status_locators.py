from selenium.webdriver.common.by import By


class StatusLocators:
    CHECK_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть" and contains(@class, "Button_Button__ra12g")]')

class LogoLocators:
    LOGO = (By.XPATH, '//img[@alt="Yandex"]')
