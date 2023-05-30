import pytest
import json
from selenium.webdriver.remote.webdriver import WebDriver
from API_training.scr.pages.page_api_proglib import ApiPage


@pytest.mark.usefixtures('chrome')
class TestApiPage:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_api = ApiPage(self.driver)

    def test_get_api_users_list(self):
        url_users = 'https://reqres.in/api/users?page=1'
        response_list_users = self.page_api.get_api_users_list(url_users)
        with open('users_list.json', 'w') as file:
            json.dump(response_list_users.json(), file, indent=4)
        assert response_list_users.status_code == 200

    def test_post_new_user(self):
        url_new_user = 'https://reqres.in/api/users'
        new_user = {"name": "morpheus", "job": "leader"}
        response_new_user = self.page_api.post_new_user(add_user_url=url_new_user, user_data=new_user)
        with open('registration_new_user.json', 'w') as file:
            json.dump(response_new_user.json(), file, indent=4)
        assert response_new_user.status_code == 201
