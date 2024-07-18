import json
import pytest
import requests

class TestAPI:

    def test_01_get_api(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        assert response.status_code == 200, f"Failed: {response.text}"
        print(response.json())  # Optional: Print response JSON

    def test_02_post_api(self):
        payload = {
            "name": "piyush",
            "job": "testing"
        }
        response = requests.post("https://reqres.in/api/users", json=payload)
        assert response.status_code == 201, f"Failed: {response.text}"
        assert response.json()["job"] == "testing"
        print(response.json())  # Optional: Print response JSON

    def test_03_put_api(self):
        payload = {
            "name": "piyush",
            "job": "zion resident"
        }
        response = requests.put("https://reqres.in/api/users/2", json=payload)
        assert response.status_code == 200, f"Failed: {response.text}"
        assert response.json()['name'] == "piyush"
        print(response.json())  # Optional: Print response JSON

    def test_04_post_api_login(self):
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post('https://reqres.in/api/login', json=payload)
        assert response.status_code == 200, f"Failed: {response.text}"
        print(response.json())  # Optional: Print response JSON

    def test_05_delete_api(self):
        response = requests.delete("https://reqres.in/api/users/2")
        assert response.status_code == 204, f"Failed: {response.text}"
        print("Deletion successful")

