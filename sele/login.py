from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.get("https://yatra.com")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links found: {len(all_links)}")
for link in all_links:
    url = link.get_attribute("href")
    try:
        response = requests.head(url, allow_redirects=True, timeout=2)
        status = response.status_code

        if status >= 400:
            print(f"Broken link: {url} --> Status code: {status}")
        else:
            print(f"Valid link: {url} --> Status code: {status}")

    except requests.exceptions.RequestException as e:
        print(f"Error checking link: {url} --> {e}")
driver.quit()
