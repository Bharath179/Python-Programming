import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MobilesPrice:
    def get_mobile_price(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("iphone" + Keys.RETURN)
        time.sleep(2)
        mobile_names = self.driver.find_elements(By.XPATH, "//div[@class='KzDlHZ']")
        time.sleep(2)
        mobile_prices = self.driver.find_elements(By.XPATH, "//div[@class='Nx9bqj _4b5DiR']")
        for name, price in zip(mobile_names, mobile_prices):
            print(f"Mobile Name: {name.text}")
            print(f"Mobile Price: {price.text}")
            print("-------------------------------------------------------------------------------")
            time.sleep(2)
        self.driver.quit()


# Create an instance of the class and call the method
mobiles = MobilesPrice()
mobiles.get_mobile_price()
