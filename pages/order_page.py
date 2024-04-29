from pages.base_page import BasePageScooter
from selenium.webdriver.common.by import By
import allure

class ScooterOrderPage(BasePageScooter):

    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    order_button_bottom = (By.XPATH, './/button[contains(@class,"Button_Button__ra12g Button_UltraBig__UU3Lp")][text()="Заказать"]')
    question_header = (By.XPATH, "//div[text()='Вопросы о важном']")
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_station_dropdown_choose_rokossovskogo = (By.XPATH, "//button[@value='1']")
    phone_number_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    go_on_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Далее']")
    when_scooter_arrive_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    choose_date_on_calendar = (By.XPATH, "//div[@aria-label='Choose понедельник, 1-е апреля 2024 г.']")
    rent_time_dropdown_open = (By.XPATH, "//div[text()='* Срок аренды']")
    rent_time_dropdown_choose_time_one_day = (By.XPATH, "//div[@class='Dropdown-option' and text() = 'сутки']")
    accept_order_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']")
    accept_order_window_header = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    order_confirm_button_in_window = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    order_decline_button_in_window = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i' and text()='Нет']")
    order_confirmation_header = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")

    @allure.step("Найти инпут, отправить в него значение")
    def send_keys_in_input(self, locator, text):
        input_element = self.wait_and_find_element(locator)
        input_element.send_keys(text)

