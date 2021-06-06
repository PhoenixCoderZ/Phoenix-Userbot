from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('repo', ['.']) & filters.me)
async def repo(client: Client, message: Message):
    await message.edit(f'''<b>---THE TOXIC USERBOT---
• UserboT Is AlIVe
• License: GNU GPL v3.0
• <a href="https://t.me/ToxicUb_Support">SUPPORT</a>
• <a href="https://github.com/Khush-Botz/Toxic-Userbot">GITHUB</a>
</b>''')


utils.modules_help.update({'repo': '''repo - Userbot information''', 'repo module': 'Repo: repo'})
