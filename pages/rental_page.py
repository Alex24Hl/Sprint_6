import allure

from pages.base_page import BasePage
from locators.rental_locators import RentalPageUserDataLocators, RentalPageInfoLocators, OrderModalLocators
from data import Data

class RentalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем появления экрана "Для кого самокат"')
    def check_load_rental_page(self):
        self.wait(RentalPageUserDataLocators.RENTAL_PAGE_HEADER)

    @allure.step('Ожидаем появления экрана "Про аренду"')
    def check_load_scooter_page(self):
        self.wait(RentalPageUserDataLocators.RENTAL_SCOOTER_HEADER)

    @allure.step('Заполняем поле "Имя"')
    def set_name(self):
        self.send_keys(RentalPageUserDataLocators.USERNAME_INPUT, text=Data.TEST_USER_ONE['name'])

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self):
        self.send_keys(RentalPageUserDataLocators.SURNAME_INPUT, text=Data.TEST_USER_ONE['surname'])

    @allure.step('Заполняем поле "Адресс"')
    def set_adress(self):
        self.send_keys(RentalPageUserDataLocators.ADRESS_INPUT, text=Data.TEST_USER_ONE['adress'])

    @allure.step('Устанавливаем значение для поля "Станция метро"')
    def set_undeground_station(self):
        self.click(RentalPageUserDataLocators.UNDERGROUND_STATION_INPUT)
        self.click(RentalPageUserDataLocators.STATION_ROKOSSOVSKY_BOULEVARD)

    @allure.step('Заполняем поле "Адресc"')
    def set_number(self):
        self.send_keys(RentalPageUserDataLocators.PHONE_INPUT, text=Data.TEST_USER_ONE['number'])

    @allure.step('Устанавливаем дату в "Когда привезти самокат"')
    def set_date(self):
        self.click(RentalPageInfoLocators.DELIVERY_DATE_INPUT)
        self.click(RentalPageInfoLocators.DELIVERT_DATE)

    @allure.step('Устанавливаем значение для поля "Срок аренды"')
    def set_rental_period(self):
        self.click(RentalPageInfoLocators.RENTAL_PERIOD_INPUT)
        self.click(RentalPageInfoLocators.RENTAL_PERIOD)

    @allure.step('Выбираем значение для поля "Цвет скутера"')
    def set_scooter_color(self):
        self.click(RentalPageInfoLocators.SCOOTER_COLOR)

    @allure.step('Заполняем поле "Комментарий для курьера"')
    def set_comment(self):
        self.send_keys(RentalPageInfoLocators.COMMENT_INPUT, text=Data.TEST_USER_ONE['comment'])

    @allure.step('Выполняем клик по кнопке "Далее"')
    def click_next_button(self):
        self.click(RentalPageUserDataLocators.NEXT_BUTTON)

    @allure.step('Выполняем клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click(RentalPageInfoLocators.ORDER_BUTTON)

    @allure.step('Выполняем клик по кнопке "Да"')
    def click_yes_button(self):
        self.click(OrderModalLocators.YES_BUTTON)

    @allure.step('Выполняем клик по кнопке "Посмотреть статус"')
    def click_status_button(self):
        self.click(OrderModalLocators.CHECK_STATUS_BUTTON)
