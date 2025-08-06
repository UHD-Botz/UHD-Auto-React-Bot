from pyrogram import Client
from plugins.emojis import EMOJIS
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Script import text

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_text(
            text.START.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', url=f'https://t.me/{client.me.username}?startgroup=true')],
                [
                    InlineKeyboardButton('🔥 ᴍᴇɴᴜ 🔥', callback_data='menu'),
                    InlineKeyboardButton('❤️ ᴅᴏɴᴀᴛᴇ ❤️', url="https://uhd-donate-page.vercel.app/")
                ],
                [
                    InlineKeyboardButton('😃 ʜᴇʟᴘ 😃', callback_data='help'),
                    InlineKeyboardButton('🤖 ᴀʙᴏᴜᴛ 🤖', callback_data='about')
                ],
                [InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕', url=f'https://t.me/{client.me.username}?startchannel=true')],
            ])
        )

    elif query.data == "help":
        await query.message.edit_text(
            text.HELP.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇs 🤖", url="https://t.me/UHD_Bots"),
                 InlineKeyboardButton("👀 sᴜᴘᴘᴏʀᴛ 👀", url="https://t.me/UHDBots_Support")],
                [InlineKeyboardButton("🏹 ʙᴀᴄᴋ 🏹", callback_data="start"),
                 InlineKeyboardButton("🔒 ᴄʟᴏsᴇ 🔒", callback_data="close")]
            ])
        )

    elif query.data == "about":
        await query.message.edit_text(
            text.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/UHD-Botz/UHD-Auto-React-Bot"),
                 InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Ankan_Contact_BOT")],
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
            ])
        )

    elif query.data == "menu":
        await query.message.edit_text(
            text.MENU,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("UPDATES", url="https://t.me/UHD_Bots"),
                 InlineKeyboardButton("SUPPORT", url="https://t.me/+fx7ngJZDyFlhNTM1")],
                [InlineKeyboardButton("BACK", callback_data="start"),
                 InlineKeyboardButton("CLOSE", callback_data="close")]

            ])
        )

    elif query.data == "special":
        await query.answer("No special features enabled yet!", show_alert=True)

    elif query.data == "close":
        await query.message.delete()
