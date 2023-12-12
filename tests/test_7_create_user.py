import requests
import json

from common_constants import CREATE_USER_DATA, CREATE_USER_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/users"


def test_create_user():
    response = requests.post(
            ENDPOINT,
            data=json.dumps(CREATE_USER_DATA),
            headers={'Content-Type': 'application/json'}
        )

    assert response.status_code == 201, (
        f"Ожидался код 201, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in CREATE_USER_EXPECTED_KEYS:
        assert key in data, f"В ответе отсутствует {key}"

    assert data["name"] == CREATE_USER_DATA["name"], (
        "Значение 'name' не соответствует ожидаемому"
    )
    assert data["job"] == CREATE_USER_DATA["job"], (
        "Значение 'job' не соответствует ожидаемому"
    )
