import requests

from common_constants import EXPECTED_KEYS_SINGLE, RESOURCE_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/unknown/2"
RESOURCE_ID = 2


def test_get_single_resource():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in EXPECTED_KEYS_SINGLE:
        assert key in data, f"В ответе отсутствует {key}"

    resource_data = data["data"]

    for key in RESOURCE_EXPECTED_KEYS:
        assert key in resource_data, f"У ресурса отсутствует {key}"

    assert resource_data["id"] == RESOURCE_ID, (
        f"Значение 'id' ресурса не соответствует ожидаемому {RESOURCE_ID}")
