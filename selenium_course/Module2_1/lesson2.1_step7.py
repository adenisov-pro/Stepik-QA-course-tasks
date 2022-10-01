import time
import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать (в смысле, прочитать и запомнить) значение атрибута valuex
    chest = browser.find_element(By.CSS_SELECTOR, "#treasure")
    chest_valuex = chest.get_attribute("valuex")
    x = chest_valuex
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "input[type='text']")
    input1.send_keys(y)


    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()


    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()


    # Нажать на кнопку Submit.
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_button.click()
    print("Значение атрибута равно: ", x)


finally:
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла