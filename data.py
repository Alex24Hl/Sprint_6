from locators.main_locators import QuestionsLocators

class Data:

    TEST_USER_ONE = {'name': 'Тест', 
                     'surname': 'Тестович',
                     'adress': 'Москва, Открытое шоссе, 5', 
                     'number': '89006321473',
                     'comment': 'Привезите, пожалуйста, самокат к 10:00 утра'}

    TEST_USER_TWO = {'name': 'СуперТест',
                     'surname': 'СуперТестович',
                     'adress': 'Москва, Открытое шоссе, 5',
                     'number': '89006321473',
                     'comment': 'Привезите, пожалуйста, самокат к 12:00 утра'}

class QuestionsData:
    QUESTIONS = [
        {
            "question_locator": QuestionsLocators.HEADER_PRICING,
            "answer_locator": QuestionsLocators.ANSWER_PRICING,
            "expected_text": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        },
        {
            "question_locator": QuestionsLocators.HEADER_SEVERAL_SCOOTERS,
            "answer_locator": QuestionsLocators.ANSWER_SEVERAL_SCOOTERS,
            "expected_text": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                             "можете просто сделать несколько заказов — один за другим."
        },
        {
            "question_locator": QuestionsLocators.HEADER_RENTAL_TIME,
            "answer_locator": QuestionsLocators.ANSWER_RENTAL_TIME,
            "expected_text": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                             "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                             "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        },
        {
            "question_locator": QuestionsLocators.HEADER_ORDER_TODAY,
            "answer_locator": QuestionsLocators.ANSWER_ORDER_TODAY,
            "expected_text": 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        },
        {
            "question_locator": QuestionsLocators.HEADER_EXTEND_SCOOTER,
            "answer_locator": QuestionsLocators.ANSWER_EXTEND_SCOOTER,
            "expected_text": 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                             'по красивому номеру 1010.'
        },
        {
            "question_locator": QuestionsLocators.HEADER_CHARGING_WITH_SCOOTER,
            "answer_locator": QuestionsLocators.ANSWER_CHARGING_WITH_SCOOTER,
            "expected_text": 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже '
                             'если будете кататься без передышек и во сне. Зарядка не понадобится.'
        },
        {
            "question_locator": QuestionsLocators.HEADER_CANCEL_ORDER,
            "answer_locator": QuestionsLocators.ANSWER_CANCEL_ORDER,
            "expected_text": 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                             'Все же свои.'
        },
        {
            "question_locator": QuestionsLocators.HEADER_TERRITORY,
            "answer_locator": QuestionsLocators.ANSWER_TERRITORY,
            "expected_text": 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        }
    ]
