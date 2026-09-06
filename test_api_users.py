# test_api_users.py - Complete Enterprise REST API CRUD Test Suite

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_by_id_success():
    # 1. GET రిక్వెస్ట్ పంపడం
    response = requests.get(f"{BASE_URL}/users/1")

    # 2. హెచ్‌టీటీపీ స్టేటస్ కోడ్ వాలిడేషన్ (200 OK)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    # 3. కంటెంట్-టైప్ హెడర్ వాలిడేషన్
    assert "application/json" in response.headers["Content-Type"], "Response is not JSON"

    # 4. JSON రెస్పాన్స్ బాడీ వాలిడేషన్
    user_data = response.json()
    assert user_data["id"] == 1, "User ID does not match"
    assert "name" in user_data, "Missing 'name' field in payload"
    assert "email" in user_data, "Missing 'email' field in payload"
    assert user_data["username"] == "Bret", f"Unexpected username: {user_data['username']}"

def test_get_non_existent_user_returns_404():
    # ఉనికిలో లేని యూజర్ కోసం నెగటివ్ టెస్ట్ (404 Not Found)
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404, f"Expected 404 for invalid user, got {response.status_code}"

def test_create_user_post_success():
    # కొత్త యూజర్ డేటా పేలోడ్ (POST - 201 Created)
    new_user_payload = {
        "name": "Satya Architect",
        "username": "satya_arch",
        "email": "satya@enterprise.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=new_user_payload)
    assert response.status_code == 201, f"Expected 201 Created, but got {response.status_code}"

    created_data = response.json()
    assert created_data["name"] == new_user_payload["name"], "Created user name mismatch"
    assert created_data["username"] == new_user_payload["username"], "Username mismatch"
    assert "id" in created_data, "Server did not return a generated ID"

def test_update_user_put_success():
    # యూజర్ డేటా అప్‌డేట్ పేలోడ్ (PUT - 200 OK)
    update_payload = {
        "name": "Satya Principal Architect",
        "username": "satya_arch",
        "email": "satya_lead@enterprise.com"
    }

    response = requests.put(f"{BASE_URL}/users/1", json=update_payload)
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"

    updated_data = response.json()
    assert updated_data["name"] == update_payload["name"], "Updated name does not match"
    assert updated_data["email"] == update_payload["email"], "Updated email does not match"

def test_delete_user_success():
    # యూజర్ డిలీట్ రిక్వెస్ట్ (DELETE - 200 OK)
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 200, f"Expected 200 OK for delete, but got {response.status_code}"