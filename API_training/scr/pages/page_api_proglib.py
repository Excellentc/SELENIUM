import json
import requests

url_users = 'https://reqres.in/api/users?page=1'
url_new_user = 'https://reqres.in/api/users'
new_user = {
    "name": "morpheus",
    "job": "leader"
}


def get_api_users_list(list_of_users_url):
    response_users = requests.get(list_of_users_url)
    return response_users


def post_new_user(add_user_url, user_data: tuple):
    response_add_user = requests.post(add_user_url, data=user_data)
    return response_add_user


response_list_users = get_api_users_list(url_users)
with open('users_list.json', 'w') as file:
    json.dump(response_list_users.json(), file, indent=4)
print(response_list_users.status_code)

response_new_user = post_new_user(add_user_url=url_new_user, user_data=new_user)
with open('registration_new_user.json', 'w') as file:
    json.dump(response_new_user.json(), file, indent=4)
print(response_new_user.status_code)
