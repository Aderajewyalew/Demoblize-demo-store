import allure
import pytest
from Web.Pages.home_page import *


class Test_phone_hamo_page:
    @allure.description("select  Samsung_s6 phone and order it ")
    @pytest.mark.sanity
    def test_galaxy_s6_phone(self):
        web_run_s6 = Phone_device(self)
        web_run_s6.function_common()
        web_run_s6.click_samsung_s6()
        web_run_s6.click_add_to_cart()
        web_run_s6.click_alert_box()
        web_run_s6.click_cart_button()
        web_run_s6.click_placeOrder_button()
        web_run_s6.payment_inputs()
        web_run_s6.click_purchase_botton()
        web_run_s6.click_okay()

    @allure.description("select  Nokia lumia phone and order it ")
    @pytest.mark.sanity
    def test_nokia_phone(self):
        web_run_s6 = Phone_device(self)
        web_run_s6.function_common()
        web_run_s6.click_phone_Nokia()
        web_run_s6.click_add_to_cart()
        web_run_s6.click_alert_box()
        web_run_s6.click_cart_button()
        web_run_s6.click_placeOrder_button()
        web_run_s6.payment_inputs()
        web_run_s6.click_purchase_botton()
        web_run_s6.click_okay()



    @allure.description("selct nexus phone to order")
    @pytest.mark.sanity
    def test_phone_nexus6(self):
        web_run_nexus = Phone_device(self)
        web_run_nexus.function_common()
        web_run_nexus.click_phone_nuxes6()
        web_run_nexus.click_add_to_cart()
        web_run_nexus.click_alert_box()
        web_run_nexus.click_cart_button()
        web_run_nexus.click_placeOrder_button()
        web_run_nexus.payment_inputs()
        web_run_nexus.click_purchase_botton()
        web_run_nexus.click_okay()

    @allure.description("select  galaxy_s7 phone and order it ")
    @pytest.mark.sanity
    def test_nokia_phone(self):
        web_run_s6 = Phone_device(self)
        web_run_s6.function_common()
        web_run_s6.click_phone_samsung_s7()
        web_run_s6.click_add_to_cart()
        web_run_s6.click_alert_box()
        web_run_s6.click_cart_button()
        web_run_s6.click_placeOrder_button()
        web_run_s6.payment_inputs()
        web_run_s6.click_purchase_botton()
        web_run_s6.click_okay()

    @allure.description("select  galaxy_s7 phone and order it ")
    @pytest.mark.sanity
    def test_nokia_phone(self):
        web_run_s6 = Phone_device(self)
        web_run_s6.function_common()
        web_run_s6.click_phone_Iphone()
        web_run_s6.click_add_to_cart()
        web_run_s6.click_alert_box()
        web_run_s6.click_cart_button()
        web_run_s6.click_placeOrder_button()
        web_run_s6.payment_inputs()
        web_run_s6.click_purchase_botton()
        web_run_s6.click_okay()

    @allure.description("select soney xpariaz5 to order")
    @pytest.mark.sanity
    def test_product_Sony_xperia_z5(self):
        web_run_z5 = Phone_device(self)
        web_run_z5.function_common()
        web_run_z5.scroll_upward()
        web_run_z5.click_Sony_xperia_z5()
        web_run_z5.click_add_to_cart()
        web_run_z5.click_alert_box()
        web_run_z5.click_cart_button()
        web_run_z5.click_placeOrder_button()
        web_run_z5.payment_inputs()
        web_run_z5.click_purchase_botton()
        web_run_z5.click_okay()

    @allure.description("select HTC ONE to order")
    @pytest.mark.sanity
    def test_Htc_one(self):
        web_run_s6 = Phone_device(self)
        web_run_s6.function_common()
        web_run_s6.click_phone_HTC_one()
        web_run_s6.click_add_to_cart()
        web_run_s6.click_alert_box()
        web_run_s6.click_cart_button()
        web_run_s6.click_placeOrder_button()
        web_run_s6.payment_inputs()
        web_run_s6.click_purchase_botton()
        web_run_s6.click_okay()



