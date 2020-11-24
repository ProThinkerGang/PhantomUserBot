#Plugin made by @Anonymous_Machinee
# Kang with Credit #
# (c) Phantom Userbot
# Images Taken from @Quotery channel and @StudyTimeFactsBot Bot
# Total Pics = 205
#inspired by plugins Based on Random

from telethon import events
import asyncio
import os
import sys
from userbot.utils import phantom_cmd, sudo_cmd
import random
from userbot import CMD_HELP

img1="https://telegra.ph/file/31cf7484892cfdf85415f.jpg"
img2="https://telegra.ph/file/7408561005781ae9125ed.jpg"
img3="https://telegra.ph/file/18cd647447ad8421a7923.jpg"
img4="https://telegra.ph/file/6f18699851d78be60c9dc.jpg"
img5="https://telegra.ph/file/80073f27cd8dcccb55cc8.jpg"
img6="https://telegra.ph/file/04d7ebd5657a388514753.jpg"
img7="https://telegra.ph/file/f3fe1b4d5623dadb8fdc6.jpg"
img8="https://telegra.ph/file/ad5b030e5596c1a1eea03.jpg"
img9="https://telegra.ph/file/758dfac8d5061c0660cbb.jpg"
img10="https://telegra.ph/file/56f439a2b533dfa8373d7.jpg"
img11="https://telegra.ph/file/8632fd0f1ee5dddf02027.jpg"
img12="https://telegra.ph/file/7f7872d89a5573746bd34.jpg"
img13="https://telegra.ph/file/d2445817e0b103b939aed.jpg"
img14="https://telegra.ph/file/cddb7e77e4082a4a0be52.jpg"
img15="https://telegra.ph/file/b8eb7f9a41241bae0cea0.jpg"
img16="https://telegra.ph/file/b92050d05c10f4680f1aa.jpg"
img17="https://telegra.ph/file/82e4634de56da033509a0.jpg"
img18="https://telegra.ph/file/c18f58061dd536503c4b5.jpg"
img19="https://telegra.ph/file/18ca367663225c40a8cbb.jpg"
img20="https://telegra.ph/file/098207c0f7079caec1c23.jpg"
img21="https://telegra.ph/file/48ee775b12239a2a986a9.jpg"
img22="https://telegra.ph/file/367a368af7fbdb3aa53c3.jpg"
img23="https://telegra.ph/file/906934141e7a8d4258261.jpg"
img24="https://telegra.ph/file/6ec6810e2b0fedca4cf01.jpg"
img25="https://telegra.ph/file/7c8b043ce1067d92c1916.jpg"
img26="https://telegra.ph/file/1457f66f729cedfcee07a.jpg"
img27="https://telegra.ph/file/0a87339240a7976e46496.jpg"
img28="https://telegra.ph/file/73b4a376c0fb1a1f6f609.jpg"
img29="https://telegra.ph/file/8ba0f1cec5c812937f040.jpg"
img30="https://telegra.ph/file/0f9f34902eb3573fd5952.jpg"
img31="https://telegra.ph/file/d37b8ebfe14136f84586c.jpg"
img32="https://telegra.ph/file/f993f3f80071dd390eb0e.jpg"
img33="https://telegra.ph/file/c4ebecede33be6e1c0da0.jpg"
img34="https://telegra.ph/file/e8639396eca652baad053.jpg"
img35="https://telegra.ph/file/2e1b67d21fede429a9b17.jpg"
img36="https://telegra.ph/file/1be71e60aa29aae1f1fe7.jpg"
img37="https://telegra.ph/file/2ff07b757875aac453a54.jpg"
img38="https://telegra.ph/file/3ec4e4b017194be65ace7.jpg"
img39="https://telegra.ph/file/0b1ddef4d9d0947b10785.jpg"
img40="https://telegra.ph/file/6b6652a5a5ef3456a180b.jpg"
img41="https://telegra.ph/file/3ec4e4b017194be65ace7.jpg"
img42="https://telegra.ph/file/0b1ddef4d9d0947b10785.jpg"
img43="https://telegra.ph/file/2ff07b757875aac453a54.jpg"
img44="https://telegra.ph/file/2e1b67d21fede429a9b17.jpg"
img45="https://telegra.ph/file/1be71e60aa29aae1f1fe7.jpg"
img46="https://telegra.ph/file/d37b8ebfe14136f84586c.jpg"
img47="https://telegra.ph/file/e8639396eca652baad053.jpg"
img48="https://telegra.ph/file/c4ebecede33be6e1c0da0.jpg"
img49="https://telegra.ph/file/f993f3f80071dd390eb0e.jpg"
img50="https://telegra.ph/file/8ba0f1cec5c812937f040.jpg"
img51="https://telegra.ph/file/0f9f34902eb3573fd5952.jpg"
img52="https://telegra.ph/file/73b4a376c0fb1a1f6f609.jpg"
img53="https://telegra.ph/file/1457f66f729cedfcee07a.jpg"
img54="https://telegra.ph/file/0a87339240a7976e46496.jpg"
img55="https://telegra.ph/file/7c8b043ce1067d92c1916.jpg"
img56="https://telegra.ph/file/6ec6810e2b0fedca4cf01.jpg"
img57="https://telegra.ph/file/906934141e7a8d4258261.jpg"
img58="https://telegra.ph/file/367a368af7fbdb3aa53c3.jpg"
img59="https://telegra.ph/file/48ee775b12239a2a986a9.jpg"
img60="https://telegra.ph/file/098207c0f7079caec1c23.jpg"
img61="https://telegra.ph/file/c18f58061dd536503c4b5.jpg"
img62="https://telegra.ph/file/18ca367663225c40a8cbb.jpg"
img63="https://telegra.ph/file/82e4634de56da033509a0.jpg"
img64="https://telegra.ph/file/b92050d05c10f4680f1aa.jpg"
img65="https://telegra.ph/file/b8eb7f9a41241bae0cea0.jpg"
img66="https://telegra.ph/file/d2445817e0b103b939aed.jpg"
img67="https://telegra.ph/file/cddb7e77e4082a4a0be52.jpg"
img68="https://telegra.ph/file/56f439a2b533dfa8373d7.jpg"
img69="https://telegra.ph/file/7f7872d89a5573746bd34.jpg"
img70="https://telegra.ph/file/758dfac8d5061c0660cbb.jpg"
img71="https://telegra.ph/file/8632fd0f1ee5dddf02027.jpg"
img72="https://telegra.ph/file/ad5b030e5596c1a1eea03.jpg"
img73="https://telegra.ph/file/04d7ebd5657a388514753.jpg"
img74="https://telegra.ph/file/f3fe1b4d5623dadb8fdc6.jpg"
img75="https://telegra.ph/file/80073f27cd8dcccb55cc8.jpg"
img76="https://telegra.ph/file/6f18699851d78be60c9dc.jpg"
img77="https://telegra.ph/file/18cd647447ad8421a7923.jpg"
img78="https://telegra.ph/file/57f6cc9f320141571e891.jpg"
img79="https://telegra.ph/file/b0fb24f2edf204a056cb3.jpg"
img80="https://telegra.ph/file/caab2f1e143ebff9c1348.jpg"
img81="https://telegra.ph/file/ea09a2421755d72afc4f2.jpg"
img82="https://telegra.ph/file/deda7cfabceb6a40922ce.jpg"
img83="https://telegra.ph/file/bddc34abde3b405386de6.jpg"
img84="https://telegra.ph/file/6f8fdb8863dafd20e51a0.jpg"
img85="https://telegra.ph/file/d8b3019fcbc5639f9e5de.jpg"
img86="https://telegra.ph/file/b3b9fadb5e3a76122f10e.jpg"
img87="https://telegra.ph/file/28f18ef5493dc8afb7651.jpg"
img88="https://telegra.ph/file/52dcf4f26c141810c1ea1.jpg"
img89="https://telegra.ph/file/039a99ea5b522fc3ee6a5.jpg"
img90="https://telegra.ph/file/110303da38fc62cef7f02.jpg"
img91="https://telegra.ph/file/9d541190905177a8fdf35.jpg"
img92="https://telegra.ph/file/5e154d0f8ff4cbc9501d0.jpg"
img93="https://telegra.ph/file/5b5bf288e35afa17d80a3.jpg"
img94="https://telegra.ph/file/6743960672cc5869d5ce6.jpg"
img95="https://telegra.ph/file/4e5934c4430dd83d8aa3e.jpg"
img96="https://telegra.ph/file/ecbadf0ca13d895043ba9.jpg"
img97="https://telegra.ph/file/696b4acb978b8b75d0e0d.jpg"
img98="https://telegra.ph/file/b69cea578d0e38c82bf69.jpg"
img99="https://telegra.ph/file/9d2e6ae2cba2aa601cf1d.jpg"
img100="https://telegra.ph/file/390f0d7630ce272bff46b.jpg"
img101="https://telegra.ph/file/5430cbce72906d9d0f4a5.jpg"
img102="https://telegra.ph/file/c798f161552e5870fa600.jpg"
img103="https://telegra.ph/file/e69492d98594652c46640.jpg"
img104="https://telegra.ph/file/707f1b0b5241856ef49a3.jpg"
img105="https://telegra.ph/file/768c5475d8d367e4abc29.jpg"
img106="https://telegra.ph/file/e1f772b2cbade6b4167ee.jpg"
img107="https://telegra.ph/file/9e47c7b287c295e463339.jpg"
img108="https://telegra.ph/file/c6627a8252c7d9077ee24.jpg"
img109="https://telegra.ph/file/eecd011d90178f8985c1a.jpg"
img110="https://telegra.ph/file/c8e5d9fabbebfe9229b81.jpg"
img111="https://telegra.ph/file/bf5538926bf0aaea5a7f5.jpg"
img112="https://telegra.ph/file/657ee2d091b40cd97e01a.jpg"
img113="https://telegra.ph/file/c35e41f64016f55359a72.jpg"
img114="https://telegra.ph/file/d331d8e05040b3fc00b8e.jpg"
img115="https://telegra.ph/file/04509ed1e1e019663c41e.jpg"
img116="https://telegra.ph/file/b453a1dc8de09549fc333.jpg"
img117="https://telegra.ph/file/1731211b564e75ed54c54.jpg"
img118="https://telegra.ph/file/7e5fe6ccde7012f8723dd.jpg"
img119="https://telegra.ph/file/0722fda98d6f9a86057fd.jpg"
img120="https://telegra.ph/file/ff48e9cf2b6604f9a66f8.jpg"
img121="https://telegra.ph/file/e12b3898d8d6729c3654e.jpg"
img122="https://telegra.ph/file/4f2e9f9cb90516e194c78.jpg"
img123="https://telegra.ph/file/5fcf9eb2df29617e2e80e.jpg"
img124="https://telegra.ph/file/3d7f2e978278e32d4d4a7.jpg"
img125="https://telegra.ph/file/7593437abef2202049b83.jpg"
img126="https://telegra.ph/file/03c8fe2133842c9783224.jpg"
img127="https://telegra.ph/file/c81462a92a11edc104284.jpg"
img128="https://telegra.ph/file/7e6ede2caa3d57d243269.jpg"
img129="https://telegra.ph/file/2d29b664b93431e59dcb5.jpg"
img130="https://telegra.ph/file/51c99cd360fbcd56f17bf.jpg"
img131="https://telegra.ph/file/61671067f80f517a82a76.jpg"
img132="https://telegra.ph/file/57f42b6a7bafda2720e70.jpg"
img133="https://telegra.ph/file/fb3bece783e56c85e2cec.jpg"
img134="https://telegra.ph/file/d713bcaef934fdb437e62.jpg"
img135="https://telegra.ph/file/13f7b41c67f04a6d41be2.jpg"
img136="https://telegra.ph/file/f74128f91c84527c11022.jpg"
img137="https://telegra.ph/file/4ab4e025b13bade2d87f8.jpg"
img138="https://telegra.ph/file/ed725d23027d5389f0fb0.jpg"
img139="https://telegra.ph/file/19a310bdb1c2673d7ba82.jpg"
img140="https://telegra.ph/file/8371a0847b442295390d2.jpg"
img141="https://telegra.ph/file/0df8b153f0651de6c626b.jpg"
img142="https://telegra.ph/file/7d0741820ea78960932d2.jpg"
img143="https://telegra.ph/file/f0ea9943dd23beb9471b9.jpg"
img144="https://telegra.ph/file/cf54c5aeb2b9741c24456.jpg"
img145="https://telegra.ph/file/9d93aa9e616f958004835.jpg"
img146="https://telegra.ph/file/a88b6fef1165f41e7dd31.jpg"
img147="https://telegra.ph/file/b5ffc27f7bc901cdf2c99.jpg"
img148="https://telegra.ph/file/f1bd7602551911b0e839d.jpg"
img149="https://telegra.ph/file/379ab37982bd106161bc0.jpg"
img150="https://telegra.ph/file/13fe78243c4ecae6dd88e.jpg"
img151="https://telegra.ph/file/13fe78243c4ecae6dd88e.jpg"
img152="https://telegra.ph/file/c2569bf34927da03489f1.jpg"
img153="https://telegra.ph/file/73f2021bd8c75fe1e0eeb.jpg"
img154="https://telegra.ph/file/a6353819387428487efb6.jpg"
img155="https://telegra.ph/file/eed80e8dfecb737aafeda.jpg"
img156="https://telegra.ph/file/65bbf55b914688c765b20.jpg"
img157="https://telegra.ph/file/12e1a9a3625b83fa3231c.jpg"
img158="https://telegra.ph/file/cd063a8b140b15724ac51.jpg"
img159="https://telegra.ph/file/0e24385797846a9547a21.jpg"
img160="https://telegra.ph/file/0e8d183e7fe95046bae7a.jpg"
img161="https://telegra.ph/file/8b0d31173d042b9aff7a8.jpg"
img162="https://telegra.ph/file/c242579153bb0003253ce.jpg"
img163="https://telegra.ph/file/43336d625435aabab9233.jpg"
img164="https://telegra.ph/file/98baa98a893589518b828.jpg"
img165="https://telegra.ph/file/c91d07d5734c504c07bda.jpg"
img166="https://telegra.ph/file/dafb1403f592e87ea7091.jpg"
img167="https://telegra.ph/file/7c0d586e1c0062efabf32.jpg"
img168="https://telegra.ph/file/57a3e657559c5375a36bb.jpg"
img169="https://telegra.ph/file/f0e7cdc5b1f95c2fee685.jpg"
img170="https://telegra.ph/file/f236569e301d63e365686.jpg"
img171="https://telegra.ph/file/eb546a58d5468d926408a.jpg"
img172="https://telegra.ph/file/68359b4077efa83496ee9.jpg"
img173="https://telegra.ph/file/68359b4077efa83496ee9.jpg"
img174="https://telegra.ph/file/5fbbc64bb60c868be40b1.jpg"
img175="https://telegra.ph/file/125cc277bceebc66f5d77.jpg"
img176="https://telegra.ph/file/bdd67e55d9e255a7faed4.jpg"
img177="https://telegra.ph/file/4d1dd0101ccce54a126b3.jpg"
img178="https://telegra.ph/file/ae708583295df9b4678ae.jpg"
img179="https://telegra.ph/file/de78987990cb7256616a0.jpg"
img180="https://telegra.ph/file/24f935e56aed457a06436.jpg"
img181="https://telegra.ph/file/e04781fb5484212e237b8.jpg"
img182="https://telegra.ph/file/dd48219c164f2c091e272.jpg"
img183="https://telegra.ph/file/e4657d9f5c87216c08cf7.jpg"
img184="https://telegra.ph/file/6e03f81f42a1665ffb438.jpg"
img185="https://telegra.ph/file/104986938cb74d9f39c81.jpg"
img186="https://telegra.ph/file/f7282f6589d0ad0156357.jpg"
img187="https://telegra.ph/file/ae8f7da5b66a2a868c582.jpg"
img188="https://telegra.ph/file/165d0fc674284c06b34e7.jpg"
img189="https://telegra.ph/file/04468fbdd2593b3afe2a8.jpg"
img190="https://telegra.ph/file/a28ddfa8ad385cc322782.jpg"
img191="https://telegra.ph/file/2e0a80998068bfb62fd79.jpg"
img192="https://telegra.ph/file/5ce253c46e8e522d713a1.jpg"
img193="https://telegra.ph/file/2ffa9a72b932b2298a68e.jpg"
img194="https://telegra.ph/file/022e2c9fac5750bb2231a.jpg"
img195="https://telegra.ph/file/f3200cfecf63c3256dc43.jpg"
img196="https://telegra.ph/file/884d36760fa38cea1e152.jpg"
img197="https://telegra.ph/file/6abbc3d7628a68470701b.jpg"
img198="https://telegra.ph/file/18bdda3f017d4ff8f3f74.jpg"
img199="https://telegra.ph/file/e8fd68aef562354efd005.jpg"
img200="https://telegra.ph/file/8118905ebd193bc9f3013.jpg"
img201="https://telegra.ph/file/532f8939760a22ac91667.jpg"
img202="https://telegra.ph/file/cf58b020a89f8fb9a0e0a.jpg"
img203="https://telegra.ph/file/b588d77c41d3451e560c1.jpg"


