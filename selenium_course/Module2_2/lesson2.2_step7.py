from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')
# element.send_keys(file_path)
print(os.path.abspath(__file__)) # Путь до файла lesson2.2_step7.py

print(os.path.abspath(os.path.dirname(__file__))) # покажет вам дирректорию (папку), в которой у вас лежит ваш исполняемый код

print(current_dir) # покажет вам дирректорию (папку), в которой у вас лежит ваш исполняемый код

print(file_path) # путь до вашего файла который вы хотите загрузить


# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# link = "http://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome()
# browser.get(link)
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_name = "file.txt"
# file_path = os.path.join(current_dir, file_name)
# element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
# element.send_keys(file_path)