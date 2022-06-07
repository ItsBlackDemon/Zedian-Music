import os
import asyncio
import sys
import git
import heroku3
from Zedian.main import BOT
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, ALIVE_IMG as Zedian_PIC
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
hl = '/'
deadlyversion = 'Spambot0.10'

  

Zedian = "✯ 𝐌𝐮𝐬𝐢𝐜+𝐑𝐚𝐢𝐝 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭 ✯\n\n"
Zedian += f"═══════════════════\n"
Zedian += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.1`\n"
Zedian += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
Zedian += f"• **vᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
Zedian += f"═══════════════════\n\n"   

                                  
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
     await BOT.send_file(event.chat_id,
                                  Zedian_PIC,
                                  caption=Zedian,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Zedian_updates"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Zedian_project")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/S780821/Zedian-Music")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🎉 🇵 🇴 🇳 🇬 !\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎")
        
        
