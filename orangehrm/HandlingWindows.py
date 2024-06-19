import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#windowid=driver.current_window_handle
#print(windowid)
time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIds=driver.window_handles
#parentWIds=windowIds[0]
#childWIds=windowIds[1]
#print(parentWIds,childWIds)

#driver.switch_to.window(childWIds)
#print(driver.title)

#driver.switch_to.window(parentWIds)
#print(driver.title)

#Approach2

#for wind in windowIds:
 #   driver.switch_to.window(wind)
    #print(driver.title)

    #close particular window
for wind in windowIds:
    driver.switch_to.window(wind)
    if driver.title=="OrangeHRM":
        driver.close()
