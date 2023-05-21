import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures('chrome')
class PageButtons:
    _instance = None
    URL = 'https://demoqa.com/dynamic-properties'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def status_button(self, button_id=None):  # button_disabled_enabled
        enable_disable_button = self.driver.find_element(By.ID, button_id)
        return enable_disable_button

    def wait_until_button_enabled(self, button):
        WebDriverWait(self.driver, 6).until(ec.element_to_be_clickable(button))
        return button

    def enabled_disabled_button(self, button_id=None):
        button = self.status_button(button_id)
        button_status = self.wait_until_button_enabled(button)
        button.click()
        return button_status

    def get_color_change_button_class(self):
        color_change_button = self.driver.find_element(By.ID, 'colorChange')
        color_change_button_class = color_change_button.get_attribute('class')
        color_change_button.click()
        return color_change_button_class

    def appeared_button(self, button_id=None):
        visible_after_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, button_id)))
        visible_after_button.click()
        return visible_after_button
