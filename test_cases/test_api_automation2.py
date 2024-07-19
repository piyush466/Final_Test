import json

import requests

class Test_API2:

    def test_01_get_api(self):
        responce = requests.get("https://api.restful-api.dev/objects")
        json_str = json.dumps(responce.json(), indent=4)
        print(json_str)
        assert responce.status_code == 200

    def test_02_post_api(self):
        payload = {
                 "name": "Apple MacBook Pro 17",
                 "data": {
                 "year": 2019,
                 "price": 1800.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
                 }
            }
        response = requests.post("https://api.restful-api.dev/objects", json=payload)
        json_str = json.dumps(response.json(), indent=4)
        print(json_str)
        print(response.status_code)
        assert response.json()['name'] == "Apple MacBook Pro 17"
        assert (response.json()['data']['year']) == 2019
        id = response.json()['id']
        response_get = requests.get(f"https://api.restful-api.dev/objects/{id}")
        status_code = json.dumps(response_get.status_code, indent=4)
        print(status_code)






