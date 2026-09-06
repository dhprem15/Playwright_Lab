import pytest
from playwright.sync_api import Page
from pages.banking_portal_page import BankingPortalPage

def test_secure_banking_transaction_pom(page: Page):
    banking_page = BankingPortalPage(page)
    
    html_content = """
    <!DOCTYPE html>
    <html>
        <body>
            <iframe id="payment-frame" srcdoc="
                <input id='cc-number' type='text' placeholder='Card Number'/>
                <button id='pay-now'>Pay</button>
            "></iframe>
            <banking-status-panel>
                <template shadowrootmode="open">
                    <div class="status-verified">TRANSACTION_SUCCESSFUL</div>
                </template>
            </banking-status-panel>
        </body>
    </html>
    """
    page.set_content(html_content)

    banking_page.complete_secure_payment("4532-8921-0012-9982")
    
    status = banking_page.get_verification_status()
    assert status == "TRANSACTION_SUCCESSFUL", f"Expected success status, but got {status}"
    print(f"\n[POM Execution Verified] Status extracted: {status}")