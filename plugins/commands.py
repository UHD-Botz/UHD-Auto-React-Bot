import random
import os
import sys
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from plugins.emojis import EMOJIS
from config import *
from Script import text
from .db import tb
from .fsub import get_fsub


@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(message.from_user.mention, message.from_user.id)
        )
    if IS_FSUB and not await get_fsub(client, message):
        return
    await message.reply_text(
        text.START.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{client.me.username}?startgroup=true")],
            [
                InlineKeyboardButton("🔥 ᴍᴇɴᴜ 🔥", callback_data="menu"),
                InlineKeyboardButton("❤️ ᴅᴏɴᴀᴛᴇ ❤️", url="https://uhd-donate-page.vercel.app/")
            ],
            [
                InlineKeyboardButton("😃 ʜᴇʟᴘ 😃", callback_data="help"),
                InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ 🤖", callback_data="about")
            ],
            [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕", url=f"https://t.me/{client.me.username}?startchannel=true")]
        ])
    )


@Client.on_message(filters.command("stats") & filters.private & filters.user(ADMIN))
async def total_users(client, message):
    try:
        users = await tb.get_all_users()
        await message.reply(
            f"👥 **Total Users:** {len(users)}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎭 ᴄʟᴏsᴇ 🎭", callback_data="close")]
            ])
        )
    except Exception as e:
        r = await message.reply(f"❌ *Error:* `{str(e)}`")
        await asyncio.sleep(30)
        await r.delete()


@Client.on_message(filters.command("ping") & filters.private & filters.user(ADMIN))
async def ping_command(client, message):
    start = asyncio.get_event_loop().time()
    r = await message.reply("🏓 Pong...")
    end = asyncio.get_event_loop().time()
    latency = (end - start) * 1000
    await r.edit(f"🏓 **Pong!** `{int(latency)}ms`")


@Client.on_message(filters.command("restart") & filters.private & filters.user(ADMIN))
async def restart_command(client, message):
    msg = await message.reply("♻️ ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...")
    try:
        await asyncio.sleep(2)
        await msg.edit("✅ ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!")
    except:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)


@Client.on_message(filters.group | filters.channel)
async def send_reaction(client: Client, msg: Message):
    try:
        await msg.react(random.choice(EMOJIS))
    except FloodWait as e:
        print(f"FloodWait: Sleeping for {e.value} seconds")
        await asyncio.sleep(e.value)
        await msg.react(random.choice(EMOJIS))
    except Exception as e:
        print(f"Error: {e}")
