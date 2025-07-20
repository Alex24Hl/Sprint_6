import allure
import pytest

import sys

sys.path.insert(1, "../pages")

from pages.main_page import MainPage
from pages.rental_page import RentalPage
from pages.status_page import StatusPage
from pages.yandex_page import YandexPage

from locators.main_locators import HeaderLocators
from data import Data

from urls import QA_SCOOTER_URL


class TestOrderScooter:

    @pytest.mark.parametrize('header_order_button, user',
                             [(HeaderLocators.HEADER_ORDER_BUTTON, Data.TEST_USER_ONE),
                              (HeaderLocators.FOOTER_ORDER_BUTTON, Data.TEST_USER_TWO)])

    @allure.title('Тест "Заказ самоката"')
    def test_order_scooter(self, driver, header_order_button, user):
        with allure.step('Инициализируем драйвер'):
            main_page = MainPage(driver)
        with allure.step('Шаг 1. Открываем сайт "https://qa-scooter.praktikum-services.ru/"'):
            main_page.open_url(QA_SCOOTER_URL)
            with allure.step('На экране отображается кнопка "Заказать" в хедере сайта'):
                main_page.check_order_button_in_header()
        with allure.step('Шаг 2. Делаем клик по кнопке "Заказать"'):
            main_page.click_order_button_in_header()
            with allure.step('На экране появилось окно "Для кого самокат"'):
                rental_page = RentalPage(driver)
                rental_page.check_load_rental_page()
        with allure.step('Шаг 3. Заполняем поля:'):
            with allure.step('Имя'):
                rental_page.set_name()
            with allure.step('Фамилия'):
                rental_page.set_surname()
            with allure.step('Адрес: куда привезти заказ'):
                rental_page.set_adress()
            with allure.step('Станция метро'):
                rental_page.set_undeground_station()
            with allure.step('Телефон: на него позвонит курьер'):
                rental_page.set_number()
        with allure.step('Шаг 4. Кликаем на кнопку "Далее"'):
            rental_page.click_next_button()
            with allure.step('На экране появился хедер "Про аренду"'):
                rental_page.check_load_scooter_page()
        with allure.step('Шаг 5. Заполняем поля:'):
            with allure.step('Когда привезти самокат'):
                rental_page.set_date()
            with allure.step('Срок аренды'):
                rental_page.set_rental_period()
            with allure.step('Цвет самоката'):
                rental_page.set_scooter_color()
            with allure.step('Комментарий для курьера'):
                rental_page.set_comment()
        with allure.step('Шаг 6. Кликаем на кнопку "Заказать"'):
            rental_page.click_order_button()
            with allure.step('На экране появился окно "Хотите оформить заказ?"'):
                rental_page.check_order_window()
        with allure.step('Шаг 7. Кликаем на кнопку "Да"'):
            rental_page.click_yes_button()
            with allure.step('На экране появилось окно с заказом и кнопкой "Посмотреть статус"'):
                rental_page.check_order_status()
        with allure.step('Шаг 8. Кликаем на кнопку "Посмотреть статус"'):
            rental_page.click_status_button()
            with allure.step('Открылась страница проверки статуса заказа'):
                status_page = StatusPage(driver)
                status_page.check_load_status_page()
        with allure.step('Шаг 9. Кликаем по логотипу "Яндекс"'):
            status_page.click_yandex_logo()
            with allure.step('Осуществился редирект на экран "Яндекс.Дзен"'):
                status_page.switch_window()
                yandex_page = YandexPage(driver)
                yandex_page.check_load_dzen_page()
