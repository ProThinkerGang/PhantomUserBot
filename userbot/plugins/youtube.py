# Coded by t.me/Fusuf #
# Please ask before kang #
# 2020 @AsenaUserBot #

from os import remove
from urllib.parse import quote

from requests import get
from telegraph import upload_file
from telethon.tl.functions.users import GetFullUserRequest

from userbot.events import register


@register(outgoing=True, pattern="^.youtube")
async def yutup(event):
    if not event.is_reply:
        return await event.edit("**Reply to a message!**")

    if not event.text:
        return await event.edit("**Please reply to a message!**")

    await event.edit("`Commenting On Youtube \nwait a while....`")
    reply = await event.get_reply_message()
    foto = await event.client.download_profile_photo(reply.sender_id)
    if foto == None:
        return await event.edit("`this message doesn't support on your device`")
    kullanici = await event.client(GetFullUserRequest(reply.sender_id))

    if not kullanici.user.username:
        return await event.edit("`Join` @PhantomSupport `for any Query or Help..`")

    avatar = upload_file(foto)
    json = f"https://some-random-api.ml/canvas/youtube-comment?avatar=https://telegra.ph{avatar[0]}&comment={quote(reply.message)}&username={kullanici.user.username}"
    r = get(json, allow_redirects=True)
    open("phantom.png", "wb").write(r.content)

    await event.client.send_file(
        event.chat_id,
        "phantom.png",
        caption="Commented By **PHANTOM Userbot**",
        reply_to=reply,
    )
    await event.delete()
    remove(foto)
    remove("phantom.png")
