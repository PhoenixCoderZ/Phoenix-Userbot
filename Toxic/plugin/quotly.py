import asyncio
import random
from asyncio import sleep
from pyrogram import filters, Client
from pyrogram.types import Message
from Toxic import cmd


@Client.on_message(cmd(["q"]))
async def quotly(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Reply to any users text message")
        return
    await message.edit("```Making a Quote```")
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            msg = await client.get_history("@QuotLyBot", 1)
            is_sticker = True
        except:
            await sleep(0.5)
            progress += random.randint(0, 10)
            try:
                await message.edit("```Making a Quote```\nProcessing {}%".format(progress))
            except:
                await message.edit("ERROR SUUUU")
    if msg_id := msg[0]['message_id']:
        await asyncio.gather(
            message.delete(),
            client.forward_messages(message.chat.id,"@QuotLyBot", msg_id)
        )


# Command help section
add_command_help(
    'quotly', [
        ['.q | .quote', 'Make a quote with reply to message.'],
    ]
)
