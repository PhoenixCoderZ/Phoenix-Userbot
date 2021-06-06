import os


class Config:
    LOGGER = True
    APP_ID = int(os.environ.get("APP_ID", 123456))
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MAX_MESSAGE_LENGTH = 4096
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", ".")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get(
        "TMP_DOWNLOAD_DIRECTORY", "/root/toxic/downloads/"
    )
    OFFICIAL_UPSTREAM_REPO = os.environ.get(
        "OFFICIAL_UPSTREAM_REPO", "https://github.com/Khush-Botz/Toxic-Userbot.git"
    )
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    OWNER_NAME = os.environ.get("OWNER_NAME", "")
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID"))
    PM_PERMIT = bool(os.environ.get("PM_PERMIT", False))
    REMBG_API_KEY = os.environ.get("REMBG_API_KEY", None)

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
