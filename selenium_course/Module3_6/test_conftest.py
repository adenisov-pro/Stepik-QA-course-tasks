from selenium.webdriver.common.by import By

# Путь для запуска из директории stepic_auto_tests_course:
# pytest -s -v  selenium_course/Module3_6/test_conftest.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser): # should see login link - должен увидеть ссылку для входа
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")