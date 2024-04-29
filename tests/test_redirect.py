import allure
from pages.questions_page import QuestionsPage
from conftest import driver
from data import Urls

class TestPageRedirect:

    @allure.title("Проверка, что при клике на логотип Яндекс происходит переход на Дзен")
    @allure.description("Тест проверяет, что при клике на логотип Яндекса в новой вкладке открывается страничка Дзена")
    def test_redirect_to_dzen_by_yandex_logo_click(self, driver):

        with allure.step("Инициировать браузер"):
            redirect_to_dzen_page = QuestionsPage(driver)

        with allure.step("Открыть страницу 'https://qa-scooter.praktikum-services.ru/'"):
            redirect_to_dzen_page.open_page(Urls.BASE_PAGE)

        with allure.step("Кликнуть на логотип Яндекса"):
            redirect_to_dzen_page.element_click(redirect_to_dzen_page.yandex_logo)

        with allure.step("Дождаться открытия окна Дзена"):
            redirect_to_dzen_page.new_window_created()

        with allure.step("Проверить, что открыта страница Дзен 'https://dzen.ru/?yredirect=true'"):
            assert redirect_to_dzen_page.get_url() == Urls.DZEN_PAGE

    @allure.title("Проверка, что при клике на логотип Самокат происходит переход на главную страницу")
    @allure.description("Тест проверяет, что при клике на логотип Самокат происходит возвращение на главную страницу сервиса")
    def test_redirect_to_question_page_by_scooter_logo_click(self, driver):

        with allure.step("Инициировать браузер"):
            redirect_to_question_page = QuestionsPage(driver)

        with allure.step("Открыть страницу 'https://qa-scooter.praktikum-services.ru/'"):
            redirect_to_question_page.open_page(Urls.BASE_PAGE)

        with allure.step("Перейти с главной страницы на страницу заказа самоката кликнув на кнопку 'Заказать'"):
            redirect_to_question_page.element_click(redirect_to_question_page.order_button_top)

        with allure.step("Кликнуть на логотип сервиса Самокат"):
            redirect_to_question_page.element_click(redirect_to_question_page.scooter_logo)

        with allure.step("Проверить, что вернулись на главную страницу 'https://qa-scooter.praktikum-services.ru/'"):
            assert redirect_to_question_page.get_url() == Urls.BASE_PAGE



