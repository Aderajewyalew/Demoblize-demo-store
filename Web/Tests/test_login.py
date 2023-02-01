import pytest
import allure
from Web.Pages.login_page import *
from Web.Locatores.login_locators import *


class Test_login_page(Login_locatores):
    @allure.description("login test valid username and password")
    @pytest.mark.sanity
    def test_login_valid(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("abebe")
        login_run.enter_valid_password("123456")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test invalid password")
    @pytest.mark.sanity
    def test_login_invalid_oassword(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("abebe")
        login_run.enter_valid_password("aaaaaa")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test invalid username")
    @pytest.mark.sanity
    def test_login_invalid_username(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("solomon")
        login_run.enter_valid_password("123456")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test invalid password and username")
    @pytest.mark.sanity
    def test_login_invalid_passwordUsername(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("asdfghj")
        login_run.enter_valid_password("aaaaaa")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test null password and username")
    @pytest.mark.sanity
    def test_login_invalid_input(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("")
        login_run.enter_valid_password("")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test null username")
    @pytest.mark.sanity
    def test_login_null_username(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("")
        login_run.enter_valid_password("4152655")
        login_run.click_send_login_button()
        login_run.click_alert_button()

    @allure.description("login test null password ")
    @pytest.mark.sanity
    def test_login_null_password(self):
        login_run = Login_pages(self)
        login_run.open()
        login_run.click_login_button()
        login_run.enter_valid_username("")
        login_run.enter_valid_password("4152655")
        login_run.click_send_login_button()
        login_run.click_alert_button()

