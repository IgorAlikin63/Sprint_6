from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from data import Urls

class BasePageScooter:

    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    order_button_top = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')

    @allure.step("Инициировать драйвер")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть урл")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости элемента блок вопросов")
    def wait_for_element_visibility(self, locator, question_number, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator[question_number]))

    @allure.step("Подождать пока отобразится элемент")
    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть на элемент")
    def element_click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Найти кнопку и кликнуть")
    def accept_cookie(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step("Проскроллить до заголовка блока вопросов")
    def scroll_to_questions(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.wait_and_find_element(locator))
    @allure.step("Получить текущий урл страницы")
    def get_url(self):
        return self.driver.current_url

    @allure.step("Дождаться открытия второго окна Дзена")
    def new_window_created(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == Urls.DZEN_PAGE)


