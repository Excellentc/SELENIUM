import pytest
from lecture_selenium.src.pages.page_radiobutton import RadioButton
# from lecture_selenium.src.pages.page_radiobutton import ListRadioButton


@pytest.mark.usefixtures('chrome')
class TestRadioButton:
    def test_activate_yes_radio(self):
        self.driver.get('https://demoqa.com/radio-button')
        radiobutton_yes = RadioButton(self.driver, name='Yes')
        radiobutton_yes.enable().select()
        status_button_yes = radiobutton_yes.is_selected()

        radiobutton_impressive = RadioButton(self.driver, name='Impressive')
        radiobutton_no = RadioButton(self.driver, name='No')

        status_button_impressive = radiobutton_impressive.is_selected()
        status_button_no = radiobutton_no.is_selected()

        assert status_button_yes is True and (
                status_button_no is False and status_button_impressive is False), "Radio button YES is OFF"
        assert status_button_yes is True, "Radio button YES is OFF"

    def test_activate_disabled_radio_button(self):
        self.driver.get('https://demoqa.com/radio-button')
        radiobutton_no = RadioButton(self.driver, name='No')
        radiobutton_no.enable().select()
        status_button_no = radiobutton_no.is_selected()

        radiobutton_impressive = RadioButton(self.driver, name='Impressive')
        radiobutton_yes = RadioButton(self.driver, name='Yes')

        status_button_impressive = radiobutton_impressive.is_selected()
        status_button_yes = radiobutton_yes.is_selected()

        assert status_button_no is True and (
                status_button_yes is False and status_button_impressive is False), "Radio button NO is OFF"

    def test_get_radio_buttons_info(self):
        self.driver.get('https://demoqa.com/radio-button')
        radio_button_list = RadioButton(self.driver, name=None)
        radio_button_status = radio_button_list.get_radio_buttons_info()
        print(radio_button_status)
