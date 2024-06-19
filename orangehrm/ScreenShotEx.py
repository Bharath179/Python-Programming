from selenium import webdriver
import os

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.google.com")
driver.maximize_window()
#driver.save_screenshot(os.getcwd()+"\\google.png")
driver.get_screenshot_as_file(os.getcwd()+"\\google.png")
driver.quit()