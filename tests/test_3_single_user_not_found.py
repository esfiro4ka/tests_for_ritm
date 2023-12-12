import requests


ENDPOINT = "https://reqres.in/api/users/23"


def test_get_nonexistent_user():
    response = requests.get(ENDPOINT)

    assert response.status_code == 404, (
        f"Ожидался код 404, получен {response.status_code}")

    assert response.content, "Тело ответа пустое"
    assert response.json() == {}, (
        "Тело ответа не соответствует ожидаемому (пустому JSON)")
