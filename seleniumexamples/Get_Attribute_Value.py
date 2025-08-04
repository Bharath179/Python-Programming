from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoAttribueVale:
    def get_attribute_value(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()

        # Open the webpage
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        try:
            # Wait until the 'username' input field is available (up to 10 seconds)
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
            )
            # Get the attribute value
            attr_value = username_field.get_attribute("name")
            print("Attribute value:", attr_value)

        except Exception as e:
            print("Error:", e)

        # Close the browser
        self.driver.quit()


# Create an instance of the class
demo = DemoAttribueVale()

# Call the method using the instance
demo.get_attribute_value()
