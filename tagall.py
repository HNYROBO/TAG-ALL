# Changing some lines of code won't make you a programmer.
# use with credits else gay.
# © By @HNYOP.

import os, logging, asyncio

from telegraph import upload_file

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
AJ = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


# here replace "TAGALL_ROBOT" with your own bot username.
# use with credits else gay.

@AJ.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴛᴀɢᴀʟʟ ʀᴏʙᴏᴛ.\nɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴛᴀɢ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀꜱ ᴡɪᴛʜ ʟᴇꜱꜱ ᴛɪᴍᴇ ɪɴ ᴍᴀꜱꜱ Qᴜᴀɴᴛɪᴛʏ. [✨](https://te.legra.ph/file/0aaf54a1ac3dda5cd7b3c.jpg) \nɪꜰ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇʀʏ, ᴅᴏ /help ",
                    buttons=(
                      [
                         Button.url('ꜱᴜᴘᴘᴏʀᴛ', 'https://telegram.dog/chatroom_xd'), 
                         Button.url('ᴄʀᴇᴀᴛᴏʀ', 'https://telegram.dog/hnyrobo'), 
                      ], 
                      [
                        Button.url('𝗔𝗗𝗗 𝗠𝗘  𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣', 'http://t.me/TagAll_Robot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

# here also replace "TAGALL_ROBOT" with your own bot username.
# use with credits else gay.

@AJ.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**ᴛᴀɢ ʜᴇʟᴘ ʙᴏᴛ'ꜱ ʜᴇʟᴘ ᴍᴇɴᴜ**\n\nᴄᴏᴍᴍᴀɴᴅ: /all \n ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴇʟʟ ᴏᴛʜᴇʀꜱ. \n`Example: /all ʜɪ, ɪ ᴀᴍ ʜɴʏ!` \nʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴀꜱ ᴀɴ ᴀɴꜱᴡᴇʀ. ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ ʙᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜꜱᴇʀꜱ ᴛᴏ ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('ꜱᴜᴘᴘᴏʀᴛ', 'https://telegram.dog/chatroom_xd'), 
                         Button.url('ᴄʀᴇᴀᴛᴏʀ', 'https://telegram.dog/hnyrobo'), 
                      ], 
                      [
                        Button.url('𝗔𝗗𝗗 𝗠𝗘  𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣', 'http://t.me/TagAll_Robot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

@AJ.on(events.NewMessage(pattern="^/repo$"))
async def repo(event):
  repotext = "ɪ ᴀᴍ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [𝗛𝗡𝗬](https://t.me/hnyop)."
  await event.reply(repotext,
                    buttons=(
                      [
                         Button.url('ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ', 'https://github.com/HNYROBO/TAG-ALL'), 
                         Button.url('ᴄʀᴇᴀᴛᴏʀ', 'https://t.me/hnyop'), 
                      ], 
                      [
                        Button.url('𝗔𝗗𝗗 𝗠𝗘  𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣', 'https://t.me/tagall_robot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

@AJ.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all|@hny?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("Use this command in channel or group!")
  
  admins = []
  async for admin in AJ.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Only admin can use it.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀꜱ ꜰᴏʀ ᴏʟᴅ ᴘᴏꜱᴛ!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("ɢɪᴠᴇ ᴍᴇ ᴀɴ ᴀʀɢᴜᴍᴇɴᴛ. ᴇx: `/tag ʜɪɪ, ᴡʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜ`")
  else:
    return await event.respond("ʀᴇᴘʟʏ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ɢɪᴠᴇ ꜱᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in AJ.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await AJ.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in AJ.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped")
        return
      if usrnum == 5:
        await AJ.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@AJ.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond("ɴᴏᴛʜɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ...")
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**ꜱᴛᴏᴘᴘᴇᴅ ᴍᴇɴᴛɪᴏɴ...**')


print("Connecting...")
print("Started Successfully....")
print("Made by @HNYOP. Join the channel to be updated !")
AJ.run_until_disconnected()


# MADE UNDER AKIRA PROJECT
