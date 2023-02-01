from selenium.webdriver.common.by import By
from Web.Base_test.base_test import *
from Web.Locatores.locatores_contact_us import *
import allure
from time import sleep


class Contac_page:
    contact_button = Contact_locatores.contact_path
    email = Contact_locatores.contact_email_path
    name = Contact_locatores.contact_name_path
    message = Contact_locatores.contact_message_path
    send_button = Contact_locatores.send_path
    close_button = Contact_locatores.close_path
    email_value = Contact_locatores.email
    name_value = Contact_locatores.name
    message_value = Contact_locatores.message
    act_title = Contact_locatores.title


class New(Contac_page, BaseTest):
    # This used to open the browsers
    def opens_function(self):
        super().init()

    @allure.step
    @allure.description('click a contact button')
    def click_contact_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_button).click()
        self.driver.implicitly_wait(200000)

    @allure.step
    @allure.description('enter an your valid email')
    def enter_email_contact(self, contact_email):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.email).clear()
        self.driver.find_element(By.ID, self.email).send_keys(contact_email)

    @allure.step
    @allure.description('enter a contact name')
    def enter_name_contact(self, contact_name):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.name).clear()
        self.driver.find_element(By.ID, self.name).send_keys(contact_name)

    @allure.step
    @allure.description('write a message on a message box')
    def enter_message_contact(self, contact_message):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.message).clear()
        self.driver.find_element(By.ID, self.message).send_keys(contact_message)

    @allure.step
    @allure.description('click a send message to sena a message')
    def click_send_message(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.send_button).click()

    @allure.step
    @allure.description('Alert after add to cart successfully')
    def click_alert_box(self):
        sleep(2)
        self.driver.switch_to.alert.accept()
        title_name = self.driver.title
        if title_name == "STORE":
            assert True
        else:
            assert False
