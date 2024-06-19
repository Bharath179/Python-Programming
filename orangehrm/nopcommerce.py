from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo ThinkpadX1 Carbon Laptop")
driver.find_element(By.XPATH,"//button[text()='Search']").click()
driver.close()