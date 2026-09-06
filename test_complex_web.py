# test_complex_web.py - Enterprise iFrame & Shadow DOM Automation Suite

import pytest
from playwright.sync_api import Page, expect

def test_handle_isolated_iframe(page: Page):
    """సినారియో 1: బ్యాంకింగ్ గేట్‌వే తరహా ఐఫ్రేమ్ (iFrame) లోపల డేటాను ఇన్పుట్ చేయడం"""
    
    # ఐఫ్రేమ్ కలిగిన డైనమిక్ వెబ్ పేజీని బ్రౌజర్‌లో లోడ్ చేయడం
    html_content = """
    <html>
        <body>
            <h2>Enterprise Payment Portal</h2>
            <iframe id="payment-frame" srcdoc="
                <html>
                    <body>
                        <label for='card'>Secure Card Input:</label>
                        <input type='text' id='card' placeholder='Enter 16-digit card'>
                        <button id='pay-btn'>Submit Payment</button>
                    </body>
                </html>
            "></iframe>
        </body>
    </html>
    """
    page.set_content(html_content)
    
    # ప్లేరైట్ frame_locator ద్వారా ఐఫ్రేమ్ లోపలికి ప్రవేశించడం
    payment_frame = page.frame_locator("#payment-frame")
    
    # ఫ్రేమ్ లోపల ఉన్న కార్డ్ నంబర్ ఫీల్డ్‌లో డేటా ఎంటర్ చేయడం
    card_input = payment_frame.locator("#card")
    card_input.fill("4111222233334444")
    
    # బటన్ క్లిక్ చేయడం మరియు వాల్యూ నిర్ధారణ
    payment_frame.locator("#pay-btn").click()
    expect(card_input).to_have_value("4111222233334444")
    print("\n[iFrame Verified] Successfully pierced iFrame boundary and submitted data!")

def test_handle_shadow_dom_components(page: Page):
    """సినారియో 2: షాడో డామ్ (Shadow DOM / Web Components) లో దాగి ఉన్న ఎలిమెంట్లను ఆటోమేట్ చేయడం"""
    
    # షాడో రూట్ కలిగిన ఆధునిక వెబ్ కాంపోనెంట్ పేజీని లోడ్ చేయడం
    html_content = """
    <html>
        <body>
            <h2>Custom Enterprise Web Components</h2>
            <div id='host-element'></div>
            <script>
                const host = document.querySelector('#host-element');
                const shadowRoot = host.attachShadow({mode: 'open'});
                shadowRoot.innerHTML = `
                    <div class='shadow-container'>
                        <input type='text' id='shadow-search' placeholder='Shadow Search Box'>
                        <span id='shadow-status'>Ready</span>
                    </div>
                `;
            </script>
        </body>
    </html>
    """
    page.set_content(html_content)
    
    # ప్లేరైట్ ఆటోమేటిక్‌గా షాడో బౌండరీని చేధించి ఎలిమెంట్‌ను గుర్తిస్తుంది
    shadow_input = page.locator("#shadow-search")
    shadow_input.fill("Architect Level Automation")
    
    expect(shadow_input).to_have_value("Architect Level Automation")
    print("\n[Shadow DOM Verified] Playwright pierced shadow boundary natively without boilerplate!")