import random
from asyncio import sleep
from telethon import types
import os
from .. import loader, utils


@loader.owner
def register(cb):
    cbRENEWAL()


class RENEWAL(loader.Module):
    strings = {"name": "RENEWAL"}
    
    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def rnwcmd(self, message):
        '''⟨задержка в секундах⟩ ⟨шапка⟩'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "пока, ты сосал")
            return
        await utils.answer(
            message,
            "<b>здарова соси\n\n",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        wablon = ["текст"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(wablon)))
            await sleep(time)
            
            
    async def typercmd(self, message):
        """время в секундах"""
        args = utils.get_args(message)
        if args:
            try:
                await message.delete()
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(args[0]))
            except ValueError:
                await message.edit("Некорректное значение времени.")
            except Exception as e:
                await message.edit(f"Ошибка: {str(e)}")
        else:
            await message.edit("Укажите время тайпа в секундах.")
            
            
    async def client_ready(self, _, db):
        self.db = db

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


    async def klcmd(self, m: types.Message):
        "[on/off] - переключить режим работы"
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



    async def kltcmd(self, m: types.Message):
        '''установка шапки'''
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "sh", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )


    async def kilscmd(self, m: types.Message):
        "задержка секунды"
        args: str = utils.get_args_raw(m)
        if args.isdigit():
            self.db.set(self._db_name, "chance", int(args))
            return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

        return await utils.answer(
            m, self.strings("need_arg").format(self.strings("pref"))
        )


    async def kilacmd(self, m: types.Message):
        "установка шаблона с форматом .txt"
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "text", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

    async def dlrcmd(self, message):
        """⟨реплай⟩ ⟨название по желанию⟩ - скачка шаблонов .txt"""
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
            
            

    async def client_ready(self, client, db):
        self.db = db
        self.users = self.db.get("uam", "users", [])
        self.phrases = self.db.get("uam", "phrases", [])
    
    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("uam", "users", self.users)
    
    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("uam", "users", self.users)



async def brcmd(self, message):
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b>ᴄᴋᴏᴩᴏ ᴛы ᴄдᴏхнᴇɯь, ʙᴇдь ʙᴇᴧиᴋий #Ꮮuxᴏdᴇy ᴨᴏйдᴇᴛ ᴨᴏ ᴛʙᴏю дуɯу.</b>"
                )

                self.add_user(reply.from_id)
            
            else:
                await utils.answer(
                    message=message,
                    response="<b>Ꮱунᴋция нᴇ ᴩᴀбᴏᴛᴀᴇᴛ нᴀ ʙᴄᴇʙыɯних. 🍺</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🍺 Ꮋужᴇн ᴩᴇᴨᴧᴀй.</b>"
            )
    
async def bccmd(self, message):
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>#Ꮮuxᴏdᴇy ᴩᴀɜᴩᴇɜᴀᴧ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄʙᴏиʍ ᴄᴛᴀᴧьныʍ хуйᴏʍ. 🍺</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b>Ꭲы ᴄын ɯᴧюхи ᴨᴏдᴏхнᴇɯь ᴏᴛ ᴩуᴋ #Ꮮuxᴏdᴇy 🍺</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🍺 Ꮋужᴇн ᴩᴇᴨᴧᴀй.</b>"
            )
        
     
async def brmcmd(self, message):
        """нᴇ хуяᴩиᴛь ʙыбᴩᴀннᴏᴦᴏ ᴄʙинᴏᴩуᴄᴀ ⟨𝗋𝖾𝗉𝗅𝗒⟩"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>ᴛᴇᴩяйᴄя, ᴩуᴄᴏбᴧядь</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b>[ϟϟ] ᴛы нᴇ ᴇбᴇниᴧ ϶ᴛᴏ ᴩыᴧᴏ ᴩуᴄᴏᴄʙиннᴏᴇ 𓆩ꑭ𓆪</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b><code>⟨!⟩ ᴏᴛʙᴇᴛь нᴀ ᴄᴏᴏбщᴇниᴇ ᴩуᴄняʙᴏᴦᴏ ᴨидᴏᴩᴀ ⟨!⟩</code>"
            )
    
async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(shabl + self.phrases))
            
    
async def bscmd(self, message):
        '''Интервал в секундах + Шапка \n''' 
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "#реневал ебашит")
            return
        await utils.answer(
            message,
            "#реневал ебашит"
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = ["e"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)
            
async def  bmcmd(self, message):
        """⟨ɜᴀдᴇᴩжᴋᴀ ʙ ᴄᴇᴋундᴀх⟩ ⟨ɯᴀᴨᴋᴀ⟩ ⟨𝗋𝖾𝗉𝗅𝗒 𝗈𝗇 𝗆𝖾𝖽𝗂𝖺⟩"""
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>ʍᴇдиᴀᴀнниᴦиᴧяция ᴏᴛʍᴇнᴇнᴀ\nчᴛᴏбы ɜᴀᴨуᴄᴛиᴛь иᴄᴨᴏᴧьɜуй <code>.bm</code> ⟨ɜᴀдᴇᴩжᴋᴀ ʙ ᴄᴇᴋундᴀх⟩ ⟨ɯᴀᴨᴋᴀ⟩ ⟨ᴏᴛʙᴇᴛ нᴀ ʍᴇдиᴀɸᴀйᴧ⟩</b>")
            return
        await utils.answer(
            message,
            "<b>#lilbiruonomimasen ᴇбᴀɯиᴛ</b>",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        media = reply.media
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(wablon)), file=media)
            await sleep(time)
            
            
async def krestidcmd(self, message):
        "узнать айди аккаунта"
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
            f"user = <code>{user.first_name}</code>\n"
            f"id = <code>{user.id}</code>"
            
            )
            
            
async def krestchidcmd(self, message):
        "узнать айди чата"
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
            f"чат: <code>{chat.title}</code>\n"
            f"id = <code>{chat.id}</code>"
            
            )

async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

async def dlr1cmd(self, message):
        """Команда .dlr <реплай на файл> <название (по желанию)> скачивает файл, либо сохраняет текст в файл на который был сделан реплай."""
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
                    f'Файл сохранён как: <code>{fname}</code>')
            else:
                ext = reply.file.ext
                fname = f'{name or message.id + reply.id}{ext}'
                await message.client.download_media(reply, fname)
                await message.edit(
                    f'Этот файл сохранён как: <code>{fname}')
        else:
            return await message.edit('Нет реплая.')

async def shbcmd(self, message):
        """тайминг в секундах + название шаблона(с .txt) + шапка"""
        shapka = utils.get_args_raw(message)
        if not shapka:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>Модуль Shaby остановлен!</b>")
            return
        await utils.answer(
            message,
            "<b>Модуль Shaby запущен!\n\n"
            "Чтобы его остановить, используй <code>.shb</code></b>",
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
