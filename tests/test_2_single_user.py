import requests

from common_constants import EXPECTED_KEYS_SINGLE, USER_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/users/2"
USER_ID = 2


def test_get_single_user():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in EXPECTED_KEYS_SINGLE:
        assert key in data, f"В ответе отсутствует {key}"

    user_data = data["data"]
    for key in USER_EXPECTED_KEYS:
        assert key in user_data, f"У пользователя отсутствует {key}"

    assert user_data["id"] == USER_ID, (
        f"Значение 'id' пользователя не соответствует ожидаемому {USER_ID}")
