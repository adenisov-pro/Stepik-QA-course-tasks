# Путь для запуска
# pytest -s -v --browser_name=firefox selenium_course/Module3_6/test_file5.py


from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")