# Путь для запуска из директории stepic_auto_tests_course:
# pytest -s -v selenium_course/Module3_6/test_task4.py

import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # Применяем неявные ожидания
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

data = []

@pytest.mark.parametrize(
    'address',
    [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
)
def test_solving_the_problem(browser, address):
    link = f"https://stepik.org/lesson/{address}/step/1/"
    browser.get(link)

    # ищем textarea (текстовая область)
    answer = str(math.log(int(time.time())))

    text_field = browser.find_element(By.CSS_SELECTOR, "div.quiz-component.ember-view textarea")
    text_field.send_keys(answer)

    # button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    # button.click()

    # Нажмем button с явным ожиданием
    wait = WebDriverWait(browser, 5)
    button = wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

    # находим класс сообщения текст его присваиваем переменной element
    wait = WebDriverWait(browser, 5)
    message_text = wait.until(
        ec.visibility_of_element_located((
            By.CSS_SELECTOR,
            "div.smart-hints.ember-view.lesson__hint p"
        ))
    ).text

    if message_text != "Correct!":
        data.append(message_text)

    # print('\n\n RESULT =>', "".join(data))

    # Если хотим увидеть упавшие тесты и вручную "доставать" из них
    # кусочки фраз, то используем assert

    assert message_text == "Correct!", "текст в опциональном фидбеке не совпадает с 'Correct!'"
