from selenium import webdriver

def headless_Chrome():
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome()
    return driver

driver=headless_Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()