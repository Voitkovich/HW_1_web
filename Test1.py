import yaml
import pytest
from api.api_func import get_token


with open('config.yaml', encoding='utf-8') as f:
    data1 = yaml.safe_load(f)
    username, password, address, adress_post,  = data1['username'], data1['password'], data1['address'], data1['address_posts']


def test_step1(login):
    assert '' in get_token(login)


def test_step2(post_create):
    assert 'Test description' in post_create


if __name__ == '__main__':
    # print(token_auth('token'))
    pytest.main(['-v'])
