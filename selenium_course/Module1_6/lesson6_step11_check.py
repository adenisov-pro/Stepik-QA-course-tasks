from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    first_name.send_keys("first name")

    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    last_name.send_keys("last name")

    email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    email.send_keys("email")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
