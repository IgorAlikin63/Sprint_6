from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePageScooter:

    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    scooter_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    yandex_logo = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    order_button_top = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element_visibility(self, locator, question_number, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator[question_number]))

    def wait_and_find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    def element_click(self, locator):
        self.driver.find_element(*locator).click()

    def accept_cookie(self):
        button = self.wait_and_find_element(self.ACCEPT_COOKIE_BUTTON)
        button.click()



