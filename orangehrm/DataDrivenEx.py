import time
from importlib.resources import files

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from orangehrm import XLUtils
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

file="C:\\Users\\Lenovo\\Desktop\\Book2.xlsx"
rows=XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
#reading data from excel
 pric=XLUtils.readData(file,"Sheet1",r,1)
 rateofInterest=XLUtils.readData(file,"Sheet1",r,2)
 per1=XLUtils.readData(file,"Sheet1",r,3)
 per2=XLUtils.readData(file,"Sheet1",r,4)
 fre=XLUtils.readData(file,"Sheet1",r,5)
 exp_mvalue=XLUtils.readData(file,"Sheet1",r,6)

#passing data to application
driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
perioddrop=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
perioddrop.select_by_visible_text(per2)
frquency=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
frquency.select_by_visible_text(fre)
driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']//strong").text

#validation
if float(exp_mvalue)==float(act_mvalue):
    print("test passed")
    XLUtils.writeData(file,"Sheet1",r,8,"Passed")
    XLUtils.fillGreenColor(file,"Sheet1",r,8)
else:
    print("test failed")
    XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
    XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
    driver.close()




