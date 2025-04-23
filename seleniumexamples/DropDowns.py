import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

"""class DemoDropDown():
    def drop_downs(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        dayDropdown=Select(self.driver.find_element(By.ID, "day"))
        time.sleep(2)
        dayDropdown.select_by_index(8)
        monthDropdown = Select(self.driver.find_element(By.ID, "month"))
        time.sleep(2)
        monthDropdown.select_by_visible_text("Apr")
        yearDropdown = Select(self.driver.find_element(By.ID, "year"))
        time.sleep(2)
        yearDropdown.select_by_value("2020")
        self.driver.quit()
demo = DemoDropDown()
demo.drop_downs()"""

"""class DemoDropDown():
    def drop_downs(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Select all options in 'day' dropdown
        dayDropdown = Select(self.driver.find_element(By.ID, "day"))
        for option in dayDropdown.options:
            dayDropdown.select_by_visible_text(option.text)
            print(f"Selected day: {option.text}") 
            time.sleep(2)

        # Select all options in 'month' dropdown
        monthDropdown = Select(self.driver.find_element(By.ID, "month"))
        for option in monthDropdown.options:
            monthDropdown.select_by_visible_text(option.text)  
            print(f"Selected month: {option.text}")
            time.sleep(2)

        # Select all options in 'year' dropdown
        yearDropdown = Select(self.driver.find_element(By.ID, "year"))
        for option in yearDropdown.options:
            yearDropdown.select_by_visible_text(option.text)  
            print(f"Selected year: {option.text}") 
            time.sleep(2)
        self.driver.quit()

demo = DemoDropDown()
demo.drop_downs()"""


#check dropdown is multiple or not
"""class DemoDropDown():
    def drop_downs(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        dayDropdown=Select(self.driver.find_element(By.ID, "day"))
        
        
        if dayDropdown.is_multiple:
            print("The selected dropdown is multiple")
        else:
            print("The selected dropdown is not multiple")
        self.driver.quit()
demo = DemoDropDown()
demo.drop_downs()"""

#select multiple options in multiselect dropdown
class DemoDropDown():
    def drop_downs(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///C:/Users/Lenovo/Desktop/dropdown.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        dayDropdown=Select(self.driver.find_element(By.ID, "cars"))
        if dayDropdown.is_multiple:
            print("The selected dropdown is multiple")
        else:
            print("The selected dropdown is not multiple")
        dayDropdown.select_by_visible_text("BMW")
        time.sleep(1)
        dayDropdown.select_by_value("5")
        time.sleep(1)
        dayDropdown.select_by_index(1)
        time.sleep(1)
        selected_options=dayDropdown.all_selected_options
        for options in selected_options:
            print(options.text)
        self.driver.quit()
demo = DemoDropDown()
demo.drop_downs()
