from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.ID, "gsc-i-id2")

# send keys
element.send_keys("Arrays")

# submit contents - отправить содержимое
element.submit()
driver.quit()
