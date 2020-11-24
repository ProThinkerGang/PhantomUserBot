#Inspired and Help Taken by Animesticker plugin("waifu" command)
# Plugin Made By @Anonymous_Machinee
# Kang With Credit
# (c) Phantom Userbot

## ALL IMPORTS ARE OF WAIFU PLUGIN (NO DELETION , ONLY ADDITION IN IMPORT)

from asyncio import sleep
from random import choice, getrandbits, randint
import re
from re import sub
from telethon import errors
import random
from os import execl
from telethon import events
from userbot import bot
import sys
import io
import html
from telethon.errors import ChatSendStickersForbiddenError
import json
from PIL import ImageEnhance, ImageOps
from userbot import CMD_HELP
from userbot.utils import phantom_cmd, sudo_cmd
from userbot.events import register
from telethon.tl.functions.messages import GetInlineBotResultsRequest

#@borg.on(phantom_cmd(pattern="^.stic ?(.*)"))
#@borg.on(sudo_cmd(pattern="^.stic ?(.*)", allow_sudo=True))

@register(outgoing=True, pattern="^.stic ?(.*)") #Kang With Credit
async def machine(stick):
#"""Creates random anime sticker!"""
    text = stick.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.stic <emoji>`")
    stickers = await bot.inline_query(
        "sticker", f"{text}")
    hm=len(stickers)
    op=random.randrange(0,hm)
    try:
        await stickers[op].click(stick.chat_id,
                            reply_to=stick.reply_to_msg_id,
                            silent=True if stick.is_reply else False,
                            hide_via=True)
        await stick.delete()
    except ValueError:
    	await stick.edit("**Use This Command as** `.stic <any emoji>`\nor Stickers are Not Avaliable for Entered Emoji")
    except ChatSendStickersForbiddenError:
    	await stick.edit("Sorry boss Can't Send Sticker Here !!")
#Phantomot
# @Anonymous_Machinee
        
@register(outgoing=True, pattern="^.gqbot ?(.*)") #Kang With Credit
async def phantomot(quote):
#"""Creates random anime sticker!"""
    text = quote.pattern_match.group(1)
    if text is None:
        await event.edit("Use This Command as `.gqbot <search query>`")
    quotes = await bot.inline_query(
        "GoodQuoteBot", f"{text}")
    hm=len(quotes)
    op=random.randrange(0,hm) #Phantomot
    try:
        await quotes[op].click(quote.chat_id,
                            reply_to=quote.reply_to_msg_id,
                            silent=True if quote.is_reply else False,
                            hide_via=True)
        await quote.delete()
    except ValueError:
    	await quote.edit("**Use This Command as** `.gqbot <author name>`")

        
    CMD_HELP.update({
    'stic':
    ".stic : will send random sticker from emoji."
        
})
    CMD_HELP.update({
    'gqbot':
    ".gqbot : use this as .gqbot <author name>. Send Quoted Related to Search."
        
})
