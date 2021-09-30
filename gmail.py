from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://mail.google.com")
driver.forward()
print(driver.current_url)