#PHANTOMOT


@borg.on(phantom_cmd(outgoing=True, pattern="aquote"))
@borg.on(sudo_cmd(outgoing=True, pattern="aquote", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Sending...")
    await asyncio.sleep(0.2)
    await event.delete()
    x=(random.randrange(1,203))
    if x==1:
        await borg.send_file(event.chat_id,img1)
    if x==2:
        await borg.send_file(event.chat_id,img2)
    if x==3:
        await borg.send_file(event.chat_id,img3)
    if x==4:
        await borg.send_file(event.chat_id,img3)
    if x==5:
        await borg.send_file(event.chat_id,img4)
    if x==6:
        await borg.send_file(event.chat_id,img5)
    if x==7:
        await borg.send_file(event.chat_id,img6)
    if x==8:
        await borg.send_file(event.chat_id,img7)
    if x==9:
        await borg.send_file(event.chat_id,img9)
    if x==10:
        await borg.send_file(event.chat_id,img10)
    if x==11:
        await borg.send_file(event.chat_id,img11)
    if x==12:
        await borg.send_file(event.chat_id,img12)
    if x==13:
        await borg.send_file(event.chat_id,img13)
    if x==14:
        await borg.send_file(event.chat_id,img14)
    if x==15:
        await borg.send_file(event.chat_id,img15)
    if x==16:
        await borg.send_file(event.chat_id,img16)
    if x==17:
        await borg.send_file(event.chat_id,img17)  
    if x==18:
        await borg.send_file(event.chat_id,img18)
    if x==19:
        await borg.send_file(event.chat_id,img19)
    if x==20:
        await borg.send_file(event.chat_id,img20)
    if x==21:
        await borg.send_file(event.chat_id,img21)   
    if x==22:
        await borg.send_file(event.chat_id,img22)
    if x==23:
        await borg.send_file(event.chat_id,img23)
    if x==24:
        await borg.send_file(event.chat_id,img24)
    if x==25:
        await borg.send_file(event.chat_id,img25)
    if x==26:
        await borg.send_file(event.chat_id,img26)
    if x==27:
        await borg.send_file(event.chat_id,img27)
    if x==28:
        await borg.send_file(event.chat_id,img28)
    if x==29:
        await borg.send_file(event.chat_id,img29)
    if x==30:
        await borg.send_file(event.chat_id,img30)
    if x==31:
        await borg.send_file(event.chat_id,img31)
    if x==32:
        await borg.send_file(event.chat_id,img32)
    if x==33:
        await borg.send_file(event.chat_id,img33)
    if x==34:
        await borg.send_file(event.chat_id,img34)
    if x==35:
        await borg.send_file(event.chat_id,img35) 
    if x==36:
        await borg.send_file(event.chat_id,img36)
    if x==37:
        await borg.send_file(event.chat_id,img37)
    if x==38:
        await borg.send_file(event.chat_id,img38)
    if x==39:
        await borg.send_file(event.chat_id,img39)
    if x==40:
        await borg.send_file(event.chat_id,img40)
    if x==41:
        await borg.send_file(event.chat_id,img41)
    if x==42:
        await borg.send_file(event.chat_id,img42)
    if x==43:
        await borg.send_file(event.chat_id,img43)
    if x==44:
        await borg.send_file(event.chat_id,img44)
    if x==45:
        await borg.send_file(event.chat_id,img45)
    if x==46:
        await borg.send_file(event.chat_id,img46)
    if x==47:
        await borg.send_file(event.chat_id,img47)
    if x==48:
        await borg.send_file(event.chat_id,img48)
    if x==49:
        await borg.send_file(event.chat_id,img49)
    if x==50:
        await borg.send_file(event.chat_id,img50)
    if x==51:
        await borg.send_file(event.chat_id,img51)    
    if x==52:
        await borg.send_file(event.chat_id,img52)
    if x==53:
        await borg.send_file(event.chat_id,img53)
    if x==54:
        await borg.send_file(event.chat_id,img54)
    if x==55:
        await borg.send_file(event.chat_id,img55)
    if x==56:
        await borg.send_file(event.chat_id,img56)  
    if x==57:
        await borg.send_file(event.chat_id,img57)
    if x==58:
        await borg.send_file(event.chat_id,img58)
    if x==59:
        await borg.send_file(event.chat_id,img59)
    if x==60:
        await borg.send_file(event.chat_id,img60)
    if x==61:
        await borg.send_file(event.chat_id,img61)       
    if x==62:
        await borg.send_file(event.chat_id,img62)
    if x==63:
        await borg.send_file(event.chat_id,img63)
    if x==64:
        await borg.send_file(event.chat_id,img64)
    if x==65:
        await borg.send_file(event.chat_id,img65)
    if x==66:
        await borg.send_file(event.chat_id,img66)
    if x==67:
        await borg.send_file(event.chat_id,img67)
    if x==68:
        await borg.send_file(event.chat_id,img68)
    if x==69:
        await borg.send_file(event.chat_id,img69)
    if x==70:
        await borg.send_file(event.chat_id,img70)
    if x==71:
        await borg.send_file(event.chat_id,img71)            
    if x==72:
        await borg.send_file(event.chat_id,img72)
    if x==73:
        await borg.send_file(event.chat_id,img73)
    if x==74:
        await borg.send_file(event.chat_id,img74)
    if x==75:
        await borg.send_file(event.chat_id,img75)
    if x==76:
        await borg.send_file(event.chat_id,img76)
    if x==77:
        await borg.send_file(event.chat_id,img77)
    if x==78:
        await borg.send_file(event.chat_id,img78)
    if x==79:
        await borg.send_file(event.chat_id,img79)
    if x==80:
        await borg.send_file(event.chat_id,img80)
    if x==81:
        await borg.send_file(event.chat_id,img81)
    if x==82:
        await borg.send_file(event.chat_id,img82)
    if x==83:
        await borg.send_file(event.chat_id,img83)
    if x==84:
        await borg.send_file(event.chat_id,img84)
    if x==85:
        await borg.send_file(event.chat_id,img85)
    if x==86:
        await borg.send_file(event.chat_id,img86)
    if x==87:
        await borg.send_file(event.chat_id,img87)
    if x==88:
        await borg.send_file(event.chat_id,img88)
    if x==89:
        await borg.send_file(event.chat_id,img89)
    if x==90:
        await borg.send_file(event.chat_id,img90)
    if x==91:
        await borg.send_file(event.chat_id,img91)
    if x==92:
        await borg.send_file(event.chat_id,img92)
    if x==93:
        await borg.send_file(event.chat_id,img93)  
    if x==94:
        await borg.send_file(event.chat_id,img94)
    if x==95:
        await borg.send_file(event.chat_id,img95)
    if x==96:
        await borg.send_file(event.chat_id,img96)
    if x==97:
        await borg.send_file(event.chat_id,img97)
    if x==98:
        await borg.send_file(event.chat_id,img98)
    if x==99:
        await borg.send_file(event.chat_id,img98)
    if x==100:
        await borg.send_file(event.chat_id,img100)  
    if x==101:
        await borg.send_file(event.chat_id,img101)
    if x==102:
        await borg.send_file(event.chat_id,img102)
    if x==103:
        await borg.send_file(event.chat_id,img103)
    if x==104:
        await borg.send_file(event.chat_id,img104)
    if x==105:
        await borg.send_file(event.chat_id,img105)
    if x==106:
        await borg.send_file(event.chat_id,img106)
    if x==107:
        await borg.send_file(event.chat_id,img107)
    if x==108:
        await borg.send_file(event.chat_id,img108)
    if x==109:
        await borg.send_file(event.chat_id,img109)
    if x==110:
        await borg.send_file(event.chat_id,img110)
    if x==111:
        await borg.send_file(event.chat_id,img111)  
    if x==112:
        await borg.send_file(event.chat_id,img112)
    if x==113:
        await borg.send_file(event.chat_id,img113)
    if x==114:
        await borg.send_file(event.chat_id,img114)
    if x==115:
        await borg.send_file(event.chat_id,img115)
    if x==116:
        await borg.send_file(event.chat_id,img116)
    if x==117:
        await borg.send_file(event.chat_id,img117)  
    if x==118:
        await borg.send_file(event.chat_id,img118)
    if x==119:
        await borg.send_file(event.chat_id,img119)
    if x==120:
        await borg.send_file(event.chat_id,img120)
    if x==121:
        await borg.send_file(event.chat_id,img121)
    if x==122:
        await borg.send_file(event.chat_id,img122)
    if x==123:
        await borg.send_file(event.chat_id,img123)
    if x==124:
        await borg.send_file(event.chat_id,img124)
    if x==125:
        await borg.send_file(event.chat_id,img125)  
    if x==126:
        await borg.send_file(event.chat_id,img126)
    if x==127:
        await borg.send_file(event.chat_id,img127)
    if x==128:
        await borg.send_file(event.chat_id,img128)
    if x==129:
        await borg.send_file(event.chat_id,img129)
    if x==130:
        await borg.send_file(event.chat_id,img130)  
    if x==131:
        await borg.send_file(event.chat_id,img131)
    if x==132:
        await borg.send_file(event.chat_id,img132)
    if x==133:
        await borg.send_file(event.chat_id,img133)
    if x==134:
        await borg.send_file(event.chat_id,img134)
    if x==135:
        await borg.send_file(event.chat_id,img135)
    if x==136:
        await borg.send_file(event.chat_id,img136)  
    if x==137:
        await borg.send_file(event.chat_id,img137)
    if x==138:
        await borg.send_file(event.chat_id,img138)
    if x==139:
        await borg.send_file(event.chat_id,img139)
    if x==140:
        await borg.send_file(event.chat_id,img140)
    if x==141:
        await borg.send_file(event.chat_id,img141)  
    if x==142:
        await borg.send_file(event.chat_id,img142)
    if x==143:
        await borg.send_file(event.chat_id,img143)
    if x==144:
        await borg.send_file(event.chat_id,img144)
    if x==145:
        await borg.send_file(event.chat_id,img145)
    if x==146:
        await borg.send_file(event.chat_id,img146)
    if x==147:
        await borg.send_file(event.chat_id,img147)
    if x==148:
        await borg.send_file(event.chat_id,img148)
    if x==149:
        await borg.send_file(event.chat_id,img149)
    if x==150:
        await borg.send_file(event.chat_id,img150)
    if x==151:
        await borg.send_file(event.chat_id,img151)  
    if x==152:
        await borg.send_file(event.chat_id,img152)
    if x==153:
        await borg.send_file(event.chat_id,img153)
    if x==154:
        await borg.send_file(event.chat_id,img154)
    if x==155:
        await borg.send_file(event.chat_id,img155)
    if x==156:
        await borg.send_file(event.chat_id,img156)
    if x==157:
        await borg.send_file(event.chat_id,img157)
    if x==158:
        await borg.send_file(event.chat_id,img158)
    if x==159:
        await borg.send_file(event.chat_id,img159)
    if x==160:
        await borg.send_file(event.chat_id,img160)
    if x==161:
        await borg.send_file(event.chat_id,img161)
    if x==162:
        await borg.send_file(event.chat_id,img162)  
    if x==163:
        await borg.send_file(event.chat_id,img163)
    if x==164:
        await borg.send_file(event.chat_id,img164)
    if x==165:
        await borg.send_file(event.chat_id,img165)
    if x==166:
        await borg.send_file(event.chat_id,img166)
    if x==167:
        await borg.send_file(event.chat_id,img167)
    if x==168:
        await borg.send_file(event.chat_id,img168)
    if x==169:
        await borg.send_file(event.chat_id,img169)  
    if x==170:
        await borg.send_file(event.chat_id,img170)
    if x==171:
        await borg.send_file(event.chat_id,img171)
    if x==172:
        await borg.send_file(event.chat_id,img172)
    if x==173:
        await borg.send_file(event.chat_id,img173)
    if x==174:
        await borg.send_file(event.chat_id,img174)
    if x==175:
        await borg.send_file(event.chat_id,img175)
    if x==176:
        await borg.send_file(event.chat_id,img176)  
    if x==177:
        await borg.send_file(event.chat_id,img177)
    if x==178:
        await borg.send_file(event.chat_id,img178)
    if x==179:
        await borg.send_file(event.chat_id,img179)
    if x==180:
        await borg.send_file(event.chat_id,img180)
    if x==181:
        await borg.send_file(event.chat_id,img181)
    if x==182:
        await borg.send_file(event.chat_id,img182)
    if x==183:
        await borg.send_file(event.chat_id,img183)  
    if x==184:
        await borg.send_file(event.chat_id,img184)
    if x==185:
        await borg.send_file(event.chat_id,img185)
    if x==186:
        await borg.send_file(event.chat_id,img186)
    if x==187:
        await borg.send_file(event.chat_id,img187)
    if x==188:
        await borg.send_file(event.chat_id,img188)
    if x==189:
        await borg.send_file(event.chat_id,img189)
    if x==190:
        await borg.send_file(event.chat_id,img190)  
    if x==191:
        await borg.send_file(event.chat_id,img191)
    if x==192:
        await borg.send_file(event.chat_id,img192)
    if x==193:
        await borg.send_file(event.chat_id,img193)
    if x==194:
        await borg.send_file(event.chat_id,img194)        
    if x==195:
        await borg.send_file(event.chat_id,img195)  
    if x==196:
        await borg.send_file(event.chat_id,img196)
    if x==197:
        await borg.send_file(event.chat_id,img197)
    if x==198:
        await borg.send_file(event.chat_id,img198)
    if x==199:
        await borg.send_file(event.chat_id,img199)     
    if x==200:
        await borg.send_file(event.chat_id,img200)  
    if x==201:
        await borg.send_file(event.chat_id,img201)
    if x==202:
        await borg.send_file(event.chat_id,img202)
    if x==203:
        await borg.send_file(event.chat_id,img203)
        
        
