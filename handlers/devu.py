# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from helpers.filters import command
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import (BOT_NAME, SUPPORT_GROUP, OWNER_USERNAME, BOT_USERNAME)


@bot.on_message(filters.command("start"))
def start_(bot, message):
    
    START_TEXT = """ʜᴇʏ {}\n\nᴍʏsᴇʟғ {} \nᴀ sɪᴍᴘʟᴇ , ʟᴀɢғʀᴇᴇ ᴀɴᴅ ғʟᴇxɪʙʟᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ!\nɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ᴛʜᴇɴ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ @{}\nғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ʏᴏᴜ ᴄᴀɴ ᴇxᴘʟᴏʀᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ /help !"""

    START_BUTTON = [
                [
                    InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs🥀", url=f"https://t.me/SILENT_BOTS"),
                    InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(text="ᴏᴡɴᴇʀ👻", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton(text="sᴏᴜʀᴄᴇ✨", callback_data="repo_k"),
                ],                
                [                    
                    InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs!", callback_data="help_"),
                ],
                
            ]
    message.reply_text(
        START_TEXT.format(message.from_user.mention, BOT_NAME, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
    message.delete()

@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """ʜᴏɪ {}\nʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsɪʀᴇᴏᴘᴛɪᴏɴ ᴀɴᴅ ᴇxᴘʟᴏʀᴇʀ ɪᴛ!!\nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @{} ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ!!"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="ʙᴀsɪᴄ🧜", callback_data="basic_"),
            InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ🧚", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ🧞", callback_data="close_"),
            InlineKeyboardButton(text="ʙᴀᴄᴋ🧝", callback_data="HOME"),
        ],
    ]
    message.reply_text(
        HELP_TXT.format(message.from_user.first_name, SUPPORT_GROUP),
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""ʜᴏɪ, ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴅᴇsʀɪᴇᴏᴘᴛɪᴏɴ ᴀɴᴅ ᴇxᴘʟᴏʀᴇʀ ɪᴛ!!\nғᴏʀ ᴀɴʏ ᴋɪɴᴅ ᴏғ ʜᴇʟᴘ ᴏʀ ǫᴜᴇʀʏ ᴊᴜsᴛ ᴊᴏɪɴ @{SUPPORT_GROUP} ᴀɴᴅ ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇʀʏ!!"""
    
        HELP_BUTTON = [
            [
                InlineKeyboardButton(text="ʙᴀsɪᴄ🧜", callback_data="basic_"),
                InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ🧚", callback_data="admin_cmd"),
            ],
            [
                InlineKeyboardButton(text="ᴄʟᴏsᴇ🧞", callback_data="close_"),
                InlineKeyboardButton(text="ʙᴀᴄᴋ🧝", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "repo_k":
        REPO_MSG = f"""ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ {BOT_NAME} ɪs ᴘʀɪᴠᴀᴛᴇ. \nsᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ. ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʀᴇᴘᴏ ᴀsᴋ ᴛᴏ ᴏᴡɴᴇʀ ✨👻 !!"""
        REPO_BUTTONS = [
            [
                InlineKeyboardButton(text="ᴏᴡɴᴇʀ👻", url="https://t.me/My_Dear_Lightbright"),
                InlineKeyboardButton(text="ʙᴀᴄᴋ🧝", callback_data="HOME"),
            ],
        ]
        callback.edit_message_text(
            REPO_MSG,
            reply_markup=InlineKeyboardMarkup(REPO_BUTTONS)
        )
    elif callback.data == "HOME":
 
        START_TEXT = f"""ʜᴇʏ, ᴍʏsᴇʟғ {BOT_NAME} \nᴀ sɪᴍᴘʟᴇ , ʟᴀɢғʀᴇᴇ ᴀɴᴅ ғʟᴇxɪʙʟᴇ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ!\nɪғ ʏᴏᴜ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ᴛʜᴇɴ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ @{SUPPORT_GROUP}\nғᴏʀ ᴍᴏʀᴇ ʜᴇʟᴘ ʏᴏᴜ ᴄᴀɴ ᴇxᴘʟᴏʀᴇʀ ʜᴇʟᴘ ᴍᴇɴᴜ ʙʏ ᴛᴀᴘᴘɪɴɢ ᴏɴ /help !"""
        START_BUTTON = [
                    [
                        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs🥀", url="https://t.me/SILENT_BOTS"),
                        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ💥", url=f"http://t.me/{BOT_USERNAME}?startgroup=true"),
                    ],
                    [
                        InlineKeyboardButton(text="ᴏᴡɴᴇʀ👻", url=f"https://t.me/{OWNER_USERNAME}"),
                        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ✨", callback_data="repo_k"),
                    ],                
                    [                    
                        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs!", callback_data="help_"),
                    ],      
        ]
        
        callback.edit_message_text(
            START_TEXT,
            reply_markup=InlineKeyboardMarkup(START_BUTTON)
        )
    elif callback.data == "basic_":
        B_HELP = """
`ʙᴀsɪᴄs ᴄᴏᴍᴍᴀɴᴅs🧜`

/play (query, ytlink, audio file) - use this command and enjoy music
/ytp (query) - Use it for better search music!!
/song (query) - Download your favourite songs using this command!
/search (query) - This command will give you youtube search of your query!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_"),
                InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin_cmd":
        A_HELP = """
`ᴀᴅᴍɪɴs ᴄᴏᴍᴍᴀɴᴅs🧚`

/pause - To pause the song!
/resume - Resume paused song!
/skip - skip to the next song!
/end - End the stream!
/joinub - To invite assistant in your group!


`sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs🧞`

/rmf - To clean Download file from database!
/rmw - To clean raw files from database!
/dclean - To clean files from server!
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close_"),
                InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "close_":
        callback.message.delete()
