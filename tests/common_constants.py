CREATE_USER_DATA = {
        "name": "morpheus",
        "job": "leader"
    }

CREATE_USER_EXPECTED_KEYS = ["name", "job", "id", "createdAt"]

EXPECTED_KEYS_LIST = [
    "page", "per_page", "total", "total_pages", "data", "support"]

EXPECTED_KEYS_SINGLE = ["data", "support"]

UPDATE_USER_DATA = {
        "name": "morpheus",
        "job": "zion resident"
    }

UPDATE_USER_EXPECTED_KEYS = ["name", "job", "updatedAt"]

USER_EXPECTED_KEYS = ["id", "email", "first_name", "last_name", "avatar"]

RESOURCE_EXPECTED_KEYS = ["id", "name", "year", "color", "pantone_value"]
