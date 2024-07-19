import json

import requests
class Test_API:

    def test_01_get_api(self):
        responce = requests.get("https://reqres.in/api/users?page=2")
        print(responce.text)
        assert responce.status_code == 200, "Failed"

    def test_02_post_api(self):
        payload = {
              "name": "piyush",
              "job": "testing"
                    }
        responce = requests.post("https://reqres.in/api/users", json=payload)
        print(responce.status_code)
        print(responce.text)
        assert responce.json()["job"] == 'testing'
        assert responce.status_code == 201, "Pot API not working"

    def test_03_put_api(self):
        payload = {
          "name": "piyush",
          "job": "QA Automation"
                }
        responce = requests.put("https://reqres.in/api/users/2",  json=payload)
        print(responce.status_code)
        print(responce.text)
        assert responce.json()['name'] == "piyush"
        assert responce.status_code == 200, "PUT API is not working"

    def test_04_post_api_login(self):
        payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
            }
        responce = requests.post('https://reqres.in/api/login', json=payload)
        print(responce.text)
        print(responce.status_code)
        assert responce.status_code == 200, "Login API is not working"


    def test_05_delete(self):
        id = 20
        response = requests.delete(f"https://reqres.in/api/users/{id}")
        print(response.status_code)
        assert response.status_code == 204


    def test_06_post_api_register(self):
        pyload = {
                  "email": "eve.holt@reqres.in",
                  "password": "pistol"
                    }
        response = requests.post("https://reqres.in/api/register", json=pyload)
        print(response.status_code)
        assert response.status_code == 200

    def test_07_post_api_unsuccesful(self):
        payload = {
                    "email": "sydney@fife"
                    }
        response = requests.post("https://reqres.in/api/register", json=payload)
        print(response.json()['error'])
        assert response.status_code == 400

    def test_08_api_login_uncessful(self):
        payload = {
                "email": "peter@klaven"
                    }
        response = requests.post("https://reqres.in/api/login")
        print(response.json())
        print(response.status_code)
        assert response.status_code == 400

    def test_10_get_api_delay(self):
        responce = requests.get('https://reqres.in/api/users?delay=3')
        print(responce.status_code)
        assert responce.status_code == 200

    def test_11_patch_api(self):
        payload = {
                    "name": "Piyush",
                    "job": "QA testing"
                    }
        response = requests.patch('https://reqres.in/api/users/2', json=payload)
        print(response.status_code)
        print(response.json())
        assert response.status_code == 200

    def test_12_get_request_not_found(self):
        response = requests.get('https://reqres.in/api/unknown/23')
        print(response.status_code)
        assert  response.status_code == 404






