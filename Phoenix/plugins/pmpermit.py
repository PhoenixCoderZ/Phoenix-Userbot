#Original Plugin Don't Change Anything 
#Credits of Team Phoinex 

from pyrogram import filters
from pyrogram.types import Message
from Phoenix import Phoenix


 from pyrogram.errors import FloodWait
 from Phoenix.plugins.help import add_command_help
 from Phoenix.database.pmpermit import PmPermit
 from time import sleep




@Phoenix.on_message(filters.command("pmpermit", ".") & filters.me)
async def pm_permit_enable(_, message: Message):
    await message.delete()


 UNAPPROVED_MSG = (
     "`Hi! I'm Phoenix Userbot bot.\n\n`"
     "`My master hasn't approved you to PM.\n`"
     "`Wait for My Master to approve `"
 )

 @Phoenix.on_message(filters.private & ~Filters.me)
 async def incoming_pm(_, message: Message):
     if PM_PERMIT:
         approved = PmPermit().check_if_approved(message.chat.id)
         warned = PmPermit().check_if_warned(message.chat.id)
         force_blocked = PmPermit().check_if_force_blocked(message.chat.id)

         if approved:
             return
         elif not approved and not warned:
             await message.reply(UNAPPROVED_MSG)
             PmPermit().warn(message.chat.id)
             PmPermit().increment_retard_level(message.chat.id)
         elif not approved and warned and not force_blocked:
             if PmPermit().calculate_retard_level(message.chat.id) >= PM_LIMIT:
                 await message.reply("You have been blocked for being a spamy retard.")
                 dialogs = [x async for x in bot.iter_dialogs()]
                 for dialog in dialogs:
                     if dialog.chat.id == message.chat.id:
                         await Phoenix.block_user(message.chat.id)
                         history = [x async for x in bot.iter_history(message.chat.id, reverse=True)]
                         message_ids = [x.message_id for x in history]
                         for item in history:
                             try:
                                 await UserBot.delete_messages(chat_id=message.chat.id, message_ids=[item.message_id])
                                 sleep(0.3)
                             except FloodWait as e:
                                 sleep(e.x)
             else:
                 PmPermit().increment_retard_level(message.chat.id)


 @Phoenix.on_message(filters.private & filters.me)
 async def auto_approve_user_on_message(_, message: Message):
     PmPermit().approve(message.chat.id)


 @Phoenix.on_message(filters.command('approve', '.') & filters.me)
 async def approve(_, message: Message):
     PmPermit().approve(message.chat.id)
     await message.edit("You have been approved to PM me. Please continue on with your story.")
     sleep(3)
     await message.delete()


 @Phoenix.on_message(filters.command('block', '.') & filters.me)
 async def block(_, message: Message):
     PmPermit().block_pm(message.chat.id)
     await message.edit("`You have been blocked. Sad day for you.`")
     await Phoenix().block_user(message.chat.id)


 if PM_PERMIT:
     add_command_help(
         'pmpermit',
         [
             ['.approve', "Approves the current chat to PM.\nUsage: `.approve`"],
             ['.block', "Blocks the current chat to PM.\nUsage: `.block`"],
         ]
     )
