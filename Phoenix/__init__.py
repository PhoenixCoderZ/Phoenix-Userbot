import os
import importlib
from Phoenix.setclient import cmd
# the logging things
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


# Configuration Things
if bool(os.environ.get("ENV", False)):
    from Phoenix.sample_config import Config
else:
    from Phoenix.config import Development as Config


LOGGER = logging.getLogger(__name__)
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
COMMAND_HAND_LER = Config.COMMAND_HAND_LER
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH

# Ensure Directories
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.exists(TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(TMP_DOWNLOAD_DIRECTORY)

if not os.path.exists("Phoenix/cache"):
    os.makedirs("Phoenix/cache")

HEROKU_API_KEY = Config.HEROKU_API_KEY
OFFICIAL_UPSTREAM_REPO = Config.OFFICIAL_UPSTREAM_REPO
DATABASE_URL = Config.DATABASE_URL
SUDO_USERS = list(Config.SUDO_USERS)
TG_MAX_SELECT_LEN = Config.TG_MAX_SELECT_LEN
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
OWNER_ID = Config.OWNER_ID
OWNER_NAME = Config.OWNER_NAME
PRIVATE_GROUP_ID = Config.PRIVATE_GROUP_ID
PM_PERMIT = Config.PM_PERMIT
UB_VERSION = "v0.2"
REMBG_API_KEY = Config.REMBG_API_KEY
USERBOT_PREFIX = os.environ.get("CMD_HNDLR")
HELP_COMMANDS = {}


def load_cmds(ALL_PLUGINS):
    for oof in ALL_PLUGINS:
        if oof.lower() == "help":
            continue
        imported_module = importlib.import_module("Phoenix.plugins." + oof)
        if not hasattr(imported_module, "__PLUGIN__"):
            imported_module.__PLUGIN__ = imported_module.__name__

        if not imported_module.__PLUGIN__.lower() in HELP_COMMANDS:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one"
            )

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELP_COMMANDS[imported_module.__PLUGIN__.lower()] = imported_module.__help__
    return "Done Loading Plugins and Commands!"
