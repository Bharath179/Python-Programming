from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

#capture cookies from the browser
cookies=driver.get_cookies()
print("size of cookies:",len(cookies))

#print details of all cookies
for c in cookies:
# print(c)
 print(c.get("name"),":",c.get("value"))

#print single cookie
cook=driver.get_cookie(".Nop.Customer")
print(cook)

#delete single cookie
dele=driver.delete_cookie(".Nop.Customer")
print(dele)

#delete all cookies
deleteallcookies=driver.delete_all_cookies()
print(deleteallcookies)

driver.close()