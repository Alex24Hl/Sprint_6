from selenium.webdriver.common.by import By

class HeaderLocators:
    HEADER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    FOOTER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']

class QuestionsLocators:
    HEADER_PRICING = (By.ID, "accordion__heading-0")
    ANSWER_PRICING = (By.XPATH, "//div[@id='accordion__panel-0']/p")

    HEADER_SEVERAL_SCOOTERS = (By.ID, "accordion__heading-1")
    ANSWER_SEVERAL_SCOOTERS = (By.XPATH, "//div[@id='accordion__panel-1']/p")

    HEADER_RENTAL_TIME = (By.ID, "accordion__heading-2")
    ANSWER_RENTAL_TIME = (By.XPATH, "//div[@id='accordion__panel-2']/p")

    HEADER_ORDER_TODAY = (By.ID, "accordion__heading-3")
    ANSWER_ORDER_TODAY = (By.XPATH, "//div[@id='accordion__panel-3']/p")

    HEADER_EXTEND_SCOOTER = (By.ID, 'accordion__heading-4')
    ANSWER_EXTEND_SCOOTER = (By.XPATH, "//div[@id='accordion__panel-4']/p")

    HEADER_CHARGING_WITH_SCOOTER = (By.ID, 'accordion__heading-5')
    ANSWER_CHARGING_WITH_SCOOTER = (By.XPATH, "//div[@id='accordion__panel-5']/p")

    HEADER_CANCEL_ORDER = (By.ID, 'accordion__heading-6')
    ANSWER_CANCEL_ORDER = (By.XPATH, "//div[@id='accordion__panel-6']/p")

    HEADER_TERRITORY = (By.ID, 'accordion__heading-7')
    ANSWER_TERRITORY = (By.XPATH, "//div[@id='accordion__panel-7']/p")
