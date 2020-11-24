import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from userbot.utils import phantom_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"


@borg.on(phantom_cmd(pattern="ping$"))
@borg.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(★ Pong!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**✦҈͜͡➳ Pong!__**\n★ {ms}\n★ __**My**__ __**Master**__ [{DEFAULTUSER}]"
    )
#Change The View its look

CMD_HELP.update(
    {
        "ping": "Show Ping Speed of Server"
    }
)
