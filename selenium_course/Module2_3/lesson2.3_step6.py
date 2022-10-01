from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# создать объект webdriver
browser = webdriver.Chrome()

# Открываем сайт по указанной ссылке
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    # Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "div.container>button.trollface.btn.btn-primary")
    button.click()
    # time.sleep(5)

    # Узнаем имя новой вкладки
    new_window = browser.window_handles[1]
    # Переключаемся на новую вкладку
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать (в смысле, прочитать и запомнить) значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
    x = x_element.text
    y = calc(x)
    # Ввести ответ в текстовое поле

    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_field.send_keys(y)

    # Нажать кнопку Submit
    button1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button1.click()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
