import allure
from pages.questions_page import QuestionsPage
from conftest import driver
from data import Urls
import pytest

class TestQuestionsAndAnswers:

    @pytest.mark.parametrize("question_number, expected_answer",
    [
        ('1', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ('2', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        ('3', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        ('4', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        ('5', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        ('6', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        ('7', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        ('8', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])

    @allure.title("Проверка, что при клике на вопрос в блоке 'Вопросы о важном' будет отображаться ответ")
    @allure.description("На странице проверяем, что в блоке 'Вопросы о важном' при клике на каждый вопрос есть ответ подсказка и этот ответ верный")
    def test_find_question_and_check_answer(self, driver, question_number, expected_answer):
        with allure.step("Инициировать браузер"):
            question_page = QuestionsPage(driver)

        with allure.step("Открываем страничку 'https://qa-scooter.praktikum-services.ru/' "):
            question_page.open_page(Urls.BASE_PAGE)

        with allure.step("Принять куки на страничке"):
            question_page.accept_cookie(question_page.ACCEPT_COOKIE_BUTTON)

        with allure.step("Проскроллить до раздела 'Вопросы о важном' "):
            question_page.scroll_to_questions(question_page.question_header)

        with allure.step("Подождать пока отобразится список вопросов "):
            question_page.wait_for_element_visibility(question_page.question_buttons, question_number)

        with allure.step("Кликнуть на вопрос из списка"):
            question_page.click_question(question_number)

        with allure.step("Подождать пока отобразится ответ на вопрос"):
            question_page.wait_for_element_visibility(question_page.question_answers, question_number)

        with allure.step("Получить значение ответа вопроса"):
            answer = question_page.get_answer(question_number)

        with allure.step("Проверить соответствие ответа ожидаемому"):
            assert answer == expected_answer

