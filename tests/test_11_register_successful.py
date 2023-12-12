import requests
import json


ENDPOINT = "https://reqres.in/api/register"
USER_DATA = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }


def test_user_registration():
    response = requests.post(
            ENDPOINT,
            data=json.dumps(USER_DATA),
            headers={'Content-Type': 'application/json'})

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    assert "id" in data, "Ответ не содержит 'id'"
    assert "token" in data, "Ответ не содержит 'token'"
