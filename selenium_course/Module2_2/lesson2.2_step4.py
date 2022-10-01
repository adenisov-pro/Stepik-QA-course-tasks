# Метод execute_script синхронно выполняет JavaScript в текущем окне/фрейме
from selenium import webdriver
import time

# создать объект webdriver
driver = webdriver.Chrome()

# получить geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# написать сценарий (script)
script = "alert('Alert via selenium')"  # Оповещение через Selenium

# сгенерируйте оповещение с помощью javascript
driver.execute_script(script)
time.sleep(5)

driver.quit()
