import allure
from time import sleep
from Web.Pages.place_order_page import *
from selenium.webdriver.common.by import By


class Phone_device(Home_page_phone, Order_page):

    # This is help to open the web  browsers
    @allure.step
    @allure.description('Navigate the website to order the products')
    def function_common(self):
        super().init()

    # select the product that we want to order in phone device page
    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_samsung_s6(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.galaxy_s6).click()

    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_Nokia(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Nokia).click()

    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_nuxes6(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Nuxes_6).click()

    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_samsung_s7(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.galaxy_s7).click()

    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_Iphone(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Iphone_6).click()


    @allure.step
    @allure.description('Clic the product to buy adn view details ')
    def click_phone_HTC_one(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.HTC_ONE).click()


    @allure.step
    @allure.description('Alert after order successfully')
    def scroll_upward(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0, 700);")

    @allure.step
    @allure.description('Click the product to buy adn view details ')
    def click_Sony_xperia_z5(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.sony_xpria).click()

    @allure.step
    @allure.description('Add the product to the cart')
    def click_add_to_cart(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.add_cart).click()

    @allure.step
    @allure.description('Alert after add to cart successfully')
    def click_alert_box(self):
        sleep(2)
        self.driver.switch_to.alert.accept()

    # To complete payment for selected ordered  products
    @allure.step
    @allure.description('View teh product after added to cart')
    def click_cart(self):
        super().click_cart_button()

    # Testing the payment process of selected product
    @allure.step
    @allure.description('Start to fill paymenet proccess')
    def click_place_Order(self):
        super().click_placeOrder_button()



    @allure.step
    @allure.description('Alert after order successfully')
    def payment_inputs(self):
        super().payment_formation("Aderajew", "Ethiopia", "Gondar", "412452", "10", "1999")



    @allure.step
    @allure.description('click the purchase button to finsh the order proccess')
    def click_purchase(self):
        super().click_purchase_botton()

    # Testing  the product work properly by assertion method
    @allure.step
    @allure.description('Alert after order successfully')
    def click_okay(self):
        super().click_ok_button()


class Laptope_device(Home_page_laptope, Order_page):
    @allure.step
    @allure.description('Alert after order successfully')
    def function_common(self):
        super().init()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_laptope_catagories(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.catagories).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_vaio_i5(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.vaio_i5).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_vaio_i7(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.vaio_i7).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_macbook_air(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.mack_book_air).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def scroll_upwards(self):
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0, 700);")

    @allure.step
    @allure.description('Alert after order successfully')
    def clickk_Dell_i7(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Dell_i7).click()


    @allure.step
    @allure.description('Alert after order successfully')
    def click_dell_2017(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.dell_2017).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_macbook_pro(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.macbook_pro).click()



    @allure.step
    @allure.description('Alert after order successfully')
    def click_add_cart(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.add_cart).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def clcik_allerBox(self):
        sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_cart(self):
        super().click_cart_button()

    # Testing the payment proccess of selected product
    @allure.step
    @allure.description('Alert after order successfully')
    def click_place_Order(self):
        super().click_placeOrder_button()

    @allure.step
    @allure.description('Alert after order successfully')
    def paymment_input_laptope(self):
        super().payment_formation("Aderajew", "Ethiopia", "Gondar", "412452", "10", "1999")



    @allure.step
    @allure.description('click the purchase button to finsh the order proccess')
    def click_purchase(self):
        super().click_purchase_botton()

    # Testing  the product work proprely by assertion method
    @allure.step
    @allure.description('Alert after order successfully')
    def click_okay(self):
        super().click_ok_button()


class MOnitore_page(Monitore_locatores, Order_page):
    @allure.step
    @allure.description('Alert after order successfully')
    def open_web(self):
        super().init()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_ctagorie_monitores(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.monitor_catagories).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def clickk_apple_24(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.apple_24).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def clickk_asuss_HD(self):
        sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Assus_HD).click()

    def click_add_cart(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, self.add_cart).click()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_AlertBox(self):
        sleep(2)
        self.driver.switch_to.alert.accept()

    @allure.step
    @allure.description('Alert after order successfully')
    def click_cart(self):
        super().click_cart_button()

        # Testing the payment proccess of selected product

    @allure.step
    @allure.description('Alert after order successfully')
    def click_place_Order(self):
        super().click_placeOrder_button()

    @allure.step
    @allure.description('Alert after order successfully')
    def paymment_apple(self):
        super().payment_formation("Aderajew", "Ethiopia", "Gondar", "412452", "10", "1999")

    @allure.step
    @allure.description('Alert after order successfully')
    def paymment_Assus_Hd(self):
        super().payment_formation("Aderajew", "Ethiopia", "Gondar", "412452", "10", "1999")

    @allure.step
    @allure.description('click the purchase button to finsh the order proccess')
    def click_purchase(self):
        super().click_purchase_botton()

        # Testing  the product work proprely by assertion method

    @allure.step
    @allure.description('Alert after order successfully')
    def click_okay(self):
        super().click_ok_button()

    # -------------------------------------------------------------------------------------------------------------------
