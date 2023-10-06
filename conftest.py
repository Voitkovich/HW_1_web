import pytest
import yaml
import requests
import json


with open('config.yaml', 'r', encoding='utf-8') as f:
    data=yaml.safe_load(f)
    username, password, address, adress_post = data['username'], data['password'], data['address'], data['address_posts']


@pytest.fixture()
def user_login():
    obj_data = requests.post(url=address, data={'username':username, 'password':password})
    token = obj_data.json()['token']
    return token


@pytest.fixture()
def post_create(token):
    param={
        'title': 'Test title',
        'description': 'Test description',
        'content':'Test content'}
    new_post = requests.post(url=adress_post, headers={"X-Auth-Token": token}, params={'owner':'notMe'},
                             data=param)
    return new_post.json()['description']


@pytest.fixture()
def get_token():
    response = requests.post(url=conf['url'], data={'username': conf['username'], 'password': conf['password']})
    return response.json()['token']









