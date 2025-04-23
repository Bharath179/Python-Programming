import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.o2.co.uk/")
driver.maximize_window()
driver.implicitly_wait(10)

actions = ActionChains(driver)


# Function to scroll into view
def scroll_to_element(element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


# Reject cookies
driver.find_element(By.ID, "onetrust-reject-all-handler").click()

# Hover over Shop > Phones
shop = driver.find_element(By.XPATH, "//span[text()='Shop']")
actions.move_to_element(shop).perform()
driver.find_element(By.XPATH, "(//span[text()='Phones'])[1]").click()

# Select iPhone 16
iphone = driver.find_element(By.XPATH, "//span[text()='iPhone 16']")
scroll_to_element(iphone)
actions.move_to_element(iphone).click().perform()

time.sleep(2)

# Select month plan
month_plan = driver.find_element(By.XPATH, "//button[@aria-label='Choose this plan 50GB tariff plan']")
scroll_to_element(month_plan)
actions.move_to_element(month_plan).pause(1).click().perform()

time.sleep(2)

# Pick Amazon Prime extra
pick_extra = driver.find_element(By.XPATH, "//button[@aria-label='Amazon Prime Pick this Extra, on us']")
scroll_to_element(pick_extra)
actions.move_to_element(pick_extra).pause(1).click().perform()

time.sleep(2)

# Add insurance
add_insurance = driver.find_element(By.XPATH,
                                    "//div[@class='_margin_top-s ng-star-inserted']//button[@aria-label='Add insurance O2 Insure Full Cover']")
scroll_to_element(add_insurance)
actions.move_to_element(add_insurance).pause(1).click().perform()

time.sleep(2)

# Add accessory
add_accessory = driver.find_element(By.XPATH,
                                    "//img[@alt='Apple AirPods 4']/ancestor::*[2]//span[text()=' Add accessory ']")
scroll_to_element(add_accessory)
actions.move_to_element(add_accessory).pause(1).click().perform()

time.sleep(2)

# Use plastic SIM
plastic_sim = driver.find_element(By.XPATH,
                                  "//div[@class='mat-radio-label-content' and contains(., 'Use a plastic sim')]")
scroll_to_element(plastic_sim)
actions.move_to_element(plastic_sim).pause(1).click().perform()

time.sleep(2)

# Add to basket
add_to_basket = driver.find_element(By.XPATH, "//span[text()=' Add to basket ']")
scroll_to_element(add_to_basket)
add_to_basket.click()

print("Done. Proceeded to basket with all extras added.")

# Checkout
checkout = driver.find_element(By.XPATH, "//button[@manual_cm_re='Standard Checkout']")
scroll_to_element(checkout)
checkout.click()

# Sign-In
try:
    signin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, " Sign in ")))
    signin.click()
    print("Sign-in page loaded successfully.")
except Exception as e:
    print("Sign-in element not found or page didn't load properly:", e)

# Quit browser
driver.quit()
