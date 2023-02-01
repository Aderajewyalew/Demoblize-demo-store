import allure
from time import sleep
from Web.Pages.place_order_page import *
from selenium.webdriver.common.by import By


class Phone_device(Home_page_phone, Order_page):
    # To select phone products
    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_products(self):
        l = 0
        for i in range(6):
            super().init()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, f"/html/body/div[5]/div/div[2]/div/div[{l + 1}]/div/a/img").click()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.LINK_TEXT, "Add to cart").click()

            sleep(2)
            self.driver.switch_to.alert.accept()

            super().click_cart_button()
            super().click_placeOrder_button()
            super().payment_formation("David", "Ethiopia", "Adiis Ababa", "74185296", "1", "2000")
            super().click_purchase_botton()
            super().click_ok_button()
            l += 1


class Laptope_device(Home_page_laptope, Order_page):
    # To select laptop products
    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_laptope_products(self):
        l = 0
        for i in range(6):
            super().init()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.LINK_TEXT, self.catagories).click()
            sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, f"/html/body/div[5]/div/div[2]/div/div[{l + 1}]/div/a/img").click()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.LINK_TEXT, "Add to cart").click()

            sleep(2)
            self.driver.switch_to.alert.accept()

            super().click_cart_button()
            super().click_placeOrder_button()
            super().payment_formation("Aderajew", "Ethiopia", "Gondar", "412452", "10", "1999")
            super().click_purchase_botton()
            super().click_ok_button()
            l += 1


class Monitore_device(Monitore_locatores, Order_page):
    #  To select monitors product
    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_moniter_products(self):
        l = 0
        for i in range(2):
            super().init()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.LINK_TEXT, self.monitor_catagories).click()
            sleep(2)
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH, f"/html/body/div[5]/div/div[2]/div/div[{l + 1}]/div/a/img").click()

            self.driver.implicitly_wait(5)
            self.driver.find_element(By.LINK_TEXT, "Add to cart").click()

            sleep(2)
            self.driver.switch_to.alert.accept()
            super().click_cart_button()
            super().click_placeOrder_button()
            super().payment_formation("Temsgen", "Israel", "Ashkelon", "1111111111", "7", "1997")
            super().click_purchase_botton()
            super().click_ok_button()
            l += 1
