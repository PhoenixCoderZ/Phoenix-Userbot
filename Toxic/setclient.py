from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from Toxic.plugins import ALL_PLUGINS
from Toxic import APP_ID, API_HASH, STRING_SESSION, LOGGER, load_cmds


class Toxic(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            STRING_SESSION,
            plugins=dict(root=f"{name}/plugins"),
            workdir=f"{name}/session",
            api_id=APP_ID,
            api_hash=API_HASH,
        )

    async def start(self):
        await super().start()
        result = load_cmds(ALL_PLUGINS)
        LOGGER.info(result)

        me = await self.get_me()
        LOGGER.info(
            f"THE Toxic Userbot based on Pyrogram v{__version__} "
            f"(Layer {layer}) started...\n"
            f"Hey {me.first_name}!"
        )

    async def stop(self, *args):
        await super().stop()
        LOGGER.info("THE Toxic Userbot stopped. Bye.")
