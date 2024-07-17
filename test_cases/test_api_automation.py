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
        assert responce.status_code == 201, "Pot API not working"

    def test_03_put_api(self):
        payload = {
          "name": "piyush",
          "job": "zion resident"
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









