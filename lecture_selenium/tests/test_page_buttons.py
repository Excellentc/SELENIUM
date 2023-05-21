import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from lecture_selenium.src.pages.page_buttons import PageButtons


@pytest.mark.usefixtures('chrome')
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_button = PageButtons(self.driver)
        self.page_button.open()

    def test_enabled_disabled_button(self):
        button = self.page_button.enabled_disabled_button(button_id='enableAfter')
        assert button.is_enabled()

    def test_get_color_change_button_class(self):
        color_button = self.page_button.get_color_change_button_class()
        assert color_button == 'mt-4 btn btn-primary'

    def test_appeared_button_two(self):
        button = self.page_button.appeared_button(button_id='visibleAfter')
        assert button.is_displayed()
