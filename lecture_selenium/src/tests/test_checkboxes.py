import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from lecture_selenium.src.pages.page_checkboxes import TestTextCheckbox


@pytest.mark.usefixtures('chrome')
class TestCheckbox:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = TestTextCheckbox(self.driver).open()

    def test_checkbox_task_one(self):
        self.page.expand_folder('home')
        self.page.expand_second_folder('documents')
        assert self.page.mark_folder('desktop')
        assert self.page.mark_folder('office')
