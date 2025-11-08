import requests
import logging
import pytest

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api"


@pytest.fixture
def api_headers():
    return {"x-api-key": "reqres-free-v1"}


@pytest.fixture(autouse=True)
def setup_and_teardown():
    logging.debug(f"Setup")
    yield
    logging.debug(f"Teardown")


def test_get_list_users(api_headers):
    response = requests.get(f"{BASE_URL}/users?page=2", headers=api_headers)
    data = response.json()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert "data" in data, "Response JSON missing 'data' key"
    assert isinstance(data["data"], list), "'data' is not a list"


def test_check_page_key(api_headers):
    response = requests.get(f"{BASE_URL}/users?page=2", headers=api_headers)
    data = response.json()
    logging.debug(f"Response page: {data['page']}")
    assert "page" in data, "Response JSON missing 'page' key"
    assert data["page"] == 2, "page is not 2"
    assert "data" in data, "Response JSON missing 'data' key"
    

def test_get_nonexistent_page(api_headers):
    response = requests.get(f"{BASE_URL}/users?page=9999", headers=api_headers)
    data = response.json()
    logging.debug(f"Response for nonexistent page: {data}")
    assert response.status_code == 200, "Ожидается статус 200"
    assert "data" in data, "В ответе отсутствует ключ 'data'"
    assert isinstance(data["data"], list), "'data' не список"
    assert len(data["data"]) == 0, "Список пользователей должен быть пустым"

