from selenium.webdriver.common.by import By
from Web.Base_test.base_test import *
from Web.Locatores.login_locators import *
from time import sleep
import allure


class Login_page_locatores:
    login_button = Login_locatores.login_button_link_text
    user_name = Login_locatores.login_username_xpath
    password = Login_locatores.login_password_xpath
    send_login = Login_locatores.send_login_Xpath
    close = Login_locatores.close_xpath
    act_title = Login_locatores.title_xpath


class Login_pages(Login_page_locatores, BaseTest):

    def open(self):
        super().init()

    def click_login_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.login_button).click()

    def enter_valid_username(self, username):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.user_name).clear()
        self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def enter_valid_password(self, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def click_send_login_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.send_login).click()

    def click_alert_button(self):
        sleep(2)
        self.driver.switch_to.alert.accept()
        title_name = self.driver.title
        if title_name == "STORE":
            assert True
        else:
            assert False







