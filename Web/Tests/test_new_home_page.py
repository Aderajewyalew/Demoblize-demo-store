import allure
import pytest
from Web.Pages.new_home_page import *


class Test_phone_home_page:
    @allure.description('Sellect and order all phone product ')
    @pytest.mark.sanity
    def test_phone_products(self):
        run_phone_products = Phone_device(self)
        run_phone_products.click_phone_products()


class Test_laptope_home_page:
    @allure.description('Sellect and order all laptope product ')
    @pytest.mark.sanity
    def test_laptop_products(self):
        run_laptope_products = Laptope_device(self)
        run_laptope_products.click_laptope_products()


class Test_moniter_home_page:
    @allure.description('Sellect and order all moniter product ')
    @pytest.mark.sanity
    def test_moniter_products(self):
        run_moniter_products = Monitore_device(self)
        run_moniter_products.click_moniter_products()
