import time
import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать (в смысле, прочитать и запомнить) значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    # Проскроллим страницу вниз.
    # Делается это с помощью следующего скрипта:
    # "return arguments[0].scrollIntoView(true);"
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    # Ввести ответ в текстовое поле
    input1.send_keys(y)


    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()


    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()


    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    time.sleep(2)
    button.click()
    time.sleep(2)
    print("Значение атрибута равно: ", x)


finally:
    time.sleep(1)
    browser.quit()

# не забываем оставить пустую строку в конце файла