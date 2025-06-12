from selenium.webdriver.common.by import By

class HeaderLocators:
    HEADER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    FOOTER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']

class QuestionsLocators:
    HEADER_FAQ = [By.XPATH, '//div[@class="Home_SubHeader__zwi_E"]']

    HEADER_PRICING_QUESTION = [By.ID, 'accordion__heading-0']
    ANSWER_PRICING_QUESTION = [By.XPATH, '//*[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]']

    HEADER_SEVERAL_SCOOTERS_QUESTION = [By.ID, 'accordion__heading-1']
    ANSWER_SEVERAL_SCOOTERS_QUESTION = [By.XPATH, '//*[contains(., "один заказ — один самока")]']

    HEADER_RENTAL_TIME_QUESTION = [By.ID, 'accordion__heading-2']
    ANSWER_RENTAL_TIME_QUESTION = [By.XPATH, '//*[contains(., "времени аренды начинается")]']

    HEADER_ORDER_TODAY = [By.ID, 'accordion__heading-3']
    ANSWER_ORDER_TODAY = [By.XPATH, '//*[contains(., "завтрашнего дня")]']

    HEADER_EXTEND_SCOOTER = [By.ID, 'accordion__heading-4']
    ANSWER_EXTEND_SCOOTER = [By.XPATH, '//*[contains(., "красивому номеру")]']

    HEADER_CHARGING_WITH_SCOOTER = [By.ID, 'accordion__heading-5']
    ANSWER_CHARGING_WITH_SCOOTER = [By.XPATH, '//*[contains(., "полной зарядкой")]']

    HEADER_CANCEL_ORDER = [By.ID, 'accordion__heading-6']
    ANSWER_CANCEL_ORDER = [By.XPATH, '//*[contains(., "Штрафа")]']

    HEADER_TERRITORY = [By.ID, 'accordion__heading-7']
    ANSWER_TERRITORY = [By.XPATH, '//*[contains(., "Московской области")]']
