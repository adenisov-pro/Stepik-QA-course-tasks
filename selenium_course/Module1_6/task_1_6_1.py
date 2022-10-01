from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
time.sleep(3)

browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(3)

button = browser.find_element(By.ID, "submit_button")

time.sleep(3)
# После выполнения всех действий мы должны не забыть закрыть окно браузера
browser.quit()