from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class BaseTest:

    def __init__(self, driver):
        self.driver = driver

    def init(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()
        self.driver.close()
        return self.driver
