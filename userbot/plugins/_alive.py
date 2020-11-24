# Plugin Made By @Anonymous_Machinee
# kang with Credits
# Dont Remove This Lines
# (C) Phantom Userbot

import asyncio
import os
import random
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.errors import ChatSendMediaForbiddenError
from userbot import ALIVE_NAME
from userbot import ALIVE_PIC, SUDO_ALIVE_PIC
from userbot.utils import phantom_cmd, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PHANTOM USER"

PHANTOM_PIC="https://telegra.ph/file/ecb974be110f8141e861d.jpg"

if ALIVE_PIC is None:
    ALIVE_PIC=PHANTOM_PIC
else:
    ALIVE_PIC=ALIVE_PIC
    
if SUDO_ALIVE_PIC is None:
    SUDO_ALIVE_PIC = ALIVE_PIC
else:
    SUDO_ALIVE_PIC = SUDO_ALIVE_PIC
    

alive_caption = "**PHANTOM UB IS ONLINE**\n"
alive_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
alive_caption += "🤖 **SYSTEM INFO** 🤖\n"
alive_caption += "**ᴜsᴇʀʙᴏᴛ - ᴠᴇʀsɪᴏɴ------>> 0.4**\n"
alive_caption += "**ᴛᴇʟᴇᴛʜᴏɴ - ᴠᴇʀsɪᴏɴ ----> 1.17.0**\n"
alive_caption += "**ᴘʏᴛʜᴏɴ -  ᴠᴇʀsɪᴏɴ ------> 3.8.6**\n\n"
alive_caption += "**🌀 SUPPORT INFO 🌀**\n"
alive_caption += "**sᴜᴘᴘᴏʀᴛ - ᴄʜᴀɴɴᴇʟ ---->** [PhantomOt](https://t.me/PhantomOt)\n"
alive_caption += "**sᴜᴘᴘᴏʀᴛ - ɢʀᴏᴜᴘ =** [PhantomSupport](https://t.me/PhantomSupport)\n\n"
alive_caption += f"**[❤️ Create your own PHANTOM USERBOT ❤️](https://dashboard.heroku.com/new?template=https://github.com/prothinkergang/Phantomuserbot)**"

medianotallowed = (
    "**PHANTOM UB IS ONLINE**\n"
    "\n**🌀 Current Stats 🌀\n**"
    f"**My Master** => **{DEFAULTUSER}**\n"
    "**ᴜsᴇʀʙᴏᴛ - ᴠᴇʀsɪᴏɴ------>> 0.4**\n"
    "**ᴘʏᴛʜᴏɴ -  ᴠᴇʀsɪᴏɴ ------> 3.8.6**\n"
    "**sᴜᴘᴘᴏʀᴛ - ᴄʜᴀɴɴᴇʟ ---->** [PhantomOt](https://t.me/PhantomOt)\n"
    "\n**[❤️Deploy Your Own Phantom Userbot ❤️](https://dashboard.heroku.com/new?template=https://github.com/prothinkergang/Phantomuserbot)**"
)
                   
                   

@borg.on(phantom_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    try:
         await borg.send_file(alive.chat_id, file=ALIVE_PIC, caption=alive_caption)
         await alive.delete()
    except ChatSendMediaForbiddenError:
    	await alive.edit(medianotallowed)
 #Phantomot


@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def sudoalivepic(sudoalive):
    chat = await sudoalive.get_chat()
    """ For .alive command, check if the bot is running.  """
    try:
         await borg.send_file(sudoalive.chat_id, file=SUDO_ALIVE_PIC, caption=alive_caption)
         await sudoalive.delete()
    except ChatSendMediaForbiddenError:
    	await sudoalive.edit(medianotallowed)
    
