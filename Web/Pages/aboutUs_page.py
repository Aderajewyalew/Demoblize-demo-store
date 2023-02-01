from selenium.webdriver.common.by import By
from Web.Base_test.base_test import *
from Web.Locatores.locators_aboutUs import *
from time import  sleep


class Locators_aboutUs:
    aboutUs_button = About_us.about_button_linkText
    start_vedio = About_us.vedio_play_xpath
    play_pause = About_us.play_puase_button
    close_button = About_us.close_button_xpath
    act_title = About_us.title


class AboutUs_pages(Locators_aboutUs, BaseTest):
    # this used to open the browsers
    def open_web(self):
        super().init()


    def click_aboutUs(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.aboutUs_button).click()

    def click_play_vedio(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.start_vedio).click()

    def click_pause_button(self):
        sleep(5)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.play_pause).click()

    def click_close_button(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.close_button).click()
        title_name = self.driver.title
        if title_name == "STORE":
            assert True
        else:
            assert False


