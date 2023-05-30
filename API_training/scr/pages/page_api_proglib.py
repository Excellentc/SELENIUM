import pytest
import requests
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('chrome')
class ApiPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @staticmethod
    def get_api_users_list(list_of_users_url=None):
        response_users = requests.get(list_of_users_url)
        return response_users

    @staticmethod
    def post_new_user(add_user_url, user_data: tuple):
        response_add_user = requests.post(add_user_url, data=user_data)
        return response_add_user
