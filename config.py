
import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", default="DARK_RAVAN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default="6215534047:AAGC5JvFzG69CaJ9Q6u0vukFrpY5kxvlmm4")
BOT_TOKEN2 = getenv("BOT_TOKEN2", default="6568638985:AAGLbu9Cb35t-ZkDY0hqn6pSalw5QeHMNjg")
BOT_TOKEN3 = getenv("BOT_TOKEN3", default="6478217552:AAFEr7aZeesOyv-S821QZB9CkjAi7gyxuf4")
BOT_TOKEN4 = getenv("BOT_TOKEN4", default="6466925710:AAHI-7RXl2ff80vB6U0p4eb6EerHhPX-BFs")
BOT_TOKEN5 = getenv("BOT_TOKEN5", default="6518264121:AAF1MWRrFidfXZK9luI7FrG6UGOucW5nHr8")
BOT_TOKEN6 = getenv("BOT_TOKEN6", default="6459651344:AAEhKIELqkwrhfOdZMdDELhb-LkG8mOmsIQ")
BOT_TOKEN7 = getenv("BOT_TOKEN7", default="5852275658:AAGLTVIySLjNLmJvWTP0JXpS44wzqYod1VI")
BOT_TOKEN8 = getenv("BOT_TOKEN8", default="6680841962:AAFKYAMng1PkXGCEJ9OeaBqlXf8JX9gBBg0")
BOT_TOKEN9 = getenv("BOT_TOKEN9", default="6464222164:AAEnDpXNY-YVfcKFZQ8KrUKAWfcFW4NHOAY")
BOT_TOKEN10 = getenv("BOT_TOKEN10", default="6461908827:AAHOi9Ftp6DtDjO-gTzPGaF4fief1ZUq25I")

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6638057092").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5695560295")
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)


