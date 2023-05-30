import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from API_training.scr.pages.page_api_proglib import ApiPage


@pytest.mark.usefixtures('chrome')
class TestApiPage:
    url_new_user = 'https://reqres.in/api/users'
    url_users = 'https://reqres.in/api/users?page=1'
    new_user = {"name": "morpheus", "job": "leader"}

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_api = ApiPage(self.driver)

    def test_get_api_users_list(self):
        response_list_users = self.page_api.get_api_users_list(self.url_users)
        assert response_list_users.status_code == 200

    def test_post_new_user(self):
        response_new_user = self.page_api.post_new_user(add_user_url=self.url_new_user, user_data=self.new_user)
        assert response_new_user.status_code == 201
