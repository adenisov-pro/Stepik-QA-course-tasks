# Явные ожидания (Explicit Waits)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# создать объект webdriver
browser = webdriver.Chrome()

# Открываем сайт по указанной ссылке
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:

    # Ожидаем, когда цена дома уменьшится до $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100"))

    # Нажать на кнопку "Book"
    button = browser.find_element(By.CSS_SELECTOR, "button#book.btn.btn-primary")
    button.click()


    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Считать (в смысле, прочитать и запомнить) значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,"span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    input_field.send_keys(y)
    # time.sleep(1)

    # Нажать кнопку Submit
    # говорим Selenium проверять в течение 1 секунды, пока кнопка не станет кликабельной
    button1 = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#solve.btn.btn-primary")))
    # Проскроллим страницу вниз.
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    time.sleep(5)


    print("Тест пройден")



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
