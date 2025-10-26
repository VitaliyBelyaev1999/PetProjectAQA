import requests
import allure
import pytest

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"
headers = {"x-api-key": API_KEY}

@allure.feature('Public Resources')
@allure.story('Get Resource List')
def test_get_list_of_unknown_resources():
    endpoint = "/unknown"
    
    with allure.step(f"Send GET request to {BASE_URL}{endpoint} with API key"):
        response = requests.get(url=f"{BASE_URL}{endpoint}", headers=headers)

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    with allure.step("Check response has data key and it is a list"):
        response_json = response.json()
        assert "data" in response_json
        assert isinstance(response_json['data'], list)


@allure.feature('Users')
@allure.story('Get User List')
def test_get_list_users():
    endpoint = "/users"
    params = {"page": 2}
    
    with allure.step(f"Send GET request to {BASE_URL}{endpoint} with params {params} and API key"):
        response = requests.get(url=f"{BASE_URL}{endpoint}", params=params, headers=headers)

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    with allure.step("Validate response body"):
        response_json = response.json()
        assert "data" in response_json, "Missing data key in response"
        assert isinstance(response_json['data'], list), "Data key is not a list"
        assert response_json['page'] == params['page'], "Page number mismatch"


@allure.feature("Users API")
@allure.story("Update user with PUT")
def test_update_user():
    endpoint = "/users/2"
    payload = {"name": "neo", "job": "chosen one"}

    with allure.step(f"Send PUT request to {BASE_URL}{endpoint}"):
        response = requests.put(f"{BASE_URL}{endpoint}", json=payload, headers=headers)

    with allure.step("Check that status code is 200"):
        assert response.status_code == 200

    with allure.step("Check fields in the answer"):
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]
        assert "updatedAt" in body


@allure.feature("Users API")
@allure.story("Delete user")
def test_delete_user():
    endpoint = "/users/2"

    with allure.step(f"Send DELETE request to {BASE_URL}{endpoint}"):
        response = requests.delete(f"{BASE_URL}{endpoint}", headers=headers)

    with allure.step("Check status code 204 (correct delete)"):
        assert response.status_code == 204


@pytest.mark.api
def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=headers)

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body
    assert "createdAt" in body

