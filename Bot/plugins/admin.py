from pyrogram import Client, filters
from pyrogram.types import Message

from Bot import app
from Bot.plugins import *


@app.on_message(filters.regex("لیست ادمین") & filters.incoming & filters.private & ~filters.edited)
async def show_list_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(f"{x}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن ادمین") & filters.incoming & filters.private & ~filters.edited)
async def add_paas(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    x.append(int(p.text))
                    await p.reply("ادمین جدید با موفقیت افزوده شد", quote=True) 
                    return True
                if not p.text:
                    await p.reply("آیدی یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف ادمین") & filters.incoming & filters.private & ~filters.edited)
async def add_paas(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای حذف ادمین و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    x.remove(int(p.text))
                    await p.reply("ادمین با موفقیت حذف شد", quote=True) 
                    return True
                if not p.text:
                    await p.reply("آیدی یافت نشد", quote=True) 
                if not p.text in x:
                    await p.reply("آیدی در لیست ادمین ها یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("لیست پسورد") & filters.incoming & filters.private & ~filters.edited)
async def show_list_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                await m.reply(f"{PASS}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن پسورد") & filters.incoming & filters.private & ~filters.edited)
async def add_paas(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    PASS.append(p.text)
                    await p.reply("پسورد جدید با موفقیت افزوده شد", quote=True) 
                    return True
                if not p.text:
                    await p.reply("پسوردی یافت نشد", quote=True) 
                else:
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف پسورد") & filters.incoming & filters.private & ~filters.edited)
async def add_paas(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای حذف و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    PASS.remove(p.text)
                    await p.reply("پسورد با موفقیت حذف شد", quote=True) 
                    return True
                if not p.text:
                    await p.reply("پسورد یافت نشد", quote=True) 
                if not p.text in PASS:
                    await p.reply("پسورد در لیست پسورد ها یافت نشد", quote=True) 
                if p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 
