from selenium.webdriver.common.by import By

# Путь для запуска:
# pytest -v --tb=line --reruns 1 selenium_course/Module3_6/test_rerun.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")