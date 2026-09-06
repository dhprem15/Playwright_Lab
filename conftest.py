import pytest
from playwright.sync_api import Page
from login_page import LoginPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)