import allure
from pages.order_page import ScooterOrderPage
from conftest import driver
from data import Urls

class TestOrderScooter:
    @allure.title("Проверка заказа самоката через кнопку заказа в хэдере страницы с подтверждением аренды")
    @allure.description("Тест проверяет возможность заказа самоката по кнопке в хедере страницы с последующим подтверждением аренды")
    def test_order_scooter_from_top_button_with_confirmation(self, driver):
        with allure.step("Инициировать браузер"):
            order_page = ScooterOrderPage(driver)

        with allure.step("Открыть страницу 'https://qa-scooter.praktikum-services.ru/'"):
            order_page.open_page(Urls.BASE_PAGE)

        with allure.step("Принять куки"):
            order_page.accept_cookie()

        with allure.step("Кликнуть на кнопку 'Заказать' в хедере страницы"):
            order_page.element_click(order_page.order_button_top)

        with allure.step("Проверить, что произошел переход на страницу заказа 'https://qa-scooter.praktikum-services.ru/order'"):
            assert driver.current_url == Urls.MAKE_ORDER_PAGE

        with allure.step("Ввести имя в поле Имя"):
            order_page.send_keys_in_input(order_page.name_input, 'Борис')

        with allure.step("Ввести фамилию в поле Фамилия"):
            order_page.send_keys_in_input(order_page.surname_input, 'Акулов')

        with allure.step("Ввести адрес доставки самоката"):
            order_page.send_keys_in_input(order_page.address_input, 'Москва Кремль')

        with allure.step("Кликнуть на поле ввода станции метро"):
            order_page.element_click(order_page.metro_station_input)

        with allure.step("Выбрать в списке станций метро Рокоссовская"):
            order_page.element_click(order_page.metro_station_dropdown_choose_rokossovskogo)

        with allure.step("Ввести номер телефона"):
            order_page.send_keys_in_input(order_page.phone_number_input, '79991234567')

        with allure.step("Кликнуть на кнопку 'Далее' "):
            order_page.element_click(order_page.go_on_button)

        with allure.step("Кликнуть на поле выбора даты доставки самоката"):
            order_page.element_click(order_page.when_scooter_arrive_input)

        with allure.step("Выбрать дату в выпадающем календаре"):
            order_page.element_click(order_page.choose_date_on_calendar)

        with allure.step("Кликнуть на поле срока аренды"):
            order_page.element_click(order_page.rent_time_dropdown_open)

        with allure.step("Выбрать время в выпадающем списке - сутки"):
            order_page.element_click(order_page.rent_time_dropdown_choose_time_one_day)

        with allure.step("Кликнуть кнопку 'Заказать'"):
            order_page.element_click(order_page.accept_order_button)

        with allure.step("Проверить, что отобразилось окно 'Хотите оформить заказ'"):
            assert order_page.wait_and_find_element(order_page.accept_order_window_header).is_displayed()

        with allure.step("Кликнуть кнопку подтверждения 'Да' в окне 'Хотите оформить заказ' "):
            order_page.element_click(order_page.order_confirm_button_in_window)

        with allure.step("Проверить, что отображается заголовок подтвержденного заказа в окне' "):
            assert order_page.wait_and_find_element(order_page.order_confirmation_header).is_displayed()

    @allure.title("Проверка заказа самоката через кнопку заказа в боттоме страницы с отклонением подтверждения аренды")
    @allure.description("Тест проверяет альтернативную возможность заказа самоката по кнопке в боттоме страницы с последующим отклонением подтверждения аренды и возвращением пользователя к анкете")
    def test_order_scooter_from_bottom_button_with_decline(self, driver):

        with allure.step("Инициировать браузер"):
            order_page = ScooterOrderPage(driver)

        with allure.step("Открыть страницу 'https://qa-scooter.praktikum-services.ru/'"):
            order_page.open_page(Urls.BASE_PAGE)

        with allure.step("Принять куки"):
            order_page.accept_cookie()

        with allure.step("Проскроллить до раздела с вопросами"):
            order_page.scroll_to_questions()

        with allure.step("Кликнуть на кнопку 'Заказать' в боттоме страницы"):
            order_page.element_click(order_page.order_button_bottom)

        with allure.step("Проверить, что произошел переход на страницу заказа 'https://qa-scooter.praktikum-services.ru/order'"):
            assert driver.current_url == Urls.MAKE_ORDER_PAGE

        with allure.step("Ввести имя в поле Имя"):
            order_page.send_keys_in_input(order_page.name_input, 'Анна ')

        with allure.step("Ввести фамилию в поле Фамилия"):
            order_page.send_keys_in_input(order_page.surname_input, 'Комарова')

        with allure.step("Ввести адрес доставки самоката"):
            order_page.send_keys_in_input(order_page.address_input, 'Москва Кремль')

        with allure.step("Кликнуть на поле ввода станции метро"):
            order_page.element_click(order_page.metro_station_input)

        with allure.step("Выбрать в списке станций метро Рокоссовская"):
            order_page.element_click(order_page.metro_station_dropdown_choose_rokossovskogo)

        with allure.step("Ввести номер телефона"):
            order_page.send_keys_in_input(order_page.phone_number_input, '79991234567')

        with allure.step("Кликнуть на кнопку 'Далее' "):
            order_page.element_click(order_page.go_on_button)

        with allure.step("Кликнуть на поле выбора даты доставки самоката"):
            order_page.element_click(order_page.when_scooter_arrive_input)

        with allure.step("Выбрать дату в выпадающем календаре"):
            order_page.element_click(order_page.choose_date_on_calendar)

        with allure.step("Кликнуть на поле срока аренды"):
            order_page.element_click(order_page.rent_time_dropdown_open)

        with allure.step("Выбрать время в выпадающем списке - сутки"):
            order_page.element_click(order_page.rent_time_dropdown_choose_time_one_day)

        with allure.step("Кликнуть кнопку 'Заказать'"):
            order_page.element_click(order_page.accept_order_button)

        with allure.step("Проверить, что отобразилось окно 'Хотите оформить заказ'"):
            assert order_page.wait_and_find_element(order_page.accept_order_window_header).is_displayed()

        with allure.step("Кликнуть кнопку подтверждения 'Нет' в окне 'Хотите оформить заказ' "):
            order_page.element_click(order_page.order_decline_button_in_window)

        with allure.step("Проверяем отображение кнопки 'Заказать' анкеты"):
            assert order_page.wait_and_find_element(order_page.accept_order_button).is_displayed()

