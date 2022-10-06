# Фикстуры, возвращающие значение

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Путь для запуска из директории stepic_auto_tests_course:
# pytest -s -v selenium_course/Module3_4/test_fixture2.py


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser): # тестовый гость должен увидеть ссылку для входа
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        # тестовый гость должен увидеть ссылку на корзину на главной странице
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

