# test_api_negative.py - Parametrized Negative & Fault Injection Suite

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# వివిధ నెగటివ్ సినారియోల టెస్ట్ డేటా మ్యాట్రిక్స్
negative_test_data = [
    # (scenario_name, endpoint, method, payload, headers, expected_status)
    (
        "Invalid Resource ID",
        f"{BASE_URL}/users/0",
        "GET",
        None,
        {},
        404
    ),
    (
        "Malformed Resource ID",
        f"{BASE_URL}/users/invalid_id",
        "GET",
        None,
        {},
        404
    )
]

@pytest.mark.parametrize("scenario, endpoint, method, payload, headers, expected_status", negative_test_data)
def test_api_negative_scenarios(scenario, endpoint, method, payload, headers, expected_status):
    # రిక్వెస్ట్ మెథడ్ ఆధారంగా డైనమిక్ కాల్ చేయడం
    if method == "GET":
        response = requests.get(endpoint, headers=headers)
    elif method == "POST":
        response = requests.post(endpoint, json=payload, headers=headers)

    # నెగటివ్ స్టేటస్ కోడ్ వాలిడేషన్
    assert response.status_code == expected_status, (
        f"Failed [{scenario}]: Expected {expected_status}, but received {response.status_code}"
    )