import requests
import json

from common_constants import UPDATE_USER_DATA, UPDATE_USER_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/users/2"


def test_update_user_put():
    response = requests.put(
            ENDPOINT,
            data=json.dumps(UPDATE_USER_DATA),
            headers={'Content-Type': 'application/json'}
        )

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in UPDATE_USER_EXPECTED_KEYS:
        assert key in data, f"В ответе отсутствует {key}"

    assert data["name"] == UPDATE_USER_DATA["name"], (
        "Значение 'name' не соответствует ожидаемому")
    assert data["job"] == UPDATE_USER_DATA["job"], (
        "Значение 'job' не соответствует ожидаемому")
