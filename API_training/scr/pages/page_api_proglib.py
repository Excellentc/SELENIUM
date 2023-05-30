import json
import pytest
import requests
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('chrome')
class ApiPage:

    @staticmethod
    def get_api_users_list(list_of_users_url=None):
        response_users = requests.get(list_of_users_url)
        with open('users_list.json', 'w') as file:
            json.dump(response_users.json(), file, indent=4)
        return response_users

    @staticmethod
    def post_new_user(add_user_url, user_data):
        response_add_user = requests.post(add_user_url, data=user_data)
        with open('registration_new_user.json', 'w') as file:
            json.dump(response_add_user.json(), file, indent=4)
        return response_add_user
