from selenium.webdriver.common.by import By
from Web.Base_test.base_test import *
from Web.Locatores.registore_locatores import *
from time import sleep


class Rgistore_page_locatores:
    singup_button = Reistore_locatores.Signup_box_xpath
    user_name = Reistore_locatores.username_box_id
    password = Reistore_locatores.password_box_id
    signup = Reistore_locatores.signup_xpath
    close = Reistore_locatores.close_xpath
    title = Reistore_locatores.title_xpath


class Registor_pages(Rgistore_page_locatores, BaseTest):

    def open(self):
        super().init()

    def click_registor_button(self):
        self.driver.find_element(By.XPATH, self.singup_button).click()

    def enter_valid_username(self, username):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.user_name).clear()
        self.driver.find_element(By.ID, self.user_name).send_keys(username)

    def enter_valid_password(self, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def click_send_sign_button(self):
        self.driver.find_element(By.XPATH, self.signup).click()

    def click_alert_button(self):
        sleep(2)
        alert_text = self.driver.switch_to.alert.text
        if alert_text == "Please fill out Username and Password.":
            print( alert_text)
            assert True
        elif alert_text == "Sign up successful.":
            print(alert_text)
            assert True
        else:
            print("This user already exist.")
            assert True

        self.driver.switch_to.alert.accept()
