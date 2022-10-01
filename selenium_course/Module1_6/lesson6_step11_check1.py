from cgitb import text
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
# Ваш код, который заполняет обязательные поля
name = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>.first").send_keys('My name is')
LastName = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>.second").send_keys('My last name is')
email = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>.third").send_keys('MyMail@gmail.com')


# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
print=(welcome_text_elt)

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()