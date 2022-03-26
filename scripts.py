import email
import json
from datetime import datetime

import pytest
import requests


# latitude = '55'
# longitude = '37'
# res = requests.get( "http://api.open-notify.org/iss-pass.json?lat="+latitude+"&lon="+longitude)
# print(res.text)
#
# def get_api_key(email: str, passwd: str):
#    headers = {
#        'email': email,
#        'password': passwd,
#    }
#    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
#    status = res.status_code
#    try:
#        result = res.json()
#    except json.decoder.JSONDecodeError:
#        result = res.text
#    return status, result
#
#
# print(get_api_key('vasya@mail.com','12345'))


# @pytest.fixture()
# def get_key():
#     # переменные email и password нужно заменить своими учетными данными
#     response = requests.post(url='https://petfriends1.herokuapp.com/login',
#                              data={"email": "via@gmail.com", "pass": "qwerty"})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     return response.request.headers.get('Cookie')
#
# def test_getAllPets(get_key):
#     response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
#                             headers={"Cookie": get_key})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
#
# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")


#
# @pytest.fixture(scope="class", autouse=True)
# def session_fixture():
#     print("\nclass fixture starts")
#
# @pytest.fixture(scope="function", autouse=True)
# def function_fixture():
#     print("\nfunction fixture starts")
#
#
# class TestClass23:
#
#     def test_first(self):
#         pass
#
#     def test_second(self):
#         pass


# @pytest.fixture()
# def request_fixture(request):
#     print(request.fixturename)
#     print(request.scope)
#     print(request.function.__name__)
#     print(request.cls)
#     print(request.module.__name__)
#     print(request.fspath)
#     if request.cls:
#         return f"\n У теста {request.function.__name__} класс есть\n"
#     else:
#         return f"\n У теста {request.function.__name__} класса нет\n"
#
# def test_request_1(request_fixture):
#     print(request_fixture)
#
# class TestClassRequest:
#
#     def test_request_2(self, request_fixture):
#         print(request_fixture)


#
#
# @pytest.fixture(scope="class")
# def get_key(request):
#     # переменные email и password нужно заменить своими учетными данными
#     response = requests.post(url='https://petfriends1.herokuapp.com/login',
#                              data={"email": "via@gmail.com", "pass": "qwerty"})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     print("\nreturn auth_key")
#     return response.request.headers.get('Cookie')
#
#
# @pytest.fixture(autouse=True)
# def request_fixture(request):
#     if 'Pets' in request.function.__name__:
#         print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")
#
#
# class TestClassPets:
#
#     def test_getAllPets2(self, get_key):
#         response = requests.get(url='https://petfriends1.herokuapp.com/api/pets',
#                                 headers={"Cookie": get_key})
#         assert response.status_code == 200, 'Запрос выполнен неуспешно'
#         assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
#     def test_getMyPets2(self, get_key):
#         response = requests.get(url='https://petfriends1.herokuapp.com/my_pets',
#                                 headers={"Cookie": get_key})
#         assert response.status_code == 200, 'Запрос выполнен неуспешно'
#         assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
#
#     def test_anotherTest(self):
#         pass





@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
    pass


@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
    pass


@pytest.mark.api
@pytest.mark.event
def test_event_api():
    pass


@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
    pass
