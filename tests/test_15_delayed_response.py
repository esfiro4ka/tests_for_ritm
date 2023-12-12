import requests
import time

from common_constants import EXPECTED_KEYS_LIST, USER_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/users?delay=3"


def test_get_users_list_with_delay():
    start_time = time.time()

    response = requests.get(ENDPOINT)

    end_time = time.time()

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    expected_delay = 3
    actual_delay = end_time - start_time
    assert actual_delay >= expected_delay, (
        f"Задержка {actual_delay} меньше ожидаемой {expected_delay}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in EXPECTED_KEYS_LIST:
        assert key in data, f"Ответ не содержит {key}"

    for user in data["data"]:
        for key in USER_EXPECTED_KEYS:
            assert key in user, f"У пользователя {user} отсутствует {key}"
