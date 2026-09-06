# test_login_pom.py - ఆర్కిటెక్చర్ లెవల్ క్లీన్ టెస్ట్ సూట్

import pytest
from playwright.sync_api import expect
from login_page import LoginPage

LOGIN_DATA_MATRIX = [
    ("satya_architect", "EnterprisePass2026", "Welcome Back, Principal Architect!"),
    ("satya_architect", "WrongPassword999", "Access Denied: Invalid Credentials"),
    ("unknown_hacker", "EnterprisePass2026", "Access Denied: Invalid Credentials"),
    ("", "", "Access Denied: Invalid Credentials"),
]

@pytest.mark.parametrize("username, password, expected_message", LOGIN_DATA_MATRIX)
def test_login_scenarios_clean(login_page: LoginPage, username: str, password: str, expected_message: str):
    # conftest.py నుండి login_page ఆటోమేటిక్‌గా ఇంజెక్ట్ అయ్యింది
    login_page.load()
    login_page.login(username, password)

    # వాలిడేషన్
    expect(login_page.flash_banner).to_be_visible()
    expect(login_page.flash_banner).to_contain_text(expected_message)