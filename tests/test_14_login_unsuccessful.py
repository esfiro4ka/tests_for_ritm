import requests
import json


ENDPOINT = "https://reqres.in/api/login"
INVALID_USER_PASSWORD = {
        "email": "peter@klave"
    }
INVALID_USER_EMAIL = {
        "password": "newpassword"
    }


def test_invalid_user_authentication_password():
    response = requests.post(
            ENDPOINT,
            data=json.dumps(INVALID_USER_PASSWORD),
            headers={'Content-Type': 'application/json'}
        )

    assert response.status_code == 400, (
        f"Ожидался код ответа 400, получен {response.status_code}")

    error_message = response.json()

    assert "error" in error_message, "Ответ не содержит 'error'"
    assert error_message["error"] == "Missing password", (
        "Неверное сообщение об ошибке")


def test_invalid_user_authentication_email():
    response = requests.post(
            ENDPOINT,
            data=json.dumps(INVALID_USER_EMAIL),
            headers={'Content-Type': 'application/json'}
        )

    assert response.status_code == 400, (
        f"Ожидался код ответа 400, получен {response.status_code}")

    error_message = response.json()

    assert "error" in error_message, "Ответ не содержит 'error'"
    assert error_message["error"] == "Missing email or username", (
        "Неверное сообщение об ошибке")
