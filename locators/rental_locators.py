from selenium.webdriver.common.by import By


class RentalPageUserDataLocators:
    RENTAL_PAGE_HEADER = [By.XPATH, '//div[text()="Для кого самокат"]']
    RENTAL_SCOOTER_HEADER = [By.XPATH, '//div[text()="Про аренду"]']
    USERNAME_INPUT = [By.XPATH, '//input[@placeholder="* Имя"]']
    SURNAME_INPUT = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    ADRESS_INPUT = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    UNDERGROUND_STATION_INPUT = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    STATION_ROKOSSOVSKY_BOULEVARD = [By.XPATH, '//li[@data-value="1"]']
    PHONE_INPUT = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, '//button[text()="Далее"]']


class RentalPageInfoLocators:    
    DELIVERY_DATE_INPUT = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    DELIVERT_DATE = [By.XPATH, '//div[@aria-label="Choose понедельник, 16-е июня 2025 г."]']
    RENTAL_PERIOD_INPUT = [By.XPATH, '//div[text()="* Срок аренды"]']
    RENTAL_PERIOD = [By.XPATH, '//div[text()="двое суток"]']
    SCOOTER_COLOR = [By.ID, 'black']
    COMMENT_INPUT = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']"]

class OrderModalLocators:
    YES_BUTTON = [By.XPATH, '//button[text()="Да"]']
    INFORMATION_ABOUT_ORDER = [By.CLASS_NAME, 'Order_Text__2broi']
    CHECK_STATUS_BUTTON = [By.XPATH, '//button[text()="Посмотреть статус"]']
    ORDER_HEADERS = [By.XPATH, '//*[contains(., "Хотите оформить заказ?")]']
    ORDER_DONE = [By.XPATH, '//*[contains(., "Заказ оформлен")]']

