# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    def calc(x, y):
        return str(int(x)+int(y))

    # Считать (в смысле, прочитать и запомнить) значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,"#num1")
    x = x_element.text
    # Считать (в смысле, прочитать и запомнить) значение для переменной y
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = y_element.text
    z = calc(x, y)


    select = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    select.select_by_value(str(z))
    # Или подойдет иной способ:
    # input1 = browser.find_element(By.CSS_SELECTOR, "select#dropdown")
    # input1.send_keys(z)


    # Нажать на кнопку Submit.
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_button.click()
    print("Значение атрибута равно: ", z)


finally:
    time.sleep(5)
    browser.quit()
