import pytest
import allure
from Web.Pages.aboutUs_page import *


class Test_aboutUs:

    @allure.description('test page about us')
    @pytest.mark.sanity
    def test_aboutUs(self):
        run_aboutUs = AboutUs_pages(self)
        run_aboutUs.open_web()
        run_aboutUs.click_aboutUs()
        run_aboutUs.click_play_vedio()
        run_aboutUs.click_pause_button()
        run_aboutUs.click_close_button()

