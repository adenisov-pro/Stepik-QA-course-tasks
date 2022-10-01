from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("abc@mail.ru")

    # Чтобы руками не создавать файл, можно сделать это с помощью Python
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file


    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__)) # current_dir – текущая директория
    # В переменную file_name помещаем название нашего текстового файла
    file_name = "test.txt"
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    # Для загрузки файла на веб-странице используем метод send_keys.
    # Только теперь в качестве аргумента передаем путь к нужному файлу на диске
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    # time.sleep(10)

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
