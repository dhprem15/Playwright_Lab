# login_page.py - పేజీ మేనేజర్ (కేవలం లొకేటర్లు మరియు యాక్షన్లు మాత్రమే)

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Enterprise Secure Login</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0f172a; color: #f8fafc; padding: 50px; }
        .login-box { background: #1e293b; padding: 30px; border-radius: 8px; width: 350px; margin: auto; }
        input { width: 100%; padding: 10px; margin: 10px 0; border-radius: 4px; border: 1px solid #475569; background: #020617; color: white; box-sizing: border-box; }
        button { width: 100%; background: #2563eb; color: white; border: none; padding: 12px; border-radius: 4px; font-weight: bold; cursor: pointer; margin-top: 10px; }
        .banner { margin-top: 15px; padding: 10px; border-radius: 4px; font-size: 14px; text-align: center; }
        .success { background: #16a34a; color: white; }
        .error { background: #dc2626; color: white; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>System Login</h2>
        <input id="username" type="text" placeholder="Username" />
        <input id="password" type="password" placeholder="Password" />
        <button id="login-btn" onclick="handleLogin()">Sign In</button>
        <div id="flash-banner" class="banner" style="display: none;"></div>
    </div>

    <script>
        function handleLogin() {
            const u = document.getElementById('username').value;
            const p = document.getElementById('password').value;
            const b = document.getElementById('flash-banner');
            b.style.display = 'block';

            if (u === 'satya_architect' && p === 'EnterprisePass2026') {
                b.className = 'banner success';
                b.innerText = 'Welcome Back, Principal Architect!';
            } else {
                b.className = 'banner error';
                b.innerText = 'Access Denied: Invalid Credentials';
            }
        }
    </script>
</body>
</html>
"""

class LoginPage:
    def __init__(self, page):
        self.page = page
        # 1. ఎలిమెంట్ లొకేటర్లు
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-btn")
        self.flash_banner = page.locator("#flash-banner")

    # 2. పేజీ లోడింగ్ యాక్షన్
    def load(self):
        self.page.set_content(LOGIN_HTML)

    # 3. లాగిన్ యాక్షన్ మెథడ్
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()