import requests

from common_constants import EXPECTED_KEYS_LIST, USER_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/users?page=2"
PAGE = 2


def test_get_users_list_page_two():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in EXPECTED_KEYS_LIST:
        assert key in data, f"В ответе отсутствует {key}"

    assert data["page"] == PAGE, (
                           f"Значение 'page' не равно {PAGE}")

    for user in data["data"]:
        for key in USER_EXPECTED_KEYS:
            assert key in user, f"У пользователя {user} отсутствует {key}"
