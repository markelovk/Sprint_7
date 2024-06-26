import requests
from variables import Urls, MessageText, Data
import allure
import pytest
from helpers import Helpers


class TestCreateOrder(Helpers):
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color',
        Data.order_data)
    @allure.title('Заказ с выбором цвета')
    def test_create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                          color):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": [color]
        }
        response = requests.post(Urls.create_order, json=payload)
        assert response.status_code == 201
        assert MessageText.create_order in response.text
