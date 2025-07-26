import os

API_ID = int(os.environ.get("API_ID", 1111111))
API_HASH = os.environ.get("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token_here")
OWNER_ID = os.environ.get("OWNER_ID", "11111111")

DATABASE_URL = os.environ.get("DATABASE_URL", "your_database_url_here")

AUTH_CHAT = [int(x) for x in os.environ.get("AUTH_CHAT", "-100123456789 -1001234567890").split()]
LOGS_CHAT = int(os.environ.get("LOGS_CHAT", "-1001234567891"))
POST_CHAT = int(os.environ.get("POST_CHAT", "-1001234567891"))

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "adminadmin")

SITE_SECRET = os.environ.get("SITE_SECRET", "your_secret_key")
TMDB_API_KEY = os.environ.get("TMDB_API_KEY", "")

MULTI_TOKENS = {}  # Load from env/json if needed
DELETE_AFTER_MINUTES = int(os.environ.get("DELETE_AFTER_MINUTES", 10))
POST_UPDATES = os.environ.get("POST_UPDATES", "True") == "True"
USE_CAPTION = os.environ.get("USE_CAPTION", "False") == "True"

PORT = int(os.environ.get("PORT", 6519))
