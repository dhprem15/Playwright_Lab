import json
from playwright.sync_api import Page, expect

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Server Dynamic Interception</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; }
        .card { background: #1e293b; padding: 25px; border-radius: 10px; max-width: 650px; margin: auto; }
        button { background: #16a34a; color: white; border: none; padding: 12px 24px; font-size: 15px; border-radius: 6px; cursor: pointer; font-weight: bold; margin-bottom: 20px; }
        pre { background: #020617; padding: 15px; border-radius: 6px; color: #4ade80; font-family: Consolas, monospace; font-size: 14px; border: 1px solid #334155; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Live API Response Interceptor</h2>
        <button id="get-data-btn" onclick="fetchLiveProfile()">Fetch Real Server User</button>
        <pre id="output-profile">Waiting for server call...</pre>
    </div>

    <script>
        async function fetchLiveProfile() {
            try {
                const res = await fetch('https://jsonplaceholder.typicode.com/users/1');
                const data = await res.json();
                document.getElementById('output-profile').innerText = JSON.stringify(data, null, 2);
            } catch (err) {
                console.error('JS FETCH ERROR:', err.message);
                document.getElementById('output-profile').innerText = 'ERROR: ' + err.message;
            }
        }
    </script>
</body>
</html>
"""

def test_dynamic_response_interception(page: Page):
    # బ్రౌజర్‌లో ఏదైనా ఎర్రర్ వస్తే టెర్మినల్‌లో ప్రింట్ చేసే సెటప్
    page.on("console", lambda msg: print(f"---> [BROWSER CONSOLE]: {msg.text}"))

    def intercept_and_modify(route):
        try:
            # 1. అసలు సర్వర్ నుంచి లైవ్ రెస్పాన్స్ తెచ్చుకుంటున్నాం
            response = route.fetch()
            data = response.json()

            print(f"\n---> [ORIGINAL SERVER NAME]: {data.get('name')}")

            # 2. పేరును మన పేరుతో రీప్లేస్ చేస్తున్నాం
            data["name"] = "Satya (Enterprise Architect)"

            print(f"---> [MODIFIED MOCKED NAME]: {data.get('name')}")

            # 3. పాత content-length ని తీసేసి కొత్త బాడీని పంపుతున్నాం
            headers = response.headers
            headers.pop("content-length", None)

            route.fulfill(
                status=response.status,
                headers=headers,
                body=json.dumps(data)
            )
        except Exception as e:
            print(f"\n---> [INTERCEPT ERROR]: {str(e)}\n")
            route.abort()

    # నెట్‌వర్క్ రూట్
    page.route("https://jsonplaceholder.typicode.com/users/1", intercept_and_modify)

    # పేజీ లోడ్ & బటన్ క్లిక్
    page.set_content(HTML_PAGE)
    page.locator("#get-data-btn").click()

    # అసెర్షన్లు
    output_box = page.locator("#output-profile")
    expect(output_box).to_contain_text("Satya (Enterprise Architect)")
    expect(output_box).to_contain_text("Sincere@april.biz")

    page.wait_for_timeout(4000)