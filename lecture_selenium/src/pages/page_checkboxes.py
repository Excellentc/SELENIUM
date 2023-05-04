import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('chrome')
class TestTextCheckbox:
    _instance = None
    URL = 'https://demoqa.com/checkbox'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.folder_loc = '//label[contains(@for, "tree-node-{folder}")]'
        self.folder_expand_button_loc = f'{self.folder_loc}//ancestor::span/button'
        self.expand_status_loc = '//*[contains(@class, "expand-{}")]'
        self.folder_checkbox_input_loc = f'{self.folder_loc}/input'

    def open(self):
        self.driver.get(self.URL)
        return self

    def collapse_folder(self, name):
        home = self.driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
        try:
            collapse = home.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
            if collapse.is_displayed():
                collapse.click()
        except NoSuchElementException:
            pass
        home.click()

    def change_folder_selection_state(self, name, enabled=False):
        folder_loc = f'//label[contains(@for, "tree-node-{name}")]'
        input_loc = f'{folder_loc}/input'
        home = self.driver.find_element(By.XPATH, folder_loc)
        input_el = self.driver.find_element(By.XPATH, input_loc)
        if enabled:
            if not input_el.is_selected():
                home.click()
                return True
        else:
            if input_el.is_selected():
                home.click()
                return False

    def mark_folder(self, name):
        return self.change_folder_selection_state(name, enabled=True)

    def un_mark_folder(self, name):
        return self.change_folder_selection_state(name, enabled=False)

    def expand_folder_from_list(self, names, parent=None):
        for name in names:
            if parent is None:
                parent_element = self.driver.find_element(By.XPATH,
                                                          f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
            else:
                parent_element = parent.find_element(By.XPATH,
                                                     f'//label[@for="tree-node-{name}"]/preceding-sibling::button')
            try:
                expand = parent_element.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
                if expand.is_displayed():
                    parent_element.click()
            except NoSuchElementException:
                pass
            parent = parent_element


""" next three functions its a previoisly atempts for reolization Expand_folder function
    All worked. expand_folder + expand_second_folder and expand_folder_1"""



    #
    # def expand_folder_1(self, name, parent=None):
    #
    #     if parent is None:
    #         parent_element = self.driver.find_element(By.XPATH,
    #                                                   f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
    #     else:
    #         parent_element = self.driver.find_element(By.XPATH,
    #                                                   f'//label[@for="tree-node-{name}"]/preceding-sibling::button')
    #     try:
    #         expand = parent_element.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
    #         if expand.is_displayed():
    #             parent_element.click()
    #     except NoSuchElementException:
    #         pass
    #
    # def expand_second_folder(self, name):
    #     parent_element = self.driver.find_element(By.XPATH,
    #                                              f'//label[@for="tree-node-{name}"]/preceding-sibling::button')
    #     try:
    #         expand = parent_element.find_element(By.XPATH, './/*[contains(@class, "expand-open")]')
    #         if expand.is_displayed():
    #             expand.click()
    #     except NoSuchElementException:
    #         pass
    #     parent_element.click()

# def expand_folder(self, name):
#     home = self.driver.find_element(By.XPATH, f'//label[contains(@for, "tree-node-{name}")]//ancestor::span/button')
#     try:
#         expand = home.find_element(By.XPATH, '//*[contains(@class, "expand-open")]')
#         if expand.is_displayed():
#             expand.click()
#     except NoSuchElementException:
#         pass
#     home.click()
