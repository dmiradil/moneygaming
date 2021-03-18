import settings
from pages.base import BasePage
from pages.locators import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(settings.BASE_RUL)

    def click_join_button(self):
        self.driver.find_element_by_css_selector(Locators.home.SIGN_IN_BUTTON_CSS).click()
