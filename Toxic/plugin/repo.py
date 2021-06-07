from pyrogram import Client, filters
from pyrogram.types import Message
from functools import partial as cmd
from toxic import cmd


@Client.on_message(cmd("repo"))
async def repo(client: Client, message: Message):
    await message.edit(f'''<b>---THE TOXIC USERBOT---
• ToXic Is AlIVe
• License: GNU GPL v3.0
• <a href="https://t.me/ToxicUb_Support">SUPPORT</a>
• <a href="https://github.com/Khush-Botz/Toxic-Userbot">GITHUB</a>
• ToXic UB: Made With Lub❤️</b>''')

