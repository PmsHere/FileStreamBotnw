from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 𝖧𝖾𝗒, </b>{}\n 
<i>send me a file or add me as an admin to any channel to instantly generate file links.\n

Add me to your channel to instantly generate links for any downloadable media. Once received, I will automatically attach appropriate buttons to the post containing the URL.</i>

<blockquote>Powered by @MalluTorentzTG</blockquote>"""

    HELP_TEXT = """
<i>- 𝖠𝖽𝖽 𝖬𝖾 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇 𝖮𝗇 𝖳𝗁𝖾 𝖢𝗁𝖺𝗇𝗇𝖾𝗅
- 𝖲𝖾𝗇𝖽 𝖬𝖾 𝖠𝗇𝗒 𝖣𝗈𝖼𝗎𝗆𝖾𝗇𝗍 𝖮𝗋 𝖬𝖾𝖽𝗂𝖺
- 𝖨 𝖶𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖲𝗍𝗋𝖾𝖺𝗆𝖺𝖻𝗅𝖾 𝖫𝗂𝗇𝗄</i>\n
<blockquote>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ. ⚠️</blockquote>"""

    ABOUT_TEXT = """
<b><a href="https://t.me/MalluFileStreamRoBot">🤖 𝖬𝗒 𝗇𝖺𝗆𝖾: 𝖥𝗂𝗅𝖾 𝖲𝗍𝗋𝖾𝖺𝗆 𝖡𝗈𝗍</a>
<a href="https://t.me/TGFilmRobot">📚 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
<a href="https://t.me/TGFilmRobot">🚀 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖢𝗅𝗈𝗎𝖽𝖿𝗅𝖺𝗋𝖾</a>
<a href="https://t.me/TGFilmRobot">📝 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: 𝖯𝗒𝗍𝗁𝗈𝗇3</a>
<a href="https://t.me/TGFilmRobot">💾 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾: 𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
<a href="https://t.me/Chiyaan_Dhruv">🧑‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: 𓊈Ｄｒ⚕️ ᴀᴅɪᴛʏᴀ𓊉 </a></b>

<b><i>Powered and Maintained By @MalluTorentzTG</i></b>
"""

    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🌨Support', url=f'https://t.me/{Telegram.UPDATES_CHANNEL}'),
            InlineKeyboardButton('⛅️Updates', url='https://t.me/MalluTorentzTG')
        ],
        [
            InlineKeyboardButton('❗️Help', callback_data='help'),
            InlineKeyboardButton('📦About', callback_data='about')
        ],
            [InlineKeyboardButton("🧑‍💻 Developer", url=f'https://t.me/chiyaan_dhruv')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🢇 Back', callback_data='home'),
            InlineKeyboardButton('Close ✘', callback_data='close'),
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🢇 Back', callback_data='home'),
            InlineKeyboardButton('Close ✘', callback_data='close'),
        ]]
    )
