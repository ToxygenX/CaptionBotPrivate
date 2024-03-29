# All Credits Belong to @CipherXBot 

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid
from pyrogram.dispatcher import Dispatcher

from Bot import app
from Bot.plugins import *
from Bot.config import Var


@app.on_chat_member_updated()
async def track_admin_status(client: Client, chat_member_updated: ChatMemberUpdated):
    if (
        chat_member_updated.new_chat_member is not None 
        and chat_member_updated.new_chat_member.user is not None
    ):
        me = await client.get_me()
        if chat_member_updated.new_chat_member.user.id == me.id:
            if chat_member_updated.new_chat_member.status == 'administrator':
                try:
                    channel_info_str=""
                    async for admin in app.iter.chat_members(chat_details.id , filter="administrators"):
                        owner_username=admin.user.username or ""
                        first_name=admin.user.first_name or ""
                        last_name=admin.user.last_name or ""
                        channel_info_str=(
                                f"#افزودن_بات\n"
                                f"نام چنل : {chat.title}\n"
                                f"آیدی چنل : {chat.id}\n"
                                f"یوزرنیم مالک : @{owner_username}\n"
                                f"مشخصات مالک :{first_name} {last_name}"
                            )
                        break
                    if channel_info_str:
                        await client.send_message(Var.OWNER_ID ,channel.info_str)
                except Exception as e:
                    print(f"Error: {str(e)}")


@app.on_message(filters.regex("چتز") & filters.incoming & filters.private)
async def all_chats(c: Client, m: Message):
    cmd = m.text.split("_")[-1]
    if cmd == "چتز":
        if m.from_user.id == Var.OWNER_ID:
            try:
                async for chat in app.get_dialogs():
                    print(chat)
                    if chat.chat.type == "channel" and chat.chat.is_admin:
                        owner = await app.get_users(chat.chat.owner_id)
                        owner_info = f"{owner.first_name} {owner.last_name} -Username: ({owner.username})"
                        await m.reply(f"Channel Name: {chat.chat.title}\nChannel ID: {chat.chat.id}\nChannel Owner: {owner_info}", quote=True)
            except Exception as e:
                print(str(e))


@app.on_message(filters.command(["id"]) & filters.channel)
async def id_channel(c: Client, m: Message):
    try:
        await m.reply(f"آیدی : `{m.chat.id}`")
    except Exception as e:
        return str(e)


