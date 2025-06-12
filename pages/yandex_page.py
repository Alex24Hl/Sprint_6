import allure

from base_page import BasePage

from locators.yandex_locators import YandexLocators


class YandexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем появления страницы "Яндекс.Дзен"')
    def check_load_dzen_page(self):
        self.wait(YandexLocators.YANDEX_FIND_BUTTON)
