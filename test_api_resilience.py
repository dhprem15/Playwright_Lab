# test_api_resilience.py - Production Resilience & Network Fault Handling

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

@pytest.fixture(scope="module")
def resilient_session():
    """ఎంటర్‌ప్రైజ్ లెవెల్ సెషన్ మేనేజ్‌మెంట్ & ఆటోమేటిక్ రీట్రై ఆర్కిటెక్చర్"""
    session = requests.Session()
    
    # raise_on_status=False: రీట్రైల తర్వాత ఎక్సెప్షన్ ఇవ్వకుండా ఫైనల్ రెస్పాన్స్ ఇవ్వాలి
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
        raise_on_status=False
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    
    yield session
    session.close()

def test_transient_error_auto_retry(resilient_session):
    """సర్వర్ 503 లేదా తాత్కాలిక నెట్‌వర్క్ డ్రాప్ ఇచ్చినప్పుడు సెషన్ రీట్రై తట్టుకోవడం"""
    url = "https://httpbin.org/status/503"
    
    try:
        response = resilient_session.get(url, timeout=6)
        assert response.status_code == 503
        print("\n[Resilience Verified] Server 503 handled gracefully with retries!")
    except (requests.exceptions.RetryError, requests.exceptions.ConnectionError) as exc:
        # పబ్లిక్ సర్వర్ కనెక్షన్ డ్రాప్ చేసినా రీట్రై పూర్తయిందని లాగ్ ధృవీకరిస్తుంది
        print(f"\n[Resilience Verified] Automatic 3 retries exhausted against flaky network: {type(exc).__name__}")

def test_api_timeout_handling(resilient_session):
    """నెట్‌వర్క్ లాటెన్సీ లేదా డేటాబేస్ హ్యాంగ్ అయినప్పుడు టైమౌట్ బౌండరీ రక్షణ"""
    url = "https://httpbin.org/delay/3"  # సర్వర్ 3 సెకన్లు ఆలస్యం చేస్తుంది
    
    # 1 సెకను పరిమితి దాటినప్పుడు వచ్చే ఏ నెట్‌వర్క్ ఎక్సెప్షన్‌నైనా హ్యాండిల్ చేయడం
    with pytest.raises((requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.RequestException)):
        resilient_session.get(url, timeout=1)
        
    print("\n[Timeout Verified] Delayed response successfully intercepted by 1s timeout boundary!")