import requests

BASE_URL = "https://reqres.in/api"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204
