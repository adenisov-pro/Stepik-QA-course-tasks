# Классические фикстуры (fixtures)

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

# Путь для запуска из директории stepic_auto_tests_course:
# pytest -s selenium_course/Module3_4/test_fixture1.py

class TestMainPage1(): # Тестовая Главная страница1

    @classmethod
    def setup_class(self): # установочный класс
        print("\nstart browser for test suite..")  # запустите браузер для набора тестов
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self): # демонтаж_класса
        print("quit browser for test suite..") # закройте браузер для набора тестов
        self.browser.quit()

    def test_guest_should_see_login_link(self): # тестовый гость должен увидеть ссылку для входа
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        # тестовый гость должен увидеть ссылку на корзину на главной странице
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():  # Тестовая Главная страница2

    def setup_method(self): #метод настройки
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self): # метод демонтажа
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self): # тестовый гость должен увидеть ссылку для входа
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        # тестовый гость должен увидеть ссылку на корзину на главной странице
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
