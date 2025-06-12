import allure

import sys

sys.path.insert(1, "../pages")

from pages.main_page import MainPage
from locators.main_locators import QuestionsLocators


from urls import QA_SCOOTER_URL


class TestQuestions:

    def test_order_scooter(self, driver):
        with allure.step('Инициализируем драйвер'):
            main_page = MainPage(driver)
        with allure.step('Шаг 1. Открываем сайт "https://qa-scooter.praktikum-services.ru/"'):
            main_page.open_url(QA_SCOOTER_URL)
        with allure.step('Шаг 2. Скроллим до раздела "Вопросы о важном"'):
            main_page.scroll(QuestionsLocators.HEADER_SEVERAL_SCOOTERS_QUESTION)
        with allure.step('Шаг 3. Кликаем на вопрос "Сколько это стоит? И как оплатить?"'):
            main_page.click_pricing_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_pricing_question()
        with allure.step('Шаг 4. Кликаем на вопрос "Хочу сразу несколько самокатов! Так можно?"'):
            main_page.click_several_scooters_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_several_scooters_question()
        with allure.step('Шаг 5. Кликаем на вопрос "Как рассчитывается время аренды?"'):
            main_page.click_rental_time_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_rental_time_question()
        with allure.step('Шаг 6. Кликаем на вопрос "Можно ли заказать самокат прямо на сегодня?"'):
            main_page.click_order_today_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_order_today_question()
        with allure.step('Шаг 7. Кликаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"'):
            main_page.click_extend_scooter_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_order_today_question()
        with allure.step('Шаг 8. Кликаем на вопрос "Вы привозите зарядку вместе с самокатом?"'):
            main_page.click_charging_with_scooter_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_charging_with_scooter_question()
        with allure.step('Шаг 9. Кликаем на вопрос "Можно ли отменить заказ?"'):
            main_page.click_cancel_order_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_cancel_order_question()
        with allure.step('Шаг 10. Кликаем на вопрос "Я жизу за МКАДом, привезёте?"'):
            main_page.click_territory_question()
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.check_territory_question()
