from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("Bharath")
act_title=driver.title
exp_title="Facebook – log in or sign up"
if act_title==exp_title:
    print("Passed")
else:
    print("Failed")
    driver.quit()
