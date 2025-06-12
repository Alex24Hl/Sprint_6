import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем сайт')
    def open_url(self, url):
        self.driver.get(url)
    
    @allure.step('Метод выполняющий ожидание элемента')
    def wait(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Метод выполняющий клик по элементу')
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Метод передаёт значение в поле')
    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step('Метод скроллит до элемента')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
