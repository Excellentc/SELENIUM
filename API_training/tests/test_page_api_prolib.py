import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from API_training.scr.pages.page_api_proglib import ApiPage


class TestApiPage:
    url_new_user = 'https://reqres.in/api/users'
    url_users = 'https://reqres.in/api/users?page=1'

    def setup_method(self):
        self.page_api = ApiPage()

    def test_get_api_users_list(self):
        response_list_users = self.page_api.get_api_users_list(self.url_users)
        print(response_list_users.status_code)
        assert response_list_users.status_code == 200

    @pytest.mark.parametrize('new_user', [
        {"name": "morpheus", "job": "leader"},
        {"name": "morpheus", "job": False},
        {"name": 1, "job": "QA"}
    ])
    def test_post_new_user(self, new_user):
        response_new_user = self.page_api.post_new_user(add_user_url=self.url_new_user, user_data=new_user)
        print(response_new_user.status_code)
        assert response_new_user.status_code == 201
