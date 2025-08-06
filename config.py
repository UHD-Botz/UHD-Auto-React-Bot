import os
from typing import List

# ─────────────────────🔐 API CREDENTIALS ─────────────────────

API_ID: int = int(os.environ.get("API_ID", ""))
API_HASH: str = os.environ.get("API_HASH", "")
BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")

# 👤 Telegram Owner ID
ADMIN: int = int(os.environ.get("ADMIN", ""))

# ─────────────────────📊 DATABASE SETTINGS ─────────────────────

DB_URI: str = os.environ.get("DB_URI", "")
DB_NAME: str = os.environ.get("DB_NAME", "")

# ─────────────────────📡 LOGGING AND CHANNELS ─────────────────────

LOG_CHANNEL: int = int(os.environ.get("LOG_CHANNEL", ""))
IS_FSUB: bool = os.environ.get("IS_FSUB", "False").lower() == "true"

AUTH_CHANNELS: List[int] = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
