import random
import time
from asyncio import sleep
import os

from telethon import types
from .. import loader, utils

from datetime import datetime

from datetime import timedelta

from contextlib import suppress
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from .. import loader, utils

from asyncio import sleep

from datetime import timedelta

from telethon import types

import datetime

import logging

import time

import datetime

import random

from random import choice

import io

from asyncio import sleep
from telethon.tl.types import Message
from telethon import types
from random import randint
from os import remove
from datetime import datetime
from datetime import timedelta
from contextlib import suppress

from telethon.tl.functions.users import GetFullUserRequest


from datetime import timedelta

import random
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
import io
import logging
from io import BytesIO

import requests
from PIL import Image
from requests import post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename


logger = logging.getLogger(__name__)
from typing import List

from urllib.parse import quote

import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from contextlib import suppress
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message, MessageMediaPhoto

start = ""



userss = []
states = ""
reason = ""
ph = ""

shapka = "  "
shablon = ["ⱀƴҁѳѣʌᴙđџʜѧ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ʜѧ ҁπџʜє ϯʙѳєґѳ ґѳⱀѣѧϯѳґѳ ӡѧđⱀѳϯѧ ѳϯҵѧ",
"ϯƀӀ ҁʙџʜϯƴҁ ѫџⱀʜѳєѣʌƀӀӣ ҁʌѧʙѧⱀѧҁџҁᴙʜҁκџӣ ѧ ʜƴ χƴᴙ ҁѳҁџ",
"ӡѧⱀєѫєʍ ϯʙѳѥ ѫџⱀʜƴѥ ʍѧϯƴχƴ",
"ϯʙѳєґѳ ѳϯҵѧ πⱀџʌѥđʜѳ ƴʜџӡџʍ πџđѳⱀѧҁѧ ϶ϯѳґѳ",
"ϯƀӀ ʜєđєєҁπѳҁѳѣʜƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ ⱀƴҁʜᴙʙƀӀӣ χƴӣ ʌѳʙџ",
"đєⱀѫџ ӌʌєʜ ʙѳ ⱀϯƴ ҁʙѳёʍ ҁƀӀʜ ɯʌѥχџ",
"ƴʜџӡџʍ ϯʙѳё ҁʙџʜѳⱀƀӀʌѳ ϯƴϯ ӡѧπⱀѳҁϯѳ",
"ϯʙѳѥ ʍѧϯƴχƴ єѣѧʌџ ӡđєҁƀ ʙҁє",
"ⱀƴҁѳҁʙџʜ єѣѧʜƀӀӣ ᴙ ѫє ϯʙѳӣ ⱀѳđ џҁϯⱀєѣʌᴙѥϯ ʜє πⱀџʌѧґѧᴙ ҁџʌ",
"ϯʙѳѥ ѧⱀʍєӣκƴ κѳҁѳєѣʌƀӀχ πџđѧⱀѧҁѳʙ џӡʜџӌϯѳѫџʍ ʌєґκѳ",
"ϯƀӀ ⱀƴҁκџӣ ҁʙџʜ κƴđѧ πѳʌєӡ ϯѳ",
"ϯʙѳѥ ʍѧϯƴχƴ ⱀєѫєʍ ⱀѧҁҁѳҁѧӣ",
"ѣƴđєʍ ϯєѣᴙ πџʜѧϯƀ πѳκѧ ϯƀӀ ҁʙѳџ κѳπƀӀϯѧ ʜє ѳϯκџʜєɯƀ ҁƀӀʜ ɯʌѥχџ ҁʙџʜѳⱀƀӀʌƀӀӣ",
"ѧ ʜƴ ҁѳҁџ ʍʜє πєґѧҁ єѣѧʜƀӀӣ",
"ҵƀӀґѧʜҁκѳґѳ ҁƀӀʜκѧ ɯʌѥχџ ϯƴϯ ʙƀӀπʜєʍ",
"ϯʙѳџ ӡƴѣƀӀ ӌёⱀʜƀӀє ʙƀӀѣƀєʍ κ χƴᴙʍ ",
"ʙҁє ҵƀӀґѧʜҁκџє πѳѣⱀєκƴɯκџ ҁʜџʍєʍ ҁ ϯʙѳєӣ ɯєџ џ ӡѧπџχѧєʍ ϯєѣє ʙ ӡѧđ",
"ҁƀӀʜџѱє ⱀƴҁѳҁʙџʜҁκѳӣ ɯʌѥχџ ϯƀӀ ʙ ҁєѣᴙ πѳʙєⱀџʌ ӌϯѳ-ʌџ",
"ⱀѧӡʌѧґѧѥѱєӣҁᴙ ϯєʌѳ ϯʙѳєӣ ɯʌѥχѳʍѧϯєⱀџ ϯƴϯ ⱀѧҁπџđѳⱀѧҁџʍ ѳκѳʜӌѧϯєʌƀʜѳ",
"ҁʙџʜʜѳӣ πᴙϯѧκ ϯє ϯƴϯ єѣєʍ",
"κⱀџʙѳӡƴѣѳґѳ ѳϯҵѧ ϯʙѳєґѳ ʜѧѻѧⱀɯʍѧӌџʍ ѣєӡ πⱀѳѣʌєʍ",
"ƴʜџѫєʜʜƀӀӣ ҁƀӀʜƴʌᴙ κѳπⱀѳѻџʌκџ πⱀєκⱀѧϯџ ʙƀӀєѣƀӀʙѧϯƀҁᴙ ᴙ ϯєѣє ⱀƀӀʌƀʜџκ πєⱀєʌѳʍѧѥ",
"ϯʙѳё ⱀƀӀґѧʌѳ ϯƴϯ πєⱀєєѣѧɯџʍ ʙʜѳʙƀ",
"ʜє ѳϯκџđƀӀʙѧӣ κѳπƀӀϯѧ ҁƀӀʜџѱє ɯʌѥχџ єѣѧʜѳӣ",
"ӡѧκⱀѳӣ єѣѧʌѳ ᴙ ѫє ϯєѣє ʜѳґџ πєⱀєʌѳʍѧѥ ҁєӣӌѧҁ",
"ϯƀӀ ҁƀӀʜ ґѳʙʜѧ ҁѳҁџ ϯƴϯ",
"ⱀѧҁχƴᴙⱀџʍ ϯʙѳё ҁʙџʜѳⱀƀӀʌѳ џ ⱀѧҁκџđѧєʍ ѳҁϯѧϯκџ πѳ ʙҁєӣ κѳʜѻє",
"ӡѧκⱀѳӣ єѣѧʌѳ ϯƀӀ ʜєʍѳѱƀ єѣƴӌѧᴙ",
"ҁƀӀʜ ɯʌѥχџ ӡѧκⱀѳӣ ⱀƀӀґѧʌѳ ᴙ ϯєѣє ʍѧϯƀ ҁєӣӌѧҁ ʙʜѳʙƀ πєⱀєєѣƴ",
"ѫєʌϯѳӡƴѣƀӀӣ ѳϯҁѳҁѧӣđєⱀ ϯƀӀ ѫє ʜџѱƴκ ҁѳґʌѧҁџҁƀ",
"ʍѧϯƀ ϯʙѳѥ ϯⱀѧχѧʌџ ҁʌѧѣѧκ єѣѧʜƀӀӣ",
"ʜє πѧđѧӣ ʙ ҁʌёӡƀӀ ѳϯҁѳҁʜџκ ʜѧџҁʌѧѣєӣɯџӣ",
"ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ӌϯѳ ҁκѧѫєɯƀ",
"χѧӌ ᴙ ϯʙѳѥ ʍѳʜѳѣⱀѳʙƀ ϯƴϯ ҁ κѳѫєӣ ʜѧχƴӣ ʙƀӀⱀєѫƴ",
"χѧⱀӌѳκ ʌѳʙџ ҁƀӀʜƴʌᴙ ɯʌѥχџ єѣѧʜѳӣ",
"πⱀџʜџʍѧӣ πʌєʙκџ ʙ ҁʙѳё ҁʙџʜѳⱀƀӀʌѳ đєґєʜєⱀѧϯ єѣѧʜƀӀӣ",
"ϯєⱀπџʌѧ ʜє ʙӡđƴʍѧӣ ϯƴϯ πѳđѳχʜƴϯƀ",
"πѳκѧѫџ ҁʙѳѥ ʍџӡєⱀʜƴѥ ѻѧʜϯѧӡџѥ πѳκѧ ᴙ ʜє ӡѧπʌєʙѧʌ ϯʙѳѥ κⱀџʙѳʜѳҁƴѥ ⱀѳѫƴ",
"ҁʌƀӀɯџɯƀ πєđџκ ґѳʙʜѳєѣʌƀӀӣ ʌѳʙџ ӌʌєʜ",
"ⱀƴҁѳҁʙџʜѧ ϯƴϯ πѳⱀєѫєʍ",
"ϯƀӀ ϯƴϯ ʍѧκҁџʍƴʍ κѧκ πєɯκѧ ѣєґѧєɯƀ џ ʙҁєʍ χѳχʌѧʍ χƴџ ѳϯҁѧҁƀӀʙѧєɯƀ",
"ϯєⱀπџʌѧ єѣѧʜѧᴙ ϯєѣᴙ ϯƴϯ ӡѧҁʍєѥϯ ҁ ϯѧκџʍ ƴҁπєχѳʍ",
"ѳϯҁѳҁџ ʍʜє πєɯѧκ єѣѧʜƀӀӣ",
"πџđѧⱀѧҁ ґѳʙʜѳⱀѳѫџӣ ʜѧʍƴϯџ ѳϯҁѳҁѧ",
"ѧⱀƴ ʜƴƴƴ ϯƀӀ ӌє ҁƀӀʜѳκ ɯʌѥχџ ҁѥđѧ ʙ ҁʌєӡѧχ πⱀџπєⱀҁᴙ",
"đѧʙѧӣ πѳ ґѧӡѧʍ πѳκѧ ᴙ ϯʙѳѥ ҁєҁϯⱀџӌκƴ ⱀƴҁѳҁʙџʜҁκƴѥ ʜє ʙƀӀєѣѧʌ",
"ʍʜє πѳχƴӣ ӌё ϯƀӀ ϯѧʍ ʙ χƴӣ ʍƴⱀӌџɯƀ ƴєѣџѱє ᴙ ϯєѣє ʜѧπѳʍџʜѧѥ ӌϯѳ ϯʙѳѥ ʍѧϯƀ ʜѧϯᴙґџʙѧʌ џ ӌё ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ϯѳ ϯєⱀπџʌѧ єѣѧʜѧᴙ",
"ϯєⱀπџʌƴ ϯƴϯ ⱀѧҁχƴᴙⱀџʍ ѫє ʜѧχƴӣ",
"ѧ ʜƴ ӡѧκⱀѳӣ єѣѧʌѳ ҁƀӀʜ ɯʌѥχџ",
"ᴙ ϯʙѳё ҁʙџʜѳⱀƀӀʌѳ ϯƴϯ ⱀѧҁπџđѳⱀѧɯƴ"]


state = True
state1 = True
state2 = True
shapka = ""

prem = "[<emoji document_id=5379696449502060899>🔥</emoji>|<emoji document_id=6073619880131693600>👹</emoji><emoji document_id=5316751509050895464>🇺🇦</emoji>|-[<emoji document_id=5469702445582004130>😈</emoji>]-<emoji document_id=5377834924776627189>⚡️</emoji><emoji document_id=5409310974857455487>🇪🇪</emoji>⟩"
prem2 = "⟨<emoji document_id=5409310974857455487>🇪🇪</emoji><emoji document_id=5377834924776627189>⚡️</emoji>-[<emoji document_id=5469702445582004130>😈</emoji>]-|<emoji document_id=5316751509050895464>🇺🇦</emoji><emoji document_id=6073619880131693600>👹</emoji>|<emoji document_id=5379696449502060899>🔥</emoji>]"
prem3 = "[<emoji document_id=5370724688022482249>🌟</emoji>|<emoji document_id=5346089481462095285>🔥</emoji><emoji document_id=5388931913383680272>💜</emoji>|-[<emoji document_id=5217454154384943897>🦋</emoji>]-<emoji document_id=5217666265639822706>💀</emoji><emoji document_id=5431766360961068331>🌟</emoji>⟩"
prem4 = "⟨<emoji document_id=5431766360961068331>🌟</emoji><emoji document_id=5217666265639822706>💀</emoji>-[<emoji document_id=5217454154384943897>🦋</emoji>]-<emoji document_id=5388931913383680272>💜</emoji><emoji document_id=5346089481462095285>🔥</emoji>|<emoji document_id=5370724688022482249>🌟</emoji>]"
prem5 = "[<emoji document_id=5231391336145365545>🇺🇦</emoji>|<emoji document_id=5352542184493031170>😈</emoji><emoji document_id=5379650961503428163>❤️</emoji>|-[<emoji document_id=6073490627385887309>👹</emoji>]-<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5467908304598475967>😈</emoji>⟩"
prem6 = "⟨<emoji document_id=5467908304598475967>😈</emoji><emoji document_id=5352919308391424163>🔥</emoji>-[<emoji document_id=6073490627385887309>👹</emoji>]-|<emoji document_id=5379650961503428163>❤️</emoji><emoji document_id=5352542184493031170>😈</emoji>|<emoji document_id=5231391336145365545>🇺🇦</emoji>]"
prem7 = "[<emoji document_id=5445118241758257251>🇺🇦</emoji>|<emoji document_id=5188638346917717584>🌝</emoji><emoji document_id=6071177551273790342>👹</emoji>|-[<emoji document_id=5474261042265598751>👹</emoji>]-<emoji document_id=5474342835622782187>🔥</emoji><emoji document_id=5449696625356186811>😈</emoji>⟩"
prem8 = "⟨<emoji document_id=5449696625356186811>😈</emoji><emoji document_id=5474342835622782187>🔥</emoji>-[<emoji document_id=5474261042265598751>👹</emoji>]-|<emoji document_id=6071177551273790342>👹</emoji><emoji document_id=5188638346917717584>🌝</emoji>|<emoji document_id=5445118241758257251>🇺🇦</emoji>]"
prem9 = "[<emoji document_id=5199939531154924006>💀</emoji>|<emoji document_id=5312005570188819724>☠️</emoji><emoji document_id=6073311553019447554>👹</emoji>|-[<emoji document_id=5312537523363259501>☠️</emoji>]-<emoji document_id=5312190021854308362>☠️</emoji><emoji document_id=5370766984860411217>🔪</emoji>⟩"
prem10 = "⟨<emoji document_id=5370766984860411217>🔪</emoji><emoji document_id=5312190021854308362>☠️</emoji>-[<emoji document_id=5312537523363259501>☠️</emoji>]-|<emoji document_id=6073311553019447554>👹</emoji><emoji document_id=5312005570188819724>☠️</emoji>|<emoji document_id=5199939531154924006>💀</emoji>]"
@loader.owner
def register(cb):
    cbrenewalmod()
