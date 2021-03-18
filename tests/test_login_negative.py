import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from selenium import webdriver

import settings
from pages.home import HomePage
from pages.login import LoginPage


class BaseChromeDriver(unittest.TestCase):

    def setUp(self):
        print("Creating WebDriver")
        self.driver = webdriver.Chrome(settings.CHROME_DRIVER_PATH)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class TestLogin(BaseChromeDriver):
    def setUp(self):
        super().setUp()
        self.homePage = HomePage(self.driver)
        self.loginPage = LoginPage(self.driver)

    def test_error_dob_message(self):
        self.homePage.click_join_button()

        self.assertTrue('gameaccount' in self.driver.current_url)

        self.loginPage.select_title()
        self.loginPage.enter_first_and_last_name('First-Name', 'Last-Name')

        self.loginPage.scroll_down()

        self.loginPage.select_checkbox_agreement()
        self.loginPage.submit_form()

        is_present = self.loginPage.is_bod_error_present()

        self.assertTrue(is_present,
                        "Missing error message for 'Date of Birth'")
