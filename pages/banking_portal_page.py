from playwright.sync_api import Page
from pages.base_page import BasePage

class BankingPortalPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.frame_container = self.page.frame_locator("#payment-frame")
        self.card_number_input = self.frame_container.locator("#cc-number")
        self.submit_payment_button = self.frame_container.locator("#pay-now")
        self.shadow_status_badge = self.page.locator("banking-status-panel .status-verified")

    def complete_secure_payment(self, card_number: str):
        self.enter_text(self.card_number_input, card_number)
        self.click_element(self.submit_payment_button)

    def get_verification_status(self) -> str:
        return self.get_element_text(self.shadow_status_badge)