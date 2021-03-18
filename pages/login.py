from selenium.webdriver.support.select import Select
from pages.base import BasePage
from pages.locators import Locators
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_title(self):
        sel = Select(self.driver.find_element_by_id(Locators.login.DROP_DOWN_MENU_ID))
        sel.select_by_index(1)

    def enter_first_and_last_name(self, first_name, last_name):
        self.driver.find_element_by_id(Locators.login.FIRST_NAME_INPUT_ID).send_keys(first_name)
        self.driver.find_element_by_css_selector(Locators.login.LAST_NAME_INPUT_CSS).send_keys(last_name)

    def select_checkbox_agreement(self):
        self.driver.find_element_by_css_selector(Locators.login.CHECKBOX_CSS).click()

    def submit_form(self):
        self.driver.find_element_by_id(Locators.login.SUBMIT_FORM_ID).click()

    def is_bod_error_present(self):
        time.sleep(2)

        element = self.driver.find_element_by_css_selector(Locators.login.DOB_INPUT_CSS)
        class_value = element.get_attribute('class')
        return 'error' in class_value

