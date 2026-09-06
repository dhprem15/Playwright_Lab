from playwright.sync_api import Page, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    def click_element(self, locator: Locator, timeout: float = 10000):
        locator.click(timeout=timeout)

    def enter_text(self, locator: Locator, text: str, timeout: float = 10000):
        locator.fill(text, timeout=timeout)

    def get_element_text(self, locator: Locator, timeout: float = 10000) -> str:
        return locator.text_content(timeout=timeout).strip()