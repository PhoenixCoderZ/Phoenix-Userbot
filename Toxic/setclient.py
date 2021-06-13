import os
from pyrogram.raw.all import layer
from Toxic.plugin import ALL_PLUGINS
from Toxic import APP_ID, API_HASH, STRING_SESSION, USERBOT_PREFIX, LOGGER
from pyrogram import Client, __version__

class Toxic(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            STRING_SESSION,
            plugins=dict(root=f"{name}/plugin"),
            workdir=f"{name}/session",
            api_id=APP_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        await super().start()
        LOGGER.info(
            f"THE Toxic Userbot based on Pyrogram V{__version__} "
            f"(Layer {layer}) started...\n"
        )

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("THE Toxic Userbot stopped. Bye.")
