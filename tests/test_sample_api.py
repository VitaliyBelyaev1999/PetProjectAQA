import requests
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BASE_URL = "https://reqres.in/api"

headers = { "x-api-key": "reqres-free-v1" }

def test_get_list_users():
    response = requests.get(f"{BASE_URL}/users?page=2", headers=headers)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()

    # Логируем данные через логгер
    logger.info(f"Response data: {data}")

    assert "data" in data, "Response JSON missing 'data' key"
    assert isinstance(data["data"], list), "'data' is not a list"

