import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ClassRoom:
    def test_fee(self):
        expected_fee = 71250
        driver = webdriver.Chrome()
        driver.get("https://techassignments.imsindia.com/ipm-bba-classroom-2025/")
        driver.implicitly_wait(5)
        driver.maximize_window()

        # Selecting City as Cochin
        city = Select(driver.find_element(By.ID, "city"))
        city.select_by_visible_text("Cochin")
        time.sleep(2)

        # Selecting Center as M G Road
        center = Select(driver.find_element(By.ID, "centernew"))
        center.select_by_visible_text("M G Road")
        time.sleep(2)

        base_fee_element = driver.find_element(By.XPATH,
                                               "//div[@class='course-cost__cost']/span[normalize-space(text())='Base "
                                               "Fees:']/following-sibling::span[1]"
                                               )
        base_fee_text = base_fee_element.text.strip()
        print("Base Fee Text:", base_fee_text)

        # Regex module to extract only numbers
        fee_digits = re.findall(r'\d+', base_fee_text.replace(',', ''))
        if fee_digits:
            base_fee_value = int(''.join(fee_digits))
            print(f"Extracted Base Fee value: {base_fee_value}")

            if base_fee_value == expected_fee:
                print("Test Passed: Base fees match expected amount excluding GST.")
            else:
                print("Test Failed: Base fees do not match expected amount.")
        else:
            print("Could not extract digits from base fee text.")

        driver.quit()


fee = ClassRoom()
fee.test_fee()
