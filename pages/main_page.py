import allure


from pages.base_page import BasePage
from locators.main_locators import HeaderLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления кнопки "Заказать" в хедере')
    def check_order_button_in_header(self):
        self.wait(HeaderLocators.HEADER_ORDER_BUTTON)
    
    @allure.step('Осуществляем клик по кнопке "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.click(HeaderLocators.HEADER_ORDER_BUTTON)

