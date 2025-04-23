from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver with WebDriverManager
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.google.com")

# Get the title of the webpage
title_of_webpage = driver.title
print("The title of the webpage is:", title_of_webpage)

# Close the driver
driver.quit()
