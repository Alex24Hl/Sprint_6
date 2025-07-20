import allure
import pytest
import sys

sys.path.insert(1, "../pages")

from pages.main_page import MainPage
from data import QuestionsData

from urls import QA_SCOOTER_URL


class TestQuestions:

    @pytest.mark.parametrize('question', QuestionsData.QUESTIONS)

    @allure.step('Тест "Вопросы о важном"')
    def test_questions(self, driver, question):
        with allure.step('Инициализируем драйвер'):
            main_page = MainPage(driver)
        with allure.step('Шаг 1. Открываем сайт "https://qa-scooter.praktikum-services.ru/"'):
            main_page.open_url(QA_SCOOTER_URL)
            question_locator = question["question_locator"]
            answer_locator = question["answer_locator"]
            expected_text = question["expected_text"]
        with allure.step(f'Шаг 2. Скроллим до вопроса {question_locator}'):
            main_page.scroll(question_locator)
        with allure.step(f'Шаг 3. Кликаем по вопросу {question_locator}'):
            main_page.click(question_locator)
            with allure.step('Вопрос развернулся - экране появился ответ'):
                main_page.wait(answer_locator)
                actual_text = main_page.get_text(answer_locator)
                assert actual_text == expected_text, \
                    f"Текст ответа не совпадает. Ожидалось: '{expected_text}', получено: '{actual_text}'"
