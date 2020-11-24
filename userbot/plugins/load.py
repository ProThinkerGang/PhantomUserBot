"""Emoji

Available Commands:
.up
.gnl"""

import asyncio
from telethon import events
from userbot.utils import phantom_cmd, sudo_cmd


# @borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
@borg.on(phantom_cmd(pattern="up$", outgoing=True))
@borg.on(sudo_cmd(pattern="up$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    animation_chars = ["╹", "╻", "╹", "╻" "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])
    

@borg.on(phantom_cmd(pattern="round$", outgoing=True))
@borg.on(sudo_cmd(pattern="round$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    animation_chars = ["⚫", "⬤", "●", "∘" "‎","‎", "●", "⬤","⚫️"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
        

# @borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
@borg.on(phantom_cmd(pattern="gnl$", outgoing=True))
@borg.on(sudo_cmd(pattern="gnl$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = [
        "😁🏿",
        "😁🏾",
        "😁🏽",
        "😁🏼",
        "‎😁",
        "**Glow & Lovely GeNg Is BeHiNd You....**",
        ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
