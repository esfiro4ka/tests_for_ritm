import requests

from common_constants import EXPECTED_KEYS_LIST, RESOURCE_EXPECTED_KEYS


ENDPOINT = "https://reqres.in/api/unknown"


def test_get_resources_list():
    response = requests.get(ENDPOINT)

    assert response.status_code == 200, (
        f"Ожидался код 200, получен {response.status_code}")

    assert "application/json" in response.headers["Content-Type"], (
        "Ответ не в формате JSON")

    data = response.json()

    for key in EXPECTED_KEYS_LIST:
        assert key in data, f"В ответе отсутствует {key}"

    for resource in data["data"]:
        for key in RESOURCE_EXPECTED_KEYS:
            assert key in resource, f"У ресурса {resource} отсутствует {key}"
