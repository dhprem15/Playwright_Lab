# test_network_mock.py - Playwright Network Interception & UI Fault Injection

import pytest
from playwright.sync_api import Page, expect

def test_mock_api_success_payload(page: Page):
    """సినారియో 1: బ్యాకెండ్ API రెస్పాన్స్‌ను మాక్ చేసి కస్టమ్ డేటాను UI లో ఇంజెక్ట్ చేయడం"""
    
    # 1. API నెట్‌వర్క్ కాల్‌ను మధ్యలోనే అడ్డుకోవడం (Interception)
    def handle_route(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"userId": 1, "id": 1, "title": "ARCHITECT LEVEL MOCKED TITLE", "completed": false}'
        )
    
    page.route("**/todos/1", handle_route)
    
    # 2. అప్లికేషన్ పేజీకి వెళ్లడం
    page.goto("https://jsonplaceholder.typicode.com/")
    
    # 3. బ్రౌజర్ నుండి ఆ API కాల్ జరిపి మాక్ డేటా వచ్చిందో లేదో ధృవీకరించడం
    response = page.evaluate("""async () => {
        const res = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        return await res.json();
    }""")
    
    assert response["title"] == "ARCHITECT LEVEL MOCKED TITLE"
    print("\n[Mocking Verified] Browser received intercepted custom payload seamlessly!")

def test_inject_server_500_fault(page: Page):
    """సినారియో 2: బ్యాకెండ్ 500 సర్వర్ ఎర్రర్ ఇచ్చినప్పుడు UI స్థితిని పరీక్షించే ఫాల్ట్ ఇంజెక్షన్"""
    
    # సర్వర్ 500 Internal Server Error ఇచ్చినట్లు అడ్డుకోవడం
    page.route("**/todos/1", lambda route: route.fulfill(
        status=500,
        content_type="application/json",
        body='{"error": "Internal Server Crash Simulated"}'
    ))
    
    page.goto("https://jsonplaceholder.typicode.com/")
    
    # బ్రౌజర్‌లో API రెస్పాన్స్ స్టేటస్‌ను రికార్డ్ చేయడం
    status_code = page.evaluate("""async () => {
        const res = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        return res.status;
    }""")
    
    # 500 ఎర్రర్ వచ్చినప్పుడు సిస్టమ్ హ్యాండిల్ చేసిందా లేదా నిర్ధారించడం
    assert status_code == 500
    print("\n[Fault Injection Verified] 500 Internal Server Error successfully simulated in browser!")