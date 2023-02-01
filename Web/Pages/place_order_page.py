from selenium.webdriver.common.by import By
import allure
from Web.Locatores.place_order_locatorest import *
from Web.Base_test.base_test import *
from Web.Locatores.locatores_home_page import *


class Order_page_locatore:
    order = Order_locatores.order__button_xpath
    user_name = Order_locatores.name_box_id
    country = Order_locatores.country_box_id
    city = Order_locatores.city_box_id
    card = Order_locatores.card_box_id
    month = Order_locatores.month_box_id
    year = Order_locatores.year_box_id
    pearchus = Order_locatores.pearchus_button_xpath
    close = Order_locatores.close_button_xpath
    ok_button = Order_locatores.successful_xoath
    title = Order_locatores.title_text
    cart = Order_locatores.cart_button


class Home_page_phone:
    galaxy_s6 = Home_page_locatores.samsung_galaxy_s6
    Nokia = Home_page_locatores.nokiya_lumi
    Nuxes_6 = Home_page_locatores.nuxes_6
    galaxy_s7 = Home_page_locatores.samsung_galaxy_s7
    Iphone_6 = Home_page_locatores.iphone_32gb
    sony_xpria = Home_page_locatores.sony_xpria_Z5
    HTC_ONE = Home_page_locatores.htc_one
    add_cart = Home_page_locatores.add_cart
    cart = Home_page_locatores.cart_button
    name_product = Home_page_locatores.title_samsung
    phone_nuxs = Home_page_locatores.title_nexus
    title_xpari = Home_page_locatores.title_xpria
    text = Home_page_locatores.next_button
    order = Home_page_locatores.order__button_xpath
    user_name = Order_locatores.name_box_id
    country = Order_locatores.country_box_id
    city = Order_locatores.city_box_id
    card = Order_locatores.card_box_id
    month = Order_locatores.month_box_id
    year = Order_locatores.year_box_id
    pearchus = Order_locatores.pearchus_button_xpath
    close = Order_locatores.close_button_xpath
    ok_button = Order_locatores.successful_xoath
    title = Order_locatores.title_text
    act_title = Home_page_locatores.title


class Home_page_laptope:
    catagories = Home_page_laotope_locatore.link_laptope
    vaio_i5 = Home_page_laotope_locatore.viao_i5
    vaio_i7 = Home_page_laotope_locatore.vaio_i7
    mack_book_air = Home_page_laotope_locatore.mack_book_air
    Dell_i7 = Home_page_laotope_locatore.Dell_i7
    dell_2017 = Home_page_laotope_locatore.Dell_2017
    macbook_pro = Home_page_laotope_locatore.mackBook_pro
    add_cart = Home_page_locatores.add_cart
    cart = Home_page_locatores.cart_button
    title = Home_page_laotope_locatore.title_vaio
    titl_i7 = Home_page_laotope_locatore.title_vaio_i7
    title_macbook = Home_page_laotope_locatore.title_macbook
    title_dell = Home_page_laotope_locatore.dell
    order = Order_locatores.order__button_xpath
    user_name = Order_locatores.name_box_id
    country = Order_locatores.country_box_id
    city = Order_locatores.city_box_id
    card = Order_locatores.card_box_id
    month = Order_locatores.month_box_id
    year = Order_locatores.year_box_id
    pearchus = Order_locatores.pearchus_button_xpath
    close = Order_locatores.close_button_xpath
    ok_button = Order_locatores.successful_xoath
    titles = Order_locatores.title_text


class Monitore_locatores:
    monitor_catagories = Moniter_device.monitore_device_link_texs
    apple_24 = Moniter_device.apple24_xpath
    Assus_HD = Moniter_device.assus_HD_xpath
    order = Moniter_device.order__button_xpath
    user_name = Moniter_device.name_box_id
    country = Moniter_device.country_box_id
    city = Moniter_device.city_box_id
    card = Moniter_device.card_box_id
    month = Moniter_device.month_box_id
    year = Moniter_device.year_box_id
    pearchus = Moniter_device.pearchus_button_xpath
    close = Moniter_device.close_button_xpath
    ok_button = Moniter_device.successful_xoath
    title = Moniter_device.title_text
    act_title = Moniter_device.title
    add_cart = Moniter_device.add_cart
    cart = Moniter_device.cart_button


class Order_page(Order_page_locatore, BaseTest):

    @allure.step
    @allure.description('View teh product after added to cart')
    def click_cart_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.cart).click()

    # Testing the payment proccess of selected product I used this module becase i did for all products
    # the same assertion methods

    @allure.step
    @allure.description('Start to fill paymenet proccess')
    def click_placeOrder_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.order).click()

    def payment_formation(self, name, country, city, card, month, year):
        self.driver.find_element(By.ID, self.user_name).clear()
        self.driver.find_element(By.ID, self.user_name).send_keys(name)

        self.driver.find_element(By.ID, self.country).clear()
        self.driver.find_element(By.ID, self.country).send_keys(country)

        self.driver.find_element(By.ID, self.city).clear()
        self.driver.find_element(By.ID, self.city).send_keys(city)

        self.driver.find_element(By.ID, self.card).clear()
        self.driver.find_element(By.ID, self.card).send_keys(card)

        self.driver.find_element(By.ID, self.month).clear()
        self.driver.find_element(By.ID, self.month).send_keys(month)

        self.driver.find_element(By.ID, self.year).clear()
        self.driver.find_element(By.ID, self.year).send_keys(year)

    @allure.step
    @allure.description('click the purchase button to finsh the order process')
    def click_purchase_botton(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.pearchus).click()

    # Testing  the product work proprely by assertion method used it title
    @allure.step
    @allure.description('Alert after order successfully')
    def click_ok_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.ok_button).click()
        title_name = self.driver.title
        if title_name == "STORE":
            assert True
        else:
            assert False

