from pages.base_page import BasePageScooter
from selenium.webdriver.common.by import By
import allure

class QuestionsPage(BasePageScooter):

    question_header = (By.XPATH, "//div[text()='Вопросы о важном']")
    ACCEPT_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    question_buttons = {
        '1': (By.ID, 'accordion__heading-0'),
        '2': (By.ID, 'accordion__heading-1'),
        '3': (By.ID, 'accordion__heading-2'),
        '4': (By.ID, 'accordion__heading-3'),
        '5': (By.ID, 'accordion__heading-4'),
        '6': (By.ID, 'accordion__heading-5'),
        '7': (By.ID, 'accordion__heading-6'),
        '8': (By.ID, 'accordion__heading-7')
    }

    question_answers = {
        '1': (By.XPATH, '(//p)[1]'),
        '2': (By.XPATH, '(//p)[2]'),
        '3': (By.XPATH, '(//p)[3]'),
        '4': (By.XPATH, '(//p)[4]'),
        '5': (By.XPATH, '(//p)[5]'),
        '6': (By.XPATH, '(//p)[6]'),
        '7': (By.XPATH, '(//p)[7]'),
        '8': (By.XPATH, '(//p)[8]')
    }



    @allure.step("Кликнуть на вопрос в блоке вопросов и ответов")
    def click_question(self, question_number):
        question_button_locator = self.question_buttons.get(question_number)
        self.element_click(question_button_locator)

    @allure.step("Получить значение ответа на вопрос в блоке вопросов и ответов")
    def get_answer(self, question_number):
        answer_locator = self.question_answers.get(question_number)
        answer = self.wait_and_find_element(answer_locator)
        return answer.text