class renewal(loader.Module):
    strings = {"name": "RENEWAL",
         "pref": "<b>[RENEWAL]</b> ",
        "need_arg": "{}Нужен аргумент",
        "status": "{}{}",
        "on": "{}Запущен",
        "off": "{}Выключен",
        "load": "downloading...",
        "loading": "⁣<emoji document_id=5411397985365927767>🇦🇲</emoji><emoji document_id=5411397985365927767>🇦🇲</emoji><emoji document_id=5411397985365927767>🇦🇲</emoji>",
    }
    _db_name = "RENEWAL"

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        self.users = []


    @staticmethod
    def str2bool(v):
        return v.lower() in (
            "yes",
            "y",
            "ye",
            "yea",
            "true",
            "t",
            "1",
            "on",
            "enable",
            "start",
            "run",
            "go",
            "да",
        )


    async def rwtagcmd(self, message):
        '''[id] [задержка в секундах]'''
        args = utils.get_args(message)
        global state
        message = await utils.answer(message, self.strings("load"))
        state = True
        await message.delete()
        user_id = int(args[0])
        while state:
            text = random.choice(shablon)
            time = float(args[1])
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_message(message.peer_id, f"{shapka} {prem}<a href='tg://user?id={user_id}'>{text}</a>{prem2}")
                await sleep(0.1)
                await sleep(time)

    async def rwstopcmd(self, message):
        '''останавливает тэггер'''
        args = utils.get_args_raw(message)
        global state
        state = False
        message = await utils.answer(message, "<b>остановлено</b>")


    async def rwidcmd(self, message):
        "[reply]"
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        try:
            if args:
                user = await message.client.get_entity(
                    int(args) if args.isdigit() else args)

            else:
                user = await message.client.get_entity(reply.sender_id)
        except ValueError:
            user = await message.client.get_entity(reply.sender_id)

        await message.edit(
            f"[࿕] user = <code>{user.first_name}</code>\n"
            f"[࿕] id = <code>{user.id}</code>"
            
            )


    async def rwtypercmd(self, message):
        """[время в секундах]"""
        args = utils.get_args(message)
        if args:
            try:
                await message.delete()
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(args[0]))
            except ValueError:
                await message.edit("некорректное значение времени.")
            except Exception as e:
                await message.edit(f"ошибка: {str(e)}")
        else:
            await message.edit("укажите время тайпа в секундах.")


    async def client_ready(self, client, db):

        self.client = client


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client


    async def rwanscmd(self, m: types.Message):
        "[on/off]"
        args = utils.get_args_raw(m)
        if not m.chat:
            return
        chat = m.chat.id
        if self.str2bool(args):
            chats: list = self.db.get(self._db_name, "chats", [])
            chats.append(chat)
            chats = list(set(chats))
            self.db.set(self._db_name, "chats", chats)
            return await utils.answer(
                m, self.strings("on").format(self.strings("pref"))
            )
        chats: list = self.db.get(self._db_name, "chats", [])
        try:
            chats.remove(chat)
        except:
            pass
        chats = list(set(chats))
        self.db.set(self._db_name, "chats", chats)
        return await utils.answer(m, self.strings("off").format(self.strings("pref")))



    async def rwansscmd(self, m: types.Message):
        '''шапка для автоотвечика'''
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "sh", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )


    async def rwanszcmd(self, m: types.Message):
        "[время в секундах]"
        args: str = utils.get_args_raw(m)
        if args.isdigit():
            self.db.set(self._db_name, "chance", int(args))
            return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

        return await utils.answer(
            m, self.strings("need_arg").format(self.strings("pref"))
        )


    async def rwanstxtcmd(self, m: types.Message):
        "[название текстовика с .txt]"
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "text", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

    async def rwansdcmd(self, message):
        """[reply]"""
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if reply:
            await message.edit('скачиваем...')
            if reply.text:
                text = reply.text
                fname = f'{name or message.id + reply.id}.txt'
                file = open(fname, 'w')
                file.write(text)
                file.close()
                await message.edit(
                    f'файл сохранён как: <code>{fname}</code>')
            else:
                ext = reply.file.ext
                fname = f'{name or message.id + reply.id}{ext}'
                await message.client.download_media(reply, fname)
                await message.edit(
                    f'этот файл сохранён как: <code>{fname}</code>')
        else:
            return await message.edit('нет реплая.')


    async def watcher(self, m: types.Message):
        if not isinstance(m, types.Message):
            return
        if m.sender_id == (await m.client.get_me()).id or not m.chat:
            return
        if m.chat.id not in self.db.get(self._db_name, "chats", []):
            return
        ch = self.db.get(self._db_name, "chance", [])
        sh = self.db.get(self._db_name, 'sh', [])
        text = self.db.get(self._db_name, 'text', [])
        with open(f'{text}', 'r', encoding='utf-8') as f:
            a = f.read()
            b = a.split('\n')
            await sleep(ch)
            await m.reply(sh + random.choice(b))


    async def rwusedcmd(self, message):
        """[reply]"""
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if reply:
            await message.edit('Скачиваем...')
            if reply.text:
                text = reply.text
                fname = f'{name or message.id + reply.id}.txt'
                file = open(fname, 'w')
                file.write(text)
                file.close()
                await message.edit(
                    f'файл сохранён как: <code>{fname}</code>')
            else:
                ext = reply.file.ext
                fname = f'{name or message.id + reply.id}{ext}'
                await message.client.download_media(reply, fname)
                await message.edit(
                    f'этот файл сохранён как: <code>{fname}</code>')
        else:
            return await message.edit('нет реплая.')

    async def rwusecmd(self, message):
        """[задержка в секундах] [текстовик] [шапка]"""
        shapka = utils.get_args_raw(message)
        if not shapka:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "модуль остановлен!")
            return
        await utils.answer(
            message,
            "модуль запущен!"
            )
        text = shapka.split(' ')
        time = int(text[0])
        sh = ''.join(text[1])
        shp = ' '.join(text[2:])
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            with open(f'{sh}', 'r', encoding='utf-8') as f:
                s = f.read()
                w = s.split('\n')
                await message.respond((shp + random.choice(w)))
                await sleep(time)


    async def rwchatidcmd(self, message):
        "узнает айди чата"
        if message.is_private:
            return await message.edit("...")
        args = utils.get_args_raw(message)
        to_chat = None

        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id


        except ValueError:
            to_chat = message.chat_id

        chat = await message.client.get_entity(to_chat)

        await message.edit(
            f"[࿕] title = <code>{chat.title}</code>\n"
            f"[࿕] id = <code>{chat.id}</code>"
            
            )

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client


    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client


    async def rwshcmd(self, message):
        '''шапка тегера'''
        args = utils.get_args_raw(message)
        if args:
            s = args
            global shapka
            shapka = s
            await message.edit(f'<b>ваша шапка:{shapka}</b>')


    async def rwtag1cmd(self, message):
        '''[id] [задержка в секундах]'''
        args = utils.get_args(message)
        global state
        message = await utils.answer(message, self.strings("load"))
        state = True
        await message.delete()
        user_id = int(args[0])
        while state:
            text = random.choice(shablon)
            time = float(args[1])
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_message(message.peer_id, f"{shapka} {prem3}<a href='tg://user?id={user_id}'>{text}</a>{prem4}")
                await sleep(0.1)
                await sleep(time)


    async def rwtag2cmd(self, message):
        '''[id] [задержка в секундах]'''
        args = utils.get_args(message)
        global state
        message = await utils.answer(message, self.strings("load"))
        state = True
        await message.delete()
        user_id = int(args[0])
        while state:
            text = random.choice(shablon)
            time = float(args[1])
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_message(message.peer_id, f"{shapka} {prem5}<a href='tg://user?id={user_id}'>{text}</a>{prem6}")
                await sleep(0.1)
                await sleep(time)


    async def rwtag3cmd(self, message):
        '''[id] [задержка в секундах]'''
        args = utils.get_args(message)
        global state
        message = await utils.answer(message, self.strings("load"))
        state = True
        await message.delete()
        user_id = int(args[0])
        while state:
            text = random.choice(shablon)
            time = float(args[1])
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_message(message.peer_id, f"{shapka} {prem7}<a href='tg://user?id={user_id}'>{text}</a>{prem8}")
                await sleep(0.1)
                await sleep(time)


    async def rwtag4cmd(self, message):
        '''[id] [задержка в секундах]'''
        args = utils.get_args(message)
        global state
        message = await utils.answer(message, self.strings("load"))
        state = True
        await message.delete()
        user_id = int(args[0])
        while state:
            text = random.choice(shablon)
            time = float(args[1])
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_message(message.peer_id, f"{shapka} {prem9}<a href='tg://user?id={user_id}'>{text}</a>{prem10}")
                await sleep(0.1)
                await sleep(time)


    async def ragecmd(self, message):
        """[задержка в секундах] [шапка]"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴋᴏнчиᴧ ᴩᴇɜᴀᴛь ᴩуᴄᴏᴄʙинᴇй 𓆩ꏢ𓆪</b>")
            return
        await utils.answer(
            message,
            "<b>ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уᴋᴩᴀинᴄᴋᴀя яᴩᴏᴄᴛь нᴀчᴀᴧᴀ ᴨᴩᴏᴧиʙᴀᴛь ᴩуᴄᴏᴄʙинᴄᴋую ᴋᴩᴏʙь 𓆩ꏢ𓆪</b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        wablon = [
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴇɜᴀʍᴇдᴧиᴛᴇᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴄʍᴏᴛᴩя нᴀ ᴄᴧᴏжнᴏᴄᴛи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴨᴩиʙычᴋᴇ ᴛы ʍнᴇ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ ᴄᴨᴇᴩʍᴏй ɜᴀᴧью 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ʍнᴇ ᴛᴇчёᴛ ᴋᴩᴏʙь ᴄ бᴩюхᴀ ᴛʙᴏᴇᴦᴏ бᴀᴛи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏ ʍнᴇ ᴛᴇчёᴛ чиᴄᴛᴀя ᴋᴩᴏʙь уᴋᴩᴀинцᴀ, ʙᴏ ʙᴩᴇʍя ϶ᴛᴏᴦᴏ жᴇ ᴛы чуᴩᴋᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ɸуᴧᴧ ᴇбᴀᴧᴇ ᴛᴇ ʙ ᴩᴏᴛ ᴄᴄу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛᴇбя ᴋᴀᴋ ᴇбᴀᴧи ᴋᴩᴀᴄных ʙ 44 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюхи хᴇх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇчнᴏ ᴦᴏᴛᴏʙ ᴛᴇбя ᴨᴏᴇбыʙᴀᴛь бᴇᴄᴨᴧᴀᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɯёʙую ᴨᴩᴏᴄᴛиᴛуᴛᴋу ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴧищᴇ ʙ хуй ʙᴏᴛᴋни 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄёɯь ᴋᴀᴋ ᴄᴏᴄуᴛ ʙᴀᴦнᴇᴩяᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ʙᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи уᴇбищᴇ ᴩуᴄняʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀɜᴏʙ ᴛя ᴇбёᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴩиʙыᴋ ᴛᴀᴋ хуи ᴄᴏᴄᴀᴛь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> удᴏбнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴀ ᴩᴏᴄᴄийᴄᴋᴏʍ яɜыᴋᴇ чᴛᴏбы ᴛы ᴨᴏняᴧ ᴋᴀᴋᴏй ᴛы ᴏᴨущᴇнный ᴄын ɯᴧюхи) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏɯибᴀяᴄь ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴏᴧᴦᴏ ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴩᴏᴄᴄиянᴄᴋий ᴄын бᴧяди ᴛуᴛ нᴇ хᴩюᴋᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɸᴇᴋᴀᴧищᴇ ᴄᴏжᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиʙычнᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛя ᴨᴏᴩᴇɜᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй яɜыᴋ нᴀ чᴧᴇнᴇ, чё ᴛы ᴏᴛцу ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛы ᴄ хуя ʍнᴇ ᴋᴩичᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы унижᴇннᴀя ᴄʙинᴏᴨᴄинᴀ ᴇбᴧищᴇ ᴛᴇ ᴛуᴛ ᴩᴀᴄᴋᴀᴛᴀᴧ ᴄучᴋᴇ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чᴏ ᴛᴇᴩᴨиɯь дᴇбиᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨуᴛиниᴄᴛ ᴛы хуй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛиᴋ ɯᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛᴇбя ʙ ᴛʙᴏй ᴩᴏᴛ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ ʍᴀʍᴇ ᴨᴏд ɜᴇᴩᴋᴀᴧьныʍ ʙᴏɜдᴇйᴄᴛʙиᴇʍ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ɜᴀᴋᴏнчиᴧ ᴛᴩᴀхᴀᴛь ᴛʙᴏю ᴄᴇᴄᴛᴩу ᴋᴏᴦдᴀ ᴛʙᴏй ᴏᴛᴇц ᴨᴏᴩʙᴀᴧ ᴛᴇбᴇ ᴀнᴀᴧ, ᴀ ᴛы иɜ ʙᴏɜʍущᴇния чᴛᴏ ᴄ хуя ᴋᴩиᴋнуᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴨᴀᴄᴛь, ᴀ ᴛы чᴛᴏ ʍнᴇ ʙ хуй ᴏᴩᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴋᴩᴏй ᴄʙᴏё ᴇбᴧищᴇ ᴨᴀᴩɯиʙᴏᴇ, ᴇбᴧᴀнихᴀ ᴄᴛᴩёʍнᴏʙыᴦᴧядящᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чё ᴛы ʙ хуй ᴛᴀʍ ᴄᴋуᴧиɯь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи хᴀᴩчᴋи ʙ ᴛʙᴏё ᴇбᴧᴏ, дᴇбиᴧᴋᴀ ᴩуᴄняʙᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴄ хуя ʍᴏᴧʙиɯь ʙᴄё ᴛы бᴇɜ иᴄᴋᴧючᴇний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛʙᴇᴛь ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇᴄᴧи ᴄᴩᴀᴧи нᴀ ᴛя ᴏᴛʙᴇᴛь ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴛᴏ ᴛᴇбя ᴇбᴀᴧ ᴏбʍᴀни ᴄᴇбя жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴛᴇбя яɜыᴋ нᴀ хуᴇ чᴛᴏ ʍᴀʍᴇ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴦᴀдᴀй жᴇᴧᴀниᴇ ʙ ʙидᴇ хуя ʙ ᴩᴏᴛ ᴄᴇбᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛᴇбᴇ нᴀ ϶ᴛᴏ ʙᴄё бᴀбᴋᴀ хуᴇʍ ʙ ᴩᴏᴛ дᴀᴧᴀ ᴇᴄᴧи дᴏ и ᴨᴏᴄᴧᴇ у ᴛᴇбя яɜыᴋ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я бᴏᴦ ᴨᴩᴀʙды ᴀ ᴛы ᴋᴛᴏ ᴨᴩᴇдᴄᴛᴀʙьᴄя ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀᴋ ᴋᴀᴋᴏᴇ ᴨᴩᴇдᴄʍᴇᴩᴛнᴏᴇ ᴄᴧᴏʙᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи быᴧᴏ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨᴩᴀʙдᴀния ᴛуᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ниᴋᴏᴦдᴀ нᴇ будᴇɯь бᴏᴦᴏʍ ᴨᴩᴀʙды и ʙᴄᴇ ᴛʙᴏи ᴄᴧᴏʙᴀ ʙыɯᴇ и нижᴇ будуᴛ ᴏᴛʍᴇнᴇны 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴛы ᴄʙᴏю ᴩᴏдную ʍᴀᴛь убиᴧ ᴏᴛᴨиɯи нижᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴏ ᴛы бᴀбᴋᴇ ʙ ᴋᴧиᴛᴏᴩ ᴦᴏʙᴏᴩиᴧ яɜыᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴏᴛᴨᴩᴀʙиᴧ быᴧᴏ нᴀᴨиᴄᴀнᴏ ʙ ʍиᴩᴇ ʙᴩᴀнья ᴄ яɜыᴋᴏʍ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иᴦнᴏᴩᴏʍ ᴩᴏдᴏᴄᴧᴏʙную убᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏʙᴩи ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ уʍᴇю ʙᴩᴀᴛь, ᴛы ᴄын ɯᴧюхи  𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴩуᴄᴏᴄʙинᴄᴋᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᏌᴋrᴀiniᴀnᏒᴀgᴇ ᴇбᴀɯиᴛ ᴦᴧᴏᴛᴋу ᴛᴇ 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>нᴀ ᴧᴇᴄᴏᴨиᴧᴋᴇ ᴛя ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ нᴏй ᴄʙинᴏᴩуᴄ ᴏᴨущᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу хуᴇʍ ᴛᴇ ᴨᴇᴩдᴀᴋ нᴀ ᴧᴇᴦᴋᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀᴩᴋᴀю ᴛᴇ ʙ ᴇбᴀᴧᴏ дуᴩᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуя ᴨᴏᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧ ᴛᴇ ʙ ᴩᴏᴛ хуй ᴄᴏ ᴄᴧᴏʙᴀʍи ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏбᴏᴄᴩᴀᴧ ᴛᴇбᴇ ᴇбᴀᴧᴏ и чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу, ᴀ ᴛы чᴛᴏ ᴇй ᴋᴩичᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴩᴀᴧ нᴀ ᴛʙᴏё ᴇбᴧищᴇ ᴄᴏ ᴄᴧᴏʙᴀʍи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄᴋᴩиᴨᴛᴏʙᴀнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя удуɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇйчᴀᴄ ᴛᴇбя ᴇбёᴛ хᴏхᴏᴧ, ᴩᴀᴄᴋᴩыʙᴀй ᴄʙᴏю ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюɯᴇчᴋи ᴨиɜдᴏᴨᴩᴏʙᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴀᴄᴀй хуяᴩу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇбᴇ бᴀбᴋᴀ ʙ ᴩᴏᴛ, чᴛᴏ ᴛы нᴀ ϶ᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ хуᴇʍ ᴋᴩᴀᴄиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ɜуб ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хую ᴛы ᴋᴩуᴛиᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴋᴏнчᴀᴧ ᴛᴇбᴇ нᴀ ᴧицᴏ, ᴀ ᴛы чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏё ᴩыᴧᴏ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ бᴀбᴋᴇ ᴄ хуᴇʍ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴄʙᴏё ʙᴀᴧьни ᴄын бᴧяди ᴏᴛᴄᴛᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ᴛя хᴏхᴧы хᴏɜяᴇʙᴀ ᴛʙᴏи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу ᴄʙинᴏᴩуᴄню и ᴛы нᴇ ᴨᴏᴄᴧᴇдний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴇбуᴛ ʙᴄ ᴩɸ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴋᴩиᴄᴛᴀᴧичнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩʙу ᴛᴇбя ᴋᴀᴋ ᴩʙуᴛ ʙᴀᴦнᴇᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ʍᴀʍᴀɯу ᴛᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи ʙяᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏᴩʙᴀᴧ ɜᴩᴋ ᴄ-300 ʙ ᴋᴏᴛᴏᴩᴏʍ быᴧ ᴛʙᴏй ᴏᴛᴇц ᴄ ʙᴀᴦнᴇᴩᴀ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴛᴩᴏᴧᴧиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴋᴩыᴧ жиʙᴏᴛ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴄᴀᴛᴀнᴏй хуяᴩиʍ ᴋᴀᴦᴏᴩ и ᴇбᴇʍ ᴛʙᴏю ʍᴀʍᴀɯᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ дуᴧᴏ ᴛᴀнᴋᴀ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи нᴀᴄᴀдиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴩᴇнᴏй ᴨᴏдᴏᴩʙᴀᴧ ᴛʙᴏᴇᴦᴏ бᴀᴛю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴩᴇжу ᴛᴇ ᴦᴧᴏᴛᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴛᴀᴧ нᴀ ᴄʍᴇᴩᴛный бᴏй и ɜᴀᴩубиᴧ ᴛʙᴏᴇᴦᴏ бᴩᴀᴛᴀ ᴋᴀᴛᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴨᴩиниʍᴀᴇᴛ ʙ ᴄᴇбя ʙᴄё чᴛᴏ ʙᴧᴇɜᴇᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя хᴀᴩᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуйцᴏʍ ᴛя ᴩᴀɜʙᴧᴇᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛя нᴀ ᴧᴏᴨᴀᴛу нᴀᴄᴀжу и чиᴄᴛᴏ ᴋᴀᴋ ᴄиʍбу ᴩᴀᴄᴋᴩучу и ᴏб ᴄᴋᴀᴧу уᴇбу ᴛᴀᴋую дуᴩу ᴛуᴨᴏᴩыᴧую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴏʍᴀᴧ ᴛᴇ ᴄᴨину хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛхуяᴩю ᴛя ᴨᴏ ᴧбу чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уᴇбᴀᴧ ᴛᴇбя ᴄ нᴏᴦи ᴨᴏ ᴩᴇбᴩᴀʍ ᴛʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʍᴇᴩᴄᴀй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧый ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бью ᴛя ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ᴄᴨᴀᴄибᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь? ᴏᴛʙᴇᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ дуᴩᴀ ᴇбᴀнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴛᴇбᴇ ᴄᴋᴀɜᴀᴧи ᴨидᴀᴩᴀᴄᴋᴀ нᴇдᴏᴩᴀɜʙиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧюнуᴧ ʙ ᴛя ɜᴀᴧуᴨᴏй, ᴨᴏᴋᴀ ᴛы хᴀᴩᴋᴀᴇɯь ʙ ɜᴇᴩᴋᴀᴧᴏ ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ жᴀᴧᴋий ᴄынᴏчᴇᴋ хуᴇᴄᴏᴄᴀᴧᴋи нищᴇй чё ᴛы ᴛуᴛ ɜᴀбыᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ɜᴀᴋᴩᴏй ужᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇᴄᴨᴩᴇᴩыʙнᴏ ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ уᴋᴩᴀинᴄᴋᴏй ʍинᴇ ᴛʙᴏй ᴏᴛᴇц ᴨᴏдᴏᴩʙᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇхуй ᴧᴇɜᴛь, ᴨидᴏᴩᴀɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄи чуɯᴋᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди ᴏᴨущᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴇ чуᴩᴋᴏхᴀч ᴛы нᴀхуй ᴄᴏᴄнуᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴧучиᴧ ᴛы ᴨᴏ ᴇбᴀᴧу ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴦдᴀ ᴛя ᴨᴏᴇбᴀᴧи ᴛᴀᴋ жᴇ ᴋᴀᴋ и ᴛы ʍᴏᴧчᴀᴧи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜбᴩᴀннᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ бᴏᴋу ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴛᴏʙ ᴛᴇ бᴇᴄᴋᴏнᴇчнᴏ нᴀ ᴋᴧыᴋ ᴏɸᴏᴩʍᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ ᴧюбʙи ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴛы нᴀᴄᴏᴄᴀᴧ хуя ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴋᴀйɸ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи чᴧᴇн ʙ ᴦᴏᴩᴧᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴄыᴋᴧиʙᴏ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴇʍ ᴛя чинᴦиɜхᴀнᴀ ᴇбᴀнᴏᴦᴏ ᴄ буᴩяᴛии нᴀхуй хᴀɜхᴀɜɜᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴄын ɯᴧюхи ᴋᴏᴨыᴛный ɜᴀчᴇʍ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴄʙин ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙяᴧый хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴄᴛᴀнциᴏннᴏ ᴄᴏᴄёɯь ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя, ᴩуᴄᴏᴄʙин 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛᴇбя ᴨᴏиʍᴇᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏинᴄᴛʙᴇннᴏ ᴛᴇбя ᴨᴏᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ ᴄын ᴄʙиньи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴛʙᴏё ᴨᴏᴇбᴇʍ, дᴇᴦᴇнᴇᴩᴀᴛины ᴄын 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦʙᴏɜдь ᴋ ᴩуᴋᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋ ᴇбᴀᴧу ᴛᴇ диᴧдᴀᴋ жᴇᴧᴇɜный ᴨᴩиᴧᴇᴨиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ᴨᴏᴨᴩᴀʙь ᴋᴩиʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи нᴀᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ʙᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴄᴛᴏʍᴀᴛᴏᴧᴏᴦии ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴀᴩᴀɯᴇ я ᴄᴩᴀᴧ и ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴛᴀʍ жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴩᴏʙᴀᴛи ᴛʙᴏй ᴩᴏᴛ ᴛᴩᴀхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы нᴀ ᴨᴀчᴋу ᴄухᴀᴩиᴋᴏʙ бᴧя ᴇбᴀнᴀᴛ нищᴇнᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴧяᴛь ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩу ʙᴄᴏᴄи ᴄынᴏᴋ бᴧядины 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩяйᴄя нᴀхуй ᴨᴏᴋᴀ ᴛᴇ ᴇбᴀᴧᴏ ᴛуᴛ хуᴇʍ нᴇ ᴩᴀᴄᴋʙᴀᴄиᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ ɜᴀᴧуᴨы ʍᴏᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу жᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏжᴩи дᴇᴩьʍᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛᴇбя у ɯᴋᴏᴧы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦᴧᴀɜ ʙыᴩʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴨᴧяжᴇ чёᴩнᴏᴦᴏ ʍᴏᴩя ᴛʙᴏю ʍᴀᴛь ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧбᴀᴇб ɯᴧᴀнᴦ дᴩᴏчи ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏбᴩᴀннᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴩу ᴋᴏᴦдᴀ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴧюби ᴄᴏᴄᴀᴛь ᴋᴀᴋ ᴧюбиɯь ᴄᴦᴧᴀᴛыʙᴀᴛь ᴄын ɯᴧюхᴛ хᴀɜ϶ᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ Ꮧёɯᴋᴀ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩю ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀбиᴧ ᴛя ʙ уᴦᴧу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴨинᴀᴧ ᴛя хуᴇʍ дуᴩу ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇᴨᴏʙᴛᴏᴩиʍᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛʙᴏᴇй ᴨиɜдᴇ иᴦᴩᴀᴧᴄя, ᴛёᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨиɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴋᴀᴋ бᴀᴩᴀн идᴇᴛ ᴄʙᴏиʍи ᴦубᴀʍи нᴀ ʍᴏй хуй нᴀ ᴛᴀᴩᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴧᴏᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏᴋɜᴀᴧᴇ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴦиᴧьныʍ ᴋᴩᴇᴄᴛᴏʍ ᴛʙᴏᴇᴦᴏ дᴇдᴀ ᴇбᴀᴧ ᴛᴩуᴨ ᴛʙᴏᴇй бᴀбᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏᴛбᴩᴀᴄыʙᴀй ᴋᴏᴨыᴛᴀ ᴏᴛ ʍᴏᴇᴦᴏ чᴧᴇнᴀ ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴩиʙᴏᴇбᴧый ᴄын ʍᴩᴀᴋᴏбᴇᴄия ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧᴏᴄᴋᴏᴇбᴧый ᴨидᴏᴩᴀᴄ нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏбиᴧ ᴛʙᴏй чᴇᴩᴇᴨᴏᴋ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀбᴄиянинᴀ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴏ ᴋᴀᴋ ᴛᴀʍ ᴩᴏᴄᴄиянцы хᴏхᴧᴀʍ ᴄᴏᴄуᴛ ʍдᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ чᴇᴛʙᴇᴩᴇньᴋᴀх ʍнᴇ ᴄᴏᴄᴀᴧᴀ ʍᴀᴛь ᴛʙᴏя 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчуʙᴄᴛʙуй хᴏᴛь ᴄᴇйчᴀᴄ ɜᴀᴨᴀх ᴄʙᴏбᴏды и ʙыбᴇᴩи чᴏ ᴄᴏᴄᴀᴛь будᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴧчи ᴄ чᴧᴇнᴏʍ ʙᴏ ᴩᴛу ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ʙᴏᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴇниᴄ ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴛᴏ Ꮯᴀɯᴋᴀ ᴄᴏᴄᴀᴛь ᴛᴏ будᴇɯь ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄиɸᴏɜнᴏй ɯᴧюхи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀ ᴛʙᴏя нᴀ чᴧᴇнᴇ ᴨᴏᴛухᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴛы чᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴛʙᴏю ʍᴀᴛь чᴧᴇнᴏʍ ɜᴀᴇхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏᴄᴛᴩᴇᴧиᴧ ᴋᴏᴧᴇни ᴏᴛцу ᴛʙᴏᴇʍу ʙᴀᴦнᴇᴩᴏʍяᴄу ᴇбучᴇʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ʍᴏнᴇᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴛь ᴛʙᴏю ʙ ᴀнᴀᴧ ᴦᴧᴀдᴋᴏ ᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ чᴇᴄᴛи ᴏᴛᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй ᴇбᴧᴏʍ ᴧᴏʙи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴏᴩʙу ᴛᴇ ᴩуᴋи и буду ᴄᴇбᴇ ниʍи дᴩᴏчиᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄʙᴏиʍи ʙиᴄячиʍи ᴄиᴄьᴋᴀʍи дᴩᴏчиᴧᴀ дуᴩᴀ бᴧяᴛь ɜᴀхɜᴀᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴛᴀʙиᴧ ᴩʙᴀныᴇ ᴩᴀны нᴀ нᴏᴦᴀх ᴛʙᴏᴇй ʍᴀʍᴀɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏɯёᴧ и ʙыᴩубиᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴩуниɯᴋᴀ ᴋᴛᴏ ᴄᴩᴀᴧ нᴀ ᴛᴇбя ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ ᴩучᴋи ᴛᴏ дᴩᴏжᴀᴛ у ᴛᴇбя ᴨᴇᴩᴇд ʍᴏиʍ чᴧᴇнᴏʍ ᴩуᴄᴏᴄʙинья ᴛы ᴇбᴀнуᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯиɯь я ᴛᴇбᴇ ᴛуᴛ ᴨᴀᴧьцы буду ᴏᴛбиʙᴀᴛь ᴏдин ɜᴀ дᴩуᴦиʍ ɜᴀ ᴛᴏ чᴛᴏ ᴛы ᴛᴀᴋᴏй ʍᴇдᴧᴇнный ᴄынᴏᴋ ɯᴧюɯᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜ ᴨᴏᴄᴧᴇдних ᴄиᴧ ʙᴏюᴇɯь ᴄ ʍᴏиʍ хуᴇʍ ᴛуᴛ чᴇᴨухᴀ ᴨᴏɜᴏᴩнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏйнᴇ ᴛы ᴄ ʍᴏиʍ хуᴇʍ дᴩᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴄᴧиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀʙᴀй ᴄын ɯᴧюхи ᴄᴏбиᴩᴀйᴄя ᴄ ʍыᴄᴧяʍи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇʙᴀᴛᴇᴧь ᴨᴇниᴄᴏʙ ᴛы чᴏ ᴛуᴛ ʙᴄᴇʍ хуй ᴏᴛᴄᴀᴄыʙᴀᴇɯь ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴨидᴏᴩ жиᴩный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄунᴇц хуя ᴛы ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴀбᴇйɯий ᴄын ɯᴧюхи ᴏчниᴄь ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴨиɜды нᴇ дᴀᴧ ᴏᴨяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏʙнᴏ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍбуᴧу ᴛы ᴩᴛᴏʍ ɯᴧиɸᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄунᴇц хуᴇʙ хᴏхᴧᴏʙ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ʙ ᴦᴏᴧᴏʙу ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩᴏᴄʙин ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩыᴧᴏ ᴛᴇ ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴩᴀɜбиᴧ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩуᴄᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛᴇ хуй ʙ ᴩыᴧᴏ ᴄᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀч нᴀ хуй ʍᴏй нᴇ ᴨᴀдᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏʙцᴇᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ʙыʙᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴛᴀᴄᴋᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуᴇ ᴛы ᴋᴀᴛᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя биᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя дᴏбиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴛᴀниᴩᴏʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙɜᴏᴩʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴏʍбᴇɜнᴏ ᴨᴏᴇбᴀᴧ ᴛʙᴏю ʍᴀʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩᴏᴄᴄиянᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴩᴀɯиᴄᴛ ᴛы ʙᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь нᴀ ᴩуᴄᴄᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь будᴛᴏ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жуᴛь нᴀ ᴛᴇбя нᴀʙᴏдиᴛ ʍᴏй ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴏᴄᴄиянᴇц ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇᴧᴇɜнᴏбᴇᴛᴏннᴏ ᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴨᴏᴋᴀ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀхуй ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴋуᴄыʙᴀя ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴋᴩыʙᴀяᴄь ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуй ʍᴏй ᴛы нᴀᴨᴀᴧ и ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴀждᴏй ᴧᴀʙᴋᴇ ᴨᴀᴩᴋᴀ ᴛʙᴏю ʍᴀᴛь я ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇᴄᴏᴄ ᴩᴀɜбᴇй ᴦᴏᴧᴏʙу ᴄᴇбᴇ ᴏб ᴄᴛᴇнᴋу нᴀхуй ᴨᴏᴋᴀ я ɜᴀняᴛ ᴨᴏᴇбыʙᴀниᴇʍ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴛуᴨᴏᴦᴏᴧᴏʙᴏй ᴄын ɯᴧюхи ᴨᴇᴩᴇᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу ʙ ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴇдᴏᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀɯу ᴛʙᴏю чуᴩᴇᴋᴄᴋую ᴨᴏᴇбᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы иɜ чуᴩᴋᴏᴄᴛᴀнᴀ ᴄбᴇжᴀᴧ ᴦдᴇ ᴛᴇбя ʙ ɜᴀᴦᴏнᴇ дᴇᴩжᴀᴧи нᴀхуй ᴋᴀᴋ ᴄᴏбᴀᴋу диᴋую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> буᴩяᴛнᴏ ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы диᴋий ᴄын ɯᴧюхи ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴀ ᴛᴏ щяᴄ хуи нᴀᴧᴇᴛяᴛ ᴨᴩяʍ ʙ ᴩыᴧᴏ ᴛʙᴏё ᴛᴩᴀхᴀннᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ дᴏᴧᴦ ᴛы ʍнᴇ хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀᴛи ᴛы дᴩᴏчиᴧ ʍнᴇ ᴨᴩияᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴧᴀᴦᴏдᴀᴩиᴧ ᴛя чᴧᴇнᴏʍ ᴨᴏ ᴦубᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀщᴇᴋᴀнᴇц ᴇбᴧищᴇ ᴨᴩиᴋᴩᴏй ᴄʙᴏё ᴨᴩᴏᴛиʙнᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуи ᴨихᴀᴧи ᴛᴇ ʙ уɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇᴦᴏдня ᴛᴇбᴇ ᴦᴧᴀɜᴀ хуяʍи ʙыᴋᴏᴧяᴛ ᴄыниɯᴋᴇ ɯᴧюхи ᴛᴀᴋᴏʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ жидᴏᴄʙин ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴩᴏᴄᴄийᴄᴋᴀя хуᴇᴄᴏᴄᴀᴧᴋᴀ ɜᴀ ᴋᴏᴨᴇйᴋи ᴄᴏᴄёᴛ и ᴋиᴛᴀйцы ᴇё ᴄᴇбᴇ нᴀ нᴏчь бᴇᴩуᴛ ᴨᴏᴋᴀ ᴛы ᴄидиɯь и ждёɯь ᴇё 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏ ᴨᴩиʙычᴋᴇ уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ хуя будᴛᴏ ᴏᴛ ᴄᴨᴇᴩʍы ᴄʙᴏᴇᴦᴏ ᴏᴛцᴀ ᴀᴧᴋᴀɯᴀ ᴇбучᴇᴦᴏ бᴧя хᴀхᴀхᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴧиᴛᴇᴧьнᴏ ᴛы ʙыдᴇᴩжиʙᴀᴧ ᴄᴨᴇᴩʍу ʙ ᴦᴏᴩᴧᴇ ᴛᴏᴧьᴋᴏ нᴀхуя нᴇ ᴨᴏняᴧ я 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʙɜяᴧ ᴨᴇᴩᴇдыɯᴋу чᴛᴏбы нᴇ ᴄᴏᴄᴀᴛь хᴏᴛь ʍинуᴛу ᴄʙᴏᴇй жиɜни ᴋᴏᴛᴏᴩᴀя ᴋᴏнчиᴛᴄя ᴋᴏᴦдᴀ ᴛы ᴨᴩиᴇдᴇɯь ʙ Ꭹᴋᴩᴀину ʙᴏᴇʙᴀᴛь ʙᴇдь ᴛы ᴏʙцᴀ ᴄᴧᴀбᴀя ᴋᴏᴛᴏᴩᴏй ᴀнᴀᴧ ᴦᴩᴀнᴀᴛᴏй ᴩᴀɜᴏᴩʙуᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄʍᴇхᴀюᴄь нᴀд ᴛᴏбᴏй чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нищуᴦᴀн ᴛы ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏё ᴇбᴀᴧᴏ ᴄʙᴏᴇй ɜᴀᴧуᴨᴏй ᴄᴋᴩуᴛиᴧ ɯᴏб нᴇ ᴨиɜдᴇᴧ ʍнᴏᴦᴏ ɜᴀ ᴩᴏᴄᴄию ᴄʙᴏю ʙᴇᴧиᴋую ʙᴏ ʙᴄᴇ щᴇᴧи ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇ ᴨᴏ ᴦᴏᴧᴏʙᴇ нᴀᴄᴛучу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи чуᴩᴇᴋᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴋᴄᴛᴀ ᴨидᴏᴩᴀᴄ чуᴩᴋᴏᴄᴛᴀнᴏʙᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> униɜиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀхуяᴩю ᴛя хуᴇʍ ᴋᴀᴋ ᴏᴋᴋуᴨᴀнᴛᴀ будᴇɯь ᴏдниʍ ᴄ 200ᴋ дᴏхᴧых ᴩᴏᴄᴄиянᴄᴋих ᴄʙинᴏᴨᴄᴏʙ ᴀхɜᴨɜᴨɜᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙыᴩубиᴧ ᴛя хуᴇʍ ᴋᴀᴋ ᴋуʙᴀᴧдᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ʙᴏ ᴩᴛу щᴇᴋᴏᴛᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чё ᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨидᴏᴩᴀᴄня ᴩᴀᴄᴄиянᴄᴋᴀя хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴨьёʍ ᴛᴇбᴇ ᴦᴧᴀɜᴀ ᴋ хуяʍ ʙыᴋᴏᴧю дᴇбиᴧᴋᴇ ᴛᴩᴇхɜубᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ хуᴇц ᴄᴧюняʙиᴧ ɜᴀчᴇʍ хᴀчуᴩᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴧᴇни ᴛᴇ ᴨᴇᴩᴇᴧᴏʍᴀю нᴀхуй дуᴩᴇ ᴄᴧыɯиɯь ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ʍᴏй хуй ɜᴀ ᴄʙᴏᴇй ʍᴀʍᴏй дᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍ ᴛя бᴩᴏᴄиᴧ ʙ яʍу ᴦдᴇ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴄ ᴨᴏʍᴏщью хуя ᴛᴏᴧьᴋᴏ чᴛᴏ ɜᴀᴇбᴀɯиᴧ ɸᴀнᴀᴛᴏчᴋу ʙᴀᴦнᴇᴩᴏᴄʙинᴇй ᴄᴏᴄунцᴏʙ ʍᴏᴇᴦᴏ хуя ᴇбᴀнуᴛых нᴀ ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ᴛы нᴀ ʍᴏёʍ хуᴇ ᴋᴀᴋ нᴀ ʍᴏᴨᴇдᴇ ᴋᴀᴛᴀᴇɯьᴄя ᴇбᴀнᴀᴛиᴋ ᴄᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> быᴄᴛᴩᴏ ᴛы нᴀ чᴧᴇнᴇ ᴨᴏᴛух ᴄынᴏᴋ ɯᴧюхи ᴛуᴨᴏдᴏхᴏдящᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀнᴋиᴄᴛу ᴛы ᴄᴏᴄᴀᴧ чᴛᴏбы ᴏн ᴛʙᴏих ʙᴀᴦнᴇᴩᴏᴄʙинᴇй нᴇ ᴇбᴀɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя ᴋᴀᴋ ᴋᴀᴩᴀᴛᴇᴧь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴋᴀйɸу ᴛя ʙыᴇб 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀбыᴧ ᴋᴀᴋ ʍнᴇ ɜᴀᴧуᴨу бᴧᴀᴦᴏдᴀᴛную цᴇᴧᴏʙᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨущᴇнᴇц ᴏᴛъᴇбᴀнный ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛёᴧᴋᴀ ᴛы у ᴋᴏᴦᴏ ᴄᴏᴄᴀᴛь учиᴧᴀᴄь ᴏᴛʙᴇᴛ ʙ ɜᴀᴧуᴨу ᴏɸᴏᴩʍи ᴨᴏ ᴋᴀйɸу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴩᴇжу ᴛʙᴏю ᴦᴏᴧᴏʙу нᴀхуй ᴋᴀᴋ чᴇчᴇнᴇц 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜдᴇᴧᴀᴧᴄя ᴄ ᴛᴏбᴏй ᴋᴀᴋ ᴋᴩᴀᴋᴇн ᴄ ʙᴀᴦнᴇᴩᴏʍяᴄᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴀɸᴏᴄнᴏ ᴛы хуй ᴄᴏᴄᴀᴧ ᴏᴨᴏɜᴏᴩᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чё ᴇбᴀᴧᴏʍ ᴄʙᴏиʍ нᴀᴄᴏᴄᴀᴧ нᴀ ʍᴀɯину чᴛᴏ-ᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜᴏᴩʙи ᴄᴇбᴇ ᴩᴏᴛ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴀᴩиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴛь ᴛы ᴋᴀᴋ ᴄʙин жиᴩнющий ʍнᴇ хуй ᴄᴏᴄёɯь ᴨᴩяʍ диᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏɜᴏᴩищᴇ ᴋᴄᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄʍᴇиʙᴀюᴛ ᴛᴇбя, ᴀ ᴛы ᴛᴇᴩᴨиɯь чᴧᴇн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы дуᴩᴀ уᴄᴨᴏᴋᴏйᴄя ᴨᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы хуᴇᴄᴏᴄᴀᴧᴋᴀ нищᴀя ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄунуᴧ ᴛᴇ хуй ʙ ᴩыᴧᴏ, ᴛᴇᴩᴨи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴋ ᴄᴛᴇнᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя нᴇ ʍᴀᴧᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴛы ᴨᴩᴇᴋᴩᴀᴄнᴏ ʍᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴧᴀя ᴛы ɯᴀᴧᴀʙᴋᴀ хᴇхᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ʍнᴇ ɯᴋᴏᴧьниᴋ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ᴇбᴀнᴀя ɯᴀᴧᴀʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴇх ᴀᴧьɸᴀч ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴛᴀйᴄᴋᴀя ᴏᴛдᴀᴧᴀᴄь ɜᴀ нᴏн ᴄᴛᴏᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɜᴏᴩный уᴩᴏд ᴛы нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жиᴩный ᴋуᴄᴏᴋ ʙᴏнючᴇᴦᴏ дᴇᴩьʍᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй ʍинᴇᴛ ᴨᴏхᴏж нᴀ хуйню 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ чᴧᴇняᴩу ᴄᴏᴄᴇɯь ᴋᴀᴋ бᴇɯᴇный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄиᴧьный ᴏᴛᴄᴏᴄниᴋ ᴛᴀᴋ ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴀ ᴛы ᴋуᴄᴏᴋ ᴨᴏхᴏжᴇᴦᴏ нᴀ дᴇᴩьʍᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴏᴇд ᴇбᴀный ɜᴀᴋᴩᴏй ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ ᴛᴩᴀхᴀᴧ ᴛʙᴏй ᴀнᴀᴧ бич 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴄᴏᴄи чᴧᴇн ɸᴩиᴋᴏʙᴀᴛый ᴨᴇдиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄуᴋи ᴛы чᴇᴩнᴏʙᴀᴛᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇдᴩиᴧᴀ ᴛы ᴩᴀɜуᴋᴩᴀɯᴇнᴏᴇ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛы ʍнᴇ хуй ᴄᴏᴄᴇɯᴧ ᴛᴀᴋ чᴀᴄᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙ ʍнᴇ чᴧᴇн ᴄᴏᴄᴀᴧ ᴇʙᴩидᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄ ʍᴏиʍ чᴧᴇнᴏʍ ʍᴀɜᴏхиᴄᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇʙᴩᴇйᴄᴋᴀя нᴀᴛуᴩᴀ у ᴛᴇбя ᴄ чᴧᴇнᴀʍы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦниᴧью ᴏᴛ ᴛᴇбя ʙᴏняᴇᴛ ᴨᴇдᴀᴩᴀᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄᴀᴧ ʍнᴇ и нᴇ ᴛᴏᴧьᴋᴏ ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>ᴨᴏ ᴨᴩиᴋᴏᴧу ᴛᴇбя ᴛᴩᴀхᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>  ʙьᴇбᴀᴧ ᴛᴇбя чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ хуᴇʍ ʙ ᴩуᴋᴀх ᴛы ʍнᴇ ᴨиɜдиɯь чᴛᴏ-ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɯᴧюхᴀ ᴋᴏɜᴀцᴋᴀя ᴨᴀᴩᴇнᴇᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴋᴏᴧᴏ ɜᴀᴨᴏᴩᴏжᴄᴋᴏй ᴄичи ᴛы хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏц ниᴋ ᴨᴇниᴄᴏɸᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я хᴏчу ᴛʙᴏю ʍᴀᴛь ɯᴀᴧᴀʙу ᴛᴩᴀхᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛᴇᴋ ᴦᴇй ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄи чᴧᴇн уᴋᴩᴀинᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʙᴏй ɸᴀᴋᴇᴩ я дᴧя ᴛя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй ʍнᴇ чᴧᴇняᴩу ʍᴏнᴄᴛᴩ ᴋᴀʍᴏʙый 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбя нᴀ ʍᴏдуᴧях ʙыᴇбу ᴄᴧᴀб ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛиɯᴇ ᴄᴏᴄи ᴧᴏх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛя ᴋᴏɜᴇᴧ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴀᴄи ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴀᴧᴏ ᴛᴇбя ᴨуᴄᴛиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴧичный ᴄᴨᴇᴩʍᴏᴨᴩиᴇʍныᴋ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ 43 ᴦᴏду ᴛᴇбя ʙыᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛʙᴏй ᴇбыᴩь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ᴄᴧᴏн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴋᴀᴋ ᴇбᴀнуᴛый ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇбя ᴩᴀɜъᴇбᴀᴧ я чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ᴨᴀᴛᴧы ʙыᴩʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴦᴏᴧубя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɸᴀйᴄя ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи, ᴛᴇᴩᴨи ᴇᴄᴧи ᴛʙᴏй ᴏᴛᴇц ᴨидᴏᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀждᴏᴇ ᴛʙᴏё ᴄᴧᴏʙᴏ нижᴇ ϶ᴛᴏ хуи ᴧᴇᴛящиᴇ ʙ ᴄᴏᴄᴀᴧᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨᴇᴧᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ж ᴛя убью нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴏ ᴄын бᴧядины ᴛы иɜ ᴄᴇбя нихуя нᴇ ᴨᴩᴇдᴄᴛᴀʙᴧяᴇɯь бᴇᴩи ʍᴏᴇᴦᴏ хуя ʙ ᴩᴏᴛ ᴛᴇᴩᴨиᴧᴏид чё ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ ɜнᴀᴇɯь чᴛᴏ ʍᴀᴛь ᴛʙᴏю ʙ ᴦᴏᴩᴧᴏ ʙᴄᴇ ᴇбуᴛ нᴀᴄᴧᴇдниᴋ хуя ᴛы ʍᴏᴇᴦᴏ ᴧучɯᴇ ᴨᴏ хᴏᴩᴏɯᴇʍу ᴛᴇᴩяйᴄя ᴨᴏᴋᴀ ᴛʙᴏя ᴦᴧᴏᴛᴋᴀ цᴇᴧᴀ ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴇбᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴨᴧᴇжуй ᴛы чё ᴛуᴛ ᴩᴇɯиᴧ чᴛᴏ-ᴧи жᴀᴧᴏʙᴀᴛьᴄя чᴛᴏ ᴛᴇбя ʙ дыᴩы ᴛʙᴏи ᴇбуᴛ ᴨᴏᴋᴀ ᴛы хуй ᴄᴏᴄёɯь иᴧи чё ᴄᴧᴀбинᴀ нᴇʙьᴇбᴇннᴀя нᴀʙᴇᴩни ɜᴀᴧуᴨы ᴄʙинᴏᴩыᴧый ᴄын ɯᴧюхи ʙыᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴏᴛᴄᴏᴄᴀйдᴇᴩ ᴇбучий ᴛы чё нᴇ ᴏᴨᴩᴀʙдыʙᴀᴇɯь ᴄʙᴏй ʍинᴇᴛ ʍнᴇ, ᴛы чᴛᴏ-ᴧи ᴄчиᴛᴀᴇɯь чᴛᴏ ᴦᴧᴏᴛᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи дᴧя ᴩуᴄᴄᴋᴏᴦᴏ ϶ᴛᴏ чᴇᴄᴛь ᴩᴀɜ ᴛы ᴛᴀᴋ ᴨᴩиʙыᴋ жᴩᴀᴛь ᴨᴇниᴄы хᴏхᴧяᴛᴄᴋиᴇ? ᴩᴇщᴇ ᴛуᴛ ᴏᴨᴩᴀʙдᴀния ʙ хуй ᴏɸᴏᴩʍи ᴄынᴏᴋ ɯᴧюɯᴇчᴋи нᴇʙᴏᴄᴨиᴛᴀнный ᴇбᴀᴧ жᴇ ᴛя ʙ ᴦᴏᴩᴧᴏʙину ᴛʙᴏю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀ я ᴨᴏᴋᴀ ᴛᴇбᴇ нᴀ ᴋᴧыᴋ нᴀᴋидыʙᴀᴧ ᴛы ʍнᴇ ᴨᴀᴧьчиᴋᴀʍи ᴀнᴀᴧ хᴏᴛᴇᴧ ʙычиᴄᴛиᴛь ᴛᴀᴋ ʙᴏᴛ я ɜᴀᴄᴛᴀʙиᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋуу ᴇё яɜыᴋᴏʍ ʍнᴇ жᴏᴨу ᴧиɜᴀᴛь ибᴏ у ᴛᴇбя ϶ᴛᴏ нᴇ ᴏᴄᴏбᴏ хᴏᴩᴏɯᴏ ʙыхᴏдиᴧᴏ ᴨᴏᴛᴏʍу чᴛᴏ ᴛы ᴨᴏ бᴏᴧьɯᴇй чᴀᴄᴛи ᴧиɯь хуи ᴦᴧᴏᴛᴀᴛь ᴄᴨᴏᴄᴏбᴇн ᴩуᴄᴏᴄʙинᴄᴋий ᴄынᴏᴋ ɜᴇᴧьᴇʙᴀᴩᴋи нᴇ бᴏйᴄя ʍᴇня ᴛуᴛ ᴨᴏᴋᴀ я ᴛя ᴨᴇниᴄᴏʍ бью ᴛы жᴇ ᴋᴀйɸᴏʙᴀᴧ ʙᴄᴇᴦдᴀ ᴏᴛ ϶ᴛᴏᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ужᴇ ʙᴄᴇʍ ᴨᴩиɜнᴀᴛьᴄя дᴏᴧжᴇн чᴛᴏ ᴛы хуя ʍᴏᴇᴦᴏ ɸᴀнᴀᴛᴋᴀ и ᴋᴀждый ʙᴇчᴇᴩ ʍᴏᴇй ɜᴀᴧуᴨᴇ ᴨᴏᴋᴧᴏняᴇɯьᴄя ᴋᴀᴋ будᴛᴏ бᴏᴦᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи уᴄᴋᴏᴦᴧᴀɜый жиʙущий ʙ буᴩяᴛии нᴀɜыʙᴀᴧ ᴄᴇбя ᴩуᴄᴄᴋиʍ ᴨᴏᴋᴀ хуину ʍᴏю ɯᴧиɸᴏʙᴀᴧ ɯᴧюхи ᴛы ᴄынᴏᴋ ᴨᴏᴋᴀ уж ᴛᴇбᴇ ɜубы хуᴇʍ ʙыбиᴛь чᴛᴏбы ᴛы ᴋᴏ ʙᴄᴇʍу ᴇщё и ɯыᴨиᴧяʙиᴧ уᴩᴏдᴇц ʙыᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙнᴀᴛуᴩᴇ жᴇ ᴛᴇбя ᴄᴇйчᴀᴄ ᴄынᴋᴀ бᴧяди хуᴇʍ чᴇᴄᴛи иɜбᴀʙᴧю 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧё ᴄын ɯᴀᴧᴀʙы уᴩᴏдᴧиʙый хуяᴩу ʍᴏю нᴀᴄᴀᴄыʙᴀй инᴀчᴇ ᴛᴇ ϶ᴛᴀ хуяᴩᴀ ᴨᴏ ᴧбу ᴄᴇйчᴀᴄ ᴄᴛучᴀᴛь нᴀчнᴇᴛ и ᴛʙᴏи нᴇ ᴩᴀбᴏчиᴇ ʍᴏɜᴦи ᴨᴏᴧуᴄᴦниʙɯиᴇ ᴨᴩᴏᴄᴛᴏ нᴀᴦᴧухᴏ ʙыбьᴇᴛ бᴇɜ ʙᴏɜʍᴏжнᴏᴄᴛи ʙᴏᴄᴄᴛᴀнᴏʙᴧᴇния ᴛы нᴀʙᴄᴇᴦдᴀ ᴛуᴨыʍ ᴄынᴋᴏʍ ɯᴀᴧᴀɯᴏʙᴋи ᴏᴄᴛᴀнᴇɯьᴄя и нихуя нᴇ ᴨᴏʍᴏжᴇᴛ ᴛᴇбᴇ, ᴀ ϶ᴛᴏ ʙᴄё ᴧиɯь ᴨᴏᴛᴏʍу чᴛᴏ ᴛы нᴀ ʍᴏй чᴧᴇн ᴩыᴨнуᴧᴄя ᴨуᴛᴧᴇᴩᴄᴋий нᴀᴄᴏᴄниᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын дᴀʙᴀᴧᴋи ᴇᴄᴧи ᴄᴧыɯиɯь ʍᴇня ᴨᴩᴏʍᴏᴧчи ᴇᴄᴧи ᴄᴏᴦᴧᴀᴄᴇн ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ ᴏᴛдᴇɸᴀᴛьᴄя ᴨыᴛᴀйᴄя нᴏ я жᴇ ɜнᴀю чᴛᴏ нᴀ хуи уᴋᴩᴀинᴄᴋиᴇ ᴛы ᴨᴀдᴏᴋ и ᴄᴇйчᴀᴄ у нᴏᴦ ʍᴏих уʍᴏᴧяᴛь будᴇɯь чᴛᴏбы ʍᴏй ᴨᴇниᴄ ʙ ᴛʙᴏёʍ ᴩᴏᴛиᴋᴇ ɯᴇʙᴇᴧиᴧᴄя ᴄᴏ ᴄᴋᴏᴩᴏᴄᴛью ёбᴧи ᴄ ᴛʙᴏᴇй ʍᴀᴛᴇᴩью ᴛуᴨᴏᴦᴏᴧᴏʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶у хуᴇᴛᴇнь ᴄᴧᴀбᴇйɯᴀя нᴇ ʙɜдуʍᴀй ᴛᴇᴩᴨᴇᴛь ᴛᴏᴛ ɸᴀᴋᴛᴏᴩ чᴛᴏ ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ʍнᴇ ɜᴀ 200 ᴦᴩиʙᴇн ᴏᴛдᴀᴧᴀᴄь и ᴩᴀɜᴩᴇɯиᴧᴀ ʍнᴇ ᴄ нᴇй чᴛᴏ уᴦᴏднᴏ дᴇᴧᴀᴛь дᴀжᴇ ᴇю ɜᴀᴧуᴨᴏй ᴨᴏʙᴇᴧᴇʙᴀᴛь, ᴀ ɜᴀ 300 ᴦᴩиʙᴇн ᴏнᴀ ʙᴀщᴇ будᴇᴛ ᴧᴇжᴀᴛь нᴀ ᴄᴨинᴋᴇ и яйцᴀ ʍᴏи ᴧиɜᴀᴛь ну и ɯᴀᴧᴀɯᴏʙᴋᴀ ᴋᴏнᴋᴩᴇᴛнᴀя у ᴛя ʍᴀɜᴇᴩ я бы ᴇй ᴋиᴩᴨичᴏʍ ᴇбᴀᴧьниᴋ ᴄᴧᴏʍᴀᴧ нᴏ ᴨᴏдуʍᴀᴧ чᴇʍ ᴏнᴀ ᴨᴏᴄᴧᴇ ϶ᴛᴏᴦᴏ ɜᴀᴩᴀбᴀᴛыʙᴀᴛь ᴛᴏ будᴇᴛ и ᴨᴏжᴀᴧᴇᴧ ᴛʙᴏю ʍᴀᴛь ɯᴧюху ᴛуᴨᴏᴩᴏᴦую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы нᴇдᴏᴩᴀɜʙиᴛыʍ ᴩᴏдиᴧᴄя ᴨᴏᴛᴏʍу чᴛᴏ ᴨᴏᴋᴀ ᴛʙᴏя ʍᴀʍᴀɯᴋᴀ быᴧᴀ ᴛᴏбᴏю бᴇᴩᴇʍᴇннᴀя я ᴇй ᴨᴩᴏᴄᴛᴏ ᴄ дʙух нᴏᴦ нᴀхуй ʙ жиʙᴏᴛ ʙᴧᴇᴛᴀᴧ и ɜᴀᴄᴛᴀʙᴧяᴧ ᴇё ᴄᴏᴄᴀᴛь ʍнᴇ, ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴄʙᴏᴇй ɜдᴏᴩᴏʙᴇннᴏй ɜᴀᴧуᴨᴏй хуяᴩиᴧ ᴇй ᴨᴏ бᴏɯᴋᴇ ᴏᴛ чᴇᴦᴏ ᴇё ʍᴏɜᴦ быᴧ ᴛᴏᴛᴀᴧьнᴏ ᴨᴏʙᴩᴇждён ᴋᴀᴋ ᴛʙᴏй ᴩᴏᴛ ᴏᴛ ʍᴏᴇᴦᴏ хуя ᴄᴇйчᴀᴄ и ᴨᴏ иᴛᴏᴦу ᴏнᴀ нᴀ ʙᴄю жиɜнь ᴏʙᴏщᴇʍ ᴏᴄᴛᴀᴧᴀᴄь и я ᴇё ʙᴛихᴀᴩя нᴀʙᴇщᴀᴧ и ᴩᴇɜинᴏʙый ᴨᴇниᴄ ɜᴀ щᴇᴋу ᴇй ᴄᴏʙᴀᴧ ᴨᴏᴋᴀ ᴏнᴀ хᴏᴛᴇᴧᴀ ᴏᴛбиᴛьᴄя ᴏᴛ ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛ хуя ʍᴏᴇᴦᴏ ʙ ᴨиɜдᴇ ᴄʙᴏᴇй ʍᴀʍᴋи нᴇ ᴨᴩячьᴄя ᴛᴏ ɜᴀᴄᴄыᴋᴀнный ᴄыниɯᴋᴀ бᴧядины я ᴛᴇбя ᴨᴏжᴀᴧᴇю ᴇᴄᴧи ʍнᴇ ᴇщё ᴨᴀᴩу ᴩᴀɜ дᴀɯь ᴄʙᴏи иᴄᴨᴏᴧьɜᴏʙᴀнныᴇ ᴦубᴇɯᴋи чᴛᴏбы я ʍᴏᴦ ниʍи ᴛᴏᴩᴦᴏʙᴀᴛь ᴋᴀᴋ хᴀч ᴨᴏʍидᴏᴩᴀʍи нᴀ бᴀɜᴀᴩᴇ нᴏ ʙ ʍᴏёʍ ᴄᴧучᴀᴇ ϶ᴛᴏ будᴇᴛ ᴨᴩиᴛᴏн ʙ ᴋᴏᴛᴏᴩᴏʍ будуᴛ ᴛʙᴏи ᴦубы иᴄᴨᴏᴧьɜᴏʙᴀᴛь дᴧя ᴛᴇᴄᴛᴀ ʍᴀᴋᴄиʍᴀᴧьнᴏй дᴏɜы нᴀᴩᴋᴏ ᴨᴏᴄᴧᴇ ᴋᴏᴛᴏᴩᴏй чᴇᴧᴏʙᴇᴋ уʍᴩᴇᴛ нᴏ ᴨᴩᴧбᴧᴇʍᴀ ᴛᴏ ʙ ᴛᴏʍ чᴛᴏ ϶ᴛи ᴛᴇᴄᴛы нᴇ ᴨᴩинᴇᴄуᴛ ᴨᴏᴧьɜы ибᴏ ᴛы ᴄʙиннᴏᴩыᴧый ᴄын ɯᴧюхи и нᴀ ᴨᴏᴧᴏʙину ᴨёᴄ цᴇᴨнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ɜᴀ щᴇᴋу ужᴇ уᴄᴛᴀᴧ нᴀᴋидыʙᴀᴛь бᴧя ᴄᴛяни ᴇбᴧищᴇ ᴄʙᴏё чᴛᴏбы я нᴇ ᴩᴀᴄᴛᴇᴦнуᴧ ɯиᴩинᴋу и нᴇ дᴀᴧ ᴛᴇбᴇ ᴨᴏ ᴦубᴀʍ хуйцᴇʍ ᴄнᴏʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏйди ᴋᴏ ʍнᴇ ᴏᴛᴄᴏᴄный ᴄʙинᴏᴩуᴄ я ᴛᴇбᴇ дᴀʍ хуя ᴄʙᴏᴇᴦᴏ ᴨᴏᴨᴩᴏбᴏʙᴀᴛь нᴀ ʙᴋуᴄ ʍᴏжᴇᴛ ᴛᴇбᴇ ʍᴏй чᴧᴇн ᴨᴏнᴩᴀʙиᴛᴄя ᴋᴀᴋ ʍᴀʍᴀɯᴇ ᴛʙᴏᴇй ᴋᴏᴛᴏᴩᴀя ᴩᴛᴏʍ ᴄ хуя ужᴇ ᴋᴏᴛᴏᴩый дᴇнь нᴇ ᴄᴧᴇɜᴀᴇᴛ, дуʍᴀю у ʙᴀᴄ ϶ᴛᴏ ᴄᴇʍᴇйнᴏᴇ ᴄᴏᴄᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи хɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ у ʙᴀᴄ ʙ ᴄᴇʍьᴇ ᴨᴩиняᴛᴏ у уᴋᴩᴀинцᴇʙ ʙ нᴏᴦи ᴨᴩиᴨᴀдᴀᴛь и ᴋ хую ᴄʙᴏᴇй ᴨᴀᴄᴛью ᴛянуᴛᴄя? я ᴨᴩᴏᴄᴛᴏ ниᴋᴀᴋ нᴇ ʍᴏᴦу ᴨᴏняᴛь ᴋᴀᴋᴏᴦᴏ хуя ᴛы ᴄын ɯᴧюхи ɜᴀ ʍᴀᴛᴇᴩью ᴄʙᴏᴇй ᴨᴏʙᴛᴏᴩяᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄынᴋу ɯᴀᴧᴀʙы ᴛᴇ нᴏᴦи ᴩᴀᴄхуяᴩиʍ ʙ ʍяᴄᴏ ɜᴀ ᴛᴏ чᴛᴏ ᴛы уᴄᴄыᴋᴀнный ᴨидᴀᴩᴀᴄ ᴏᴛ ʍᴏᴇй ɜᴀᴧуᴨы бᴇᴦᴀᴇɯь ᴧᴏɯᴏᴋ жᴀᴧᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯь ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴛы чё ᴛуᴛ удуʍᴀᴧ ᴄᴛᴇᴩᴨᴇᴛь ʍᴏи ᴄᴏᴏбщᴇния чᴛᴏ-ᴧи бᴇᴩи хуя нᴀʙᴇᴩни и ᴏᴛᴨᴏᴩ ᴏᴩᴦᴀниɜуй ᴛᴇᴩᴨиᴧᴏиднᴏᴇ ᴨᴏᴄʍᴇɯищᴇ ᴛя ᴛуᴛ ʙᴄё ʙ хᴀᴩю ᴇбуᴛ ᴨᴏᴋᴀ ᴛы ᴛᴇᴩᴨиɯь и ᴇщё бᴏᴧьɯᴇ ᴨᴏɜᴏᴩиɯьᴄя ну дᴀʙᴀй бᴧяᴛь хᴏᴛь хуй ᴏᴛбᴇй ʍᴏй нᴇдᴇᴇᴄᴨᴏᴄᴏбный ᴩᴇбёнᴏᴋ ᴨᴩᴏᴄᴛиᴛуᴛᴋи ᴏᴨущᴇнный чиᴄᴛᴏ ʍнᴏю и ᴋᴀждыʍ ᴋᴛᴏ ᴛᴇбᴇ ʙ ᴇбᴀᴧᴏ хᴀᴩᴋᴀᴧ ᴨᴏᴋᴀ ᴛы ᴛᴀᴋ жᴇ ᴛᴇᴩᴨᴇᴧ нᴀхуй ᴨᴩᴏбᴧядинᴏɜᴀᴧуᴨинᴄᴋий ᴋᴀждыʍ ɜᴀᴄʍᴇянный ᴨᴀᴩᴀɯниᴋ бᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀхуᴇᴛь ʍнᴇ ᴋᴀжᴇᴛᴄя ᴛы ᴨᴇᴩʙый ᴋᴛᴏ ɜᴀᴧуᴨᴇнь ᴛᴀᴋ яᴩᴏᴄᴛнᴏ нᴀᴄᴀᴄыʙᴀᴇᴛ ɜнᴀя чᴛᴏ ᴏᴨᴨᴏнᴇнᴛ уᴋᴩᴀинᴇц ну дᴀʙᴀй ᴇщё ᴨᴀᴩу ʍинуᴛ нᴀᴄᴧᴀждᴀйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴛᴏᴨᴏᴩᴏʍ ᴇбᴧᴇᴛ нᴇ уᴇбᴀɯиᴧ ᴛʙᴏй ᴋᴩиʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀɯуᴦᴀнный ᴄын ɯᴀᴧᴀʙы ᴄᴏбᴇᴩиᴄь ᴄ ᴄиᴧᴀʍи и ᴏᴛ хуя ʍᴏᴇᴦᴏ ᴏᴛбᴇйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴋᴏᴧᴇни нᴇ ᴨᴇᴩᴇᴧᴏʍᴀᴧ ᴛᴩёхɜубᴏʍу ᴨидᴏᴩу ᴋᴏᴛᴏᴩый ʍнᴇ хуй ᴨᴩиᴋуᴄыʙᴀя нᴀᴄᴀᴄыʙᴀᴇᴛ ᴀ ну ᴋᴀ ᴋᴧᴏунич дᴀʙᴀй ᴛы ᴨᴏᴛᴇᴩᴨиɯь чᴧᴇн ᴨᴏᴋᴀ я ᴛᴇбя нᴇ ᴏᴛᴨиɜдᴏɯиᴧ ᴀᴩʍᴀᴛуᴩᴏй ᴋᴀᴋ ᴛʙᴏю бᴀбᴋу ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴩᴏᴄᴛᴏ нᴀ ʍᴇᴄᴛᴇ ᴨᴏʍᴇᴩᴧᴀ нᴇ дᴏᴄᴏᴄя ʍнᴇ хуяᴩу ᴀ нᴀ ɜᴀʍᴇну ᴨᴩибᴇжᴀᴧᴀ ᴛʙᴏя ᴦᴏᴧᴀя ʍᴀʍᴀɯᴀ ɯᴀᴧᴀʙᴀ чᴇᴩнᴏʍᴀɜᴀя ᴋᴏᴛᴏᴩᴀя ʙᴄᴇᴦдᴀ хᴏхᴧᴀʍ ᴏбᴄᴀᴄыʙᴀᴧᴀ чᴧᴇны бᴇɜ ᴏᴄᴛᴀнᴏʙᴏᴋ нᴀ ᴏᴛдых и дᴇᴧᴀᴧᴀ ϶ᴛᴏ ᴏᴨыᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ ʙ ᴋуᴩᴄᴇ ɜнᴀᴧ ᴧи ᴛы нᴏ ᴏᴛᴄюдᴀ ᴛы ᴄ цᴇᴧыʍ ᴇбᴀᴧьниᴋᴏʍ нᴇ ʙыйдᴇɯь ʙᴇдь я ᴛᴇбᴇ ᴇᴦᴏ ʍᴏᴧᴏᴛᴋᴏʍ ᴏᴛᴏбью ɜᴀ ᴛᴏ чᴛᴏ ᴛᴇᴩᴨиɯь ᴛᴀᴋ ᴨᴇниᴄ и ᴛы будᴇɯь ʍяᴄᴏʍ бᴇᴄᴨᴏᴧᴇɜныʍ ᴏб ᴋᴏᴛᴏᴩᴏᴇ нᴏᴦи дᴀжᴇ ʙыᴛиᴩᴀᴛь нᴇ будуᴛ ибᴏ ᴛʙᴏй ᴇбᴧᴇᴛ быᴧ ᴨᴩи жиɜни нᴀᴄᴛᴏᴧьᴋᴏ ᴦᴩяɜныʍ чᴛᴏ ᴇᴦᴏ ᴄᴏ ᴄᴩᴀᴋᴏй ᴨуᴛᴀᴧи и ᴛудᴀ хуи ᴨихᴀᴧи ᴨᴩᴏᴄᴛᴛ нᴀхуй ᴋᴀждый ʙᴄᴛᴩᴇчный ᴛᴇбᴇ чᴇᴧᴏʙᴇᴋ ᴛᴇбᴇ хуй ʙ ᴩᴏᴛ нᴀᴄᴏʙыʙᴀᴧ ᴨᴏᴋᴀ ᴛы ᴄ удᴏʙᴏᴧьᴄᴛʙиᴇʍ ᴛᴇᴩᴨᴇᴧ ᴋᴀᴋ и ᴄᴇйчᴀᴄ ϶ᴛᴏ дᴇᴧᴀᴇɯь ᴨᴏᴋᴀ ᴛя ᴇбуᴛ хᴏхᴧᴏᴄᴛᴀнцы бᴧя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй ᴛᴇᴦни ʍᴇня ᴇᴄᴧи ᴛы ᴄᴏᴄᴀᴧ хуи ʙᴄю ᴄʙᴏю ᴏᴄᴏɜнᴀнную жиɜнь, ᴏᴛʙᴇᴛь нᴀ ᴧюбᴏᴇ ʍᴏё ᴄᴏᴏбщᴇниᴇ ᴇᴄᴧи ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ᴄ ᴩᴏждᴇния нᴀ хуи ᴋидᴀᴧᴀᴄь бᴇɜ ᴨᴧᴀᴛы нᴀ ϶ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я буду яᴄнᴏ и ᴋᴩᴀᴛᴋᴏ ᴛᴇбᴇ ᴋᴀждый ᴩᴀɜ ᴏбъяᴄняᴛь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴨᴩᴏᴄᴛиᴛуᴛᴋᴀ дᴇɯёʙᴀя ʍнᴇ хуй ᴨᴏᴄᴀᴄыʙᴀᴧᴀ бᴇɜ ᴨᴩичины нᴀ ϶ᴛᴏ ну чиᴄᴛᴀя ɯᴀᴧᴀʙᴀ ᴨᴩᴏᴄᴛᴏ ᴛᴀᴋих ᴇщё ᴨᴏиᴄᴋᴀᴛь нᴀдᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶й ᴦниᴧᴏɜубый ᴄын ɯᴧюхи ᴏᴛɜᴏʙиᴄь ᴨᴧᴀчᴇʍ ᴋᴏᴛᴏᴩый ни нᴀ ᴄᴇᴋунду нᴇ уᴛихᴀᴇᴛ дᴀжᴇ чиᴛᴀя ϶ᴛᴏ ᴛы ᴨᴧᴀчᴇɯь и ʙ ᴀхуᴇ ᴄидиɯь ᴋᴀᴋ жᴇ я ϶ᴛᴏ уᴦᴀдᴀᴧ, нᴏ я жᴇ ᴛᴇбᴇ ᴄᴇйчᴀᴄ ʙ ᴛʙᴏё ᴄʙинᴏᴩыᴧᴏ хуй ᴨихᴀю и ᴄᴧыɯу ᴋᴀждᴏᴇ ᴛʙᴏё ʙᴄхᴧиᴨыʙᴀниᴇ ᴋᴀᴋ ᴄучᴇчᴋᴀ ᴛы нᴏᴇɯь ʙ ᴨᴇниᴄ ᴨᴏᴋᴀ нᴀд ᴛᴏбᴏй нᴀᴄʍᴇхᴀᴇᴛᴄя ᴛᴏᴧᴨᴀ ᴛʙᴏих ᴇбыᴩᴇй ᴏᴛ ᴋᴏᴛᴏᴩых ᴛы дᴀжᴇ нᴇ ʙ ᴄиᴧᴀх ᴏᴛбиʙᴀᴛьᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏᴋᴀ чᴛᴏ нᴇ ᴀнниᴧиᴦиᴩᴏʙᴀн ʍᴏиʍ чᴧᴇнᴏʍ ᴄынᴏчᴇᴋ ᴩуᴄᴏᴄʙинᴄᴋᴏй хуᴇᴄᴏᴄᴀᴧᴋи нищᴇнᴄᴋᴏй ᴋᴏᴛᴏᴩый ʍнᴇ ᴛуᴛ хуя нᴀᴛᴏчиᴛ яɜыᴋᴏʍ ᴄʙᴏиʍ ᴨᴏᴋᴀ я ᴛʙᴏю ʍᴀʍᴀɯу ʙ уᴦᴧу ᴋᴀᴋ ᴄʙинью ᴇбᴀную ɜᴀбью ɯᴧюху ᴛᴀᴋую ᴨуᴛиниᴄᴛᴄᴋую дᴀʙᴀй ᴛᴇᴨᴇᴩь ᴨᴏ ᴨᴏᴩядᴋу ᴨᴩᴏйдᴇʍᴄя, ᴛᴀᴋ ʙᴏᴛ, я ᴇбᴀᴧ ᴛʙᴏю жиᴩную ʍᴀʍᴀɯу ᴨᴏᴋᴀ ᴛʙᴏй ᴏᴛᴇц иᴄᴛᴇᴋᴀᴧ ᴋᴩᴏʙью ᴏᴛ ᴦᴩᴀнᴀᴛы ᴄбᴩᴏɯᴇнᴏй ᴄ уᴋᴩᴀинᴄᴋᴏᴦᴏ дᴩᴏнᴀ нᴀ ᴋᴏᴛᴏᴩый нᴀᴄᴏᴄᴀᴧᴀ ʍᴀᴛухᴀ ᴛʙᴏя и ᴏᴛдᴀʙɯи дᴇньᴦи ᴨᴏд нᴀᴨᴏᴩᴏʍ хуя ʍᴏᴇᴦᴏ ʙᴇдь дᴏбᴩᴏʙᴏᴧьнᴏᴄᴛи ᴏᴛ нᴇё ʍᴏжнᴏ яʙнᴏ нᴇ ждᴀᴛь и ʍᴏжнᴏ ᴧиɯь ᴇё ɜᴀᴄᴛᴀʙиᴛь ᴨᴇниᴄᴏʍ ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴏᴄᴧуɯнᴏ будᴇᴛ ᴨᴩиᴋᴀɜы иᴄᴨᴏᴧняᴛь ᴋᴀᴋ ᴄучᴋᴀ нᴀ ʙᴄю ᴦᴏᴧᴏʙу ᴏᴛбиᴛᴀя уᴋᴩᴀинᴄᴋиʍи чᴧᴇнᴀʍи хᴇхᴇ 𓆩ꏢ𓆪"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(wablon))
            await sleep(0.1)
            await sleep(time)


    async def client_ready(self, client, db):
        self.db = db

    async def rwonlinecmd(self, message):
        """включить вечный онлайн"""
        if not self.db.get("Eternal Online", "status"):
            self.db.set("Eternal Online", "status", True)
            await message.edit("<b>Вечный онлайн включен</b>")
            while self.db.get("Eternal Online", "status"):
                msg = await message.client.send_message(
                    "me", "тгк @killrussians"
                )
                await msg.delete()
                await sleep(1000)

        else:
            self.db.set("Eternal Online", "status", False)
            await message.edit("<b>Вечный онлайн выключен</b>")

    async def watcher(self, message):
        if self.db.get("Eternal Online", "status"):
            await message.client.send_read_acknowledge(
                message.chat_id, clear_mentions=True
            )


    async def rwcmd(self, message):
        """[задержка в секундах] [шапка]"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "ⱀѧҁπџӡđѳⱀѧҁџʌ ϯʙѳё ҁʙџʜѳⱀƀӀʌѳ ѣʌᴙđҁκѳє")
            return
        await utils.answer(
            message,
            "ҁƀӀʜџѱє ⱀƴҁѳҁʙџʜҁκѳӣ πѧđѧʌџ ѣєґџ",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shablon))
            await sleep(0.1)
            await sleep(time)


    async def rwhelpcmd(self, message):
        """запускает renewal help"""
        args = utils.get_args_raw(message)
        await message.edit("Ꮢ")
        await message.edit("ᏒᎬ")
        await message.edit("ᏒᎬN")
        await message.edit("ᏒᎬNᎬ")
        await message.edit("ᏒᎬNᎬᎳ")
        await message.edit("ᏒᎬNᎬᎳᎪ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲Ꮋ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬᏞ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬᏞᏢ")
        await message.edit("⁣<emoji document_id=5411397985365927767>🇦🇲</emoji>")
        await message.edit("⁣<emoji document_id=5411397985365927767>🇦🇲</emoji><emoji document_id=5411397985365927767>🇦🇲</emoji>")
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("loading"))
        await message.delete()
        media_files = ("https://te.legra.ph/file/5d39bebbbef6f967c673b.mp4", "https://te.legra.ph/file/7939a8225e4d0401be0e3.mp4", "https://te.legra.ph/file/e8b6d04a3fb72a46be610.mp4", "https://te.legra.ph/file/42b282d0aa8e28d1f9f0d.mp4")
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

            user_info = ("❲࿕❳ ᏒᎬNᎬᎳᎪᏞϟϟᎻᎬᏞᏢ 𓆩ꏢ𓆪\nʍᴏдуᴧи хᴇᴧᴨᴀ ↓↓↓\n\n\n𓆩ꏢ𓆪 <code>.rage</code> - запускает модуль ᏌᏦᏒᎪᏆNᏆᎪN ᏒᎪᏀᎬ\n𓆩ꏢ𓆪 <code>.rwrage</code> - запускает календарь модуль ᏌᏦᏒᎪᏆNᏆᎪN ᏒᎪᏀᎬ\n𓆩ꏢ𓆪 <code>.rw</code> - запускает модуль ᏒᎬNᎬᎳᎪᏞ\n𓆩ꏢ𓆪 <code>.rwonline</code> - включает вечный онлайн\n𓆩ꏢ𓆪 <code>.rwtyper</code> - включает ложный тайп\n𓆩ꏢ𓆪 <code>.rwchatid</code> - узнаёт айди чата\n𓆩ꏢ𓆪 <code>.rwhour</code> - включает тайп на час\n\n𓆩ꏢ𓆪 модуль АФК (с фото):\n├ <code>.rwafk</code> - включает АФК режим\n├ <code>.rwafkoff</code> - выключает АФК режим\n├ <code>.rwrsn</code> - причина АФК\n└ <code>.rwafkf</code> - фото для АФК\n\n𓆩ꏢ𓆪 модуль автоответчик:\n├ <code>.rwansd</code> - скачивание текстового файла\n├ <code>.rwanstxt</code> - установка текстового файла\n├ <code>.rwansz</code> - задержка в секундах\n├ <code>.rwanss</code> - установка шапки\n└ <code>.rwans</code> - переключает режим работы [on/off]\n\n𓆩ꏢ𓆪 модуль тэггер:\n├ <code>.rwtag</code> - запускает синий тэггер\n├ <code>.rwtag1</code> - запускает фиолетовый тэггер\n├ <code>.rwtag2</code> - запускает красный тэггер\n├ <code>.rwtag3</code> - запускает жёлтый тэггер\n├ <code>.rwtag4</code> - запускает белый тэггер\n├ <code>.rwsh</code> - устаналивает шапку тэггера\n├ <code>.rwstop</code> - останавливает тэггер\n└ <code>.rwid</code> - узнаёт айди аккаунта\n\n𓆩ꏢ𓆪  модуль медиа-тэггер:\n├ <code>.rwtagm</code> - запускает синий медиа-тэггер\n├ <code>.rwtagm1</code> - запускает фиолетовый медиа-тэггер\n├ <code>.rwtagm2</code> - запускает красный медиа-тэггер\n├ <code>.rwtagm3</code> - запускает жёлтый медиа-тэггер\n├ <code>.rwtagm4</code> - запускает белый медиа-тэггер\n└ <code>.rwstopm</code> - останавливает медиа-тэггер\n\n𓆩ꏢ𓆪 модуль календарь-тэггер:\n├ <code>.rwkal</code> - запускает синий календарь-тэггер\n├ <code>.rwkal1</code> - запускает фиолетовый календарь-тэггер\n├ <code>.rwkal2</code> - запускает красный календарь-тэггер\n├ <code>.rwkal3</code> - запускает жёлтый календарь-тэггер\n├ <code>.rwkal4</code> - запускает белый календарь-тэггер\n\n𓆩ꏢ𓆪 модуль медиакалендарь-тэггер:\n├ <code>.rwkalm</code> - запускает синий медиакалендарь-тэггер\n├ <code>.rwkalm1</code> - запускает фиолетовый медиакалендарь-тэггер\n├ <code>.rwkalm2</code> - запускает красный медиакалендарь-тэггер\n├ <code>.rwkalm3</code> - запускает жёлтый медиакалендарь-тэггер\n├ <code>.rwkaml4</code> - запускает белый медиакалендарь-тэггер\n\n𓆩ꏢ𓆪 модуль для текстовых файлов\n├ <code>.rwused</code> - скачивает текстовик\n└ <code>.rwuse</code> - использует текстовик\n\n"
            f"<i>ᏌᏚᎬᏒNᎪᎷᎬ:</i> @{user_ent.username or '☠️'}\n"
            f"<i>NᏆᏟᏦNᎪᎷᎬ:</i> <code>{user_ent.first_name or '🚫'}</code>\n"
            f"<i>ᏌᏚᎬᏒ ᏆᎠ:</i> <code>{user_ent.id}</code>\n"
            f"ᎷᏫᎠᏌᏞᎬ ᎠᎬᏙᎬᏞᏫᏢᎬᏒ: @killrussians"
        )

        chat_id = message.chat.id
        if chat_id:
               await self.client.send_file(message.peer_id, random.choice(media_files), caption=user_info)


    async def rwtagmcmd(self, message):
        '''[id] [задержка в секундах] [ссылка на медиа]'''
        args = utils.get_args(message)
        message = await utils.answer(message, self.strings("load"))
        global state1
        state1 = True
        await message.delete()
        user_id = int(args[0])
        if args:
            time = float(args[1])
        while state1:
            text = random.choice(shablon)
            chat_id = message.chat.id
            if chat_id:
                ph = args[2]
                ph1 = f"{ph}"
                await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem}<a href='tg://user?id={user_id}'>{text}</a>{prem2}")
                await sleep(0.1)
                await sleep(time)


    async def rwtagm1cmd(self, message):
        '''[id] [задержка в секундах] [ссылка на медиа]'''
        args = utils.get_args(message)
        message = await utils.answer(message, self.strings("load"))
        global state1
        state1 = True
        await message.delete()
        user_id = int(args[0])
        if args:
            time = float(args[1])
        while state1:
            text = random.choice(shablon)
            chat_id = message.chat.id
            if chat_id:
                ph = args[2]
                ph1 = f"{ph}"
                await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem3}<a href='tg://user?id={user_id}'>{text}</a>{prem4}")
                await sleep(0.1)
                await sleep(time)


    async def rwtagm2cmd(self, message):
        '''[id] [задержка в секундах] [ссылка на медиа]'''
        args = utils.get_args(message)
        message = await utils.answer(message, self.strings("load"))
        global state1
        state1 = True
        await message.delete()
        user_id = int(args[0])
        if args:
            time = float(args[1])
        while state1:
            text = random.choice(shablon)
            chat_id = message.chat.id
            if chat_id:
                ph = args[2]
                ph1 = f"{ph}"
                await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem5}<a href='tg://user?id={user_id}'>{text}</a>{prem6}")
                await sleep(0.1)
                await sleep(time)


    async def rwtagm3cmd(self, message):
        '''[id] [задержка в секундах] [ссылка на медиа]'''
        args = utils.get_args(message)
        message = await utils.answer(message, self.strings("load"))
        global state1
        state1 = True
        await message.delete()
        user_id = int(args[0])
        if args:
            time = float(args[1])
        while state1:
            text = random.choice(shablon)
            chat_id = message.chat.id
            if chat_id:
                ph = args[2]
                ph1 = f"{ph}"
                await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem7}<a href='tg://user?id={user_id}'>{text}</a>{prem8}")
                await sleep(0.1)
                await sleep(time)


    async def rwtagm4cmd(self, message):
        '''[id] [задержка в секундах] [ссылка на медиа]'''
        args = utils.get_args(message)
        message = await utils.answer(message, self.strings("load"))
        global state1
        state1 = True
        await message.delete()
        user_id = int(args[0])
        if args:
            time = float(args[1])
        while state1:
            text = random.choice(shablon)
            chat_id = message.chat.id
            if chat_id:
                ph = args[2]
                ph1 = f"{ph}"
                await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem9}<a href='tg://user?id={user_id}'>{text}</a>{prem10}")
                await sleep(0.1)
                await sleep(time)


    async def rwstopmcmd(self, message):
        '''остановить медиа-тэггер'''
        args = utils.get_args(message)
        global state1
        state1 = False
        message = await utils.answer(message, "<b>Stopped!</b>")


    async def rwkalmcmd(self, message):
        '''[id] [задержка в минутах] [ссылка на медиа]'''
        args = utils.get_args(message)
        global state2
        state2 = True
        message = await utils.answer(message, self.strings("load"))
        user_id = int(args[0])
        while state2:
            time = int(args[1])
            time1 = time
            for i in range(100):
                ph = args[2]
                ph1 = f"{ph}"
                chat_id = message.chat.id
                if chat_id:
                    text = random.choice(shablon)
                    await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem}<a href='tg://user?id={user_id}'>{text}</a>{prem2}", schedule=timedelta(minutes=time))
                    time+=time1


    async def rwkalm1cmd(self, message):
        '''[id] [задержка в минутах] [ссылка на медиа]'''
        args = utils.get_args(message)
        global state2
        state2 = True
        message = await utils.answer(message, self.strings("load"))
        user_id = int(args[0])
        while state2:
            time = int(args[1])
            time1 = time
            for i in range(100):
                ph = args[2]
                ph1 = f"{ph}"
                chat_id = message.chat.id
                if chat_id:
                    text = random.choice(shablon)
                    await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem3}<a href='tg://user?id={user_id}'>{text}</a>{prem4}", schedule=timedelta(minutes=time))
                    time+=time1


    async def rwkalm2cmd(self, message):
        '''[id] [задержка в минутах] [ссылка на медиа]'''
        args = utils.get_args(message)
        global state2
        state2 = True
        message = await utils.answer(message, self.strings("load"))
        user_id = int(args[0])
        while state2:
            time = int(args[1])
            time1 = time
            for i in range(100):
                ph = args[2]
                ph1 = f"{ph}"
                chat_id = message.chat.id
                if chat_id:
                    text = random.choice(shablon)
                    await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem5}<a href='tg://user?id={user_id}'>{text}</a>{prem6}", schedule=timedelta(minutes=time))
                    time+=time1


    async def rwkalm3cmd(self, message):
        '''[id] [задержка в минутах] [ссылка на медиа]'''
        args = utils.get_args(message)
        global state2
        state2 = True
        message = await utils.answer(message, self.strings("load"))
        user_id = int(args[0])
        while state2:
            time = int(args[1])
            time1 = time
            for i in range(100):
                ph = args[2]
                ph1 = f"{ph}"
                chat_id = message.chat.id
                if chat_id:
                    text = random.choice(shablon)
                    await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem7}<a href='tg://user?id={user_id}'>{text}</a>{prem8}", schedule=timedelta(minutes=time))
                    time+=time1


    async def rwkalm4cmd(self, message):
        '''[id] [задержка в минутах] [ссылка на медиа]'''
        args = utils.get_args(message)
        global state2
        state2 = True
        message = await utils.answer(message, self.strings("load"))
        user_id = int(args[0])
        while state2:
            time = int(args[1])
            time1 = time
            for i in range(100):
                ph = args[2]
                ph1 = f"{ph}"
                chat_id = message.chat.id
                if chat_id:
                    text = random.choice(shablon)
                    await self.client.send_file(message.peer_id, ph1, caption=f"{shapka} {prem9}<a href='tg://user?id={user_id}'>{text}</a>{prem10}", schedule=timedelta(minutes=time))
                    time+=time1


    async def client_ready(self, client, db):

        self.db = db

        self.client = client
        self.users = []
        
    async def rwkalcmd(self, message):
        '''[id] [задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        user_id = int(args[0])
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[1])
            time1 = time
            for i in range(100):
                await self.client.send_message(message.peer_id, f"{shapka} {prem}<a href='tg://user?id={user_id}'>{choice(shablon)}</a>{prem2}", schedule=timedelta(minutes=time))
                time+=time1


    async def rwkal1cmd(self, message):
        '''[id] [задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        user_id = int(args[0])
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[1])
            time1 = time
            for i in range(100):
                await self.client.send_message(message.peer_id, f"{shapka} {prem3}<a href='tg://user?id={user_id}'>{choice(shablon)}</a>{prem4}", schedule=timedelta(minutes=time))
                time+=time1


    async def rwkal2cmd(self, message):
        '''[id] [задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        user_id = int(args[0])
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[1])
            time1 = time
            for i in range(100):
                await self.client.send_message(message.peer_id, f"{shapka} {prem5}<a href='tg://user?id={user_id}'>{choice(shablon)}</a>{prem6}", schedule=timedelta(minutes=time))
                time+=time1


    async def rwkal3cmd(self, message):
        '''[id] [задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        user_id = int(args[0])
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[1])
            time1 = time
            for i in range(100):
                await self.client.send_message(message.peer_id, f"{shapka} {prem7}<a href='tg://user?id={user_id}'>{choice(shablon)}</a>{prem8}", schedule=timedelta(minutes=time))
                time+=time1


    async def rwkal4cmd(self, message):
        '''[id] [задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        user_id = int(args[0])
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[1])
            time1 = time
            for i in range(100):
                await self.client.send_message(message.peer_id, f"{shapka} {prem9}<a href='tg://user?id={user_id}'>{choice(shablon)}</a>{prem10}", schedule=timedelta(minutes=time))
                time+=time1


    async def rwhourcmd(self, message):
        '''тайп на час'''
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(randint(3600, 3601))
            except BaseException:
                return


    async def rwragecmd(self, message):
        '''[задержка в минутах]'''

        args = utils.get_args(message)

        chat_id = message.chat_id
        if chat_id:
            await utils.answer(message, self.strings("load"))
            time = int(args[0])
            time1 = time
            for i in range(100):
                wablon1 = [" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴇɜᴀʍᴇдᴧиᴛᴇᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴄʍᴏᴛᴩя нᴀ ᴄᴧᴏжнᴏᴄᴛи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴨᴩиʙычᴋᴇ ᴛы ʍнᴇ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ ᴄᴨᴇᴩʍᴏй ɜᴀᴧью 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ʍнᴇ ᴛᴇчёᴛ ᴋᴩᴏʙь ᴄ бᴩюхᴀ ᴛʙᴏᴇᴦᴏ бᴀᴛи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏ ʍнᴇ ᴛᴇчёᴛ чиᴄᴛᴀя ᴋᴩᴏʙь уᴋᴩᴀинцᴀ, ʙᴏ ʙᴩᴇʍя ϶ᴛᴏᴦᴏ жᴇ ᴛы чуᴩᴋᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ɸуᴧᴧ ᴇбᴀᴧᴇ ᴛᴇ ʙ ᴩᴏᴛ ᴄᴄу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛᴇбя ᴋᴀᴋ ᴇбᴀᴧи ᴋᴩᴀᴄных ʙ 44 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюхи хᴇх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇчнᴏ ᴦᴏᴛᴏʙ ᴛᴇбя ᴨᴏᴇбыʙᴀᴛь бᴇᴄᴨᴧᴀᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɯёʙую ᴨᴩᴏᴄᴛиᴛуᴛᴋу ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴧищᴇ ʙ хуй ʙᴏᴛᴋни 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄёɯь ᴋᴀᴋ ᴄᴏᴄуᴛ ʙᴀᴦнᴇᴩяᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ʙᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи уᴇбищᴇ ᴩуᴄняʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀɜᴏʙ ᴛя ᴇбёᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴩиʙыᴋ ᴛᴀᴋ хуи ᴄᴏᴄᴀᴛь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> удᴏбнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴀ ᴩᴏᴄᴄийᴄᴋᴏʍ яɜыᴋᴇ чᴛᴏбы ᴛы ᴨᴏняᴧ ᴋᴀᴋᴏй ᴛы ᴏᴨущᴇнный ᴄын ɯᴧюхи) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏɯибᴀяᴄь ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴏᴧᴦᴏ ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴩᴏᴄᴄиянᴄᴋий ᴄын бᴧяди ᴛуᴛ нᴇ хᴩюᴋᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɸᴇᴋᴀᴧищᴇ ᴄᴏжᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиʙычнᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛя ᴨᴏᴩᴇɜᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй яɜыᴋ нᴀ чᴧᴇнᴇ, чё ᴛы ᴏᴛцу ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛы ᴄ хуя ʍнᴇ ᴋᴩичᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы унижᴇннᴀя ᴄʙинᴏᴨᴄинᴀ ᴇбᴧищᴇ ᴛᴇ ᴛуᴛ ᴩᴀᴄᴋᴀᴛᴀᴧ ᴄучᴋᴇ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чᴏ ᴛᴇᴩᴨиɯь дᴇбиᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨуᴛиниᴄᴛ ᴛы хуй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛиᴋ ɯᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛᴇбя ʙ ᴛʙᴏй ᴩᴏᴛ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ ʍᴀʍᴇ ᴨᴏд ɜᴇᴩᴋᴀᴧьныʍ ʙᴏɜдᴇйᴄᴛʙиᴇʍ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ɜᴀᴋᴏнчиᴧ ᴛᴩᴀхᴀᴛь ᴛʙᴏю ᴄᴇᴄᴛᴩу ᴋᴏᴦдᴀ ᴛʙᴏй ᴏᴛᴇц ᴨᴏᴩʙᴀᴧ ᴛᴇбᴇ ᴀнᴀᴧ, ᴀ ᴛы иɜ ʙᴏɜʍущᴇния чᴛᴏ ᴄ хуя ᴋᴩиᴋнуᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴨᴀᴄᴛь, ᴀ ᴛы чᴛᴏ ʍнᴇ ʙ хуй ᴏᴩᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴋᴩᴏй ᴄʙᴏё ᴇбᴧищᴇ ᴨᴀᴩɯиʙᴏᴇ, ᴇбᴧᴀнихᴀ ᴄᴛᴩёʍнᴏʙыᴦᴧядящᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чё ᴛы ʙ хуй ᴛᴀʍ ᴄᴋуᴧиɯь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи хᴀᴩчᴋи ʙ ᴛʙᴏё ᴇбᴧᴏ, дᴇбиᴧᴋᴀ ᴩуᴄняʙᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴄ хуя ʍᴏᴧʙиɯь ʙᴄё ᴛы бᴇɜ иᴄᴋᴧючᴇний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛʙᴇᴛь ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇᴄᴧи ᴄᴩᴀᴧи нᴀ ᴛя ᴏᴛʙᴇᴛь ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴛᴏ ᴛᴇбя ᴇбᴀᴧ ᴏбʍᴀни ᴄᴇбя жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴛᴇбя яɜыᴋ нᴀ хуᴇ чᴛᴏ ʍᴀʍᴇ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴦᴀдᴀй жᴇᴧᴀниᴇ ʙ ʙидᴇ хуя ʙ ᴩᴏᴛ ᴄᴇбᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛᴇбᴇ нᴀ ϶ᴛᴏ ʙᴄё бᴀбᴋᴀ хуᴇʍ ʙ ᴩᴏᴛ дᴀᴧᴀ ᴇᴄᴧи дᴏ и ᴨᴏᴄᴧᴇ у ᴛᴇбя яɜыᴋ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я бᴏᴦ ᴨᴩᴀʙды ᴀ ᴛы ᴋᴛᴏ ᴨᴩᴇдᴄᴛᴀʙьᴄя ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀᴋ ᴋᴀᴋᴏᴇ ᴨᴩᴇдᴄʍᴇᴩᴛнᴏᴇ ᴄᴧᴏʙᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи быᴧᴏ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨᴩᴀʙдᴀния ᴛуᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ниᴋᴏᴦдᴀ нᴇ будᴇɯь бᴏᴦᴏʍ ᴨᴩᴀʙды и ʙᴄᴇ ᴛʙᴏи ᴄᴧᴏʙᴀ ʙыɯᴇ и нижᴇ будуᴛ ᴏᴛʍᴇнᴇны 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴛы ᴄʙᴏю ᴩᴏдную ʍᴀᴛь убиᴧ ᴏᴛᴨиɯи нижᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴏ ᴛы бᴀбᴋᴇ ʙ ᴋᴧиᴛᴏᴩ ᴦᴏʙᴏᴩиᴧ яɜыᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴏᴛᴨᴩᴀʙиᴧ быᴧᴏ нᴀᴨиᴄᴀнᴏ ʙ ʍиᴩᴇ ʙᴩᴀнья ᴄ яɜыᴋᴏʍ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иᴦнᴏᴩᴏʍ ᴩᴏдᴏᴄᴧᴏʙную убᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏʙᴩи ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ уʍᴇю ʙᴩᴀᴛь, ᴛы ᴄын ɯᴧюхи  𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴩуᴄᴏᴄʙинᴄᴋᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᏌᴋrᴀiniᴀnᏒᴀgᴇ ᴇбᴀɯиᴛ ᴦᴧᴏᴛᴋу ᴛᴇ 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>нᴀ ᴧᴇᴄᴏᴨиᴧᴋᴇ ᴛя ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ нᴏй ᴄʙинᴏᴩуᴄ ᴏᴨущᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу хуᴇʍ ᴛᴇ ᴨᴇᴩдᴀᴋ нᴀ ᴧᴇᴦᴋᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀᴩᴋᴀю ᴛᴇ ʙ ᴇбᴀᴧᴏ дуᴩᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуя ᴨᴏᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧ ᴛᴇ ʙ ᴩᴏᴛ хуй ᴄᴏ ᴄᴧᴏʙᴀʍи ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏбᴏᴄᴩᴀᴧ ᴛᴇбᴇ ᴇбᴀᴧᴏ и чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу, ᴀ ᴛы чᴛᴏ ᴇй ᴋᴩичᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴩᴀᴧ нᴀ ᴛʙᴏё ᴇбᴧищᴇ ᴄᴏ ᴄᴧᴏʙᴀʍи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄᴋᴩиᴨᴛᴏʙᴀнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя удуɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇйчᴀᴄ ᴛᴇбя ᴇбёᴛ хᴏхᴏᴧ, ᴩᴀᴄᴋᴩыʙᴀй ᴄʙᴏю ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюɯᴇчᴋи ᴨиɜдᴏᴨᴩᴏʙᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴀᴄᴀй хуяᴩу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇбᴇ бᴀбᴋᴀ ʙ ᴩᴏᴛ, чᴛᴏ ᴛы нᴀ ϶ᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ хуᴇʍ ᴋᴩᴀᴄиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ɜуб ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хую ᴛы ᴋᴩуᴛиᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴋᴏнчᴀᴧ ᴛᴇбᴇ нᴀ ᴧицᴏ, ᴀ ᴛы чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏё ᴩыᴧᴏ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ бᴀбᴋᴇ ᴄ хуᴇʍ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴄʙᴏё ʙᴀᴧьни ᴄын бᴧяди ᴏᴛᴄᴛᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ᴛя хᴏхᴧы хᴏɜяᴇʙᴀ ᴛʙᴏи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу ᴄʙинᴏᴩуᴄню и ᴛы нᴇ ᴨᴏᴄᴧᴇдний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴇбуᴛ ʙᴄ ᴩɸ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴋᴩиᴄᴛᴀᴧичнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩʙу ᴛᴇбя ᴋᴀᴋ ᴩʙуᴛ ʙᴀᴦнᴇᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ʍᴀʍᴀɯу ᴛᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи ʙяᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏᴩʙᴀᴧ ɜᴩᴋ ᴄ-300 ʙ ᴋᴏᴛᴏᴩᴏʍ быᴧ ᴛʙᴏй ᴏᴛᴇц ᴄ ʙᴀᴦнᴇᴩᴀ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴛᴩᴏᴧᴧиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴋᴩыᴧ жиʙᴏᴛ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴄᴀᴛᴀнᴏй хуяᴩиʍ ᴋᴀᴦᴏᴩ и ᴇбᴇʍ ᴛʙᴏю ʍᴀʍᴀɯᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ дуᴧᴏ ᴛᴀнᴋᴀ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи нᴀᴄᴀдиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴩᴇнᴏй ᴨᴏдᴏᴩʙᴀᴧ ᴛʙᴏᴇᴦᴏ бᴀᴛю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴩᴇжу ᴛᴇ ᴦᴧᴏᴛᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴛᴀᴧ нᴀ ᴄʍᴇᴩᴛный бᴏй и ɜᴀᴩубиᴧ ᴛʙᴏᴇᴦᴏ бᴩᴀᴛᴀ ᴋᴀᴛᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴨᴩиниʍᴀᴇᴛ ʙ ᴄᴇбя ʙᴄё чᴛᴏ ʙᴧᴇɜᴇᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя хᴀᴩᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуйцᴏʍ ᴛя ᴩᴀɜʙᴧᴇᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛя нᴀ ᴧᴏᴨᴀᴛу нᴀᴄᴀжу и чиᴄᴛᴏ ᴋᴀᴋ ᴄиʍбу ᴩᴀᴄᴋᴩучу и ᴏб ᴄᴋᴀᴧу уᴇбу ᴛᴀᴋую дуᴩу ᴛуᴨᴏᴩыᴧую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴏʍᴀᴧ ᴛᴇ ᴄᴨину хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛхуяᴩю ᴛя ᴨᴏ ᴧбу чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уᴇбᴀᴧ ᴛᴇбя ᴄ нᴏᴦи ᴨᴏ ᴩᴇбᴩᴀʍ ᴛʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʍᴇᴩᴄᴀй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧый ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бью ᴛя ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ᴄᴨᴀᴄибᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь? ᴏᴛʙᴇᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ дуᴩᴀ ᴇбᴀнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴛᴇбᴇ ᴄᴋᴀɜᴀᴧи ᴨидᴀᴩᴀᴄᴋᴀ нᴇдᴏᴩᴀɜʙиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧюнуᴧ ʙ ᴛя ɜᴀᴧуᴨᴏй, ᴨᴏᴋᴀ ᴛы хᴀᴩᴋᴀᴇɯь ʙ ɜᴇᴩᴋᴀᴧᴏ ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ жᴀᴧᴋий ᴄынᴏчᴇᴋ хуᴇᴄᴏᴄᴀᴧᴋи нищᴇй чё ᴛы ᴛуᴛ ɜᴀбыᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ɜᴀᴋᴩᴏй ужᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇᴄᴨᴩᴇᴩыʙнᴏ ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ уᴋᴩᴀинᴄᴋᴏй ʍинᴇ ᴛʙᴏй ᴏᴛᴇц ᴨᴏдᴏᴩʙᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇхуй ᴧᴇɜᴛь, ᴨидᴏᴩᴀɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄи чуɯᴋᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди ᴏᴨущᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴇ чуᴩᴋᴏхᴀч ᴛы нᴀхуй ᴄᴏᴄнуᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴧучиᴧ ᴛы ᴨᴏ ᴇбᴀᴧу ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴦдᴀ ᴛя ᴨᴏᴇбᴀᴧи ᴛᴀᴋ жᴇ ᴋᴀᴋ и ᴛы ʍᴏᴧчᴀᴧи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜбᴩᴀннᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ бᴏᴋу ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴛᴏʙ ᴛᴇ бᴇᴄᴋᴏнᴇчнᴏ нᴀ ᴋᴧыᴋ ᴏɸᴏᴩʍᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ ᴧюбʙи ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴛы нᴀᴄᴏᴄᴀᴧ хуя ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴋᴀйɸ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи чᴧᴇн ʙ ᴦᴏᴩᴧᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴄыᴋᴧиʙᴏ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴇʍ ᴛя чинᴦиɜхᴀнᴀ ᴇбᴀнᴏᴦᴏ ᴄ буᴩяᴛии нᴀхуй хᴀɜхᴀɜɜᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴄын ɯᴧюхи ᴋᴏᴨыᴛный ɜᴀчᴇʍ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴄʙин ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙяᴧый хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴄᴛᴀнциᴏннᴏ ᴄᴏᴄёɯь ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя, ᴩуᴄᴏᴄʙин 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛᴇбя ᴨᴏиʍᴇᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏинᴄᴛʙᴇннᴏ ᴛᴇбя ᴨᴏᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ ᴄын ᴄʙиньи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴛʙᴏё ᴨᴏᴇбᴇʍ, дᴇᴦᴇнᴇᴩᴀᴛины ᴄын 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦʙᴏɜдь ᴋ ᴩуᴋᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋ ᴇбᴀᴧу ᴛᴇ диᴧдᴀᴋ жᴇᴧᴇɜный ᴨᴩиᴧᴇᴨиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ᴨᴏᴨᴩᴀʙь ᴋᴩиʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи нᴀᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ʙᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴄᴛᴏʍᴀᴛᴏᴧᴏᴦии ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴀᴩᴀɯᴇ я ᴄᴩᴀᴧ и ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴛᴀʍ жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴩᴏʙᴀᴛи ᴛʙᴏй ᴩᴏᴛ ᴛᴩᴀхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы нᴀ ᴨᴀчᴋу ᴄухᴀᴩиᴋᴏʙ бᴧя ᴇбᴀнᴀᴛ нищᴇнᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴧяᴛь ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩу ʙᴄᴏᴄи ᴄынᴏᴋ бᴧядины 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩяйᴄя нᴀхуй ᴨᴏᴋᴀ ᴛᴇ ᴇбᴀᴧᴏ ᴛуᴛ хуᴇʍ нᴇ ᴩᴀᴄᴋʙᴀᴄиᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ ɜᴀᴧуᴨы ʍᴏᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу жᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏжᴩи дᴇᴩьʍᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛᴇбя у ɯᴋᴏᴧы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦᴧᴀɜ ʙыᴩʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴨᴧяжᴇ чёᴩнᴏᴦᴏ ʍᴏᴩя ᴛʙᴏю ʍᴀᴛь ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧбᴀᴇб ɯᴧᴀнᴦ дᴩᴏчи ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏбᴩᴀннᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴩу ᴋᴏᴦдᴀ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴧюби ᴄᴏᴄᴀᴛь ᴋᴀᴋ ᴧюбиɯь ᴄᴦᴧᴀᴛыʙᴀᴛь ᴄын ɯᴧюхᴛ хᴀɜ϶ᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ Ꮧёɯᴋᴀ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩю ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀбиᴧ ᴛя ʙ уᴦᴧу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴨинᴀᴧ ᴛя хуᴇʍ дуᴩу ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇᴨᴏʙᴛᴏᴩиʍᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛʙᴏᴇй ᴨиɜдᴇ иᴦᴩᴀᴧᴄя, ᴛёᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨиɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴋᴀᴋ бᴀᴩᴀн идᴇᴛ ᴄʙᴏиʍи ᴦубᴀʍи нᴀ ʍᴏй хуй нᴀ ᴛᴀᴩᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴧᴏᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏᴋɜᴀᴧᴇ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴦиᴧьныʍ ᴋᴩᴇᴄᴛᴏʍ ᴛʙᴏᴇᴦᴏ дᴇдᴀ ᴇбᴀᴧ ᴛᴩуᴨ ᴛʙᴏᴇй бᴀбᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏᴛбᴩᴀᴄыʙᴀй ᴋᴏᴨыᴛᴀ ᴏᴛ ʍᴏᴇᴦᴏ чᴧᴇнᴀ ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴩиʙᴏᴇбᴧый ᴄын ʍᴩᴀᴋᴏбᴇᴄия ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧᴏᴄᴋᴏᴇбᴧый ᴨидᴏᴩᴀᴄ нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏбиᴧ ᴛʙᴏй чᴇᴩᴇᴨᴏᴋ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀбᴄиянинᴀ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴏ ᴋᴀᴋ ᴛᴀʍ ᴩᴏᴄᴄиянцы хᴏхᴧᴀʍ ᴄᴏᴄуᴛ ʍдᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ чᴇᴛʙᴇᴩᴇньᴋᴀх ʍнᴇ ᴄᴏᴄᴀᴧᴀ ʍᴀᴛь ᴛʙᴏя 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчуʙᴄᴛʙуй хᴏᴛь ᴄᴇйчᴀᴄ ɜᴀᴨᴀх ᴄʙᴏбᴏды и ʙыбᴇᴩи чᴏ ᴄᴏᴄᴀᴛь будᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴧчи ᴄ чᴧᴇнᴏʍ ʙᴏ ᴩᴛу ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ʙᴏᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴇниᴄ ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴛᴏ Ꮯᴀɯᴋᴀ ᴄᴏᴄᴀᴛь ᴛᴏ будᴇɯь ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄиɸᴏɜнᴏй ɯᴧюхи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀ ᴛʙᴏя нᴀ чᴧᴇнᴇ ᴨᴏᴛухᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴛы чᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴛʙᴏю ʍᴀᴛь чᴧᴇнᴏʍ ɜᴀᴇхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏᴄᴛᴩᴇᴧиᴧ ᴋᴏᴧᴇни ᴏᴛцу ᴛʙᴏᴇʍу ʙᴀᴦнᴇᴩᴏʍяᴄу ᴇбучᴇʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ʍᴏнᴇᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴛь ᴛʙᴏю ʙ ᴀнᴀᴧ ᴦᴧᴀдᴋᴏ ᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ чᴇᴄᴛи ᴏᴛᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй ᴇбᴧᴏʍ ᴧᴏʙи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴏᴩʙу ᴛᴇ ᴩуᴋи и буду ᴄᴇбᴇ ниʍи дᴩᴏчиᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄʙᴏиʍи ʙиᴄячиʍи ᴄиᴄьᴋᴀʍи дᴩᴏчиᴧᴀ дуᴩᴀ бᴧяᴛь ɜᴀхɜᴀᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴛᴀʙиᴧ ᴩʙᴀныᴇ ᴩᴀны нᴀ нᴏᴦᴀх ᴛʙᴏᴇй ʍᴀʍᴀɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏɯёᴧ и ʙыᴩубиᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴩуниɯᴋᴀ ᴋᴛᴏ ᴄᴩᴀᴧ нᴀ ᴛᴇбя ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ ᴩучᴋи ᴛᴏ дᴩᴏжᴀᴛ у ᴛᴇбя ᴨᴇᴩᴇд ʍᴏиʍ чᴧᴇнᴏʍ ᴩуᴄᴏᴄʙинья ᴛы ᴇбᴀнуᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯиɯь я ᴛᴇбᴇ ᴛуᴛ ᴨᴀᴧьцы буду ᴏᴛбиʙᴀᴛь ᴏдин ɜᴀ дᴩуᴦиʍ ɜᴀ ᴛᴏ чᴛᴏ ᴛы ᴛᴀᴋᴏй ʍᴇдᴧᴇнный ᴄынᴏᴋ ɯᴧюɯᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜ ᴨᴏᴄᴧᴇдних ᴄиᴧ ʙᴏюᴇɯь ᴄ ʍᴏиʍ хуᴇʍ ᴛуᴛ чᴇᴨухᴀ ᴨᴏɜᴏᴩнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏйнᴇ ᴛы ᴄ ʍᴏиʍ хуᴇʍ дᴩᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴄᴧиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀʙᴀй ᴄын ɯᴧюхи ᴄᴏбиᴩᴀйᴄя ᴄ ʍыᴄᴧяʍи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇʙᴀᴛᴇᴧь ᴨᴇниᴄᴏʙ ᴛы чᴏ ᴛуᴛ ʙᴄᴇʍ хуй ᴏᴛᴄᴀᴄыʙᴀᴇɯь ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴨидᴏᴩ жиᴩный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄунᴇц хуя ᴛы ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴀбᴇйɯий ᴄын ɯᴧюхи ᴏчниᴄь ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴨиɜды нᴇ дᴀᴧ ᴏᴨяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏʙнᴏ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍбуᴧу ᴛы ᴩᴛᴏʍ ɯᴧиɸᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄунᴇц хуᴇʙ хᴏхᴧᴏʙ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ʙ ᴦᴏᴧᴏʙу ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩᴏᴄʙин ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩыᴧᴏ ᴛᴇ ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴩᴀɜбиᴧ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩуᴄᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛᴇ хуй ʙ ᴩыᴧᴏ ᴄᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀч нᴀ хуй ʍᴏй нᴇ ᴨᴀдᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏʙцᴇᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ʙыʙᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴛᴀᴄᴋᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуᴇ ᴛы ᴋᴀᴛᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя биᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя дᴏбиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴛᴀниᴩᴏʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙɜᴏᴩʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴏʍбᴇɜнᴏ ᴨᴏᴇбᴀᴧ ᴛʙᴏю ʍᴀʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩᴏᴄᴄиянᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴩᴀɯиᴄᴛ ᴛы ʙᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь нᴀ ᴩуᴄᴄᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь будᴛᴏ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жуᴛь нᴀ ᴛᴇбя нᴀʙᴏдиᴛ ʍᴏй ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴏᴄᴄиянᴇц ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇᴧᴇɜнᴏбᴇᴛᴏннᴏ ᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴨᴏᴋᴀ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀхуй ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴋуᴄыʙᴀя ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴋᴩыʙᴀяᴄь ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуй ʍᴏй ᴛы нᴀᴨᴀᴧ и ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴀждᴏй ᴧᴀʙᴋᴇ ᴨᴀᴩᴋᴀ ᴛʙᴏю ʍᴀᴛь я ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇᴄᴏᴄ ᴩᴀɜбᴇй ᴦᴏᴧᴏʙу ᴄᴇбᴇ ᴏб ᴄᴛᴇнᴋу нᴀхуй ᴨᴏᴋᴀ я ɜᴀняᴛ ᴨᴏᴇбыʙᴀниᴇʍ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴛуᴨᴏᴦᴏᴧᴏʙᴏй ᴄын ɯᴧюхи ᴨᴇᴩᴇᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу ʙ ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴇдᴏᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀɯу ᴛʙᴏю чуᴩᴇᴋᴄᴋую ᴨᴏᴇбᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы иɜ чуᴩᴋᴏᴄᴛᴀнᴀ ᴄбᴇжᴀᴧ ᴦдᴇ ᴛᴇбя ʙ ɜᴀᴦᴏнᴇ дᴇᴩжᴀᴧи нᴀхуй ᴋᴀᴋ ᴄᴏбᴀᴋу диᴋую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> буᴩяᴛнᴏ ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы диᴋий ᴄын ɯᴧюхи ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴀ ᴛᴏ щяᴄ хуи нᴀᴧᴇᴛяᴛ ᴨᴩяʍ ʙ ᴩыᴧᴏ ᴛʙᴏё ᴛᴩᴀхᴀннᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ дᴏᴧᴦ ᴛы ʍнᴇ хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀᴛи ᴛы дᴩᴏчиᴧ ʍнᴇ ᴨᴩияᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴧᴀᴦᴏдᴀᴩиᴧ ᴛя чᴧᴇнᴏʍ ᴨᴏ ᴦубᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀщᴇᴋᴀнᴇц ᴇбᴧищᴇ ᴨᴩиᴋᴩᴏй ᴄʙᴏё ᴨᴩᴏᴛиʙнᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуи ᴨихᴀᴧи ᴛᴇ ʙ уɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇᴦᴏдня ᴛᴇбᴇ ᴦᴧᴀɜᴀ хуяʍи ʙыᴋᴏᴧяᴛ ᴄыниɯᴋᴇ ɯᴧюхи ᴛᴀᴋᴏʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ жидᴏᴄʙин ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴩᴏᴄᴄийᴄᴋᴀя хуᴇᴄᴏᴄᴀᴧᴋᴀ ɜᴀ ᴋᴏᴨᴇйᴋи ᴄᴏᴄёᴛ и ᴋиᴛᴀйцы ᴇё ᴄᴇбᴇ нᴀ нᴏчь бᴇᴩуᴛ ᴨᴏᴋᴀ ᴛы ᴄидиɯь и ждёɯь ᴇё 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏ ᴨᴩиʙычᴋᴇ уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ хуя будᴛᴏ ᴏᴛ ᴄᴨᴇᴩʍы ᴄʙᴏᴇᴦᴏ ᴏᴛцᴀ ᴀᴧᴋᴀɯᴀ ᴇбучᴇᴦᴏ бᴧя хᴀхᴀхᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴧиᴛᴇᴧьнᴏ ᴛы ʙыдᴇᴩжиʙᴀᴧ ᴄᴨᴇᴩʍу ʙ ᴦᴏᴩᴧᴇ ᴛᴏᴧьᴋᴏ нᴀхуя нᴇ ᴨᴏняᴧ я 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʙɜяᴧ ᴨᴇᴩᴇдыɯᴋу чᴛᴏбы нᴇ ᴄᴏᴄᴀᴛь хᴏᴛь ʍинуᴛу ᴄʙᴏᴇй жиɜни ᴋᴏᴛᴏᴩᴀя ᴋᴏнчиᴛᴄя ᴋᴏᴦдᴀ ᴛы ᴨᴩиᴇдᴇɯь ʙ Ꭹᴋᴩᴀину ʙᴏᴇʙᴀᴛь ʙᴇдь ᴛы ᴏʙцᴀ ᴄᴧᴀбᴀя ᴋᴏᴛᴏᴩᴏй ᴀнᴀᴧ ᴦᴩᴀнᴀᴛᴏй ᴩᴀɜᴏᴩʙуᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄʍᴇхᴀюᴄь нᴀд ᴛᴏбᴏй чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нищуᴦᴀн ᴛы ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏё ᴇбᴀᴧᴏ ᴄʙᴏᴇй ɜᴀᴧуᴨᴏй ᴄᴋᴩуᴛиᴧ ɯᴏб нᴇ ᴨиɜдᴇᴧ ʍнᴏᴦᴏ ɜᴀ ᴩᴏᴄᴄию ᴄʙᴏю ʙᴇᴧиᴋую ʙᴏ ʙᴄᴇ щᴇᴧи ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇ ᴨᴏ ᴦᴏᴧᴏʙᴇ нᴀᴄᴛучу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи чуᴩᴇᴋᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴋᴄᴛᴀ ᴨидᴏᴩᴀᴄ чуᴩᴋᴏᴄᴛᴀнᴏʙᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> униɜиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀхуяᴩю ᴛя хуᴇʍ ᴋᴀᴋ ᴏᴋᴋуᴨᴀнᴛᴀ будᴇɯь ᴏдниʍ ᴄ 200ᴋ дᴏхᴧых ᴩᴏᴄᴄиянᴄᴋих ᴄʙинᴏᴨᴄᴏʙ ᴀхɜᴨɜᴨɜᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙыᴩубиᴧ ᴛя хуᴇʍ ᴋᴀᴋ ᴋуʙᴀᴧдᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ʙᴏ ᴩᴛу щᴇᴋᴏᴛᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чё ᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨидᴏᴩᴀᴄня ᴩᴀᴄᴄиянᴄᴋᴀя хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴨьёʍ ᴛᴇбᴇ ᴦᴧᴀɜᴀ ᴋ хуяʍ ʙыᴋᴏᴧю дᴇбиᴧᴋᴇ ᴛᴩᴇхɜубᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ хуᴇц ᴄᴧюняʙиᴧ ɜᴀчᴇʍ хᴀчуᴩᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴧᴇни ᴛᴇ ᴨᴇᴩᴇᴧᴏʍᴀю нᴀхуй дуᴩᴇ ᴄᴧыɯиɯь ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ʍᴏй хуй ɜᴀ ᴄʙᴏᴇй ʍᴀʍᴏй дᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍ ᴛя бᴩᴏᴄиᴧ ʙ яʍу ᴦдᴇ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴄ ᴨᴏʍᴏщью хуя ᴛᴏᴧьᴋᴏ чᴛᴏ ɜᴀᴇбᴀɯиᴧ ɸᴀнᴀᴛᴏчᴋу ʙᴀᴦнᴇᴩᴏᴄʙинᴇй ᴄᴏᴄунцᴏʙ ʍᴏᴇᴦᴏ хуя ᴇбᴀнуᴛых нᴀ ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ᴛы нᴀ ʍᴏёʍ хуᴇ ᴋᴀᴋ нᴀ ʍᴏᴨᴇдᴇ ᴋᴀᴛᴀᴇɯьᴄя ᴇбᴀнᴀᴛиᴋ ᴄᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> быᴄᴛᴩᴏ ᴛы нᴀ чᴧᴇнᴇ ᴨᴏᴛух ᴄынᴏᴋ ɯᴧюхи ᴛуᴨᴏдᴏхᴏдящᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀнᴋиᴄᴛу ᴛы ᴄᴏᴄᴀᴧ чᴛᴏбы ᴏн ᴛʙᴏих ʙᴀᴦнᴇᴩᴏᴄʙинᴇй нᴇ ᴇбᴀɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя ᴋᴀᴋ ᴋᴀᴩᴀᴛᴇᴧь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴋᴀйɸу ᴛя ʙыᴇб 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀбыᴧ ᴋᴀᴋ ʍнᴇ ɜᴀᴧуᴨу бᴧᴀᴦᴏдᴀᴛную цᴇᴧᴏʙᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨущᴇнᴇц ᴏᴛъᴇбᴀнный ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛёᴧᴋᴀ ᴛы у ᴋᴏᴦᴏ ᴄᴏᴄᴀᴛь учиᴧᴀᴄь ᴏᴛʙᴇᴛ ʙ ɜᴀᴧуᴨу ᴏɸᴏᴩʍи ᴨᴏ ᴋᴀйɸу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴩᴇжу ᴛʙᴏю ᴦᴏᴧᴏʙу нᴀхуй ᴋᴀᴋ чᴇчᴇнᴇц 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜдᴇᴧᴀᴧᴄя ᴄ ᴛᴏбᴏй ᴋᴀᴋ ᴋᴩᴀᴋᴇн ᴄ ʙᴀᴦнᴇᴩᴏʍяᴄᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴀɸᴏᴄнᴏ ᴛы хуй ᴄᴏᴄᴀᴧ ᴏᴨᴏɜᴏᴩᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чё ᴇбᴀᴧᴏʍ ᴄʙᴏиʍ нᴀᴄᴏᴄᴀᴧ нᴀ ʍᴀɯину чᴛᴏ-ᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜᴏᴩʙи ᴄᴇбᴇ ᴩᴏᴛ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴀᴩиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴛь ᴛы ᴋᴀᴋ ᴄʙин жиᴩнющий ʍнᴇ хуй ᴄᴏᴄёɯь ᴨᴩяʍ диᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏɜᴏᴩищᴇ ᴋᴄᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄʍᴇиʙᴀюᴛ ᴛᴇбя, ᴀ ᴛы ᴛᴇᴩᴨиɯь чᴧᴇн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы дуᴩᴀ уᴄᴨᴏᴋᴏйᴄя ᴨᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы хуᴇᴄᴏᴄᴀᴧᴋᴀ нищᴀя ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄунуᴧ ᴛᴇ хуй ʙ ᴩыᴧᴏ, ᴛᴇᴩᴨи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴋ ᴄᴛᴇнᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя нᴇ ʍᴀᴧᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴛы ᴨᴩᴇᴋᴩᴀᴄнᴏ ʍᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴧᴀя ᴛы ɯᴀᴧᴀʙᴋᴀ хᴇхᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ʍнᴇ ɯᴋᴏᴧьниᴋ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ᴇбᴀнᴀя ɯᴀᴧᴀʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴇх ᴀᴧьɸᴀч ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴛᴀйᴄᴋᴀя ᴏᴛдᴀᴧᴀᴄь ɜᴀ нᴏн ᴄᴛᴏᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɜᴏᴩный уᴩᴏд ᴛы нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жиᴩный ᴋуᴄᴏᴋ ʙᴏнючᴇᴦᴏ дᴇᴩьʍᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй ʍинᴇᴛ ᴨᴏхᴏж нᴀ хуйню 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ чᴧᴇняᴩу ᴄᴏᴄᴇɯь ᴋᴀᴋ бᴇɯᴇный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄиᴧьный ᴏᴛᴄᴏᴄниᴋ ᴛᴀᴋ ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴀ ᴛы ᴋуᴄᴏᴋ ᴨᴏхᴏжᴇᴦᴏ нᴀ дᴇᴩьʍᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴏᴇд ᴇбᴀный ɜᴀᴋᴩᴏй ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ ᴛᴩᴀхᴀᴧ ᴛʙᴏй ᴀнᴀᴧ бич 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴄᴏᴄи чᴧᴇн ɸᴩиᴋᴏʙᴀᴛый ᴨᴇдиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄуᴋи ᴛы чᴇᴩнᴏʙᴀᴛᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇдᴩиᴧᴀ ᴛы ᴩᴀɜуᴋᴩᴀɯᴇнᴏᴇ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛы ʍнᴇ хуй ᴄᴏᴄᴇɯᴧ ᴛᴀᴋ чᴀᴄᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙ ʍнᴇ чᴧᴇн ᴄᴏᴄᴀᴧ ᴇʙᴩидᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄ ʍᴏиʍ чᴧᴇнᴏʍ ʍᴀɜᴏхиᴄᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇʙᴩᴇйᴄᴋᴀя нᴀᴛуᴩᴀ у ᴛᴇбя ᴄ чᴧᴇнᴀʍы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦниᴧью ᴏᴛ ᴛᴇбя ʙᴏняᴇᴛ ᴨᴇдᴀᴩᴀᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄᴀᴧ ʍнᴇ и нᴇ ᴛᴏᴧьᴋᴏ ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>ᴨᴏ ᴨᴩиᴋᴏᴧу ᴛᴇбя ᴛᴩᴀхᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>  ʙьᴇбᴀᴧ ᴛᴇбя чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ хуᴇʍ ʙ ᴩуᴋᴀх ᴛы ʍнᴇ ᴨиɜдиɯь чᴛᴏ-ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɯᴧюхᴀ ᴋᴏɜᴀцᴋᴀя ᴨᴀᴩᴇнᴇᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴋᴏᴧᴏ ɜᴀᴨᴏᴩᴏжᴄᴋᴏй ᴄичи ᴛы хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏц ниᴋ ᴨᴇниᴄᴏɸᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я хᴏчу ᴛʙᴏю ʍᴀᴛь ɯᴀᴧᴀʙу ᴛᴩᴀхᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛᴇᴋ ᴦᴇй ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄи чᴧᴇн уᴋᴩᴀинᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʙᴏй ɸᴀᴋᴇᴩ я дᴧя ᴛя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй ʍнᴇ чᴧᴇняᴩу ʍᴏнᴄᴛᴩ ᴋᴀʍᴏʙый 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбя нᴀ ʍᴏдуᴧях ʙыᴇбу ᴄᴧᴀб ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛиɯᴇ ᴄᴏᴄи ᴧᴏх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛя ᴋᴏɜᴇᴧ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴀᴄи ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴀᴧᴏ ᴛᴇбя ᴨуᴄᴛиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴧичный ᴄᴨᴇᴩʍᴏᴨᴩиᴇʍныᴋ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ 43 ᴦᴏду ᴛᴇбя ʙыᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛʙᴏй ᴇбыᴩь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ᴄᴧᴏн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴋᴀᴋ ᴇбᴀнуᴛый ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇбя ᴩᴀɜъᴇбᴀᴧ я чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ᴨᴀᴛᴧы ʙыᴩʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴦᴏᴧубя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɸᴀйᴄя ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи, ᴛᴇᴩᴨи ᴇᴄᴧи ᴛʙᴏй ᴏᴛᴇц ᴨидᴏᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀждᴏᴇ ᴛʙᴏё ᴄᴧᴏʙᴏ нижᴇ ϶ᴛᴏ хуи ᴧᴇᴛящиᴇ ʙ ᴄᴏᴄᴀᴧᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨᴇᴧᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ж ᴛя убью нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴏ ᴄын бᴧядины ᴛы иɜ ᴄᴇбя нихуя нᴇ ᴨᴩᴇдᴄᴛᴀʙᴧяᴇɯь бᴇᴩи ʍᴏᴇᴦᴏ хуя ʙ ᴩᴏᴛ ᴛᴇᴩᴨиᴧᴏид чё ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ ɜнᴀᴇɯь чᴛᴏ ʍᴀᴛь ᴛʙᴏю ʙ ᴦᴏᴩᴧᴏ ʙᴄᴇ ᴇбуᴛ нᴀᴄᴧᴇдниᴋ хуя ᴛы ʍᴏᴇᴦᴏ ᴧучɯᴇ ᴨᴏ хᴏᴩᴏɯᴇʍу ᴛᴇᴩяйᴄя ᴨᴏᴋᴀ ᴛʙᴏя ᴦᴧᴏᴛᴋᴀ цᴇᴧᴀ ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴇбᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴨᴧᴇжуй ᴛы чё ᴛуᴛ ᴩᴇɯиᴧ чᴛᴏ-ᴧи жᴀᴧᴏʙᴀᴛьᴄя чᴛᴏ ᴛᴇбя ʙ дыᴩы ᴛʙᴏи ᴇбуᴛ ᴨᴏᴋᴀ ᴛы хуй ᴄᴏᴄёɯь иᴧи чё ᴄᴧᴀбинᴀ нᴇʙьᴇбᴇннᴀя нᴀʙᴇᴩни ɜᴀᴧуᴨы ᴄʙинᴏᴩыᴧый ᴄын ɯᴧюхи ʙыᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴏᴛᴄᴏᴄᴀйдᴇᴩ ᴇбучий ᴛы чё нᴇ ᴏᴨᴩᴀʙдыʙᴀᴇɯь ᴄʙᴏй ʍинᴇᴛ ʍнᴇ, ᴛы чᴛᴏ-ᴧи ᴄчиᴛᴀᴇɯь чᴛᴏ ᴦᴧᴏᴛᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи дᴧя ᴩуᴄᴄᴋᴏᴦᴏ ϶ᴛᴏ чᴇᴄᴛь ᴩᴀɜ ᴛы ᴛᴀᴋ ᴨᴩиʙыᴋ жᴩᴀᴛь ᴨᴇниᴄы хᴏхᴧяᴛᴄᴋиᴇ? ᴩᴇщᴇ ᴛуᴛ ᴏᴨᴩᴀʙдᴀния ʙ хуй ᴏɸᴏᴩʍи ᴄынᴏᴋ ɯᴧюɯᴇчᴋи нᴇʙᴏᴄᴨиᴛᴀнный ᴇбᴀᴧ жᴇ ᴛя ʙ ᴦᴏᴩᴧᴏʙину ᴛʙᴏю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀ я ᴨᴏᴋᴀ ᴛᴇбᴇ нᴀ ᴋᴧыᴋ нᴀᴋидыʙᴀᴧ ᴛы ʍнᴇ ᴨᴀᴧьчиᴋᴀʍи ᴀнᴀᴧ хᴏᴛᴇᴧ ʙычиᴄᴛиᴛь ᴛᴀᴋ ʙᴏᴛ я ɜᴀᴄᴛᴀʙиᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋуу ᴇё яɜыᴋᴏʍ ʍнᴇ жᴏᴨу ᴧиɜᴀᴛь ибᴏ у ᴛᴇбя ϶ᴛᴏ нᴇ ᴏᴄᴏбᴏ хᴏᴩᴏɯᴏ ʙыхᴏдиᴧᴏ ᴨᴏᴛᴏʍу чᴛᴏ ᴛы ᴨᴏ бᴏᴧьɯᴇй чᴀᴄᴛи ᴧиɯь хуи ᴦᴧᴏᴛᴀᴛь ᴄᴨᴏᴄᴏбᴇн ᴩуᴄᴏᴄʙинᴄᴋий ᴄынᴏᴋ ɜᴇᴧьᴇʙᴀᴩᴋи нᴇ бᴏйᴄя ʍᴇня ᴛуᴛ ᴨᴏᴋᴀ я ᴛя ᴨᴇниᴄᴏʍ бью ᴛы жᴇ ᴋᴀйɸᴏʙᴀᴧ ʙᴄᴇᴦдᴀ ᴏᴛ ϶ᴛᴏᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ужᴇ ʙᴄᴇʍ ᴨᴩиɜнᴀᴛьᴄя дᴏᴧжᴇн чᴛᴏ ᴛы хуя ʍᴏᴇᴦᴏ ɸᴀнᴀᴛᴋᴀ и ᴋᴀждый ʙᴇчᴇᴩ ʍᴏᴇй ɜᴀᴧуᴨᴇ ᴨᴏᴋᴧᴏняᴇɯьᴄя ᴋᴀᴋ будᴛᴏ бᴏᴦᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи уᴄᴋᴏᴦᴧᴀɜый жиʙущий ʙ буᴩяᴛии нᴀɜыʙᴀᴧ ᴄᴇбя ᴩуᴄᴄᴋиʍ ᴨᴏᴋᴀ хуину ʍᴏю ɯᴧиɸᴏʙᴀᴧ ɯᴧюхи ᴛы ᴄынᴏᴋ ᴨᴏᴋᴀ уж ᴛᴇбᴇ ɜубы хуᴇʍ ʙыбиᴛь чᴛᴏбы ᴛы ᴋᴏ ʙᴄᴇʍу ᴇщё и ɯыᴨиᴧяʙиᴧ уᴩᴏдᴇц ʙыᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙнᴀᴛуᴩᴇ жᴇ ᴛᴇбя ᴄᴇйчᴀᴄ ᴄынᴋᴀ бᴧяди хуᴇʍ чᴇᴄᴛи иɜбᴀʙᴧю 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧё ᴄын ɯᴀᴧᴀʙы уᴩᴏдᴧиʙый хуяᴩу ʍᴏю нᴀᴄᴀᴄыʙᴀй инᴀчᴇ ᴛᴇ ϶ᴛᴀ хуяᴩᴀ ᴨᴏ ᴧбу ᴄᴇйчᴀᴄ ᴄᴛучᴀᴛь нᴀчнᴇᴛ и ᴛʙᴏи нᴇ ᴩᴀбᴏчиᴇ ʍᴏɜᴦи ᴨᴏᴧуᴄᴦниʙɯиᴇ ᴨᴩᴏᴄᴛᴏ нᴀᴦᴧухᴏ ʙыбьᴇᴛ бᴇɜ ʙᴏɜʍᴏжнᴏᴄᴛи ʙᴏᴄᴄᴛᴀнᴏʙᴧᴇния ᴛы нᴀʙᴄᴇᴦдᴀ ᴛуᴨыʍ ᴄынᴋᴏʍ ɯᴀᴧᴀɯᴏʙᴋи ᴏᴄᴛᴀнᴇɯьᴄя и нихуя нᴇ ᴨᴏʍᴏжᴇᴛ ᴛᴇбᴇ, ᴀ ϶ᴛᴏ ʙᴄё ᴧиɯь ᴨᴏᴛᴏʍу чᴛᴏ ᴛы нᴀ ʍᴏй чᴧᴇн ᴩыᴨнуᴧᴄя ᴨуᴛᴧᴇᴩᴄᴋий нᴀᴄᴏᴄниᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын дᴀʙᴀᴧᴋи ᴇᴄᴧи ᴄᴧыɯиɯь ʍᴇня ᴨᴩᴏʍᴏᴧчи ᴇᴄᴧи ᴄᴏᴦᴧᴀᴄᴇн ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ ᴏᴛдᴇɸᴀᴛьᴄя ᴨыᴛᴀйᴄя нᴏ я жᴇ ɜнᴀю чᴛᴏ нᴀ хуи уᴋᴩᴀинᴄᴋиᴇ ᴛы ᴨᴀдᴏᴋ и ᴄᴇйчᴀᴄ у нᴏᴦ ʍᴏих уʍᴏᴧяᴛь будᴇɯь чᴛᴏбы ʍᴏй ᴨᴇниᴄ ʙ ᴛʙᴏёʍ ᴩᴏᴛиᴋᴇ ɯᴇʙᴇᴧиᴧᴄя ᴄᴏ ᴄᴋᴏᴩᴏᴄᴛью ёбᴧи ᴄ ᴛʙᴏᴇй ʍᴀᴛᴇᴩью ᴛуᴨᴏᴦᴏᴧᴏʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶у хуᴇᴛᴇнь ᴄᴧᴀбᴇйɯᴀя нᴇ ʙɜдуʍᴀй ᴛᴇᴩᴨᴇᴛь ᴛᴏᴛ ɸᴀᴋᴛᴏᴩ чᴛᴏ ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ʍнᴇ ɜᴀ 200 ᴦᴩиʙᴇн ᴏᴛдᴀᴧᴀᴄь и ᴩᴀɜᴩᴇɯиᴧᴀ ʍнᴇ ᴄ нᴇй чᴛᴏ уᴦᴏднᴏ дᴇᴧᴀᴛь дᴀжᴇ ᴇю ɜᴀᴧуᴨᴏй ᴨᴏʙᴇᴧᴇʙᴀᴛь, ᴀ ɜᴀ 300 ᴦᴩиʙᴇн ᴏнᴀ ʙᴀщᴇ будᴇᴛ ᴧᴇжᴀᴛь нᴀ ᴄᴨинᴋᴇ и яйцᴀ ʍᴏи ᴧиɜᴀᴛь ну и ɯᴀᴧᴀɯᴏʙᴋᴀ ᴋᴏнᴋᴩᴇᴛнᴀя у ᴛя ʍᴀɜᴇᴩ я бы ᴇй ᴋиᴩᴨичᴏʍ ᴇбᴀᴧьниᴋ ᴄᴧᴏʍᴀᴧ нᴏ ᴨᴏдуʍᴀᴧ чᴇʍ ᴏнᴀ ᴨᴏᴄᴧᴇ ϶ᴛᴏᴦᴏ ɜᴀᴩᴀбᴀᴛыʙᴀᴛь ᴛᴏ будᴇᴛ и ᴨᴏжᴀᴧᴇᴧ ᴛʙᴏю ʍᴀᴛь ɯᴧюху ᴛуᴨᴏᴩᴏᴦую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы нᴇдᴏᴩᴀɜʙиᴛыʍ ᴩᴏдиᴧᴄя ᴨᴏᴛᴏʍу чᴛᴏ ᴨᴏᴋᴀ ᴛʙᴏя ʍᴀʍᴀɯᴋᴀ быᴧᴀ ᴛᴏбᴏю бᴇᴩᴇʍᴇннᴀя я ᴇй ᴨᴩᴏᴄᴛᴏ ᴄ дʙух нᴏᴦ нᴀхуй ʙ жиʙᴏᴛ ʙᴧᴇᴛᴀᴧ и ɜᴀᴄᴛᴀʙᴧяᴧ ᴇё ᴄᴏᴄᴀᴛь ʍнᴇ, ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴄʙᴏᴇй ɜдᴏᴩᴏʙᴇннᴏй ɜᴀᴧуᴨᴏй хуяᴩиᴧ ᴇй ᴨᴏ бᴏɯᴋᴇ ᴏᴛ чᴇᴦᴏ ᴇё ʍᴏɜᴦ быᴧ ᴛᴏᴛᴀᴧьнᴏ ᴨᴏʙᴩᴇждён ᴋᴀᴋ ᴛʙᴏй ᴩᴏᴛ ᴏᴛ ʍᴏᴇᴦᴏ хуя ᴄᴇйчᴀᴄ и ᴨᴏ иᴛᴏᴦу ᴏнᴀ нᴀ ʙᴄю жиɜнь ᴏʙᴏщᴇʍ ᴏᴄᴛᴀᴧᴀᴄь и я ᴇё ʙᴛихᴀᴩя нᴀʙᴇщᴀᴧ и ᴩᴇɜинᴏʙый ᴨᴇниᴄ ɜᴀ щᴇᴋу ᴇй ᴄᴏʙᴀᴧ ᴨᴏᴋᴀ ᴏнᴀ хᴏᴛᴇᴧᴀ ᴏᴛбиᴛьᴄя ᴏᴛ ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛ хуя ʍᴏᴇᴦᴏ ʙ ᴨиɜдᴇ ᴄʙᴏᴇй ʍᴀʍᴋи нᴇ ᴨᴩячьᴄя ᴛᴏ ɜᴀᴄᴄыᴋᴀнный ᴄыниɯᴋᴀ бᴧядины я ᴛᴇбя ᴨᴏжᴀᴧᴇю ᴇᴄᴧи ʍнᴇ ᴇщё ᴨᴀᴩу ᴩᴀɜ дᴀɯь ᴄʙᴏи иᴄᴨᴏᴧьɜᴏʙᴀнныᴇ ᴦубᴇɯᴋи чᴛᴏбы я ʍᴏᴦ ниʍи ᴛᴏᴩᴦᴏʙᴀᴛь ᴋᴀᴋ хᴀч ᴨᴏʍидᴏᴩᴀʍи нᴀ бᴀɜᴀᴩᴇ нᴏ ʙ ʍᴏёʍ ᴄᴧучᴀᴇ ϶ᴛᴏ будᴇᴛ ᴨᴩиᴛᴏн ʙ ᴋᴏᴛᴏᴩᴏʍ будуᴛ ᴛʙᴏи ᴦубы иᴄᴨᴏᴧьɜᴏʙᴀᴛь дᴧя ᴛᴇᴄᴛᴀ ʍᴀᴋᴄиʍᴀᴧьнᴏй дᴏɜы нᴀᴩᴋᴏ ᴨᴏᴄᴧᴇ ᴋᴏᴛᴏᴩᴏй чᴇᴧᴏʙᴇᴋ уʍᴩᴇᴛ нᴏ ᴨᴩᴧбᴧᴇʍᴀ ᴛᴏ ʙ ᴛᴏʍ чᴛᴏ ϶ᴛи ᴛᴇᴄᴛы нᴇ ᴨᴩинᴇᴄуᴛ ᴨᴏᴧьɜы ибᴏ ᴛы ᴄʙиннᴏᴩыᴧый ᴄын ɯᴧюхи и нᴀ ᴨᴏᴧᴏʙину ᴨёᴄ цᴇᴨнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ɜᴀ щᴇᴋу ужᴇ уᴄᴛᴀᴧ нᴀᴋидыʙᴀᴛь бᴧя ᴄᴛяни ᴇбᴧищᴇ ᴄʙᴏё чᴛᴏбы я нᴇ ᴩᴀᴄᴛᴇᴦнуᴧ ɯиᴩинᴋу и нᴇ дᴀᴧ ᴛᴇбᴇ ᴨᴏ ᴦубᴀʍ хуйцᴇʍ ᴄнᴏʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏйди ᴋᴏ ʍнᴇ ᴏᴛᴄᴏᴄный ᴄʙинᴏᴩуᴄ я ᴛᴇбᴇ дᴀʍ хуя ᴄʙᴏᴇᴦᴏ ᴨᴏᴨᴩᴏбᴏʙᴀᴛь нᴀ ʙᴋуᴄ ʍᴏжᴇᴛ ᴛᴇбᴇ ʍᴏй чᴧᴇн ᴨᴏнᴩᴀʙиᴛᴄя ᴋᴀᴋ ʍᴀʍᴀɯᴇ ᴛʙᴏᴇй ᴋᴏᴛᴏᴩᴀя ᴩᴛᴏʍ ᴄ хуя ужᴇ ᴋᴏᴛᴏᴩый дᴇнь нᴇ ᴄᴧᴇɜᴀᴇᴛ, дуʍᴀю у ʙᴀᴄ ϶ᴛᴏ ᴄᴇʍᴇйнᴏᴇ ᴄᴏᴄᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи хɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ у ʙᴀᴄ ʙ ᴄᴇʍьᴇ ᴨᴩиняᴛᴏ у уᴋᴩᴀинцᴇʙ ʙ нᴏᴦи ᴨᴩиᴨᴀдᴀᴛь и ᴋ хую ᴄʙᴏᴇй ᴨᴀᴄᴛью ᴛянуᴛᴄя? я ᴨᴩᴏᴄᴛᴏ ниᴋᴀᴋ нᴇ ʍᴏᴦу ᴨᴏняᴛь ᴋᴀᴋᴏᴦᴏ хуя ᴛы ᴄын ɯᴧюхи ɜᴀ ʍᴀᴛᴇᴩью ᴄʙᴏᴇй ᴨᴏʙᴛᴏᴩяᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄынᴋу ɯᴀᴧᴀʙы ᴛᴇ нᴏᴦи ᴩᴀᴄхуяᴩиʍ ʙ ʍяᴄᴏ ɜᴀ ᴛᴏ чᴛᴏ ᴛы уᴄᴄыᴋᴀнный ᴨидᴀᴩᴀᴄ ᴏᴛ ʍᴏᴇй ɜᴀᴧуᴨы бᴇᴦᴀᴇɯь ᴧᴏɯᴏᴋ жᴀᴧᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯь ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴛы чё ᴛуᴛ удуʍᴀᴧ ᴄᴛᴇᴩᴨᴇᴛь ʍᴏи ᴄᴏᴏбщᴇния чᴛᴏ-ᴧи бᴇᴩи хуя нᴀʙᴇᴩни и ᴏᴛᴨᴏᴩ ᴏᴩᴦᴀниɜуй ᴛᴇᴩᴨиᴧᴏиднᴏᴇ ᴨᴏᴄʍᴇɯищᴇ ᴛя ᴛуᴛ ʙᴄё ʙ хᴀᴩю ᴇбуᴛ ᴨᴏᴋᴀ ᴛы ᴛᴇᴩᴨиɯь и ᴇщё бᴏᴧьɯᴇ ᴨᴏɜᴏᴩиɯьᴄя ну дᴀʙᴀй бᴧяᴛь хᴏᴛь хуй ᴏᴛбᴇй ʍᴏй нᴇдᴇᴇᴄᴨᴏᴄᴏбный ᴩᴇбёнᴏᴋ ᴨᴩᴏᴄᴛиᴛуᴛᴋи ᴏᴨущᴇнный чиᴄᴛᴏ ʍнᴏю и ᴋᴀждыʍ ᴋᴛᴏ ᴛᴇбᴇ ʙ ᴇбᴀᴧᴏ хᴀᴩᴋᴀᴧ ᴨᴏᴋᴀ ᴛы ᴛᴀᴋ жᴇ ᴛᴇᴩᴨᴇᴧ нᴀхуй ᴨᴩᴏбᴧядинᴏɜᴀᴧуᴨинᴄᴋий ᴋᴀждыʍ ɜᴀᴄʍᴇянный ᴨᴀᴩᴀɯниᴋ бᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀхуᴇᴛь ʍнᴇ ᴋᴀжᴇᴛᴄя ᴛы ᴨᴇᴩʙый ᴋᴛᴏ ɜᴀᴧуᴨᴇнь ᴛᴀᴋ яᴩᴏᴄᴛнᴏ нᴀᴄᴀᴄыʙᴀᴇᴛ ɜнᴀя чᴛᴏ ᴏᴨᴨᴏнᴇнᴛ уᴋᴩᴀинᴇц ну дᴀʙᴀй ᴇщё ᴨᴀᴩу ʍинуᴛ нᴀᴄᴧᴀждᴀйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴛᴏᴨᴏᴩᴏʍ ᴇбᴧᴇᴛ нᴇ уᴇбᴀɯиᴧ ᴛʙᴏй ᴋᴩиʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀɯуᴦᴀнный ᴄын ɯᴀᴧᴀʙы ᴄᴏбᴇᴩиᴄь ᴄ ᴄиᴧᴀʍи и ᴏᴛ хуя ʍᴏᴇᴦᴏ ᴏᴛбᴇйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴋᴏᴧᴇни нᴇ ᴨᴇᴩᴇᴧᴏʍᴀᴧ ᴛᴩёхɜубᴏʍу ᴨидᴏᴩу ᴋᴏᴛᴏᴩый ʍнᴇ хуй ᴨᴩиᴋуᴄыʙᴀя нᴀᴄᴀᴄыʙᴀᴇᴛ ᴀ ну ᴋᴀ ᴋᴧᴏунич дᴀʙᴀй ᴛы ᴨᴏᴛᴇᴩᴨиɯь чᴧᴇн ᴨᴏᴋᴀ я ᴛᴇбя нᴇ ᴏᴛᴨиɜдᴏɯиᴧ ᴀᴩʍᴀᴛуᴩᴏй ᴋᴀᴋ ᴛʙᴏю бᴀбᴋу ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴩᴏᴄᴛᴏ нᴀ ʍᴇᴄᴛᴇ ᴨᴏʍᴇᴩᴧᴀ нᴇ дᴏᴄᴏᴄя ʍнᴇ хуяᴩу ᴀ нᴀ ɜᴀʍᴇну ᴨᴩибᴇжᴀᴧᴀ ᴛʙᴏя ᴦᴏᴧᴀя ʍᴀʍᴀɯᴀ ɯᴀᴧᴀʙᴀ чᴇᴩнᴏʍᴀɜᴀя ᴋᴏᴛᴏᴩᴀя ʙᴄᴇᴦдᴀ хᴏхᴧᴀʍ ᴏбᴄᴀᴄыʙᴀᴧᴀ чᴧᴇны бᴇɜ ᴏᴄᴛᴀнᴏʙᴏᴋ нᴀ ᴏᴛдых и дᴇᴧᴀᴧᴀ ϶ᴛᴏ ᴏᴨыᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ ʙ ᴋуᴩᴄᴇ ɜнᴀᴧ ᴧи ᴛы нᴏ ᴏᴛᴄюдᴀ ᴛы ᴄ цᴇᴧыʍ ᴇбᴀᴧьниᴋᴏʍ нᴇ ʙыйдᴇɯь ʙᴇдь я ᴛᴇбᴇ ᴇᴦᴏ ʍᴏᴧᴏᴛᴋᴏʍ ᴏᴛᴏбью ɜᴀ ᴛᴏ чᴛᴏ ᴛᴇᴩᴨиɯь ᴛᴀᴋ ᴨᴇниᴄ и ᴛы будᴇɯь ʍяᴄᴏʍ бᴇᴄᴨᴏᴧᴇɜныʍ ᴏб ᴋᴏᴛᴏᴩᴏᴇ нᴏᴦи дᴀжᴇ ʙыᴛиᴩᴀᴛь нᴇ будуᴛ ибᴏ ᴛʙᴏй ᴇбᴧᴇᴛ быᴧ ᴨᴩи жиɜни нᴀᴄᴛᴏᴧьᴋᴏ ᴦᴩяɜныʍ чᴛᴏ ᴇᴦᴏ ᴄᴏ ᴄᴩᴀᴋᴏй ᴨуᴛᴀᴧи и ᴛудᴀ хуи ᴨихᴀᴧи ᴨᴩᴏᴄᴛᴛ нᴀхуй ᴋᴀждый ʙᴄᴛᴩᴇчный ᴛᴇбᴇ чᴇᴧᴏʙᴇᴋ ᴛᴇбᴇ хуй ʙ ᴩᴏᴛ нᴀᴄᴏʙыʙᴀᴧ ᴨᴏᴋᴀ ᴛы ᴄ удᴏʙᴏᴧьᴄᴛʙиᴇʍ ᴛᴇᴩᴨᴇᴧ ᴋᴀᴋ и ᴄᴇйчᴀᴄ ϶ᴛᴏ дᴇᴧᴀᴇɯь ᴨᴏᴋᴀ ᴛя ᴇбуᴛ хᴏхᴧᴏᴄᴛᴀнцы бᴧя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй ᴛᴇᴦни ʍᴇня ᴇᴄᴧи ᴛы ᴄᴏᴄᴀᴧ хуи ʙᴄю ᴄʙᴏю ᴏᴄᴏɜнᴀнную жиɜнь, ᴏᴛʙᴇᴛь нᴀ ᴧюбᴏᴇ ʍᴏё ᴄᴏᴏбщᴇниᴇ ᴇᴄᴧи ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ᴄ ᴩᴏждᴇния нᴀ хуи ᴋидᴀᴧᴀᴄь бᴇɜ ᴨᴧᴀᴛы нᴀ ϶ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я буду яᴄнᴏ и ᴋᴩᴀᴛᴋᴏ ᴛᴇбᴇ ᴋᴀждый ᴩᴀɜ ᴏбъяᴄняᴛь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴨᴩᴏᴄᴛиᴛуᴛᴋᴀ дᴇɯёʙᴀя ʍнᴇ хуй ᴨᴏᴄᴀᴄыʙᴀᴧᴀ бᴇɜ ᴨᴩичины нᴀ ϶ᴛᴏ ну чиᴄᴛᴀя ɯᴀᴧᴀʙᴀ ᴨᴩᴏᴄᴛᴏ ᴛᴀᴋих ᴇщё ᴨᴏиᴄᴋᴀᴛь нᴀдᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶й ᴦниᴧᴏɜубый ᴄын ɯᴧюхи ᴏᴛɜᴏʙиᴄь ᴨᴧᴀчᴇʍ ᴋᴏᴛᴏᴩый ни нᴀ ᴄᴇᴋунду нᴇ уᴛихᴀᴇᴛ дᴀжᴇ чиᴛᴀя ϶ᴛᴏ ᴛы ᴨᴧᴀчᴇɯь и ʙ ᴀхуᴇ ᴄидиɯь ᴋᴀᴋ жᴇ я ϶ᴛᴏ уᴦᴀдᴀᴧ, нᴏ я жᴇ ᴛᴇбᴇ ᴄᴇйчᴀᴄ ʙ ᴛʙᴏё ᴄʙинᴏᴩыᴧᴏ хуй ᴨихᴀю и ᴄᴧыɯу ᴋᴀждᴏᴇ ᴛʙᴏё ʙᴄхᴧиᴨыʙᴀниᴇ ᴋᴀᴋ ᴄучᴇчᴋᴀ ᴛы нᴏᴇɯь ʙ ᴨᴇниᴄ ᴨᴏᴋᴀ нᴀд ᴛᴏбᴏй нᴀᴄʍᴇхᴀᴇᴛᴄя ᴛᴏᴧᴨᴀ ᴛʙᴏих ᴇбыᴩᴇй ᴏᴛ ᴋᴏᴛᴏᴩых ᴛы дᴀжᴇ нᴇ ʙ ᴄиᴧᴀх ᴏᴛбиʙᴀᴛьᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏᴋᴀ чᴛᴏ нᴇ ᴀнниᴧиᴦиᴩᴏʙᴀн ʍᴏиʍ чᴧᴇнᴏʍ ᴄынᴏчᴇᴋ ᴩуᴄᴏᴄʙинᴄᴋᴏй хуᴇᴄᴏᴄᴀᴧᴋи нищᴇнᴄᴋᴏй ᴋᴏᴛᴏᴩый ʍнᴇ ᴛуᴛ хуя нᴀᴛᴏчиᴛ яɜыᴋᴏʍ ᴄʙᴏиʍ ᴨᴏᴋᴀ я ᴛʙᴏю ʍᴀʍᴀɯу ʙ уᴦᴧу ᴋᴀᴋ ᴄʙинью ᴇбᴀную ɜᴀбью ɯᴧюху ᴛᴀᴋую ᴨуᴛиниᴄᴛᴄᴋую дᴀʙᴀй ᴛᴇᴨᴇᴩь ᴨᴏ ᴨᴏᴩядᴋу ᴨᴩᴏйдᴇʍᴄя, ᴛᴀᴋ ʙᴏᴛ, я ᴇбᴀᴧ ᴛʙᴏю жиᴩную ʍᴀʍᴀɯу ᴨᴏᴋᴀ ᴛʙᴏй ᴏᴛᴇц иᴄᴛᴇᴋᴀᴧ ᴋᴩᴏʙью ᴏᴛ ᴦᴩᴀнᴀᴛы ᴄбᴩᴏɯᴇнᴏй ᴄ уᴋᴩᴀинᴄᴋᴏᴦᴏ дᴩᴏнᴀ нᴀ ᴋᴏᴛᴏᴩый нᴀᴄᴏᴄᴀᴧᴀ ʍᴀᴛухᴀ ᴛʙᴏя и ᴏᴛдᴀʙɯи дᴇньᴦи ᴨᴏд нᴀᴨᴏᴩᴏʍ хуя ʍᴏᴇᴦᴏ ʙᴇдь дᴏбᴩᴏʙᴏᴧьнᴏᴄᴛи ᴏᴛ нᴇё ʍᴏжнᴏ яʙнᴏ нᴇ ждᴀᴛь и ʍᴏжнᴏ ᴧиɯь ᴇё ɜᴀᴄᴛᴀʙиᴛь ᴨᴇниᴄᴏʍ ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴏᴄᴧуɯнᴏ будᴇᴛ ᴨᴩиᴋᴀɜы иᴄᴨᴏᴧняᴛь ᴋᴀᴋ ᴄучᴋᴀ нᴀ ʙᴄю ᴦᴏᴧᴏʙу ᴏᴛбиᴛᴀя уᴋᴩᴀинᴄᴋиʍи чᴧᴇнᴀʍи хᴇхᴇ 𓆩ꏢ𓆪"]
                await self.client.send_message(message.peer_id, f"{shapka} {choice(wablon1)}", schedule=timedelta(minutes=time))
                time+=time1


    async def  rwmcmd(self, message):
        """[задержка в секундах] [шапка] [reply]"""
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "медиа модуль выключен")
            return
        await utils.answer(
            message,
            "медиа модуль включен",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        media = reply.media
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            wablon2 = [" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴇɜᴀʍᴇдᴧиᴛᴇᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴄʍᴏᴛᴩя нᴀ ᴄᴧᴏжнᴏᴄᴛи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴨᴩиʙычᴋᴇ ᴛы ʍнᴇ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ ᴄᴨᴇᴩʍᴏй ɜᴀᴧью 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ʍнᴇ ᴛᴇчёᴛ ᴋᴩᴏʙь ᴄ бᴩюхᴀ ᴛʙᴏᴇᴦᴏ бᴀᴛи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏ ʍнᴇ ᴛᴇчёᴛ чиᴄᴛᴀя ᴋᴩᴏʙь уᴋᴩᴀинцᴀ, ʙᴏ ʙᴩᴇʍя ϶ᴛᴏᴦᴏ жᴇ ᴛы чуᴩᴋᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ɸуᴧᴧ ᴇбᴀᴧᴇ ᴛᴇ ʙ ᴩᴏᴛ ᴄᴄу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛᴇбя ᴋᴀᴋ ᴇбᴀᴧи ᴋᴩᴀᴄных ʙ 44 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюхи хᴇх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇчнᴏ ᴦᴏᴛᴏʙ ᴛᴇбя ᴨᴏᴇбыʙᴀᴛь бᴇᴄᴨᴧᴀᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɯёʙую ᴨᴩᴏᴄᴛиᴛуᴛᴋу ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴧищᴇ ʙ хуй ʙᴏᴛᴋни 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄёɯь ᴋᴀᴋ ᴄᴏᴄуᴛ ʙᴀᴦнᴇᴩяᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ʙᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи уᴇбищᴇ ᴩуᴄняʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀɜᴏʙ ᴛя ᴇбёᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴩиʙыᴋ ᴛᴀᴋ хуи ᴄᴏᴄᴀᴛь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> удᴏбнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя нᴀ ᴩᴏᴄᴄийᴄᴋᴏʍ яɜыᴋᴇ чᴛᴏбы ᴛы ᴨᴏняᴧ ᴋᴀᴋᴏй ᴛы ᴏᴨущᴇнный ᴄын ɯᴧюхи) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏɯибᴀяᴄь ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴏᴧᴦᴏ ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴩᴏᴄᴄиянᴄᴋий ᴄын бᴧяди ᴛуᴛ нᴇ хᴩюᴋᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɸᴇᴋᴀᴧищᴇ ᴄᴏжᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиʙычнᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛя ᴨᴏᴩᴇɜᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй яɜыᴋ нᴀ чᴧᴇнᴇ, чё ᴛы ᴏᴛцу ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛы ᴄ хуя ʍнᴇ ᴋᴩичᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы унижᴇннᴀя ᴄʙинᴏᴨᴄинᴀ ᴇбᴧищᴇ ᴛᴇ ᴛуᴛ ᴩᴀᴄᴋᴀᴛᴀᴧ ᴄучᴋᴇ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чᴏ ᴛᴇᴩᴨиɯь дᴇбиᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨуᴛиниᴄᴛ ᴛы хуй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛиᴋ ɯᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛᴇбя ʙ ᴛʙᴏй ᴩᴏᴛ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ ʍᴀʍᴇ ᴨᴏд ɜᴇᴩᴋᴀᴧьныʍ ʙᴏɜдᴇйᴄᴛʙиᴇʍ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ɜᴀᴋᴏнчиᴧ ᴛᴩᴀхᴀᴛь ᴛʙᴏю ᴄᴇᴄᴛᴩу ᴋᴏᴦдᴀ ᴛʙᴏй ᴏᴛᴇц ᴨᴏᴩʙᴀᴧ ᴛᴇбᴇ ᴀнᴀᴧ, ᴀ ᴛы иɜ ʙᴏɜʍущᴇния чᴛᴏ ᴄ хуя ᴋᴩиᴋнуᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴨᴀᴄᴛь, ᴀ ᴛы чᴛᴏ ʍнᴇ ʙ хуй ᴏᴩᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴋᴩᴏй ᴄʙᴏё ᴇбᴧищᴇ ᴨᴀᴩɯиʙᴏᴇ, ᴇбᴧᴀнихᴀ ᴄᴛᴩёʍнᴏʙыᴦᴧядящᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чё ᴛы ʙ хуй ᴛᴀʍ ᴄᴋуᴧиɯь? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи хᴀᴩчᴋи ʙ ᴛʙᴏё ᴇбᴧᴏ, дᴇбиᴧᴋᴀ ᴩуᴄняʙᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴄ хуя ʍᴏᴧʙиɯь ʙᴄё ᴛы бᴇɜ иᴄᴋᴧючᴇний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛʙᴇᴛь ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇᴄᴧи ᴄᴩᴀᴧи нᴀ ᴛя ᴏᴛʙᴇᴛь ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴛᴏ ᴛᴇбя ᴇбᴀᴧ ᴏбʍᴀни ᴄᴇбя жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴛᴇбя яɜыᴋ нᴀ хуᴇ чᴛᴏ ʍᴀʍᴇ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴦᴀдᴀй жᴇᴧᴀниᴇ ʙ ʙидᴇ хуя ʙ ᴩᴏᴛ ᴄᴇбᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴛᴏ ᴛᴇбᴇ нᴀ ϶ᴛᴏ ʙᴄё бᴀбᴋᴀ хуᴇʍ ʙ ᴩᴏᴛ дᴀᴧᴀ ᴇᴄᴧи дᴏ и ᴨᴏᴄᴧᴇ у ᴛᴇбя яɜыᴋ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я бᴏᴦ ᴨᴩᴀʙды ᴀ ᴛы ᴋᴛᴏ ᴨᴩᴇдᴄᴛᴀʙьᴄя ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀᴋ ᴋᴀᴋᴏᴇ ᴨᴩᴇдᴄʍᴇᴩᴛнᴏᴇ ᴄᴧᴏʙᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи быᴧᴏ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨᴩᴀʙдᴀния ᴛуᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ниᴋᴏᴦдᴀ нᴇ будᴇɯь бᴏᴦᴏʍ ᴨᴩᴀʙды и ʙᴄᴇ ᴛʙᴏи ᴄᴧᴏʙᴀ ʙыɯᴇ и нижᴇ будуᴛ ᴏᴛʍᴇнᴇны 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴛы ᴄʙᴏю ᴩᴏдную ʍᴀᴛь убиᴧ ᴏᴛᴨиɯи нижᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴏ ᴛы бᴀбᴋᴇ ʙ ᴋᴧиᴛᴏᴩ ᴦᴏʙᴏᴩиᴧ яɜыᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄё чᴛᴏ ᴛы ᴏᴛᴨᴩᴀʙиᴧ быᴧᴏ нᴀᴨиᴄᴀнᴏ ʙ ʍиᴩᴇ ʙᴩᴀнья ᴄ яɜыᴋᴏʍ ᴨиɜдᴀбᴏᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иᴦнᴏᴩᴏʍ ᴩᴏдᴏᴄᴧᴏʙную убᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏʙᴩи ʙ ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ уʍᴇю ʙᴩᴀᴛь, ᴛы ᴄын ɯᴧюхи  𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴩуᴄᴏᴄʙинᴄᴋᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᏌᴋrᴀiniᴀnᏒᴀgᴇ ᴇбᴀɯиᴛ ᴦᴧᴏᴛᴋу ᴛᴇ 𓆩ꏢ𓆪",
"  ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>нᴀ ᴧᴇᴄᴏᴨиᴧᴋᴇ ᴛя ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ нᴏй ᴄʙинᴏᴩуᴄ ᴏᴨущᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу хуᴇʍ ᴛᴇ ᴨᴇᴩдᴀᴋ нᴀ ᴧᴇᴦᴋᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀᴩᴋᴀю ᴛᴇ ʙ ᴇбᴀᴧᴏ дуᴩᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуя ᴨᴏᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧ ᴛᴇ ʙ ᴩᴏᴛ хуй ᴄᴏ ᴄᴧᴏʙᴀʍи ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏбᴏᴄᴩᴀᴧ ᴛᴇбᴇ ᴇбᴀᴧᴏ и чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу, ᴀ ᴛы чᴛᴏ ᴇй ᴋᴩичᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴩᴀᴧ нᴀ ᴛʙᴏё ᴇбᴧищᴇ ᴄᴏ ᴄᴧᴏʙᴀʍи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄᴋᴩиᴨᴛᴏʙᴀнᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя удуɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇйчᴀᴄ ᴛᴇбя ᴇбёᴛ хᴏхᴏᴧ, ᴩᴀᴄᴋᴩыʙᴀй ᴄʙᴏю ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴀᴧ ᴛы ᴄынᴏᴋ ɯᴧюɯᴇчᴋи ᴨиɜдᴏᴨᴩᴏʙᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴀᴄᴀй хуяᴩу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇбᴇ бᴀбᴋᴀ ʙ ᴩᴏᴛ, чᴛᴏ ᴛы нᴀ ϶ᴛᴏ ᴄ хуя? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴛᴇ хуᴇʍ ᴋᴩᴀᴄиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ɜуб ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хую ᴛы ᴋᴩуᴛиᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴋᴏнчᴀᴧ ᴛᴇбᴇ нᴀ ᴧицᴏ, ᴀ ᴛы чᴛᴏ ᴄᴋᴀɜᴀᴧ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛʙᴏё ᴩыᴧᴏ, ᴀ ᴛы чᴛᴏ нᴀ ϶ᴛᴏ бᴀбᴋᴇ ᴄ хуᴇʍ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴄʙᴏё ʙᴀᴧьни ᴄын бᴧяди ᴏᴛᴄᴛᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ᴛя хᴏхᴧы хᴏɜяᴇʙᴀ ᴛʙᴏи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀɯу ᴄʙинᴏᴩуᴄню и ᴛы нᴇ ᴨᴏᴄᴧᴇдний 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴇбуᴛ ʙᴄ ᴩɸ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴋᴩиᴄᴛᴀᴧичнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩʙу ᴛᴇбя ᴋᴀᴋ ᴩʙуᴛ ʙᴀᴦнᴇᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбуᴛ ʍᴀʍᴀɯу ᴛᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи ʙяᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏᴩʙᴀᴧ ɜᴩᴋ ᴄ-300 ʙ ᴋᴏᴛᴏᴩᴏʍ быᴧ ᴛʙᴏй ᴏᴛᴇц ᴄ ʙᴀᴦнᴇᴩᴀ) 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴛᴩᴏᴧᴧиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴋᴩыᴧ жиʙᴏᴛ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴄᴀᴛᴀнᴏй хуяᴩиʍ ᴋᴀᴦᴏᴩ и ᴇбᴇʍ ᴛʙᴏю ʍᴀʍᴀɯᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ дуᴧᴏ ᴛᴀнᴋᴀ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи нᴀᴄᴀдиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴩᴇнᴏй ᴨᴏдᴏᴩʙᴀᴧ ᴛʙᴏᴇᴦᴏ бᴀᴛю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴩᴇжу ᴛᴇ ᴦᴧᴏᴛᴋу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄᴛᴀᴧ нᴀ ᴄʍᴇᴩᴛный бᴏй и ɜᴀᴩубиᴧ ᴛʙᴏᴇᴦᴏ бᴩᴀᴛᴀ ᴋᴀᴛᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴨᴩиниʍᴀᴇᴛ ʙ ᴄᴇбя ʙᴄё чᴛᴏ ʙᴧᴇɜᴇᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя хᴀᴩᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуйцᴏʍ ᴛя ᴩᴀɜʙᴧᴇᴋᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛя нᴀ ᴧᴏᴨᴀᴛу нᴀᴄᴀжу и чиᴄᴛᴏ ᴋᴀᴋ ᴄиʍбу ᴩᴀᴄᴋᴩучу и ᴏб ᴄᴋᴀᴧу уᴇбу ᴛᴀᴋую дуᴩу ᴛуᴨᴏᴩыᴧую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴏʍᴀᴧ ᴛᴇ ᴄᴨину хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛхуяᴩю ᴛя ᴨᴏ ᴧбу чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уᴇбᴀᴧ ᴛᴇбя ᴄ нᴏᴦи ᴨᴏ ᴩᴇбᴩᴀʍ ᴛʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʍᴇᴩᴄᴀй ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧый ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бью ᴛя ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ᴋᴏɯʍᴀᴩиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ᴄᴨᴀᴄибᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь? ᴏᴛʙᴇᴛ ʙ хуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀдуʍчиʙᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ дуᴩᴀ ᴇбᴀнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɯᴧᴀ нᴀхуй ᴛᴇбᴇ ᴄᴋᴀɜᴀᴧи ᴨидᴀᴩᴀᴄᴋᴀ нᴇдᴏᴩᴀɜʙиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧюнуᴧ ʙ ᴛя ɜᴀᴧуᴨᴏй, ᴨᴏᴋᴀ ᴛы хᴀᴩᴋᴀᴇɯь ʙ ɜᴇᴩᴋᴀᴧᴏ ᴄ хуя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ жᴀᴧᴋий ᴄынᴏчᴇᴋ хуᴇᴄᴏᴄᴀᴧᴋи нищᴇй чё ᴛы ᴛуᴛ ɜᴀбыᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ɜᴀᴋᴩᴏй ужᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇᴄᴨᴩᴇᴩыʙнᴏ ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ уᴋᴩᴀинᴄᴋᴏй ʍинᴇ ᴛʙᴏй ᴏᴛᴇц ᴨᴏдᴏᴩʙᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇхуй ᴧᴇɜᴛь, ᴨидᴏᴩᴀɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄи чуɯᴋᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴄᴏᴄᴇɯь ᴄынᴏᴋ бᴧяди ᴏᴨущᴇннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴇ чуᴩᴋᴏхᴀч ᴛы нᴀхуй ᴄᴏᴄнуᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴧучиᴧ ᴛы ᴨᴏ ᴇбᴀᴧу ɜᴀᴧуᴨᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴦдᴀ ᴛя ᴨᴏᴇбᴀᴧи ᴛᴀᴋ жᴇ ᴋᴀᴋ и ᴛы ʍᴏᴧчᴀᴧи? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜбᴩᴀннᴏ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ бᴏᴋу ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴛᴏʙ ᴛᴇ бᴇᴄᴋᴏнᴇчнᴏ нᴀ ᴋᴧыᴋ ᴏɸᴏᴩʍᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ ᴧюбʙи ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиɜдᴇц ᴛы нᴀᴄᴏᴄᴀᴧ хуя ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴋᴀйɸ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩᴨи чᴧᴇн ʙ ᴦᴏᴩᴧᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴄыᴋᴧиʙᴏ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴇʍ ᴛя чинᴦиɜхᴀнᴀ ᴇбᴀнᴏᴦᴏ ᴄ буᴩяᴛии нᴀхуй хᴀɜхᴀɜɜᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴄын ɯᴧюхи ᴋᴏᴨыᴛный ɜᴀчᴇʍ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴄʙин ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙяᴧый хуй ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴄᴛᴀнциᴏннᴏ ᴄᴏᴄёɯь ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя, ᴩуᴄᴏᴄʙин 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴇᴩᴛиᴋᴀᴧьнᴏ ᴛᴇбя ᴨᴏиʍᴇᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴏинᴄᴛʙᴇннᴏ ᴛᴇбя ᴨᴏᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ ᴄын ᴄʙиньи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄʙинᴏᴩыᴧᴏ ᴛʙᴏё ᴨᴏᴇбᴇʍ, дᴇᴦᴇнᴇᴩᴀᴛины ᴄын 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦʙᴏɜдь ᴋ ᴩуᴋᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋ ᴇбᴀᴧу ᴛᴇ диᴧдᴀᴋ жᴇᴧᴇɜный ᴨᴩиᴧᴇᴨиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧᴏ ᴄʙᴏё ᴨᴏᴨᴩᴀʙь ᴋᴩиʙᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи нᴀᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ ᴨᴩичʍᴏᴋᴀʍи ʙᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> у ᴄᴛᴏʍᴀᴛᴏᴧᴏᴦии ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴀᴩᴀɯᴇ я ᴄᴩᴀᴧ и ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴛᴀʍ жᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴩᴏʙᴀᴛи ᴛʙᴏй ᴩᴏᴛ ᴛᴩᴀхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄᴏᴄᴀᴧ ᴛы нᴀ ᴨᴀчᴋу ᴄухᴀᴩиᴋᴏʙ бᴧя ᴇбᴀнᴀᴛ нищᴇнᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴧяᴛь ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩу ʙᴄᴏᴄи ᴄынᴏᴋ бᴧядины 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇᴩяйᴄя нᴀхуй ᴨᴏᴋᴀ ᴛᴇ ᴇбᴀᴧᴏ ᴛуᴛ хуᴇʍ нᴇ ᴩᴀᴄᴋʙᴀᴄиᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ ɜᴀᴧуᴨы ʍᴏᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴧуᴨу жᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏжᴩи дᴇᴩьʍᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛᴇбя у ɯᴋᴏᴧы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ᴦᴧᴀɜ ʙыᴩʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴨᴧяжᴇ чёᴩнᴏᴦᴏ ʍᴏᴩя ᴛʙᴏю ʍᴀᴛь ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀᴧбᴀᴇб ɯᴧᴀнᴦ дᴩᴏчи ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏбᴩᴀннᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴩу ᴋᴏᴦдᴀ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴧюби ᴄᴏᴄᴀᴛь ᴋᴀᴋ ᴧюбиɯь ᴄᴦᴧᴀᴛыʙᴀᴛь ᴄын ɯᴧюхᴛ хᴀɜ϶ᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ Ꮧёɯᴋᴀ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяᴩю ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀбиᴧ ᴛя ʙ уᴦᴧу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴨинᴀᴧ ᴛя хуᴇʍ дуᴩу ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇᴨᴏʙᴛᴏᴩиʍᴏ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛʙᴏᴇй ᴨиɜдᴇ иᴦᴩᴀᴧᴄя, ᴛёᴧᴋᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨиɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴋᴀᴋ бᴀᴩᴀн идᴇᴛ ᴄʙᴏиʍи ᴦубᴀʍи нᴀ ʍᴏй хуй нᴀ ᴛᴀᴩᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴧᴏᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏᴋɜᴀᴧᴇ ᴛя ᴇбу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴦиᴧьныʍ ᴋᴩᴇᴄᴛᴏʍ ᴛʙᴏᴇᴦᴏ дᴇдᴀ ᴇбᴀᴧ ᴛᴩуᴨ ᴛʙᴏᴇй бᴀбᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴇ ᴏᴛбᴩᴀᴄыʙᴀй ᴋᴏᴨыᴛᴀ ᴏᴛ ʍᴏᴇᴦᴏ чᴧᴇнᴀ ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴩиʙᴏᴇбᴧый ᴄын ʍᴩᴀᴋᴏбᴇᴄия ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴧᴏᴄᴋᴏᴇбᴧый ᴨидᴏᴩᴀᴄ нᴀ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏбиᴧ ᴛʙᴏй чᴇᴩᴇᴨᴏᴋ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀбᴄиянинᴀ ᴛя ᴨᴏᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴏ ᴋᴀᴋ ᴛᴀʍ ᴩᴏᴄᴄиянцы хᴏхᴧᴀʍ ᴄᴏᴄуᴛ ʍдᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ чᴇᴛʙᴇᴩᴇньᴋᴀх ʍнᴇ ᴄᴏᴄᴀᴧᴀ ʍᴀᴛь ᴛʙᴏя 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчуʙᴄᴛʙуй хᴏᴛь ᴄᴇйчᴀᴄ ɜᴀᴨᴀх ᴄʙᴏбᴏды и ʙыбᴇᴩи чᴏ ᴄᴏᴄᴀᴛь будᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴏᴧчи ᴄ чᴧᴇнᴏʍ ʙᴏ ᴩᴛу ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ʙᴏᴧьнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴨᴇниᴄ ʍᴏᴧчᴀниᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чᴛᴏ Ꮯᴀɯᴋᴀ ᴄᴏᴄᴀᴛь ᴛᴏ будᴇɯь ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄиɸᴏɜнᴏй ɯᴧюхи ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀ ᴛʙᴏя нᴀ чᴧᴇнᴇ ᴨᴏᴛухᴧᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴛы чᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ ᴛʙᴏю ʍᴀᴛь чᴧᴇнᴏʍ ɜᴀᴇхᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩᴏᴄᴛᴩᴇᴧиᴧ ᴋᴏᴧᴇни ᴏᴛцу ᴛʙᴏᴇʍу ʙᴀᴦнᴇᴩᴏʍяᴄу ᴇбучᴇʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ ʍᴏнᴇᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴛь ᴛʙᴏю ʙ ᴀнᴀᴧ ᴦᴧᴀдᴋᴏ ᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴇɜ чᴇᴄᴛи ᴏᴛᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуй ᴇбᴧᴏʍ ᴧᴏʙи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴏᴩʙу ᴛᴇ ᴩуᴋи и буду ᴄᴇбᴇ ниʍи дᴩᴏчиᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄʙᴏиʍи ʙиᴄячиʍи ᴄиᴄьᴋᴀʍи дᴩᴏчиᴧᴀ дуᴩᴀ бᴧяᴛь ɜᴀхɜᴀᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴄᴛᴀʙиᴧ ᴩʙᴀныᴇ ᴩᴀны нᴀ нᴏᴦᴀх ᴛʙᴏᴇй ʍᴀʍᴀɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏɯёᴧ и ʙыᴩубиᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴩуниɯᴋᴀ ᴋᴛᴏ ᴄᴩᴀᴧ нᴀ ᴛᴇбя ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ ᴩучᴋи ᴛᴏ дᴩᴏжᴀᴛ у ᴛᴇбя ᴨᴇᴩᴇд ʍᴏиʍ чᴧᴇнᴏʍ ᴩуᴄᴏᴄʙинья ᴛы ᴇбᴀнуᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯиɯь я ᴛᴇбᴇ ᴛуᴛ ᴨᴀᴧьцы буду ᴏᴛбиʙᴀᴛь ᴏдин ɜᴀ дᴩуᴦиʍ ɜᴀ ᴛᴏ чᴛᴏ ᴛы ᴛᴀᴋᴏй ʍᴇдᴧᴇнный ᴄынᴏᴋ ɯᴧюɯᴋи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> иɜ ᴨᴏᴄᴧᴇдних ᴄиᴧ ʙᴏюᴇɯь ᴄ ʍᴏиʍ хуᴇʍ ᴛуᴛ чᴇᴨухᴀ ᴨᴏɜᴏᴩнᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ʙᴏйнᴇ ᴛы ᴄ ʍᴏиʍ хуᴇʍ дᴩᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴄᴧиᴛᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴀʙᴀй ᴄын ɯᴧюхи ᴄᴏбиᴩᴀйᴄя ᴄ ʍыᴄᴧяʍи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇʙᴀᴛᴇᴧь ᴨᴇниᴄᴏʙ ᴛы чᴏ ᴛуᴛ ʙᴄᴇʍ хуй ᴏᴛᴄᴀᴄыʙᴀᴇɯь ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ᴛы ᴨидᴏᴩ жиᴩный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ʙ ᴛя ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄунᴇц хуя ᴛы ʍᴏᴇᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧᴀбᴇйɯий ᴄын ɯᴧюхи ᴏчниᴄь ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴨиɜды нᴇ дᴀᴧ ᴏᴨяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏʙнᴏ ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍбуᴧу ᴛы ᴩᴛᴏʍ ɯᴧиɸᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄунᴇц хуᴇʙ хᴏхᴧᴏʙ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛᴇ ʙ ᴦᴏᴧᴏʙу ʙᴧᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩᴏᴄʙин ᴄᴏᴄᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ʙᴀᴦнᴇᴩ ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩыᴧᴏ ᴛᴇ ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴩᴀɜбиᴧ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩуᴄᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴇднᴏ ᴛᴇ хуй ʙ ᴩыᴧᴏ ᴄᴏʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴀч нᴀ хуй ʍᴏй нᴇ ᴨᴀдᴀй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏʙцᴇᴇб ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуёʍ ᴛя ʙыʙᴇɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴛᴀᴄᴋᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуᴇ ᴛы ᴋᴀᴛᴀᴧᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя биᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя дᴏбиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> диᴛᴀниᴩᴏʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙɜᴏᴩʙᴀᴧ ᴛя хуᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> бᴏʍбᴇɜнᴏ ᴨᴏᴇбᴀᴧ ᴛʙᴏю ʍᴀʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴩᴏᴄᴄиянᴄᴋи ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ ᴩᴀɯиᴄᴛ ᴛы ʙᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь нᴀ ᴩуᴄᴄᴋᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь будᴛᴏ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жуᴛь нᴀ ᴛᴇбя нᴀʙᴏдиᴛ ʍᴏй ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴏᴄᴄиянᴇц ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жᴇᴧᴇɜнᴏбᴇᴛᴏннᴏ ᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛя ᴨᴏᴋᴀ ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀхуй ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴩиᴋуᴄыʙᴀя ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴋᴩыʙᴀяᴄь ᴛы нᴀᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ хуй ʍᴏй ᴛы нᴀᴨᴀᴧ и ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴋᴀждᴏй ᴧᴀʙᴋᴇ ᴨᴀᴩᴋᴀ ᴛʙᴏю ʍᴀᴛь я ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇᴄᴏᴄ ᴩᴀɜбᴇй ᴦᴏᴧᴏʙу ᴄᴇбᴇ ᴏб ᴄᴛᴇнᴋу нᴀхуй ᴨᴏᴋᴀ я ɜᴀняᴛ ᴨᴏᴇбыʙᴀниᴇʍ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴛуᴨᴏᴦᴏᴧᴏʙᴏй ᴄын ɯᴧюхи ᴨᴇᴩᴇᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ʙыᴇбᴀᴧ ᴛʙᴏю ᴄᴇᴄᴛᴩу ʙ ᴩᴏᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴇдᴏᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀʍᴀɯу ᴛʙᴏю чуᴩᴇᴋᴄᴋую ᴨᴏᴇбᴇʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы иɜ чуᴩᴋᴏᴄᴛᴀнᴀ ᴄбᴇжᴀᴧ ᴦдᴇ ᴛᴇбя ʙ ɜᴀᴦᴏнᴇ дᴇᴩжᴀᴧи нᴀхуй ᴋᴀᴋ ᴄᴏбᴀᴋу диᴋую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> буᴩяᴛнᴏ ᴄᴏᴄёɯь ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы диᴋий ᴄын ɯᴧюхи ᴇбᴀᴧᴏ ɜᴀᴋᴩᴏй ᴄʙᴏё ᴀ ᴛᴏ щяᴄ хуи нᴀᴧᴇᴛяᴛ ᴨᴩяʍ ʙ ᴩыᴧᴏ ᴛʙᴏё ᴛᴩᴀхᴀннᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀ дᴏᴧᴦ ᴛы ʍнᴇ хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀᴛи ᴛы дᴩᴏчиᴧ ʍнᴇ ᴨᴩияᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏбᴧᴀᴦᴏдᴀᴩиᴧ ᴛя чᴧᴇнᴏʍ ᴨᴏ ᴦубᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀщᴇᴋᴀнᴇц ᴇбᴧищᴇ ᴨᴩиᴋᴩᴏй ᴄʙᴏё ᴨᴩᴏᴛиʙнᴏᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуи ᴨихᴀᴧи ᴛᴇ ʙ уɯи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴇᴦᴏдня ᴛᴇбᴇ ᴦᴧᴀɜᴀ хуяʍи ʙыᴋᴏᴧяᴛ ᴄыниɯᴋᴇ ɯᴧюхи ᴛᴀᴋᴏʍу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀᴋ жидᴏᴄʙин ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏя ʍᴀᴛь ᴩᴏᴄᴄийᴄᴋᴀя хуᴇᴄᴏᴄᴀᴧᴋᴀ ɜᴀ ᴋᴏᴨᴇйᴋи ᴄᴏᴄёᴛ и ᴋиᴛᴀйцы ᴇё ᴄᴇбᴇ нᴀ нᴏчь бᴇᴩуᴛ ᴨᴏᴋᴀ ᴛы ᴄидиɯь и ждёɯь ᴇё 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏ ᴨᴩиʙычᴋᴇ уʙᴏᴩᴀчиʙᴀᴇɯьᴄя ᴏᴛ хуя будᴛᴏ ᴏᴛ ᴄᴨᴇᴩʍы ᴄʙᴏᴇᴦᴏ ᴏᴛцᴀ ᴀᴧᴋᴀɯᴀ ᴇбучᴇᴦᴏ бᴧя хᴀхᴀхᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴧиᴛᴇᴧьнᴏ ᴛы ʙыдᴇᴩжиʙᴀᴧ ᴄᴨᴇᴩʍу ʙ ᴦᴏᴩᴧᴇ ᴛᴏᴧьᴋᴏ нᴀхуя нᴇ ᴨᴏняᴧ я 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʙɜяᴧ ᴨᴇᴩᴇдыɯᴋу чᴛᴏбы нᴇ ᴄᴏᴄᴀᴛь хᴏᴛь ʍинуᴛу ᴄʙᴏᴇй жиɜни ᴋᴏᴛᴏᴩᴀя ᴋᴏнчиᴛᴄя ᴋᴏᴦдᴀ ᴛы ᴨᴩиᴇдᴇɯь ʙ Ꭹᴋᴩᴀину ʙᴏᴇʙᴀᴛь ʙᴇдь ᴛы ᴏʙцᴀ ᴄᴧᴀбᴀя ᴋᴏᴛᴏᴩᴏй ᴀнᴀᴧ ᴦᴩᴀнᴀᴛᴏй ᴩᴀɜᴏᴩʙуᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀᴄʍᴇхᴀюᴄь нᴀд ᴛᴏбᴏй чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нищуᴦᴀн ᴛы ᴄᴏᴄёɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏё ᴇбᴀᴧᴏ ᴄʙᴏᴇй ɜᴀᴧуᴨᴏй ᴄᴋᴩуᴛиᴧ ɯᴏб нᴇ ᴨиɜдᴇᴧ ʍнᴏᴦᴏ ɜᴀ ᴩᴏᴄᴄию ᴄʙᴏю ʙᴇᴧиᴋую ʙᴏ ʙᴄᴇ щᴇᴧи ᴇбᴀную 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʍ ᴛᴇ ᴨᴏ ᴦᴏᴧᴏʙᴇ нᴀᴄᴛучу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи чуᴩᴇᴋᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴋᴄᴛᴀ ᴨидᴏᴩᴀᴄ чуᴩᴋᴏᴄᴛᴀнᴏʙᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> униɜиᴧ ᴛя чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀхуяᴩю ᴛя хуᴇʍ ᴋᴀᴋ ᴏᴋᴋуᴨᴀнᴛᴀ будᴇɯь ᴏдниʍ ᴄ 200ᴋ дᴏхᴧых ᴩᴏᴄᴄиянᴄᴋих ᴄʙинᴏᴨᴄᴏʙ ᴀхɜᴨɜᴨɜᴀᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙыᴩубиᴧ ᴛя хуᴇʍ ᴋᴀᴋ ᴋуʙᴀᴧдᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ʙᴏ ᴩᴛу щᴇᴋᴏᴛᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ну чё ᴛы ᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨидᴏᴩᴀᴄня ᴩᴀᴄᴄиянᴄᴋᴀя хуй нᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴨьёʍ ᴛᴇбᴇ ᴦᴧᴀɜᴀ ᴋ хуяʍ ʙыᴋᴏᴧю дᴇбиᴧᴋᴇ ᴛᴩᴇхɜубᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ хуᴇц ᴄᴧюняʙиᴧ ɜᴀчᴇʍ хᴀчуᴩᴀ ᴇбучᴀя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ ᴩуᴄᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴏᴧᴇни ᴛᴇ ᴨᴇᴩᴇᴧᴏʍᴀю нᴀхуй дуᴩᴇ ᴄᴧыɯиɯь ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ʍᴏй хуй ɜᴀ ᴄʙᴏᴇй ʍᴀʍᴏй дᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуяʍ ᴛя бᴩᴏᴄиᴧ ʙ яʍу ᴦдᴇ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴄ ᴨᴏʍᴏщью хуя ᴛᴏᴧьᴋᴏ чᴛᴏ ɜᴀᴇбᴀɯиᴧ ɸᴀнᴀᴛᴏчᴋу ʙᴀᴦнᴇᴩᴏᴄʙинᴇй ᴄᴏᴄунцᴏʙ ʍᴏᴇᴦᴏ хуя ᴇбᴀнуᴛых нᴀ ᴦᴏᴧᴏʙу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴇᴀᴧьнᴏ ᴛы нᴀ ʍᴏёʍ хуᴇ ᴋᴀᴋ нᴀ ʍᴏᴨᴇдᴇ ᴋᴀᴛᴀᴇɯьᴄя ᴇбᴀнᴀᴛиᴋ ᴄᴀᴧьнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> быᴄᴛᴩᴏ ᴛы нᴀ чᴧᴇнᴇ ᴨᴏᴛух ᴄынᴏᴋ ɯᴧюхи ᴛуᴨᴏдᴏхᴏдящᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴀнᴋиᴄᴛу ᴛы ᴄᴏᴄᴀᴧ чᴛᴏбы ᴏн ᴛʙᴏих ʙᴀᴦнᴇᴩᴏᴄʙинᴇй нᴇ ᴇбᴀɯиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя ᴋᴀᴋ ᴋᴀᴩᴀᴛᴇᴧь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏ ᴋᴀйɸу ᴛя ʙыᴇб 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɜᴀбыᴧ ᴋᴀᴋ ʍнᴇ ɜᴀᴧуᴨу бᴧᴀᴦᴏдᴀᴛную цᴇᴧᴏʙᴀᴧ ? 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴨущᴇнᴇц ᴏᴛъᴇбᴀнный ᴛы ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛёᴧᴋᴀ ᴛы у ᴋᴏᴦᴏ ᴄᴏᴄᴀᴛь учиᴧᴀᴄь ᴏᴛʙᴇᴛ ʙ ɜᴀᴧуᴨу ᴏɸᴏᴩʍи ᴨᴏ ᴋᴀйɸу 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏᴇбᴀᴧ ᴛя и ᴛᴏчᴋᴀ. 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴩᴇжу ᴛʙᴏю ᴦᴏᴧᴏʙу нᴀхуй ᴋᴀᴋ чᴇчᴇнᴇц 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜдᴇᴧᴀᴧᴄя ᴄ ᴛᴏбᴏй ᴋᴀᴋ ᴋᴩᴀᴋᴇн ᴄ ʙᴀᴦнᴇᴩᴏʍяᴄᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴀɸᴏᴄнᴏ ᴛы хуй ᴄᴏᴄᴀᴧ ᴏᴨᴏɜᴏᴩᴇнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы чё ᴇбᴀᴧᴏʍ ᴄʙᴏиʍ нᴀᴄᴏᴄᴀᴧ нᴀ ʍᴀɯину чᴛᴏ-ᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴩᴀɜᴏᴩʙи ᴄᴇбᴇ ᴩᴏᴛ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄёɯь ᴋᴀᴋ нᴀᴩиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴛь ᴛы ᴋᴀᴋ ᴄʙин жиᴩнющий ʍнᴇ хуй ᴄᴏᴄёɯь ᴨᴩяʍ диᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏɜᴏᴩищᴇ ᴋᴄᴛᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀᴄʍᴇиʙᴀюᴛ ᴛᴇбя, ᴀ ᴛы ᴛᴇᴩᴨиɯь чᴧᴇн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы дуᴩᴀ уᴄᴨᴏᴋᴏйᴄя ᴨᴏᴄᴏᴄи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы хуᴇᴄᴏᴄᴀᴧᴋᴀ нищᴀя ᴨᴏɯᴧᴀ нᴀхуй ᴏᴛᴄюдᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙᴄунуᴧ ᴛᴇ хуй ʙ ᴩыᴧᴏ, ᴛᴇᴩᴨи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хуᴇʍ ᴛя ᴋ ᴄᴛᴇнᴇ ᴨᴩибиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбᴀᴧ ᴛᴇбя нᴇ ʍᴀᴧᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴛы ᴨᴩᴇᴋᴩᴀᴄнᴏ ʍᴀᴧᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʍᴀᴧᴀя ᴛы ɯᴀᴧᴀʙᴋᴀ хᴇхᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴀᴧ ʍнᴇ ɯᴋᴏᴧьниᴋ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ᴇбᴀнᴀя ɯᴀᴧᴀʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> хᴇх ᴀᴧьɸᴀч ᴛʙᴏя ʍᴀᴛь ɯᴧюхᴀ ᴛᴀйᴄᴋᴀя ᴏᴛдᴀᴧᴀᴄь ɜᴀ нᴏн ᴄᴛᴏᴨ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏɜᴏᴩный уᴩᴏд ᴛы нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> жиᴩный ᴋуᴄᴏᴋ ʙᴏнючᴇᴦᴏ дᴇᴩьʍᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй ʍинᴇᴛ ᴨᴏхᴏж нᴀ хуйню 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ʍнᴇ чᴧᴇняᴩу ᴄᴏᴄᴇɯь ᴋᴀᴋ бᴇɯᴇный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄиᴧьный ᴏᴛᴄᴏᴄниᴋ ᴛᴀᴋ ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴀ ᴛы ᴋуᴄᴏᴋ ᴨᴏхᴏжᴇᴦᴏ нᴀ дᴇᴩьʍᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇᴩьʍᴏᴇд ᴇбᴀный ɜᴀᴋᴩᴏй ᴨᴀᴄᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦᴏᴩиɜᴏнᴛᴀᴧьнᴏ ᴛᴩᴀхᴀᴧ ᴛʙᴏй ᴀнᴀᴧ бич 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴄᴏᴄи чᴧᴇн ɸᴩиᴋᴏʙᴀᴛый ᴨᴇдиᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын ᴄуᴋи ᴛы чᴇᴩнᴏʙᴀᴛᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇдᴩиᴧᴀ ᴛы ᴩᴀɜуᴋᴩᴀɯᴇнᴏᴇ ʍᴏиʍ чᴧᴇнᴏʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏчᴇʍу ᴛы ʍнᴇ хуй ᴄᴏᴄᴇɯᴧ ᴛᴀᴋ чᴀᴄᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙ ʍнᴇ чᴧᴇн ᴄᴏᴄᴀᴧ ᴇʙᴩидᴇй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄ ʍᴏиʍ чᴧᴇнᴏʍ ʍᴀɜᴏхиᴄᴛ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇʙᴩᴇйᴄᴋᴀя нᴀᴛуᴩᴀ у ᴛᴇбя ᴄ чᴧᴇнᴀʍы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴦниᴧью ᴏᴛ ᴛᴇбя ʙᴏняᴇᴛ ᴨᴇдᴀᴩᴀᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄᴏᴄᴀᴧ ʍнᴇ и нᴇ ᴛᴏᴧьᴋᴏ ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>ᴨᴏ ᴨᴩиᴋᴏᴧу ᴛᴇбя ᴛᴩᴀхᴀю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji>  ʙьᴇбᴀᴧ ᴛᴇбя чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄ хуᴇʍ ʙ ᴩуᴋᴀх ᴛы ʍнᴇ ᴨиɜдиɯь чᴛᴏ-ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ɯᴧюхᴀ ᴋᴏɜᴀцᴋᴀя ᴨᴀᴩᴇнᴇᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴋᴏᴧᴏ ɜᴀᴨᴏᴩᴏжᴄᴋᴏй ᴄичи ᴛы хуй ᴄᴏᴄᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏц ниᴋ ᴨᴇниᴄᴏɸᴀн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я хᴏчу ᴛʙᴏю ʍᴀᴛь ɯᴀᴧᴀʙу ᴛᴩᴀхᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛᴇᴋ ᴦᴇй ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄи чᴧᴇн уᴋᴩᴀинᴄᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ʍнᴇ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴇниᴄᴏʙᴏй ɸᴀᴋᴇᴩ я дᴧя ᴛя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй ʍнᴇ чᴧᴇняᴩу ʍᴏнᴄᴛᴩ ᴋᴀʍᴏʙый 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбя нᴀ ʍᴏдуᴧях ʙыᴇбу ᴄᴧᴀб ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛиɯᴇ ᴄᴏᴄи ᴧᴏх 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛʙᴏй бᴀᴛя ᴋᴏɜᴇᴧ ᴇбᴀный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴀᴄи ᴨᴇниᴄ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> нᴀ ᴄᴀᴧᴏ ᴛᴇбя ᴨуᴄᴛиᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛᴧичный ᴄᴨᴇᴩʍᴏᴨᴩиᴇʍныᴋ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙ 43 ᴦᴏду ᴛᴇбя ʙыᴇбᴀᴧи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛʙᴏй ᴇбыᴩь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄиᴩуй чᴧᴇняᴩу ᴄᴧᴏн 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨиᴄюнᴏɸᴀн ᴛы ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴄᴇɯь ᴋᴀᴋ ᴇбᴀнуᴛый ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛᴇбя ᴩᴀɜъᴇбᴀᴧ я чᴧᴇнᴏʍ ᴄʙᴏиʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ᴨᴀᴛᴧы ʙыᴩʙᴀᴧ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴇбу ᴛя ᴋᴀᴋ ᴦᴏᴧубя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> дᴇɸᴀйᴄя ᴇᴄᴧи ᴛы ᴄын ɯᴧюхи, ᴛᴇᴩᴨи ᴇᴄᴧи ᴛʙᴏй ᴏᴛᴇц ᴨидᴏᴩ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴀждᴏᴇ ᴛʙᴏё ᴄᴧᴏʙᴏ нижᴇ ϶ᴛᴏ хуи ᴧᴇᴛящиᴇ ʙ ᴄᴏᴄᴀᴧᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> чᴧᴇн ᴛᴇᴩᴨᴇᴧᴀ ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ж ᴛя убью нᴀхуй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧᴏ ᴄын бᴧядины ᴛы иɜ ᴄᴇбя нихуя нᴇ ᴨᴩᴇдᴄᴛᴀʙᴧяᴇɯь бᴇᴩи ʍᴏᴇᴦᴏ хуя ʙ ᴩᴏᴛ ᴛᴇᴩᴨиᴧᴏид чё ᴛы 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы жᴇ ɜнᴀᴇɯь чᴛᴏ ʍᴀᴛь ᴛʙᴏю ʙ ᴦᴏᴩᴧᴏ ʙᴄᴇ ᴇбуᴛ нᴀᴄᴧᴇдниᴋ хуя ᴛы ʍᴏᴇᴦᴏ ᴧучɯᴇ ᴨᴏ хᴏᴩᴏɯᴇʍу ᴛᴇᴩяйᴄя ᴨᴏᴋᴀ ᴛʙᴏя ᴦᴧᴏᴛᴋᴀ цᴇᴧᴀ ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴇбᴀнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴏᴨᴧᴇжуй ᴛы чё ᴛуᴛ ᴩᴇɯиᴧ чᴛᴏ-ᴧи жᴀᴧᴏʙᴀᴛьᴄя чᴛᴏ ᴛᴇбя ʙ дыᴩы ᴛʙᴏи ᴇбуᴛ ᴨᴏᴋᴀ ᴛы хуй ᴄᴏᴄёɯь иᴧи чё ᴄᴧᴀбинᴀ нᴇʙьᴇбᴇннᴀя нᴀʙᴇᴩни ɜᴀᴧуᴨы ᴄʙинᴏᴩыᴧый ᴄын ɯᴧюхи ʙыᴛᴩᴀхᴀннᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯ ᴏᴛᴄᴏᴄᴀйдᴇᴩ ᴇбучий ᴛы чё нᴇ ᴏᴨᴩᴀʙдыʙᴀᴇɯь ᴄʙᴏй ʍинᴇᴛ ʍнᴇ, ᴛы чᴛᴏ-ᴧи ᴄчиᴛᴀᴇɯь чᴛᴏ ᴦᴧᴏᴛᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи дᴧя ᴩуᴄᴄᴋᴏᴦᴏ ϶ᴛᴏ чᴇᴄᴛь ᴩᴀɜ ᴛы ᴛᴀᴋ ᴨᴩиʙыᴋ жᴩᴀᴛь ᴨᴇниᴄы хᴏхᴧяᴛᴄᴋиᴇ? ᴩᴇщᴇ ᴛуᴛ ᴏᴨᴩᴀʙдᴀния ʙ хуй ᴏɸᴏᴩʍи ᴄынᴏᴋ ɯᴧюɯᴇчᴋи нᴇʙᴏᴄᴨиᴛᴀнный ᴇбᴀᴧ жᴇ ᴛя ʙ ᴦᴏᴩᴧᴏʙину ᴛʙᴏю 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴋᴄᴛᴀ я ᴨᴏᴋᴀ ᴛᴇбᴇ нᴀ ᴋᴧыᴋ нᴀᴋидыʙᴀᴧ ᴛы ʍнᴇ ᴨᴀᴧьчиᴋᴀʍи ᴀнᴀᴧ хᴏᴛᴇᴧ ʙычиᴄᴛиᴛь ᴛᴀᴋ ʙᴏᴛ я ɜᴀᴄᴛᴀʙиᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋуу ᴇё яɜыᴋᴏʍ ʍнᴇ жᴏᴨу ᴧиɜᴀᴛь ибᴏ у ᴛᴇбя ϶ᴛᴏ нᴇ ᴏᴄᴏбᴏ хᴏᴩᴏɯᴏ ʙыхᴏдиᴧᴏ ᴨᴏᴛᴏʍу чᴛᴏ ᴛы ᴨᴏ бᴏᴧьɯᴇй чᴀᴄᴛи ᴧиɯь хуи ᴦᴧᴏᴛᴀᴛь ᴄᴨᴏᴄᴏбᴇн ᴩуᴄᴏᴄʙинᴄᴋий ᴄынᴏᴋ ɜᴇᴧьᴇʙᴀᴩᴋи нᴇ бᴏйᴄя ʍᴇня ᴛуᴛ ᴨᴏᴋᴀ я ᴛя ᴨᴇниᴄᴏʍ бью ᴛы жᴇ ᴋᴀйɸᴏʙᴀᴧ ʙᴄᴇᴦдᴀ ᴏᴛ ϶ᴛᴏᴦᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ужᴇ ʙᴄᴇʍ ᴨᴩиɜнᴀᴛьᴄя дᴏᴧжᴇн чᴛᴏ ᴛы хуя ʍᴏᴇᴦᴏ ɸᴀнᴀᴛᴋᴀ и ᴋᴀждый ʙᴇчᴇᴩ ʍᴏᴇй ɜᴀᴧуᴨᴇ ᴨᴏᴋᴧᴏняᴇɯьᴄя ᴋᴀᴋ будᴛᴏ бᴏᴦᴀʍ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄын ɯᴧюхи уᴄᴋᴏᴦᴧᴀɜый жиʙущий ʙ буᴩяᴛии нᴀɜыʙᴀᴧ ᴄᴇбя ᴩуᴄᴄᴋиʍ ᴨᴏᴋᴀ хуину ʍᴏю ɯᴧиɸᴏʙᴀᴧ ɯᴧюхи ᴛы ᴄынᴏᴋ ᴨᴏᴋᴀ уж ᴛᴇбᴇ ɜубы хуᴇʍ ʙыбиᴛь чᴛᴏбы ᴛы ᴋᴏ ʙᴄᴇʍу ᴇщё и ɯыᴨиᴧяʙиᴧ уᴩᴏдᴇц ʙыᴛᴩᴀхᴀнный 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ʙнᴀᴛуᴩᴇ жᴇ ᴛᴇбя ᴄᴇйчᴀᴄ ᴄынᴋᴀ бᴧяди хуᴇʍ чᴇᴄᴛи иɜбᴀʙᴧю 𓆩ꏢ𓆪",
  " ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀᴧё ᴄын ɯᴀᴧᴀʙы уᴩᴏдᴧиʙый хуяᴩу ʍᴏю нᴀᴄᴀᴄыʙᴀй инᴀчᴇ ᴛᴇ ϶ᴛᴀ хуяᴩᴀ ᴨᴏ ᴧбу ᴄᴇйчᴀᴄ ᴄᴛучᴀᴛь нᴀчнᴇᴛ и ᴛʙᴏи нᴇ ᴩᴀбᴏчиᴇ ʍᴏɜᴦи ᴨᴏᴧуᴄᴦниʙɯиᴇ ᴨᴩᴏᴄᴛᴏ нᴀᴦᴧухᴏ ʙыбьᴇᴛ бᴇɜ ʙᴏɜʍᴏжнᴏᴄᴛи ʙᴏᴄᴄᴛᴀнᴏʙᴧᴇния ᴛы нᴀʙᴄᴇᴦдᴀ ᴛуᴨыʍ ᴄынᴋᴏʍ ɯᴀᴧᴀɯᴏʙᴋи ᴏᴄᴛᴀнᴇɯьᴄя и нихуя нᴇ ᴨᴏʍᴏжᴇᴛ ᴛᴇбᴇ, ᴀ ϶ᴛᴏ ʙᴄё ᴧиɯь ᴨᴏᴛᴏʍу чᴛᴏ ᴛы нᴀ ʍᴏй чᴧᴇн ᴩыᴨнуᴧᴄя ᴨуᴛᴧᴇᴩᴄᴋий нᴀᴄᴏᴄниᴋ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄын дᴀʙᴀᴧᴋи ᴇᴄᴧи ᴄᴧыɯиɯь ʍᴇня ᴨᴩᴏʍᴏᴧчи ᴇᴄᴧи ᴄᴏᴦᴧᴀᴄᴇн ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ ᴏᴛдᴇɸᴀᴛьᴄя ᴨыᴛᴀйᴄя нᴏ я жᴇ ɜнᴀю чᴛᴏ нᴀ хуи уᴋᴩᴀинᴄᴋиᴇ ᴛы ᴨᴀдᴏᴋ и ᴄᴇйчᴀᴄ у нᴏᴦ ʍᴏих уʍᴏᴧяᴛь будᴇɯь чᴛᴏбы ʍᴏй ᴨᴇниᴄ ʙ ᴛʙᴏёʍ ᴩᴏᴛиᴋᴇ ɯᴇʙᴇᴧиᴧᴄя ᴄᴏ ᴄᴋᴏᴩᴏᴄᴛью ёбᴧи ᴄ ᴛʙᴏᴇй ʍᴀᴛᴇᴩью ᴛуᴨᴏᴦᴏᴧᴏʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶у хуᴇᴛᴇнь ᴄᴧᴀбᴇйɯᴀя нᴇ ʙɜдуʍᴀй ᴛᴇᴩᴨᴇᴛь ᴛᴏᴛ ɸᴀᴋᴛᴏᴩ чᴛᴏ ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ʍнᴇ ɜᴀ 200 ᴦᴩиʙᴇн ᴏᴛдᴀᴧᴀᴄь и ᴩᴀɜᴩᴇɯиᴧᴀ ʍнᴇ ᴄ нᴇй чᴛᴏ уᴦᴏднᴏ дᴇᴧᴀᴛь дᴀжᴇ ᴇю ɜᴀᴧуᴨᴏй ᴨᴏʙᴇᴧᴇʙᴀᴛь, ᴀ ɜᴀ 300 ᴦᴩиʙᴇн ᴏнᴀ ʙᴀщᴇ будᴇᴛ ᴧᴇжᴀᴛь нᴀ ᴄᴨинᴋᴇ и яйцᴀ ʍᴏи ᴧиɜᴀᴛь ну и ɯᴀᴧᴀɯᴏʙᴋᴀ ᴋᴏнᴋᴩᴇᴛнᴀя у ᴛя ʍᴀɜᴇᴩ я бы ᴇй ᴋиᴩᴨичᴏʍ ᴇбᴀᴧьниᴋ ᴄᴧᴏʍᴀᴧ нᴏ ᴨᴏдуʍᴀᴧ чᴇʍ ᴏнᴀ ᴨᴏᴄᴧᴇ ϶ᴛᴏᴦᴏ ɜᴀᴩᴀбᴀᴛыʙᴀᴛь ᴛᴏ будᴇᴛ и ᴨᴏжᴀᴧᴇᴧ ᴛʙᴏю ʍᴀᴛь ɯᴧюху ᴛуᴨᴏᴩᴏᴦую 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы нᴇдᴏᴩᴀɜʙиᴛыʍ ᴩᴏдиᴧᴄя ᴨᴏᴛᴏʍу чᴛᴏ ᴨᴏᴋᴀ ᴛʙᴏя ʍᴀʍᴀɯᴋᴀ быᴧᴀ ᴛᴏбᴏю бᴇᴩᴇʍᴇннᴀя я ᴇй ᴨᴩᴏᴄᴛᴏ ᴄ дʙух нᴏᴦ нᴀхуй ʙ жиʙᴏᴛ ʙᴧᴇᴛᴀᴧ и ɜᴀᴄᴛᴀʙᴧяᴧ ᴇё ᴄᴏᴄᴀᴛь ʍнᴇ, ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴄʙᴏᴇй ɜдᴏᴩᴏʙᴇннᴏй ɜᴀᴧуᴨᴏй хуяᴩиᴧ ᴇй ᴨᴏ бᴏɯᴋᴇ ᴏᴛ чᴇᴦᴏ ᴇё ʍᴏɜᴦ быᴧ ᴛᴏᴛᴀᴧьнᴏ ᴨᴏʙᴩᴇждён ᴋᴀᴋ ᴛʙᴏй ᴩᴏᴛ ᴏᴛ ʍᴏᴇᴦᴏ хуя ᴄᴇйчᴀᴄ и ᴨᴏ иᴛᴏᴦу ᴏнᴀ нᴀ ʙᴄю жиɜнь ᴏʙᴏщᴇʍ ᴏᴄᴛᴀᴧᴀᴄь и я ᴇё ʙᴛихᴀᴩя нᴀʙᴇщᴀᴧ и ᴩᴇɜинᴏʙый ᴨᴇниᴄ ɜᴀ щᴇᴋу ᴇй ᴄᴏʙᴀᴧ ᴨᴏᴋᴀ ᴏнᴀ хᴏᴛᴇᴧᴀ ᴏᴛбиᴛьᴄя ᴏᴛ ʍᴇня 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴏᴛ хуя ʍᴏᴇᴦᴏ ʙ ᴨиɜдᴇ ᴄʙᴏᴇй ʍᴀʍᴋи нᴇ ᴨᴩячьᴄя ᴛᴏ ɜᴀᴄᴄыᴋᴀнный ᴄыниɯᴋᴀ бᴧядины я ᴛᴇбя ᴨᴏжᴀᴧᴇю ᴇᴄᴧи ʍнᴇ ᴇщё ᴨᴀᴩу ᴩᴀɜ дᴀɯь ᴄʙᴏи иᴄᴨᴏᴧьɜᴏʙᴀнныᴇ ᴦубᴇɯᴋи чᴛᴏбы я ʍᴏᴦ ниʍи ᴛᴏᴩᴦᴏʙᴀᴛь ᴋᴀᴋ хᴀч ᴨᴏʍидᴏᴩᴀʍи нᴀ бᴀɜᴀᴩᴇ нᴏ ʙ ʍᴏёʍ ᴄᴧучᴀᴇ ϶ᴛᴏ будᴇᴛ ᴨᴩиᴛᴏн ʙ ᴋᴏᴛᴏᴩᴏʍ будуᴛ ᴛʙᴏи ᴦубы иᴄᴨᴏᴧьɜᴏʙᴀᴛь дᴧя ᴛᴇᴄᴛᴀ ʍᴀᴋᴄиʍᴀᴧьнᴏй дᴏɜы нᴀᴩᴋᴏ ᴨᴏᴄᴧᴇ ᴋᴏᴛᴏᴩᴏй чᴇᴧᴏʙᴇᴋ уʍᴩᴇᴛ нᴏ ᴨᴩᴧбᴧᴇʍᴀ ᴛᴏ ʙ ᴛᴏʍ чᴛᴏ ϶ᴛи ᴛᴇᴄᴛы нᴇ ᴨᴩинᴇᴄуᴛ ᴨᴏᴧьɜы ибᴏ ᴛы ᴄʙиннᴏᴩыᴧый ᴄын ɯᴧюхи и нᴀ ᴨᴏᴧᴏʙину ᴨёᴄ цᴇᴨнᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я ᴛᴇбᴇ ɜᴀ щᴇᴋу ужᴇ уᴄᴛᴀᴧ нᴀᴋидыʙᴀᴛь бᴧя ᴄᴛяни ᴇбᴧищᴇ ᴄʙᴏё чᴛᴏбы я нᴇ ᴩᴀᴄᴛᴇᴦнуᴧ ɯиᴩинᴋу и нᴇ дᴀᴧ ᴛᴇбᴇ ᴨᴏ ᴦубᴀʍ хуйцᴇʍ ᴄнᴏʙᴀ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴨᴏдᴏйди ᴋᴏ ʍнᴇ ᴏᴛᴄᴏᴄный ᴄʙинᴏᴩуᴄ я ᴛᴇбᴇ дᴀʍ хуя ᴄʙᴏᴇᴦᴏ ᴨᴏᴨᴩᴏбᴏʙᴀᴛь нᴀ ʙᴋуᴄ ʍᴏжᴇᴛ ᴛᴇбᴇ ʍᴏй чᴧᴇн ᴨᴏнᴩᴀʙиᴛᴄя ᴋᴀᴋ ʍᴀʍᴀɯᴇ ᴛʙᴏᴇй ᴋᴏᴛᴏᴩᴀя ᴩᴛᴏʍ ᴄ хуя ужᴇ ᴋᴏᴛᴏᴩый дᴇнь нᴇ ᴄᴧᴇɜᴀᴇᴛ, дуʍᴀю у ʙᴀᴄ ϶ᴛᴏ ᴄᴇʍᴇйнᴏᴇ ᴄᴏᴄᴀᴛь уᴋᴩᴀинᴄᴋиᴇ хуи хɜ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀ у ʙᴀᴄ ʙ ᴄᴇʍьᴇ ᴨᴩиняᴛᴏ у уᴋᴩᴀинцᴇʙ ʙ нᴏᴦи ᴨᴩиᴨᴀдᴀᴛь и ᴋ хую ᴄʙᴏᴇй ᴨᴀᴄᴛью ᴛянуᴛᴄя? я ᴨᴩᴏᴄᴛᴏ ниᴋᴀᴋ нᴇ ʍᴏᴦу ᴨᴏняᴛь ᴋᴀᴋᴏᴦᴏ хуя ᴛы ᴄын ɯᴧюхи ɜᴀ ʍᴀᴛᴇᴩью ᴄʙᴏᴇй ᴨᴏʙᴛᴏᴩяᴇɯь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄынᴋу ɯᴀᴧᴀʙы ᴛᴇ нᴏᴦи ᴩᴀᴄхуяᴩиʍ ʙ ʍяᴄᴏ ɜᴀ ᴛᴏ чᴛᴏ ᴛы уᴄᴄыᴋᴀнный ᴨидᴀᴩᴀᴄ ᴏᴛ ʍᴏᴇй ɜᴀᴧуᴨы бᴇᴦᴀᴇɯь ᴧᴏɯᴏᴋ жᴀᴧᴋий 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴄᴧыɯь ᴄынᴏᴋ ɯᴀᴧᴀʙы ᴛы чё ᴛуᴛ удуʍᴀᴧ ᴄᴛᴇᴩᴨᴇᴛь ʍᴏи ᴄᴏᴏбщᴇния чᴛᴏ-ᴧи бᴇᴩи хуя нᴀʙᴇᴩни и ᴏᴛᴨᴏᴩ ᴏᴩᴦᴀниɜуй ᴛᴇᴩᴨиᴧᴏиднᴏᴇ ᴨᴏᴄʍᴇɯищᴇ ᴛя ᴛуᴛ ʙᴄё ʙ хᴀᴩю ᴇбуᴛ ᴨᴏᴋᴀ ᴛы ᴛᴇᴩᴨиɯь и ᴇщё бᴏᴧьɯᴇ ᴨᴏɜᴏᴩиɯьᴄя ну дᴀʙᴀй бᴧяᴛь хᴏᴛь хуй ᴏᴛбᴇй ʍᴏй нᴇдᴇᴇᴄᴨᴏᴄᴏбный ᴩᴇбёнᴏᴋ ᴨᴩᴏᴄᴛиᴛуᴛᴋи ᴏᴨущᴇнный чиᴄᴛᴏ ʍнᴏю и ᴋᴀждыʍ ᴋᴛᴏ ᴛᴇбᴇ ʙ ᴇбᴀᴧᴏ хᴀᴩᴋᴀᴧ ᴨᴏᴋᴀ ᴛы ᴛᴀᴋ жᴇ ᴛᴇᴩᴨᴇᴧ нᴀхуй ᴨᴩᴏбᴧядинᴏɜᴀᴧуᴨинᴄᴋий ᴋᴀждыʍ ɜᴀᴄʍᴇянный ᴨᴀᴩᴀɯниᴋ бᴧяᴛь 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴀхуᴇᴛь ʍнᴇ ᴋᴀжᴇᴛᴄя ᴛы ᴨᴇᴩʙый ᴋᴛᴏ ɜᴀᴧуᴨᴇнь ᴛᴀᴋ яᴩᴏᴄᴛнᴏ нᴀᴄᴀᴄыʙᴀᴇᴛ ɜнᴀя чᴛᴏ ᴏᴨᴨᴏнᴇнᴛ уᴋᴩᴀинᴇц ну дᴀʙᴀй ᴇщё ᴨᴀᴩу ʍинуᴛ нᴀᴄᴧᴀждᴀйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴛᴏᴨᴏᴩᴏʍ ᴇбᴧᴇᴛ нᴇ уᴇбᴀɯиᴧ ᴛʙᴏй ᴋᴩиʙᴏй 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ɜᴀɯуᴦᴀнный ᴄын ɯᴀᴧᴀʙы ᴄᴏбᴇᴩиᴄь ᴄ ᴄиᴧᴀʍи и ᴏᴛ хуя ʍᴏᴇᴦᴏ ᴏᴛбᴇйᴄя ᴨᴏᴋᴀ я ᴛᴇбᴇ ᴋᴏᴧᴇни нᴇ ᴨᴇᴩᴇᴧᴏʍᴀᴧ ᴛᴩёхɜубᴏʍу ᴨидᴏᴩу ᴋᴏᴛᴏᴩый ʍнᴇ хуй ᴨᴩиᴋуᴄыʙᴀя нᴀᴄᴀᴄыʙᴀᴇᴛ ᴀ ну ᴋᴀ ᴋᴧᴏунич дᴀʙᴀй ᴛы ᴨᴏᴛᴇᴩᴨиɯь чᴧᴇн ᴨᴏᴋᴀ я ᴛᴇбя нᴇ ᴏᴛᴨиɜдᴏɯиᴧ ᴀᴩʍᴀᴛуᴩᴏй ᴋᴀᴋ ᴛʙᴏю бᴀбᴋу ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴩᴏᴄᴛᴏ нᴀ ʍᴇᴄᴛᴇ ᴨᴏʍᴇᴩᴧᴀ нᴇ дᴏᴄᴏᴄя ʍнᴇ хуяᴩу ᴀ нᴀ ɜᴀʍᴇну ᴨᴩибᴇжᴀᴧᴀ ᴛʙᴏя ᴦᴏᴧᴀя ʍᴀʍᴀɯᴀ ɯᴀᴧᴀʙᴀ чᴇᴩнᴏʍᴀɜᴀя ᴋᴏᴛᴏᴩᴀя ʙᴄᴇᴦдᴀ хᴏхᴧᴀʍ ᴏбᴄᴀᴄыʙᴀᴧᴀ чᴧᴇны бᴇɜ ᴏᴄᴛᴀнᴏʙᴏᴋ нᴀ ᴏᴛдых и дᴇᴧᴀᴧᴀ ϶ᴛᴏ ᴏᴨыᴛнᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я нᴇ ʙ ᴋуᴩᴄᴇ ɜнᴀᴧ ᴧи ᴛы нᴏ ᴏᴛᴄюдᴀ ᴛы ᴄ цᴇᴧыʍ ᴇбᴀᴧьниᴋᴏʍ нᴇ ʙыйдᴇɯь ʙᴇдь я ᴛᴇбᴇ ᴇᴦᴏ ʍᴏᴧᴏᴛᴋᴏʍ ᴏᴛᴏбью ɜᴀ ᴛᴏ чᴛᴏ ᴛᴇᴩᴨиɯь ᴛᴀᴋ ᴨᴇниᴄ и ᴛы будᴇɯь ʍяᴄᴏʍ бᴇᴄᴨᴏᴧᴇɜныʍ ᴏб ᴋᴏᴛᴏᴩᴏᴇ нᴏᴦи дᴀжᴇ ʙыᴛиᴩᴀᴛь нᴇ будуᴛ ибᴏ ᴛʙᴏй ᴇбᴧᴇᴛ быᴧ ᴨᴩи жиɜни нᴀᴄᴛᴏᴧьᴋᴏ ᴦᴩяɜныʍ чᴛᴏ ᴇᴦᴏ ᴄᴏ ᴄᴩᴀᴋᴏй ᴨуᴛᴀᴧи и ᴛудᴀ хуи ᴨихᴀᴧи ᴨᴩᴏᴄᴛᴛ нᴀхуй ᴋᴀждый ʙᴄᴛᴩᴇчный ᴛᴇбᴇ чᴇᴧᴏʙᴇᴋ ᴛᴇбᴇ хуй ʙ ᴩᴏᴛ нᴀᴄᴏʙыʙᴀᴧ ᴨᴏᴋᴀ ᴛы ᴄ удᴏʙᴏᴧьᴄᴛʙиᴇʍ ᴛᴇᴩᴨᴇᴧ ᴋᴀᴋ и ᴄᴇйчᴀᴄ ϶ᴛᴏ дᴇᴧᴀᴇɯь ᴨᴏᴋᴀ ᴛя ᴇбуᴛ хᴏхᴧᴏᴄᴛᴀнцы бᴧя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴄынᴏᴋ бᴧяди нᴇдᴏнᴏɯᴇннᴏй ᴛᴇᴦни ʍᴇня ᴇᴄᴧи ᴛы ᴄᴏᴄᴀᴧ хуи ʙᴄю ᴄʙᴏю ᴏᴄᴏɜнᴀнную жиɜнь, ᴏᴛʙᴇᴛь нᴀ ᴧюбᴏᴇ ʍᴏё ᴄᴏᴏбщᴇниᴇ ᴇᴄᴧи ᴛʙᴏя ʍᴀᴛь ɯᴀᴧᴀʙᴀ ᴄ ᴩᴏждᴇния нᴀ хуи ᴋидᴀᴧᴀᴄь бᴇɜ ᴨᴧᴀᴛы нᴀ ϶ᴛᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> я буду яᴄнᴏ и ᴋᴩᴀᴛᴋᴏ ᴛᴇбᴇ ᴋᴀждый ᴩᴀɜ ᴏбъяᴄняᴛь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴨᴩᴏᴄᴛиᴛуᴛᴋᴀ дᴇɯёʙᴀя ʍнᴇ хуй ᴨᴏᴄᴀᴄыʙᴀᴧᴀ бᴇɜ ᴨᴩичины нᴀ ϶ᴛᴏ ну чиᴄᴛᴀя ɯᴀᴧᴀʙᴀ ᴨᴩᴏᴄᴛᴏ ᴛᴀᴋих ᴇщё ᴨᴏиᴄᴋᴀᴛь нᴀдᴏ 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ϶й ᴦниᴧᴏɜубый ᴄын ɯᴧюхи ᴏᴛɜᴏʙиᴄь ᴨᴧᴀчᴇʍ ᴋᴏᴛᴏᴩый ни нᴀ ᴄᴇᴋунду нᴇ уᴛихᴀᴇᴛ дᴀжᴇ чиᴛᴀя ϶ᴛᴏ ᴛы ᴨᴧᴀчᴇɯь и ʙ ᴀхуᴇ ᴄидиɯь ᴋᴀᴋ жᴇ я ϶ᴛᴏ уᴦᴀдᴀᴧ, нᴏ я жᴇ ᴛᴇбᴇ ᴄᴇйчᴀᴄ ʙ ᴛʙᴏё ᴄʙинᴏᴩыᴧᴏ хуй ᴨихᴀю и ᴄᴧыɯу ᴋᴀждᴏᴇ ᴛʙᴏё ʙᴄхᴧиᴨыʙᴀниᴇ ᴋᴀᴋ ᴄучᴇчᴋᴀ ᴛы нᴏᴇɯь ʙ ᴨᴇниᴄ ᴨᴏᴋᴀ нᴀд ᴛᴏбᴏй нᴀᴄʍᴇхᴀᴇᴛᴄя ᴛᴏᴧᴨᴀ ᴛʙᴏих ᴇбыᴩᴇй ᴏᴛ ᴋᴏᴛᴏᴩых ᴛы дᴀжᴇ нᴇ ʙ ᴄиᴧᴀх ᴏᴛбиʙᴀᴛьᴄя 𓆩ꏢ𓆪",
" ϟϟ<emoji document_id=5231391336145365545>🇺🇦</emoji> ᴛы ᴨᴏᴋᴀ чᴛᴏ нᴇ ᴀнниᴧиᴦиᴩᴏʙᴀн ʍᴏиʍ чᴧᴇнᴏʍ ᴄынᴏчᴇᴋ ᴩуᴄᴏᴄʙинᴄᴋᴏй хуᴇᴄᴏᴄᴀᴧᴋи нищᴇнᴄᴋᴏй ᴋᴏᴛᴏᴩый ʍнᴇ ᴛуᴛ хуя нᴀᴛᴏчиᴛ яɜыᴋᴏʍ ᴄʙᴏиʍ ᴨᴏᴋᴀ я ᴛʙᴏю ʍᴀʍᴀɯу ʙ уᴦᴧу ᴋᴀᴋ ᴄʙинью ᴇбᴀную ɜᴀбью ɯᴧюху ᴛᴀᴋую ᴨуᴛиниᴄᴛᴄᴋую дᴀʙᴀй ᴛᴇᴨᴇᴩь ᴨᴏ ᴨᴏᴩядᴋу ᴨᴩᴏйдᴇʍᴄя, ᴛᴀᴋ ʙᴏᴛ, я ᴇбᴀᴧ ᴛʙᴏю жиᴩную ʍᴀʍᴀɯу ᴨᴏᴋᴀ ᴛʙᴏй ᴏᴛᴇц иᴄᴛᴇᴋᴀᴧ ᴋᴩᴏʙью ᴏᴛ ᴦᴩᴀнᴀᴛы ᴄбᴩᴏɯᴇнᴏй ᴄ уᴋᴩᴀинᴄᴋᴏᴦᴏ дᴩᴏнᴀ нᴀ ᴋᴏᴛᴏᴩый нᴀᴄᴏᴄᴀᴧᴀ ʍᴀᴛухᴀ ᴛʙᴏя и ᴏᴛдᴀʙɯи дᴇньᴦи ᴨᴏд нᴀᴨᴏᴩᴏʍ хуя ʍᴏᴇᴦᴏ ʙᴇдь дᴏбᴩᴏʙᴏᴧьнᴏᴄᴛи ᴏᴛ нᴇё ʍᴏжнᴏ яʙнᴏ нᴇ ждᴀᴛь и ʍᴏжнᴏ ᴧиɯь ᴇё ɜᴀᴄᴛᴀʙиᴛь ᴨᴇниᴄᴏʍ ᴨᴏᴄᴧᴇ чᴇᴦᴏ ᴏнᴀ ᴨᴏᴄᴧуɯнᴏ будᴇᴛ ᴨᴩиᴋᴀɜы иᴄᴨᴏᴧняᴛь ᴋᴀᴋ ᴄучᴋᴀ нᴀ ʙᴄю ᴦᴏᴧᴏʙу ᴏᴛбиᴛᴀя уᴋᴩᴀинᴄᴋиʍи чᴧᴇнᴀʍи хᴇхᴇ 𓆩ꏢ𓆪"]
            await message.respond(sh+(random.choice(wablon2)), file=media)
            await sleep(time)


    async def rwafkcmd(self, message):
        'включает АФК'
        args = utils.get_args_raw(message)
        user_id = self._tg_id
        user = await self._client(GetFullUserRequest(user_id))
        user_ent = user.users[0]
        self.users.append(int(user_ent.id))
        await message.edit("<b>включено!</b>")
        global states
        states = "on"
        global start
        start = datetime.now()


    async def rwafkoffcmd(self, message):
        'выключает АФК'
        self.users = []
        await message.edit("<b>выключено!</b>")
        global state
        states = "off"
        if states == "off":
            global start
            start = ""


    async def rwafkfcmd(self, message):
        '[ссылка на фото]'
        args = utils.get_args_raw(message)
        photo = args
        global ph
        ph = f"{photo}"
        await message.edit("<b>аргументы приняты!</b>")

    async def rwrsncmd(self, message):
        'устанавливает причину АФК'
        args = utils.get_args_raw(message)
        global reason
        s = args
        reason = s 
        await message.edit("<b>готово!</b>")


    async def watcher(self, message):
        if message.is_private:
            sender = message.sender_id
            if states == "on":
                time_now = datetime.now()
                timing = time_now - start 
                time_string = str(timing)
                time_result = time_string.split(".")[0]
                if getattr(message, "from_id", None) not in self.users:
                    await message.reply(f"<b>в АФК по причине: {reason}\nвремени в АФК:<code> {time_result}</code></b>", file=ph)
                    if sender:
                        self.users.append(int(sender))


    async def helprwcmd(self, message):
        """запускает renewal help premium"""
        args = utils.get_args_raw(message)
        await message.edit("Ꮢ")
        await message.edit("ᏒᎬ")
        await message.edit("ᏒᎬN")
        await message.edit("ᏒᎬNᎬ")
        await message.edit("ᏒᎬNᎬᎳ")
        await message.edit("ᏒᎬNᎬᎳᎪ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲Ꮋ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬᏞ")
        await message.edit("ᏒᎬNᎬᎳᎪᏞ🇦🇲ᎻᎬᏞᏢ")
        await message.edit("⁣<emoji document_id=5411397985365927767>🇦🇲</emoji>")
        await message.edit("⁣<emoji document_id=5411397985365927767>🇦🇲</emoji><emoji document_id=5411397985365927767>🇦🇲</emoji>")
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("loading"))
        await message.delete()
        media_files = ("https://te.legra.ph/file/5d39bebbbef6f967c673b.mp4", "https://te.legra.ph/file/7939a8225e4d0401be0e3.mp4", "https://te.legra.ph/file/e8b6d04a3fb72a46be610.mp4", "https://te.legra.ph/file/42b282d0aa8e28d1f9f0d.mp4")
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

            user_info  = ("<emoji document_id=5373230724130285725>🇺🇦</emoji> ᏒᎬNᎬᎳᎪᏞϟϟᎻᎬᏞᏢ <emoji document_id=5199939531154924006>💀</emoji>\nʍᴏдуᴧи хᴇᴧᴨᴀ ↓↓↓\n\n\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rage</code> - запускает модуль ᏌᏦᏒᎪᏆNᏆᎪN ᏒᎪᏀᎬ\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwrage</code> - запускает календарь модуль ᏌᏦᏒᎪᏆNᏆᎪN ᏒᎪᏀᎬ\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rw</code> - запускает модуль ᏒᎬNᎬᎳᎪᏞ\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwonline</code> - включает вечный онлайн\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtyper</code> - включает ложный тайп\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwchatid</code> - узнаёт айди чата\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwhour</code> - включает тайп на час\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль АФК (с фото):\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwafk</code> - включает АФК режим\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwafkoff</code> - выключает АФК режим\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwrsn</code> - причина АФК\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwafkf</code> - фото для АФК\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль автоответчик:\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwansd</code> - скачивание текстового файла\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwanstxt</code> - установка текстового файла\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwansz</code> - задержка в секундах\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwanss</code> - установка шапки\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwans</code> - переключает режим работы [on/off]\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль тэггер:\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtag</code> - запускает синий тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtag1</code> - запускает фиолетовый тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtag2</code> - запускает красный тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtag3</code> - запускает жёлтый тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtag4</code> - запускает белый тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwsh</code> - устаналивает шапку тэггера\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwstop</code> - останавливает тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwid</code> - узнаёт айди аккаунта\n\n<emoji document_id=5199939531154924006>💀</emoji>  модуль медиа-тэггер:\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtagm</code> - запускает синий медиа-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtagm1</code> - запускает фиолетовый медиа-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtagm2</code> - запускает красный медиа-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtagm3</code> - запускает жёлтый медиа-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwtagm4</code> - запускает белый медиа-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwstopm</code> - останавливает медиа-тэггер\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль календарь-тэггер:\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkal</code> - запускает синий календарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkal1</code> - запускает фиолетовый календарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkal2</code> - запускает красный календарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkal3</code> - запускает жёлтый календарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkal4</code> - запускает белый календарь-тэггер\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль медиакалендарь-тэггер:\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkalm</code> - запускает синий медиакалендарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkalm1</code> - запускает фиолетовый медиакалендарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkalm2</code> - запускает красный медиакалендарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkalm3</code> - запускает жёлтый медиакалендарь-тэггер\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwkaml4</code> - запускает белый медиакалендарь-тэггер\n\n<emoji document_id=5199939531154924006>💀</emoji> модуль для текстовых файлов\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwused</code> - скачивает текстовик\n<emoji document_id=5199939531154924006>💀</emoji> <code>.rwuse</code> - использует текстовик\n\n"
            f"<i>ᏌᏚᎬᏒNᎪᎷᎬ:</i> @{user_ent.username or '☠️'}\n"
            f"<i>NᏆᏟᏦNᎪᎷᎬ:</i> <code>{user_ent.first_name or '🚫'}</code>\n"
            f"<i>ᏌᏚᎬᏒ ᏆᎠ:</i> <code>{user_ent.id}</code>\n"
            f"ᎷᏫᎠᏌᏞᎬ ᎠᎬᏙᎬᏞᏫᏢᎬᏒ: @killrussians"
        )

        chat_id = message.chat.id
        if chat_id:
               await self.client.send_file(message.peer_id, random.choice(media_files), caption=user_info)