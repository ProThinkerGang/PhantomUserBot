import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import sudo_cmd, phantom_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.ded$")
@borg.on(phantom_cmd(pattern=r"ded"))
@borg.on(sudo_cmd(pattern=r"ded", allow_sudo=True))
async def bluedevilded(ded):
    await ded.edit(n + " ==             |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
K = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - -\n"
"_/﹋\_\n")
G = ("........___________________\n"
"....../ `-___________--_____|] - - - - - -\n"" - - ░ ▒▓▓█D \n"
"...../==o;;;;;;;;______.:/\n"
".....), -.(_(__) /\n"
"....// (..) ), —\n"
"...//___//\n")
D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
H = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")
E = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")


@borg.on(phantom_cmd(pattern=r"monster"))
@borg.on(sudo_cmd(pattern=r"monster", allow_sudo=True))
async def bluedevilmonster(monster):
    await monster.edit(M)
    
@borg.on(phantom_cmd(pattern=r"pig"))
@borg.on(sudo_cmd(pattern=r"pig", allow_sudo=True))
async def bluedevilpig(pig):
    await pig.edit(P)
    
@borg.on(phantom_cmd(pattern=r"kiler"))
@borg.on(sudo_cmd(pattern=r"killer", allow_sudo=True))
async def bluedevilkiller(kiler):
    await kiler.edit(K)
    
@borg.on(phantom_cmd(pattern=r"gun"))
@borg.on(sudo_cmd(pattern=r"gun", allow_sudo=True))
async def bluedevilgun(gun):
    await gun.edit(G)
    
@borg.on(phantom_cmd(pattern=r"dog"))
@borg.on(sudo_cmd(pattern=r"dog", allow_sudo=True))
async def bluedevildog(dog):
    await dog.edit(D)    
    
@borg.on(phantom_cmd(pattern=r"hello"))
@borg.on(sudo_cmd(pattern=r"hello", allow_sudo=True))
async def bluedevilhello(hello):
    await hello.edit(H)
    
@borg.on(phantom_cmd(pattern=r"hmf"))
@borg.on(sudo_cmd(pattern=r"hmf", allow_sudo=True))
async def bluedevilhmf(hmf):
    await hmf.edit(E)
