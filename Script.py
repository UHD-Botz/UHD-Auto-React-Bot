from pyrogram import Client, filters
from plugins.emojis import EMOJIS
import random

class text(object):
  START = """<b>{},

ɪ ᴀᴍ ʟᴀᴛᴇsᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴘᴏᴡᴇʀꜰᴜʟʟ ᴀᴜᴛᴏ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ.

ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀs ᴀ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ.

<blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/Ankan_Contact_Bot'>ᴀɴᴋᴀɴ</a></blockquote></b>"""

  LOG = """👁️‍🗨️ 𝘜𝘚𝘌𝘙 𝘋𝘌𝘛𝘈𝘐𝘓𝘚

○ 𝘐𝘋 : <code>{}</code>
○ 𝘋𝘊 : {}
○ 𝘍𝘪𝘳𝘴𝘵 𝘕𝘢𝘮𝘦 : {}
○ 𝘜𝘴𝘦𝘳𝘕𝘢𝘮𝘦 : {}

𝘉𝘺 = @{}"""
  
  ABOUT = """<b>📜 Cʜᴇᴄᴋ Aʙᴏᴜᴛ:
  
📚 Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
🧑‍💻 Lᴀɴɢᴜᴀɢᴇ: ᴊᴀᴠᴀ
🌐 Sᴇʀᴠᴇʀ: ʜᴇʀᴜᴋᴏ
🚀 ᴠᴇʀsɪᴏɴ: V2.0
👇 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ: (ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ) 

<blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/Ankan_Contact_Bot'>ᴀɴᴋᴀɴ</a></blockquote></b>"""
  
  HELP = """<b>{},

ᴛʜɪꜱ ɪꜱ ʀᴇᴀʟʟʏ sɪᴍᴘʟᴇ 🤣

ᴊᴜsᴛ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ, ᴀɴᴅ ᴇɴᴊᴏʏ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴍᴀɢɪᴄᴀʟ ʀᴇᴀᴄᴛɪᴏɴs 💞

<blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/Ankan_Contact_Bot'>ᴀɴᴋᴀɴ</a></blockquote></b>"""

  MENU = """
🔥 **ʜᴇʀᴇ ɪꜱ ᴀʟʟ ɪᴍᴘᴏʀᴛᴀɴᴛ ʙᴜᴛᴛᴏɴs ᴄʜᴇᴄᴋ ɪᴛ ᴏᴜᴛ** 🔥"""