@app.on_message(filters.regex("آیدی") & filters.incoming & filters.private)
async def id_command(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "آیدی":
        try:
            x = await c.ask(m.chat.id, "یوزرنیم را بفرستید")
            chat = await c.get_chat(x.text)
            await c.send_message(
                chat_id=m.chat.id,
                text= f"آیدی {chat.title} : `{chat.id}`"
            )
        except Exception as er:
            await c.send_message(
                chat_id=m.chat.id,
                text= f"یوزرنیمی که فرستادید معتبر نمی باشد\nمتن ارور:\n{str(er)}"
            )


@app.on_message(filters.regex("بفرس") & filters.incoming & filters.private)
async def send(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "بفرس":
        msg = await c.ask(m.chat.id, "بر روی فایل مورد نظر خود ریپلای کنید تا آن را برایتان به چنل داخواهتان در لیست چنل های اضافه شده بفرستم") 
        msg = msg.reply_to_message
        if msg:
            chat = await c.ask(m.chat.id, "اکنون چت آیدی چنل مورد نظر خود را بفرستید. شما میتوانید چت آیدی چنل مورد نظر خود را از لیست چنل دریافت نمایید") 
            if chat.text.startswith("-100"):
                await msg.copy(chat_id=int(chat.text))
                await chat.reply(f"پست مورد نظر با موفقیت به چنل {(await app.get_chat(int(chat.text))).title} ارسال شد", quote=True)
            else:
                await chat.reply("لطفا چت آیدی صحیح را وارد نمایید", quote=True) 
        else:
            await c.send_message(m.chat.id, "شما بر روی فایل مورد نظر خود ریپلای نکردید")


@app.on_message(filters.regex("لیست چنل") & filters.incoming & filters.private)
async def show_channels(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                mad = await chad(c, m) 
                if mad == None:
                    await m.reply("لیست چنل خالی می باشد", quote=True) 
                else:
                    await m.reply(f"{mad}", quote=True)  
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن چنل") & filters.incoming & filters.private)
async def add_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی چنل مورد نظر خود را وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل") and p.text.startswith("-100"):
                    try:
                        list1.append((await app.get_chat(int(p.text))).title)
                        list2.append(int(p.text))
                        await chad(c, m) 
                        await p.reply("چنل جدید با موفقیت افزوده شد", quote=True) 
                    except ChannelInvalid:
                        await p.reply("ابتدا بات را در چنل ادمین کرده و سپس چت آیدی آن را بفرستید", quote=True)
                elif not p.text.startswith("-100") and p.text != "کنسل":
                    await p.reply("لطفا فقط چت عددی چنل وارد نمایید", quote=True)  
                elif not p.text and not p.text.startswith("کنسل"):
                    await p.reply("چت آیدی یافت نشد", quote=True) 
                elif p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 

    
@app.on_message(filters.regex("حذف چنل") & filters.incoming & filters.private)
async def rem_channel(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف چنل":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "چت آیدی مورد نظر خود را برای حذف چنل وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if p.text.startswith("-100"):
                        if not int(p.text) in list2:
                            await p.reply("چت آیدی در لیست چنل ها یافت نشد", quote=True)  
                        else:
                            await p.reply("چنل با موفقیت حذف شد", quote=True)  
                            await chad(c, m) 
                            list1.remove((await app.get_chat(int(p.text))).title)
                            list2.remove(int(p.text))
                            rm = dict.pop((await app.get_chat(int(p.text))).title)
                    elif not p.text.startswith("-100"): 
                        await p.reply("لطفا فقط چت آیدی وارد نمایید", quote=True) 
                else:  
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("لیست ادمین") & filters.incoming & filters.private)
async def show_admins(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                if x == []:
                    await m.reply("لیست ادمین خالی می باشد", quote=True) 
                else:
                    await m.reply(f"{x}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن ادمین") & filters.incoming & filters.private)
async def add_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "افزودن ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای افزودن ادمین و دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل") and p.text.isnumeric() is True:
                    x.append(int(p.text))
                    await p.reply("ادمین جدید با موفقیت افزوده شد", quote=True) 
                elif p.text.isnumeric() is False and p.text != "کنسل":
                    await p.reply("لطفا فقط آیدی عددی وارد نمایید", quote=True) 
                elif not p.text and not p.text.startswith("کنسل"):
                    await p.reply("آیدی یافت نشد", quote=True) 
                elif p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف ادمین") & filters.incoming & filters.private)
async def rem_admin(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف ادمین":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "آیدی عددی مورد نظر خود را برای حذف ادمین و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if p.text.isnumeric() is True:
                        if not int(p.text) in x:
                            await p.reply("آیدی در لیست ادمین ها یافت نشد", quote=True)  
                        else:
                            x.remove(int(p.text))
                            await p.reply("ادمین با موفقیت حذف شد", quote=True) 
                    elif p.text.isnumeric() is False: 
                        await p.reply("لطفا فقط آیدی عددی وارد نمایید", quote=True) 
                else:  
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("لیست پسورد") & filters.incoming & filters.private)
async def show_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "لیست پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                if PASS == []:
                    await m.reply("لیست پسورد خالی می باشد", quote=True) 
                else:
                    await m.reply(f"{PASS}", quote=True) 
        except Exception as e:
            return 


@app.on_message(filters.regex("افزودن پسورد") & filters.incoming & filters.private)
async def add_pass(c: Client, m: Message):
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
                elif not p.text:
                    await p.reply("پسوردی یافت نشد", quote=True) 
                elif p.text.startswith("کنسل"): 
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 


@app.on_message(filters.regex("حذف پسورد") & filters.incoming & filters.private)
async def rem_pass(c: Client, m: Message):
    id = m.from_user.id
    cmd = m.text.split("_")[-1]
    if cmd == "حذف پسورد":
        try:
            if not id in x:
                vf = await verifys(c, m) 
            else:
                p = await c.ask(m.chat.id, "پسورد مورد نظر خود را برای حذف و عدم دسترسی به بات وارد نمایید. برای کنسل کردن این فرایند بنویسید `کنسل`")
                if not p.text.startswith("کنسل"):
                    if not p.text in PASS:
                        await p.reply("پسورد در لیست پسورد ها یافت نشد", quote=True)  
                    else:
                        PASS.remove(p.text)
                        await p.reply("پسورد با موفقیت حذف شد", quote=True) 
                elif not p.text and not p.text.startswith("کنسل"):
                    await p.reply("پسورد یافت نشد", quote=True) 
                elif p.text.startswith("کنسل"):
                    await p.reply("فرایند کنسل شد", quote=True) 
                    return True 
        except Exception as e:
            return 
