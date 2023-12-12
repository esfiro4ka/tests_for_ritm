import requests
import json


ENDPOINT = "https://reqres.in/api/login"
USER_DATA = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }


def test_user_authentication():
    response = requests.post(
            ENDPOINT,
            data=json.dumps(USER_DATA),
            headers={'Content-Type': 'application/json'}
        )

    assert response.status_code == 200, (
        f"Ожидался код ответа 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    assert "token" in data, "Ответ не содержит 'token'"
