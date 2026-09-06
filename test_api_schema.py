# test_api_schema.py - Enterprise JSON Schema Contract Validation

import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

# API కాంట్రాక్ట్ రూల్స్ (Schema Blueprint)
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"}
            },
            "required": ["city", "street"]
        }
    },
    # రెస్పాన్స్‌లో తప్పనిసరిగా ఉండాల్సిన కీలు (Mandatory Contract Fields)
    "required": ["id", "name", "username", "email"]
}

def test_user_api_schema_contract():
    # 1. API కాల్ చేయడం
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200, "API request failed"

    # 2. JSON పేలోడ్ స్కీమా కాంట్రాక్ట్‌కు సరిపోతుందో లేదో వాలిడేట్ చేయడం
    payload = response.json()
    
    # స్కీమా నిబంధనలు తప్పితే ఇది ValidationError ను రైజ్ చేస్తుంది
    validate(instance=payload, schema=USER_SCHEMA)
    print("\n[Contract Verified] API response strictly adheres to the JSON Schema!")