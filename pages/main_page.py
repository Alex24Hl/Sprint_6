import allure

from pages.base_page import BasePage
from locators.main_locators import HeaderLocators, QuestionsLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание появления кнопки "Заказать" в хедере')
    def check_order_button_in_header(self):
        self.wait(HeaderLocators.HEADER_ORDER_BUTTON)
    
    @allure.step('Осуществляем клик по кнопке "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.click(HeaderLocators.HEADER_ORDER_BUTTON)

    @allure.step('Осуществляем клик по вопросу "Сколько это стоит?"')
    def click_pricing_question(self):
        self.scroll(QuestionsLocators.HEADER_PRICING_QUESTION)
        self.click(QuestionsLocators.HEADER_PRICING_QUESTION)

    @allure.step('Ожидаем появление текста под заголовком "Сколько это стоит?"')
    def check_pricing_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_PRICING_QUESTION).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Сколько это стоит?' не найден")

    @allure.step('Осуществляем клик по вопросу "Хочу сразу несколько самокатов!"')
    def click_several_scooters_question(self):
        self.scroll(QuestionsLocators.HEADER_SEVERAL_SCOOTERS_QUESTION)
        self.click(QuestionsLocators.HEADER_SEVERAL_SCOOTERS_QUESTION)

    @allure.step('Ожидаем появление текста под заголовком "Хочу сразу несколько самокатов!"')
    def check_several_scooters_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_SEVERAL_SCOOTERS_QUESTION).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Хочу сразу несколько самокатов!' не найден")

    @allure.step('Осуществляем клик по вопросу "Как рассчитывается время аренды?"')
    def click_rental_time_question(self):
        self.scroll(QuestionsLocators.HEADER_RENTAL_TIME_QUESTION)
        self.click(QuestionsLocators.HEADER_RENTAL_TIME_QUESTION)

    @allure.step('Ожидаем появление текста под заголовком "Как рассчитывается время аренды?"')
    def check_rental_time_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_RENTAL_TIME_QUESTION).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Как рассчитывается время аренды?' не найден")

    @allure.step('Осуществляем клик по вопросу "Можно ли заказать самокат прямо на сегодня?"')
    def click_order_today_question(self):
        self.scroll(QuestionsLocators.HEADER_ORDER_TODAY)
        self.click(QuestionsLocators.HEADER_ORDER_TODAY)

    @allure.step('Ожидаем появление текста под заголовком "Можно ли заказать самокат прямо на сегодня?"')
    def check_order_today_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_ORDER_TODAY).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Можно ли заказать самокат прямо на сегодня?' не найден")

    @allure.step('Осуществляем клик по вопросу "Можно ли продлить заказ или вернуть самокат раньше?"')
    def click_extend_scooter_question(self):
        self.scroll(QuestionsLocators.HEADER_EXTEND_SCOOTER)
        self.click(QuestionsLocators.HEADER_EXTEND_SCOOTER)

    @allure.step('Ожидаем появление текста под заголовком "Можно ли продлить заказ или вернуть самокат раньше?"')
    def check_extend_scooter_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_EXTEND_SCOOTER).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Можно ли продлить заказ или вернуть самокат раньше' не найден")

    @allure.step('Осуществляем клик по вопросу "Вы привозите зарядку вместе с самокатом?"')
    def click_charging_with_scooter_question(self):
        self.scroll(QuestionsLocators.HEADER_CHARGING_WITH_SCOOTER)
        self.click(QuestionsLocators.HEADER_CHARGING_WITH_SCOOTER)

    @allure.step('Ожидаем появление текста под заголовком "Вы привозите зарядку вместе с самокатом?"')
    def check_charging_with_scooter_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_CHARGING_WITH_SCOOTER).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Вы привозите зарядку вместе с самокатом?' не найден")

    @allure.step('Осуществляем клик по вопросу "Можно ли отменить заказ?"')
    def click_cancel_order_question(self):
        self.scroll(QuestionsLocators.HEADER_CANCEL_ORDER)
        self.click(QuestionsLocators.HEADER_CANCEL_ORDER)

    @allure.step('Ожидаем появление текста под заголовком "Можно ли отменить заказ?"')
    def check_cancel_order_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_CANCEL_ORDER).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Можно ли отменить заказ?' не найден")

    @allure.step('Осуществляем клик по вопросу "Я живу за МКАДом, привезёте?"')
    def click_territory_question(self):
        self.scroll(QuestionsLocators.HEADER_TERRITORY)
        self.click(QuestionsLocators.HEADER_TERRITORY)

    @allure.step('Ожидаем появление текста под заголовком "Я живу за МКАДом, привезёте?"')
    def check_territory_question(self):
        try:
            answer = self.wait(QuestionsLocators.ANSWER_TERRITORY).text
            return answer
        except Exception:
            raise Exception("Текст под заголовком 'Я живу за МКАДом, привезёте?' не найден")
