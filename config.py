import os
from typing import List

# ────────────────────────────────🔐 API CREDENTIALS ────────────────────────────────

API_ID: int = int(os.environ.get("API_ID", "23889992"))
API_HASH: str = os.environ.get("API_HASH", "70bf3c9baebf30afff8c32649bf23c3d")
BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")

# 😃 Telegram Owner ID
ADMIN: int = int(os.environ.get("ADMIN", "1900118264"))

# ───────────────────────────────📊 DATABASE SETTINGS ───────────────────────────────

DB_URI: str = os.environ.get("DB_URI", "mongodb+srv://HDMoviesEarth:unqOY8gUrmDLNXHd@cluster0.0xjypxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME: str = os.environ.get("DB_NAME", "HDMoviesEarth")

# ───────────────────────────────📡 LOGGING AND CHANNELS ─────────────────────────────

# 🔔 Channel where logs or join messages will be sent
LOG_CHANNEL: int = int(os.environ.get("LOG_CHANNEL", "-1002645203047"))

# 🔐 Force Subscription Feature (True/False)
IS_FSUB: bool = os.environ.get("IS_FSUB", "False").lower() == "true"

# ✅ List of Allowed Channel IDs for Usage
AUTH_CHANNELS: List[int] = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001943817170").split()))

# ─────────────────────────👑 (MR Ankan) 👑───────────────────────────
# 🟢 Linktree - https://linktr.ee/diesen_gaming
# 🗿 UHD Official - https://uhd-official.vercel.app/
# 👑 MR Ankan - https://t.me/Ankan_Contact_Bot
# 🤖 UHD Bots - https://t.me/UHD_Bots
# ─────────────────────────────────────────────────────────────────────────────────────
