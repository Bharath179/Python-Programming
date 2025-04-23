from selenium.webdriver.common.by import By


class LoginPage():
    username_txt_field_name="user-name"
    password_txt_field_name="password"
    login_button_xpath="//input[@type='submit']"
    open_menu_button_xpath="//button[text()='Open Menu']"
    logout_button_link_text="Logout"

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.NAME, self.username_txt_field_name).clear()
        self.driver.find_element(By.NAME,self.username_txt_field_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.password_txt_field_name).clear()
        self.driver.find_element(By.NAME, self.password_txt_field_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_button_xpath).click()

    def click_menu(self):
        self.driver.find_element(By.NAME, self.open_menu_button_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.NAME, self.logout_button_link_text).click()