import pytest
import allure
from Web.Pages.registore_pages import *


class Test_registore_page(Reistore_locatores):
    @allure.description("register with username and password")
    @pytest.mark.sanity
    def test_registore_valid_inputs(self):
        run_registore = Registor_pages(self)
        run_registore.open()
        run_registore.click_registor_button()
        run_registore.enter_valid_username("abebe")
        run_registore.enter_valid_password(415263)
        run_registore.click_send_sign_button()
        run_registore.click_alert_button()

    @allure.description("register with username and password")
    @pytest.mark.sanity
    def test_registore_null_username(self):
        run_registore = Registor_pages(self)
        run_registore.open()
        run_registore.click_registor_button()
        run_registore.enter_valid_username("")
        run_registore.enter_valid_password(415263)
        run_registore.click_send_sign_button()
        run_registore.click_alert_button()

    @allure.description("register with username and password")
    @pytest.mark.sanity
    def test_registore_null_passwor(self):
        run_registore = Registor_pages(self)
        run_registore.open()
        run_registore.click_registor_button()
        run_registore.enter_valid_username("adino")
        run_registore.enter_valid_password("")
        run_registore.click_send_sign_button()
        run_registore.click_alert_button()

    @allure.description("register with username and password")
    @pytest.mark.sanity
    def test_registore_null_passwor_username(self):
        run_registore = Registor_pages(self)
        run_registore.open()
        run_registore.click_registor_button()
        run_registore.enter_valid_username("")
        run_registore.enter_valid_password("")
        run_registore.click_send_sign_button()
        run_registore.click_alert_button()

