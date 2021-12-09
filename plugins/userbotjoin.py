from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from helpers.decorators import authorized_users_only, errors
from Client.callsmusic import client as USER
from config import SUDO_USERS
from helpers.filters import command
@Client.on_message(filters.command(["انضم","join","userbotjoin",f"انضم @{XxVPlllllllllxX}",f"انضم@{VPllllllbot}",f"join@{VPllllllbot}",f"userbotjoin@{VPllllllbot}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمسؤول في مجموعتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "XxlllllllllllllllllllllllllllxX"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "انضممت هنا كما طلبت")
        await message.reply_text(
        "<b>انضم الحساب المساعد إلى محادثتك</b>",
    )
    except UserAlreadyParticipant:
        await USER.send_message(message.chat.id, "انا بالفعل موجود هنا 😐")
        await message.reply_text(
            "<b>الحساب المساعد بالفعل في الدردشة الخاصة بك</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطأ كثره الطلبات 🛑 \n الحساب المساعد تعذر الانضمام إلى مجموعتك بسبب كثرة طلبات الانضمام للحساب المساعد تأكد من عدم حظر الحساب المساعد في المجموعة."
            f"\n\nأو أضف يدويًا @{XxVPlllllllllxX} إلى مجموعتك وحاول مرة أخرى</b>",
        )
        return
    


@USER.on_message(filters.command(["left","غادر",f"غادر@{VPllllllbot}",f"left@{VPllllllbot}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.send_message(message.chat.id, "جاري المغادره")
        await USER.leave_chat(message.chat.id)
        Client.message.reply_text(
        "<b>قام الحساب المساعد بي مغادره المجموعه</b>",
    )
    except:
        await message.reply_text(
            f"<b>لا يمكن للحساب المساعد مغادرة مجموعتك! قد يكون بسبب الضغط."
            f"\n\nأو اطرده @{XxVPlllllllllxX} يدويًا من مجموعتك</b>",
        )
        return
    
@Client.on_message(filters.command(["leftall","مغادره",f"مغادره@{VPllllllbot}",f"leftall@{VPllllllbot}"]) & ~filters.bot)
async def bye(client, message):
    if message.from_user.id in SUDO_USERS or message.from_user.id == "2093265110":
        left=0
        failed=0
        lol = await message.reply("الحساب مساعد مغادرة جميع الدردشات")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"المساعد ترك {left} دردشة.\nفشل: {failed} دردشة.")
            except:
                failed=failed+1
                await lol.edit(f"المساعد ترك {left} دردشة.\nفشل: {failed} دردشة.")
        await client.send_message(message.chat.id, f"خرج من {left} محادثة.\nفشل {failed} محادثة.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc","القناه انضم",f"userbotjoinchannel@{VPllllllbot}",f"ubjoinc@{VPllllllbot}",f"القناه انضم@{VPllllllbot}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("لم يتم ربط القناه")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمشرف في قناتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Rengoku_Kyujoro_Helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "انضممت هنا كما طلبت")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>الحساب المساعد بالفعل في الدردشة الخاصة بك</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطأ كثره الطلبات 🛑 \n الحساب المساعد تعذر الانضمام إلى قناتك بسبب كثرة طلبات الانضمام علي الحساب المساعد او تأكد من عدم حظر الحساب المساعد في القناة."
            f"\n\nأو أضف يدويًا @{XxVPlllllllllxX} إلى قناتك وحاول مرة أخرى</b>",
        )
        return
    await message.reply_text(
        "<b>انضم الحساب المساعد إلى قناتك</b>",
    )
    
