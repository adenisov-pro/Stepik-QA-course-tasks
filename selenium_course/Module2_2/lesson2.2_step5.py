from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")

# мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
# Делается это с помощью следующего скрипта:
# "return arguments[0].scrollIntoView(true);"
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(2)

button.click()
time.sleep(2)


browser.quit()
