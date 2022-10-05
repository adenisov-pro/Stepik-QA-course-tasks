import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestForm(unittest.TestCase):

    def test_form1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)


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

        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


        time.sleep(2)
        browser.quit()



    def test_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

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

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(2)
        browser.quit()

if __name__ == "__main__":
    unittest.main()

