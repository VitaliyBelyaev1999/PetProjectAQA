import requests
import allure

BASE_URL = "https://reqres.in/api"

# Бесплатный API ключ, предоставляемый ReqRes всем пользователям
API_KEY = "reqres-free-v1"

# Заголовок с ключом, который будет использоваться во всех запросах
headers = {
    "x-api-key": API_KEY
}

@allure.feature('Public Resources')
@allure.story('Get Resource List')
def test_get_list_of_unknown_resources():
    """
    Тест для проверки получения списка ресурсов с использованием бесплатного API ключа.
    """
    endpoint = "/unknown"
    
    with allure.step(f"Отправляем GET-запрос на {BASE_URL}{endpoint} с API ключом"):
        response = requests.get(url=f"{BASE_URL}{endpoint}", headers=headers)

    with allure.step("Проверяем, что статус-код ответа - 200"):
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    with allure.step("Проверяем, что в ответе есть данные"):
        response_json = response.json()
        assert "data" in response_json
        assert isinstance(response_json['data'], list)
        print("\n✅ Тест /api/unknown успешно пройден! Статус-код 200 получен.")


@allure.feature('Users')
@allure.story('Get User List')
def test_get_list_users():
    """
    Тест для проверки получения списка пользователей со второй страницы.
    """
    endpoint = "/users"
    params = {"page": 2}
    
    with allure.step(f"Отправляем GET-запрос на {BASE_URL}{endpoint} с API ключом"):
        response = requests.get(url=f"{BASE_URL}{endpoint}", params=params, headers=headers)

    with allure.step("Проверяем, что статус-код ответа - 200"):
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

    with allure.step("Проверяем тело ответа"):
        response_json = response.json()
        assert "data" in response_json, "В ответе отсутствует ключ data"
        assert isinstance(response_json['data'], list), "Ключ data не является списком"
        assert response_json['page'] == params['page'], f"Номер страницы не совпадает"
        print("\n✅ Тест /api/users успешно пройден! Данные пользователей получены.")

