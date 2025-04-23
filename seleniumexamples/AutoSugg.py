import time

from selenium import webdriver
from selenium.webdriver.common.by import By


"""class DemoAutoSugg():
    def auto_sugg(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        autosugg=self.driver.find_element(By.NAME, "q")
        autosugg.send_keys("Selenium")
        options=self.driver.find_elements(By.XPATH,"//span[contains(text(), 'selenium')]")
        number=len(options)
        print(number)
        for option in options:
            print(option.text)
        self.driver.quit()
demo=DemoAutoSugg()
demo.auto_sugg()"""

class DemoCalender():
    def calender_date(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yatra.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//div[@class='css-rd021u']").click()
        time.sleep(5)
        all_dates=self.driver.find_elements(By.XPATH,"//div[@class='MuiBox-root css-1hl8t8y']")
        for date in all_dates:
            if date.get_attribute("aria-label")=="Choose Saturday, January 25th, 2025":
                date.click()
                break
        self.driver.quit()
demo=DemoCalender()
demo.calender_date()

