# meta author: 𝑳𝒐𝒓𝒅
#meta developer: 𝑳𝒐𝒓𝒅
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
from telethon import types
from random import randint
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon import errors, functions
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    MessageTooLongError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserIdInvalidError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)



class Lord(loader.Module):
    '''Информация о хелпе'''
    strings = {
    "name":  "𝒗𝑳𝒐𝒓𝒅𝑯𝒆𝒍𝒑",
    "loading": "<b>Караю шалав во имя Lord...</b>",
    "not_chat": "<b>Ты не караешь шалав от имени Lord в конференции</b>",} # name loader () \n
    
    
    async def client_ready(self, client, db) -> None:
        
        self.db = db
        self.client = client
        
        
    async def lordhelpcmd(self, message):
        """запустить анимацию"""
        args = utils.get_args_raw(message)
        await message.edit("𝐋")
        time.sleep(0.1)
        await message.edit("𝐋𝐨")
        time.sleep(0.1)
        await message.edit("𝐋𝐨𝐫")
        time.sleep(0.1)
        await message.edit("𝐋𝐨𝐫𝐝")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        await message.edit("𝒛𝒂𝒈𝒓𝒖𝒛𝒌𝒂...")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji><emoji document_id=5352625214800797332>⭐️</emoji>")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        
        message = await utils.answer(message, self.strings("name"))
        media_files = ("https://te.legra.ph/file/7a7926911c0fef3483864.mp4", "https://te.legra.ph/file/7a7926911c0fef3483864.mp4")
        try:
            user_id = (
                (
                    (
                        await self._client.get_entity(
                        args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id

            user = await self._client(GetFullUserRequest(user_id))

            user_ent = user.users[0]

            photo = await self._client.download_profile_photo(user_ent.id, bytes)
            user_info = (
            "<b><emoji document_id=5352792306208480366>🌎</emoji><emoji document_id=5352540225987943305>💃</emoji><emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5776149796670673457>🔠</emoji><emoji document_id=5776060598789868807>🔠</emoji><emoji document_id=5775969365094568088>🔠</emoji><emoji document_id=5776269527473984208>🔠</emoji> <emoji document_id=5776287227034210814>🔠</emoji><emoji document_id=5776098750984359418>🔠</emoji><emoji document_id=5776149796670673457>🔠</emoji><emoji document_id=5776072942525877772>🔠</emoji><emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5352540225987943305>💃</emoji><emoji document_id=5352792306208480366>🌎</emoji></b>\n\n"
            "<b><emoji document_id=5021665527576134431>✨️</emoji><emoji document_id=5258306268396790997>😇</emoji><emoji document_id=5258372097360535274>🙃</emoji><emoji document_id=5255704549007566838>😆</emoji><emoji document_id=5258228271790694261>😘</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5256012833170139346>🤣</emoji> <emoji document_id=5255777305753561750>😄</emoji> <emoji document_id=5256142901959729905>😙</emoji><emoji document_id=5256150684440470680>🥹</emoji><emoji document_id=5256056186570024436>😊</emoji><emoji document_id=5255921814223201321>😉</emoji><emoji document_id=5256150684440470680>🥹</emoji><emoji document_id=5021665527576134431>✨️</emoji></b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji></code><code>.lord</code> - [<emoji document_id=5352585602317426381>💀</emoji>] -Запустить модуль Lord- [<emoji document_id=5352585602317426381>💀</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lordov</code> - [<emoji document_id=5276174174161739848>😈</emoji>] - Запустить модуль во имя Lord - [<emoji document_id=5276174174161739848>😈</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lordnn</code> - [<emoji document_id=5341557921597631101>😈</emoji>] - Запустить модуль LordNN - [<emoji document_id=5341557921597631101>😈</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lorddm</code> - [<emoji document_id=5391112781812473534>💎</emoji>] - Запустить модуль Daimond во имя Lord - [<emoji document_id=5391112781812473534>💎</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lordger</code> - [<emoji document_id=5409324508299405361>🇩🇪</emoji>] - Запустить модуль German во имя Lord -[<emoji document_id=5409324508299405361>🇩🇪</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lorddino</code> - [<emoji document_id=5393327477403688907>🦕</emoji>]- Запустить модуль Dino во имя Lord - [<emoji document_id=5393327477403688907>🦕</emoji>]</b>\n\n"
            "<b><emoji document_id=5352625214800797332>⭐️</emoji><code>.lordcer</code> - [<emoji document_id=5388994705805549866>🤡</emoji>]-задержка + шапка: запускает модуль по     шаблону[<emoji document_id=5388994705805549866>☠️</emoji>]</b>\n\n"
                        f"<b><emoji document_id=5352964886584367997>🚨</emoji>Инɸ᧐ρⲙᥲцᥙя<emoji document_id=5352964886584367997>🚨</emoji></b>\n"
              f"<b><emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5353034963270771323>✝️</emoji>𝑶𝒏𝒍𝒊𝒏𝒆:<emoji document_id=5353034963270771323>✝️</emoji><emoji document_id=5404717537399154963>❤️</emoji></b>\n"
              f"<b><emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5353036831581544549>🤩</emoji>𝑽𝒆𝒓𝒔𝒊𝒐𝒏: <emoji document_id=5857047245152587687>1️⃣</emoji>.<emoji document_id=5857047245152587687>1️⃣</emoji>.<emoji document_id=5855068317496119791>0️⃣</emoji><emoji document_id=5353036831581544549>🤩</emoji><emoji document_id=5404717537399154963>❤️</emoji></b>\n"
            f"<emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5352535402739672117>💀</emoji><b>𝑼𝒔𝒆𝒓𝒔:</b> @{user_ent.username or '<emoji document_id=5454064486837133402>☠️</emoji>'}<emoji document_id=5352535402739672117>💀</emoji><emoji document_id=5404717537399154963>❤️</emoji>\n"
            f"<b><emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5353055570523856699>😈</emoji>𝑳𝒐𝒓𝒅:</b> {user_ent.first_name or '🚫'}<emoji document_id=5353055570523856699>😈</emoji><emoji document_id=5404717537399154963>❤️</emoji>\n"
            f"<b><emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5352958736191200616>⭐️</emoji>𝑰𝑫:</b> <code>{user_ent.id}</code><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5404717537399154963>❤️</emoji>\n"
            f"<b><emoji document_id=5404717537399154963>❤️</emoji><emoji document_id=5352727529511723136>❣️</emoji>Рᥲᤋρᥲδ᧐ᴛчᥙκ:<code>𝑳𝒐𝒓𝒅</code><emoji document_id=5352727529511723136>❣️</emoji><emoji document_id=5404717537399154963>❤️</emoji></b>\n"
            )

        if photo:
            await self._client.send_file(
                message.peer_id,
                photo,
                caption=user_info,
                link_preview=False,
                reply_to=reply.id if reply else None,
            )
            if message.out:
                await message.delete()
        else:
            await utils.answer(
                message,
                user_info,
                reply_to=reply.id if reply else None,
                link_preview=False,
            )

    async def lordcmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный модуль Lord прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль Lord начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lord</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [
        "члᴇнǿϻ ϻᴀть твǿю ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " стᴀль в пизду твǿᴇй ϻᴀϻᴀши всунул) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в рылǿ твǿю ϻᴀть ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в ǿчҝǿ твǿю ϻᴀть ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в ҝрᴇдит твтя ϻᴀть сᴀсᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " лᴇтя сᴀсᴀлᴀ ϻᴀть твǿя) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть шлюхᴀ хуй сᴀсᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " всᴇ чᴀщᴇ сую члᴇн в ϻᴀть твǿю) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в трᴇжиϻᴇ твǿю ϻᴀть трᴀхᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " прǿжǿг ᴇбᴀлǿ твǿᴇй ϻᴀϻᴀшᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю пингвинил члᴇнǿϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀшᴀ твǿя шлюхᴀ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть зᴀ ᴇбᴀлǿ нᴀд хуᴇϻ пǿвᴇсил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю члᴇнǿϻ дырявил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " члᴇнǿϻ твǿю ϻᴀть чᴇҝᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю хуᴇϻ вытрᴀхивᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀню твǿю зᴀлупǿй дрᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть лᴇтᴀᴇт пǿ хую ϻǿᴇϻу) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю зᴀлупǿй прихуярил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿя зᴀлупǿй дᴀвиться) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀшу твǿю зᴀ пизду пǿвᴇшᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " сᴀсᴇт твǿя ϻᴀть пǿҝᴀ ты сϻǿтришь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀшу твǿю зᴀлупǿй уничтǿжил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в пᴀрᴀшᴇ твǿю ϻᴀть тǿплю) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀшᴇ твǿᴇй зᴀлупǿй шᴀры выбил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " тяну твǿю ϻᴀть шлюху) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть нᴀ 5+ сᴀсᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀши твǿᴇй улǿжил зᴀлупу в рǿт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в щᴇҝǿлду твǿю ϻᴀть ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пǿ ҝᴀбинᴇ твǿᴇй ϻᴀϻᴀши зᴀлупǿй бью) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " зᴀлупǿй твǿю ϻᴀть пидᴀрᴀсил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻᴀшу твǿю в рǿт жᴇ ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " трᴀхᴀнул твǿю ϻᴀть ну) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю рᴇжу хуᴇϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " хуᴇϻ ϻᴀть твǿю иϻᴇл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в ǿчҝǿ твǿᴇй ϻᴀϻᴀши ҝǿнчил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻǿю спᴇрϻу жуᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " чᴇтҝᴀ твǿя ϻᴀть сᴀсᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " зᴀҝрыл рǿт твǿᴇй ϻᴀϻᴀши члᴇнǿϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пᴀлᴇруᴇт твǿя ϻᴀть ϻǿю зᴀлупу) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " члᴇнǿϻ твǿю ϻᴀть вьᴇбᴀшил в ᴀсфᴀлт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " зᴀсᴀдил твǿᴇй ϻᴀϻᴀши) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " в пузǿ твǿю ϻᴀть ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " члᴇнǿϻ твǿю ϻᴀть дᴀвил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю ǿпрᴀҝинул зᴀлупǿй) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нǿгиϻи твǿя ϻᴀть дрǿчит ϻнᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " хуᴇϻ твǿю ϻᴀть ҝǿвырял) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " глубǿҝǿ твǿю ϻᴀть ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ǿтьᴇхᴀлᴀ твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " придушил твǿю ϻᴀть хуᴇϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿя ᴇбᴀнит нᴀ хую) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю рву хуᴇϻ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пизду твǿᴇй ϻᴀϻᴀши пǿрвᴀл члᴇнǿϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нᴀ ҝлыҝ твǿᴇй ϻᴀϻᴀши дᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть чᴇрᴇз ϻǿй хуй прǿливᴀᴇтся ҝᴀҝ вǿдᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть сǿсᴇт я твǿю ϻᴀть дǿширᴀҝǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть сǿсᴇтя твǿю ϻᴀть спичҝᴀϻи ᴇбу ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть с хуя пусҝᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть снǿвᴀ нᴀ ϻǿй члᴇн призᴇϻлилᴀсь пǿслᴇ пǿлётᴀ в тᴀджиҝистᴀн нᴀ рǿдину ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пǿчᴇϻу пиздᴀҝ твǿᴇй ϻᴀтᴇри, зᴀтягивᴀᴇт хуи, ҝᴀҝ трᴇугǿльниҝ бᴇрϻудсҝий ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть пылᴇсǿсǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть с хуя чᴇрᴇз зᴀбǿры пᴇрᴇҝидывᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты вǿзьϻи сᴇбᴇ в зубы лᴇйҝу и пǿливᴀй ǿгǿрǿды в пиздᴇ свǿᴇй ϻᴀϻᴀши ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я жᴇ рᴀҝǿвую ǿпухǿль в пиздᴇ твǿᴇй ϻᴀϻᴀши устрǿнял при пǿϻǿщи свǿᴇгǿ хуя ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ҝǿгдᴀ у твǿᴇй ϻᴀтᴇри будᴇт ᴀнгинᴀ пǿзǿви ϻᴇня я буду ᴇй в гǿрлǿ бры3гᴀть свǿᴇй спᴇрϻǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю грудную ҝлᴇтҝу хуᴇϻ рᴀсспиливᴀл пǿпǿлᴀϻ и стᴇлил пǿд свǿиϻи двᴇрьϻи ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " зᴀчᴇϻ ты ртǿϻ нᴀ хуй упᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀϻᴀшҝᴀ зᴀ бᴀрбᴀрисҝу хуй сǿсᴇт нᴀ рынҝᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пǿслᴇ тǿгǿ ҝᴀҝ я ᴇй лᴇчил рᴀҝ губы зᴀлупǿй ǿнᴀ пǿлбюбилᴀ ᴇгǿ сҝǿрǿ ϻǿй хуй ты сϻǿжᴇшь нᴀзывᴀть пᴀпҝǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " вǿт у тᴇбя явнǿ пидǿрсҝиᴇ нᴀҝлǿннǿсти( ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴇня вдǿхнᴀвляᴇт твǿй рǿт нᴀпᴀвший нᴀ ϻǿй хуй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ҝᴀҝ ты ǿтнᴇсᴇшься ҝ тǿϻу чтǿ ϻǿй хуй зᴀстрял в 12 пᴇрстнǿй ҝишҝᴇ твǿᴇй ϻᴀϻᴀши ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ пиздил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри зубы хуᴇϻ выбил, ǿнᴀ тᴀҝ гǿрьҝǿ плᴀҝᴀлᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ ҝлизϻу сдᴇлᴀю ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ хрᴇбᴇт лǿϻᴀю ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ шᴇю лǿϻᴀю ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри ҝлитǿр с нǿги выбивᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри ҝирпиичи в ᴇблǿ ҝидᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть нᴀ чᴇрдᴀҝᴇ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть нᴀ двᴇрнǿй ручҝᴇ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть нᴀ ҝᴀлитҝᴇ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть зᴀбǿринǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ҝᴀчᴇргǿй ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри бычҝи тушил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты свǿю сᴇстру пǿ ϻǿᴇϻу сǿглᴀсию ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нǿждᴀчҝǿй хуярил пǿ пиздᴇ твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тёрҝǿй тᴇр ᴇблǿ твǿᴇᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ǿбǿссᴀл пǿҝᴀ ты ҝлитǿр сᴇстрᴇ лизᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть ǿсудили пǿжизᴇннǿ зᴀ пǿсидᴇлҝи нᴀ ϻǿᴇϻ хуᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть нᴀ ϻǿй члᴇн с 5 этᴀжᴀ пᴀдᴀлᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀϻҝᴇ хуᴇϻ в глᴀз тыҝᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри нᴀ ᴇблǿ ҝǿнчᴀл пǿҝᴀ ты хуй ǿтцᴀ сǿсᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ губᴇ дᴀвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ щᴇҝᴇ удᴀрил , у нᴇᴇ чᴇлюсть слǿϻᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри зᴀлупǿй пǿ лбу хуярил пǿҝᴀ ты ϻнᴇ яйцᴀ лизᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть зᴀ дᴇньги сниϻᴀл, пǿслᴇ ǿтдᴀвᴀл бǿϻжᴀϻ и ǿни ᴇᴇ пǿ ҝругу ᴇбᴀли ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть блядь, ᴀ твǿй ǿтᴇц рᴀбǿтᴀᴇт в гᴇй ҝлубᴇ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я рǿзу впизду твǿᴇй ϻᴀтᴇри тыҝᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть пᴀдᴀлᴀ нᴀ ϻǿй члᴇн ҝᴀҝ зᴀсǿхший лист с дᴇрᴇвᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть плǿсҝǿгруднᴀя ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я пизду твǿᴇй ϻᴀтᴇри тᴇбᴇ нᴀ ᴇблǿ нᴀтягивᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я ҝлитǿр твǿᴇй ϻᴀтᴇри рᴀстягивᴀл, ǿн стᴀнǿвился длиднный ҝᴀҝ зϻᴇя ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть зᴀ пǿлǿвыᴇ губы ҝ пǿтǿлҝу прибивᴀл и хᴀрҝᴀл ᴇй в ᴇблǿ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀтьшᴀϻпурǿϻ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я приниϻᴀю эҝзᴀϻᴇны, ᴀ твǿя ϻᴀϻᴀ дᴀёт ϻнᴇ взятҝу нᴀтурǿй ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я рвᴀл тᴇбᴇ цᴇлҝуу твǿᴇй ϻᴀтᴇри ржᴀвǿй трубǿй :3 ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты свǿиϻ языҝǿϻ вшᴇй лǿбҝǿвых нᴀ пиздᴇ ϻᴀтᴇри гǿнял ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты свǿиϻ ртǿϻ глистǿв из жǿпы ϻᴀтᴇри вытᴀсҝивᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ в лᴇсу зᴀрǿю ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбᴇ нǿги в рǿт ҝлᴀл пидᴀрᴀс ты ᴇбᴀный ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прǿстрᴇлил ҝᴀҝ с двух ствǿлҝи ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть и тᴀҝ и сяҝ ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿ юϻᴀть в гǿрᴀх ᴇбᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ твǿй ǿтᴇц тᴇбᴇ ҝǿнчу в рǿт сливᴀл ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ ты в шҝǿлᴇ был ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть с хуя выҝинул в рᴇҝу ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть въᴇбᴀннᴀя ϻǿиϻ хуᴇϻ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть вᴇрхнǿгᴀϻи ᴇбᴀл суҝᴀ ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты сǿсᴇшь и бᴀлдᴇᴇшь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я нᴀ пиздᴇ твǿᴇй ϻᴀтᴇри урǿҝи хуᴇϻ дᴇлᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть пǿд пǿᴇз хуᴇϻ ҝину щᴀс) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу спǿриϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻǿй члᴇн в пǿҝǿᴇ нᴇ ǿстᴀвляᴇшь ртǿϻ свǿиϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу грубǿ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу в пᴀдиҝᴇ хуᴇϻ пǿгнул) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую тᴀщится) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть пǿд ϻǿиϻ хуᴇϻ тᴇбя высрᴀлᴀ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ҝᴀҝ высҝᴀчҝᴀ нᴀ ϻǿᴇϻ хую) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть нᴀ люстрᴇ ǿтъᴇбу щᴀс) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты нᴀ ϻǿᴇϻ хую извивᴀᴇшься ҝᴀҝ зϻᴇя) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝᴀҝ нᴇвϻиняᴇϻый) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ рᴀсписᴀл ҝᴀҝ диҝтᴀнт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбᴇ хуᴇϻ ϻǿзгǿв дǿбᴀвлю щᴀс) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻнᴇ сǿсᴇшь ҝǿгдᴀ нᴇбǿ звᴇзднǿᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты нᴀ ҝǿртǿчҝᴀх ϻǿй хуй сǿсᴇшь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ҝ ϻǿᴇϻу хую лᴇтишь ҝᴀҝ вǿрǿбᴇй) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты нюни пустил ҝǿгдᴀ ϻǿй хуй ǿтпиздил тᴇбя) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻǿй хуй тᴇбя встрᴇтил бᴇз трусǿв нᴀ улицᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты нᴀ ϻǿᴇϻ хую зᴀиҝᴀтся нᴀчᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пǿд люстрǿй сǿсᴀл ϻнᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻǿй хуй нᴀ руҝᴀх свǿих нǿсишь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻǿй хуй вǿняᴇт пизжᴇ чᴇϻ твǿи духи) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбя хуᴇϻ зᴀҝручу щᴀс ҝᴀҝ ϻᴇтᴇль ᴇбᴀть) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ҝ ϻǿᴇϻу хую в жᴇны нᴀбивᴀᴇшься) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻǿю спᴇрϻу ҝ сᴇбᴇ нᴀ пǿлǿвыᴇ губы ϻᴀжᴇшь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри вырᴇжу хуᴇϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть с пᴇрвǿгǿ рᴀзᴀ пǿрвᴀл ҝᴀҝ гᴀзᴇту) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿᴇй ϻᴀтᴇри рᴀҝ губы хуᴇϻ лᴇчил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ǿвсянҝǿй ᴇбᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл 2 гǿдᴀ нᴀзᴀд, ҝǿгдᴀ в шҝǿлᴇ учился) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть зᴀстᴀвил нᴀ ϻǿй хуй сᴇсть) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть ᴇбут ϻǿи друзья) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻǿиϻ члᴇнǿϻ с дᴇтствᴀ питᴀᴇтся) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я чᴇт чᴀстǿ твǿю ϻᴀтуху в дᴇснᴀ ᴇбу) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты жᴇ сǿ свǿᴇй ϻᴀϻᴀшᴇй пǿ ϻǿᴇϻу хую гǿришь) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я плǿтнǿ твǿю ϻᴀть в пизду ᴇбу) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я ᴇблǿϻ твǿиϻ пǿ пиздᴇ твǿᴇй ϻᴀϻҝᴇ ᴇздил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты сǿсᴇшь ϻнᴇ нᴀ пᴇрᴇднᴇϻ плᴀнᴇ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть нᴇ ǿстᴀнᴀвить нᴀ ϻǿᴇϻ хую) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть ᴇбᴀл пǿ пьянᴇ нᴀ сцᴇнᴀх) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пᴇрᴇд ϻǿиϻ хуᴇϻ гнулᴀсь ҝᴀҝ институтҝᴀ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿй рǿт сǿсᴇт ϻнᴇ ҝᴀҝ бᴀлᴀбǿл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ нᴀ стрᴇлᴇ пиздил) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть ᴇбу ҝǿгдᴀ ты нᴇ успᴇвᴀᴇшь бᴀтᴇ сǿсᴀть) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты нᴀ ϻǿй хуй ϻǿлишься ҝᴀҝ нᴀ иҝǿну) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пǿд ϻǿиϻ хуᴇϻ прǿгинᴀᴇшься) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты ϻǿиϻ хуᴇϻ пᴇрᴇбитый) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты сǿсᴇшь , ᴀ ϻǿй хуй нᴇ цᴇнит этǿгǿ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿю ϻᴀть ǿт ϻǿᴇгǿ хуя прᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ пᴇрᴇгнул ҝᴀҝ жᴇлᴇзǿ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть прǿϻᴇж яиц зᴀжᴀл) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я тᴇбᴇ тᴇϻпᴇрᴀтуру хуᴇϻ сбивᴀю) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прихуярил ҝᴀҝ ϻуху) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ты пǿд ϻǿиϻи яйцᴀϻи прячᴇшься ҝᴀҝ пǿд зǿнтиҝǿϻ) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ϻᴀть твǿю в пǿдвᴀлᴇ ᴇбу ҝᴀҝ хǿчу) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]",
                " ǿпрᴀҝину твǿю ϻᴀть с хуя свǿᴇгǿ щᴀс) ⼂가[<emoji document_id=5352585602317426381>💀</emoji>]" ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)


    async def lordovcmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный  модуль Lordov прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль Lordov начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lordov</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon1 = [
        
        '<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏⲙυⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲱⲉю ⲡⲁⲅⲁⲏⲩю ⲣⲁⳅьⲉⳝёⲧ ⲏⲁⲭⲩύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲃⲧⲟύ ⲣⲟⲧ ⲏⲉⲃⲉⲗυⲣⲟⲃⲁⲧь ⲕⲁⲕ ⲭⲩⲉⲥⲟⲥ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲩⲧⲕⲁ ⲉⳝⲁⲏⲁя ⲙⲏⲉ ⲧⲃⲟύ ⲣⲟⲧ ⲇⲣⲉⲗью ⲣⲁⳅьⲉⳝⲁⲧь?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲃ ⲗⲉⲥⲩ ⳅⲁⲣⲟю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲉⳝⲉ ⲏⲟⲅυ ⲃ ⲣⲟⲧ ⲕⲗⲁⲗ ⲡυⲇⲁⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲣⲟⲥⲧⲣⲉⲗυⲗ ⲕⲁⲕ ⲥ ⲇⲃⲩⲭ ⲥⲧⲃⲟⲗⲕυ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥыⲏ ⳝⲗⲩⲇⲏⲟύ ⲱⲗюⲭυ?) ⲙⲟύ ⲧⲉⲗⲉⲫⲟⲏ ⲕⲟⲅⲇⲁ ⲣⲟⳅⲣяⲇυⲧⲥⲁ я ⲥⲩю ⲡⲣⲟⲃⲟⲇ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃ ⲃⲗⲁⲅⲁⲗυⳃⲉ υ ⲟⲏ ⳅⲁⲣяⲇⲯⲁⲉⲧⲥⲁ ⲁ ⲃⲥⲉ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧю ⲥⲃⲉⲧⲁ υ ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⲧⲉⲣⲥя ⲟⳝ ⲕⲣⲁυ ⲡυⳅⲇυ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳡⲧⲟ ⲧⲁⲙ ⲡⲟⲱⲗⲟ ⲉⲗⲉⲕⲣυⳡⲉⲥⲧⲃⲟ ?) ⲉⳝⲁⲏыύ ⲧы ⲭⲩⲉⲡⲗⲉⲧ ⲧы ⲇⲃⲁ ⲥⲗⲟⲃⲁ ⲥⲃяⳅⲁⲧь ⲏⲉ ⲙⲟⲯⲉⲱь ⲧы ⲙⲟύ ⲭⲩύ ⲏⲁⲥⲟⲥⲁⲗⲥя?)ⲃыⲉⳝⲁⲏⲏⲟⲉ ⲯυⲃⲟⲧⲏⲟⲉ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲟⳝⲣыⲅⲁⲏⲏⲟⲉ ⲉⳝⲁⲗⲟ  я ⲕⲟⲅⲇⲁ υⲅⲣⲁⲗ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲃ ⲡυⲏⳝⲟⲗ я ⲥⲧⲣⲉⲗьⲏⲩⲗ эύ ⲃ ⲡυⳅⲇⲩ ⲧⲉⲡⲉⲣь ⲩ ⲏⲉύⲟ ⲡυⳅⲇⲁ ⳅⲇⲉⲗⲁⲗⲁⲥь ⲕⲣⲁⲥⲏⲟύ я ⲉⳃⲉ ⲕⲟⲅⲇⲁ ⲕⲟⲏⳡⲁю ⲧⲩⲇⲁ ⲥⲧⲁⲏⲟⲃυⲧⲥⲁ ⲫⲗⲁⲅ ⲡⲟⲗьⳃυ ⲉⳝⲁⲏыύ ⲧы ⲃⲟⲇⲟⲗⲉύ ⲕⲟⲧⲟⲣыύ ⲏⲁⲡⲣυⲅⲏⲩⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲡⲣⲟⲥυⲗ ⳡⲧⲟⳝы я ⲧⲉⳝя ⲡⲟⲕⲁⲧⲁⲗ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲧ ⲏⲁ ⲧⲃⲟⲉⲙ ⲣⲧⲩ ⲡⲣⲉⲇⲥⲕⲁⳅыⲃⲁⲁⲧь ⲧⲉⳝⲉ ⳝⲩⲇⲩⳃυⲉ ⲧⲟ)?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲙⲟⲯⲏⲟ ⲣⲟⳅⲃⲟⲇυⲧь ⲥⲃυⲏⲉύ ⲏⲁⲭⲩύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃⲧⲟю ⲙⲁⲧь ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲩ ⲥⲟⲃⲙ ⲭⲩⲉⲙ ⲗⲉⳡυⲧьь ⲕⲁⲕ ⲇⲟⲕⲧⲟⲣ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲩⲯⲉ ⲩⲥⲧⲁⲗ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲧⲁь υ ⲩⲙⲉⲣⲁⲉⲱьⲥ ⲙⲏⲉ ⲡⲣⲙ ⲃ яύцⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲡⲟⲅυⳝⲏυⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲅⲉⲣⲟύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⲥⲉύⳡⲁⲥⳝⲩⲇⲩ ⲥⲟⲃυⲙ ⲭⲩⲉⲙ ⲕⲁⲥⲧυⲣⲟⲃⲁⲧь ⲕⲗⲧⲟⲣ ⲉё)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲧ ⲡⲟⲕⲁⳅыⲃⲁⲧь ⲃ ⲕⲁⲕⲟύ ⲥⲧⲟⲣⲟⲏⲉ ⲧы ⲉⲅⲟ ⲥⲟⲥⲁⲗ) ⲡⲟⲧⲟⲙ ⲕⲣⳡ ⲧы ⲡⲣυύⲇⲉⲱь ⲏⲁ ⲧⲟ ⲙⲉⲥⲧⲟ ⲥⲧⲁⲏⲉⲱь ⲣⲁⲕⲟⲙ υ ⲥⲕⲁⲯⲉⲱь ⳡⲧⲟ ⳝы ⲃⲉⳝⲁⲗ ⲧⲉⳝ0 ⲁ ⲕⲣⳡ ⲏⲟⲅⲟύ ⲧⲉⳝⲉ ⲡⲟ ⲉⳝⲁⲗьⲏυⲕⲩ ⲇⲁⲙ υⲥ ⲕⲁⲯⲩ ⳡⲧⲟ ⳝы ⲡⲟⲱⲉⲗ ⲏⲁⲭⲩύ ⲟⲧ ⲥюⲇⲁ)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲏⲉ ⲥⲡⲣⲁⲱυⲃⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧью ⲥⲃⲉⲧⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ, ⲩ ⲏⲉⲉ ⲁⲯ ⲡυⳅⲇⲁ ⳅⲁⲅⲟⲣⲉⲗⲁⲥь??   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⳃⲁ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲗⲟⲯⲩ ⲧⲟⲣⲅⲟⲃыⲉ ⲡⲩⲧυ ⲕ ⲡυⳅⲇⲁⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲉⳝя ⲉⳝⲁⲗυ ⲭⲁⳡυ ⲕⲟⲅⲇⲁ ⲧⲃⲟύ ⲟⲧⲉц ⲙⲁⲥⲥυⲣⲟⲃⲁⲗ ⲙⲏⲉ яυцⲁ ⲥⲃⲟⲉύ ⲅⲩⳝⲟύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲃъⲉⳅⲯⲁⲉⲱь ⲏⲁ ⲙⲟύ ⲭⲩύ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲩⲇυⳝυⲗⲇⲉⲣ ⲙⲟⲉⲅⲟ ⲭⲩя ⲧы ⳅⲏⲁⲗ?()   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲉⳝя ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⳝⲟⲙⳝⲩⲕⲟⲃⲟύ ⲣⲟⳅⲉύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲗⲭⲟⳅⲏυцⲁ ⲉⳝⲁⲏⲁя ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲡяⲗⲱⲉⲧ ⳡⲉⳡёⲧⲕⲩ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲟⲥёⲧ ⲙⲟύ ⲭⲩύ ⲡⲟⲇ ⲣⲩⲥⲥⲕυύ ⳝυⲧ ⲥⲧⲁⲥⲁ ⲙⲉⲭⲁύⲗⲟⲃⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲙⲁⲣⲉⲟⲏⲉⲧⲕⲁ ⲉⳝⲁⲏⲁя ⲡⲟⲇ ⲙⲟύ ⲭⲩύ ⲭⲟⲇυⲱь   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲏⲁⲭⲩύ ⲧы ⲙⲟύ ⲭⲩύ ⲕⲗⲁⲇⲉⲱь ⲥⲉⳝⲉ ⲃ ⲣⲟⲧ,ⲧⲉⳝⲉ ⲏⲣⲁⲃυⲧⲥя ⲃⲕⲩⲥ ?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲥⲟⲡⲁⲅⲟⲙ ⲉⳝⲁⲗ ⲡⲟύⲙυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ ⲟⲧⲇⲁⲗⲁⲥь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲡⲣυ ⲗⲩⲏⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥⲉⲧ) я ⲧⲃⲟю ⲙⲁⲧь ⲇⲟⲱυⲣⲁⲕⲟⲙ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥⲉⲧ)я ⲧⲃⲟю ⲙⲁⲧь ⲥⲡυⳡⲕⲁⲙυ ⲉⳝⲩ)   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ыⲧ ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⳝⲩⲇⲩ ⳅⲁ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ ⲉⳝⲁⲧь) ⲧы ⲃⲟⲧ ⲭⲩⲗυ ⲕⲁⳡⲁⲉⲱь ⲙыⲱцы ⲙⲟⲉύ ⲕⲟⳡⲏⲟύ ⲧⲟ?) ⲧы ⲇⲩⲙⲁⲉⲱьⳡ ⲧⲟ ⲙⲟⲉύ ⲕⲟⳡⲏⲟύ ⲙⲟⲯⲏⲟ ⲏⲁⲕⲁⳡⲁⲧь ⲧⲉⲗⲟ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⳡⲉⲙⲩ ⲧы ⲏюⲭⲁⲗⲗ ⲙⲟю ⲕⲟⲏⳡⲩ ⲧⲟ?)??ⲧы ⲥⲩⲕⲁ ⲏⲁⲣⲕⲟⲙⲁⲏ ⲉⳝⲁⲏύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲡⲟⲡⲁⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲏⲁ ⲣⲁύ ⲧⲟ υ ⲏⲁⳡⲁⲗ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲉⲅⲟ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ыⲧ ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲥⲩⲕⲁ ⲟⲧⲥⲟⲥⲁⲗ ⲙⲟύ ⲭⲩύ υ ⲧⲉⲡⲉⲣь ыⲧ ⲥⲩⲕⲁ ⲫⲉύⲗυⲱьⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲕⲁⲕ ⲇⲏⲁⲣ ⲉⳝⲁⲏыύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲥⲉύⳡⲁⲥ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲏⲁⲧяⲏⲩ ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ) ⳡⲧⲟⳝы ⲕⲣⲁⲥυⲃⲉⲉ ⲥⲧⲁⲗ0  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲡⲟⲇⲥⲟⲥ ⲙⲟⲉⲅⲟ ⲭⲩя, ⲕⲟⲧⲟⲣыύ ⲡⲣⲁⲃυⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲥⲡⲉⲣⲙⲟⲅⲗⲟⲧ ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲡⲟ ⲧⲃⲟⲉⲙⲩ ⲉⳝⲁⲗⲩ ⲭⲩⲉⲙ ⲧⲟⲣⲙⲟⳅυⲗ,υ ⲥⲧⲉⲣ ⲧⲟⲣⲙⲟⳅⲏыⲉ ⲕⲟⲗⲟⲇⲕυ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃⲟⲧ ⲧы ⲥⲩⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя) ⲧы ⳝⲗяⲧь ⲡⲟⲡⲩⲧⲁⲗⲁ ⲃⲥⲉ ⲏⲁⲭⲩύ) ⳅⲁⳡⲉⲙ ⲧы ⲃ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲥⲕⲗⲁⲇυⲣⲩⲉⲱь ⲇⲣⲁⲃⲁ ⲏⲁ ⳅυⲙⲩ? ⲇⲗя эⲧⲟⲅⲟ ⲉⲥⲧь ⲥⲁⲣⲁύ) ⲧⲩⲡⲁя ⲧы ⲱⲗюⲭⲁ) ⲧы ⲉⳃⲉ ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲕⲁⲙυⲏ ⳅⲁⲙⲩⲧυ) ⳡⲙⲟ ⲧы ⲏⲉⲇⲟⲣⲁⳅⲃυⲧⲟⲉ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲉⳝя ⲉⳝⲁⲗ ⲃ ⲡⲟⲇⲃⲁⲗⲉ ⲏⲁ ⲅⲏυⲗⲟⲙ ⲥⲧⲩⲗⲉ) ⲧы ⲧⲃⲁⲣь ⲉⳝⲩⳡⲁя) ⲁ ⲏⲩ ⲏⲁⲭⲩύ ⲡⲟⲱⲉⲗ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳅⲏⲁⲉⲱь,ⲕⲟⲅⲇⲁ я ⲩⲃυⲇⲉⲗ ⲧⲃⲟю ⲡυⳅⲇⲩ, я ⲡⲟⲇⲩⲙⲁⲗ, ⲡⲟⳡⲉⲙⲩ ⳝы ⲧⲁⲙ ⲏⲉ ⲡⲟⲥⲧⲟⲣυⲧь ⲏⲟⲃыύ ⲅⲟⲣⲟⲇ? ⲟⲭⲩⲉⲏⲏⲁя υⲇⲉя! ⲧⲁⲙ ⲙⲏⲟⲅⲟ ⲙⲉⲥⲧⲟ) ⲡⲟⲥⲧⲣⲟυⲙ ⲅⲟⲣⲟⲇ) ⲏⲉⲉⲉ,ⲥⲧⲟύ,ⲥⲧⲣⲁⲏⲩ! υ я ⳝⲩⲇⲩ ⲉύ ⲡⲣⲁⲃυⲧь) υⲥⲭⲟⲇя υⳅ ⲃⲥⲉⲅⲟ эⲧⲟⲅⲟ,ⲡⲟⲗⲩⳡⲁⲉⲧⲥя,ⳡⲧⲟ я ⲡⲣⲁⲃⲗю ⲧⲃⲟⲉύ ⲡυⳅⲇⲟύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳅⲏⲁⲉⲱь ⳡⲧⲟ? ⲥыⳝⲁⲗⲁⲥь ⲏⲁⲭⲩύ ⲥ ⲙⲟυⲭ ⲅⲗⲁⳅ) ⲱⲗюⲭⲁ ⲧы ⲉⳝⲁⲏⲏⲁя) я ⲧⲉⳝя ⲥⲉύⳡⲁⲥ ⲧⲩⲧ ⲏⲁⲭⲩύ ⳅⲁⲣⲉⲯⲩ,ⲕⲁⲕ ⲱⲁύⲧⲁⲏ, ⲧⲃⲁⲣυⲏⲁ ⲧы ⲟⳝⲟⲥⲁⲏⲏⲁя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱ! ⲧы ⲟⲗⲉⲏь ⲉⳝⲁⲏⲏыύ) я ⲧⲉⳝⲉ ⲃⲥⲉⲅⲇⲁ ⳝⲩⲇⲩ ⲣⲁⲇ ⲇⲁⲧь ⲡⲟⲥⲟⲥⲁⲧь)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗя, ⲡυⳅⲇⲁ ⲧⲩⲡⲁя, ⲧы ⳡⲉ ⲥⲩⲕⲁ ⲏⲁⲭⲩύ ⲃъⲉⳝⲁⲗⲁⲥь ⲡⲟ ⲡⲟⲗⲏⲟύ? я ⲧⲉⳝⲉ ⲥⲉύⳡⲁⲥ ⲡυⳅⲇⲩ ⲧⲃⲟю ⲏⲁⲭⲩύ ⲥⲕⲣⲩⳡⲩ,ⲡⲟⲧⲁⲥⲕⲩⲱⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя) υⲇυ ⳝⲁⲏⲁⲏы ⲃⲟⲣⲩύ,ⲯυⲃⲟⲧⲏⲟⲉ ⲧы ⲭⲩⲉⲥⲟⲥⲏⲟⲉ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲁⲗⲕⲟⲉ ⲭⲩⲉⲡⲟⲧⲁⲗⲟ) ⲡⲉⲣⲉⲥⲧⲁⲏь ⲭⲩυ ⲥⲟⲥⲁⲧь) ⲡυⲇⲁⲣⲥⲕⲁ) я ⲧⲉⳝя ⲥⲉύⳡⲁⲥ ⲏⲁ ⲭⲩю ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ ⲣⲁⲥⲡⲏⲩ, ⲕⲁⲕ υυⲥⲩⲥⲁ ⲭⲣυⲥⲧⲁ ⲏⲁ ⲕⲣⲉⲥⲧⲉ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲁ ⳅⲁⳡⲉⲙ ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲃⲟ ⲃⲣⲉⲙя ⲙυⲏⲉⲧⲁ ⲡⲟⲕⲩⲥыⲃⲁⲉⲱь   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲙⲟύ ⲭⲩύ ⲩⳅⲏⲁⲗⲁ,ⲥⲣⲉⲇυ ⲧыⲥяⳡυ? ⲥⲣⲁⳅⲩ ⲩⲃυⲇⲉⲗⲁ ⲧⲟ,ⳡⲧⲟ ⲡⲣυⲏυⲙⲁⲉⲱь ⲃ ⲣⲟⲧ ⲕⲁⲯⲇыύ ⲇⲉⲏь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃⲟⲧ ⲥⲕⲁⲯυ ⲙⲏⲉ ⲟⲇⲏⲟ) ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲙⲁⳅⲁⲗⲁ? ⲇⲁ, я ⲡⲟⲏυⲙⲁю,ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳝⲟⲗьⲱⲟύ,ⲏⲟ ⲁⲏⲁⲗ ⲧⲁ ⲉⲉ ⳝⲟⲗьⲱⲉ) ⲧⲁⲙ ⲭⲟⲇяⲧ ⲥⲗⲩⲭυ ⲥⲧⲟⲗьⲕⲟ ⲭⲩⲉⲃ ⳅⲁⲧⲉⲣяⲗⲟⲥь)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲙⳡⲁⲗ ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧь 300 ⲕⲙ ⲃ ⳡⲁⲥ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲩⲕⲁ ⲕⲁⲕ ⲇⲉⲙⲟⲏ ⲉⳝⲁⲏыύ) ыⲧ ⲏⲉ ⲩⲥⲧⲁⲗ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩ?) ⲙⲟⲯⲉⲧ ⲡⲟύⲇⲉⲱь ⲡⲣυⲗⲯυⲱь ⲏⲁ ⲙⲟυ ύцⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲗⲟⲃυⲧь ⲣыⳝⲩ ⲃ ⲡⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲥⲩⲕⲁ ⲅⲉⲣⲟύ) ⲕⲟⲧⲟⲣыύ ⲟⲧⲥⲟⲥⲁⲗ ⲙⲟύ ⲭⲩύ υ ⲣⲁⲥⲥⲕⲁⳅⲁⲗ ⲥⲟⲥⲉⲇяⲙ ⲧⲟ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲉύⳡⲁⲥ ⳡυⲥⲧυⲧь ⲁⲏⲁⲗьⲏыύ ⲕⲁⲏⲁⲗы ⲧⲃⲟⲉύ ⲙⲁⲙы ⲧⲟ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⳡⲉⲙⲩ ⲕⲟⲅⲇⲁ ⲡⲣυⲭⲟⲇυⲱь ⲥⲟ ⲱⲕⲟⲗы ⲧⲟ ⲃⲥⲉⲅⲇⲁ ⲥⲁⲇυⲱьⲥ ⲏⲁ ⲙⲟύ ⲭⲩύ) ⲟⲧⲇⲟⲭⲏⲩⲧь ⲱⲟⲗυ υ ⲥⲏⲧь ⲥⲧⲣⲉⲥ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ⲡⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙы ⳝⲩⲇⲉⲧ ⳝⲉⲗⲁ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲕⲟⲏⳡⲩ ⲏⲁ ⲏⲉё?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⳃⲁ ⳡⲉⲣⲉⳅ ⲥⲃⲟύ ⲭⲩύ ⲡⲩⳃⲩ эⲗⲉⲕⲧⲣⲟ ⳅⲁⲣяⲇ ⲧⲉⳝⲉ ⲃ ⲙⲟⳅⲅ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃⲕⲣⲩⲧυⲗ ⲗⲁⲙⲡⲟⳡⲕⲩ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⳡⲉⲣⲉⳅ ⲙⲟύ ⲭⲩύ ⲡⲣⲟⲗυⲃⲁⲉⲧⲥя ⲕⲁⲕ ⲃⲟⲇⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲃⲉⲇⲣⲟⲙ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲥⲁⲗⲁⲧⲟⲙ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲧь ⲧⲃⲟю ⲫⲉⲏⲟⲙ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲧь ⲧⲃⲟю ⲕⲁⲣⲧⲟⲱⲕⲟύ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲧь ⲧⲃⲟю ⲅⲣⲉⳡⲕⲟύ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲙⲕⲁ ⲧⲃⲟя ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲏяⲗⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲧь ⲧⲃⲟю ⲃ ⳝⲟⲗьⲏυцⲉ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ ⲩ ⲏⲉⲉ ⲁⲯ ⲡυⳅⲇⲁ ⳅⲁⲇыⲙυⲗⲁⲥь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲟя ⲕⲟⲏⳡⲁ ⳅⲁⲙⲉⲏяⲉⲧ ⲕⲣⲟⲃь ⲃ ⲧⲃⲟⲉⲙ ⲧⲉⲗⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲕⲩⲣⲥⲉ ⳡⲧⲟ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ ⲯυⲃⲩⲧ ⲅⲏⲟⲙы?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃⲟⲧ ⳅⲁⳡⲉⲙ ⲧы ⲧⲁⲕ ⲏⲁⲕυⲇыⲃⲁⲉⲱьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲟⲃⳡⲁⲣⲕⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲏⲁⲭⲩύ ⲧы ⲡⲣⲟⲃⲟⲇυⲗ ⲧⲉⲥⲧ ⲇⲣⲁύⲃ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⲇⲟⲣ ⲟⲅⲏⲉⲇыⳃⲁⳃυύ υⲇυ ⲥюⲇⲁ я ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> яⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲏⲁ ⲙⲟⲣⲟⳅⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⳝыⲗⲁ ⲡьяⲏⲁя υ ⲥⲕⲁⲕⲁⲗⲁ ⲏⲁ ⲙⲟⲉю ⲭⲩю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲉ ⲡⲟⲏяⲗ ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⲁⲗьⲏⲟ ⳃⲁⲥ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⳝⲩⲇⲉⲧ)   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲭⲩя ⲡⲩⲥⲕⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲥⲏⲟⲃⲁ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲣυⳅⲉⲙⲗυⲗⲁⲥь ⲡⲟⲥⲗⲉ ⲡⲟⲗёⲧⲁ ⲃ ⲧⲁⲇⲯυⲕυⲥⲧⲁⲏ ⲏⲁ ⲣⲟⲇυⲏⲩ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⳡⲉⲙⲩ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⳅⲁⲧяⲅυⲃⲁⲉⲧ ⲭⲩυ, ⲕⲁⲕ ⲧⲣⲉⲩⲅⲟⲗьⲏυⲕ ⳝⲉⲣⲙⲩⲇⲥⲕυύ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲡыⲗⲉⲥⲟⲥⲟⲙ ⲉⳝⲁⲗ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲭⲩя ⳡⲉⲣⲉⳅ ⳅⲁⳝⲟⲣы ⲡⲉⲣⲉⲕυⲇыⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⳅьⲙυ ⲥⲉⳝⲉ ⲃ ⳅⲩⳝы ⲗⲉύⲕⲩ υ ⲡⲟⲗυⲃⲁύ ⲟⲅⲟⲣⲟⲇы ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲣⲁⲕⲟⲃⲩю ⲟⲡⲩⲭⲟⲗь ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲩⲥⲧⲣⲟⲏяⲗ ⲡⲣυ ⲡⲟⲙⲟⳃυ ⲥⲃⲟⲉⲅⲟ ⲭⲩя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲟⲅⲇⲁ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲇⲉⲧ ⲁⲏⲅυⲏⲁ ⲡⲟⳅⲟⲃυ ⲙⲉⲏя я ⳝⲩⲇⲩ ⲉύ ⲃ ⲅⲟⲣⲗⲟ ⳝⲣы3ⲅⲁⲧь ⲥⲃⲟⲉύ ⲥⲡⲉⲣⲙⲟύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲅⲣⲩⲇⲏⲩю ⲕⲗⲉⲧⲕⲩ ⲭⲩⲉⲙ ⲣⲁⲥⲥⲡυⲗυⲃⲁⲗ ⲡⲟⲡⲟⲗⲁⲙ υ ⲥⲧⲉⲗυⲗ ⲡⲟⲇ ⲥⲃⲟυⲙυ ⲇⲃⲉⲣьⲙυ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳅⲁⳡⲉⲙ ⲧы ⲣⲧⲟⲙ ⲏⲁ ⲭⲩύ ⲩⲡⲁⲗ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⳅⲁ ⳝⲁⲣⳝⲁⲣυⲥⲕⲩ ⲭⲩύ ⲥⲟⲥⲉⲧ ⲏⲁ ⲣыⲏⲕⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲉύ ⲗⲉⳡυⲗ ⲣⲁⲕ ⲅⲩⳝы ⳅⲁⲗⲩⲡⲟύ ⲟⲏⲁ ⲡⲟⲗⳝюⳝυⲗⲁ ⲉⲅⲟ ⲥⲕⲟⲣⲟ ⲙⲟύ ⲭⲩύ ⲧы ⲥⲙⲟⲯⲉⲱь ⲏⲁⳅыⲃⲁⲧь ⲡⲁⲡⲕⲟύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃⲟⲧ ⲩ ⲧⲉⳝя яⲃⲏⲟ ⲡυⲇⲟⲣⲥⲕυⲉ ⲏⲁⲕⲗⲟⲏⲏⲟⲥⲧυ(   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲉⲏя ⲃⲇⲟⲭⲏⲁⲃⲗяⲉⲧ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁⲡⲁⲃⲱυύ ⲏⲁ ⲙⲟύ ⲭⲩύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲁⲕ ⲧы ⲟⲧⲏⲉⲥⲉⲱьⲥя ⲕ ⲧⲟⲙⲩ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲥⲧⲣяⲗ ⲃ 12 ⲡⲉⲣⲥⲧⲏⲟύ ⲕυⲱⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ??   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡυⳅⲇυⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲩⳝы ⲭⲩⲉⲙ ⲃыⳝυⲗ, ⲟⲏⲁ ⲧⲁⲕ ⲅⲟⲣьⲕⲟ ⲡⲗⲁⲕⲁⲗⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲕⲗυⳅⲙⲩ ⲥⲇⲉⲗⲁю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲭⲣⲉⳝⲉⲧ ⲗⲟⲙⲁю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲱⲉю ⲗⲟⲙⲁю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲗυⲧⲟⲣ ⲥ ⲏⲟⲅυ ⲃыⳝυⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕυⲣⲡυⳡυ ⲃ ⲉⳝⲗⲟ ⲕυⲇⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⳡⲉⲣⲇⲁⲕⲉ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲇⲃⲉⲣⲏⲟύ ⲣⲩⳡⲕⲉ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕⲁⲗυⲧⲕⲉ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⳝⲟⲣυⲏⲟύ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲕⲁⳡⲉⲣⲅⲟύ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲟⳝ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝыⳡⲕυ ⲧⲩⲱυⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲃⲟю ⲥⲉⲥⲧⲣⲩ ⲡⲟ ⲙⲟⲉⲙⲩ ⲥⲟⲅⲗⲁⲥυю ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲟⲯⲇⲁⳡⲕⲟύ ⲭⲩяⲣυⲗ ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧёⲣⲕⲟύ ⲧⲉⲣ ⲉⳝⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲟⳝⲟⲥⲥⲁⲗ ⲡⲟⲕⲁ ⲧы ⲕⲗυⲧⲟⲣ ⲥⲉⲥⲧⲣⲉ ⲗυⳅⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟю ⲙⲁⲧь ⲟⲥⲩⲇυⲗυ ⲡⲟⲯυⳅⲉⲏⲏⲟ ⳅⲁ ⲡⲟⲥυⲇⲉⲗⲕυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲥ 5 эⲧⲁⲯⲁ ⲡⲁⲇⲁⲗⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲭⲩⲉⲙ ⲃ ⲅⲗⲁⳅ ⲧыⲕⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲉⳝⲗⲟ ⲕⲟⲏⳡⲁⲗ ⲡⲟⲕⲁ ⲧы ⲭⲩύ ⲟⲧцⲁ ⲥⲟⲥⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲃⲟю ⲙⲁⲧь ⲩⳡυⲗ ⲭⲩύ ⲥⲟⲥⲁⲧь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⲅⲩⳝⲉ ⲇⲁⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⳃⲉⲕⲉ ⲩⲇⲁⲣυⲗ , ⲩ ⲏⲉⲉ ⳡⲉⲗюⲥⲧь ⲥⲗⲟⲙⲁⲗⲁⲥь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲗⳝⲩ ⲭⲩяⲣυⲗ ⲡⲟⲕⲁ ⲧы ⲙⲏⲉ яύцⲁ ⲗυⳅⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁ ⲇⲉⲏьⲅυ ⲥⲏυⲙⲁⲗ, ⲡⲟⲥⲗⲉ ⲟⲧⲇⲁⲃⲁⲗ ⳝⲟⲙⲯⲁⲙ υ ⲟⲏυ ⲉⲉ ⲡⲟ ⲕⲣⲩⲅⲩ ⲉⳝⲁⲗυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⳝⲗяⲇь, ⲁ ⲧⲃⲟύ ⲟⲧⲉц ⲣⲁⳝⲟⲧⲁⲉⲧ ⲃ ⲅⲉύ ⲕⲗⲩⳝⲉ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲣⲟⳅⲩ ⲃⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧыⲕⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲕⲁⲕ ⳅⲁⲥⲟⲭⲱυύ ⲗυⲥⲧ ⲥ ⲇⲉⲣⲉⲃⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲡⲗⲟⲥⲕⲟⲅⲣⲩⲇⲏⲁя ⲉⳝⲁⲏⲁⲱⲕⲁ ⲥⲩⲕⲁ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲗⲟ ⲏⲁⲧяⲅυⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲅυⲃⲁⲗ, ⲟⲏ ⲥⲧⲁⲏⲟⲃυⲗⲥя ⲇⲗυⲇⲏⲏыύ ⲕⲁⲕ ⳅⲙⲉя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲕ ⲡⲟⲧⲟⲗⲕⲩ ⲡⲣυⳝυⲃⲁⲗ υ ⲭⲁⲣⲕⲁⲗ ⲉύ ⲃ ⲉⳝⲗⲟ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲱⲁⲙⲡⲩⲣⲟⲙ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁ ⳃⲉⲕⲩ ⳅⲁ ⳅⲁⳝⲟⲣⲟⲙ ⲇⲁⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲡυⳅⲇⲟύ ⲕⲁⲣⲧⲟⲱⲕⲩ ⲥⲟⲣⲧυⲣⲟⲃⲁⲧь ⲩⲙⲉⲉⲧ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⳡⲉⲣⲉⳅ ⲡⲣⲟⲅυⳝ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲕⲩⲣⲥⲉ ⳡⲧⲟ я ⳃⲁⲥ ⲧⲃⲟю ⲙⲁⲧь ⳡⲗⲉⲏⲟⲙ ⲟⲧⲡυⳅⲇυⲗ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲭⲗⲉⳝ ⲥⲟⲥⲁⲗⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲟⲇⲉⲯⲇⲩ ⲥⲟⲥⲁⲗⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲣⲩⳝⲗь ⲟⲧⲇⲁⲗⲁⲥь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲣυⲭⲗⲟⲡⲏⲩⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲗⲉⲏⲟⲙ ⲡⲟⲥⲗⲉⲇⲏυⲉ ⳅⲩⳝы ⲃыⳝυⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲟⳝⲗυⳅыⲃⲁⲉⲱь ⲙⲏⲉ ⳡⲗⲉⲏ ⲡⲟⲥⲗⲉ ⲁⲏⲁⲗьⲏⲟⲅⲟ ⲥⲉⲕⲥⲁ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟⲗυⲃⲁⲉⲱь ⲕⲁⲕ ⲟⲅⲟⲣⲟⲇ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳝⲗⲟ ⲟⳝ ⲁⲥⲫⲁⲗьⲧ ⲣⲁⳅъⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲉⳝⲗⲟ ⲭⲁⲣⲏⲩⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲗυⲱⲩ ⲧⲉⳝя ⲇⲉⲃⲥⲧⲃⲉⲏⲏⲟⲥⲧυ, υ ⳝⲩⲇⲩ ⲣⲉⳅⲁⲧь ⲧⲃⲟⲉ ⲇⲉⲃⲧⲥⲃⲉⲏⲏⲟⲉ ⲧⲉⲗⲟ ⲏⲟⲯⲟⲃⲕⲟύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲏⲁ ⲏⲟⲅⲁⲭ ⲏⲟⲅⲧυ ⲅⲣыⳅⲉⲧ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲅⲟⲣⲱⲟⲕ ⲥ ⲅⲟⲃⲏⲟⲙ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲇⲉⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟⲇⳃⲉⳡυⲏы ⲇⲁⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲅⲩⳝⲩ ⲥⲗⲟⲙⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲁ ⲉⳝⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲩⲥⲟⲣⲏыύ ⲡⲁⲕⲉⲧ ⲟⲇⲉⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲃ ⲧⲩⲭⲗⲟύ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲡⲁⲣыⲱⲉύ ⲣⲁⳅⲃⲟⲇυⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲟυⲙυ ⲅⲗⲁⲏⲇⲁⲙυ ⲙⲁⲱⲟⲏⲕυ ⳃⲉⲕⲟⳡυⲧ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲭⲩύ ⲡⲟⲗⲟⲥⲕⲁⲗ ⲃ ⲙⲟ3ⲅⲁⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲭⲩύ ⲃ ⲅⲟⲣⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲩⲃⲁⲗ , ⳡⲧⲟⳝ ⲟⲏⲁ ⲩ ⲏⲉⲉ ⲏⲉ ⲱⲁⲧⲁⲗⲁⲥь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⳡⲉⲣⲉⳅ ⲙⲟⳅⲅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲟⳡⲩ ⲫυⲗьⲧⲣⲟⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲡⲣυⲏυⲙⲁю эⲕⳅⲁⲙⲉⲏы, ⲁ ⲧⲃⲟя ⲙⲁⲙⲁ ⲇⲁёⲧ ⲙⲏⲉ ⲃⳅяⲧⲕⲩ ⲏⲁⲧⲩⲣⲟύ).   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲣⲃⲁⲗ ⲧⲉⳝⲉ цⲉⲗⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲯⲁⲃⲟύ ⲧⲣⲩⳝⲟύ :3   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲃⲟυⲙ яⳅыⲕⲟⲙ ⲃⲱⲉύ ⲗⲟⳝⲕⲟⲃыⲭ ⲏⲁ ⲡυⳅⲇⲉ ⲙⲁⲧⲉⲣυ ⲅⲟⲏяⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲅⲗυⲥⲧⲟⲃ υⳅ ⲯⲟⲡы ⲙⲁⲧⲉⲣυ ⲃыⲧⲁⲥⲕυⲃⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲃⲟύ ⲣⲟⲧ ⲕⲁⲕ ⲃⲁύ ⲫⲁύ) ⲕⲟⲧⲟⲣыύ ⲡⲣυⲏυⲙⲁⲉⲧ ⲧⲟⲗьⲕⲟ ⲭⲩυ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲧы ⲁⲏⲁⲗьⲏыύ ⳃⲁ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲃыⲕυⲏⲩ ⲕⲁⲕ ⲧⲣяⲡⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲟⲗⲉⲏь ёⳝⲁⲏⲏыύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲭⲩύⲗⲁⲏ ⲟⳝⲟⲥⲁⲏⲏыύ ⲧыⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲕⲥⲕⲩⲣⲥυю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲃⲟⲯⲩ?) ⲉⳝⲗⲁⲕ ⲥⲩⲕⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲟⳝⲟⲥⲁⲏⲏыύ ⲡⲣⲉⳅυⲣⲫⲁⲧυⲃ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲡυⳅⲇⲩ ⲕⲁⲕ ⲩ ⲇⲁⲗⲙⲁⲧυⲏⲉцⲁ ⲇⲉⲗⲁю?))  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱ ⳡυⲭⲟⲧⲕⲁ ⲉⳝⲁⲏⲏⲁ я ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⳝⲗяⲧь ⲁⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⲡⲣⲟⳡυⳃⲁⲧь ⲥⲃυⲏⲟⲙⲁⲧⲕⲁ ⲧы ⲟⳝⲟⲥⲣⲁⲏⲏⲁя  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟύ ⲣⲟⲧ ⲉⳝⲁⲗ)ⲕⲁⲕ ⲇяⲧⲉⲗ ⲇⲩⲡⲗⲟ)ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲁⲧ ⲉⳝⲁⲏⲏⲁя)ⲇⲁⲃⲁύ ⲃⲥⲁⲥыⲃⲁύ ⲙⲟⲣύ ⲭⲩύ)ⲉⳝⲁⲏⲏыύ ⲧы ⲡыⲗⲉⲥⳝⲟⲣⲏυⲕ)ⲧⲃⲟύ ⲟⲧⲉц ⲡυⲇⲟⲣⲁⲥ ⳅⲟⲟⲫυⲗ)ⲇⲁⲃⲁύ ⳝⲗяⲧь ⲭⲟⳝⲟⲧ ⲉⳝⲁⲏⲏыύ)ⲥⲟⲥυ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥⲟⲥⲕⲩ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲇⲃⲩⲗυⲕυύ ⲯⲟⲡⲟⲇⲣⲁⲏⲉц))) я ⳃⲁ ⲥⲇⲉⲗⲁю υⳅ ⲧⲉⳝя ⳅⲁⲃⲟⲇ ⲥⲁⲗⲟⲉⲇⲥⲕυύ υ ⲟⳝⲉⲥⲡⲉⳡⲩ ⲭⲟⲭⲗⲟⲃ ⲏⲁ ⳝⲉⲥⲕⲟⲏⲉⳡⲏыⲙυ ⳅⲁⲡⲁⲥⲁⲙυ ⲥⲁⲗⲁ)))  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇ ⲏυⲕⲟⲙ ⲡυⲇⲟⲣ ⲏⲁⲃⲉⲣⲏⲟⲉⲣⲁⲏьⲱⲉ ⳅⲁⲃυⲥⲁⲗ, я ⲥⲡⲣⲁⲃⲕυ ⲏⲁⲃⲉⲗ ⲧⲉⳝя ⲧⲁⲙ ⳅⲏⲁюⲧ ⲃⲥⲉ ⲧы ⳅⲁⳝυⲃⲁⲉⲱь ⲧⲁⲙ ⲥⲧⲣⲉⲗⲕυ ⲁ ⲡⲟⲧⲟⲙ ⲥⲟⲥⲉⲱь ⲃ ⲣⲉⲁⲗⲉ υ ⲧⲉⳝⲉ ⲣⲃⲩⲧ ⲟⳡⲕⲟ ⲏⲩ эⲧⲟ ⲕⲟⲏⲉⳡⲏⲟ ⲧⲃⲟя ⲯυⳅⲏь ⲧы ⲇⲉⲗⲁύ ⳡⲧⲟ ⲭⲟⳡⲉⲱь ⲙⲏⲉ ⲃ ⲡⲣυⲏцυⲡⲉ ⲥⲣⲁⲧь ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲗⲟ ⲥ ⲇυⲃⲁⲏⲁ ⲡⲟⲏⲟⲥⲟⲙ..ⲏⲟ ⲧы ⲥⲁⲙ ⲧⲟ ⲕⲁⲕ? ⲕⲁⲕ ⲧы ⲙⲁⲧⲉⲣυ ⲃ ⲅⲗⲁⳅⲁ ⲧⲟ ⲥⲙⲟⲧⲣυⲱь υ ⲟⲧцⲩ ⲕⲟⲅⲇⲁ ⲇⲟⲙⲟύ ⲣⲁⲥⲡⲉⲣⲇⲟⲗⲉⲏⲏыύ ⲡⲣυⲭⲟⲇυⲱь ⲥⲁⲇυⲱьⲥя ⲃⲉⳡⲉⲣⲟⲙ ⳅⲁ ⲥⲉⲙⲉύⲏыύ ⲩⲯυⲏ ⲁ ⲩ ⲧⲉⳝя ⲏⲁ ⲅⲩⳝⲁⲭ ⲥⲡⲉⲣⲙⲁ υ ⲇⲉⲣьⲙⲟⲙ ⲃⲟⲏяⲉⲧ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲅⲟⲃⲏⲟ ⳝⲗяⲧь ⲧы ⲅⲁⲏⲇⲟυⳅⲃυⲗυⲥⲧⲟⲉ)ⲙⲏⲉ ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲟⲡяⲧь ⳝⲗяⲧь ⲅⲡⲗⲁⳅⲏыⲉ яⳝⲗⲟⲕυ ⲭⲩⲉⲙ ⲃыⲯυⲙⲁⲧь?ⲁⲗⲗⲉ ⳝⲗяⲧь)ⲁⲗυⳝⲁⳝⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩяⲭυⲗⲁ ⲧы ⲥ ⲕⲁⳅⲁⲏⲥⲕⲟⲅⲟ ⲃⲟⲕⳅⲁⲗⲁ)я ⳃⲁⲥ ⳝⲗяⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⲉ ⲁⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⳡυⲥⲧυⲧь)я ⳝⲗяⲧь ⲁⲏⲁⲗⲇьⲏыύ ⲙυⲥⲧⲉⲣ ⲡⲣⲟⲡⲉⲣ ⲇⲗя ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)ⲡⲟⲏυⲙⲁⲉⲱь ⲙⲉⲏя?ⲏⲉ ⳅⲁⲅⲗⲁⲧыⲃⲁύ ⲙⲏⲉ)ⲗⲁⲇⲏⲟ?ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉⲙ ⲁⲏⲁⲗⲉ ⲕⲁⲕ ⲃⲉⲏⲧυⲗяⲧⲟⲣ ⳝⲟⲗⲧⲁⲉⲧⲥя)ⲟⲏ ⳝⲗяⲧь ⲃ ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⳅⲁⲗⲉⲧⲉⲗ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⳡυⲥⲧυⲧь)я ⳝⲗяⲧь ⲁⲏⲁⲗⲇьⲏыύ ⲙυⲥⲧⲉⲣ ⲡⲣⲟⲡⲉⲣ ⲇⲗя ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)ⲡⲟⲏυⲙⲁⲉⲱь ⲙⲉⲏя?ⲏⲉ ⳅⲁⲅⲗⲁⲧыⲃⲁύ ⲙⲏⲉ)ⲗⲁⲇⲏⲟ?ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉⲙ ⲁⲏⲁⲗⲉ ⲕⲁⲕ ⲃⲉⲏⲧυⲗяⲧⲟⲣ ⳝⲟⲗⲧⲁⲉⲧⲥя)ⲟⲏ ⳝⲗяⲧь ⲃ ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⳅⲁⲗⲉⲧⲉⲗ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲁⲗⲗⲉ ⳝⲗяⲧь)ⲕⲗяⳡⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲥⲟⲏⲏⲩю ⲁⲣⲧⲉⲣυю ⲡⲉⲣⲉⲯυⲙⲁю ⲟⳝⲟⲥⲁⲏⲏыύ ⲧы ⲙⲩⲇⲉⲏь)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲁ ⲃⲟⲧ ⲧы ⲙⲏⲉ ⲟⲧⲃⲉⲧь ⲏⲁ ⲃⲟⲡⲣⲟⲥ ⲡⲟⳡⲉⲙⲩ ⲧы ⲧⲁⲕⲟύ ⲉⳝⲁⲏⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲉⳝⲩⲧ ⲃⲥⲉ ⲃ ⲯⲟⲡⲩ ⲡⲟⲇⲣяⲇ)ⲅⲗυⲏⲟⲙⲉⲥ ⲧы ⲉⳝⲁⲏⲏыύ)ⲧⲃⲟя ⲅⲟⲗⲩⳝяⲧⲏя ⲡⲟⲧⲣⲉⲡⲁⲏⲁ ⲏⲁⲭⲩύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁⲃⲁύ ⲕⲣⳡ ⲙы ⲧⲃⲟю ⲙⲁⲧь ⲃⲙⲉⲥⲧⲉ ⲡⲟⲉⳝⲉⲙ я ⲇⲁⲙ ⲧⲉⳝⲉ ⲱⲁⲏⲥ)ⲉⲥⲗυ ⲏⲉ ⲥⲡⲣⲁⲃυⲱьⲥя я ⲟⲧⲡυⳅⲯⲩ ⲧⲉⳝя ⲥⲃⲟⲉύ ⳅⲁⲗⲩⲡⲟύ υ ⳅⲁⲥⲧⲁⲃⲗю ⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱ ⲧы ⲏⲁⲭⲩύ ⲉⲁⲏⲩⲧⲁя ⲧы ⲥⲕⲟⲣⲟⲡⲟⲥⲧυⲯⲏⲁя ⲙⲁⲏⲇⲁ)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⳃⲁⲥ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲧⲩⲭⲏⲉⲱь ⲕⲁⲕ ⲥⲡυⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳃⲁⲥ ⲃ ⲧⲃⲟⲉύ ⲉⳝⲁⲏⲩⲧⲟύ ⳝⲁⲱⲕⲉ ⳝⲗяⲧь ⲟⲥⲧⲁⲃⲗю ⲟⲅⲣⲟⲙⲏⲩю ⲇыⲣⲕⲩ υ ⳝⲩⲇⲩ ⲧⲩⲇⲁ ⲥⲩⲃⲁⲧь ⲥⲃⲟύ ⲭⲩύ)ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲙⲟⳅⲅⲁ ⲩ ⲧⲉⳝя ⲏⲉⲧⲩ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> эύ ⳝⲗⲉⲧ)ⲅⲟⲃⲏⲟ ⲧы ⲏⲁⲭⲩύ ⲟⲡⲩⳃⲉⲏⲏⲟⲉ)υⲇυ ⲥⲕⲗⲟⲏυⲥь ⲕ ⲙⲟυⲙ яύцⲁⲙ υ ⲥυⲇυ ⲧⲁⲙ ⲧυⲭⲟ)ⲥыⲏ ⲉⳝⲁⲏⲏⲟⲅⲟ ⲁⳝⲟⲣⲧⲁ)ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲏⲁ ⲥⲃⲟύ ⲕⲣⲉⲥⲗⲟ ⲕⲁⲧⲁⲗⲕⲉ ⲉⲇⲉⲧ ⲕⲟ ⲙⲏⲉ)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> я ⲕⲣⳡ ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲣⲁⲕⲟⲙ ⲥⲧⲁⲃυⲧь)ⲧⲟⲣⲧυⲗⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ эⲧⲩ ⲥⲧⲁⲣⲩⲭⲩ υⲏⲃⲁⲗυⲇⲕⲟύ ⲡⲣⲟⲥⲧⲟ ⲥⲇⲉⲗⲁⲗ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲏⲩⲥ)ⲧы ⲯⲉ ⳃⲁⲥ ⳝⲩⲇⲉⲱь ⲙⲟⲉ ⲅⲟⲃⲏⲟ ⲥ ⲗⲟⲡⲁⲧы ⲉⲥⲧь ⲉⳝⲁⲏⲏⲁя ⲧы ⳝⲗяⲧь ⲧюⲗⲉⲏυⲭⲁ υ ⲧы ⳃⲁⲥ ⲡⲣⲟⲥⲧⲟ ⳝⲩⲇⲉⲱь ⲉⳝⲁⲧьⲥя ⲃⲥⲣⲁⲧьⲥя ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> эээ ⲃⳃ)ⲧы ⲧⲁⲙ ⲃⲟⲟⳝⳃⲉ ⳅⲁⲃⲁⲗυⲥь ⲏⲁⲭⲩύ ⲧы ⳝⲗяⲧь ⲇⲁⲙⳝⲁ ⲉⳝⲁⲏⲏⲁя ⲟⳝⲟⲥⲥⲁⲏⲏⲁя υ ⲩⲏυⲯⲉⲏⲏⲁя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲉⲣⲉⳝυⲧⲁя ⲁⲏⲁⲗьⲏⲟ цⲉⲗυⲏⲇⲣυⲃⲉⲥⲕⲁя ⲏⲉⲃьⲉⳝυⳡⲉⲥⲕⲁя ⲙⲁⲏⲇⲁ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗυⲁ)ⲧы ⳝⲗяⲧь ⲡⲣⲟⲥⲧⲟ ⲉⳝⲁⲏⲏⲟⲉ ⲃыⲙя)ⲇⲁⲃⲁύ ⲕⲟⲣыⲧⲟ ⲉⳝⲁⲏⲏⲟⲉ ⲥьⲉυⲥь ⲡⲣⲟⲥⲧⲟ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⳡⲙⲟⲱⲏυцⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲟⲣυ ⳡⲉⲣⲃяⲕ ⲧы ⳝⲉⲱⲉⲏⲏыύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲁⲕⲥ-ⲧⲁⲕⲥ)ⲇⲁⲃⲁύ ⲕⲁ ⲧы ⲡⲟύⲇⲉⲱь ⲏⲁⲭⲩύ ⲟⳝьⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲁⲏⲇⲁ ⲕⲟⲧⲟⲣⲁя ⲧⲟⲗьⲕⲟ ⲙⲟⲯⲉⲧ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲣⲟⲱⲕυ яⳅыⲕⲟⲙ ⲡⲟⲇⲙⲉⲧⲁⲧь)ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ)ⲡыⲗⲉⲥⳝⲟⲣⲏυⲕ ⲉⳝⲩⳡυύ ⲡⲉⲣⲉⲥⲕⲩⳡυύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲁⲭⲁⲭⲁ)ⲧы ⳝⲗяⲧь ⲟⲡⲟⲥⲥⲩⲙ ⲉⳝⲁⲏⲏыύ ⲥьⲉⳝυⲥь ⳝⲗяⲧь ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⲏⲉ ⲇⲟⲥⲧυⲅ ⲧⲃⲟⲉⲅⲟ ⲉⳝⲁⲏⲏⲟⲅⲟ ⲁⲏⲁⲗⲁ)ⲧы ⳝⲗяⲧь ⲟⳝⲟⲥⲥⲁⲏⲏⲟⲉ ⲙⲩⲣⲗⲟ)ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⳝⲗяⲧь ⲟⲡⲩⳃⲉⲏⲏⲕⲁ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲭⲙ)ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲣⲟⲥⲧⲟ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⳡⲉⲣⲃь ⲏⲁⲃⲟⳅⲏыύ ⲏⲁⲭⲩύ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲩⲇⲩⲱⲉⲏⲏыύ ⳝⲗяⲧь)ⳅⲁⲭⲗⲉⳝⲏυⲥь ⲧы ⲩⲯⲉ ⲃ ⲙⲟⲉύ ⲙⲟⳡⲉ ⲥⲩⲕⲁ)ⲭыⲭыⲭыⲭ  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲥⲧⲁⲧυ ⲅⲏυⲇⲁ)ⲧы ⳝⲩⲇⲉⲱь ⲥⲃⲟⲉύ ⲙⲁⲙⲕⲟύ ⲏⲁ ⲣыⲏⲕⲉ ⲕⲁⲕ ⲡⲟⲙυⲇⲟⲣⲁⲙυ ⲧⲟⲣⲅⲟⲃⲁⲧь υⲗυ ⲕⲁⲕ?)я ⳡⲟⲧ ⳝⲗяⲧь ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ)ⳝυⳅⲏⲉⲥⲙⲉⲏ ⲧы ⲭⲩⲉⲃ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲟⲣ)ⲥⲗыⲱ ⲧы ⲏⲁⲭⲩύ ⳝⲗяⲧь ⲭⲟⳝⲟⲧ ⲉⳝⲁⲏⲏыύ)υⲇυ ⲟⲧⲥюⲇⲁ ⲏⲁⲭⲩύ ⲇⲁⲗьⲏⲉύ ⲇⲟⲣⲟⲅⲟύ ⳝⲗяⲧь ⲧⲃⲟⲉ ⲙⲉⲥⲧⲟ ⲏⲁ ⲥⲃⲁⲗⲕⲉ ⲉⳝⲁⲧь ⳅⲁⲃⲁⲗυ ⲏⲁⲭⲩύ ⳝⲗяⲧь ⲥⲃⲟύ ⲙⲩⲥⲟⲣⲟⲡⲣⲟⲃⲟⲇ υ ⲥьⲉⳝυⲥь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲉⲅⲗⲟⲧυⲏⲁ ⲧы ⳡⲉ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣⲁⲥⲕⲩⲇⲁⲭⲧⲁⲗⲁⲥь?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲱⲗюⲭⲁ ⲧы ⲉⳝⲁⲏⲁя) ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳡⲉⲣⲏⲩⳝю ⲇыⲣⲩ ⲥⲇⲉⲗⲁⲗ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝⲉ ⲕⲗυⲧⲟⲣ ⲏⲁ ⲧⲃⲟύ ⲩⲉⳝⲥⲕυύ ⲉⳝⲁⲗьⲏυⲕ ⲏⲁⲧяⲏⲩ, ⲱⲁⲗⲁⲃⲁ ⲉⳝⲁⲏⲁя?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲗυ ⲧы ⲙⲟύ ⲭⲩύ υⲅⲏⲟⲣυⲱь ⲕⲟⲏυⲏⲁ ⲉⳝⲁⲏⲁя?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳃⲁⲥ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲩⲇⲉⲱь ⲕⲣⲟⲱⲕυ яⳅыⲕⲟⲙ ⲟⳡυⳃⲁⲧь) ⲡыⲗⲉⲥⲟⲥ ⲉⳝⲁⲏыύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧⲩⲭⲩ ⲡⲟⲇ ⲉⲗⲕⲟύ ⲃ ⲭⲃⲟⲥⲧ ⲇⲟⲗⳝυⲗⲁ ⲡⲟⲕⲁ ⲧы ⲣⲁⲥⲥⲕⲁⳅыⲃⲁⲗⲁ ⲥⲧυⲭυ ⲇⲉⲇⲩ ⲙⲟⲣⲟⳅⲩ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⳅⲁⲥⲧⲩⲕⲁⲗⲁ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧю ⲃ ⲃⲁⲏⲏⲉ υ ⲧⲁⲙ ⲟⲏ ⲉⳝⲁⲗ ⲣⲉⳅυⲏⲟⲃⲩю ⳝⲁⳝⲩ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲏυⲟⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲕⲟⲃⲟⲣⲟⲇⲕⲩ ⲭⲩⲉⲙ ⲡⲟⲥⲁⲯⲩ υ ⳅⲁⲯⲁⲣю ⲕⲁⲕ яύцⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲏυⲟⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲭⲩⲉⲙ ⲡⲣⲟⳝυⲗⲁ ⲣⲁⲥⲥⲧⲟяⲏⲉυⲉ ⲙⲉⲯⲇⲩ ⲙⲉⲯⲇⲟύ υ ⲯⲟⲡⲟύ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⳝⲟяⲧⲥя ⲙⲉⲏя ⲇⲟⲗⲯⲉⲏ υⳝⲟ ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲱⲗюⲭⲁ ⲥⲡυⲇⲟⳅⲏⲁя ⲧы ⲭⲟⲧь ⲡⲟⲏυⲙⲁύ ⳡⲧⲟ ⲇⲉⲗⲁⲧь ⲏⲁⲇⲟ υⲗυ ⲧы ⲥⲟⲃⲥⲉⲙ υⳅ-ⳅⲁ ⲭⲩⲉⲃ ⲅⲟⲗⲟⲃⲩ ⲡⲟⲧⲉⲣяⲗ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲏⲉ ⲥⲩύ ⲥⲃⲟύ ⲏⲟⲥ ⲃ ⲃⲁⲅυⲏⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲧⲁⲕ ⲕⲁⲕ ⲟⲏⲁ ⳅⲁⲏяⲧⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⲥⲗυ ⲏⲉ ⲭⲟⳡⲉⲱь эⲧⲟⲅⲟ ⲃυⲇⲉⲧь υⲇυ ⲇⲣⲟⳡυ ⲏⲁ ⲥⲃⲟⲉ ⲫⲟⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲅ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲡⲟⲇⲗυⳅⲁⲗ ⲃ 45 ⲕⲟⲅⲇⲁ ⲅυⲧⲗⲉⲣ ⲭⲟⲧⲉⲗ ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⳅⲁⲥⲧⲣⲉⲗυⲧⲥя ⲩ ⲧⲉⳝя ⳡⲧⲟ ⲥⲟⲃⲥⲉⲙ ⲙⲟⳅⲅⲟⲃ ⲏⲉⲧ? ⲧы ⲏⲁⲭⲩя ⲩ ⲙⲉⲏя ⲭⲩύ ⲟⲧⲥⲟⲥⲁⲗ ⲡⲉⲣⲉⲇ ⲅυⲧⲗⲉⲣⲟⲙ? ⲡυⲇⲟⲣⲁⲥ ?? ⳝⲗяⲧь ⲏⲉ ⲡⲟⳅⲟⲣьⲥя ⲱⲗюⲭⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲃⲥⲟⲥⲧⲟяⲏυυ ⲧⲣⲟⲗυⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ ⲭⲩⲉⲥⲁⲥ ⲉьⲩⳡυύ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲭⲩⲉⲧⲩ ⲧⲩⲡⲁя  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲗя ⲧы ⲧы ⲩ ⲙⲉⲏя ⳃⲁⲥ ⲙⲟυ ⲥⲟⲟⳝⳃⲉⲏυя ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲡⲣяⲙⲟⲙ ⳅⲏⲁⳡⲉⲏυυ ⲥⲟⲥⲁⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲅⲁⲗυⲙыύ? υⲗυ ⲏⲉⲧ я ⲧⲉⳝⲉ ⲟⳡⲕⲟ ⲡⲟⲣⲃⲩ υ ⲕυⲏⲩ ⲡⲥⲁⲙ ⲏⲁⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲱⲁⲃⲕⲁ ⲉⳝⲩⳡⲁя ⲕⲟⲅⲇⲁ ⲧы ⲙⲏⲉ ⲡυⲱⲉⲱь эⲧⲟ ⲇⲟⲥⲧⲟⲃⲗяⲉⲧ ⲩⲇⲟⲃⲟⲗьⲥⲧⲃυⲉ/ⲙⲟⲉⲙⲩ ⲭⲩю υ ⲧы ⲡυⲱⲉⲱь ⲡυⳅⲇⲟⲥ ⲉⳝⲁⲏыύ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲥⲗыⲱь ⲡυⳅⲇⲟύ ⲥⲃⲟⲉύ ⲏⲉ ⲃⲉⲗяύ υⲗυ ⲧⲉⳝⲉ ⲃ ⲩⲭⲟ ⲭⲩύ ⲥⲩⲏⲩьь ⳡⲧⲟ ⳝ ⲧы ⲥⲃⲟю ⲙⲁⲧь ⲥⲗыⲱⲁⲗ ⲕⲁⲕ ⲟⲏⲁ ⲟⲣⲉⲧ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲁⳡⲉⲙ ⲡⲟⲕⲁⳅыⲃⲁⲉⲱь яⳅыⲕⲟⲙ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲕυⲃⲁⲉⲱь ⲅⲟⲗⲟⲃⲟύ ⳡⲧⲟ ⲭⲟⳡⲉⲱь ⲡⲟ ⳝыⲥⲧⲣⲉⲉ ⲉⲅⲟ ⲥⲟⲥⲏⲩⲧь ⲧы ⳡⲧⲟ ⲙⲟⲗ ⲧⲁⲕⲟύ ⲡυⲇⲣ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲡⲟⲕⲁⲯυ ⲙⲏⲉ ⲭⲟⲧь ⲟⲇⲏⲩ ⲧⲃⲟю ⲇыⲣⲕⲩ ⲕⲟⲧⲟⲣⲩю я ⲉⳃⲉ ⲏⲉ ⲉⳝⲁⲗ ⲧы ⲯⲉ ⲏⲁⲭⲩύ ⲕⲟⲏⳡⲉⲏⲏыύ ⲭⲩⲉⲥⲁⲥ ⲟⲇⲏⲁⲕⲟ ⲏⲉ ⲧⲁⲕ ⲗυ? ⲧы ⲥⲟⲥⲁⲧь ⲩⳡυⲥь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲕⲟⲅⲇⲁ-ⲧⲟ ⲙⲏⲉ ⲅⲟⲃⲟⲣυⲗ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲉⳝя цⲁⲣь ⲁ ⲧⲃⲟύ яⳅыⲕ цⲁⲣⲉⲃⲏⲁ ⲏⲁⲭⲩύ ⲧы ⲧⲁⲕⲟύ ⲉⳝⲁⲏⲩⲧыύ ⳅⲁⲇⲁⲗⲥя?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲧы ⲩⲏыⲗⲁя ⲭⲩύⲏя ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝя ⲟⲇυⲏ ⲏⲁ ⲟⲇυⲏ ⲣⲁⳅⲟⲣⲃⲉⲧ ⲡυⲇⲟⲣ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲁⲣⲟⳡ ⲏⲁⲭⲩύ ⲧы ⳃⲁⲥ ⲡⲟⲇⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲟⳡⲉⲱь?ⲇⲩⲙⲁⲉⲱь я ⲧⲉⳝⲉ ⲭⲩύ ⲃ ⲣⲟⲧ ⲏⲉ ⲥⲩⲏⲩ ⲡυⲇⲟⲣⲁⲥ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲕⲟⲏⳡⲩ ⲡυⲇⲟⲣ ⲧы ⲩⲏыⲗыύ ⲏⲩ ⲕⲁ ⲥюⲇⲁ υⲇυ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⳅⲁⲃⲁⲗ ⲟⲧ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲧы ⲯⲉ ⲙⲏⲉ ⲉⳃё ⳅⲁ ⲇⲉⲕⲁⳝⲣь ⲙυⲏⲉⲧ ⲏⲉ ⲥⲇⲉⲗⲁⲗ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲙⲏⲉ ⲕⲟⲅⲇⲁ ⲥⲟⲥⲁⲧь/ ⳝⲩⲇⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲧы ⲙⲏⲉ ⲏⲁⲭⲩύ ⲙⲟю ⲙⲟⳡⲩ ⲡυⲧь ⳝⲩⲇⲉⲱь ⲡⲟⲕⲁ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱυⲱь/ⲧы ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ я ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲕⲟⲏⳡⲁⲧь ⲧы ⳝⲩⲇⲉⲱь ⲡⲣυⲏⲉⲙⲁⲧь ⲡⲟⲣцыю ⲥⲡⲉⲣⲙ ⲡυⲇⲟⲣⲁⲥⲁ ⲕⲩⲥⲟⲕ υⲗυ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь цыⲣⲕⲩⲗⲉⲙ ⳡⲧⲟ ⲧⲉⳝⲉ ⲏⲉ ⲡⲣυⲱⲗⲟⲥь ⲡυⲧь ⲥⲡⲉⲣⲙⲩ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲟⲡⲩⲥⲧυⲗⲥя ⲇⲟ ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⳝыⲃⲱυύ ⲭⲩⲉⲥⲁⲥ юⲙⲁⲣυⲥⲧⲟⲃ ⲉⳝⲁⲧь ⲧы ⳡⲙⲟ ⲧы ⲏⲁⲭⲩύ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲇⲟⲥⲧⲟⲉⲏ ⲕⲁⲕ υ ⲙⲟⲉⲅⲟ ⲧⲣⲟⲏⲁ ⲡυⳅⲇⲁⲅⲣыⳅ ⲏⲁⲭⲩύ ь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲕⲟⲅⲇⲁ ⲏⲉ ⳅⲏⲁⲉⲱь ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⳡⲙⲟⲕυⲃⲁⲉⲱ υ ⲅⲟⲃⲟⲣυⲱь/ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲟⲯⲉ ⲡⲣυⳡⲙⲟⲕⲏⲉⲱь? ?ⳝⲗяⲧь ⲡυⲇⲟⲣ ⲧы ⲅⲁⲗυⲙыύ υⲇυ ⲟⲧⲥюⲇⲁ υ ⲉⳝυ ⲥⲃⲟю ⲙⲁⲧь ⲡυⳅⲇ ⲉⲉ ⲡυⳅⲇⲉ ⲟⲗ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ υⲇυ ⲟⲧⲥюⲇⲁ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲏ ⲡⲟⲕⲁⳅⲁⲗ ⲥⲉⳝя ⲃ ⲇⲉⲗⲉ υⳝⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲡυⲇⲟⳅⲏⲁя ⲱⲗюⲭⲁ ⲕⲁⲕ я υ ⳅⲏⲁⲗ я ⲇⲉ ⲉⲉ ⲭⲩⲉⲙ ⲡυⳅⲇυⲗ ⲧы ⳅⲏⲁⲗ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲁⲕ ⲧⲉⳝя ⲏⲁⳡⲏⲉⲙ ⲉⳝⲁⲧь ⲡⲁцⲉⲉⲏⲧ ⲧⲉⳝя ⲃыⲉⳝⲩ υ ⳝⲩⲇⲩ ⲇⲣⲁⲧь/ⲧⲉⳝя ⲕⲁⲕ ⲅⲣяⳅⲏⲩю ⲱⲗюⲭⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲣⲁⲥ ⲧы ⳝⲗяⲧь ⲕⲟⲅⲇⲁ ⲙⲏⲉ ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲧы ⲭⲟⲧь ⲡⲣυⳡⲙⲟⲕυⲃⲁύ ⲭⲩⲉⲥⲁⲥ ⲧы ⲡυⳅⲇⲁⲗⲩⲡыύ ⲉⳝⲁⲧь ⲧⲉⳝя ⲏⲁⲇⲟ ⲭⲇ  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяяя я ⲧⲩⲧ ⲡⲟⲏяⲗ ⳅⲁⳡⲉⲙ ⲧⲉⳝя ⲉⳝⲁⲧь ⲃⲟⲧ ⲥⲙⲟⲧⲣυ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲙⲏⲉ ⳅⲁ ⲥⲃⲟύ ⲟⲧⲥⲟⲥ ⲏⲉ ⲡⲗⲁⲧυⲗ? ⲧы ⲡыⲧⲁⲗⲥя ⲙⲏⲉ ⲥⲇⲉⲗⲁⲧь ⲟⲧⲥⲟⲥ ⳅⲁ ⲕⲣⲉⲇυⲧ? ⲡⲟⲏυⲙⲁⲉⲱь? ⳝⳝⲗя ⲧы ⲣυⲗυ ⲇⲩⲙⲁⲉⲱь ⲃыⲃⲉⳅⲉⲱь ⲙⲉⲏя? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱυⲱь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲁⲕ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗυ ⲥⲧυⲗⲉⲙ ⲯⲩⲣⲁⲃⲗя? ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲟⲏⲁ ⲥⲧⲁⲏⲁⲗⲁ ⲏⲁⲭⲩύ ⲥⲩⲃⲁⲗⲁ ⲥⲃⲟю ⲅⲟⲗⲟⲃⲩ ⲃ ⳅⲉⲙⲗю ⲉⳝⲁⲧь я ⲧⲟⲅⲇⲁ ⲟⲣⲁⲗ ⲩⲭⲭⲭⲁ ⲕⲁⲕ ⲱⲁⲥ ⲏⲁⲇ ⲧⲟⳝⲟύ ⲕⲁⲕ ⲣⲃⲩⲧ ⲧⲉⳝⲉ ⳃⲉⲕⲩ ⲙⲟυⲙ ⲭⲩⲉⲙ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲧы ⳡⲉ ⲏⲁⳅⲩύ ⲏⲁⲭⲩύ ⲁⲭⲩⲉⲗⲁ ⲡυⳅⲇⲁⲗυⳅⲕⲁ ⲉⳝⲁⲏⲁя ⲧⲉⳝя ⳡⲧⲟ ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⲉⲁⲕ ⲱⲗюⲭⲩ ⲇⲣⲁⲏⲩⳝ υⲗυ ⳡⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲇⲁ я/ⲧⲉⳝя ⲉⳝⲁⲧь ⲕⲁⲕ ⲱⲗюⲭⲩ ⳝⲩⲇⲩ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉьⲁⲏыύ ⲏⲁⳅⲩύ ⲡⲟⲱⲉⲗ ⲡⲉⲧⲩⲭ ⲇⲣⲁⲏⲏыύ я ⲯⲉ ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⲧⲉⳝя ⳝⲩⲇⲩ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡⲁⲗⲁ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ υ ⲡⲟⳝⲉⲯⲁⲗⲁ ⲃ ⲧⲩⲁⲗⲉⲧ ⲃⲟ ⲃⲣⲉⲙя ⲕⲟⲅⲇⲁ ⲩ ⲧⲉⳝя ⲡⲟⲏⲟⲥυⲗ υ ⲧы ⲏⲁⲥⲣⲁⲗ ⲏⲁ ⲥⲃⲟю ⲙⲁⲧь ⲁ ⲟⲏⲁ ⳅⲁ эⲧⲟ ⲧⲉⳝя ⲉⲣⲱυⲕⲟⲙ ⲃыⲉⳝⲁⲗⲁ ⲡⲟⲙⲏυⲱь ⲧы ⲯⲉ ⲏⲁⲭⲩύ ⲏⲉⲕⳡⲉⲙⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲧⲉⳝя ⲙⲁⲗⲟ ⲃыⲉⳝⲁⲧь υ ⲧы ⲉⳃё ⲡыⲧⲁⲉⲱьⲥя ⳡⲧⲟ ⲧⲟ ⲡυⲥⲁⲧь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ )ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲩⳡⲉⲏыⲉ ⲏⲁⲱⲗυ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲙ ⲕⲟⲥⲧь ⲇυⲏⲟⳅⲁⲃⲣⲁ? ⲧы ⲏⲁⲭⲩύ ⲙⲟⲉⲅⲟⲭⲩя ⲏⲉ ⲥⲧⲟυⲱь ⲡⲣυⳡⲉⲙ ⲧⲩⲧ ⲧⲃⲟύ ⲟⲧⲥⲟⲥ ⲉⳝⲁⲏыύ ⲧы ⳅⲩⲏⲥⲁⲁ ⲧы ⲩ ⲙⲉⲏя ⳝⲉⲥⲡⲗⲁⲧⲏⲟ ⲥⲡⲁⲥⲁⲧь ⲇⲟⲗⲯⲉⲏ ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ ⲧы ⳝⲗяⲧь ⲡⲉⲧⲩⲭ ⲉⳝⲁⲏыύ ⲡⲟⲱⲉⲗ я ⲧⲉⳝⲉ ⲅⲟⲃⲟⲣⳝ ⲏⲁ ⲭⲩύ ⲡυⲇⲟⲣⲁⲥ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱь ⲧы ⲡυⲇⲟⲣⲁⲥ ⲧы ⲙⲉⲏя ⲏⲉ ⳅⲁⲧⲣⲟⲗυⲱь υⳝⲟ ⲧы ⲭⲩύ ⲙⲏⲉ яⳅыⲕⲟⲙ ⲙⲟⳅⲟⲗυⲱь, я ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲣⲟⲧ ⲧⲁⲕ ⳡⲧⲟ υⲇυ ⲏⲁⲭⲩύ ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ) ⲉⳝⲁⲗυ ⲧⲉⳝя ⳡⲩⲣⲕυ ⲧы ⲉⳃё ⲭⲟⳡⲉⲱь ⲙⲏⲉ ⳡⲧⲟ ⲧⲟ ⲡυⳅⲇⲉⲧь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳡⲉ ⲉⳝⲁⲧь ⲁⲭⲩⲉⲗⲁ ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲏⲁⳅⲩύ ⳃⲁⲥ ⲙⲟύ ⲭⲩύ ⲃⲥυⲁⲏⲉⲧ ⲁ ⲧы ⲗяⲯⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉьⲁⲏыύ ⲧы ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲕⲁⲕ ⲏυⲕⲧⲟ ⲇⲣⲩⲅⲟύ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲡⲉⲧⲩⲭ ⲥⲩⲕⲁ ⲏⲁⲭⲩύ υⲇυ я ⲏⲁⲭⲩύ ⲏⲁⳡⲏⲩ ⲧⲉⳝя ⲉⳝⲁⲧь υ ⲇⲁⲯⲉ ⲏⲉ ⲡυⲕⲏⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲱⲗюⲭⲁ ⲉⳝⲁⲧь ⲡυⲱυ ⲏⲟⲣⲙⲁⲗьⲏⲟ ⲧы ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲡυⲱⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧы ⳝⲗяⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲁⲅⲣ ⲥⲃⲟύ ⲏⲉ ⲟⲧⲡⲩⲥⲕⲁύ ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ ⲡⲉⲧⲩⲭ ⲧы ⲉⳝⲁⲏыύ ⲉⳝⲁⲗυ ⲧⲉⳝя ⲡⲥы ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲡⲉⲣⲉⲃⲁⲣυⲃⲁύ ⲃⲥⲉ ⳡⲧⲟ я ⲡυⲱⲩ ⲡυⲇⲣ ??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱυⲱь ⲧы ⲯυⲃⲟⲧⲏⲟⲉ ⲧⲉⳝя ⳃⲁⲥ ⳝⲟⲅⲁⲧыⲣь ⲃ ⲯⲟⲡⲩ ⲇⲣⲁⲧь ⳝⲩⲇⲉⲧ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ я ⲧⲉⳝя ⲉⳝⲁⲧь ⲃыⲉⳝⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ ⲥⲡυⲇⲟⳅⲏⲩю ⲏⲁⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲉⳝⲁⲧь ⲧⲉⳝя ⳅⲁ ⳃⲉⲕⲩ ⲧы ⳡⲧⲟ ⲏⲁⲭⲩύ ⲡⲉⲣⲉⲇⲟⲙⲏⲟύ ⲩⲏυⲯⲁⲉⲱьⲥя? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲧⲉⳝя ⳡⲧⲟ ⲃыⲉⳝⲁⲧь? ⳡⲧⲟ ⲗⲉ? ⲭⲩⲉⲥⲁⲥ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲉⳝⲁⲧь ⲕⲟⲅⲇⲁ ⲃ ⳅⲉⲣⲕⲁⲗⲟ ⲥⲙⲟⲧⲣю ⲃυⲯⲩ ⲧⲃⲟⲉ ⲉⳝⲁⲏⲟⲉ ⲗυцⲟ ⲃ ⲥⲡⲉⲣⲙⲉ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? я ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ ⲉⳝⲁⲏⲩю ?? ⲧы ⲏⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⲡⲟⲭⲟⲇ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗя ⲉⳝⲁⲧь ⲧы ⲏⲁⲭⲩύ ⲭⲩⲉⲡⲗⲉⲧ ⲧы ⳡⲧⲟ ⲉⳝⲁⲧь ⲭⲩяⲙυ ⳅⲁⳃυⳃⲁⲉⲱьⲥя? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲉⳝⲁⲧь ⲧⲉⳝя ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲏⲁⲭⲩύ ?? ⳝⲗя ⲙⲏⲉ ⲡⲟⲭⲩύ ⲏⲁ ⲧⲉⳝя ⲇⲯ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲁⲭⲩύ ⲕⲟⲏⲃⲉⲥⲕⲩю ⲧⲃⲟύ ⲣⲟⲧ υ ⳅⲁⲥⲧⲁⲃⲗю ⲥⲟⲥⲁⲧь ⲡⲟⲏяⲧυⲉ υⲙⲉⲉⲱь? я ⲧⲃⲟύ ⲭⲩύ ⲃ ⲙяⲥⲟⲣⲩⳝⲕⲩ ⲥⲩⲃⲁⲧь ⳝⲩⲇⲩ ⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲙⲟύ ⲭⲩύ) ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲟⲇⲏⲁⲕⲟ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲁⲭⲩύ ⲡⲣⲟⲥⲧⲟⲉⲗю ⲧⲉⳝⲉ ⲅⲟⲗⲟⲃⲩ ⲥⲡⲉⲣⲙⲟύ ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲁ ⲡⲟⲏυⲙⲁⲉⲱь? ⳝⲗяⲧь ⲧⲁⲕυⲭ ⲕⲁⲕ ⲧы ⲡυⲇⲟⲣⲁⲥⲟⲃ ⲧⲟⲗьⲕⲟ ⲉⳝⲁⲧь ⲏⲁⲇⲟ ?? я ⲧⲉⳝя ⲃ ⲇⲟⳝⲁⲃⲟⲕ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗя υⲇυ ⲕⲁ ⲧы ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲅⲁⲗυⲙыύ я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲙⲏⲉ ⲃⲁⲱⲉ ⲡⲟⲭⲩύ ⲏⲁ ⲧⲃⲟυ ⲱⲗюⲭⲁⲏⲥⲕυⲉ ⲕⲟⲙⲡⲗⲉⲕⲥы  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> υⲇυ ⲏⲁ ⲭⲩύ) ⳝⲩⲇⲩ я ⲉⳝⲁⲏⲏⲟⲙⲩ ⳝυⳡⲩ ⲇⲟⲕⲁⳅыⲃⲁⲧь) ⲥⲩⲕⲁ υⲇυ ⲡⲣⲟⲇⲁⲃⲁύ ⲥⲃⲟю ⲙⲁⲧь, ⲉⲉ ⲡⲟ ⲩⲅⲗⲁⲙ ⲉⳝⲩⲧ ⲃυⲇⲏⲟ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲉⳝⲁⲧь ⲧⲉⳝя ⳡⲁύⲏυⲕⲟⲙ ⳝⲩⲇⲩ ⲉⲥⲗυ ⲧы ⲏⲉ ⳅⲁⲧⲕⲏⲉⲱьⲥя υ ⲏⲉ ⳝⲩⲇⲉⲱь ⲡυⳅⲇⲉⲧь ⲭⲩύⲏю ⲃⲥяⲕⲩю ⲡⲟⲏяⲧυⲉ ⲩ ⲧⲉⳝя ⲉⲥⲧь ⲡυⲇⲣⲁⲥ? я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲉⲥⲟⲥ ⲉⲧы ⲉⳝⲁⲏⲏыύ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲥⲩⲕⲁ ⲩ ⲧⲉⳝя ⲏⲁ ⲅⲟⲗⲟⲃⲉ ⲡⲉⲧⲩⲱⲏя ⲧы ⳡⲉ ⲙⲉⲏя ⲃыⲙⲟⲣⲁⲯⲧⲃⲙⲃⲉⲱь ⲭⲩⲉⲥⲟⲥ ⲉⳝⲩⳡυύ,ⳝⲗяⲧь ⳅⲁⲃⲁυⲗ ⲉⳝⲗⲗⲟ ⲭⲩⲉⲥⲟⲥ ⲉⲁⲁⳝⲏⲏыύ ⲥⲃⲟυ ⲥⲕⲣυⲏы ⲟⲧцⲩ ⲃ ⲯⲟⲡⲩ ⳅⲁⲥⲩⲏⲉⲱь) ⲡυⲇⲟⲣⲁⲥ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩύⲏя ⲉⳝⲁⲏⲏⲁя ⲥⲙⲟⲧⲣυ ⲕⲁⲕⲁя ⳝⲟⲙⳝⲁ ⳃⲁⲥ ⲩⲡⲁⲇⲉⲧ ⲏⲁ ⲉⳝⲗⲟ ⲧⲃⲟⲉ, ⲭⲩⲉⲥⲟⲥ ⲉⳝⲗυⲃыύ я ⲧⲉⳝя ⲃыⲉⳝⲩ ⲣⲁⲕⲟⲙ ⲧы ⳡⲉ ⲃⳅъⲉⳝыⲃⲁⲉⲱьⲥя, я 1 ⲥυⲯⲩ ⲭⲩⲉⲥⲟⲥ ⲉⳝⲩⳡυύ, я ⲯ ⲏⲉ ⲇⲟⲗⳝⲟⲉⳝ ⲕⲁⲕ ⲧы ⳡⲧⲟⳝ ⲇⲁⲃⲁⲧь ⲡⲣⲟⲫυⲗь ⲥⲃⲟύ ⲕⲟⲙⲩ-ⲧⲟ, ⲇⲩⲣⲁⲗⲉύ ⲥⲩⲕⲁ ⲉⳝⲩⳡυύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱь ⲙⲩⲇυⲗⲁ ⲉⲇⲁⲏⲁя ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲗⲁ ⲡυⳅⲇⲁ ⲉⲇⲁⲏⲃя ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲥⲕⲁⳅⲁⲗ ⲡⲟⲱⲉⲗ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲡⲣⲟⲱⲉⲗⲥя ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲕⲕⲟⲏⳡⲉⲏⲏыύ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧⲉⳝя ⲙⲁⲧь ⲩⳡυⲗⲁ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ? эⲧⲟ ⲯⲉ цⲉⲗⲁя υⲥⲧⲣⲟя ⲏⲁⲭⲩύ ⲧы ⳝⲗя ⲕⲁⲕ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲭⲇ  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲧⲉⳝя ⲏⲁⲭⲩύ ⲃ ⲣⲟⲧ ⲉⳝⲁⲧь ⲏⲁⲇⲟ ⳅⲁ ⲧⲃⲟυ ⲉⳝⲁⲏыⲉ ⲡⲟⲇⲥⲣⲥⲏыⲉ ⲥⲗⲟⲃⲁ ⲭⲩⲉⲥⲁⲥ ⲧы ⲏⲁⲭⲩύ ⲕⲟⲅⲇⲁ ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲧы ⲇⲩⲙⲁⲉⲱь ⲧⲟⲗьⲕⲟ ⲟ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲏяⲗ ?ⲧы ⳝⲗяⲧь ⲡυⲇⲁⲣⲟⲕ ⲉⳝⲁⲏыύ ⲉⳝⲁⲧь ⲧы ⲗⲟⲭ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗя ⲧы ⳝⲗяⲧь ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲗⲩⳡⲱⲉ ⲧⲉⳝя ⲥⲟⲥⲉⲧ? ⲇⲁ ⲧы ⲱⲁⲗⲟⲉⳝ ⲧы ⲏⲁⲭⲩύ ⲡⲟⲇⲥⲁⲥыⲃⲉⲱⳝ ⲃⲥⲉ ⳡⲧⲟ ⲇⲃυⲯⲉⲧⲥя ⲭⲩⲉⲥⲁⲥ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲏⲁⲭⲩύ ⲥⲟⲥⲁⲧь ⲧⲟⲗьⲕⲟ ⲩⲙⲉⲉⲱь ⲡυⲇⲣ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱь ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲕⲩⲣⲃⲁⲕ ⲉⳝⲁⲏыύ ⲁⲧⲟ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲕⲟⲏⳡⲁⲧь ⲉύ ⲃ ⲣⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь я ⲕⲟⲅⲇⲁ ⲧⲟ ⲉⳝⲁⲗ ⲉύ ⲃ ⲣⲟⲧ υ ⲏⲁⲱⲉⲗ ⳅⲟⲗⲟⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⲕⲣⲟⲙⲉ ⲕⲁⲕ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲩⲙⲉⲉⲱь? υⲗυ ⲧⲉⳝⲉ ⲡυⳅⲇⲩ ⲣⲃⲁⲧь? ⳡⲧⲟⳝ ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲃυⲇⲟⲃⲁⲗⲁ ⲧⲉⳝⲉ ?ⲡυⲇⲟⲣⲁⲥ ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲏⲁⲡυⲥⲁⲗ ⳡⲧⲟ ⲧы ⲭⲩυ ⲥⲟⲥⲉⲱь? ⳡⲙⲟ ⲉⳝⲁⲏⲟⲉ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲉⲱь? ⳝⲗяь я ⲣυⲗυ ⲅⲟⲃⲟⲣⳝ ⲧы ⲡυⲇⲟⲣ ⲧы ⲇⲁⲯⲉ ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳅⲁⳃυⲧь ⲏⲉ ⲃⲥυⲗⲁⲭ ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣ ⲧы ⲉⳝⲁⲏыύ ⲧы ⲏⲁⲭⲩύ ⲡⲟⲇⲥⲁⲥыⲃⲉⲱь ⲙⲏⲉ ⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲡυⳅⲇⲁⲅⲣыⳅ ⲉⳝⲁⲏыύ ⳝыⲥⲧⲣⲟ ⲃⲥⲁⲥⲁⲗ ⲃⲥⲉ ⳡⲧⲟ я ⲧⲉⳝⲉ ⲡυⲱⲩ ⲡυⲇⲣⲁⲥ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲏⳡⲉⲏⲁя ⲱⲗюⲭⲁ υ ⲧы ⲙⲏⲉ ⲏⲁⲭⲩύ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲡⲣυ эⲧⲟⲙ ⲡυⲇⲟⲣ ⲧы ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⳅⲇⲁⲕⲣыⲗ ⲉⳝⲩⳡυύ) ⲏⲉⲭⲩя ⲏⲉ ⲥⲙⲟⲅ) ⲏⲁⲱⲉⲗⲥя ⲧⲩⲧ ⲧⲣⲟⲗⲗь ⲭⲩⲉⲃ)) ⲧⲉⲣⲡυⲗⲁ ⲉⳝⲁⲏⲏⲁя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲱυ ⲧⲁⲕⲟύ ⲟⲅⲣⲙⲟⲏыύ ⲡυⳅⲇⲉц) ⲕⲁ ⲧы ⳃⲁⲥ ⲡⲣⲟⲃⲁⲗυⲱьⲥя ⲧⲩⲇⲁ ⲇⲟⲗⳝⲟⲉⳝ ⲉⳝⲁⲏⲏыύ ⳝⲩⲇь ⲁⲕⲕⲕⲩⲣⲁⲧⲉⲏ ⲭⲩⲉⲥⲟⲥ ⲉⲁⳝⲏⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ ⳝⲗяⲧь ⲧы ⳡⲉ ⲧⲁⲙ ⲡυⲱⲉⲱь ⲃⲥⲉ ?) ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏыύ) ⲏⲉⲥⳡⲁⲥⲏыύ ⲡⲉⲧⲩⲭ ⲥⲩⲕⲁ))) ⲱⲁⳝⲗⲟⲏυⲧь ⲩⲯⲉ ⲏⲁⳡⲁⲗ?) ⲏⲉ ⲭⲩя ⲏⲉ ⲃыⲃⲟⳅυⲱь ⲇⲁ ?)?) ⲡⲉⲧⲩⲭ ⲉⳝⲁⲏⲏыύ) ⲉⳝⲁⲗ ⲧⲉⳝя ⲏⲁ ⲏⲟⲅⲁⲭ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⲥыⲏ ⲱⲁⲗⲁⲃы) ⲥⲩⲕⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗя ⲧы ⲅⲗⲁⲃⲏⲟⲕ ⲡⲟ ⳡⲁⳃⲉ ⲙⲏⲉ ⲥⲟⲥυ ⲁⲧⲟ ⲙⲏⲉ ⲥⲧⲣⲁⲱⲏⲟ ⲃⲇⲣⲩⲅ ⲏⲁⳡⲏⲉⲱь ⲉⳝⲁⲧь ⲥⲃⲟю ⲙⲁⲙⲕⲩ ⲇⲟ ⲡⲟⲧⲉⲣυя ⲥⲟⳅⲏⲁⲏυя ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲟⳝⲇⲟⲗⳝⲁⲏыύ ??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⲭⲩⲉⲥⲁⲥ ⲕⲟⲧⲟⲣыύ ⲡыⲧⲁⲉⲧⲥя ⲥⲟⲥⲏⲩⲧь ⲙⲟύ ⲭⲩύ ⳝⲉⳅ ⲡⲣⲉⳅυⲣⲃⲟⲧυⲃⲁ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲉⲙ ⲥⲩⲧь? ⲧы ⲏⲁⲭⲩύ ⲡыⲧⲁⲉⲱьⲥя ⲥⲟⲥⲏⲩⲧь ⲙⲟύ ⳝυⲅ ⳡⲗⲉⲏ ⲩⲭⲭⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⲙⲏⲉ ⲅⲗⲁⲃⲏⲟⲉ ⲡⲟⲕⲁⲯυ ⲅⲇⲉ υ ⲃ ⲕⲁⲕⲟⲉ ⲙⲉⲥⲧⲟ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь/υ я ⲧⲉⳝя ⲏⲁⲅⲣⲁⲯⲩ ⲥⲡⲉⲣⲙⲟύ ⲡⲟⲏяⲗ ⲡυⳅⲇⲁюⳝ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗя ⲧы ⲣυⲗυ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲙⲉⲏя ⲥυⲗьⲏⲉⲉ? ⲭⲩⲉⲥⲁⲥ ⲟⳡⲏυⲥь я ⲧⲉⳝя ⲃыⲉⳝⲩ ⲧы ⲇⲁⲯⲉ ⲃяⲕⲏⲩⲧь ⲏⲁⲭⲩύ ⲏⲉ ⲩⲥⲡⲉⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь ⲧы ⲃ ⲁⲭⲩⲉ ⳝⲩⲇⲉⲱь ⲡⲟⲕⲁ ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ёⳝⲁⲏⲟⲉ ⲃ ⲣⲟⲧ ⲟⲥⲧⲟⲉⳝⲗяюⳃⲉⲉ ⲥⲧⲣⲁⲭⲟⲡυⳅⲇυⳃⲉ, ⲡⲣⲟⲙⲩⲇⲟⳝⲗяⲇⲥⲕⲁя ⲙⲟⲣⲇⲟⳅⲁⲗⲩⲡυⲏⲁ ⲟⲭⲩⲉⲃⲁюⳃⲁя ⲟⲧ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟⲅⲟ ⲏⲉⲃъⲉⳝⲉⲏυя. υ ⲃⲁⳃⲉ, ⳝⲗяⲇь, ⲃⲥⲉⲙ ⲭⲩύ ⲥⲟⲥⲁⲧь υ ⲧⲣυ ⲣⲁⳅⲁ ⲃ ⲇⲉⲏь ⲭⲟⲇυⲧь ⲏⲁ ⲃⲟⲥьⲙυⳡⲁⲥⲟⲃыⲉ ⲕⲁⲗⲟⲡⲣⲟцⲉⲇⲩⲣы ⲏⲁ ⲅⲉύⲥⲕυύ ⳡⲁⲧ ⲡυⳅⲇⲁ ⲧⲁⲙ ⲧⲉⳝя ⳅⲁⲯⲇⲁⲗυⲥ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲙⲩⲗⲉⳡⲕⲁ ⲯⲟⲥя)))ⲧы ⲧⲁⲕ ⲯⲉ ⲟⳡ ⲁⲕⲧυⲃⲏⲟ ⲡⲣⲟⲙыⲱⲗяⲉⲱь ⲡⲁⲥⲥυⲃⲏⲟύ ⲡυⲇⲟⲣⲁⲥⲏⲉύ,ⲫⲩ))  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⳅⲇⲁⳝⲟⲗ ⲧы ⲉⳝⲁⲏыύ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡⲉⲧ ⳅⲁⲡⲣⲉⲧυⲗⲁ ⳡⲧⲟⳝы ⲧы ⲩ ⲙⲉⲏя ⲭⲩύ ⲥⲟⲥⲁⲗ υ ⲡⲟ эⲧⲟⲙⲩ ⲧы ⳡⲉⲣⲉⳅ ⲟⲕⲏⲟ ⲩⳝⲉⲅⲁⲉⲱ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲉⳝя ⲥⲧⲟυⲧ ⲧⲟⲗьⲕⲟ ⲡⲟⲙⲁⲏυⲧь ⳡⲗⲉⲏⲟⲙ)) ⲕⲁⲕ ⲧы ⲥⲣⲁⳅⲩ ⲕⲩⲡυⲱьⲥя υ ⲡⲟⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲥⲧⲁⲏⲉⲧⲥя ⲃ цⲉⲗⲟⲥⲧυ υ ⲥⲟⲭⲣⲁⲏⲏⲟⲥⲧυ))ⲏⲟ ⲧⲉⳝя ⲏⲁⲉⳝⲩⲧ υ ⲡⲩⲥⲧяⲧ ⲭⲁⳡυ ⲡⲟ ⲕⲣⲩⲅⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱ я ⳃⲁ ⲏⲁ ⲥⲃⲟю ⳅⲁⲗⲩⲡⲩ ⲃⲟⳅⲏⲉⲥⲩ ⲧⲃⲟю ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲟⳡⲕυ υ ⲏⲁⳡⲏⲩ ⲃⲥⲧⲩⲡⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲡⲟⲗⲟⲃⲟύ ⲕⲟⲏⲧⲁⲕⲧ ⲥ ⲧⲃⲟυⲙυ ⲩⲱⲁⲙυ)))  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲥⲡυⳅⲇⲉⲗ ⲕⲟⲡьⲉ ⲩ ⲣыцⲁⲣя υ эⲧυⲙ ⲯⲉ ⲕⲟⲡьⲉⲙ ⲟⲧъⲉⳝⲁⲗ ⲧⲃⲟю ⳝⲁⳝⲩⲱⲕⲩ!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲉⲥⲟⲥ?) ⲧы ⲩⲃυⲇⲉⲗ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙы υⲥⲡⲩⲅⲁⲗⲥя υ ⲥъⲉⳝⲁⲗⲥя?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁ ⲧы ⳝⲗяⲧь ⲁⲗⲁⲡⲉⳅⲇыⲣь))ⲧⲃⲟя ⲙⲁⲙⲕⲁ ⲃыⲧⲃⲟⲣяⲉⲧ ⲁⲕⲣⲟⳝⲁⲧυⳡⲉⲥⲕυⲉ ⲧⲣюⲕυ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю)))  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃ ⲡⲟⲡⲉⲣⲉⳡⲏⲩю ⲕυⲱⲕⲩ υ ⲟⲏⲁ ⲇⲟⲭⲏυⲧ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲣⲉⲱυⲗ ⲃⲥⲕⲁⲣⲁⳝⲕⲁⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩⲉц ⲡⲥυⲏⲁ ⲣⲁⳅⲟⲣⲃⲁⲏⲏⲁя ⲏⲩ я ⳃⲁ ⲃⲟⳅьⲙⲩ ⲥⲃⲟю ⳝυⲧⲩ ⳝⲗяⲧь υ ⲣⲁⲥⲱυⳝⲩ ⲧⲉⳝя ⲅⲟⲗⲟⲃⲟύ ⲟⳝ ⲕⲁⲫⲉⲗь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲥⲧⲟⲣⲯⲉⲏⲏⲟ ⲩⲭⲏⲩⲗ υ ⲧⲩⲧ ⲡⲁⲣⲩ ⲃⲟⲗⲟⲥⲁⲧыⲭ яυц ⲩⲇⲁⲣυⲗυ ⲧⲉⳝя ⲧⲁⲕ ⳡⲧⲟ ⲧы ⲏⲉ ⲙⲟⲅ ⲟⲡⲣⲁⲃυⲧьⲥя υ ⲧⲟⲗьⲕⲟ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ,ⲕⲁⲕ ⲧы ⲟⳡⲏⲩⲗⲥя ⲧы ⲡⲟⳡⲩⲃⲥⲧⲃⲟⲃⲁⲗ ,ⲕⲁⲕ ⲧⲃⲟύ яⳅыⲕ ⲗⲟⲃⲕⲟ ⲣⲁⳝⲟⲧⲁⲉⲧ ⲃ ⳡёⲣⲏⲟύ ⲅⲣяⳅⲏⲟύ ⲯⲟⲡⲉ ⲟⲇⲏⲟⲅⲟ ⲡⲟⲇⳅⲁⳝⲟⲣⲏⲟⲅⲟ ⲩⳝⲗюⲇⲕⲁ ...  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲥⲧⲁⲉⲧ эⲧⲟ ⳅⲏⲁⳡυⲧ ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧυⲕ ⲭⲟⳡⲉⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? я ⳃⲁⲥ ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲣⲟⲧ ⲇыⲣяⲃυⲧь ⳝⲩⲇⲩ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ.   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⲡⲥυⲏⲁ ⲧы ⲧⲁⲕυ ⲏⲉ ⲡⲟⲏяⲗ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲉⳝя цⲁⲣь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧⲉⳝя ⳡⲧⲟ ⲭⲩⲉⲙ ⲩⲉⳝⲁⲧь ⳡⲧⲟⳝ ⲧы ⲥⲗⲩⲱⲁⲗⲥя ⲙⲉⲏя,  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⳝυⲟⲥⲫⲉⲣⲁ ⲭⲩя ⲙⲟⲉⲅⲟ, ⲏⲉ ⲃⳅъⲉⳝыⲃⲁύⲥя ⲙⲏⲟⲅⲟ, ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏⲏыύ ⳝⲗⲉⲁⲧь, ⲉⳝⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲡⲟⲕⲩⲥыⲃⲁⲗ ⳡⲗⲉⲏ ⲙⲟύ ⳅⲩⳝⲕⲁⲙυ?)?) ⲙⲏⲉ ⳝыⲗⲟ ⲡⲣυяⲧⲏⲟ, ⲃ ⲧⲟⲧ ⲙⲟⲙⲉⲏⲧ я ⲉⳃⲉ ⲕⲟⲏⳡυⲗ ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ эⲧⲟ ⳝыⲗ 1 ⲣⲁⳅ ⲭⲩⲉⲥⲟⲥ ⲧы ⲙⲟύ)) ⲧы ⲙⲟύ ⲭⲩⲉⲥⲟⲥ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲗяⲧь ⲧы ⳡⲉ ⲧⲁⲙ ⲏⲁⲭⲩύ ⲡυⲱⲉⲱь? ⲡυⲇⲟⲣⲁⲥ я ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲉⳝя ⲏⲁⲅυⳝⲁь ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲁ ⲡυⲇⲟⲣⲡⲁⲥ ⲉⲇⲁⲏыύ ⳝⲗяⲧь ⲭⲩⲉⲥⲁⲥ ⲥⲩⲕⲁ ⲏⲩ ⲕⲁ ⲡⲟⲱⲉⲗ ⲃⲟⲏ ⲟⲧⲥюⲇⲁ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲙⲁⲗⲟⲗⲉⲧⲕⲁ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲁ ⲧы ⲙⲏⲉ ⲃ ⲟⲧⲃⲉⲧ ⲕⲟⲏⲫⲉⲧⲩ ⲇⲁⲃⲁⲗ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲣⲟⲧ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲉⲗ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲡⲟⲕⲁ ⲙⲟц ⲭⲩύ ⲧⲉⳝя ⲏⲉ ⲃыⲉⳝⲁⲗ ⲡⲟ ⲥⲁⲙⲟύ ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧⲉⳝя ⲏⲁⲭⲩύ ⲙⲟⲗⲁ ⲃыⲉⳝⲁⲧь ⲃ ⲣⲟⲧⲁⲏ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲡⲟⲃⲉⲱⲩ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳡⲉ ⲏⲁⲭⲩύ ⲡⲉⲧⲩⲭ ⲉьⲁⲏыύ ⲥⲟⲁⲥⲉⲙ ⲏⲁⳅⲩύ ⲟⲭⲩⲉⲗ? ⲡυⲇⲟⲣⲁⲥ ⲉьⲁⲏыύ я ⲧⲉⳝⲃ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲧь/ⲥ ⲏⲉ ⲧⲟύ ⲏⲟⲅυ ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉьⲁⲏыύ ⳝⲗяⲧь ⲡυⲇⲟⲣ ⳅⲁⲗⲩⲡⲁ ⲟⲭⲩⲉⲃⲱⲁя ⲏⲁⲭⲩύ υⲇυ ⲧы ⳝυⲗяⲧь ⲏⲁⲭⲩύ ⲁⲅⲣυⲱьⲥя ⲏⲁ ⲙⲉⲏя ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ я ⲯⲉ ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲡυⲇⲟⲣ ⲉⲗⲁⲏыύ ⲏυⲭⲩя ⲧы ⳝⲗяⲧь ⲡⲣυⲟⲡⲁⳅⲇыⲃⲁⲉⲱь ⲱⲗюⲭⲁ ⲉⳝⲁⲏⲩⲧⲁя ⲧы ⳡⲉ/ⲉⳝⲁⲧь ⲟⲭⲩⲉⲗⲁ ⲥⲡυⲇⲟⳅⲏⲁя ⲡυⳅⲇⲁ ⲥⲩⲕⲁ ⲇыⲣяⲃⲁя ⲏⲁⲭⲩύ υⲇυ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲡυⲇⲣⲁⲥ ⲭⲩⲉⲥⲁⲥ ⲡⲉⲣⲉⲥⲗⲁⲥⲧ эⲧⲟ ⲥⲟⲟⳝⳃⲉⲏυⲉ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲩⳡυύ,я ⳝⲩⲇⲩ ⲧⲉⳝя ⲉⳝⲁⲧь ⲥⲉⲅⲟⲇⲏя ⲡⲟⲏυⲙⲁⲉⲱь?) ⲡⲉⲧⲩⲱⲏя ⲧы ⲉⳝⲗυⲃⲁя ⲡⲟύⲙυ ⲧⲟ ⳡⲧⲟ ⲧы ⲥⲟⲥⲏⲉⲱь ⲥⲉⲅⲟⲇⲏя ⲭⲩύ ⲡⲉⲧⲩⲭ ⲧы ⲉⳝⲁⲏⲏыύ, ⲧы эⲧⲟ ⲡⲟⲏυⲙⲁⲉⲱь?) ⳡⲧⲟ ⲥⲉⲅⲟⲇⲏя ⲧⲉⳝя я ⲃыⲉⳝⲩ!!  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲱⲉⲗ ⲏⲁⲭⲩύ ⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⳝⲗяⲧь ⲟⳝⲇⲟⲗⳝыⲱь ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ я ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⲥⲟⲃыⲁⲡⲧь ⲕ ⲧⲉⳝⲉ ⲃ ⲉⳝⲗⲉⲧ ⲡυⲇⲗⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲏⲁⲭⲩύ ⲡⲟύⲇυ ⲡυⲇⲟⲣ ⲩⲱⲗⲉⲡⲟⲕ я ⲡⲟⲕⲁ ⲧⲉⳝя ⲉⳝⲩ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲡⲟⲙⲉⲱⲁⲉⲧ ⲥⲇⲉⲗⲁⲧь ⲧⲉⳝⲉ ⲙυⲏⲉⲧ ⲙⲏⲉ? §??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲁⲭⲩύ ⲥⲕⲣⲉⲙⲧυⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ υ ⲥ ⲙⲟυⲙ ⳅⲩⲉⲙ ⲡⲟⲗⲩⳡυⲗυⲥя ⲧы ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ ⲡⲟⲏυⲙⲁⲉⲱь ⲏⲉⲧ? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲩⳡυύ ⳝⲗяⲧь ⲃыⲉⳝⲁⲧь ⲧⲉⳝя ⲙⲁⲗⲟ ⲭⲩⲉⲥⲁⲥ ⲏⲁⲭⲩύ ⲟⲡⲩⳃⲉⲏыύ ⳝⲗяⲧь ⲧы ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲟⲟⲡⲩⳃⲉⲏⲏыύ ⳡⲧⲟ ⲇⲁⲯⲉ ⲏⲉ ⲩⲥⲡⲉⲃⲁⲉⲱь ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁⲭⲩύ ⳡⲧⲟ ⲏⲉ ⲡⲟⲏяⲗ я ⳃⲁⲥ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲟⲧⲡⲣⲁⲃⲗю ⳡⲧⲟⳝ ⲟⲏ ⲧⲉⳝя ⲡⲟⲃⲧⲟⲣⲟⲏⲟ ⲏⲁⲭⲩύ ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲟⳡⲕⲟ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲉⲗ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩύ ⲗυⲡⲟⲃыύ ⲡυⲇⲟⲣ ⳝⲗяⲧь ⲧы ⲕⲁⲕⲟύ-ⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ υⲇυ ⲥⲟⲥⲁⲧь ⲡⲟ ⲯυⲃⲉⲉ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲡⲟⲕⲁ я ⲧⲉⳝя ⲃ ⲣⲟⲧ ⲏⲉ ⲃыⲉⳝⲁⲗ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲏⲁⲭⲩύ υⲇυ ⲟⲧⲥюⲇⲁ ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲉ ⲡⲣⲟⲇыⲣяⲃυⲗ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲥⲗыⲱυⲱь ⲡυⳅⲇⲩ ⲕ ⲥⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲏⲁ ⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲏⲁⲡⲁⲗ ⲏⲁ ⲧⲉⳝя ⲡυⲇⲟⲣⲁⲥ ⲩⲏыⲗыύ ⲥⲩⲕⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲏⲁⲭⲩύ ⲃыⲉⳝⲩ ⲧⲉⳝя ⲉⳝⲁⲧь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⳅⲁⲥⲧⲁⲃⲗю яⳅыⲕⲟⲙ ⲧⲃⲟυⲙ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲗυⳅⲁⲧь/ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲕⲣⲏⳡⲉⲏⲏыύ ⲏⲁⲭⲩύ ⲡυⳅⲇⲁⲗυⳅ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱь ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲟⲭⲩⲉⲗ? ⳝⲗяⲧь я ⲏⲁⲭⲩύ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲣⲃⲁⲧь ⳝⲩⲇⲩ ⲧⲁⲕ ⳡⲧⲟ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧы ⳡⲉ ⲇⲁⲃⲏⲟ ⲏⲁⲭⲩύ ⲡυⳅⲇы ⲏⲉ ⲡⲟⲗⲩⳡⲁⲗ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲡⲣыⲅⲁⲗⲁ ⲏⲁ ⲙⲏⲉ, ⲃ ⲙⲟⲉύ ⲙⲁⲱυⲏⲉ, ⲟⲏⲁ ⲧⲁⲕ ⲃыⲥⲟⲕⲟ ⲡⲣыⲅⲏⲩⲗⲁ ⳡⲧⲟ ⲡⲟⲙяⲗⲁ ⲕⲣыⲱⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲁⲏⲁⲗьⲏыύ ⲃⲟⲗⲟⲥ ⲥⲩⲕⲁ ⲧы ⳡⲉ ⲉⳝⲁⲧь ⲁⲭⲩⲉⲗ?) я ⲧⲃⲟύ ⲣⲟⲧ ⳃⲁⲥ ⲏⲁⲥⲧυⲅⲏⲩ ⲥⲩⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⳡⲉ ⲧⲁⲕⲟύ ⲯυⲣⲏыύ?))?) ⲁ ⳝяⲗⲧь ⲡⲉⲣⲉυⳅⳝыⲧⲟⲕ ⲕⲟⲏⳡυ ⲃ ⲧⲃⲟⲉⲙ ⲟⲣⲅⲁⲏυⳅⲙⲉ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ ⳅⲁⲕⲣⲟύ ⲉⳝⲁⲗьⲏυⲕ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏⲏыύ ⳝыⲥⲧⲣⲟ ⲥⲟⲥⲏⲩⲗ ⲙⲟύ ⲭⲩύ υ ⲥъⲉⳝⲁⲗⲥя ⲟⲧⲥюⲇⲁ ⲃыⲉⳝⲁⲏⲏⲟⲉ ⲯυⲃⲟⲧⲏⲟⲉ ⲥⲩⲕⲁ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲁ ⳅⲁⳝыⲗ ⲟⲏⲁ ⲙⲟⲉⲧⲥя ⲃ ⲙⲟⲉύ ⲥⲧυⲣⲁⲗьⲏⲟύ ⲙⲁⲱυⲏⲕⲉ) ⲟⲏⲁ ⲃⲟⲏяⲉⲧ ⲥⲡⲉⲣⲙⲟύ ⲡυⳅⲇⲉц)) υⲇυ ⲡⲟⲙⲟύ ⲥⲃⲟю ⲙⲁⲧь) ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲉⳝⲁⲧь ⲧⲃⲟя ⲥⲉⲧⲥⲣⲁ ⲃυⲇυⲙⲟ υⲣυⲏⲁ ⲥыⳡⲉⲃⲁ ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ) ⲁⲭ ⲧы ⲥⲉⲕⲥ ⲧⲩⲁⲗⲉⲧⲏыύ)) ⲧⲉⳝя ⲧⲟⲯⲉ ⲃ ⲟⳡⲕⲟ ⲃыⲉⳝⲁⲗυ ⲃ ⲧⲩⲁⲗⲉⲧⲉ?) ⲁ ⲡυⲇⲟⲣⲁⲥ ⲗюⳝяⳃυύ ⲙⲟύ ⲭⲩύ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲥⲗыⲱυⲱь ⲧы ⲯυⲅⲩⲗь ⲉⳝⲁⲏⲏыύ .я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲡυⲏⲁю ⲉⳝⲁⲏⲁⲏя ⲧы ⲙⲣⲁⳅⲟⲧⲁ, ⲃⲧⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲩⳝⲟⲅⲟ ⲥⲟⲥⲉⲧ ⲙⲟύ ⲭⲩύ ⳡⲧⲟ ⲙⲏⲉ ⲇⲁⲯⲉ ⲥⲧⲣⲁⲱⲏⲟ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲧⲩⲱⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⳝⲁⲕⲁ. ⲙⲟύ ⲭⲩύ ⲇⲉⲗⲁⲉⲧ ⲁⲭⲩⲉⲏⲏыⲉ υ ⲇⲟⳝⲣыⲉ ⲇⲉⲗⲁ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲁⲃ ⲕⲟⲅⲇⲁ ⲉⳝⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?). я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲉⲏⲧⲩⲭⲩ ⲃыⲉⳝⲩ), ⲥⲗыⲱυⲱь ⲏⲁⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲏⲉⲏыύ ⲧы ⲣⲟⲧ ⳝⲗяⲇь ⲕⲟⲧⲟⲣыύ ⳝⲉⲣⲉⲧ ⲏⲁ ⲥⲉⳝя ⲥⲗυⲱⲕⲟⲙ ⲇⲟⲭⲩя. ⲥⲗыⲱυⲱь ⲟⲧьⲉⳝⲁⲏⲏыύ ⲉⲃⲣⲉύ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲧⲣⲁⲭⲁю υ ⲃыⲕυⲏⲩ ⲉё ⳅⲁⲥⲥⲁⲏыⲉ ⲧⲣⲩⲡ ⲥⲟⳝⲁⲕⲁⲙ ⳡⲧⲟ-ⳝы ⲟⲏυ ⲉё ⲥⲭⲁⲃⲁⲗυ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲃыⲥⲥⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ. ⲙⲟύ ⲭⲩύ ⲃыⳝⲉⲣⲉⲧ ⲡⲟⳅⲩ ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟ-ⳝы ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, υ ⲃыⳝⲉⲣⲉⲧ ⲁⲭⲩⲉⲏⲏю ⲡⲟⳅⲩ ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝыⲗⲁ ⲇⲟⲃⲟⲗьⲏⲟύ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя. ⲥⲗыⲱυⲱь ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя,я ⲕⲁⲕ-ⲧⲟ ⲣⲁⳅ ⲧⲣⲁⲭⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲩ ⲏⲉё ⲡⲟⲧⲟⲙ ⲏⲁⳡⲁⲗⲥя ⲥⲡⲁⳅⲙ ⲡυⳅⲇы, ⲧы ⲙⲟⲯⲉⲱь ⳅⲁⲗⲉⳡυⲧь ⲟⳡⲕⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⳝⲉⳅ ⲟⳝυⲇ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲇυⲕ ⲇⲣⲟⳡⲁⳃυύ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲣⲟⲧⲁⲏ. ⲙⲏⲉ ⲣⲁⲥⲥⲕⲁⳅыⲃⲁⲗυ ⲧⲟ ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲡυⳅⲇⲁ, ⲡυⳅⲇⲟⲕⲣыⲗыύ ⳝⲁⲣⲁⲏ ⲥⲩⲕⲁ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⲕⲁⲕ ⲉⳝⲁⲏⲏⲩю ⲱⲃⲁⳝⲣⲩ, ⲥⲗыⲱυⲱь ⲧы ⲙⲟⲕⲣⲉⳃⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя, я ⲇⲟⲕⲁⲯⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⲧⲟ ⳡⲧⲟ я ⲙⲟⲅⲩ ⲃыⲉⳝⲁⲧь цⲉⲗυⲕⲟⲙ ⲧⲃⲟю ⲯⲟⲡⲩ ⳅⲁⲥⲥⲁⲏⲩю ⲡⲟⲕυⲏⲩⲧⲩю ⲭⲩяⲙυ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡυⲥⲧяⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲧⲭⲩⲱⲏⲉύ. ⲧы ⲯⲉ ⲃыⳝⲗяⲇⲟⲕ ⲉⳝⲁⲏⲏыύ, я ⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲧыⲕⲁⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲧы ⲥⲟⳝⲁⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⲃыⲕⲩⲡⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡυⲥⲧυⲗυ ⲃⲥⲉ ⲇыⲣⲕυ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυⲉ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲉⳝⲁⲏⲩⲏю ⲃ ⲣⲟⲧ ⲱⲁⲧⲁⲗ, ⲡⲟⲏυⲙⲁⲉⲱь ⲩ ⲧⲉⳝя ⲏⲉⲧ ⲃⲁⲣυⲁⲏⲧⲟⲃ, ⲧы ⳝⲩⲇⲉⲱь ⲙⲟⲉⲙⲩ ⲭⲩю ⲟⲧⲇⲁⲃⲁⲧьⲥя ⲕⲁⲁⲕ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲥⲥⲁⲏⲟύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲁⲕ, ⲧⲟ ⲉⲥⲧь ⲧы ⲏⲉ ⲣⲉⲱυⲗ ⳅⲁⲇⲁⳡⲩ ⲥⲧⲁⲃⲗю ⲧⲉⳝⲉ ⳅⲁ эⲧⲟ 2 ⲭⲩя ⲏⲁ ⲟⲧⲥⲟⲥ, ⲧⲁⲕ ⲏⲟⲃⲁя ⳅⲁⲇⲁⳡⲁ ⲏⲟ ⲗⲉⲅⲕⲁя ⲇⲁⲯⲉ ⲧⲁⲕⲟύ ⲭⲩⲉⲥⲁⲥ ⲕⲁⲕ ⲧы ⲥⲙⲟⲯⲉⲧ ⲣⲉⲱυⲧь эⲧⲩ ⳅⲁⲇⲁⳡⲩ ⲃⲟⲧ ⲥⲙⲟⲧⲣυ, ⲧⲃⲟя ⲙⲁⲧь ⲥⲡⲣяⲧⲁⲗⲁ ⲩ ⲥⲉⳝя ⲃ ⲡυⳅⲇⲉ 17 ⳅⲟⲗⲟⲧыⲭ ⲙⲟⲏⲉⲧ, ⲡⲣυⲱⲉⲗ ⲏυⲅⲉⲣ ⲟⲧьⳝⲉⲗ ⲉё υ ⲟⲏ ⲏⲁⲥⲕⲣⲉⳝ ⲥ ⲉⲉ ⲡυⳅⲇы 7 ⲙⲟⲏⲉⲧ, ⲥⲕⲟⲗьⲕⲟ ⲙⲟⲏⲉⲧ ⲃ ⲡυⳅⲇⲉ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲩ ⲏⲁⲥ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲏⲁⳡⲁⲗⲁⲥь ⲗюⳝⲟⲃь, я ⲉё ⲉⳝⲩ, υ ⲟⲏⲁ ⲙⲟύ ⲭⲩύ ⲟⲧⲥⲁⲥыⲃⲁⲉⲧ, ⲧы ⳝⲩⲇⲉⲱь ⲧⲁⲕ-ⲯⲉ ⲟⲥⲧⲁⲥыⲃⲁⲧь ⲕⲁⲕ υ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⳅⲁⲅⲏⲟⲉⳝⲗⲉⲏⲏⲁя ⲭⲩяⲙυ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁ я ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕυⲧⲕⲁύⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲃ ⲯⲟⲡⲩ ⲧⲣⲁⲭⲏⲩ, ⲥⲗыⲱυυⲱь ⲧы ⲯⲟⲡⲁ ⲃⲟⲗⲟⲥⲁⲧⲁя. я ⲃ ⲧⲉⳝя ⳝⲩⲇⲩ ⲃⲭⲟⲇυⲧь ⲃ ⲟⳝ ⲧⲃⲟυ ⲃⲟⲗⲟⲥы ⲃыⲧⲉⲣⲁⲧь ⲥⲃⲟю ⲥⲡⲉⲣⲙⲩ ⲕⲟⲧⲟⲣⲩю ⲏⲁⲕⲟⲏⳡⲁю ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃыⲉⳝыⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲕⲩ. υ ⲟⲥⲧⲁⲃυⲗ ⲏⲁ ⲉё ⲡυⳅⲇⲉ ⲇⲁⲯⲉ ⲧⲁⲧⲩⲭⲩ ⳝⲉⲁⲏⲏⲁя ⲧы ⲭⲩⲉⲧⲁ, я ⲃⲥⲉⲣⲟⲃⲏⲟ ⲏⲁⲉⳝⲁⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲁⲕⲁⲕⲩ ⲕⲟⲏⳡⲉⲏⲩю   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃыⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⳅⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲗⲉⲧⲁⲉⲧ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲉⲉⲣⲉⳅ ⳡⲁⲥ?), ⲃⲁⲫⲗⲉⲣⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗυⲧⲟⲕ ⲉⳝⲁⲏⲏыύ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲟⲣⲁⲗьⲏⲟ υ ⲟⲣⲁⲗьⲏⲟ ⲩⲏυⲯⲩ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲭⲩⲉⲧⲁ, ⲙⲁⲧь ⲧⲃⲟя ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁⲉⳝⲁⲏⲏⲁя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ, ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲗυⲃⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲱⲁⲱⲗыⲕ ⲉⳝⲁⲏⲏыύ, я ⲧⲉⳝя ⲡⲟⲣⲉⲯⲩ ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩⲉ ⲙⲟⲣⲇⲁ ⲧы ⲥⲩⲕⲁ ⲕⲁⲃⲕⲁⳅⲥⲕⲁя, я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲕⲩⲕⲗⲩ ⲃ ⲡυⳅⲇⲁⲕ ⲉⳝⲁⲗ, ⲅⲏυⲗⲟⲉⳝⲕⲁ ⲧы ⲉⳝⲁⲏⲁⲏя. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗυ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲉⳝⲁⲏⲏⲟύ?), ⲧы ⲡⲟⲕⲁⲯⲉⲱь ⲙⲟⲉⲙⲩ ⲭⲩю ⲙⲁⲥⲧⲉⲣ ⲕⲗⲁⲥⲥ. ⲕⲁⲕ ⲧы ⲩⲙⲉⲉⲱь ⲥⲃⲟⲉύ ⲅⲩⳝⲟύ ⲇⲉⲗⲁⲧь ⲉⳝⲁⲏⲏⲁя ⲥⲟⲥⲕⲁ)?   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃыⲉⳝⲩ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃыⲧⲣⲁⲭⲁⲗ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲡⲉⳡⲁⲗьⲏⲟύ, ⲃⲟⲧ ⲧы ⲙⲣⲁⳅⲟⲧⲁ ⲕⲟⲏⳡⲉⲏⲏⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲡⲟⲗυⲥⲙⲉⲏⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲃ ⲣⲟⲧ ⲱⲁⲧⲁⲗ ⳝⲟⲙⲯⲁⲣⲁ ⲧы ⲥⲩⲕⲁ ⲏⲉ ⲟⲕⲟⲗⲁⳡυⲃⲁύⲥя ⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲉⳝⲁⲏⲏⲁя ⲇⲩⲣⲁ ⲥⲩⲕⲁ. цыⲅⲁⲏⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя ⲃ ⲣⲟⲧⲁⲏ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲥⲩⲕⲁ ⳡⲩⲣⳝⲁⲏ ⲉⳝⲁⲏыⲏύ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳡυⲥⲧⲟ ⲃыⲉⳝⲩ υ ⲃыⲕυⲏⲩ ⲉⳝⲁⲏⲁя ⲧы ⲱⲙⲁⲣⲁ, я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲏⲁⲉⳝⲁⲱυⲗ ⲥⲗыⲱυⲱь ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⳝⲉⲁⲏⲏⲁя)?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲩⲉⲥⲟⲥⲕⲩ ⳅⲁⲡυⳅⲇυⲗ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ, ⲉⳝⲁⲏⲏыύ ⲧы ⲉⲃⲏⲩⲭ я ⳡυⲥⲧⲟ ⲩⲅⲟⲣⲁю ⲏⲁⲇ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲣⲃⲁⲏⲟύ), я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲧⲣⲁⲭⲁю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲩⲇⲉⲱь ⲇⲉⲣⲯⲁⲧь ⲙⲟύ ⲭⲩύ ⲩ ⲥⲉⳝя ⲃ ⲣⲩⲕⲁⲭ ,υ ⲏⲁⲥⲁⲥыⲃⲁⲧь ⲏⲁ ⲉⳝⲗю ⲥ υⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲉⳝⲁⲏⲏⲟύ , я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⳝⲉⲅυ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲉⲁⲏⲏⲁя ⲇыⲣⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲣυⲥⲧⲉⳝыⲃⲁⲗⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲥⲃⲟю ⲡυⳅⲇⲩ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲕⲗяⳡⲁ. я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ. ⲅⲟⲗⲩⳝⲟⲅⲗⲁⳅⲁя ⲧы ⲱⲁⲗⲁⲃⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⳅⲟⲃⲩ ⲏⲁ ⲉⳝⳝⲗю ⲕ ⲥⲃⲟⲉⲙⲩ ⲭⲩю, ⲉⳝⲁⲏⲁⲏя ⲧы ⲡⲇυⲟⲣⲁⲥⲕⲁ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⳅⲣя ⲏⲁⲡⲁⲗⲁ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲃⲟⲉύ ⲧьⲉⳝⲁⲏⲏⲟύ ⲡυⳅⲇⲟύ ⲗⲟⲭ ⲧы ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲉⳝⲁⲧь ⲇⲁ я ⲃⲏⲁⲧⲩⲣⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲭⲩяⲙυ ⳅⲁⲕυⲇⲁю ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⳝⲩⲇⲉⲧ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲧь, ⲉⳝⲁⲏⲏыύ ⲧы ⲥⲩⲕⲁ ⲟⳡⲕⲟⲏⲁⲃⲧ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⳡυⲥⲧⲟ ⲡⲟⲇⲏυⲙⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩⲉ. ⲉⳝⲁⲧь ⲟⲏⲁ ⲁⲭⲉⲩⲃⲁⲗⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲗⲩⲱⲁ, ⲥⲗыⲱυⲱь ⲧы ⲥⲏⲁύⲡⲉⲣ ⲙⲟⲉⲅⲟ ⲭⲩя. я ⲏⲁⲉⳝыⲃⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭυ ⲉⳝⲁⲏⲏⲟύ)ъ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲥⲡⲣⲁⲱυⲃⲁⲉⲧ ⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲡⲟⳡⲉⲙⲩ ⲟⲏ ⲧⲁⲕ ⲙⲁⲗⲟ ⲩⲇⲉⲗяⲉⲧ ⲉύ ⲃⲏυⲙⲁⲏυя, ⲕⲁⲕ ⲇⲩⲙⲁⲉⲱь ⲡⲉⲣⲉⲥⲧⲁⲧь ⲧⲉⳝя ⲉⳝⲁⲧь ⳡⲧⲟⲗⲉ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲧⲣⲁⲭⲁю ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲉⲃⲏⲩⲭ ⲥⲩⲕⲁ, ⲙⲟύ ⲭⲩύ ⲡⲟυⲙⲉⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲗⲏⲟⲥⲧью ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⲥⲕⲁ), я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ ⲟⲧьⲉⳝⲩ ⲭⲩⲉⲙ ⲥⲗыⲱυⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲕⲗⲟⲩⲏ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲡυⳅⲇⲁⲕ ⲃыⲧⲣⲁⲭⲁю ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲧⲁ, ⲙⲟύ ⲭⲩύ ⲃ ⲡⲁⲣⲁⲱⲉ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲃⲟⲧ ⲧы ⲥⲩⲕⲁ ⲇⲁⲩⲏυⲧⲁ ⲉⳝⲁⲏⲁя, ⲧы ⲯⲉ ⲥⲃυⲏья ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲇь ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲣⲩⲱυⲗⲁ ⲥⲃⲟю ⲡⲥυⲭυⲕⲩ ⲙⲟυⲙ ⲭⲩⲉⲙ. я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⲣⲡυⲗы ⲃыⲉⳝⲩ. ⲥⲗыⲱυⲱь ⲧы ⲙⲟύ ⲭⲩύ ⲥⲟⲥυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲇⲉⲗⲁⲗυ ⲟⳝⳅⲟⲣ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ?)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃыⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲕⲩ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲇⲁ ⲉⳝⲁⲗυ ⲉё ⲭⲟⲣⲟⲱⲟ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲩ, ⲥⲗыⲱυⲱь ⲗяⲣⲃⲁ ⲉⳝⲁⲏⲁя. я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ υ ⲃыⲕυⲏⲩ ⲏⲁ ⲭⲩύ. ⲡⲁⲣⲁⲱⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲅⲁⲣⲁⲯⲉ ⲉⳝⲁⲗ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ. ⲧы ⲡⲣⲟⲧⲩⲭⲱυύ ⲡⲉⲧⲩⲭ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕⲩⲕⲁⲣⲉⲕⲁⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲕⲟⲧⲟⲣⲩю ⲟⲧьⲉⳝыⲃⲁюⲧ ⲕⲁⲯⲇыύ ⲇⲉⲏь)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⳅⲟⲣⲏⲩю ⲃ ⲣⲟⲧⲁⲏ, ⲕⲟⲏⳡⲉⲏⲁⲏя ⲧы ⲡυⳅⲇⲁⲅⲗⲟⲧⲕⲁ?). я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ ⲉⳝⲁⲏⲏⲁя0   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲙⲩⲇⲗⲁⲏⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя. ⲧы ⳝⲩⲇⲉⲱь ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲗυⲡⲏⲩⲧь ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲉⳝⲁⲏⲏⲟύ, ⲧы ⲭⲩⲗⲉ ⲧⲁⲕⲟύ ⲏⲁⲉⳝⲁⲏⲏыύ ⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲧы ⲉⳝⲁⲏⲏыύ ⲙⲩⲇⲗⲁⲏ. ⲃⲥⲉⲣⲟⲃⲏⲟ ⲙⲟύ ⲭⲩύ ⲃыⲧⲣⲁⲭⲁⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲕⲩ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲡυⳅⲁⲇ ⲃⲧⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲥⲗыⲱυⲱь ⲧы ⲏⲉⳡⲉⲥⲧь ⲉⳝⲁⲏⲁⲏя. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩⲃ ⲣⲟⲧ ⲏⲁⲉⳝыⲃⲁ ⲕⲟⲏⳡⲉⲏⲏы ύⲧы ⳡⲗⲉⲏⲟⲥⲟⲥⲟ ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲟⲡяⲧь ⲕⲟⲡυⲣⲟⲃⲁⲧь ⲡⲟⲱⲉⲗ ⲡⲟ ⲃⲧⲟⲣⲟⲙⲩ ⲕⲣⲩⲅⲩ, ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲟⲧьⲉⳝⲁⲏыύ ⲧы ⲇⲁⲩⲏ. я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲧⲣⲁⲭⲁю ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲉⳝⲁⲏⲏⲁя ⲧы ⲕⲩⲣⲟⲡⲁⲧⲕⲁ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲉⳝⲁⲏⲏⲁя ⲡⲁⲣⲁⲱⲁ ⲃ ⲕⲟⲧⲟⲣⲩю я ⲥⲥⲩ. ⲥⲗыⲱυⲱь ⲧы ⲅⲁⲣⲙⲟⲏыύ ⲡⲉⲧⲩⲭ, я ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ ⳡυⲥⲧⲟ ⲥⲗⲗью ⲃⲩⲏυⲧⲁⳅ ⳅⲁⲥⲩⲏⲩ ⲉⳝⲁⲏⲏⲩю ⲡⲁⲣⲁⲱⲩ ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲃ ⲡⲟⳅⲉ ⲗⲟⲧⲟⲥⲁ ⲟⲧⲇⲁⲉⲱьⲥя ⲙⲟⲉⲙⲩ ⲭⲩю, ⲥⲗыⲱυⲱь ⲏⲁⲥⲥⲁⲏыύ ⲡⲉⲧⲩⲭ .я ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲟⲣⲟⲧ ⲟⲧьⲉⳝⲩ. ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲥⲏⲉⲅ я ⲧⲉⳝя ⲭⲩⲉⲙ ⲕⲟⲣⲙυⲗ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳝⲟⲗⲉⲉⲧ ⲥⲡυⲇⲟⲙ ⲉⳝⲁⲏⲏⲁя ⲥⲟⳝⲁⲕⲁ.я ⲉё ⲟⲧⲣⲁⲭⲁю ⲃ ⲡυⳅⲇⲩ ⲥⲗыⲱυⲱь ⲧы ⲇⲟⲕⲩⲙⲉⲏⲧ, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲏⲉ ⲇⲁⲗⲁ ⳝⲩⲙⲁⲅυ ⲡⲟ ⲕⲟⲧⲟⲣыⲙ я ⲙⲟⲅⲩ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь ⲕⲁⲕ ⲥⲟⳝⲁⲕⲩ   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲕⲟⲅⲇⲁ ⲥⲟ ⲙⲏⲟύ ⲟⳝⳃⲁⲉⲱьⲥя ⲧы ⲥυⲇυⲱь ⲩ ⲙⲉⲏя ⲡⲟⲇ ⲥⲧⲟⲗⲟⲙ υ ⲡыⲧⲁⲉⲱьⲥя ⳡⲧⲟ-ⲧⲟ ⲥⲕⲁⳅⲁⲧь ⲃ ⲧⲟ ⲃⲣⲉⲙя ⲕⲟⲅⲇⲁ я ⲧⲉⳝя ⲉⳝⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲇⲩⲣⲕⲩ. ⲧы ⲯⲉ ⲏⲁ ⲭⲩύ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲏⲉⲱь ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲩ ⲧⲉⳝя ⳝⲩⲇⲉⲧ ⲣⲟⲧ ⳝⲟⲗⲉⲧь ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ ⲙⲟύ ⲭⲩύ ⲟⲧьⲉⳝⲉⲧ ⲧⲉⳝя ⲙⲩⲇⲗυⳃⲉ ⲥⲩⲕⲁ ⲕⲟⲏⳡⲉⲏⲏⲟύ, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲟⲧⲇⲁⲉⲧⲥя ⲙⲏⲉ ⳝⲟⲧⲁⲏυⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇⲩⲣⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲗⲟⲯυⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ, ⲧⲁⲕ ⲥⲕⲁⳅⲁⲧь ⲡⲟⲕⲣыⲃⲁⲉⲧ ⲉⲅ ⲟⲉⳝⲁⲏⲁⲏя ⲇⲩⲣⲁ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⳡⲕⲁⲥⲧⲩю ⲥⲩⲕⲁ ⲇⲩⲣⲩ, ⲧы ⲯⲉ ⲥ ⲧⲩⲡыⲙ ⲉⳝⲁⲗⲟⲙ ⲟⲧⲇⲁⲱьⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃыⲉⳝⲁⲏⲏⲁя, ⲧы ⲯⲉ ⲟⲃⳡⲁⲣⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ, ⲃыⲉⳝⲁⲏⲏыύ ⲧы ⲥⲩⲕⲁ ⳡⲗⲉⲏⲟⲥⲟⲥ), ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲙⲟⲅⲁⲧь ⲙⲟⲉⲙⲩ ⲭⲩю ⲉⳝⲁⲧь ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲉⳝⲁⲏⲏⲟύ. ⲧы ⲯⲉ ⲕⲟⲏⳡⲉⲏⲏыύ ⲇⲁⲩⲏ ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲃ ⲣⲟⲧ ⲇⲁю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇⲉⲅⲉⲏⲉⲣⲁⲧⲕⲁ ⲉⳝⲁⲏⲏⲁя)?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲉⲗⲁ ⲣⲁⳅⲏыⲉ ⲡⲉⲥⲏυ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲏⲏⲁя ⲧы ⲇⲩⲣⲁ ⳝⲗяⲇь,я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲥⲃυⲏья. я ⳡυⲥⲧⲟ ⲇⲟⲭⲩя ⲃⲣⲉⲙⲉⲏυ ⲩⲇⲉⲗяю ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲉⲃⲣⲟⲡⲉύⲏыύ ⲧы ⲭⲩⲉⲥⲟⲥ, я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⳅⲁⲧⲣⲁⲭⲁю)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕⲟⲏⳡⲏⲉⲏⲁя ⲥⲟⲥⲕⲁ ⲕⲟⲧⲟⲣⲩю я ⲉⳝⲩ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲩ ⲡⲟⲇ ⲁⲭⲩⲉⲏⲏⲩю ⲙⲩⳅыⲕⲩ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲟⳡⲁⲗⲕⲁ. ⲟⲧⲇⲁύⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⲧьⲉⳝⲩ, ⲙυⲇⲉⲣ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ. ⲧы ⳝⲩⲇⲉⲱь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲥⲧⲟяⲧь ⳡⲧⲟ-ⳝы ⲩ ⲧⲉⳝя ⲏⲉ ⲥⲧυⲗυⲗυ ⲕⲣυⲡⲟⲃ ⲉⳝⲁⲏⲏⲁя ⲧы ⲱⲁⲃⲕⲁ. ⲙⲟύ ⲭⲩύ ⲡⲟⲣⲃⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲧы ⲯⲉ ⲉⳝⲁⲏⲏыύ ⲁⲏⲁⲏⲁⲥ ⲃ ⲕⲟⲧⲟⲣыύ я ⲧыⲕⲁю ⲭⲩⲉⲙ. ⲉⳝⲁⲏⲏⲁя ⲱⲗяⲡⲁ ⲧы ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗⲟ ⲥⲧⲁⲇⲟ ⳝыⲕⲟⲃ ⲉⳝⲁⲏⲏⲁя ⲧы ⳡⲉⲗⲕⲁⲥⲧⲁя ⲭⲩύⲏя)?, ⲧы ⲯⲉ ⲭⲁⳡⲩⲅⲁ ⲉⳝⲁⲏⲁя, я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⲃⲟ ⲃⲥⲉⲭ ⲩⲕⲣⲁυⲏⲥⲕυⲭ ⲡⲟⳅⲁⲭ ⲡⲟ ⲕⲁⲙⲁⲥⲩⲧⲣⲉ ⲉⳝⲁⲏⲏⲁя ⲧы ⳝυⳝⲗυя. я ⲡⲣⲟⳡυⲧⲁⲗ ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲇⲟ ⲉⳝⲁⲧь ⲥυⲗьⲏⲟ ⲭⲩⲉⲙ ⲃ ⲯⲟⲡⲩ. ⲇⲁⲃⲁύ ⲡⲟⲡⲣⲟⳝⲩⲉⲱь ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲏⲁ ⲡⲁⲣⲩ ,ⲉⳝⲁⲏⲏыⲉ ⲭⲩⲉⲅⲗⲟⲧы)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲟⲧⲣⲉⲡⲁⲏⲏⲁя ⲱⲁⲗⲁⲃⲁ. ⲧы ⲯⲉ ⲉⳝⲁⲏⲁя ⲙⲟⳝυⲗⲕⲁ ⲏⲁ ⲕⲟⲧⲟⲣⲩю я ⲕⲟⲡυⲗ ⲙⲏⲟⲅⲟ, υ ⲙⲏⲟⲅⲟ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲏⲉⲩю, ⲧы ⲯⲉ ⲃыⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕⲕя. ⲕⲟⲏⲉⲏⲏⲁя ⲥⲃυⲏья   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲣⲟⲧⲩⲭⲱⲩю ⲭⲩяⲙυ. ⲧы ⳝⲩⲇⲉⲱь ⲫⲁⲏⲧⲁⳅυⲣⲟⲃⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⳡⲧⲟⲗⲉ, ⲉⳝⲁⲏⲏя ⲧы ⲇыⲣⲕⲁ ⲥⲩⲕⲁ. ⲧы ⲯⲉ ⲕⲩⲃⲱυⲏ ⲉⳝⲁⲏⲏыύ ⲃ ⲕⲟⲧⲟⲣыύ я ⲥⲥⲩ ⲉⳝⲁⲏⲏⲁя ⲙяⲙⲗя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, цⲃⲉⲧⲟⲕ ⲧы ⲥⲩⲕⲁ ⲏⲁⲉⳝⲁⲏⲏыύ ⲭⲩⲉⲙ. яⲧ ⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲇ ⲃⲟⲕⲁⲗ ⲉⳝⲁⲗ, ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲡⲗⲟⳃⲁⲇⲕⲁ ⲇⲗя ⲭⲩⲉύ. ⲧы ⲅⲗⲁⲃⲏⲟⲉ ⲏⲉ ⲡⲗⲁⳡь ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲉⳝⲉⲧ ⲧⲃⲟύ ⳅⲁⲥⲥⲁⲏы ύⲣⲟⲧ ⲟⲧьⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲧⲩⲱⲉⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲡⲟⲗяⲏⲉ ⲉⳝⲁⲗ ⲅⲏυⲗь ⲧы ⲉⳝⲁⲏⲏⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ υⲏⲃⲁⲗυⲇⲕⲩ ⲉⳝⲁⲏⲏⲩю, ыⲧ ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⳝыⲗ ⲡⲟⲙⲉⲱⲁⲗ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⲥⲗыⲱυⲱь ⲭⲁⳡ ⳝⲉⲁⲏⲏыύ. ⲧы ⲯⲉ ⲥⲟⲥⲟⲕ ⲕⲟⲏⳡⲉⲏⲏыύ ⲕⲟⲧⲟⲣыύ я ⲃыⲇⲉⲣⲏⲩ ⲃⲥ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲁⲉⳝⲁⲏⲏыύ ⲕⲗυⲧⲟⲣ ⲙⲁⲧь ⲧⲃⲟя ⲱⲁⲗⲁⲃⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⲥ ⲁⲭⲩⲉⲏⲏыⲙυ ⲧⲃⲟυⲙυ ⲕⲟⲟⲣⲉⲱⲁⲙυ ⲕⲟⲧⲟⲣыⲉ ⲡⲟⲇⲇⲉⲣⲯυⲃⲁⲗυ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲟⲏⳡⲉⲏⲏⲟύ, ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲧы ⲥⲟⳝⲁⲕⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲟⲏⳡⲉⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲙⲟύ ⲭⲩύ ⲧⲩⲱυⲧ ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲧы ⲫⲁⲏⲁⲣь ⲉⳝⲁⲏⲏыύ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲡⲉⲉⲧⲩⲭ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲉ ⲃыⲃⲟⳅυⲧ ⲙⲟύ ⲭⲩύ ⲟⲟⲇⲏⲁ. ⲧы эύ ⲡⲟⲙⲟⲅⲁⲉⲱь ⲉⳝⲁⲏⲏⲟύ ⲱⲃⲁⳝⲣⲉ. ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲙⲉⲱⲁⲏⲏⲁя, ⲧы ⲯⲉ ⲃыⲉⳝⲁⲏⲏыύ ⲉⲃⲏⲩⲭ ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲇⲁю ⲃ ⲣⲟⲧⲁⲏ. ⲧы ⲯⲉ ⲏⲁⲉⳝⲁⲏⲏыύ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⲃⲣⲉύ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧ ⲟⲟⲧⲇⲁⲗⲁⲥь ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲥⲟⳝⲁⲕⲁ ⲉⳝⲁⲏⲁⲏя, ⲧы ⲯⲉ ⳅⲁⲉⳝⲁⲏⲏыύ ⲉⲃⲏⲩⲭ ⲃ ⲡυⳅⲇⲩ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲟⲥⲧⲁⲏⲟⲃⲕⲉ ⲉⳝⲩ ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲏⲁ ⲭⲩύ ⲥⲃⲟυ ⲫⲉύⲗы ⳅⲁⲥⲩⲏь ⲃ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲧⲩⲇⲁ-ⲯⲉ ⲅⲇⲉ ⲙⲟύ ⲭⲩύ ⲟⲣⲩⲇⲩⲉⲧ, ⲥⲗыⲱυⲱь ⲱⲙⲁⲣⲁ ⲉⳝⲁⲏⲏⲁя, ⲧⲉⳝⲉ ⲯⲁⲣⲕⲟ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⲗⲉ ⲟⲧьⲉⳝⲁⲏⲏы ύⲇⲁⲩⲏ. я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲗⲉⲥⲩ ⲧⲣⲁⲭⲏⲩ ⲗⲉⲥⲟⲣⲩⳝⲕⲩ ⲕⲟⲏⳡⲉⲏⲏⲩ, ⲧы ⳝⲩⲇⲉⲱь ⲩⲥⲡⲟⲕⲁυⲃⲁⲧь ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⲗⲉ ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲁⲃⲏⲁⲣьⲕⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲁⲯⲁⲗ ⲕⲁⲣⲧⲟⲱⲕⲩ ⲙⲩⲇⲗⲁⲏⲕⲁ ⲧы ⲩⳝυⲧⲁя ⳡⲗⲉⲏⲟⲙ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲕⲟⳡⲏⲉⲏⲏыύ ⲅⲁⲏⲃⲟⲉⲇ я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲣⲙⲗю ⲅⲁⲃⲏⲟⲙ ⲗⲟⲭ ⲉⳝⲁⲏⲏыύ0   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲩ ⲙⲉⲏя 2 ⲭⲩя. ⲟⲇυⲏ ⲃⲉⳡⲏⲟ ⲃ ⲧⲉⳝⲉ ⲁ ⲃⲧⲟⲣⲟύ ⲡⲁⲥⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲥⲗыⲱυⲱь ⲧⲉⳝⲉ ⲭⲟⲗⲟⲇⲏⲟ?), я ⲧⲉⳝя ⲥⲟⲅⲣⲉю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲏя ⲧы ⲙⲁⲏⲇⲁⲃⲟⲱⲕⲁ, ⲧы ⳝⲩⲇⲉⲱь ⲏⲉ ⲡⲣυⲥⲧⲟύⲏⲟ ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲏⲏⲁя ⲧы ⲡυⲇⲟⲣⲁⲥⲕⲁ. ⲧы ⲯⲉ ⲡυⳅⲇⲁⲥⲟⲥ ⲧы ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя, я ⲧⲉⳝя ⲥⲏⲉⲥⲩ ⲇⲁⲩⲏⲁ ⲉⳝⲁⲏⲏⲟⲅⲟ .я ⲏⲉ ⲟⲧⲣυцⲁю ⳡⲧⲟ ⲉⳝⲁⲗ ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲏⲁⲉⳝⲁⲱⲩ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⳡⲏⲉⲏⲏⲟύ ⲧⲁⲕ ⳡⲧⲟ ⲟⲏⲁ ⲁⲭⲩⲉⲉⲧ, ⲥⲗыⲱυⲱь ⲧы ⲟⳅⲁⳝⲟⳡⲉⲏⲏыύ ⲭⲩⲉⲥⲟⲥ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ ⳝⲁⲕⲗⲁⲏ ⲥⲕⲁ ⲏⲁⲡυⳅⲇⲯⲉⲏⲏыύ ⲭⲩяⲙυ. ⲧⲁⲕⲟύ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲏⲁⲉⳝⲁⲏⲩⲏю ⲭⲩяⲙυ ⲡυⳅⲇυⲗ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲏⲟⲅⲟ ⲟⲣⲩⲇⲟⲃⲁⲗ, υ ⲥⲇⲉⲗⲁⲗ ⲃ ⲏⲉύ ⲥⲃⲟю ⲕⲟⲡυю ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲉ ⲣⲁⲥⲥⲗⲁⳝⲗяⲗⲁⲥь ⲕⲟⲅⲇⲁ ⲥυⲇυⲧ ⲥⲁⲙⲁ ⳝⲉⳅ ⲙⲟⲉⲅⲟ ⲭⲩя ⲇⲟⲙⲁ. ⲟⲧьⲉⳝⲁⲏⲏыύ ⲟⲗⲩⲭ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲩ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲩⲭⲁⲏⲕυ ⲉⳝⲁⲏⲏⲟύ, ⲥⲗыⲱυⲱь ⲧы ⲙⲁⳡⲩⲭⲁ ⲭⲩⲉύ ⲕⲟⲧⲟⲣыⲉ ⲧⲩⲥⲩюⲧьⲥя ⲃ ⲧⲃⲟⲉύ ⲯⲟⲡⲉ. ⲧы ⲯⲉ ⲏⲁⲉⳝⲁⲏⲏыύ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲇⲁⲩⲏ ⲕⲟⲧⲟⲣⲟⲅⲟ я ⲉⳝⲩ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲇⲉⲗⲁⲉⲧ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲗυⲱⲕⲟⲙ ⲙⲏⲟⲅⲟ ⲇыⲣⲟⲕ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲩⲭⲏⲉⲧ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃⲟⲧ ⲃыⳝⲉⲁⲏⲏⲁя ⲇыⲣⲕⲁ ⲥⲕⲁ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲣⲁⳅⲏⲩю ⲭⲩύⲏю ⲧⲃⲟⲣυⲧ ⲉⳝⲁⲏⲁⲏя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⲥⲩⲕⲁ. ⲙⲟύ ⲭⲩύ ⳅⲁⲙⲉⳡⲁⲁⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲥⲉⳝⲉ ⲉⳝⲁⲏⲏы ύⲧы ⲗⲟⲭ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃⲣ ⲟⲧ ⲃыⲉⳝⲩ, ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁύⲇⲉⲧ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲡυⳅⲇⲯⲉⲏⲏⲟύ ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲉⳝⲁⲏⲁⲏя ⲥⲟⳝⲁⲕⲁ ⲭⲩⲉⲙ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲃⲟⲟⳝⳃⲉ ⲇⲏυⲏⲁ ⲕⲟⲏⳡⲉⲏⲏⲁя. ⲧы ⲙⲟύ ⲭⲩύ ⲗⲟⲃυⲱь ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲏⳡⲉⲏⲏⲟύ)?   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲅⲟⲗⲟⲇⲏⲩю ⲡυⳅⲇⲩ ⲏⲁⲧⲣⲁⲭⲁю ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύы ⲧы ⲡυⳅⲇⲁⲥⲟⲥ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⳅⲁⲉⳝⲁⲏⲏыύ ⲭⲩⲉⲅⲗⲟⲧ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧⲃыⲉⳝⲩ. ⲕⲟⲏⳡⲉⲏⲏы ύⲧы ⲇⲁⲏ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲥⲡⲉⲣⲙⲟⲅⲗⲟⲧⲕⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲇⲣⲟⳡυⲧ ⲥⲃⲟⲉύ ⳅⲁⲥⲥⲁⲏⲟύ ⲡυⳅⲇⲟύ ⲥⲗыⲱυⲱь ⲇⲁⲩⲏ ⲉⳝⲁⲏⲏыύ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲭⲁⲭⲁⲭ,ⲧы ⲙⲟύ ⲭⲩύ ⲟⲧⲥⲟⲥⲁⲗ υ ⲣⲉⲱυⲗ ⲧⲉⲡⲉⲣь ⲥьⲯⲉⲁⲧь ⲕⲁⲕ ⲉⳝⲁⲏⲏⲁя ⲇⲩⲣⲕⲁ?. ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲏⲟⲅⲟ ⲣⲁⳅⲏⲟύ ⲭⲩύⲏυ ⲙⲩⲧυⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏыⲏύ ⲗⲟⲭ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃыⲉⳝⲩ ⲥⲗыⲱυⲱь ⲧы ⲕⲟⲏⳡⲉⲏⲏⲁя ⲙⲣⲁⳅⲟⲁⲧ, ⲃⲧⲟя ⲙⲁⲙⲁⲱ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ. я ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲇⲣⲟⳡυⲧ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ, ⲥⲗыⲱυⲱь ⲧы ⲉⳝⲁⲏⲏⲁя ⲅⲁⲏⲇⲟⲏⲕⲁ.я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟ ⲟⲧьⲉⳝыⲃⲁю ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲅⲁⲏⲇⲟⲏⲟⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳅⲁ ⲅⲟⲣⲟⲇ ⲃыⲃⲟⳅυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ. ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲣⲁⳅⲏыⲉ ⲧⲣюⲕυ ⲇⲉⲗⲁⲉⲧ ⲙⲟύ ⲭⲩύ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲱⲙⲁⲣⲁ ⲥⲩⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ), ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲅⲟⲣυⲧ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲉⳝⲁⲗ ⲧⲁⲕυⲭ ⲕⲁⲕ ⲧы ⲃ ⲣⲟⲧⲁⲏ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲣⲁⲥⲥⲉⲗⲁⲥь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲉⳝⲁⲏⲁя ⲇⲩⲣⲁ.я ⲱⲩⲣⲩύ ⲟⲧ ⲥюⲇⲁ ⲡⲟⲕⲁ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲉ ⲃыⲉⳝⲁⲗ, ⲧы ⳡⲧⲟ ⲟⲣⲉⲱь ⲏⲁ ⲙⲟύ ⲭⲩύ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲉⳝⲕⲁ ⲥⲩⲕⲁ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲗяⲣⲃы ⲃыⲉⳝⲩ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲃыⲣⲃⲁⲗ υⳅ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲗυⲧⲟⲣ υ ⲇⲁⲗ ⲧⲉⳝⲉ ⲉⲅⲟ ⲥⲟⲯⲣⲁⲧь ⲉⳝⲁⲏⲏы ύⲧы ⲡυⲇⲟⲣⲕⲁⲥ. ⲧы ⲩⲗⲟⲯυⲱьⲥя ⲃ υⲏⲧⲉⲣⲃⲁⲗⲉ ⲃ 10 ⲙυⲏⲩⲧ ⳡⲧⲟ-ⳝы я ⲕⲟⲏⳡυⲗ ⲏⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲭⲣⲁⲏяⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲧ цыⲅⲁⲏⲟⲃ ⲉⳝⲁⲏⲏыⲭ ⲕⲟⲧⲟⲣыⲉ ⲉё ⲉⳝⲩⲧ ⲡⲟ 24 ⳡⲁⲥⲁ ⲃ ⲇⲉⲏь, ⲉⳝⲁⲏⲁⲏя ⲧы ⲇυⳡь   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳝⲉⲅⲁⲗⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟ ⲥⲧⲁⲇυⲟⲏⲩ, ⲃⲟⲧ ⲥⲡⲟⲣⲧⲥⲙⲉⲏⲕⲁ ⲉⳝⲁⲏⲏⲁя,я ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲟⲏⳡⲉⲏⲏⲩю ⲱⲙⲁⲣⲩ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲃⲟⲗⲅⲁ ⲉⳝⲁⲏⲁⲏя. ⲙⲟύ ⲭⲩύ ⳝⲩⲇⲉⲧ ⲕⲁⲧⲁⲧьⲥя ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲣⲩⳡяⲉⲕ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы. ⲯⲁⳝⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳝⲉⳅ ⲥυⲅⲗⲏⲁⲗυⳅⲁцυυ ⲉⳝⲁⲗ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲃⲧⲟя ⲙⲁⲙⲁⲱⲁ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲟⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲥⲃⲟⲉύ ⲁⲏⲁⲗьⲏⲟύ ⲡυⳅⲇⲟύ ,ⲉⳝⲁⲏⲏыύ ⲧы ⲱⲕⲃⲁⲣⲟⲕ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲉⲏя ⲗⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲏⲁя ⲧы ⲇυⳡь ⲥⲩⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ. я ⲧⲃⲟю ⲙⲁⲙⲱⲩ ⲥⲧⲩⲏⲇⲉⲏⲧⲕⲩ ⲧⲁⲣⲏⲭⲩ ⲥⲗыⲱυⲱь ⲧы ⲃыⲉⳝⲁⲏⲏы ύⲉⲃⲣⲉύ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲱⲁⲗⲁⲃⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲃⲥⲁⲥыⲃⲁⲉⲧ ⲉⳝⲁⲏⲁⲏя ⲧы ⲡυⳅⲇⲁⲅⲗⲟⲧⲕⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⲏⲉⲣⲉⲁⲗьⲏⲟ ⲉⳝⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲥⲗыⲱυⲱь ⲧы ⲙⲟⲯⲉⲱь ⲙⲟύ ⲭⲩύ ⲣⲉⲁⲗьⲏⲟ ⲟⲧⲥⲁⲥыⲃⲁⲧ ьыⳝⲥⲧⲣⲉⲉⲉ ⳡⲉⲙ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. я ⲯⲉ ⳅⲁⳝⲉⲣⲩ ⲩ ⲧⲉⳝя ⲃⲥⲉ υⲇ ⲁⲯⲉ ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю ⲭⲩяⲙυ. ⲧы ⲯⲉ ⲟⲕⲏⲟ ⲕⲟⲧⲟⲣⲟⲉ ⲡⲣⲟⳝυⲧⲟⲉ ⲙⲟυⲙ ⲭⲩⲉⲙ. я ⲧⲃⲟю ⲙⲁⲱⲩ ⲏⲁ ⲭⲩю ⲃⲉⲣⲧⲉⲗ ⲉⳝⲁⲏⲁⲏя ⲧы ⲙⲣⲁⳅⲟⲧⲁ)   <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲱⲗюⲭⲁ ⲧы ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟ ⲡⲣⲁⲃⲇⲉ?. я ⲡⲣυⲕⲁⳅⲁⲗ цыⲅⲁⲏⲁⲙ ⲧⲣⲁⲭⲏⲩⲧь ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲧьⲉⳝⲁⲏⲏⲟύ. ⲥⲗыⲱυⲱь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧ ⲟⲧы ⲉⳝⲁⲏⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲕⲟⲧⲟⲣыύ ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲡυⳅⲇⲩ, ⲧы ⲙⲟⲯⲉⲱь ⲥⲇⲉⲗⲁⲧь ⲧⲁⲕ ⳡⲧⲟ-ⳝы ⲧⲃⲟυ ⲕⲟⲣⲉⲱⲁ ⲟⲧⲇⲁⲗυ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲙⲁⲱυ ⲏⲁ ⲙⲟύ ⲭⲩύ. ⲥⲗыⲱυⲱь ⲧы ⲉⳝⲁⲏⲏыύ υⲏⲇюⲕ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁⲕ ⲧы ⲯ ⲉⳝⲁⲏⲏыύ ⲡⲉⲧⲩⲱⲙⲁⲏ ⲕⲟⲧⲟⲣыύ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲉⲱь, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲟⲅⲩ ⲃыⲉⳝⲁⲧь ⲉⳝⲁⲏⲏⲩю ⲇыⲣⲕⲩ, ⲥⲗыⲱυⲱь ⲧы ⲇⲩⲇⲕⲁ ⲉⳝⲁⲏⲏⲁя, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⲭⲣⲁⲏυцⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃыⲉⳝⲩ, ⲧы ⲭⲩⲗⲉ ⲧⲁⲕⲟύ ⲡυⳅⲇⲁⲅⲗⲟⲧ ⲧы ⲩⲏыⲗыύ ⲕⲟⲧⲟⲣыύ ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲣⲟⲧⲁⲏ ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲉⳝⲕⲁ. ⲧы ⲯⲉ ⲟⲧьⲉⳝⲁⲏⲏыύ ⲇⲁⲩⲏ ⲥⲩⲕⲁ?)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲡυⳅⲇⲁⲥⲟⲥ ⲉⳝⲁⲏⲏыύ. ⲧы ⲯⲇⲉⲱь ⲙⲟⲉⲅⲟ ⲭⲩя ⲃ ⲥⲃⲟⲉύ υⳅⲇⲉ ⲙⲁⲙⲁⲱⲉ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲇыⲣⲕⲁ ⲃ ⳡⲉⲣⲏⲟⲙ ⲕⲟⲥⲧьюⲙⲉ ?), я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲣⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲙⲩⲇⲅⲗⲟⲧ ⲉⳝⲁⲏⲏыύ)   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲩⲇⲉⲱь ⲧⲁⲏцⲉⲃⲁⲧь ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲁⲗьⲥ ⲏⲁ ⲃыⲡⲩⲥⲕⲏⲟⲙ ⲉⳝⲁⲏⲏы ύⲧы ⲥⲟⲥⲟⲕ?), ⲧⲉⳝⲉ ⳅⲏⲁⲕⲟⲙы ύⲙⲟύ ⲭⲩύ ⲕⲟⲧⲟⲣыύ ⲧⲣⲉⲧⲥя ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲉⳝⲁⲏⲏⲟύ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲭⲩⲉⲙ ⲗⲉⲥ ⲃⲁⲗυⲗ ⲃ ⲙⲁⲅⲁⲇⲁⲏⲉ))) ⲥⲁⲙ ⲇⲩⲙⲁύ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲙⲁⲙⲉⲏьⲕⲁ ⲙⲁⲣⲧыⲱⲕⲁ ⲉⳝⲁⲏⲁя ⲇⲟ ⲙⲟⲉⲅⲟ ⲭⲩⳡ ⲇⲟⳝⲉⲣⲉⲧⲥя я ⲉё ⲕⲁⲕ ⳝⲉⲣⲉⳅⲕⲩ ⲥⲡυⲗю ⲥⲃⲟυⲙ ⲇⲉⲧⲟⲣⲟⲇⲏыⲙ ⲟⲣⲅⲁⲏⲟⲙ)))0  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁⲃⲁύ ⲧⲃⲟё ⲟⳡⲕⲟ ⳅⲁⲕⲣⲩⲧυⲙ ⲏⲁ ⲭⲩύ? ⲕⲁⲕ ⲥⲁⲭⲁⲣⲏⲩю ⲃⲁⲧⲩ ⲏⲁ ⲡⲁⲗⲟⳡⲕⲩ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲭⲟⲇυⲗ ⲃ ⲯυⲣⲏⲩю ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ я ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⲧⲁⳃυⲧь ⲉⲅⲟ, ⲡⲣυⲱⲉⲗ ⲧⲃⲟύ ⲡⲁⲡⲁ, ⲡⲟⲧяⲏⲩⲗ ⲙⲟύ ⲭⲩύ ⲃⲙⲉⲥⲧⲉ ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃыⲧⲁⳃυⲗυ??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲉⳝⲉ ⲅⲟⲃⲟⲣю, ⲏⲉ ⲫⲟⲣⲥυ ⲧⲩⲧ ⲥⲃⲟύ ⲉⳝⲁⲗυⲏ, ⲁ ⲥⲡⲣяⳡ ⲉⲅⲟ ⲩ ⲙⲉⲏя ⲙⲉⲯⲇⲩ ⲏⲟⲅ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲯⲉ ⳅⲏⲁⲉⲱь, ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⲕⲁⲕ ⲕⲟⲱⲉⳡⲕⲟ ⲙⲟⲗⲟⲕⲟ ⳝⲩⲇⲉⲧ ⲥⲗυⳅыⲃⲁⲧь ⲙⲟⳡⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲁⲕⲁя ⳝⲉⲣⲩ υ ⲟⲡⲣⲕυⲇыⲃⲁю ⲧⲃⲟύ ⲭⲁⲃⲁⲗьⲏυⲕ ⲏⲁ ⲭⲩύ) υ ⲧы ⲱⲗюⲭⲁ, ⲏⲉ ⲥⲟⲡⲣⲟⲧυⲃⲗяⲉⲱьⲥя) ⲡⲟⲏяⲗ? ⲩⲧⲕⲟⲏⲟⲥ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲯⲉ ⲥⲉύⳡⲁⲥ ⲅⲣⲟⲙυⲧь ⲧⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⳝⲩⲇⲩ, ⲕⲁⲕ ⲇⲯⲉⲕυ ⳡⲁⲏ, ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲁⲏⲏⲁя, ⲥⲟⲥυ ⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲧⲁⲕⲟύ ⲙⲙⲉⲇⲗⲉⲏⲏыύ, ⳡⲧⲟ ⳝⲗяⲧь я ⲟⲡяⲧь ⲡⲟⲥⲥⲁⲧь ⲏⲁ ⲧⲃⲟю ⲙⲁⲧь ⲥⲙⲟⲅⲩ, ⲱⲗюⲭⲁ ⲧы ⲡⲟⲉⳝⲁⲏⲏⲁя, υⲇυ ⲏⲁ ⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟύ ⲃыⲥⲉⲣ ⲧⲁⲕⲟύ ⳝⲉⳅⲡⲟⲙⲟⳃⲏыύ, ⳡⲧⲟ ⲩ ⲙⲉⲏя ⲗυцⲟ ⲟⲧ ⲥⲙⲉⲭⲁ ⲗⲟⲡⲁⲉⲧⲥя) ⲁⲧⲃυⳡⲁю) ⲇⲁⲃⲁύ ⲧы ⲗⲩⳡⲱⲉ ⲡⲟύⲇёⲱь, υ ⲟⲡⲣⲕυⲏⲉⲱь ⲥⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⲏⲁ ⲡⲁⲇⲩⲱⲕⲩ, υ ⲟⲧⲃⲉⲣⲏёⲱьⲥя ⲉⳝⲁⲗⲟⲙ ⲕ ⲥⲧⲉⲏⲕⲉ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲧⲁⲕⲟⲉ ⳝⲣⲉⲃⲏⲟ, ⳡⲧⲟ я ⲧⲉⳝя ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲇⲣⲟⲃ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕυⲇⲁю, ⳡυⳝⲟ ⲧⲁⲙ ⲡⲉⳡь ⲧⲁⲕⲁя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲁ ⲧⲉⲡⲉⲣь ⲡⲟύⲇёⲙ ⲡⲟ ⲥⲧⲩⲡⲉⲏьⲕⲁⲙ)я ⲡⲟⲇⲏυⲙⲁюⲥь ⲭⲩⲉⲙ ⲡⲟ ⲧⲃⲟυⲙ ⲕⲟⲣⲉⲏⲏыⲙ ⳅⲩⳝⲁⲙ)я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲃыⳝυⲃⲁⲧь υⲭ, ⲡυⲇⲟⲣ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲃⲟⳅьⲙυ υ ⲉⳝⲁⲏυⲥь ⲟⳝ ⲕⲗⲁⲃⲩ) ⲁ ⲧⲟ я ⳝⲩⲇⲩ ⲧⲉⳝя ⲉⳝⲁь ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲡⲁⲗьцы ⲡⲟⲧⲉⲧь ⲏⲁⳡⲏⲩⲧ ⲟⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲡυⲱⲉⲱь ⲩⲥⲉⲣⲇⲏⲟ, ⲉⳝⲁⲏⲁⲱⲕⲁ ⲧⲩⲡⲟⲣыⲗⲁя  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲇⲁ я ⲧⲁⲕ ⲧⲉⳝя ⲩⲯⲉ ⲧⲩⲧ ⲡⲉⲣⲉⲉⳝⲁⲗ, ⳡⲧⲟ ⲧы ⳝⲗяⲧь ⲩύⲧυ ⲥⲡⲁⲧь ⲇⲟⲗⲯⲉⲏ ⳅⲩⳝⲁⲙυ ⲕ ⲥⲧⲉⲏⲕⲉ, ⲭⲩⲉⲥⲟⲥ ⲟⳝⲣыⲅⲁⲏⲏыύ   <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲧⲩⲧ ⲏυ ⲕⲁ ⲏⲉ ⲁⲥⲥⲟцυυⲣⲩⲉⲧⲥя ⲥ ⲥυⲇяⳃⲉⲙυ ⲡⲉⲣⲥⲏⲁⲙυ, υⳝⲟ ⲟⳝⲟⲥⲥⲁⲏцⲉⲙ ⲧⲩⲧ ⲏⲉ ⲙⲉⲥⲧⲟ, ⳝⲉⳅ ⲩⲃⲁⲯⲉⲏυя ⲕ ⲭⲩⲉⲥⲟⲥⲁⲙ υ ⲡⲣⲟⳡⲉύ ⲭⲩύⲏυ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥⲗыⲱь ⲥⲡυⲇⲟⳅⲏυⲕ ⲉⳝⲁⲏыύ ,ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕυⲣⳅⲟⲃыⲉ ⲥⲁⲡⲟⲅυ ⲡⲩⲥⲧυⲗⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲃыⲉⳝⲁⲏⲏⲁ ⲭⲩⲉⲙ ⲥⲃⲟⲉⲅⲟ ⲯⲉ ⲟⲧцⲁ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲥⲉύⳡⲁⲥ ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⳝⲉⳅ ⲥⲙⲥ υ ⲣⲉⲅυⲥⲧⲣⲁцυυ, ⲏⲟ ⲟⲇⲏⲟⲃⲣⲉⲙⲉⲏⲏⲟ ⲡⲗⲁⲧυⲱь ⲙⲏⲉ ⳅⲁ эⲧⲟ ⲇⲉⲏьⲅυ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲧⲁ ⲱⲕⲩⲣⲁ, ⲕⲟⲧⲟⲣⲁя ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⳡⲉⲣⲉⳅ ⲡⲣⲉⳅⲉⲣⲃⲁⲧυⲃ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲁⲕ ⲡⲟⲏяⲗ, ⳅⲁⲕⲟⲏⳡυⲗυⲥь ⲱⲁⳝⲗⲟⲏⳡυⲕυ?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲃыⲉⳝⲩ ⲧⲉⳝя, ⲕⲁⲕ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ?)0)0000)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲧⲟяⲧ ⲁⲫⲧⲟⲅⲣⲁⲫы ⲅⲣⲩⲃ ⲥⲧⲣυⲧ?ⲧⲁⲙ ⳡⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ υⲅⲣⲁⲗⲥя ⲥ ⲇⲣⲩⳅьяⲙυ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳝⲗяⲧь ⲟⲣⲩⲩⲩ!ⲇυⲕⲟ ⲟⲣⲩ!ⲧы ⲏⲁⲭⲩύ ⲥⲉⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲡыⲧⲁⲗⲥя ⲕⲁⲕ ⲧⲣⲁⲥⲫⲟⲣⲙⲉⲣ ⲧⲣⲁⲥⲫⲟⲣⲙυⲣⲟⲃⲁⲧьⲥя?ⲕⲣⲉⲧυⲏ ⲥⲩⲕⲁ)я ⲯⲉ ⲧⲃⲟⲟю ⲙⲁⲧь ⲉⳝⲁⲗ)ⲅⲣυⲫⲟⲏ ⲧы ⲥⲩⲕⲁ υⳅ ⲡⲟⲇ ⲭⲩя)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲡыⲧⲁⲗⲥь ⲡⲣыⲅⲏⲩⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲩⲗыⳝⲕⲟύ ⲏⲁ ⲗυцⲉ ⲡⲣυⳡⲉⲙ ⲥ ⲕⲣыⲗⲁ ⲥⲁⲙⲟⲗⲉⲧⲁ ?0  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ я ⲕⲟⲏⳡⲁⲗⲁ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲃ ⲣⲟⲧ, ⲁ ⲧы ⲥⲕⲃⲟⳅь ⲥⲏⲁ ⳡⲧⲟ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ ⲧⲃⲟύ ⲟⲧцⲉц ⲃыⲗυⳅыⲃⲁⲗ ⲙⲏⲉ ⲯⲟⲡⲩ ⲡⲟⲕⲁ я ⲥⲡⲁⲗⲁ) ⲁ ⲧы ⳡⲧⲟ ⲅⲟⲃⲟⲣυⲗⲁ ⲥⲕⲃⲟⳅь ⲥⲏⲁ?)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji>  ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲃⲟⲁⲙυ ⲧⲉⳝⲉ ⲕⲟⲏⳡυⲗυ ⲃ ⲅⲗⲁⳅ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲡⲟⲕⲁ ⲧы ⲙⲉⲏя υⲅⲏⲟⲣυⲱь ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁⲧяⲅυⲃⲁюⲧ ⲏⲁ ⲡυⳅⲇⲩⳝⲟⲙⲯυⲭυ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲫⲩ ⳝⲗяⲇь, ⲉⳝⲁⲧь ⲧы ⳝⲉⲇⲏⲁя, ⲏⲟⲥⲕⲁⲙυ ⲡυⲧⲁⲉⲱьⲥя, ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲙⲁⲧь ⳝⲗяⲇⲩⲉⲧ, υ ⲇⲉⲏьⲅυ ⲥ ⲧⲣⲁⲥⲥⲩ ⲧⲣⲁⲧυⲧ ⲏⲁ ⲃⲟⲇⲕⲩ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲥⲁⲇυⲗυ ⲏⲁ ⲟⲥⲧⲣⲟⲃ υ ⲇⲁⲗυ ⲉύ ⲧⲟⲗьⲕⲟ ⲙⲟⲉύ ⲭⲩύ υ ⲥⲕⲁⳅⲁⲗυ ⳡⲧⲟ ⳝы ⲟⲏⲁ ⲕⲁⲕ ⲙⲟⲯⲏⲟ ⳝⲟⲗьⲱⲉ ⲡⲣⲟⲇⲉⲣⲯⲁⲗⲁⲥь ⳝⲉⳅ ⲡυⳃυ υ ⲃыⲯυⲃⲁⲗⲁ ⲏⲩ ⲕⲁⲕ ⲃ ⲫυⲗьⲙⲉ "ⳅⲟύⲕⲁ ⲡⲉⲣⲉⲥⲙⲉⲱⲏυцⲁ")  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲗⲟⳝⲕⲟⲃⲩю ⲕⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲣⲟⲧυⲃⲟⲡⲟⲗⲟⲯⲏⲩю ⲥⲧⲟⲣⲟⲏⲩ ⲥⲙⲉⲥⲧυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲃⲥⲉ ⲡⲟⲏяⲗ,ⲧы ⲭⲟⳡⲉⲱь ⲥⲟⲥⲁⲧь,ⲧⲁⲕ ⳝы ⲥⲣⲁⳅⲩ υ ⲥⲕⲁⳅⲁⲗ)ⲏⲁⲭⲩύ ⲫⲟⲧⲕυ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲕⲁⳅыⲃⲁⲧь ⲧⲟ ⲏⲉ ⲡⲟύⲙⲩ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь υⲡⲟⲗьⳅⲩⲉⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲧяⲡⲕⲩ ⲏⲁ ⲟⲅⲟⲣⲟⲇⲉ ⲕⲟⲧⲟⲣⲟύ ⲟⲏⲁ ⲟⲕⲩⳡυⲃⲁⲉⲧ ⲕⲟⲣⲧⲟⲱⲕⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲥⲡⲟⲗьⳅⲩⲉⲧ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃⲥю ⲡⲗⲉⲱ ⲡⲣⲟⲉⲗⲁ ⲕⲁⲕ ⲙⲟⲗь ⲉⳝⲁⲏⲁя ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲥⲧⲟяⲏⲕⲩ υ ⲡⲟⲧⲟⲙ ⲡⲟⲣⲕⲟⲃⲁⲗ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ эⲗυⲧⲏⲟⲉ ⲙⲉⲥⲧⲟ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲟυⲗ ⲡυⲣⲁⲙυⲇⲩ ⲭυⲟⲡⲥⲁ ⲧⲁ ⲏⲉ ⲩⲥⲧⲟяⲗⲁ υ ⲟⳝⲣⲩⲱυⲗⲁⲥь ⲡⲣяⲙ ⲏⲁ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅ ⳅⲁ ⲡⲗⲟⲭⲟύ ⲕⲟⲏⲥⲧⲣⲩⲕцυυ υ ⲩⲕⲗⲁⲇⲕυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳝⲗяⲧь ⲇⲟⲱυⲣⲁⲕ ⲉⳝⲁⲏыύ) я ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⳅⲁ ⳃⲉⲕⲩ ⲏⲁⲥцⲁⲗ_) ⲟⲏⲁ ⲙⲟⲉύ ⲥⲥⲁⲏυⲏⲟύ ⲡⲣⲟⲡⲁⲗⲟⲥⲕⲁⲗⲁ ⲣⲟⲧυⲕ υ ⲡⲗюⲏⲩⲗⲁ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲁⲗⲟ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲙⲁⲧь ⲱυⲏⲧⲁⲯυⲣⲟⲃⲁⲗ ⲕⲁⲕ ⲃ ⲕⲣⲉⲙυⲏⲁⲗьⲏыⲭ ⲫυⲗьⲙⲁⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟυⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥυⲥьⲕⲩ ⲕⲟⲣⲟⲃⲉ,ⲭⲩⲉⲥⲟⲥ ⲧы ⲕⲟⲗⲭⲗⳅⲏыύ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)я ⲧⲃⲟύ ⲡⲉⲣⲇⲁⲕ ⲗⲁⲡⲁⲧⲟύ ⲕⲁⲡⲁⲗⲁ υ ⲗⲉⲏυⲏⲁ ⲉⳝⲁⲗⲁ ⲧⲃⲟυⲙ ⲃяⲗыⲙ ⲭⲩⲉⲙ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲉύⳡⲁⲥ ⲡⲟ ⲥⲃⲟⲉⲙⲩ ⲭⲩю ⲡⲩⳃⲩ ⲕⲁⲕ ⲡⲟ ⲟⲥυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⳡⲉⲙⲩ ⲥⲃⲟю ⲙⲁⲧь,ⲏⲁⳅыⲃⲁⲉⲱь ⲱⲗюⲭⲟύ?)ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ,ⲕⲁⲕ ⲧы ⲏⲁⳅⲃⲁⲗ ⲥⲃⲟю ⲉⳝⲁⲏⲩю ⲙⲁⲙⲁⲱⲕⲩ,ⲱⲗюⲭⲟύ,ⲟⲏⲁ ⲡⲉⲣⲉⲥⲧⲁⲗⲁ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲫⲟⲧⲁⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲡⲁⲣⲁцυύ ⲃ ⲕⲩⲣⲟⲣⲧⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲃёⲗ ⲕⲁⲕ ⲡⲟⲗⲟⲥⲙⲁⲥⲟⲃⲩю υⲅⲣⲩⲱⲕⲩ ?  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⳝⲉⲧⲟⲏυⲣⲟⲃⲁⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji>  ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲁⲏⲩⲥⲟⲙ ⲡⲣыⳃυ ⲃыⲇⲁⲃⲗυⲃⲁⲗⲁ ⲏⲁⲭⲩύ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲣⲡυⳡⲉύ ⲃыⲕⲗⲁⲇыⲃⲁⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲟⲅⲗⲩⲱυⲗ ⲕⲁⲕ ⲣыⳝⲩ ⲃ ⲃⲟⲇⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲡⲣυ ⲃыⲥⲟⲕυⲭ ⲩⲣⲟⲃⲏяⲭ ⲅⲣⲁⲃυⲧⲁцυυ ⲉⳝⲁⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲟⲗ ⳅⲁⳝⲣⲟⲱⲉⲏыⲉ ⲡⲣⲟэⲕⲧы ⲁⲣⲣⳑⲉ υ ⲡⲣⲟⲇⲁⲗ υⲭ ⳅⲁ ⲁⲕцυυ ⲃ ⲏⲁύⲕⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇьяⲃⲟⲗⲟ υⳅ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳡⲉⲣⲧυⲗⲁ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)ⲙⲏⲉ ⲧⲃⲁя ⲙⲁⲧь ⳡⲉⲥⲟⲧⲕⲩ яⳅыⲕⲟⲙ ⲃыⲃⲉⲗⲁ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲟυⲧ ⲟⲡⲟⲣⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲉⲗυⲗ ⲡⲗⲉⲙя юⲏⲅυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲕⲩⲡυⲣⲟⲃⲁⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲗⲟⲯυⲗ ⲙυⲏⲏⲟⲉ ⲡⲟⲗⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⲧⲕⲣыύ ⲡⲉⲣⲉⲗⲟⲙ ⲕⲟⲗⲉⲏⲕυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲣⲟⲣⲩⲯυⲗ ⲏⲉυⲏⲁⲣⲟⲇⲏыⲉ ⲗⲉⲧⲁⲧⲉⲗьⲏыⲉ ⲟⳝъⲉⲕⲧы ⲥ ⲃⲏⲉⳅυⲙⲏⲟύ цυⲃυⲗυⳅⲁцυυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲡⲟⲇⲕυⲏⲩⲗ ⲕⲁⲕ ⲇыⲙⲟⲃⲩю ⲅⲣⲁⲏⲁⲧⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲉⲭⲁⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲏⲟⲃⲩю ⲕⲃⲁⲣⲧυⲣⲩ ⳅⲁ ⲅⲟⲣⲟⲇⲟⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃыⲥⲧⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲧⲟⲣⲅⲟⲃⲩю ⲡⲗⲟⳃⲁⲇⲕⲩ ⲋⲧⲉⲁⲙ ⲕⲁⲕ ⲡⲟⲏⲟⲱⲉⲏⲩю υ ⲇⲟⲣⲟⲅⲩю ⲃⲉⳃь ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝ ⲁύⲥⳝⲉⲣⲅ ⲥⲧⲟⲗⲕⲏⲩⲗⲥя ⲕⲁⲕ ⲧυⲧⲁⲏυⲕ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲟⲡⲉⲣⲭⲏⲩⲗⲁⲥь ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲧⲁⲃⲗю ⳅⲁⲡяⲧыⲉ ⲏⲁ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲅⲇⲁ ⲃыⲥыⲗⲁю ⲧⲉⳝⲉ ⲧⲉⲗⲉⲅⲣⲁⲙⲙⲩ )  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲣяⲗ ⲇⲗυⲏⲩ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲣⲟυⲗ ⲥⲧυⲣⲁⲗьⲏⲩю ⲙⲁⲱυⲏⲕⲩ ⲇⲗя ⲭⲩⲉⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲩⲥⲧⲣⲟυⲗ ⲕⲁⲕ ⲕⲟⲙⲏⲁⲧⲩ ⲃ ⲕⲃⲁⲣⲧυⲣⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⳡⲗⲉⲏ ⲣⲃⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲉⳅ ⲡⲣⲉⲇⲩⲡⲣⲉⲯⲇⲉⲏυⲉ ⲏⲩ ⲕⲁⲕ ⲡⲣяⲙ ⲏⲁ ⲃⲟύⲏⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡⲟⲕⲁ ⲧы ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲕⲁⲧыⲃⲁⲗ ⳡⲉⲣⲉⳅ ⲣⲁⲃⲏυⲏы,ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲥⲧⲟⲗⲕⲏⲩⲗυⲥь ⲏⲉυⳅⲃⲉⲥⲧⲏыⲉ ⲭⲩυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲱь ⲡⲣυⲏυⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲇⲩⲱⲩ ⲕⲁⲕ ⲣⲟⲇⲏⲟⲅⲟ )  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲡⲟⲅⲣⲩⳅυⲗⲥя ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲗⲉⲧⲁⲉⲧ ⲡⲟ ⲭⲩя ⲕⲁⲕ ⲥⲁⲙⲟⲗⲉⲧ ⲡⲟ ⲙυⲣⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲁⲅⲉⲏⲧ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲡⲟⲙⲟⲅⲁⲉⲧ ⲉύ ⲣⲉⲫυⲗⲁⲣⲁⲙυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟⳝⲣⲁⲗυ ⲇⲣⲉⲃⲏυⲉ ⲁⲧцⲧⲉⲕυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲙⲟⲅⲩ ⲡⲟⲇⲃⲉⲥⲧυ ⲥⲃⲟύ ⲭⲩύ ⲕ ⲏⲟⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥ ⲡⲟⲙⲟⳃью ⲧⲃⲟⲉⲅⲟ ⲣⲧⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⲩⳡυⲗ ⲁⲏⲁⲗьⲏыⲉ ⲧⲟⲏⲏⲉⲗυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲧⲟⲣы ⲡⲟⲥⲧⲣⲟυⲗυ ⲇⲣⲉⲃⲏυⲉ υⲏⲕυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲇⲁю ⲧⲁⲕⲟ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲗⲟⳝ ⲧⲃⲟύ ⲙⲁⲧⲉⲣυ ⲱⲕⲃⲁⲣυⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲣⲁⲇυⲟ ⲡⲣυёⲙⲏυⲕ ⲃ ⲙⲁⲅⲏυⲧⲟⲫⲟⲏⲉ ?)??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲧⲟ ⲡⲁⳅⲇⳝυⳃⲉ ⲇⲗя ⲭⲩⲉⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲅⲣⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲥⲃⲟⲉ ⲭⲩю ⲧⲁⳃυⲗ ⲇⲟ ⲕⲗⲁⲇⳝυⳃⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲉⲗ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',


'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲗⲟⲯυⲗ ⲕⲁⲕ ⲅⲗⲁⲇυⲗьⲏⲟю ⲇⲟⲥⲕⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃⲟⲗⲱⲉⳝⲏⲁя ⲡⲁⲗⲟⳡьⲕⲁ ?_  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲗⲉⳡυⲗ ⲟⲧ ⲣⲁⲕⲁ ⲙⲟⳅⲅⲁ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲕⲁⲣⲧⲩ ⲙυⲣⲁ υ ⲡⲟⲧⲟⲙ ⲡⲟ ⲏⲉύ ⲟⲡⲣⲉⲇⲉⲗяⲗ ⲅⲇⲉ я ⲏⲁⲭⲟⲯⲩⲥь ⲕⲁⲕ ⲡⲟ ⳋⲣⲋ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⳝⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲟⲧ ⲙⲩⳡⲉⲏυя ⲃ ⲏυⲯⲏυⲭ ⲅⲉⲏυⲧⲁⲗυяⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲁⲃⲏⲟ ⲡⲟⲣⲃⲁⲏⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲗⲟⳃⲁⲉⲧ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃ ⲇⲃⲩⲭ ⲕⲟⲗⲉⲥⲏⲟύ ⳡⲉⲭⲟⲧⲕⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲏⲁ ⲧⲃⲟυⲭ ⲅⲩⳝⲁⲭ ⲭⲩⲉⲃ ⲡⲟⳝыⲃⲁⲗⲟ ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲃ ⲕυⲧⲁⲉ ⳝⲟⲗьⲱⲉ ⲏⲁⲣⲟⲇⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲗⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⳝυⲗ ⲃ ⲃυⲇⲉ ⲧⲣⲟⲫⲉя ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲥⲃⲟⲉύ ⲕⲗυⲧⲟⲣ ⲕυⲧⲁύⲥⲕⲩю ⲗⲁⲡⲱⲩ ⲏⲁⲕⲣⲩⳡυⲃⲁⲉⲧ ?)/  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲙⲉⲥⲧυⲗ ⲥⲃⲟύ ⲭⲩύ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲙⲉⲥⲧυⲗ ⲥⲃⲟύ ⲭⲩύ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲙⲉⲧⲕⲩ ⲟⲥⲧⲁⲃυⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧыы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⳅⲁⲧыⲗⲟⲕ ⲕυⲇⲁⲗ υ ⲟⲏⲁ ⲩⲡⲁⲗⲁ υ ⲡⲣⲟⲉⲭⲁⲃⲱυⲥь ⲣⲧⲟⲙ ⲡⲟ ⲕⲃⲁⲣⲧⲁⲗⲩ ⲟⲏⲁ ⲏⲁⲥⲟⳝυⲣⲁⲗⲁ ⲕⲩⳡⲩ ⲭⲩⲉⲃ )??  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲟⲇ ⲧⲁⲗυⳝⲥⲕυύ ⲟⳝⲥⲧⲣⲉⲗ ⲭⲩⲉⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⲅⲣⲁⲗυ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲙⲟⲣⲥⲕⲟύ ⳝⲟύ ⲕⲁⲕ ⲏⲁ ⲗυⲥⲧⲟⳡⲕⲁⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲧⲡⲣⲁⲃυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ эⲕⲡⲉⲇυцυю ⲁ ⲧⲟⳡⲏⲉⲉ ⲕⲁⲕ ⲃ ⲕυⲏⲟ "ⲧⲁύⲏы ⲡⲉⲣⲉⲃⲁⲗⲁ ⲇяⲧⲗⲟⲅⲟ" ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⳝⲣⲟⲥυⲗ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲃυⲇⲉ яⲕⲟⲣя ⲕⲟⲧⲟⲣыⲉ ⲥⲕυⲇыⲃⲁюⲧ ⲥⲩⲇⲏⲁ ⲕⲟⲅⲇⲁ ⲡⲣυⲱⲃⲁⲣⲧⲟⲃыⲃⲁюⲧⲥя ⲕ ⳝⲩⲭⲧⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,я ⳃⲁⲥ υⲅⲣⲁю ⲃ ⲇⲟⲧⲩ,υ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲇⲁю ⲣⲁⲙⲡⲁⲅυ,υ ⲉⳃⲉ,я ⲡⲣяⲙ ⲧⲟⳡⲏⲟ ⲭⲩⲕⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏыⲣⲏⲩⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⲥⲟ ⲥⲧⲣⲟⲭⲟⲃⲕⲟύ υ ⲥ ⲁⲕⲃⲁⲗⲁⲏⲅⲟⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> я ⲧⲃⲟю ⲙⲁⲧь,ⲡⲟ ⲇⲉⲱⲉⲃⲕⲉ ⳅⲁⳝυⲣⲁⲗ ⲥ ⲣыⲏⲕⲁ,ⲟⲏⲁ ⲥⲧⲟяⲗⲁ,5$ υⲗυ 6$,ⲏⲟⲣⲙ ⲯⲉ,ⳅⲏⲁⲉⲱь ⲡⲟⳡⲉⲙⲩ ⲧⲁⲕ ⲇⲉⲱⲉⲅⲟ?)ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ,ⲩ ⲏⲉⲉ ⳝыⲗ ⲏⲉⲇⲟⲉⳝ!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲭⲟⲭⲟⲗ ⲙⲟⲉⲅⲟ ⲕⲗυⲧⲟⲣⲁ?) я ⲏⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲕⲣυ ⲏⲁⲣⲟⲥⲧυⲧⲉⲗь ⲃⲁⲗⲟⲥ ⲃыⲗⲉⲗⲁ υ ⲧⲉⲡⲉⲣь ⲩ ⲏⲉⲉ ⲏⲁ ⲡυⳅⲇⲉ ⲕⲁⲥυⳡⲕυ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⳝⲩⲏⲕⲉⲣ ⲇⲗя ⲡⲣⲟⲯυⲃⲁⲏυⲉ ⲃⲟ ⲃⲣⲉⲙя ⲕⲁⲧⲁⲕⲗυⳅⲙⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⳅⲏⲁⲗ,ⳡⲧⲟ υⲙⲉⲏⲏⲟ я!)ⲉⲇυⲏⲥⲧⲃⲉⲏⲏыύ υ ⲏⲉⲡⲟⲃⲧⲟⲣυⲙыύ ⲥⲩⲧⲉⲏⲉⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲃυⲅⲁⲗ ⲕⲁⲕ ⲧяⲯⲉⲗыύ ⲡⲣⲉⲇⲙⲉⲧ ⲃ ⲃυⲇⲉ ⲇυⲃⲁⲏⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲕⲟⲅⲇⲁ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲏьⲕⲩ,ⲧⲟ ⲩ ⲏⲉⲉ ⲡυⳅⲇⲁ ⲏⲁⳡυⲏⲁⲉⲧ ⲟⲧⲕⲣыⲃⲁⲧьⲥя,ⲕⲁⲕ ⲃⲟⲣⲟⲧⲁ !)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲧⲣⲁⲯⲁⲗ ⲁⲧⲁⲕⲩ ⲧⲁⲗυⳝⲥⲕυⲭ ⲭⲩⲉⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ,ⲧⲟ ⲏⲁⳡυⲏⲁⲉⲧⲥя ⳅⲃⲉⳅⲇⲟⲡⲁⲇ!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥ ⲡⲟⲗя ⲥⲟⳝυⲣⲁⲗⲁ ⲭⲩυ ⲃ ⲃυⲇⲉ ⲅⲣυⳝⲟⲃ υ ⲥⲕⲗⲁⲇыⲃⲁⲗⲁ ⲥⲉⳝⲉ ⲃ ⲟⳡⲕⲟ ⲃ ⲃυⲇⲉ ⲕⲁⲣⳅυⲏы ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ я ⳃⲁⲥ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲯⲁⲣ ⲥⲇⲉⲗⲁю,ⲡⲟⲥⲗⲉ ⳡⲉⲅⲟ,ⲡⲣυⲉⲇⲩⲧ ⲙⲟυ ⲇⲣⲩⳅьяⲙυ,υ ⳝⲩⲇⲩⲧ ⲧⲩⲱυⲧь!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲟⲥυⲧⲥя ⳅⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲃⲟⲗⲕ ⳅⲁ ⳅⲁύцⲟⲙ υⳅ ⲙⲩⲗьⲧυⲕⲁ "ⲏⲩ ⲡⲟⲅⲟⲇυ" ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲥюⲇⲁ υⲇυ,ⲧⲃⲟю ⲙⲁⲧь ⳝⲩⲇⲉⲙ ⲃⲙⲉⲥⲧⲉ ⲉⳝⲁⲧь!)ⲅⲟⲏⲇⲟⲏы ⲃⳅяⲧь ⲏⲉ ⳅⲁⳝⲩⲇь!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲣⲟⲥⲥυя ⲡⲩⲥⲕⲁⲗⲁ ⲣⲁⲕⲉⲧы ⲧⲟ ⲇⲁⲏⲏыⲉ ⲕⲟⲟⲣⲇυⲏⲁⲧы υⳅⲙⲉⲏυⲗυⲥь υ ⲃⲗⲉⲧⲉⲗυ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲙⲟύ ⲭⲩύ,эⲧⲟ ⲕⲁⲕ ⲅυⲇⲣⲁⲃⲗυⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?)ⲟⲏⲁ ⲧⲁⲕ ⲩⲥⲕⲟⲣяⲉⲧⲥя,ⲕⲟⲅⲇⲁ я ⲉύ ⲃ ⲡυⳅⲇⲩ ⳅⲁⲕυⲇыⲃⲁю ⲥⲃⲟⲉⲅⲟ ⲇⲣⲩⲯⳝⲁⲏⲁ!)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳝⲣⲁⲥыⲃⲁⲉⲧⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲕⲁⲃⲕⲁⳅⲕⲁя ⲟⲃⳡⲁⲣⲕⲁ ⲥ ⲅⲟⲣⲏыⲭ ⲣⲁⲃⲏυⲏ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲇυⲭⲗⲟⲫⲟⲥ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗⲟⲭ ⲃыⲃⲟⲇυⲧь υⳅ ⲉё ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲟⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲃⲟⲇυⲗ ⲅⲁⳅⲟⲃⲩю ⲁⲧⲁⲕⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲧⲁ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ, ⲕⲟⲧⲟⲣⲁя ⲡυⲱⲉⲧ ⳡⲧⲟ ⲧⲟ ⲡⲉⲣⲉⲇ ⲉⳝⲗⲉύ ⲙⲟⲉⲅⲟ ⲭⲩя ⲥ ⲧⲃⲟυⲙ ⲣⲧⲟⲙ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⲡⲣⲁⲃυⲗ ⲧⲉⲭⲏυⳡⲉⲥⲕⲩю ⲏⲉⲡⲟⲗⲁⲇⲕⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲥⲡυⳅⲇυⲗ ⲇⲩⲭυ ⲏⲁⳝⲣыⳅⲅⲁⲗⲥя υⲙυ υ ⲡⲟⲱⲟⲗ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⳡⲧⲟ ⳝы ⲣⲟⲇⲏыⲙ ⳅⲁⲡⲁⲭⲟⲙ ⲡⲁⲭⲗⲟ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲉⲗяⲗ υⳅ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ υⳅ ⲗⲩⲕⲁ ⲁ ⲥⲧⲣⲉⲗы ⳝыⲗυ ⲃ ⲃυⲇⲉ ⲕⲟⲏⳡυⲏы ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲧⲁⲗ ⲕⲟⲙⲕυ ⲏⲁⲃⲟⳅⲁ ⲕⲁⲕ ⲏⲟⲃⲟⳅⲏыύ ⲯⲩⲕ υ ⲡⲟⲧⲟⲙ ⲥⲕυⲇыⲃⲁⲗ ⲃ ⲏⲩⲧⲣь ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲁⲧⲉⲣυ ⲩⲕⲗⲁⲇыⲃⲁⲗ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲡⲣⲡυⳡⲉύ ⲇⲗя ⲟⲡⲟⲣы ⲥⲃⲟⲉⲅⲟ ⲭⲩя ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲇⲭⲟⲇυⲧ ⲕ ⲟⳡⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳅⲟⲗⲟⲧⲟύ ⲕⲗюⳡυⲕ ⲕ ⲥⲩⲏⲇⲩⲕⲩ ⲥ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲟⲕⲁ ⲧы ⲧⲩⲧ ⲡυⲱⲉⲱь?) ⲥⲗыⲱυⲱь ⲕⲣυⲕυ? ⳡⲧⲟ я ⲧⲁⲙ ⲕⲣυⳡⲩ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲙⲉⲥⲧυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ υⳅⳝⲩⲱⲕⲩ ⲏⲁ ⲕⲩⲣьυⲭ ⲏⲟⲯⲕⲁⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⳝыⲃⲁⲃ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲏⲟⲣⲩⲯυⲗ ⳝⲟⲗⲉⲉ ⲧыⲥяⳡυ ⲩⲅⲣⲟⳅ ⲕⲁⲕ ⲁⲏⲧυ-ⲃυⲣⲩⲥ,ⲛⲟʀⲇ 32 ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲥⲧⲁⲃυⲗ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲇⲣⲁⲯⲉⲏυⲉ ⲕⲁⲕ ⲣⲉⲡⲉύⲏυⲕ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲟⲇυⲏⲟⲕυύ ⲥⲃυⲧυⲗьⲏυⲕ ⲃ ⲕⲣⲟⲙⲉⲱⲏⲟύ ⲧьⲙⲉ ⳝⲉⳅ ⲃⲉⲇⲟⲙⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲟⳝⲟⲅⲣⲉⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲧь эⲧⲟύ ⳅυⲙⲏⲉύ ⲥⲧⲩⲯⲟύ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲗυⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲗяⲇⲉⲏⲩю ⲅⲟⲣⲕⲩ ⲃ ⲡⲁⲣⲕⲉ υ ⲕⲁⲧⲁⲗⲥя ⲥ ⲏⲉё ⲏⲁ ⲥⲁⲏⲕⲁⲭ ⲗⲉⲇяⲏⲕⲁⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲇυⲁⲧⲟⲣ ⲟⲧ ⲃⲉⳅⲇυⲭⲟⲇⲁ ⳡⲧⲟⳝы ⲕⲧⲟ ⲧⲟ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ эⲧⲩ ⲭⲟⲗⲟⲇⲏⲩю ⳅυⲙⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ, ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲟⲃⲁⲙυ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃ ⲧⲃⲟⲉύ ⲕⲟⲙⲏⲁⲧⲉ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲉⲗⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ⲡⲟⲇ ⲃыⲥⲟⲕⲟύ ⲧⲉⲙⲡⲉⲣⲁⲧⲩⲣⲟύ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲟⲏ ⲉё ⲕⲁⲕ ⳝы υⳅⲏⲩⲧⲣυ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥъⳝυⲗ ⲕⲁⲕ ⲗⲟⲱⲁⲇь ⲃ ⲉⳝⲁⲏⲏⲩю ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲁⳅⲁⲉⲧ ⲥⲃⲟυ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲙⲟⲉύ ⲕⲟⲏⳡυⲏⲟύ ⲇⲩⲙⲁя ⳡⲧⲟ эⲧⲟ ⲡⲟⲙⲁⲇⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ ⲃ ⲏⲁⳡⲁⲗⲉ ⲡⲣⲉⲇⲗⲟⲯⲉⲏυя, ⲕⲧⲟ ⲉⳝⲁⲗ ⲧⲃⲟύ ⲣⲟⲧⲁⲏ, ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲁⲗυⲗⲁⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲧⲩⲁⲗⲉⲧⲏⲟύ ⲕⲣыⲱⲕυ ⳝυⲟ ⲧⲩⲁⲗⲉⲧⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡыⲧⲁⲗⲥя ⲥⲇⲉⲗⲁⲧь υⳅ ⲧⲃⲟⲉύ ⲥⲉⲙьυ ⳡⲉⲗⲟⲃⲉⳡⲉⲥⲕⲩю ⲙⲏⲟⲅⲟⲏⲟⲯⲕⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲯⲟⲅ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳝыⳡⲕⲟⲙ ⲥⲟⲗⲟⲫⲁⲏⲟⲃыύ ⲡⲁⲕⲉⲧυⲕ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲟ ⲗυⲏυυ ⲅⲟⲣυⳅⲟⲏⲧⲁ ⲣⲁⲥⲥⲧяⲏⲩ υ ⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲁⳝⲁⲣυⲧⲁⲙ ⲏⲉ ⲃⲗⲉⳅⲉⲧ ⲉё ⲃ ⲩⳅⲕыύ ⲁⲏⲁⲗьⲏыύ ⲡⲣⲟⲭⲟⲇ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲟⲧⲡⲣⲁⲃυⲗ ⲥⲟ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃⲟ ⲣⲧⲩ ⲃ ⲕⲣⲉⲥⲧⲟⲃыύ ⲡⲟⲭⲟⲇ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲡⲟⲗьⳅⲩⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲁⲭ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲟⲧⲡυⲱυⲥь, ⲕⲧⲟ ⲣⲁⲥⲭⲩяⲣυⲗ ⲉⳝⲗⲟ ⲧⲃⲟύ ⲙⲁⲧⲉⲣυ ⲃⳡⲉⲣⲁ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲏⲩ ⲡⲟ ⲇⲩⲡⲗⲩ ⲧⲁⲕⲏⲕⲁ ⲟⳝэⲉⲕⲧ-242 υ ⲕⲁⲕ ⲧы ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ υⳅ эⲧⲟⲅⲟ ⲃыύⲇⲉⲧ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⳡⲩⳡⲩⲏⲇⲣⲁ ⲁⲏⲁⲗьⲏⲁя?) я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗⲁ ⲕⲁⲗⲟⲏⲕⲟύ ⲃ ⲡⲉⲣⲇⲁⲕ υ ⲩ ⲏⲉⲉ ⳡⲉⲣⲉⳅ ⲡυⳃⲇⲩ ⲙⲩⳅⲃⲕⲁ υⲅⲣⲁⲉⲧ  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲱⲗюⲭⲁ ⲧы ⲡⲣⲟⳝυⲧⲁя) я ⲧⲉⳝⲉ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳃⲁⲥ ⲣⲟⲧ ⲡⲗⲣⲃⲩ υ ⲃⲟⲇⲣⲟ ⲃⲥⲧⲁⲃⲗю υ ⳝⲩⲇⲩ ⲧⲉⳝⲉ ⲥⲥⲁⲧь  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲩⲥυⲗⲟⲕ υ ⲡыⲧⲁⲗⲥя ⲣⲁⳅⲅⲟⲃⲁⲣυⲃⲁⲧь ⲃ ⲥⲕⲁύⲡⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇⲉⲙⲟⲏⲟⲃ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧυⲣⲁⲗ ⲗⲟⲧⲉⲣⲉύⲏыύ ⳝⲉⲗⲉⲧ υ ⲃыύⲅⲣⲁⲗ ⲟⲇυⲏ ⲙυⲗⲗυⲟⲏ ⲣⲩⳝⲗⲉύ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣыⳝⲁⳡυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁ ⲡⲣυⲙⲁⲏⲕⲁ ⳝыⲗⲁ υⳅ ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲕⲟⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⳅⲁ цⲉⲗыⲉ ⲥⲩⲧⲕυ я ⲏⲁⲗⲟⲃυⲗ ⲃⲉⲇⲣⲟ ⲣⲁⲧⲁⲏⲁ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ ⲃ ⲏⲁⳡⲁⲗⲉ ⲡⲣⲉⲇⲗⲟⲯⲉⲏυя, ⲕⲧⲟ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲟ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲥ ⲡⲉⳡⲉⲏⲉⲅⲁ ⲥⲧⲣⲉⲗяⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣяⲙ ⲩⲡⲟⲣ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲕⲉⲧⲏⲟⲉ ⲟⳝⲟⲣⲩⲇⲟⲃⲁⲏυя ⲡⲟⲇ ⲏⲁⳅⲃⲁⲏυⲉⲙ ⳅⲉⲏυⲧⲕυ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲯυⲣⲏⲩю ⲧⲟⳡⲕⲩ ⲕⲁⲕ ⲥⲧⲁⲃυⲗυ ⲡυⲣⲁⲧы ⲕⲣⲉⲥⲧ ⲏⲁ ⲕⲁⲣⲧⲉ υ ⲃыⲇⲃυⲅⲁⲗυⲥь ⳅⲁ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ⲕⲟⲧⲟⲣыⲉ я ⲩⲧⲁυⲗ ⲃ ⲉё ⲟⳡⲕⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⲧ ⲩⲇⲁⲣⲁ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲭⲩя ⲙⲟⲉⲅⲟ ⲟⲧцⲁ ⲥ ⲇⲃⲩⲭ ⲥⲧⲟⲣⲟⲏ ⲧⲃⲟю ⲙⲁⲧь ⲡⲣⲟⲥⲧⲟ ⲥⲡⲗюⳃυⲗⲟ ⲕⲁⲕ υ ⲉё ⲕⲗυⲧⲟⲣ ⲃ ⲧⲉⲥⲕⲁⲭ ⲕⲟⲧⲟⲣыύ ⲡⲟⲇⲕⲣⲩⳡυⲃⲁⲗ ⲧⲃⲟύ ⲟⲧⲉц )  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲉⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲉⲣⲉⲡⲏⲩю ⲕⲟⲣⲟⳝⲕⲩ ?)  <emoji document_id=5276174174161739848>😈</emoji>',  
'<emoji document_id=5276174174161739848>😈</emoji> ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲣⲩⲧυⲗⲁⲥь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲏⲁ ⲱⲉⲥⲧⲉ ?)  <emoji document_id=5276174174161739848>😈</emoji>'
        ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shablon1)))
            await sleep(time)


    async def lordnncmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный Модуль LordNN Прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль LordNN начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lordnn</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon2 = [ 
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ебанный оползень[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Матуху твою ебанную ебали со своими кентами[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Идол ебучий чекай как еблище те разорву[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Не выебывайся шавка ебанная[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ща натуре кабанчикам метнешься мне в хуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Моржовый хрен ебанный щас будешь туда сюда ползать собирать зубы свои[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Как Курокава Изана пенка пропишу тебе ебанный сын хуйни [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Как твой прадед будешь простатой страдать ебучий сын хуйни [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Маму тебе разорвал на клочья и тебя ебанного щенка точно также [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанный дегроид прям щас побежишь мне хуй лизать до блеска [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Жива нахуй мамашу чекай пока я ее не убил [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Кровякой обрызгаю свои кулаки об твое еблище [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ебанный далбаеб косолапый прям щас улетишь [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Гулял в лесу и спутал твое ебало с мухомором , по привычке пнул его нахуй [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Твои мозги монкея не способны понять о том что я ебал твою косоглазую мамашку [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Бабуин ты ебучий заблудишься в моем хуе когда я им же гортань твоей мамке порву ебанный ты бездарь [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Щас отправишься мне ноги целовать в надежде живым остаться [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ебанный далбаеб сын шлюхи куда вздумал лезть прям щас твою ебучую разломаю [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] В сиськах твоей мамки утону смотря на твое скукожное еблище [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] При морозе в минус сорок побежишь мне дрочить хуй параллельно ебля твоей матухи [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Варатником те черепушку разломаюнахуй ебанный сын хуйни [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Спидозная хуйня прям ща разорву те еблище [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>Прям ща сделаю огромную дыру в твоём брюхе как Тич Белоусу ][<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Я те ебанный его Люк Скайокер своим мечом ниже пояса разорву пасть твоей мамашке шлюхе [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Твоя ебанная мамашка ещё жирее биг мам лин лин будет, так и набивает се брюхо салом [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанный дармалей прям ща побежишь прыгать на моем хуе[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанная выскачка хуйни ебанной бегом от сюда не то зубы выбью сопляк ебучий[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сопля в носу зелёная чтобы со мной базарить максимум че можешь это помочь мне в ебле твоей мамашке [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Далбаебинский инсайдер прям ща натуре побежишь ебалом об асфалт бриться [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ща оторву те все части тела будешь как Хяккимару вербовать всю жизнь [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Как Шиба Тайджу разорву по палам ебанного далбаеба на твоём имене [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанный дохляк прям ща свое ебанное отскохшее молоко на губах побежишь разбрызгивать на моем хуе[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Как Геракл немейского льва порвал также и я порву брюхо твоей мамке и пущу ее на сало [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Случайным образом спутал твою мамашу с дубом и тк я лесоруб на реакции разрубил её нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Провокационная хуйня на не выбритой пизде твоей жирухи матушенки[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Натуре далбаебу ебанному глазу вырву будешь всю жизнь как Фуджитора гонять ебанный далбаеб [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Останешься одноруким при ещё одноглазым циклопом как Саске[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанная выскачка с наименоваем позора те приспичит вспомнить вкус детства , а именно моей спермы [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ты че ебанная остолбеневшая хуетень захотел чтобы я те еблище тута разломал [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сын хуйни ебанной чекай как мамашку твою ебашу[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Медляк ебучий как дед на пенсию пора те нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука сын хуйни ебанной прям щас же натуре те ебло разломаю тут нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Додек ебучий какого хуя твоя мать на моем хуе кувыркается[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Так и чешется рука тебя отпиздеть ебанного дауна[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука прыщавая жаба ебучая выскачка ща еблет те разверну на двести градусов[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Я же те натуре тут не оставлю и шанса не умри нахуй терпила ебанная[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Еблище скукожил быстра под давлением моего хуя колхозник ты ебанный[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ща же натуре те все хребты вытащу чтобы бездыханная туша твоего тела валялась [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Мать твою костылями бабки изобью  нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука псина ебанная ща побежишь со страху от сюда[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Еблан узкоглазый ща свои очечи расправишь нахуй под действием моего члена[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука терпила ебанная так и хочется тебе все кости оторвать [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебучий австралопитек с развитием неандертальцев те че еблище вправить[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука так бы и взял за твои нефарские волосы и об батарею нахуй еблищем[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Мамашку те ебанному сыну шлюхи разломаю[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Дятел ебанный ща мозги те вправлю ебанная амеба[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ща же натуре те еблище кровью расхлыстаем ебанный бишбербек [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Как Рокли ебанный те кости разломаю[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанный сын дохлятины я же те натуре еблище вправлю варанком [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Обезьян ебучий те че ебало прочистить тут[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука в бане те придушу ебанная выскачка[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Шваль ебучая ток тяпни я те ебло разломаю [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Норм было шпарить твою мамашку[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука тритон ебливый прям ща пизды те дам [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Когда аист принёс тебя твоим родителям - они долго смеялись и хотели сначала взять аиста.[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ебанная кабаниха твоей мамки прям ща пробежит за желудями в моем хуе [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Бля внатуре этот диградирующий астралапитек не понимает до того момента пока у его перед глазами не окажется моего члена[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука ща нижнию губу те оттяну нахуй [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ща от твоей спидозной мамашки заражусь[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Я же до твоей мамашки доберусь нахуй и черепушку ей сломаю ебанный даун[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука пизда тебе хуесос ебанный молись чтобы я тебе ебало не сломал [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Балбес ебанный сука я тебе маму ебал по самое влагалище[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Хэй залетай ко мне на хуй ебанный далбаеб[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Я же тебя не оставлю будешь на последних издохах молиться мне[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]На жигулях твоего ебанного пахана довозил до его магилки[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]В лесу тебя сука оставить чтобы подох там нахуй дубень ебанный[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Что мне мешает со всех ног тебе ебло сломать скажи мне пендикс ебанный[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Я же твоей мамке скормлю её же жирок сальца[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука прям ща мои сперматозоиды в твою мамашку залетят[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука пальцы себе сломай даун ебанный и не высирай чето больше[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ща кишечник твоей мамашке выломаю чтобы кровь украсила мой член[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>] Ебанной ногайкай по голой сраке тя отпизжу нахуй [<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Собирай живее свои селенки ебанные и готовься пизды отгребать[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Будешь прям ща мутагенить до той формы пока твое ебало не будет равно твоему     поносу[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Сука в труханы разбежался нахуй ебанный далбаеб[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Прям ща своим членярой тя отпизжу нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Мудила ебанная захотел чтобы я тебя ебалом окунул куда то в недро океана[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Ебанный сука дохляк залупы чумы свиней ебанных[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Пизда те нахуй если увижу тя в жизни кадык сломаю нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]Мамашку те ебал нахуй[<emoji document_id=5341557921597631101>😈</emoji>]",
        "[<emoji document_id=5341557921597631101>😈</emoji>]я же тебя терпилу каждый дерь хуесосить буду[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>] истребляю твою матуху своим хуем[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]куда ты снова сьебался с моего хуя[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]я твоей матери ща все кости переломаю урод ебаный[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]на пизде твоей матери танццют вальс школьники[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]тя уже все переебали олуха низкосортного[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]я тебе ща сынку шлюхи кабину снесу[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]мой хуй воняет пизже чем твои духи[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]мое слово закон запомни уебок[<emoji document_id=5341557921597631101>😈</emoji>]",
       "[<emoji document_id=5341557921597631101>😈</emoji>]я твою семейку хуем задушу ща[<emoji document_id=5341557921597631101>😈</emoji>]" ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shablon2)))
            await sleep(time)


    async def lorddmcmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный Модуль LordDM Прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль LordDM начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lorddm</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon3 = [
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же фрик ебаный соси〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же сын шлюхи сосешь〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же пидорас, отсосал〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же сосал мне, ну ка〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же гнидоподобный хе〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же хач обсосал член〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же сынокблдяи сосал〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же сосал всем нет??〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же наврал соси терь〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты же члены сосал хехе〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕сосал ты хуева ты шлюх〔<emoji document_id=5391112781812473534>💎</emoji> 〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕задавил твою мать шлюху〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать те ебал пойми〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать то твоя сосет〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать то твоя шлюха〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать те убил пойми〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать то твою имею)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать твоя сосалка)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать твоя сасала))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать твоя мертвая)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать твоя умерла))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать те епал тут))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕мать те набиваю)))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсоси сынок шлюхи〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсоси со словами:〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсоси член мой хы〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсоси хуяку мою))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсоси агрегат тут〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсосал ты мне тут〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕обсосал всем ты хы〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно ебу тя тут〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алзмано сосал ты )〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно отсосал ты〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмзано хуяку соси〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно убил тя =)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно поубивал=)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно сосеш мне)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно обсоси ты)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алмазно саси мне )〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕наври в пенис мне)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕наври матери своей〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕наври тут всем вдик〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ ТУТ МНЕ ПОНИМАЕШ?〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ ТЫ ТУТ АХАХАХАХАХ〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ ТЫ ТУТ ВСЕМ АХАХА〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ МНЕ ТУТ ПРИ ВСЕХ)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ МНЕ ДИК ПРИ ВСЕХ)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ МНЕ ЧЛЕН ПОЙМИ ХА〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ АЛМАЗНО ВСЕМ ХЕХА〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕СОСЕШ НОУНЕЙМ ТЫ ЕБАНЫЙ〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕отсосал ты ноуней ебучи〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕отсосал ты сынок шлюхи)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕отсосал ты бездарь хех)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕отсосал ты недоумок хех〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕отсосал ты хач ебучий )〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ебал тя без шанса на выживание мать твою убил пойми ты сынок шлюхи хе〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ебал тя ты не мог выбраться от моего хуя сосал ты немощь ебаная отоси〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕фричара ты алмазно сосал мне тута ну ка пососи мне сынок шлюхи ты))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ты слабомощь ебал тя вместе с азовцами отсоси ты слабак ебаный ты ))〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕пересосал ты сыночек слабой шлюхи мать те ебал тут оправдай себя )〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕это ты так своим ртом мне член дрочиш хех хвалю тя за твой отсос мне 〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕соси слабак ты ебучий〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕соси сынок шлюхи ты )〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕соси мне тут ебал тя)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕соси ты тут Азову хех〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕соси мать те ебу хехе〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕усоси сынок мертвой шлюхи〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕усоси бездарь ты ебаная)〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕усоси мне тут ну ка хехе〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕усоси слабак ебаный ух ебу〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕﻿твою мамашку ебал на тихих холмах а после этого похоронил ее под перевернутым кресто〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕с сатаной хуярим кагор и ебем твою мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕еблище твое ломом отхуярим так что ты из себя ничего кроме как куска мяса ничего представлять не будешь〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твоей беременной мамаше по коленям хуем ебанул и она шалава ебучая сразу сосать принялась〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕кончил в твою мать из нее вышла саламандра〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я наколол себе пентаграмму и твою голову на кол〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твою мамашку ебалом засунул в решетки полыхающего храма〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕расхуярил твою мамашку а ты так и остался пидорасом〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕оторву голову твоей мамаше и насажу на забор〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕﻿твою мамашку ебал на тихих холмах а после этого похоронил ее под перевернутым крестом〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕сброшу тебя с небоскреба на штык〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕с сатаной хуярим кагор и ебем твою мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я тебе пиздень порву сын шлюхи〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ноу нейм я твою мать ебал закрой нахуй свое еблище〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я тебе рылище переломаю сын шлюхи ты ебучий〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твоей беременной мамаше по коленям хуем ебанул и она шалава ебучая сразу сосать принялась〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ебучий пездарь ща кабанчикам на мой хуй ляжешь〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕матерь такому сыну шлюхи ебал〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алилирую своим членом те мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕сын хуйни ебанной ща на завод попиздуешь чаек мне варить и гайки мутить〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕в коляску ебанного молокососа с твоим именем засуну и выпну нахуй〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я те мамашку в лесу закопаю чтобы медведь гризли по ней прошел и раздавил ей все хрящи нахуй〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕﻿твою мамашку ебал на тихих холмах а после этого похоронил ее под перевернутым кресто〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕с сатаной хуярим кагор и ебем твою мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕еблище твое ломом отхуярим так что ты из себя ничего кроме как куска мяса ничего представлять не будешь〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твоей беременной мамаше по коленям хуем ебанул и она шалава ебучая сразу сосать принялась〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕кончил в твою мать из нее вышла саламандра〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я наколол себе пентаграмму и твою голову на кол〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твою мамашку ебалом засунул в решетки полыхающего храма〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕расхуярил твою мамашку а ты так и остался пидорасом〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕оторву голову твоей мамаше и насажу на забор〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕﻿твою мамашку ебал на тихих холмах а после этого похоронил ее под перевернутым крестом〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕сброшу тебя с небоскреба на штык〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕с сатаной хуярим кагор и ебем твою мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я тебе пиздень порву сын шлюхи〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ноу нейм я твою мать ебал закрой нахуй свое еблище〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я тебе рылище переломаю сын шлюхи ты ебучий〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕твоей беременной мамаше по коленям хуем ебанул и она шалава ебучая сразу сосать принялась〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ебучий пездарь ща кабанчикам на мой хуй ляжешь〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕матерь такому сыну шлюхи ебал〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕алилирую своим членом те мамашку〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕сын хуйни ебанной ща на завод попиздуешь чаек мне варить и гайки мутить〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕в коляску ебанного молокососа с твоим именем засуну и выпну нахуй〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕я те мамашку в лесу закопаю чтобы медведь гризли по ней прошел и раздавил ей все хрящи нахуй〔<emoji document_id=5391112781812473534>💎</emoji>〕"
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕ну все сын залупы наконец то пришел момент когда тебе довелось вспомнить твой любимый вкус детства в именно вкус спермы моей малофьи , готовься открывать свою ебанную пасть чтобы я вставил в нее свой хуй и ты резко метнулся мне в хуй дрочить на неё чтобы ты ебанный залупенкис прям ща не начал тут мне чета высирать я тебе мамашку вытрахаю до тех пор пока она не подохнет прям щас быстро начал мне сосать и лизать мой хуй пока я тебе твое ебанное еблище не разломал ебанному сыну шлюхи дабы ты не соснул мне мою залупу бегом нахуй побежал ебанное отродье сына шлюхи , ведь нахуя тебя твоя мамашка в поле похала чтобы вырастить такого ебанного сына шлюшки дабы он не отхуячил свои все прыщавые жабьи жабры которыми я удушу твою мамку ну что сын шлюхи я надеюсь ты приготовился к моральной ебле твоего ебанного блядского рода обезьян ебучих которые блять прям щас побегут мне дрочить на мой член и сосать его до такого состояния что твоя ебучая глотка всместк с ними прополки нахуй пропадет и я твою ебанную черепушку раздолбачу нахуй слушай сюда опарыш ебучий ты же ещё ебанный сопляк и молокосос у которого на губах ещё молоко не откисло ты на что тут рассчитываешь что я прям щас прощу тебе твой ебанный позорный высер в твою разминку ну как тебе тогда моя разминка сыоу шлюхи ебанный прям щас же нахуй быстро сметался ко мне и начал хуй мой лизать ебанный обпарщ я же тебе сука не оставлю в покое будешь на последних издохах своего состояния мне сосать ебанный клоун которому твк и чешутся руки сломать его тупое еблище ебанное чтобы сын шлюхи не втыкал ебанный оползень залупы что же мне с тобой сделать подумай ка сам нахуй своей ебанной извилиной что такому сыну шлюхе вроде тебя сделать кроме того как сломать его ебучии пальцы и засунуть их в одно ебанное место ведь такой же дятел ебучий по мимо тебя сука дебила ебанного〔<emoji document_id=5391112781812473534>💎</emoji>〕",
        "〔<emoji document_id=5391112781812473534>💎</emoji>〕тебя там Агентус ну дивиргент послал чтоле , вы понимаете что вы оба долбарукие дети ебучих шлюх куда вы тут вздумали лезть в троллинг я же все еблище вам расхуячу поганным сынам шлюх осмелившие сюда войти и чето пиздеть писав половину своей хуйни за счёт пробелов дабы они не соснули хуй решили дропнуть со страху пару некчемных ебанатов чтобы они отсосали мою залупу и вы ебучая пидоросня порешались закрыть ваше ебучие анальное отверстие в очко чтобы соснули и поняли кто тут тролляка чтобы я им еблище раскромсал , вы предстовляете что в тролли а я обычный чел писавший по фану текста , и серьезно думаете после этого что вы ебанные хохлы обосрыши чето тут решаете , я же еблище кромсал вам и вашим ебучим мамкам макакам чтобы они сидели и сосали мне до талого момента и вспоминали это всю свою оставшую ебучию жизнь повторяли как сладко это было чтобы я им ебальник об залупу таким соплякам ебучим поломал , осмелились они мне тут чето пиздануть архивные дети шлюх ебучих, ведь я своим огромным хуем продолбил черепушку ваших ебучих матеренок, бегите нахуй и пока я не начал раздавать всему стаду скопления ебучие одноразовые хуйни пиздюля пенки со скоростью света , да ещё и так что прежде чем все ваши еблеты прогнились от удара я успел там выбить зубы и своим огромным до небес хуем порвать гортань вашим матерям блять ну вы куски хуйни недоношенный жалкое сконудное существо с ебучими никами от которых меня только блюёт, чето засирают в этом чате и на что то надеется , мне же просто достаточно надристать вам и вашим ебучим матерям на ебало чтобы мой понос до блеска вылизывали они тебя, я же еблище кромсал вам и вашим ебучим мамкам макакам чтобы они сидели и сосали мне до талого момента и вспоминали это всю свою оставшую ебучию жизнь повторяли как сладко это было чтобы я им ебальник об залупу таким соплякам ебучим поломал〔<emoji document_id=5391112781812473534>💎</emoji>〕" ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shablon3)))
            await sleep(time)


    async def lordgercmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный Модуль LordGER Прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль LordGER начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lordger</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon4 = [
        "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ʍᴀʍᴀɯу ᴛʙᴏю ᴨᴏиʍᴇᴧ ᴨᴏниʍᴀᴇɯ чᴛᴏ ᴏнᴀ ужᴇ ɜᴀʙиᴄᴇʍᴀ ᴏᴛ ʍᴏᴇᴦᴏ хуя ᴋᴏᴛᴏᴩый ᴏʍыʙᴀᴇᴛ ᴇᴇ ᴏʍᴇжную ᴩᴏᴛᴏʙую ᴨᴏᴧᴏᴄᴛь[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", " [<emoji document_id=5409324508299405361>🇩🇪</emoji>]чиᴄᴛᴏ ᴛᴇᴩᴨиɯ ᴨᴏбᴏᴇʙ ʍᴏᴇᴦᴏ чᴧᴇнᴀ,ᴇщᴇ ᴏдин ᴛᴇᴩᴨᴇж и ᴨᴧᴏхᴏй ᴏᴛᴄᴏᴄ я ᴛᴇ ᴩыᴧᴏ ᴛʙᴏᴇ нᴀчну нᴀбиʙᴀᴛь ᴋᴀᴋ ɸуᴛбᴏᴧьный ʍячь[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴛʙᴏю ɯᴧюхᴀᴛᴇнь ʍᴀʍᴀɯу нᴀ чᴧᴇнᴇ ᴨᴩяʍᴏ ᴏᴛᴩᴀᴋциᴏн ᴨᴏᴋᴀɜᴀᴧ, ᴛы ᴨᴏйʍᴇɯ чᴛᴏ ᴛʙᴏᴇй ʍᴀʍᴇ ᴨᴩяʍᴏ нᴀдᴏ ʍᴏᴇᴦᴏ хуя нᴇ ᴏбхᴏдиᴛᴄя и дня чᴛᴏбы я ᴇᴇ нᴇ ᴇбᴀᴧ ᴨᴩᴏᴄᴛᴏ ᴛᴀᴋ хᴏчᴇᴛᴄя ᴨᴇᴩᴇхуяᴩиᴛь ᴛʙᴏю ʍᴀᴛуху ʙᴏ ʙᴄю ᴄʙᴏю ᴄиᴧу[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]чᴀᴄу нᴇ дᴀй нᴀ ᴄʙᴏᴇʍ ᴦᴏʙнᴏʍᴏдуᴧᴇ я жᴇ ᴛя ᴛуᴛ ᴨᴩᴀʙдᴏ убью ʍᴀʍᴀɯᴀ ᴛᴏ ᴛʙᴏя ᴛᴩяᴄᴧᴀᴄь ᴋᴏᴦдᴀ ʙидᴇᴧᴀ ʍᴏй хуй))[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]нᴀ хуя ᴛᴀᴋ ᴨᴩиᴄᴛᴏᴧьнᴏ ᴄʍᴏᴛᴩиɯ хᴏчᴇɯ ᴄᴏᴄᴀᴛь? ᴨᴩиᴄᴛуᴨᴀй))[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]бᴧяᴛь ну ᴛы ʙᴏᴛ ᴛᴀᴋ ᴄᴏᴄᴇɯ ʍнᴇ чᴛᴏ я чуʙᴄᴛую ᴄиᴧьный ᴏᴩᴦᴀɜʍ ʍнᴇ ϶ᴛᴏ ᴛᴀᴋ нᴩᴀʙиᴛᴄя я бы ᴛᴇ ᴇбᴧищᴇ бᴇ чᴧᴇнᴏʍ ᴩᴀɜᴏᴩʙᴀᴧ нᴏ ᴋᴛᴏ будᴇᴛ ʍᴇня ᴨᴩиʙᴏдиᴛь ʙ ᴏᴩᴦᴀɜʍ))[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ʍᴀʍᴀнь ᴛʙᴏю ᴨᴏиʍᴇᴧи ᴀ ᴛᴇбᴇ нᴇ ᴄᴋᴀɜᴀᴧи ю-х-у-у-у) ᴀ ʙᴇдь ᴛы ᴛᴏжᴇ хᴏᴛᴇᴧ ᴏᴛжᴀᴩиᴛь ᴄʙᴏю ʍᴀʍᴀɯу ɯᴧюху ну ᴛᴀᴋ ʙᴏᴛ ᴏнᴀ уʍᴇᴩɯᴀя ᴄидиᴛ ʙ ɯᴋᴏᴧьнᴏʍ ᴛуᴀᴧᴇᴛᴇ ᴨᴏᴧнᴏᴄᴛью я ᴦᴏʙнᴇ))ЩКЩЩКЩК[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>ᴏᴛʙёᴧ ᴛʙᴏю ᴄᴇʍᴇйᴋу ʙ ᴨᴏᴧиᴦᴏн и ᴨᴏᴄᴛᴀʙиᴧ ʍᴇᴄᴛᴏ ʍиɯᴇний ᴩᴀᴄᴄᴛᴩᴇᴧяᴧ их нᴀхуй<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄᴧᴀбᴀᴛᴀ ᴇбᴀнᴀя чᴧᴇняᴩу ᴛуᴛ ʍᴏю ᴛᴇᴩᴨи я ᴛᴇ ᴩиᴧ ᴛуᴛ ʍᴀᴛуху ᴛʙᴏю ᴇбᴀᴛь буду ᴨᴏ ʙᴄᴇʍ ᴨᴀᴩᴀʍᴇᴛᴩᴀʍ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄын ᴛы ᴨᴏдᴀʙᴧᴇннᴏй ɯᴧюхи ᴨᴧᴀчущᴇй ʍнᴇ ʙ ᴨᴇниᴄ ᴏᴛᴄᴀᴄыʙᴀй ᴨᴏ ᴦᴧубжᴇ ʍᴏй 20 ʍᴇᴛᴩᴏʙый ᴄᴛʙᴏᴧ<emoji document_id=5409324508299405361>🇩🇪</emoji> ", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ɯᴀᴧюхᴀ ᴛы чᴏ ᴛᴀʍ ʍнᴇ чᴧᴇн ʍᴏй ᴏбᴄᴀᴄыʙᴀᴇɯ я жᴇ ᴛᴇ ᴛуᴛ ʍуᴋи ᴨᴏᴋᴀɜыʙᴀю ᴛʙᴏᴇ ᴇбᴀᴧищᴇ ᴩᴀɜᴏᴩʙᴀᴧ ᴛуᴛᴀ ᴄᴏᴄи[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]чᴏ ᴨᴀᴨᴇ чᴏ ʍᴀʍᴇ чᴏ дᴇдᴋᴇ чᴏ бᴀбᴋᴇ чᴏ ᴄыну ɯᴧюху ᴦниᴧᴏɜубᴏʍу чᴏ ᴄёᴄᴛᴩᴇнᴋᴇ ᴨᴏдᴀʙᴧᴇннᴏй жиɜнью чᴏ бᴩᴀᴛиᴋу ᴋᴏᴛᴏᴩᴏᴦᴏ я ᴏᴛъᴇбᴀᴧ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>ᴛы ʙ ᴏᴛᴄᴏᴄᴇ ᴛуᴛ ᴏᴛᴄᴏᴄᴇᴩ хуᴇʙ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄᴨᴇᴩʍᴏᴨᴩиᴇʍниᴋ ᴩыᴧᴏ ужᴇ ᴄʙᴏᴇ ᴩᴀɜъᴇби ᴏб ʍᴏй чᴧᴇн ɜᴀɯью ᴛᴇ ᴩыᴧᴏ ᴄʙᴏиʍ чᴧᴇнᴏʍ ᴛуᴛᴀ ᴄᴏᴄᴇɯ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]дᴏчь ᴛᴩᴀнʙᴀя ᴨᴏᴋᴀ ᴛы ᴄᴨиɯь ᴛʙᴏя ʍᴀᴛь  нᴀ ᴛᴩᴀᴄᴄᴇ ɜᴀᴩᴀбᴀᴛыʙᴀᴇᴛ ʍинᴇᴛᴏʍ ᴛᴇбᴇ нᴀ хᴧᴇбуɯᴇᴋ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]бᴀᴛьᴋу ᴛʙᴏᴇʍу ʙ ᴦᴧᴀɜᴀ нᴀчᴀᴧ чᴧᴇн ᴄуʙᴀᴛь,ᴋᴀɜᴀᴧᴏᴄь чᴛᴏ я ᴇᴦᴏ ʍучᴀᴧ ʙ ᴧᴇᴄу[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]хуй ᴨᴩᴏᴄᴏᴄи ᴛуᴛ ʍнᴇ ну ᴋᴀ ᴨᴏᴋᴀжи ᴄʙᴏи ᴏᴛᴄᴏᴄы ᴋᴏᴛᴏᴩыᴇ ᴛы ᴨᴏᴋᴀɜыʙᴀᴇɯ яʙиᴄь ᴄюдᴀ и ᴄᴏᴄи ᴛуᴛ ʍᴏй чᴧᴇн[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]чᴧᴇн ᴛы ᴄᴧᴏʙиᴧ ʍᴏй ну ᴄᴨᴇᴩʍᴏй ᴛя ᴏбᴧиᴧ ᴨᴏᴧнᴏᴄᴛью)))))))))[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ʍᴀᴛь ᴛᴇ ᴛуᴛ ᴇбᴀᴧ ну ᴨᴏᴋᴀжи ᴄʙᴏи ᴩучᴋи ʙ ᴄᴨᴇᴩʍᴇ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴛʙᴏᴇᴦᴏ бᴀᴛьᴋᴀ ᴄʙинᴀ нᴀчᴀᴧ ʍучᴀᴛь ʙ ʍᴏᴇй ᴄᴨᴇᴩʍᴇ ᴀ ᴨᴏᴛᴏʍ ᴄʙяɜᴀᴧ ᴛʙᴏю ᴄᴇʍью и нᴀчᴀᴧ ʍучᴀᴛь ʙ ʍуᴋᴀх нᴀ ʍᴀᴛь нᴀᴄᴄᴀᴧ 0нᴀ уʍᴏᴧяᴧᴀ ʍᴇняᴏ ᴨᴏщᴀдᴇ нᴏ я ᴋᴩᴀʙᴏжᴀднᴏᴇ чʍᴏ нᴀчᴀᴧ ᴇᴇ ᴇбᴀᴛь ʙ ᴛᴏᴧᴄᴛᴏᴇ ᴏчᴋᴏ сᴇᴄᴛᴩᴇнᴋу иɜнᴏᴄиᴧᴏʙᴀᴧ и ʙыᴇбᴀᴧ ʙ ᴋᴩᴏʙᴀʙый ᴀнуᴄ,ᴏнᴀ ᴄᴛᴏнᴀᴧ ᴋᴀᴋ ᴇбᴀннᴀя ᴋᴏᴩᴏʙᴀ нᴀхуй а ᴛы ᴛᴇᴩᴨᴇᴧ ᴄʍᴏᴛᴩя нᴀ ϶ᴛᴏ ʙᴄᴇ жиʙᴏᴛнᴏᴇ ᴄᴧᴀбᴏхᴀᴩᴀᴋᴛᴇᴩнᴏᴇ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", " пес ебаный ты нахуй отсосал", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]Иɜᴩᴇɜᴀᴧ ᴛʙᴏᴇᴦᴏ ᴨᴀᴨу ᴄʙинᴏᴨᴏдᴏбнᴏᴦᴏ,ᴏн иᴄᴛᴇᴋᴀᴧ жиᴩᴏʍ ʙ ʍуᴋᴀх я бᴩᴀᴧ ᴋᴏᴧбу и ɜᴀᴧиʙᴀᴧ ᴛудᴀ жиᴩ и ᴄуʙᴀᴧ ᴛʙᴏᴇй ᴦниᴧᴏɜубᴏй ʍᴀʍᴀɯᴇ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ʙыᴩᴇɜᴀᴧ ᴛᴇбя ʙ Чᴇчнᴇ ʙʍᴇᴄᴛᴇ ᴄ дᴀнияᴩᴏʙыʍ)) ᴦᴏᴩдиᴄь нᴀʍи чᴛᴏ ᴛᴇбя нᴇ убиᴧи и ᴏᴄᴛᴀʙиᴧи ᴛᴇбя ᴄᴏᴄᴀᴛь нᴀɯ хуй[<emoji document_id=5409324508299405361>🇩🇪</emoji>]"," ",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄвииин ᴨᴏɜнᴀй ᴄиᴧу бёᴩдᴀ<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 " <emoji document_id=5409324508299405361>🇩🇪</emoji>засоси<emoji document_id=5409324508299405361>🇩🇪</emoji>", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]обсоси[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄᴀᴋᴀᴇɯ нᴀ ʍᴏᴇʍ чᴧᴇнᴇ ᴛуᴛᴀ я ᴛя ᴩиᴧ ᴛуᴛᴀ ʍᴏɜᴦи ᴏᴛбиᴧ чᴏᴧᴇ ᴏɸни ᴄʙᴏй ᴦᴏʙнᴏʍᴏдуᴧь ᴛухни ужᴇ ᴄᴧᴀбᴀᴋ ᴛы ʍᴀᴧᴏуʍный[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]я нᴀ ᴛʙᴏю ʍᴀʍу нᴀᴛᴩᴀʙиᴧ ᴄᴛᴀю бёᴩдᴏʙ ᴋᴏᴛᴏᴩыᴇ иᴄᴋᴧюʙᴧи ᴛʙᴏю ᴨᴏᴧудᴏхɯую ʍᴀʍᴀɯу,ᴨᴏᴄᴧᴇ ᴛᴏᴦᴏ ʍучᴇния я ʙъᴇбᴀᴧ ᴇй ᴄ нᴏᴦи и чуʙᴄᴛʙᴏʙᴀᴧ ᴄᴇбя ᴇбᴇйɯиʍ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴛы нᴀ ʍᴏᴇʍ чᴧᴇнᴇ ᴛᴀᴋ ʍᴏᴧчиɯ ᴨᴏᴩᴀ бы ᴛᴇбᴇ нᴀчᴀᴛь ᴄᴛᴏнᴀᴛь ᴛуᴛᴀ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴛы ᴨᴩᴏᴄᴀᴄыʙᴀᴇɯᴇᴇ ᴄᴧᴀбᴏуʍнᴏᴇ я ᴛᴇ ʙ ᴩыᴧᴏ хᴀᴩᴋᴀю иди ᴛᴀʍ ᴄхᴏди ɜᴀ чᴧᴇнᴏʍ дᴀнияᴩᴏʙᴀ ᴛуᴛᴀ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]чᴇᴩʙяᴋ чᴧᴇн ᴄᴏᴄи[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]сосал ты[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]убиᴧ ᴛяяяя))) нᴀᴄᴏᴄᴀᴧ ʍнᴇ ᴛуᴛᴀᴀᴀ ну ᴀᴛᴄᴀᴄи[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", " [<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄᴏᴄᴇɯ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]"
                                   "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴏᴛᴄᴏᴄᴀᴧ ᴨᴏ ᴨᴏᴧнᴏй ᴛы бᴇɜдᴀᴩь[<emoji document_id=5409324508299405361>🇩🇪</emoji>]", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ʙыᴩᴇɜᴀᴧ ᴋᴀᴛᴀнᴏй ᴛʙᴏю ᴄᴇʍью[<emoji document_id=5409324508299405361>🇩🇪</emoji>]",
                 "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]пересоси тут, выблядь[<emoji document_id=5409324508299405361>🇩🇪</emoji>]" " [<emoji document_id=5409324508299405361>🇩🇪</emoji>]ЩКЩКЩКЩ8ЩК ʍᴏй чᴧᴇн ᴏᴛᴄᴏᴄᴀᴧ ᴛы ɯᴀуᴩʍу ᴛуᴛᴀ ʙ ᴄыᴩнᴏʍ ɜᴀʙᴇᴩни ʍнᴇ ᴛуᴛᴀ]<emoji document_id=5409324508299405361>🇩🇪</emoji>] ", "[<emoji document_id=5409324508299405361>🇩🇪</emoji>]ᴄᴏᴄᴇɯ жᴇ ᴛᴀᴋ ᴏᴛчᴀйнᴏ ʍнᴇ[<emoji document_id=5409324508299405361>🇩🇪</emoji>]" ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shablon4)))
            await sleep(time)


    async def lorddinocmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный Модуль Lord Прекратил истреблять шалав<emoji document_id=6037464823959129840>🩸</emoji>!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль Lord начал ебенить шалав<emoji document_id=6037464823959129840>🩸</emoji>!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lorddino</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon5 = [
        "𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲁⲥⲉⲱ ⲙⲏⲉ ⲇⲩⲣⲁⲃⲗυⲃⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲃ ⲇⲃυⲯⲉⲏυυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲣⲁⲥⲗⲁⳝυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲟⳝυⲇⲉⲗ ⲧя ⲭⲩύⲉⲙ ⲱⲁⲗⲁⲃⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲣⲁⳅⲯⲁⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲅⲣⲉю ⲧя ⲭⲩⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⳝⲉⳅ ⲥⲟⲃⲉⲥⲧυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Эⲕⲁⲏⲟⲙⲏⲁ ⲉⲡⲩ ⲧя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲭⲩⲉⲙ ⲃ ⲧя ⲡⲱυⲕⲁⲗ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲡⲁⲣⲧυⲃⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲭⲩύⲉⲙ ⲧя ⲙⲁⲧⲏⲩⲗ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⳝⲗⲉⲥⲧяⳃⲉ ⲉⲡⲩ ⲧя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲡⲉⲣⲙⲩ ⲃ ⲧя υⳅⲉ ⳅⲁⲗυⲗ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲟⲧⳝⲉⲗυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲃⲁⳝⲟⲇⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⳅⲁⲧⲁυⲗ ⲃ ⲧⲉ ⲥⲃⲟύ ⲭⲩύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲗⲉⲧⲁя ⲇⲟⲭⲏⲉⲱ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲡⲣⲁⲃⲉⲣυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲕⲁⲏцⲉⲧⲣυⲣⲟⲃⲁⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲟⳝⲗⲉⲭⳡυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥⲁⲥⲁⲗⲁ ⲧы ⲙⲏⲉ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⳅⲩⳝы ⲧⲉ ⲭⲩύⲉⲙ ⲧⲣⲩ ⲧⲁⲕⲧⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲣⲁⲥⲡυⲗυⲗ ⲧя ⲭⲩⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲇⲁⲃⲗю ⲏⲁ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⳡⲟⲧ ⲃ ⲣⲟⲧ ⲧя ⲉⲡⲩ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲥ ⳡυⲥⲧⲟⲅⲟ ⲗυⲥⲧⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲣⲁⳅⲇⲣⲁⲯυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲟⲧⲕⲣыⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲭⲟⲯⲩ ⲃ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲡⲣυⳝυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲡⲟяⲃυⲗⲥя ⲃ ⲧⲉ ⲭⲩύⲉⲙ ⲥⲗⲉⲧⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟύ ⲇⲉⲇ ⲃ 45 ⲙⲏⲉ ⲭⲩύ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲥⲁⲥⲁⲗ ⲣυⲗυ ⲏⲉⲙⲟⳃь ⲟⲏ ⲉⳝⲁⲏыύ ⲇⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 υ ⳡё ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⲇⲟ ⲧⲁⲗⲟⲃⲁ υ ⲧы ⲏⲉ ⲥⲙⲟⲯⲉⲱь ⲙⲏⲉ ⲏⲉ ⳡⲉⲅⲟ ⲥⲕⲁⳅⲁⲧь ⲃⲉⲇь ⲥⲁⲙ ⲃ ⲧⲁύⲏⲉ ⲙⲏⲉ ⲥⲟⲥёⲱь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲇⲁⲃⲏⲟ ⲏⲁⳡⲁⲗⲁ ⲡⲣⲟяⲃⲗяⲧь ⲩⲃⲁⲯⲉⲏυя ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю υ ⳅⲇⲁⲣⲟⲃⲁⲉⲧьⲥя ⲥ ⲏυⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲧы ⳡё ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲅⲟ ⲥⲙⲟⲯⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣыⲡⲁⲉⲧьⲥя я ⲉύ ⳅⲁ эⲧⲟ ⲭⲩёⲙ ⲡⲟ ⲅⲟⲣⳝⲩ ⲏⲁⲃⲉⲣⲏⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃ ⲏⲁⲥⲗⲉⲇⲥⲧⲃⲟ ⳅⲁⲃⲉⳃⲁⲗⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲉⲥⲗυ ⳝⲩⲇⲉⲱь эⲧⲟ ⲟⲧⲣυцⲁⲧь я ⲉё ⲭⲩёⲙ υⳅ ⲅⲣⲟⳝⲁ ⲇⲟⲥⲧⲁⲏⲩ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲟⲇⲧⲃⲉⲣⲇυⲗⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⳡё ⲡⲣυⲥⲧⲩⲡυⲙ ⲣⲁⲥⳡⲉⲭⲗяⲧь ⲧⲃⲟю ⲙⲁⲧь υⲗυ ⲧы ⲇⲁⲯⲉ ⲡⲟⳝⲟυⲱьⲥя ⲣыⲡⲏⲩⲧьⲥя ⲏⲁ ⲙⲉⲏя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲣⲁⳅ ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲏⲟ ⲟⲏⲁ ⲥⲧⲣⲉⲙυⲗⲟⲥь ⲕ ⲃⲉⲣⲱυⲏⲉ ⲇⲩⲣⲁ ⲉⳝⲁⲏⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⲕⲩⲱⲕⲁ ⲏⲁⲭⲩύ ⲧы ⲡⲣяⳡⲉⲱьⲥя ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲭⲩя ⲙⲟⲉⲅⲟ ⲩ ⲏⲉё ⲏⲁ ⲡυⳅⲇⲉ ⲅⲉⲟⲗⲟⲕⲁⲧⲟⲣ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⲅⲗⲁ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ υ ⲃⲣёⲧ ⳡⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲃыⲗⲉⳅⲧυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲭⲟⳡⲩ ⲧⲉⳝя ⲟⲥⲕⲟⲣⳝυⲧь ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧⲥⲁⲥыⲃⲁⲗⲁ ⲙⲏⲉ ⲡⲟ 100 ⲣⲁⳅ ⲏⲁ ⲇⲏю ⲏⲟ ⲇⲗя ⲏⲉё эⲧⲟ ⲏⲉ ⲣⲉⲕⲟⲣⲇ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲧы ⲇⲟⲥυⲭⲡⲟⲣ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳝⲩⲇⲉⲧ ⲉⳝⲁⲧь ⲃⲁⲱⲩ ⲥⲉⲙύⲕⲩ ⳅⲁ ⳝⲉⲥⲡⲗⲁⲧⲏⲟ ⲥⲕⲟⲣⲟ ⲃⲁⲙ ⲡⲣυⲇёⲧьⲥя ⲡⲗⲁⲧυⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь я ⳝью ⲉύ ⲭⲩёⲙ ⲡⲟ ⲅⲩⳝⲉ ⲉύ ⲏⲣⲁⲃυⲧьⲥя ⲃⲉⲇь эⲧⲟ ⲡⲁⲥⲧⲁ ⲇⲁⲃⲏⲟ ⲃⲟ ⲃⲗⲁⲥⲧυ ⲙⲟⲉⲅⲟ ⲭⲩя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲇⲁⲯⲉ ⲏⲉ ⳅⲁⲙⲉⲧυⲱь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲯυⲧь ⲡⲉⲣⲉⲉⲇⲉⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲙⲩⳅⲉύ ⲡⲣⲉⲏⲉⲥⲧυ υ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ эⲧⲟ ⲃⲉⲗυⲕυύ ⲁⲣⲧⲉⲫⲁⲕⲧ ⳡё ⲟⲏⲁ ⲱⲁⲗⲟⲃⲁ ⲧⲟ ⲧⲁⲕⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲉⲥⲗυ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲏⲁⳡⲏёⲧ ⲃ ⲧⲉⲙⲡⲉ ⲥⲟⲥⲁⲧь я ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲉⳝⲁⲗⲩ ⲥⲉⳅⲯⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 υ ⳡё ⲧы ⳃⲁⲥ ⲧⲟⲯⲉ ⳝⲩⲇⲉⲱь ⲟⲧ ⲭⲩя ⲩⲃυⲗυⲃⲁⲧь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь υⲗυ ⲏⲁⳡⲏёⲱь ⲏⲁ ⲏⲟⲣⲙⲉ ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲙⲟⲅⲩ ⲡⲉⲣⲉⲇⲁⲧь ⲧⲉ ⳡⲩⲃⲥⲧⲃⲁ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲥⲡυⲇⲟⳅⲏⲁя ⲙⲁⲙⲁⲱⲁ ⲙⲏⲉ ⲥⲟⲥёⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⳅⲁ ⳃⲉⲕⲩ ⲡⲩⲥⲧυⲗⲁ υ ⲏⲉ ⲭⲟⳡⲉⲧ ⲃыⲥⲟⲃыⲃⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲕⲁⲕ ⲏⲁ ⲣⲁⳝⲟⲧⲩ υⲇёⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲟⲡяⲧь ⲙⲏⲉ ⲥⲟⲥёⲧ ⲙⲟⲯⲉⲧ ⲟⲏⲁ ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲙⲏⲉ ⳝⲉⳅⲗⲉⲙυⲧⲏⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲩⲡⲁⲗⲁ ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲉⲣⲇⲁⲕ ⲡⲉⲣⲉⲇ ⲥⲃⲟυⲙ ⳝⲁⲧⲉύ ⲏⲟ эⲧⲟⲧ ⲟⲥёⲗ ⲡⲟⳝⲟяⲗⲥя ⲉⲅⲟ ⲡⲟⲉⳝⲁⲧь ⲃⲉⲇь ⲟⲏ ⳅⲏⲁⲉⲧ ⳡⲧⲟ ⲙⲟя ⳅⲁⲗⲩⲡⲁ ⲟⲡяⲧь ⲡⲣⲟⳝьёⲧ ⲉⲅⲟ ⲅⲟⲣⳝ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲙⲩⲗьⲕⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲗⲁⲏⲇы ⲡⲩⲥⲧυⲗⲁ я ⲡⲣⲉⲇⲗⲁⲅⲁю ⲇⲁⲧь ⲉύ ⲙⲉⲇⲁⲗьⲕⲩ ⳅⲁ ⲅⲟⲇⲟⲃⲟύ ⲟⲧⲥⲟⲥ ⳝⲉⳅ ⲡⲉⲣⲉⲣыⲃⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⲏⲩ ⲥⲕⲁⲯυ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⲏⲉ ⲱⲁⳝⲟⲗⲇⲁ я ⲥⲃⲟυⲙ ⲭⲩёⲙ эⲧⲟ ⲟⲡⲣⲟⲃⲉⲣⲅⲏⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⳅⲃⲟⲣⲟⲱυⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲭⲩёⲙ υ ⲃыⲏⲉⲥ ⲟⲧ ⲧⲩⲇⲁ ⲃⲥё ⳡⲧⲟ ⲙⲟⲯⲏⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲧⲃⲟю ⲇⲩⲣⲏⲩю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲏⲁ ⲭⲩⲉ ⳅⲁ ⲧⲁⲕυⲉ ⲇⲃυⲯⲉⲏυя ⲡⲣⲟⲃⲉⲣⲏⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲃⲉⲣυⲱь ⲙⲏⲉ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲟύ ⲭⲩύ ⳝⲉⳅⲁⲥⲧⲟⲏⲟⲃⳡⲏⲟ ⲥⲟⲥёⲧ ⲧⲁⲕ ⲡⲣυⲭⲟⲇυ ⲟⲏⲁ ⲇⲁⲥⲧ ⲧⲉ ⲩⲣⲟⲕυ ⲟⲧⲥⲟⲥⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏяⲧь ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲁⲕⲁя ⲥⲗⲁⳝⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲟⲥυⲗυⲧь ⲏⲉ ⲙⲟⲯⲉⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲭⲩёⲙ ⲡⲉⲣⲉⲃⲉⲣⲏⲩ ⲭⲟⲧя эⲧⲟ ⲯⲁⲗⲕⲁя ⲏⲁⳡⲏёⲧ ⲟⲡяⲧь ⲃ ⲕⲟⲏⲃⲩⲗьⲥυяⲭ ⳝυⲧьⲥя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⲩⲯⲉ ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲁⲅⲏⲁⲗⲥя ⲁ ⲟⲏⲁ ⲏⲁⳡυⲏⲁⲉⲧ ⲕⲁⲕ ⲥⲃυⲏья ⲃυⳅⲯⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲉⲕ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲗⲁⲥь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⳅⲗⲁ ⲕⲟ ⲙⲏⲉ цⲉⲗⲟⲃⲁⲧьⲥя ⲏⲟ ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲗⲟⳝ ⲣⲁⲥⲕⲣⲟⲱυⲗ ⲡⲩⲥⲧь ⳅⲏⲁⲉⲧ ⲥⲃⲟё ⲙⲉⲥⲧⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲅυⲗьⲇυю ⲥⲟⳅⲇⲁⲗⲁ ⳡⲧⲟⳝы ⲙⲟύ ⲭⲩύ ⲃⲟⲥⲭⲃⲁⲗяⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲣυ ⲡⲟⲇⲣⲩⲅⲁⲭ ⲣⲁⲥⲭⲃⲁⲗυⲃⲁⲗⲁ υ ⲟⲏυ ⲧⲟⲯⲉ ⲣⲉⲱυⲗυ ⲙⲏⲉ ⲟⲧⲥⲟⲥⲁⲧь ⲏⲟ ⲗⲩⳡⲱⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ ⲏⲉ ⲕⲧⲟ ⲏⲉ ⲥⲟⲥёⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲉⲥⲗυ ⲧы ⲭⲟⳡⲉⲱь ⲙⲟύ ⲭⲩύ ⲧⲟⲅⲇⲁ ⲧⲉ ⲡⲣυⲇёⲧьⲥя ⲡⲟⲕⲟⲏⲕⲩⲣυⲣⲟⲃⲁⲧь ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲧы ⳃⲁⲥ ⲡⲟⲇⲟⲭⲏⲉⲱь ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⳡⲉⲙ ⲟⲡⲟⳅⲟⲣυⲱь ⲥⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲟⲧя ⲙⲟύ ⲭⲩύ υ ⲧⲁⲕ ⲉё ⲟⲡⲩⲥⲧυⲗ ⲉⳅ ⲉⳅ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧⲩⲱⲕⲁ ⲙⲟⲯⲉⲧ ⲟⲧⲣυцⲁⲧь ⳡⲧⲟ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲟ ⲩ ⲙⲉⲏя ⲉⲥⲧь ⲡⲣяⲙⲟⲉ ⲇⲟⲕⲁⳅⲁⲧⲉⲗьⲥⲧⲃⲟ ⲃⲉⲇь я ⳅⲁⲕⲁⳡⲁⲗ ⲉё υⳅⲏⲩⲧⲣυ ⲥⲡⲉⲣⲙⲟύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲃυⲏυⲗⲁⲥь ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ υ ⲉύ ⲡⲣυⲱⲗⲟⲥь υⳅⲃⲉⲏяⲧьⲥя ⲥⲃⲟⲉύ ⲯⲁⲗⲕⲟύ ⲅⲗⲟⲧⲕⲟύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⲧы ⲣυⲗυ ⲏⲉ ⲃⲇⲩⲡⲗяⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲁⲣⲉⲏⲇⲩ ⲃⳅяⲧь ⲏⲁ ⲇⲉⲏь υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲡⲣⲟⲇⲁⲗⲁ ⲡⲟⳡⲕⲩ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⳡё ⳝⲩⲇⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь υⲗυ ⲧы ⲟⲡяⲧь ⲣⲉⲱυⲗ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲥ ⲕⲉⲙ ⲏⲉ ⲇⲉⲗυⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲣⲁⳅⲙⲉⲏυⲣⲟⲃⲁⲗ ⲁ ⲟⲏⲁ ⲟⲧ ⳝⲗⲁⲅⲟⲇⲁⲣⲏⲟⲥⲧυ ⲟⳝ ⲙⲟύ ⲭⲩύ ⲥⲃⲟю ⲡυⳅⲇⲩ ⲥⲧёⲣⲗⲁ ⲏⲁ ⲉⳅ ⲉⳅ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲭⲩёⲙ ⲣⲁⲥⳡⲉⲗⲉⲏυⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲃ ⲧⲁⲕⲟⲙ ⲡⲟⲗⲟⲯⲉⲏυυ ⲥⲙⲟⲅⲗⲁ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⲏяⲧь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃⲥⲉⲅⲇⲁ ⳝⲩⲇⲉⲧ ⲇⲉⲣⲯⲁⲧь ⲏⲁⲇ ⲏⲉύ ⲃⲗⲁⲥⲧь ⲧⲁⲕ ⲧⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡⲗⲟⲙⳝυⲣⲟⲃⲁⲗ ⲉύ ⲇⲁⲯⲉ ⲕ ⲥⲧⲁⲙⲁⲧⲟⲗⲟⲅⲩ ⲭⲟⲇυⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲣⲁⳅⲣⲉⳅⲁⲗ ⲁ ⲟⲏⲁ ⲡⲟⳝⲉⲯⲁⲗⲁ ⲕ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ υ ⲡⲟⲕⲁⳅⲁⲗⲁ ⲟⲧⲣⲉⳅⲁⲏⲩю ⲡυⳅⲇⲩ ⲕⲁⲕ ⲡⲣυⲕⲟⲗ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲩⳡυⲗ ⲡυⲥⲁⲧь ⲏⲟ ⲟⲏⲁ ⲡⲗⲟⲭⲟ ⲃⲟⲥⲡⲣυⲏυⲙⲁⲉⲧ ⲩⳡⲉⲏυя υ ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь ⲏⲁ ⲁⲃⲧⲟⲙⲁⲧⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲥⲧⲣⲉⲗяⲗ ⲃ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲧⲣⲉⲗυⲗ υ ⲟⲏⲁ ⲧⲃⲁⲣь ⲟⲯυⲗⲁ υ ⲏⲁⳡⲁⲗⲁ ⲡⲟⲗⳅⲧυ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⲕⲟⲣⲧⲥⲙⲉⲏⲕⲁ ⲡⲟ ⲥⲟⲥⲁⲏυю ⲙⲟⲉⲅⲟ ⲭⲩя ⲉё ⲣⲉⲕⲟⲣⲇ ⲇⲁⲯⲉ ⲧⲃⲟύ ⳝⲁⲧя ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⳝυⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲏⲉ ⲏⲁⲇⲟ ⲟⲧⲣυцⲁⲧь ⲃⲉⲇь ⲧы ⲧⲟⲯⲉ ⳅⲁⲡⲟⲇⲟⳅⲣⲉⲏ ⲃ эⲧⲟⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⳅⲕⲩⲙⲁⲣυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲇⲁ ⲧⲁⲕⲟύ ⲥⲧⲉⲡⲉⲏυ ⳡⲧⲟ ⲟⲏⲁ ⲉⲗυ ⲉⲗυ ⲇⲟⳝⲣⲁⲗⲁⲥь ⲇⲟ ⲇⲟⲙⲁ ⲇⲁⲯⲉ ⲡⲟ ⲇⲟⲣⲟⲅⲉ ⲟⲏⲁ ⲩⲥⲡⲉⲗⲁ ⲕⲟⲙⲩ ⲧⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲯⲁⲗⲕⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲧы ⲙⲟⲯⲉⲱь я ⲯⲉ ⲥⲃⲟυⲙ ⲭⲩёⲙ ⲧⲃⲟυ ⲙыⲥⲗυ ⲧⲁⲕ ⲧⲟ ⲡⲉⲣⲉⲥⲧⲣⲟυⲗ ⲇⲩⲣⲉⲏь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲙⲟⲅⲩ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲃⲥⲉⲙ ⲟⳡⲉⲏь ⳡⲁⲥⲧⲟ ⲃⲉⲇь ⲃⲟⳅⲗⲉ ⲥⲃⲟⲉⲅⲟ ⲭⲩя я ⲃυⲯⲩ ⲉё ⲕⲁⲯⲇыύ ⲇⲉⲏь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯", 
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲡⲟ ⳝⲗⲁⲧⲩ ⲙⲏⲉ ⲥⲟⲥёⲧ ⲏⲟ ⲉύ ⲏⲉ ⲭⲃⲁⲧⲁⲉⲧ ⲥⲧυⲙⲩⲗⲁ ⲙⲟⲯⲉⲧ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲭⲩёⲙ ⲃⲉⲏы ⲃⲥⲕⲣыⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲣⲁⲙⲕⲩ ⲡⲟⲥⲧⲁⲃυⲗ υ ⲧⲉⲡⲉⲣь ⲃы ⲃⲥⲉύ ⲥⲉⲙьёύ υⲙ ⲗюⳝⲩⲉⲧⲉⲥь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲡⲟ ⲡⲣυⲕⲟⲗⲩ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⲗⲩⲏⲩ ⳅⲁⲕυⲏⲩⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲙ ⲃ ⲡⲉⲣⲇⲁⳡⲉⲗⲟ ⲕⲟⲙⲩ ⲧⲟ ⲇⲁⲗⲁ ⲟⲣⲏυ ⲥ эⲧⲟύ ⲱⲗюⲭυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲟⲅⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲩёⲙ ⲃⳅяⲧь ⲏⲁ ⲡⲣⲟⲅυⳝ ⲏⲟ ⲏⲉ ⲭⲟⳡⲩ ⲃⲉⲇь ⲟⲏⲁ ⲥⲧⲟυⲧ ⲣⲁⲕⲟⲙ υ ⲯⲇёⲧ ⲕⲟⲅⲇⲁ я ⲉё ⲃыⲉⳝⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⲥⲱυⲣυⲗ ⲅⲗⲁⲏⲇы ⲭⲩёⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲧⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⳝⲟⲗьⲱⲉ ⲙⲟⲯⲉⲧ ⲟⲡⲣⲁⳝⲁⲧыⲃⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲉ ⲥυⲗьⲏⲟ ⲃьⲉⳝⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲗⲩⲡⲟύ ⲏⲟ ⲟⲏⲁ ⲟⲧⲕⲗюⳡυⲗⲁⲥь ⳃⲁ ⲡⲣⲟⲥⲏёⲧьⲥя ⲡⲟ ⲏⲟⲃⲟύ ⲉё ⲡⲟⲉⳝⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲁ ⲏⲉⲅⲁⲧυⲃⲉ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю ⲃⲉⲇь ⲟⲏⲁ ⳅⲁⲉⳝⲁⲗⲁ ⲃыⲣыⲃⲁⲧьⲥя ⳅⲁ ⳡⲧⲟ я ⲉύ ⲩⲉⳝⲁⲗ ⲗⲉⳃⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⳅⲟⲣⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⳡⲁⲥⲧυ ⲧⲉⲣь ⲧы ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲙⲟύ ⲭⲩύ ⲇⲟ ⲩⳝⲟя ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⲥⲧⲣⲟⲅⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲭⲩёⲙ ⲃьⲉⳝⲁⲗ ⲉύ ⲡⲟ ⲅⲩⳝⲁⲙ ⲃⲉⲇь ⲕⲁⲕ ⲙы ⲡⲟⲙⲏυⲙ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲏьⲱⲉ ⲣⲁⳅυⳝⲃⲁⲗ ⲁ ⳃⲁⲥ ⲡⲣⲟⲥⲧⲟ ⲣⲁⲥёⲕ ⲟⲏⲁ ⲣⲁⲇⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲥⲧⲣⲟυⲗ ⲟⳝⲟⲣⲟⲏⲩ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲩⲇⲁⲣⲟⲙ ⲡⲟ ⲥⲧⲉⲏⲁⲙ эⲧⲟύ ⲟⳝⲟⲣⲟⲏы я ⲃⲥё ⳝⲗυⲯⲉ ⲕ ⲅⲗⲟⲧⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲃыⲣⲟⲥ ⲃ ⲅⲗⲁⳅⲁⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲟⲏⲁ ⲥⲟⲥёⲧ ⲉⲅⲟ ⲙⲉⲥⲧⲟ ⳅⲁⲃⲧⲣⲁⲕⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲣⲁⳅⲙⲩⲣⲟⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⳝⲣⲁⲧьⲥя υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⲡⲟ ⲯυⳅⲏⲉⲏⲟ ⲙⲏⲉ ⲇⲟⲗⲯⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲁ ⲡⲟⲧⲟⲙ ⲧы ⲉё ⲥⲙⲉⲏυⲱь ⲡⲣⲁⲃⲇⲁ ⲯⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲁⲕυⲏⲩⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲕⲁⳝυⲏⲩ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲣⲉⲱυⲗⲁ ⲟⲥυⲗυⲧь ⲙⲟύ ⲭⲩύ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲡⲩⲥⲧь ⲧⲁⲕⲁя ⲱⲁⲃⲕⲁ ⲇⲁⲯⲉ ⲏⲉ ⲡυⲧⲁⲉⲧ ⲏⲁⲇⲉⲯⲇы 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲁⲅⲟⲣⲏⲩⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲡⲣⲟⲥⲧⲟ ⲡⲟ ⲡⲣυⲏцυⲡⲩ ⲏⲟ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲕ ⲣⲉⲱυⲗⲁ ⲇⲁⲧь ⲙⲏⲉ ⲃ ⲡυⳅⲇⲩ ⲕⲁⲕ ⳝыⲗⲁ ⲱⲗюⲭⲟύ ⲧⲁⲕ υ ⲟⲥⲧⲁⲗⲁⲥь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙы ⲡⲟⲥⲡⲟⲣυⲗυ ⲥ ⲟⲧцⲟⲙ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲉ ⳝⲟⲗьⲱⲉ 200 ⲣⲁⳅ ⲃ ⲇⲉⲏь ⲏⲟ ⲟⲏ ⲡⲣⲟυⲅⲣⲁⲗ ⲃⲉⲇь ⲩⲃυⲇⲉⲗ ⲕⲁⲕ ⲟⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲉⲧ ⲙⲏⲉ ⲃ ⲯυⲃⲩю 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟю ⲙⲁⲧь ⲡⲉⲣⲃыύ ⲣⲁⳅ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲃыⲉⳝⲁⲗ ⲁ ⲟⲏⲁ ⲣⲁⲇⲟⲃⲁⲗⲁⲥь ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲏⲁⲕⲟⲣⲙυⲧь ⲧⲉⳝя ⲏⲟ ⲕⲁⲕ ⲡⲟⲉⲗ ⲥⲗυⳅⲉⲏь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲡⲟⲡⲣⲟⳝⲩύ ⲉⳃё ⲣⲁⳅ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲉⲣⲉⲃⲉⲇⲁⲗⲁ ⲥⲧⲟⲗьⲕⲟ ⲕⲗёⲃыⲭ ⲭⲩёⲃ я ⲧⲉⳝя ⲩⲉⳝⲩ ⲭⲩёⲙ ⲃⲉⲇь ⲟⲏⲁ ⲏⲁ ⲟⲧⲥⲟⲥⲉ ⲡⲣυⳅⲏⲁⲃⲁⲗⲥь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲁⲙыύ ⲗⲩⳡⲱυύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲡⲟ ⳅⲃⲉⲣⲥⲕυ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲟⲏⲁ ⲃ ⲱⲟⲕⲉ υ ⲇⲩⲙⲁⲉⲧ ⳡⲧⲟ эⲧⲟ ⲗюⳝⲟⲃь ⲏⲟ я ⲡыⲧⲁюⲥь ⲃⲕⲁⳡⲁⲧь ⲉё ⲥⲡⲉⲣⲙⲁⲕⲟⲙ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲉⲣⲉⲇⲟⳅⲏⲩⲗⲁⲥь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲩ υ ⳡё ⲙы ⲧⲉⲡⲉⲣь ⲥ ⲧⲃⲟυⲙ ⳝⲁⲧⲉύ ⲇⲣⲩⳅья ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲇⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲏⲁ ⲕⲗыⲕ ⲟⲏ ⲩⳅⲏⲁⲗ ⳡⲧⲟ ⲟⲏⲁ ⲯⲁⲗⲕⲁя ⲱⲗюⲭⲁ υ ⲥⲇⲁⲗ ⲉё ⲙⲏⲉ ⲃ ⲣⲁⳝⲥⲧⲃⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲥⲏⲁⳡⲁⲗⲁ ⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃыⳅыⲃⲁⲉⲧ ⳅⲁⲃυⲥυⲥⲙⲟⲥⲧ ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲣⲁⳅⲟⲙ ⲥⲟⲥⲁⲗⲁ ⲃⲥё ⳝⲟⲗьⲱⲉ υ ⳝⲟⲗьⲱⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲁ ⲣⲁⳅⲟⲅⲣⲉⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲉⳝⲁⲗ ⲁ ⲡⲟⲧⲟⲙ ⲧⲃⲟύ ⳝⲁⲧя ⲣⲉⲱυⲗ ⲙⲏⲉ ⲡⲟ ⲫⲁⲏⲩ ⲟⲧⲥⲟⲥⲁⲧь я ⲧⲉⲡⲉⲣь ⲇⲩⲙⲁю ⲩ ⲃⲁⲥ ⲃⲣⲟⲯⲇёⲏⲟⲉ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲁⲙⲩⲗьⲕⲁ ⲧⲃⲟя ⲣⲟⲇⲏⲉⲏьⲕⲁя ⳅⲁⲉⳝⲁⲏⲏⲁя ⲕⲩⲣυцⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟυ ⲣⲟⲇυⲧⲉⲗυ ⲟⲡⲩⳃⲉⲏы ⲃыⳝⲗяⲇⲕυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲩ ⲧⲉⳝя ⲙⲁⲧь ⲥⲣⲁⲏⲁя ⲱⲗюⲭⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 υⲥⲡυⳅⲇяⳡⲩ я ⲧⲃⲟю ⲙⲁⲙⲕⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳃⲁⲥ ⲃъⲉⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь υⲙⳝⲉцυⲗⲕⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲇⲁ ⲧⲃⲟя ⲙⲁⲧь ⲅⲟⲃⲏⲟⲉⲇⲕⲁ ⲧⲩⲡⲁⲣыⲗⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲩ ⲧⲉⳝя ⲃⲥя ⲥⲉⲙья ⲥⲟⲥⲧⲟυⲧ υⳅ ⲡυⲇⲟⲣⲟⲃ υ ⲗⲉⳅⳝυяⲏⲟⲕ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⳝⲗя ⲧⲩⲧ ⲥⲗυⲱⲕⲟⲙ ⲧⲟ ⲏⲉ ⲁⲭⲩⲉⲃⲁύ ⲩⲉⳝⲟⲕ ⲃⲁⲫⲉⲗьⲏыύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲥⲩⳡⲁⲣⲁ ⲧы ⲡⲣυⲡυⳅⲇⲏⲩⲧⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲥⲇⲟⲭⲏυ ⲅⲏυⲇⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳅⲩⳝы ⲧⲟ ⲃыⲡⲁⲗυ ⲉⲡⲧυ,ⲟⲧ υⳅⳝыⲧⲕⲁ ⲥⲡⲉⲣⲙы ⲃ ⲧⲃⲟⲉⲙ ⲃⲇⲟⲗь ⲡⲣⲟⲉⳝⲁⲏⲏⲟⲙ ⲏⲁ ⲭⲩύ ⲉⳝⲁⲗьⲏυⲕⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 Ⲕⲁⲕ ⲃы υ ⲡⲣⲟⲯυⲃⲉⲧⲉ... ⲡⲣⲁⲃⲇⲁ ⲏⲉ ⲇⲟⲗⲅⲟ..... ⲩⲣⲟⲇы υ ⲡυⲇⲟⲣы ⲇⲟⲗⲅⲟ ⲏⲉ ⲯυⲃⲩⲧ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲡⲟⲉⳝⲉⲏь ⲱⲁⲗяⲃυⲥⲧⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙы ⲥ ⲡⲣυяⲧⲉⲗяⲙυ ⲥⲉⲇⲏя ⲃⲙⲉⲥⲧⲟ ⲣⲁⳝⲟⲧы ⲇⲗя ⲡⲣυⲕⲟⲗⲁ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲟύ ⳝⲁⲗⲟⲃⲁⲗυⲥь ⲡⲟⲇ ⲩⳝⲟύⲏыύ ⲙⲩⳅⲟⲏ, ⲁ ⲧы ⲏⲁⲙ ⲡυⲃⲟ ⲡⲟⲇⲏⲟⲥυⲗ υ ⲟⳝⲟυ ⲡⲟⲡⲣⲁⲃⲗяⲗ ⲅыⲅы ⳝⲗя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲉⳝя ёⳝⲁⲏⲏыύ ⲧы ⲥⲧⲣⲁⲭⲟⳅⲁⲗⲩⲡυⳃⲉ ⲇⲁⲯⲉ ⲏⲉⲕⲟⲙⲩ ⳝⲩⲇⲉⲧ ⲃⲥⲡⲟⲙⲏυⲧь,ⲕⲟⲅⲇⲁ ⲧы ⲥⲇⲟⲭⲏυⲱь ⲩⲉⳝⲁⲕ!!! 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲧⲉⳝя ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟⲣⲩⳡⲏⲟ ⲩⲏυⳡⲧⲟⲯⲩ ⲡⲁⲇⲗⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⳡⲉⲣⲧ ⲇⲉⲃяⲧυⲥⲧⲃⲟⲣⳡⲁⲧыύ υⲇυ ⳅⲁⲗⲩⲡⲩ ⲟⳝⲗυⳅыⲃⲁύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲇⲁ я  ⲥⲙⲉⲣⲧь ⲧⲃⲟя ⲙⲗⲁⲇⲉⲏⳡⲉⲥⲕⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲥⲩⳡⲕⲁ ⲡⲟⲅⲁⲏⲁя ⳡⲧⲟ ⲯⲉ ⲧы ⲡⲁⲥⲧь ⲥⲃⲟю ⳅⲁⲭⲗⲟⲡⲏⲩⲗ ⲡⲉⲧⲩⲭ ⲡⲟⲧыⲕⲁⲏыύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲇⲣⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲕⲟⲧⲟⲣыύ ⳝыⲗ ⲏⲁⲡⲟⲗⲏⲉⲏ ⲙⲟⲉύ ⲙⲟⳡёύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳝⲉⲗⲁя ⲕⲟⲏⳡь ⲡⲣⲟⲏⳅυⲗⲁ ⲅⲗⲁⲏⲇы ⲧⲃⲟⲉύ ⲡⲣⲟⲥⲧυⲧⲩⲧⲟⳡⲏⲟύ ⲙⲁⲙы ⲁ ⲟⲧⲉц ⲏⲉ ⳅⲏⲁя ⳡⲧⲟ ⲇⲉⲗⲁⲧь ⲏⲁⳡⲁⲗ ⲗυⳅⲁⲧь ⲙⲟⲉύ ⳝⲁⳝⲕⲉ ⲥⲉⲇыⲉ ⲃⲟⲗⲟⲥы ⲏⲁ ⲙⲟⲣⳃυⲏυⲥⲧⲟⲙ ⲗⲟⳝⲕⲉ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲕⲁⲣⲗⲁⲏ ⲉⳝⲏⲩⲧыύ υⲇυ ⲥⲟⲥυ ⲭⲩύ ⲡⲁⲡυⲏ ⲙⲣⲁⳅь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲟⲭⲏⲁⲣыⲗⲁя ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲕⲟⲏⳡⲁⲗυ 3000 ⲭⲁⳡⲉύ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲁ, ⲭⲩύ ⲥ ⲧⲟⳝⲟύ , υⲧⲁⲕ ⲥⲉⲅⲟⲇⲏя ⲧы ⳝыⲗ ⲥⲗυⲱⲕⲟⲙ ⳝⲗυⳅⲕⲟ ⲡⲟⲇⲡⲩⳃⲉⲏ ⲕ ⲭⲩю 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⳅⲁⲃⲁⲗυ ⲥⲃⲟύ ⲡⲉⲣⲇⲁⲕ, υ ⲏⲉ ⲣⲁⲥⲥⲕⲣыⲃⲁύ ⲉⲅⲟ! 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲯ ⲕⲟⳡⲉⲅⲁⲣ ⲡⲟ ⲯυⳅⲏυ ⲥⲩⲕⲁ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟё ⲙⲉⲥⲧⲟ ⲏⲁ ⳝⲟⲗⲟⲧⲉ ⲧⲣⲁⲭⲁⲧь ⲗяⲅⲩⲱⲉⲕ. 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲙⲁⲧь ⲕⲣыⲥⲁ ⲡⲟⲗⲩⲇⲟⲭⲗⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲕⲁⲣⲟⳡⲉ ⲧⲃⲟя ⲙⲁⲧь ⲃⲁⲅυⲏⲁ ⲧⲩⲡⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲏⲁⲭⲩя ⲙⲏⲉ ⳡⲧⲟ ⲧⲟ ⲇⲟⲕⲁⳅыⲃⲁⲧь ⲧⲁⲕⲟⲙⲩ ⲟⲧⲣⲉⳝью ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲁⲙⲕⲁ ⲧⲃⲟя ⲅⲏυⲇⲁⲣⲁⲥⲕⲁ ⲟⲧⲭⲩяⲣυⲏⲁя 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟύ ⲟⲧⲉц ⲇⲣⲟⳡⲗυⲃыύ ⲭⲩⲉⲥⲟⲥⲏυⲕ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟⲉ ⲇⲉⲗⲟ ⲥⲟⲥⲁⲧь ⲁ ⲏⲉ ⲅⲁⲃⲕⲁⲧь ⲙⲩⲇⲗⲁⲏ. 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥυⲏⲟⲙⲡυⲕ ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲱⲕυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲟⲣⲟⲯυⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲙⲟύ ⲭⲩύ ⲧⲁⲏцⲉⲃⲁⲗ ⲧⲁⲏⲅⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣυⲭⲗⲟⲡⲏⲩⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲙⲩⲭⲩ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲧⲃⲟю ⲙⲁⲧь ⲅⲩⲥⲗяⲙυ ⲟⲧ ⲧⲁⲏⲕⲁ ⲉⳝⲁⲗ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲩ ⲧⲉⳝя ⲣⲟⲧ ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ,ⲃⲥⲁⲥыⲃⲁⲉⲧ ⲭⲩυ ⲥⲧⲣⲉⲙυⲧⲉⲗьⲏⲟ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⲡⲉⲣⲁю ⲏⲁ ⳝⲁⲗⲕⲟⲏⲉ ⳡⲧⲟⳝы ⲟⲏⲁ ⲏⲟⳡью, ⲏⲉ υⲅⲣⲁⲗⲁ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲧⲩⲱⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⳝⲁⲕⲁ. ⲙⲟύ ⲭⲩύ ⲇⲉⲗⲁⲉⲧ ⲁⲭⲩⲉⲏⲏыⲉ υ ⲇⲟⳝⲣыⲉ ⲇⲉⲗⲁ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲁⲃ ⲕⲟⲅⲇⲁ ⲉⳝⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?). я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲉⲏⲧⲩⲭⲩ ⲃыⲉⳝⲩ), ⲥⲗыⲱυⲱь ⲏⲁⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲏⲉⲏыύ ⲧы ⲣⲟⲧ ⳝⲗяⲇь ⲕⲟⲧⲟⲣыύ ⳝⲉⲣⲉⲧ ⲏⲁ ⲥⲉⳝя ⲥⲗυⲱⲕⲟⲙ ⲇⲟⲭⲩя. ⲥⲗыⲱυⲱь ⲟⲧьⲉⳝⲁⲏⲏыύ ⲉⲃⲣⲉύ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲧⲣⲁⲭⲁю υ ⲃыⲕυⲏⲩ ⲉё ⳅⲁⲥⲥⲁⲏыⲉ ⲧⲣⲩⲡ ⲥⲟⳝⲁⲕⲁⲙ ⳡⲧⲟ-ⳝы ⲟⲏυ ⲉё ⲥⲭⲁⲃⲁⲗυ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲃыⲥⲥⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ. ⲙⲟύ ⲭⲩύ ⲃыⳝⲉⲣⲉⲧ ⲡⲟⳅⲩ ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟ-ⳝы ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, υ ⲃыⳝⲉⲣⲉⲧ ⲁⲭⲩⲉⲏⲏю ⲡⲟⳅⲩ ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝыⲗⲁ ⲇⲟⲃⲟⲗьⲏⲟύ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя. ⲥⲗыⲱυⲱь ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя,я ⲕⲁⲕ-ⲧⲟ ⲣⲁⳅ ⲧⲣⲁⲭⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲩ ⲏⲉё ⲡⲟⲧⲟⲙ ⲏⲁⳡⲁⲗⲥя ⲥⲡⲁⳅⲙ ⲡυⳅⲇы, ⲧы ⲙⲟⲯⲉⲱь ⳅⲁⲗⲉⳡυⲧь ⲟⳡⲕⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⳝⲉⳅ ⲟⳝυⲇ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲇυⲕ. 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯",
"𖦯<emoji document_id=5393327477403688907>🦕</emoji>𖥜 ⲧⲃⲟя ⲥⲉⲙⲉύⲕⲁ ⲥⲟⳝⲥⲧⲃⲉⲏⲟⲥⲧь ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ! 𖥜<emoji document_id=5393327477403688907>🦕</emoji>𖦯"] 
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shablon5)))
            await sleep(time)
            
            


    async def lordcercmd(self, message):
        '''секунды в отписке сообщений + шаблон'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Легендарный Модуль Lord Прекратил истреблять шалав🩸!</b>")
            return
        await utils.answer(
        message,
        "<b>Модуль Lord начал ебенить шалав🩸!\n\n"
        "Чтобы закончить ебенить шалав пропиши эту хуйню <code>.lordcer</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shablon6 = [
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᴛᥱ᧘κᥲ ᥱδᥲнᥲя ᴛы ᥰ᧐чᥱⲙу ᥴ᧐ᥴᥱɯ ᴛᥲκ ᥰ᧘᧐᥊᧐? [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]᥊уя жⲙᥙ ρᥱщᥱ [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᴛᥱ᧘κᥲ ᥱδᥲнᥲя ᴛы ᥰ᧐чᥱⲙу ᥴ᧐ᥴᥱɯ ᴛᥲκ ᥰ᧘᧐᥊᧐? [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]почему ты мой хуй сосеш? [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴʙᥙн᧐ᥰᥲᥴ ᴛᥱρᥰᥙ ᥊уя ⲙᥱ᧐ᴦ᧐ ᴛы ᥴʙᥙнᴛуᤋ ᥱδᥲныᥔ ⲙᥲᴛь ᴛᥱ ᥰ᧐ᥱδыʙᥲю ᴛρᥱᥰᥙ ⲙᥱня[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ч᧐ ⲙнᥱ ᥊уᥔ ᥴ᧐ᥴᥲ᧘ ᴛ᧐ ᴛы ᥴʙᥙнья ᥱδᥲнᥲя ᥊уя ⲙ᧐ᥱᴦ᧐ ᥴᥲᥴᥱ ч᧐᧘ᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]", 
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴ᧐ᥴᥲ᧘ ᴛы ᥴ᧘ыɯ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ⲙᥲᴛь ᴛᥱ ᥰ᧐ᥱδыʙᥲю[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴ᧐ᥴᥲ᧘ ᴛы ⲙнᥱ ᥴ᧘ыɯ ᥴᥲᥴᥱ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ᴦ᧐ʙнᥲ ᥊уᥔ нᥲ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ⲙᥲᴛь ᴛᥱ ᥱδᥲ᧘ ᥴ᧘ыɯᥙɯ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ᴦ᧐ʙнᥲ ᥱδᥲн᧐ᴦ᧐[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ч᧐ ᥱδᥲнᥲᴛ ᥴ᧐ᥴᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я ᴛᥱ ⲙᥲᴛь ᥱδᥲ᧘ ᥊ᥱ᥊ ᥴᥲᥴᥱ ⲙнᥱ ᥴ᧘ыɯᥲ᧘ ᴛы[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ᴦ᧐ʙнᥲ ᥱδᥲн᧐ᴦ᧐ я ᴛᥱ ⲙᥲᴛь ᥰ᧐ᥱδᥲ᧘ ᥊ы᥊[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ᴦ᧐ʙн᧐δ᧘ядᥙ ᥊уя ᴛᥱρᥰᥙ ᥰ᧐ ʙᥴᥱⲙу ᴛʙ᧐ᥱⲙу ρы᧘᧐ ᧘ᥱᴛяᴛ κᥲᥰ᧘ᥙ ⲙ᧐ᥱᥔ ᥴᥰᥱρⲙы κᥲκ ᥲᥴᴛᥱρ᧐ᥙды ʙ ᴛʙ᧐ю ɯ᧘ю᥊уⲙᥲᴛь[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ч᧐ ᴛᥱρᥰᥙɯ ᴛ᧐ нᥲд ⲙ᧐ᥙⲙ ᥊уᥱⲙ ᴛы ᥴᥰρяᴛᥲ᧘ᥴя ᥊ᥱ᥊[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ч᧐ ⲙнᥱ ᥴ᧐ᥴ᧐ᥴᥱɯ ᴛы ну κᥲ ᥱδу ᴛя ᴛᥱρь[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ч᧐ ᴛᥱρᥰᥙɯ ⲙᥱня я ᴛᥱ ⲙᥲᴛь ᥰ᧐ᥱδыʙᥲю ᥙ ᴛы ᴛᥲκ жᥱ ᥴκᥲдᥱɯь чᴛ᧐ ᴛᥱδᥱ ᥰ᧐᥊уᥔ? ну ᥴʙᥙн᧐ᥰᥲᥴ ᴛы κ᧐нᥱчн᧐ ᥱδу ᴛя ᥴ ρᥲᥱᥴ᧐ⲙ ʙ ᥰᥱρᥱᥰ᧐ᥴ᧐ʙκу ᤋᥲκρчᥙʙᥲю ᴛᥱδя ᥴ ᥲдᥲⲙδᥲᥱʙыⲙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴ᧐ᥴᥲ᧘  ᴛы ⲙнᥱ 𐌺Щ𐌺Щ ᴛы ч᧐ ᴛᥱρᥰᥙɯ ᴛ᧐ нуκᥲ ᥊уя нᥲ ᥙ ᴛᥱρь ᥰ᧐ᥴᥲᥴыʙᥲᥔ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ᴦ᧐ʙн᧐ᥱдᥲ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥱδу ᴛя ᥰ᧐д ᥰᥱнᥴю [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥱδᥲ᧘ ᴛя ᴛы жᥱ ᥰ᧐нᥙⲙᥲᥱɯ чᴛ᧐ ᴛʙ᧐я ⲙᥲᴛь ⲙᥱρᴛʙᥲя ᥴᴛᥲρу᥊ᥲ ρᥲᤋдʙᥙᥲᴦ᧘ᥲ н᧐ᴦᥙ ᥲ ᴛᥲⲙ чᥱρʙᥙ δ᧘я[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴦдᥱ ᴛʙ᧐ᥔ ᴛᥲᥔᥰ ᥴын᧐κ δ᧘ядᥙ ᴛы ᥱδᥲн᧐ᥔ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]᥊уᥔ жуᥔ ⲙ᧐ᥔ ну κᥲ ᥴᥲᥴᥱɯ ᴛы[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥰᥱρᥱᥴ᧐ᥴᥲ᧘ ᴛы ᥱ᥊ᥱ᥊[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ʙ κ᧘᧐чья ᴛя ᥱδу ᥴ᧘ыɯᥲ᧘ ᴛы дᥲ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥰ᧐чᥱⲙу ᴛʙ᧐я ⲙᥲᴛь ⲙ᧐ᥔ ᥊уᥔ ᥴ᧐ᥴᥲ᧘ᥲ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴦ᧐ʙн᧐ᥱд ᴛы ᥱδᥲныᥔ ᥴᥰᥱρⲙу ρᥱщᥱ жуᥔ ᴛуᴛ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ⲙᥲᴛь ᴛᥱ ᥱδᥲ᧘ ᴛы ч᧐ ᴛу᥊нᥱɯ ужᥱ ч᧐᧘ᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴦᥙдρ᧐ɸᥱρᥲ᧘ ᴛы ᥱδᥲныᥔ ᥊уя ᴛᥱρᥰᥙɯ ᴛы ч᧐ ᴛᥲ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥴын᧐κ ⲙᥙнᥙⲙρᥙчн᧐ᥔ ᴦᥙдρ᧐ɸᥱцᥲ᧘ьн᧐ᥔ ɯᥲ᧘ᥲʙы ᴛы ч᧐ ᴛуᴛу удуⲙᥲ᧘ ⲙ᧐ᥱᴦ᧐ ᥊уя ч᧐᧘ᥙ ᴛᥱρᥰᥱᴛь ᴛуᴛ ⲙᥲᴛь ᴛᥱ ᥱδᥲ᧘ ᥴ᧘ыɯᥲ᧘ ᴛы ᥊уᥱᥴ᧐ᥴ ᥱδᥲныᥔ ᴛы[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы чᥱρн᧐δ᧘яднᥲя ᥴуκᥲᴦ᧘ᥲᤋᥲя ᥴʙᥙнᥴʙ᧐ʙᥲя ᥰ᧐ᥴᴛᥙ᧘κᥲ д᧘я ⲙ᧐ᥱᴦ᧐ ᥰ᧐᧘᧐ʙ᧐ᴦ᧐ ᧐ρᴦᥲнᥲ κ᧐ᴛ᧐ρыᥔ ᴛы цᥱᥰᴛᥙρуᥱɯ ʙκуᥴ ⲙ᧐ᥱᥔ δ᧐ᴦ᧐ᥰ᧐д᧐δн᧐ᥔ ᥴᥰᥱρⲙы ᥴʙ᧐ᥙⲙ ʙκуᥴ᧐ыⲙ яᤋыκ᧐ⲙ ᴛρᥱᥰᥙ᧘ᥙρуᥱɯь ⲙ᧐ᥱᴦ᧐ ᥊уя[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴуκᥲ δ᧘яднᥲя ʙᥴᥱⲙᥙ ʙыδᥱнᥲя ᴦᥙɸᥙдρᥙ᧘ᥙнᥲя ɯᥲ᧘ᥲʙᥲ яʙᥙ᧘ᥲᥴь дᥲδы ᥰ᧐᧘учᥙᴛь ᥱщᥱ ᧐дн᧐ᴦ᧐ ᥴᥱκᥴуᥲ᧘ьн᧐ᴦ᧐ ᧐ρᴦᥲᤋⲙᥲ ᧐ᴛ ⲙ᧐ᥱᴦ᧐ ᥊уя [<emoji document_id=5388994705805549866>☠️</emoji>]", 
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ⲙᥲᴛь ᴛᥱ ᥱδᥲ᧘ ᥴ᧘ыɯ ᴛы ᥊уᥱᥴ᧐ᥴ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛы ᥰ᧐ᥴын᧐κ ⲙρᥲᤋⲙ᧐δ᧘ядᥙ ᥴᥲᥴᥲ᧘ ᴛᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]᥊уя ᴛᥱρᥰᥙɯ ᴛ᧐ ᴛы ᤋᥲчᥱⲙ ᥲ нуκᥲ ᥴᥲᥴᥱ ч᧐᧘ᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥰᥱρᥱᥴᥲᥴᥙ ⲙнᥱ ᴛы[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᥴын᧐κ ᴛы ᴦ᧐ʙнᥲδ᧘ядᥙны ᴛы ч᧐ ᥴᥲᥴᥱɯ ᴛ᧐ ᴛы нуκᥲ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛi ᥴɦ᧐ s᧐sᥲᥣ ᴛ᧐&[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я ᴛя ᥱδᥲ᧘ ᥙы ᥴ᧘ыɯ ᥊уᥱᥴ᧐ᥴ ᴛы ᥱδᥲныᥔ ᥴ᧐ᥴᥙ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛʙ᧐я ⲙᥲᴛь нᥲчᥲ᧘ᥲ δᥱᥴᥰ᧐κ᧐ᥙᴛᥴя ᥰ᧐ᴛ᧐ⲙу чᴛ᧐ я ᥲδᥴ᧐᧘юᴛ ᥙ ᧐нᥲ ᤋнᥲ᧘ᥲ чᴛ᧐ я ʙᥙжу ʙᥴᥱ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛʙᥲя ⲙᥲᴛь ᥴ᧐ᥴᥲ᧘ᥲ ⲙᥲᥱᴦ᧐ ч᧘ᥱнᥲ дᥲ ᧐нᥲ ᧘юᥰᥙᴛ ⲙ᧐ᥔ ᥊уᥔ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ᴛʙ᧐я ⲙᥲᴛь ᤋᥲ᥊᧐дᥙᴛ нᥲ ⲙ᧐ᥔ ᥊уᥔ[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]δ᧐᧘ᥱᥱ 10 ᧘ᥱᴛ ᴛʙ᧐я ⲙᥲᴛь удᥙʙ᧘яᥱᴛᥴя ⲙ᧐ᥱⲙу ᥊ую ᥊ᥱ᥊[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты хуль сьебался с моего хуя сыняра шалавы [<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я твою семейку в покое не оставлю буду их каждый день ебашировать пока они не совершат суицид[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ебу твою мать в потоке как Аомине[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я тут чисто возьму твоей матери ебалище все окуну в сортир[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты с кем соревноваться решил то со своими мизерными объемами таким сынкам шлюх на подобии тебя здесь нужно ебалище все швырять 24 часа в сутки[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я твоей матери внатуре тут все сосалище оболью кислотой и начну трахать ее черепную коробку до атрофирования мозга[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]шнырь ебучий попробуй тут только отсосать я тебя зяблика ебанного буду тут хуярить до самой последней минуты нахуй насмешище ебанное[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ну же сынок блядины ты недоразвитой ты будешь хоть как-то противиться мне или мне продолжить твой еблет жирющий раздавливать как муравья ебанного[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ХВХВХВХ внатуре таких сынков шлюхи как ты нужно здесь перевоспитывать поочередно я тебе повторяю что ты тут уймища хуев в свою разорванную пасть возьмешь если попытаешься рыпнуться на меня но ты уже рыпнулся и опять получаешь по своему рыльнику отъебанному смачных лещин сынок бляди ты задроченной пиздец я твою маманю ебал иди отсюда[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]как Итачи тебя сынка шлюхи своим аматерасу испепелил[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я твою мать все равно отьебашу своей залупой оставив от неё лишь воспоминания[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты никчёмный сынуля бляди давай покажи мне свою мизерную фантазию которую я заплюю как твой труп свиной тебе никто не поможет допри уже это сынуля шлюхи самой ебанутой[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я таких как ты сынков шлюхи без конечностей оставлю здесь терпилоид ты ебучий вообще там берега походу попутал я тебя развалю в парашу здесь ты забудешь свою мать родную шлюху давай член мой наяривай мне похуй на тебя абсолютно ты чисто мясо очередное которое я потыкаю своей залупой и оно расплющится[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты терпила ебучая но ты повышаешь этот уровень танцуя на моей залупе а я тем временем выбиваю твои зубы своей зубодробительной членярой сын скосоеблой хуесосущей долбаебки один хуй у тебя мать шалава упертая будет мою членину сосать от рассвета до заката[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]а ну закрой ебало сученыш ебанный я тебя здесь унижу как шлюху ты будешь там искать оправдания, как бы быстрее смыться от моей огромной залупы и моих ударов слышишь меня рекс черножопый я тебе сынку шлюхи все ебало сломаю нахуй и начну твоими костями твою мать избивать[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]телочка ебанная попытайся тут что либо мне противопоставить один хуй я буду харчки в твое ебалище грязное метать очком твоей мамаши шлюхи нечисть ебанная ты будешь быстрее печатать или что я тебе мать ебал в любом случае тут ты сдохнешь раньше чем за полусуток ослоебина слабейшая я твои лапти буду хуярить об морду твоей матери ебанная ничтожная куртизанка[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ебанное попуасище что пытается тягаться со мной когда я ломаю ему все рёбрышки закидывая их в бездну где снизу навстречу ждут собаки слышишь меня ебучий зяблик я твоей мамаше сейчас все ее шлюшьи рога тут поотрываю ебанная бездарность ты с кем тягаться то вздумала на фантазии один хуй я твой трупешник мусорный буду хуярить об бетонные блоки до такой степени что у тебя весь трупешник будет разлагаться на пиздаке твоей матери ебанной шлюхи[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]тебе чет на ебло насрал, клещ ты ебаный[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]тебе чет на ебло насрал, клещ ты ебаный[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]твоя мать на моем хую танцевала дичь[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты сосешь , а мой хуй не ценит этого[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я свой хуй затачиваю об клитор твоей матери как копьё в средневековье ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я на очке твоей матери своим хуем таблицу менделеева нарисовал ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты же моему хую свою мамашу шкуру подарил за чупачупс, ущербный хуесос ты сука[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]успокойся чёрный сын шлюхи один хуй я тебе сосальню тут вытрахаю[<emoji document_id=5388994705805549866>☠️</emoji>]",  
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я на очке твоей матери нарисовал карту мира и потом по ней определял где я нахожусь как по gps ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что мой хуй сбил твою мать когда та пыталась отобрать у него сладость ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что твоя мамаша на мой хуй переезжает как на новую квартиру?[<emoji document_id=5388994705805549866>☠️</emoji>]",    
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я своим хуем выпилвал из дерева рамку для совместной фотки с твоей матерью ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]нахуй ты проводил тест драйв на моем хуе ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты понимаешь что я своим хуем выпилвал из дерева рамку для совместной фотки с твоей матерью ?[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ты к моему хую летишь как воробей[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я твоей матери яйцом глаза выбил[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]твоя мать шалава триперная[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]мой хуй тебя ебет и кормит[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]мой хуй не карандаш, но он оставил автограф на губе твоей мамаши[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]я твою мать ебал на тебе и случайно мы тебе сломали хребет[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]слушай лох на хуй соси и не скули пока я твою мать не начал ебать[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]твоя мать тупая блядь моим хуем себе карьеру сделала теперь радуется[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ахахахахахах блять как не зайдешь в магазин там твоя мать тупая сидит на коленях и у прохожих сосёт за деньги, вот блять откуда у вас в доме хлеб, оказалось твоя мать зарабатывает тяжелым трудом[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]вот ты олух ебаный забрался на мой хуй как альпинист на эверест и терь слезть не можешь[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ебу тебя лошка ебаного[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]нахуя твоя мать в рот мою сперму принимает ежедневно[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]хуем тебе зубки почистил дерьмоед ты ебаный, езз[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]свисла твоя пизда от моего большого хуя[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]а ты пониимаешь лох ебаный что я твою мать на свой хуй посажу и буду катать ее будто мой хуй это пони, а рядом я посажу тебя и скажу тебе что мой хуй это пони и ты будешь кататся на нем вместе со своей тупой мамашой[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]кароче смотри я своим хуем тебе губы щас пробивать буду[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]че твоя мать такая лахушка ебаная, я ее крч как срамоту ебаную поебал и кончил ей на сиськи а она взяла и сфоткала свои сиськи в моей конче и послала всему рунету и терь твоя мать прославлинная шлюшка[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]твоя мать грязная чертовка блять мой хуй не устает сосать ты прикинь блять лох ты ебаный она как автомат начинает и не может закончить, пока не отберу не отдаст дырка тупая[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]кароче твоя мать сказала что выдержит моего хуя и в итоге что я пришел к ней начал ее трахать во все щели выебал смотрю на нее а она мертвая лежит и на пузе у себя написала что прости я не выдерживаю но ты меня не слышешь, мда я ебать то думал она выдержит а она как грязная полумертвая хуйта погибла от моего хуя вот блядина ебаная[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]ебать че твоя мать сидя на моем хуе вытворяет чуть ли не стриптиз ебашит скача на моем хуе[<emoji document_id=5388994705805549866>☠️</emoji>]",
        "[<emoji document_id=5388994705805549866>☠️</emoji>]как шальной ты мой хуй сасешь лашок ебаный хаха[<emoji document_id=5388994705805549866>☠️</emoji>]"] 
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shablon6)))
            await sleep(time)