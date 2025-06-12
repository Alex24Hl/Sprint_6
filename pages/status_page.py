import allure

from base_page import BasePage
from  locators.status_locators import StatusLocators, LogoLocators


class StatusPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем появления экрана со статусом')
    def check_load_status_page(self):
        self.wait(StatusLocators.CHECK_STATUS_BUTTON)

    @allure.step('Выполянем клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.click(LogoLocators.LOGO)
