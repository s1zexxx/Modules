# meta author: s1zex
#meta developer: @yuki_marry
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message

class S1zexMod(loader.Module):
    '''Модуль by s1zex'''
    strings = {
    "name":  "s1zex 🔪 ",
    "loading": "<b>🔪 loading...</b>...</b>",
    "not_chat": "<b>🔪 Ты иᴦᴩᴀᴇɯь ᴄ ʍᴏиʍ ᴨᴇниᴄᴏʍ ᴋᴀᴋ ᴄ ᴇдᴏй..</b>",} 

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        
        
    async def szxhelpcmd(self, message):
        """Запустить анимацию [.szxhelp]"""
        args = utils.get_args_raw(message)
        await message.edit("🔪")
        time.sleep(0.1)
        await message.edit("🔪 s")
        time.sleep(0.1)
        await message.edit("🔪 s1")
        time.sleep(0.1)
        await message.edit("🔪 s1z")
        time.sleep(0.1)
        await message.edit("🔪 s1ze")
        time.sleep(0.1)
        await message.edit("🔪 s1zex")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("loading"))

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
            "<b>🔪 &  𝙷𝚎𝚕𝚙 & 🔪</b>\n\n"
            "<b>.szxhelp - Зᴀᴨуᴄᴛиᴛь ᴀниʍᴀцию хᴇᴧᴨы</b>\n\n\n"
            "<b>.szx1 - Сᴇᴋунды + Шᴀᴨᴋᴀ: Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь ᴨᴏ ᴨᴇᴩʙᴏʍу ɯᴀбᴧᴏну</b>\n\n"
            "<b>.szx2 - Сᴇᴋунды + Шᴀᴨᴋᴀ: Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь ᴨᴏ ʙᴛᴏᴩᴏʍу ɯᴀбᴧᴏну</b>\n\n"
            "<b>.szx4 - Сᴇᴋунды + Шᴀᴨᴋᴀ: Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь ᴨᴏ чᴇᴛʙᴇᴩᴛᴏʍу ɯᴀбᴧᴏну</b>\n\n"
            "<b>.szxmedia - Сᴇᴋунды + Шᴀᴨᴋᴀ: Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь медиа</b>\n\n"
            f"<b>User 🔪 name:</b>@{user_ent.username or '☠️'}\n"
            f"<b>First 🔪 name:</b> {user_ent.first_name or '🚫'}\n"
            f"<b>I'D:</b> <code>{user_ent.id}</code>\n"
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


    async def  szx2cmd(self, message):
        """Пример ввода: .szx2 Задержка появления текста в секундах & Обращение. \n"""
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "𐌑᧐ду᧘ь - szx - Зᴀᴋᴏнчиᴧᴀ ᴇбᴀᴛь ɯᴀᴧᴀʙ")
            return
        await utils.answer(
            message,
            "<b>𐌑᧐ду᧘ь - szx - Нᴀчᴀᴧ иᴄᴛᴩᴇбᴧяᴛь ᴄынᴋᴏʙ ɯᴀᴧᴀʙ\n\n"
        "Дᴀбы ʙыᴋᴧючиᴛь ʍᴏдуᴧь - szx - ᴨᴩᴏᴨиɯи <code>.szx2</code></b>"
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = ["твою мать шлюху ебет s1zex",]
        self.db.set(self.strings["name"], "state", True)
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)
            
    async def szxmediacmd(self, message):
        '''Запускает модуль с видео/фото/гс/кружком/гиф'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Прекратил ебать детей шлюх</b>")
            return
        await utils.answer(
            message,
            "<b>𐌑᧐ду᧘ь - szx - Нᴀчᴀᴧ иᴄᴛᴩᴇбᴧяᴛь ᴄынᴋᴏʙ ɯᴀᴧᴀʙ\n\n"
        "Дᴀбы ʙыᴋᴧючиᴛь ʍᴏдуᴧь - szx - ᴨᴩᴏᴨиɯи <code>.szxmedia</code></b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        media = reply.media
        shablon = [" мать твою шлюху ебет великий s1zex",
]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shablon)), file=media)
            await sleep(time)
            
    async def szx1cmd(self, message):
        """Пример ввода: .szx1 Задержка появления текста в секундах & Обращение. \n"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>𐌑᧐ду᧘ь - szx - Зᴀᴋᴏнчиᴧᴀ ᴇбᴀᴛь ɯᴀᴧᴀʙ</b>")
            return
        await utils.answer(
            message,
            "<b>𐌑᧐ду᧘ь - szx - Нᴀчᴀᴧ иᴄᴛᴩᴇбᴧяᴛь ᴄынᴋᴏʙ ɯᴀᴧᴀʙ\n\n"
        "Дᴀбы ʙыᴋᴧючиᴛь ʍᴏдуᴧь - szx - ᴨᴩᴏᴨиɯи <code>.szx1</code></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl2 = [" твою шлюху мать выебал @yuki_marry",]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)


    async def szx4cmd(self, message):
        """Пример ввода: .szx4 Задержка появления текста в секундах & Обращение. \n"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>𐌑᧐ду᧘ь - szx - Зᴀᴋᴏнчиᴧᴀ ᴇбᴀᴛь ɯᴀᴧᴀʙ</b>")
            return
        await utils.answer(
            message,
            "<b>𐌑᧐ду᧘ь - szx - Нᴀчᴀᴧ иᴄᴛᴩᴇбᴧяᴛь ᴄынᴋᴏʙ ɯᴀᴧᴀʙ\n\n"
        "Дᴀбы ʙыᴋᴧючиᴛь ʍᴏдуᴧь - szx - ᴨᴩᴏᴨиɯи <code>.szx4</code></b>",     
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl4 = [" сосешь сайзексу",]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl4))
            await sleep(0.1)
            await sleep(time)
