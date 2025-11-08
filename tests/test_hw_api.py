import pytest
import logging
import requests

BASE_URL = "https://reqres.in/api"

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def api_headers():
    return {"x-api-key": "reqres-free-v1"}


@pytest.fixture(autouse=True)
def setup_and_teardown():
    logging.info("SETUP")
    yield
    logging.info("TEARDOWN")    


@pytest.mark.parametrize("page", [1, 2, 3, 9999])
def test_check_pages(api_headers, page):
    response = requests.get(f"{BASE_URL}/users?page={page}", headers=api_headers)
    data = response.json()
    logging.info(f"answer length = {len(data)}")
    logging.info(f"status code = {response.status_code}")
    assert "data" in data, "key 'data' not found"
    assert "page" in data, "key 'page' not found"


def test_wrong_status():
    response = requests.get(f"{BASE_URL}/users?page={2}")

    data = response.json()
    logging.info(f"answer body: {data}")
    logging.info(f"status code = {response.status_code}")
    assert response.status_code == 200, "status code is not 200"

