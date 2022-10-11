from selenium import webdriver

# Путь для запуска
# pytest -s -v selenium_course/Module3_6/test_firefox.py

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://stepik.org/lesson/25969/step/8")
driver.quit()