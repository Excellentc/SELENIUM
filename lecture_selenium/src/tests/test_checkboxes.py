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
        self.page.expand_folder('documents', parent='home')
        # self.page.expand_second_folder('documents')    ----------for two function , first  version
        assert self.page.mark_folder('desktop')
        assert self.page.mark_folder('office')

    def test_checkbox_task_one_for_list(self):
        checkbox_list = ['home', 'documents']
        self.page.expand_folder_from_list(names=checkbox_list)
        assert self.page.mark_folder('desktop')
        assert self.page.mark_folder('office')
