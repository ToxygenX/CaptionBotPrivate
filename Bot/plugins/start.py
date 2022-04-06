from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from Bot import app

@app.on_message(filters.command('start') & filters.incoming & filters.private & ~filters.edited)
async def start(b, m : Message):
    firstname = m.from_user.first_name
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply(
            text=f"""Hey {m.from_user.mention(style="md")}, I'm the caption editor bot\nسلام {m.from_user.mention(style="md")} عزیز 🙋🏻‍♂️\nمن بات ادیت کپشن هستم\nفایل تلگرامی خود را ارسال کنید تا کپشن آن را ادیت کنم""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('✵ Developer ✵', url='https://t.me/CipherXBot')]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        return 
