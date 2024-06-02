import requests
import variables
import allure
from helpers import Helpers


class TestCreateCourier(Helpers):
    @allure.title('Создание курьера с заполненными обязательнымт полями')
    def test_create_courier(self):
        login, password, name = self.data_generate()
        payload = {
            "login": login,
            "password": password,
            "firstName": name
        }
        response = requests.post(f'{variables.url}/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == variables.create_courier
        self.delete_courier(login, password)

    @allure.title('Создание курьера с повторяющимся логином')
    def test_create_courier_duplicate(self):
        login, password, name = self.data_generate()
        payload = {
            "login": login,
            "password": password,
            "firstName": name
        }
        response = requests.post(f'{variables.url}/api/v1/courier', data=payload)
        if response.status_code == 201:
            response_duplicate = requests.post(f'{variables.url}/api/v1/courier', data=payload)
            assert response_duplicate.status_code == 409
            assert variables.create_courier_duplicate in response_duplicate.text
            self.delete_courier(login, password)

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login(self):
        login, password, name = self.data_generate()
        payload = {
            "password": password,
            "firstName": name
        }
        response = requests.post(f'{variables.url}/api/v1/courier', data=payload)
        assert response.status_code == 400
        assert variables.create_courier_without_data in response.text

    @allure.title('Создание курьера без пароля')
    def test_create_courier_without_password(self):
        login, password, name = self.data_generate()
        payload = {
            "login": login,
            "firstName": name
        }
        response = requests.post(f'{variables.url}/api/v1/courier', data=payload)
        assert response.status_code == 400
        assert variables.create_courier_without_data in response.text

    @allure.title('Создание курьера без имени')
    def test_create_courier_without_name(self):
        login, password, name = self.data_generate()
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(f'{variables.url}/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == variables.create_courier
        self.delete_courier(login, password)
