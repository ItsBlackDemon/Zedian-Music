## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8187557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce1587ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Hiro")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Owo_hiro")
ALIVE_NAME = getenv("ALIVE_NAME", "Zedian")
BOT_USERNAME = getenv("BOT_USERNAME", "Zedianmusicbot")
OWNER_ID = getenv("OWNER_ID", "5432629190")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zedian_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Zedian_project")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Zedian_Updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5432629190").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/494a436c45bee5ba18630.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/494a436c45bee5ba18630.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ItsBlackDeomn/Zedian-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