class Test_laptope_home_page:
    @allure.description("select vaio_i5 laptop to order")
    @pytest.mark.sanity
    def test_product_vaio_i5(self):
        web_run_i5 = Laptope_device(self)
        web_run_i5.function_common()
        web_run_i5.click_laptope_catagories()
        web_run_i5.click_vaio_i5()
        web_run_i5.click_add_cart()
        web_run_i5.clcik_allerBox()
        web_run_i5.click_cart()
        web_run_i5.click_place_Order()
        web_run_i5.paymment_input_laptope()
        web_run_i5.click_purchase()
        web_run_i5.click_okay()

    @allure.description("select vaio_i7 laptop to order")
    @pytest.mark.sanity
    def test_product_vaio_i7(self):
        web_run_i7 = Laptope_device(self)
        web_run_i7.function_common()
        web_run_i7.click_laptope_catagories()
        web_run_i7.click_vaio_i7()
        web_run_i7.click_add_cart()
        web_run_i7.clcik_allerBox()
        web_run_i7.click_cart()
        web_run_i7.click_place_Order()
        web_run_i7.paymment_input_laptope()
        web_run_i7.click_purchase()
        web_run_i7.click_ok_button()

    @allure.description("select macbook air to order")
    @pytest.mark.sanity
    def test_product_macbook(self):
        web_run_mac = Laptope_device(self)
        web_run_mac.function_common()
        web_run_mac.click_laptope_catagories()
        web_run_mac.click_macbook_air()
        web_run_mac.click_add_cart()
        web_run_mac.clcik_allerBox()
        web_run_mac.click_cart()
        web_run_mac.click_place_Order()
        web_run_mac.paymment_input_laptope()
        web_run_mac.click_purchase()
        web_run_mac.click_ok_button()

    @allure.description("select dell product to order")
    @pytest.mark.sanity
    def test_product_dell(self):
        web_run_dell = Laptope_device(self)
        web_run_dell.function_common()
        web_run_dell.click_laptope_catagories()
        web_run_dell.scroll_upwards()
        web_run_dell.clickk_Dell_i7()
        web_run_dell.click_add_cart()
        web_run_dell.clcik_allerBox()
        web_run_dell.click_cart()
        web_run_dell.click_place_Order()
        web_run_dell.paymment_input_laptope()
        web_run_dell.click_purchase()
        web_run_dell.click_ok_button()

    @allure.description("select dell product to order")
    @pytest.mark.sanity
    def test_product_dell(self):
        web_run_dell = Laptope_device(self)
        web_run_dell.function_common()
        web_run_dell.click_laptope_catagories()
        web_run_dell.scroll_upwards()
        web_run_dell.click_dell_2017()
        web_run_dell.click_add_cart()
        web_run_dell.clcik_allerBox()
        web_run_dell.click_cart()
        web_run_dell.click_place_Order()
        web_run_dell.paymment_input_laptope()
        web_run_dell.click_purchase()
        web_run_dell.click_ok_button()

    @allure.description("select dell product to order")
    @pytest.mark.sanity
    def test_product_dell(self):
        web_run_dell = Laptope_device(self)
        web_run_dell.function_common()
        web_run_dell.click_laptope_catagories()
        web_run_dell.scroll_upwards()
        web_run_dell.click_macbook_pro()
        web_run_dell.click_add_cart()
        web_run_dell.clcik_allerBox()
        web_run_dell.click_cart()
        web_run_dell.click_place_Order()
        web_run_dell.paymment_input_laptope()
        web_run_dell.click_purchase()
        web_run_dell.click_ok_button()


class Test_monitore_device:
    @allure.description("select Apple 24  product to order")
    @pytest.mark.sanity
    def test_product_apple(self):
        web_run_apple = MOnitore_page(self)
        web_run_apple.open_web()
        web_run_apple.click_ctagorie_monitores()
        web_run_apple.clickk_apple_24()
        web_run_apple.click_add_cart()
        web_run_apple.click_AlertBox()
        web_run_apple.click_cart()
        web_run_apple.click_place_Order()
        web_run_apple.paymment_apple()
        web_run_apple.click_purchase()
        web_run_apple.click_okay()

    @allure.description("select Assus  product to order")
    @pytest.mark.sanity
    def test_assus_product(self):
        web_run_assus = MOnitore_page(self)
        web_run_assus.open_web()
        web_run_assus.click_ctagorie_monitores()
        web_run_assus.clickk_asuss_HD()
        web_run_assus.click_add_cart()
        web_run_assus.click_AlertBox()
        web_run_assus.click_cart()
        web_run_assus.click_place_Order()
        web_run_assus.paymment_Assus_Hd()
        web_run_assus.click_purchase()
        web_run_assus.click_ok_button()
