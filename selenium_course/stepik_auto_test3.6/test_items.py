# Путь для запуска:
# pytest --language=es test_items.py
# pytest --language=es stepik_auto_test3.6/test_items.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# options = Options()
# language = "es"
# options.add_experimental_option('prefs', {'intl.accept_languages': language})
#
# @pytest.fixture(scope="function")
#
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


def test_presence_add_cart_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    wait = WebDriverWait(browser, 5)
    button_text = wait.until(
        ec.visibility_of_element_located((
            By.CSS_SELECTOR,
            "button.btn.btn-lg.btn-primary.btn-add-to-basket"
        ))
    ).text

    assert button_text == "Añadir al carrito", "Страница товара на сайте содержит кнопку добавления в корзину"
