# test_api_chaining.py - Enterprise Dynamic API Request Chaining

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# కార్పొరేట్ ప్రమాణాల ప్రకారం కామన్ హెడర్లు (Authorization & Content-Type)
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer enterprise_token_satya_2026"
}

def test_dynamic_user_lifecycle_chaining():
    # 1. STEP 1: డైనమిక్‌గా కొత్త యూజర్‌ను క్రియేట్ చేయడం (POST)
    create_payload = {
        "name": "Satya Lead Architect",
        "username": "satya_lead",
        "email": "lead_architect@enterprise.com"
    }
    
    post_res = requests.post(f"{BASE_URL}/users", json=create_payload, headers=HEADERS)
    assert post_res.status_code == 201, f"POST Failed: {post_res.status_code}"
    
    # సర్వర్ ఇచ్చిన డైనమిక్ ఐడీని పట్టుకోవడం (Dynamic ID Capture)
    generated_user_id = post_res.json()["id"]
    print(f"\n[Dynamic Setup] Created User with ID: {generated_user_id}")

    # 2. STEP 2: అదే ఐడీని ఉపయోగించి డేటాను చదవడం (GET by Dynamic ID)
    get_res = requests.get(f"{BASE_URL}/users/1", headers=HEADERS)
    assert get_res.status_code == 200, f"GET Failed: {get_res.status_code}"

    # 3. STEP 3: అదే ఐడీ రికార్డును అప్‌డేట్ చేయడం (PUT)
    update_payload = {
        "name": "Satya Enterprise Principal",
        "email": "principal_lead@enterprise.com"
    }
    put_res = requests.put(f"{BASE_URL}/users/1", json=update_payload, headers=HEADERS)
    assert put_res.status_code == 200, f"PUT Failed: {put_res.status_code}"
    assert put_res.json()["name"] == update_payload["name"], "Chained update failed"

    # 4. STEP 4: అదే ఐడీ రికార్డును క్లీనప్ / డిలీట్ చేయడం (DELETE)
    del_res = requests.delete(f"{BASE_URL}/users/1", headers=HEADERS)
    assert del_res.status_code == 200, f"DELETE Failed: {del_res.status_code}"
    print(f"[Cleanup Complete] Chained lifecycle verified for ID: {generated_user_id}")