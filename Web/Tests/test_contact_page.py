import pytest
import allure
from Web.Pages.contact_page import *


class Test_contact_page(Contac_page):
    @allure.description("contact page test valide email and username")
    @pytest.mark.sanity
    def test_page_valid_data(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("aderajew@gmail.com")
        contact.enter_name_contact("solomon")
        contact.enter_message_contact("thanks")
        contact.click_send_message()
        contact.click_alert_box()


    @allure.description("contact page test with invalid email null username ")
    @pytest.mark.sanity
    def test_pages_invalid_email(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("Ethio-form agriculture.com")
        contact.enter_name_contact("")
        contact.enter_message_contact("Be Happy don't woory")
        contact.click_send_message()
        contact.click_alert_box()


    @allure.description("contact page test with null email  ")
    @pytest.mark.sanity
    def test_paege_null_email(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("")
        contact.enter_name_contact("Mulualem ")
        contact.enter_message_contact("You are a great person keep calm and calm down")
        contact.click_send_message()
        contact.click_alert_box()

    @allure.description("contact page test with null email and username ")
    @pytest.mark.sanity
    def test_paege_null_email(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("")
        contact.enter_name_contact("")
        contact.enter_message_contact("We will be together my friends be healthy!  :)")
        contact.click_send_message()
        contact.click_alert_box()

    @allure.description("contact page test with null email and username ")
    @pytest.mark.sanity
    def test_paege_null_messages(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("")
        contact.enter_name_contact("")
        contact.enter_message_contact("")
        contact.click_send_message()
        contact.click_alert_box()

    @allure.description("contact page test  email with numbers ")
    @pytest.mark.sanity
    def test_paege_numberValue_email(self):
        contact = New(self)
        contact.opens_function()
        contact.click_contact_button()
        contact.enter_email_contact("415263987")
        contact.enter_name_contact("")
        contact.enter_message_contact("If this work completly the website has a problems")
        contact.click_send_message()
        contact.click_alert_box()


