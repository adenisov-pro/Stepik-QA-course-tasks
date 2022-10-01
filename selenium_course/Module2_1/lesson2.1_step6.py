from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, "peopleRule")
# Считать (в смысле, прочитать и запомнить) значение атрибута checked
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
# Мы можем написать проверку другим способом, сравнив строки:
# assert people_checked == "true", "People radio is not selected by default"

browser.quit()

# Если атрибута нет, то метод get_attribute вернёт значение None.
# Применим метод get_attribute ко второму radiobutton, и убедимся, что атрибут отсутствует.
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots radio: ", robots_checked)
assert robots_checked is None

browser.quit()

