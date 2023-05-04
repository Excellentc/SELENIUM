from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver, name: None):
        self.driver = driver
        self.locator = '//label[.="{}"]//ancestor::div[contains(@class, "radio")]'.format(name)
        self.input_ = '/input'
        self.label = '/label'

    def is_selected(self) -> bool:
        element = self.driver.find_element(By.XPATH, f'{self.locator}{self.input_}')
        return element.is_selected()

    def select(self) -> None:
        self.driver.find_element(By.XPATH, f'{self.locator}{self.label}').click()

    def enable(self):
        locator = (By.XPATH, f'{self.locator}{self.input_}')
        element = self.driver.find_element(*locator)

        if not element.is_enabled():
            self.driver.execute_script("arguments[0].disabled = false;", element)
        return self

    def get_radio_buttons_info(self):
        radio_button_elements = self.driver.find_elements(By.XPATH, '//div[contains(@class, "radio")]')
        radio_button_status = {}

        for element in radio_button_elements:
            name_element = element.find_element(By.TAG_NAME, 'label')
            name = name_element.text.strip()

            input_element = element.find_element(By.TAG_NAME, 'input')
            if input_element.is_selected():
                radio_button_status[name] = 'Active'
            elif input_element.is_enabled():
                radio_button_status[name] = 'Enabled'
            else:
                radio_button_status[name] = 'Off'

        return radio_button_status
