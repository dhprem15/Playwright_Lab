import os
from dotenv import load_dotenv

# ప్రాజెక్ట్ రూట్ నుండి .env వేరియబుల్స్‌ను లోడ్ చేస్తుంది
load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://reqres.in")
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10000))
    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

# సింగిల్టన్ ఆబ్జెక్ట్
config = Config()