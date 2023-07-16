#       A____A
#      /""""""\
#    =+- ◠.◠ -+=
#    ｟__'---'__｠
#       \*****\    Licensed under the MIT License
# ｟ https://murix.ru/files/ftg/modules/LICENSE.txt ｠

# for more info: https://murix.ru/files/ftg
# by xadjilut, 2023

import asyncio
import io
import logging
import re
import sys
import time
import traceback
from datetime import timedelta
from functools import wraps
from typing import Optional

from meval import meval
from telethon import TelegramClient
from telethon.errors import MessageNotModifiedError, MessageTooLongError, ChannelPrivateError
from telethon.events import Raw
from telethon.extensions.html import parse
from telethon.tl.functions.messages import GetScheduledHistoryRequest, DeleteScheduledMessagesRequest, \
    SendMessageRequest, EditMessageRequest, SendMediaRequest
from telethon.tl.types import Message, UpdateNewScheduledMessage, MessageEntityBold, MessageEntityCode, \
    MessageEntitySpoiler, MessageEntityItalic, PeerUser, PeerChannel, PeerChat, UpdateUserStatus, \
    InputMediaUploadedDocument, DocumentAttributeFilename, UpdateDeleteScheduledMessages

from .. import loader, utils

logger = logging.getLogger(__name__)


def middle(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            if args[0].me.bot:
                return await utils.answer(args[1], args[0].strings("sorry_bot"))
            if not args[1].out:
                return await utils.answer(args[1], args[0].strings("sorry_fake"))
            if args[1].post:
                return await utils.answer(args[1], args[0].strings("oppa_channel"))
            return await func(*args, **kwargs)
        except Exception as e:
            logger.debug(f"опа, случилась дичь: {e}")
            await utils.answer(args[1], args[0].strings("error").format(e=e))
    wrapper.__doc__ = func.__doc__
    return wrapper


def chat_checker(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        self: 'ScherminalMod' = args[0]
        is_delete_upd = isinstance(args[1], UpdateDeleteScheduledMessages)
        if not is_delete_upd:
            m: 'Message' = args[1].message
            if m.post or not m.out:
                return
        else:
            m: 'UpdateDeleteScheduledMessages' = args[1]
        peer = getattr(m, "to_id" if not is_delete_upd else "peer")
        if isinstance(peer, PeerUser):
            chat = peer.user_id
        elif isinstance(peer, PeerChannel):
            chat = peer.channel_id
        elif isinstance(peer, PeerChat):
            chat = peer.chat_id
        else:
            return
        if is_delete_upd:
            _count = self.db.get(self.name + "_chats", chat, 0)
            self.db.set(self.name + "_chats", chat, max(_count - len(m.messages), 0))
            return
        _count = await self.update_sch_count(chat, m.edit_date)
        logger.debug(f"_count={_count} edit_date={m.edit_date}")
        if m.fwd_from or not m.message:
            return
        if _count > 98:
            setattr(m, "_client", self.client)
            await sch_answer(m, self.strings("sorry_out_of_range"))
            logger.debug(f"случился out of range в {peer}")
        else:
            try:
                await func(*args, **kwargs)
            except TooMuchException:
                setattr(m, "_client", self.client)
                await sch_answer(m, self.strings("sorry_too_much"))
            logger.debug(f"отработал вочер в {peer}")
        if _count > 90:
            await self.sch_clean(chat, part=True)
    return wrapper


@loader.tds
class ScherminalMod(loader.Module):
    """Scheduled terminal, отложенный терминал, терминал в отложенных сообщениях.
Пожалуй, один из самых изысканных способов программирования, не выходя из Telegram"""

    strings = {
        'name': 'Scherminal',
        "sorry_bot": "<b><i>Сорян, но данный модуль не умеет работать с ботами, "
                     "т. к. отложенные сообщения в ботапи ещё не завезли\U0001f937</i></b>",
        "sorry_fake": "<b><i>Похоже, ты пытаешься работать с модулем через фейковый аккаунт. "
                      "Это недопустимо и вообще-то не очень удобно, сорян\U0001f481</i></b>",
        "oppa_channel": "<b><i>Опа, кажется, я в канале… а, не, не кажется, лол… "
                        "Отложенный терминал не работает в каналах по соображениям безопасности"
                        "\U0001f46e\U0001f3ff\u200d\u2640\ufe0f</i></b>",
        "error": "\U0001f62c<i>Есть ошиб очка</i>: {e}",
        "need_terminal": "<b>Поставь модуль для терминала, не еби мозг:</b> <code>{}dlmod terminal</code>",
        "need_restart": "<b>Ой, а где модуль для запуска питонячьего кода, ну-ка сделай</b> <code>{}restart</code> "
                        "<b>и повтори снова</b>\U0001f5ff",
        "scherminal_on": "<b><i>Отложенный терминал запущен, го в отложки\u2668\ufe0f</i></b>",
        "scherminal_already_on": "<b>Уже запущен</b>",
        "scherminal_off": "<b><i>Отложенный терминал остановлен\U0001f6d1</i></b>",
        "scherminal_already_off": "<b>Уже остановлен</b>",
        "scherminal_hint_start": "Cюда можно откладывать код или команды, которые сразу же запустятся тут.\n",
        "scherminal_hint_separ": "_________\n\n",
        "scherminal_hint_text": "Вводные:\n",
        "scherminal_hint_eval": " — запустить код и вернуть результат;\n",
        "scherminal_hint_exec": " — просто запустить код;\n",
        "scherminal_hint_terminal": " — запустить команду терминала;\n",
        "scherminal_hint_terminate": "] — прервать запущенные команды терминала в данном диалоге;\n",
        "scherminal_hint_hint": " — показать это сообщение;\n",
        "scherminal_hint_off": " — отключить отложенный терминал.\n",
        "scherminal_hint_ad": "Больше ебанутых модулей: https://t.me/somescripts\n",
        "scherminal_hint_end": "Удачного кодинга!",
        "sorry_out_of_range": "<b><i>Похоже, что тут слишком много отложек, предлагаю их слегка почистить для "
                              "более комфортной работы\U0001f9f9</i></b>",
        "sorry_too_much": "<b><i>У команды/кода просто ну ооооочень большой вывод (>=500 кБ), подумой над тем, как "
                          "сократить его\U0001f9e0</i></b>",
    }

    delta = timedelta(days=364, hours=23, minutes=59, seconds=30)

    day_hash_chars = '\u00AD\u2060\uFE0F\uFEFF'

    cmd_type_signs = {'t': '\U000E0030', 'e': '\u200C', 'x': '\u200D', "_": "\u200B"}

    def __init__(self):
        self.name = self.strings["name"]
        self.python_mod = []
        self.eval_str = 'evaluated'
        self.eval_err_str = 'evaluate_fail'
        self.exec_err_str = 'execute_fail'
        self.cur_time = time.time()
        self.day_hash = get_day_hash(self.cur_time)

    async def client_ready(self, client: 'TelegramClient', db):
        self.me = await client.get_me()
        self.client = client
        self.db = db
        self.init_python_mod()
        if not self.me.bot:
            self.check_scherminal()
            await asyncio.sleep(0.5)
            self.check_cleaner()

    def init_python_mod(self):
        _name = ".modules.python.PythonMod" if __name__.startswith("friendly-telegram.") else ".modules.eval.Evaluator"
        self.python_mod = [x for x in self.allmodules.modules if _name in str(x)]
        if not self.python_mod:
            self.python_mod = [PythonEvaluatorDummy()]
        if self.eval_str not in self.python_mod[0].strings:
            self.eval_str = 'eval'
            self.eval_err_str = 'err'
            self.exec_err_str = 'err'

    def get_eval_str(self, _err: bool, _exec: bool, *args):
        python_mod = self.python_mod[0]
        if __name__.startswith("hikka."):
            args = ("4985626654563894116", *args)
        return python_mod.strings(
            self.eval_str if not _err else (self.exec_err_str if _exec else self.eval_err_str)
        ).format(*args)

    def remove_handler(self, func: callable):
        if self.check_handler(func):
            return self.client.remove_event_handler(func)

    def check_handler(self, func: callable):
        for _func, _ in self.client.list_event_handlers():
            if func.__code__.co_code == _func.__code__.co_code:
                return True
        return False

    def check_cleaner(self):
        self.remove_handler(self.cleaner)
        self.client.add_event_handler(self.cleaner, Raw([UpdateUserStatus]))
        logger.debug("уборщик назначен.")

    def check_scherminal(self):
        self.remove_handler(self.watcher_raw)
        if self.db.get(self.name, 'status', False):
            self.client.add_event_handler(
                self.watcher_raw, Raw([UpdateNewScheduledMessage, UpdateDeleteScheduledMessages]))
            logger.debug("щерминал восстановлен, ура!")

    def get_prefix(self):
        """Берёт префикс команд юзверя (да-да, твой префикс)"""
        r = [v for k, v in dict(self.db).items() if isinstance(v, dict) and isinstance(k, str) and k.endswith(".main")]
        return r[0].get("command_prefix", ['.'])[0] if r else '.'

    @middle
    async def schoncmd(self, message: 'Message'):
        """Запускает режим отложенного терминала.
Не требует аргументов"""
        await self.schon(message)

    @middle
    async def schoffcmd(self, message: 'Message'):
        """Отключает режим терминала в отложенных сообщениях, если он запущен.
Не требует аргументов"""
        _flag = await self.handle_scherminal(message, False)
        await utils.answer(
            message,
            self.strings("scherminal_" + ("off" if _flag else "already_off"))
        )

    async def schevalcmd(self, message: 'Message'):
        """Scheduled evaluation, алиас для schon.
Допускается Python-код в кач-ве аргумента"""
        await self.schon(message, ".eval")

    async def schexeccmd(self, message: 'Message'):
        """Scheduled execution, алиас для schon.
Допускается Python-код в кач-ве аргумента"""
        await self.schon(message, ".exec")

    async def scherminalcmd(self, message: 'Message'):
        """Scheduled terminal, алиас для schon.
Допускается команда консоли в кач-ве аргумента"""
        await self.schon(message, ".terminal")

    async def schon(self, message, mode=""):
        _flag = await self.handle_scherminal(message)
        await utils.answer(
            message,
            self.strings("scherminal_" + ("on" if _flag else "already_on"))
        )
        if mode and utils.get_args_raw(message):
            message.message = mode + ' ' + utils.get_args_raw(message)
            await self.watcher_raw(UpdateNewScheduledMessage(message))
        else:
            await self.update_sch_count(utils.get_chat_id(message))

    async def on_unload(self):
        self.remove_handler(self.cleaner)
        self.remove_handler(self.watcher_raw)
        await self.handle_scherminal(None, False, False)

    async def cleaner(self, *args, **kwargs):
        if not self.db.get(self.name, 'status', False):
            return
        if int(time.time() / 86400) == int(self.cur_time / 86400):
            return
        self.cur_time = time.time()
        self.day_hash = get_day_hash(self.cur_time)
        for _chat, _count in dict(self.db).get(self.name+"_chats", dict()).items():
            if not _count:
                continue
            await self.sch_clean(_chat)

    def generate_hint(self):
        entities = []
        hint = self.strings("scherminal_hint_start")
        entities.append(MessageEntityBold(offset=9, length=71))
        hint += self.strings("scherminal_hint_separ") + self.strings("scherminal_hint_text") + "\n"
        hint_cmd = self.get_sch_command(mode="eval") + " #code"
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + self.strings("scherminal_hint_eval")
        hint_cmd = self.get_sch_command(mode="exec") + " #code"
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + self.strings("scherminal_hint_exec")
        hint_cmd = self.get_sch_command(mode="terminal") + " #cmd"
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + self.strings("scherminal_hint_terminal")
        hint_cmd = self.get_sch_command(mode="terminate")
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + ' ['
        hint_cmd = '-f'
        entities.append(MessageEntityCode(offset=len(hint)+9, length=2))
        hint += hint_cmd + self.strings("scherminal_hint_terminate")
        hint_cmd = self.get_sch_command(mode="hint")
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + self.strings("scherminal_hint_hint")
        hint_cmd = self.get_sch_command(mode="off")
        entities.append(MessageEntityCode(offset=len(hint)+9, length=len(hint_cmd)))
        hint += hint_cmd + self.strings("scherminal_hint_off") + self.strings("scherminal_hint_separ")
        hint_ad = self.strings("scherminal_hint_ad")
        entities += [MessageEntitySpoiler(offset=len(hint)+9, length=len(hint_ad)),
                     MessageEntityItalic(offset=len(hint)+9, length=len(hint_ad))]
        hint += hint_ad + "\n"
        hint_end = self.strings("scherminal_hint_end")
        entities += [MessageEntityItalic(offset=len(hint)+9, length=len(hint_end)),
                     MessageEntityBold(offset=len(hint)+9, length=len(hint_end))]
        hint += hint_end
        return hint, entities

    async def handle_scherminal(self, message: Optional['Message'], on=True, set_status=True) -> bool:
        logger.debug(f"on={on}, set_status={set_status}")
        logger.debug("чек статус…")
        _status = self.db.get(self.name, "status", False)
        if not (_status ^ on):
            return False
        logger.debug("убираем обработчик…")
        self.remove_handler(self.watcher_raw)
        if on:
            logger.debug("если да…")
            await self.update_sch_count(utils.get_chat_id(message))
            answer, entities = self.generate_hint()
            await sch_answer(message, answer, entities=entities)
            self.client.add_event_handler(
                self.watcher_raw, Raw([UpdateNewScheduledMessage, UpdateDeleteScheduledMessages]))
        else:
            logger.debug("если нет…")
            await self.sch_clean()
            if self.name+"_chats" in self.db:
                del self.db[self.name+"_chats"]
        if set_status:
            logger.debug("проставляем статус…")
            self.db.set(self.name, "status", on)
        logger.debug("конецъ")
        return True

    async def sch_clean(self, spec_chat=None, part=False):
        _chats = [spec_chat] if spec_chat else dict(self.db).get(self.name+"_chats", {}).keys()
        _count = 0
        for _chat in _chats:
            if isinstance(_chat, str):
                if not _chat.isnumeric():
                    continue
                _chat = int(_chat)
            try:
                sch = await self.client(GetScheduledHistoryRequest(_chat, 1337))
            except ChannelPrivateError:
                continue
            if spec_chat:
                _count = len(sch.messages)
            _4del = []
            for m in sch.messages:
                if m.document and m.document.mime_type == "text/plain":
                    attrs = [x for x in m.document.attributes if isinstance(x, DocumentAttributeFilename)]
                    if attrs and attrs[0].file_name.startswith(f"sch_{_chat}") and m.document.size < 500000:
                        _4del.append(m.id)
                elif re.fullmatch(r"["+self.day_hash_chars+r"]{8}", m.message[:8]):
                    if spec_chat and self.day_hash == m.message[:8]:
                        continue
                    _4del.append(m.id)
            logger.debug(f"{_4del} {_chat}")
            if part:
                _4del.reverse()
                _offset = max(int(len(_4del) / 2), 0)
                _4del = _4del[:_offset]
            _count -= len(_4del)
            if _4del:
                await self.client(DeleteScheduledMessagesRequest(_chat, _4del))
        if spec_chat:
            self.db.set(self.name+"_chats", spec_chat, _count)

    async def update_sch_count(self, chat, edit_date=None):
        _count = self.db.get(self.name + "_chats", chat, 0)
        if not _count or not isinstance(_count, int):
            _count = len((await self.client(GetScheduledHistoryRequest(chat, 1488228))).messages) - 1
        elif edit_date:
            _count -= 1
        self.db.set(self.name + "_chats", chat, _count + 1)
        return _count + 1

    @chat_checker
    async def watcher_raw(self, event: 'UpdateNewScheduledMessage'):
        _status = self.db.get(self.name, "status", False)
        if not _status:
            return
        message = event.message
        logger.debug(f"{message}")
        if self.get_sch_command(message.message, "off"):
            await self.handle_scherminal(None, False)
            await self.client(DeleteScheduledMessagesRequest(getattr(message, "to_id"), [message.id]))
            return
        setattr(message, "_client", self.client)
        if self.get_sch_command(message.message, "hint"):
            answer, entities = self.generate_hint()
            return await sch_answer(message, answer, entities=entities)
        if self.get_sch_command(message.message, "terminate"):
            terminal_mod = [x for x in self.allmodules.modules if
                            ".modules.terminal.TerminalMod" in str(x)]
            if not terminal_mod:
                return await sch_answer(
                    message, self.strings("need_terminal").format(self.get_prefix()), cmd_type='t')
            _chat_id = utils.get_chat_id(message)
            sch = await self.client(GetScheduledHistoryRequest(_chat_id, 1337))
            _ids = [str(x.id) for x in sch.messages]
            _yes, _no = 0, 0
            for _key, _proc in terminal_mod[0].activecmds.items():
                try:
                    if _key.split("/")[0] != str(_chat_id) or _key.split("/")[1] not in _ids:
                        continue
                    _proc.kill() if '-f' in message.message else _proc.terminate()
                except Exception as e:
                    logger.exception(f"убийство процесса {_key} не состоялось: {e}")
                    _no += 1
                else:
                    _yes += 1
            return await sch_answer(
                message,
                terminal_mod[0].strings("kill_fail", message) + f": {_no}\n\n" +
                terminal_mod[0].strings("killed", message) + f": {_yes}"
            )
        _eval_pred = self.get_sch_command(message.message, "eval")
        _exec_pred = self.get_sch_command(message.message, "exec")
        _terminal_pred = self.get_sch_command(message.message, "terminal")
        logger.debug(f"{_eval_pred} {_exec_pred} {_terminal_pred}")
        if not (_eval_pred or _exec_pred or _terminal_pred):
            return
        cmd = message.message[len(self.get_prefix()):].lstrip().split(maxsplit=1)[1]
        if _eval_pred or _exec_pred:
            logger.debug("выполняем питон…")
            if isinstance(self.python_mod[0], PythonEvaluatorDummy):
                self.init_python_mod()
            python_mod = self.python_mod[0]
            return await self.eval_or_exec_it(cmd, message, _exec_pred, python_mod.getattrs)
        if _terminal_pred:
            logger.debug("выполняем сосноль…")
            terminal_mod = [x for x in self.allmodules.modules if
                            ".modules.terminal.TerminalMod" in str(x)]
            if terminal_mod:
                exe = terminal_mod[0]
                return await exe.run_command(
                    message, cmd,
                    SudoSchMessageEditor(message, cmd, exe.strings))
            else:
                return await sch_answer(
                    message, self.strings("need_terminal").format(self.get_prefix()), cmd_type='t')

    def get_sch_command(self, message_text="", mode=""):
        logger.debug(f"{message_text} {mode}")
        available_aliases = [k for k, v in self.allmodules.aliases.items() if v == mode]
        available_aliases += ["e"] if self.eval_str == mode else [mode]
        logger.debug(f"{available_aliases}")
        _prefix = self.get_prefix()
        if not message_text:
            return _prefix + available_aliases[0]
        _filter = message_text[len(_prefix):].lstrip().split()[0] in available_aliases
        logger.debug(f"{_prefix} {_filter}")
        return message_text.startswith(_prefix) and _filter

    async def get_sch_reply(self, message: 'Message'):
        if message.reply_to:
            return await self.client.get_messages(getattr(message, "to_id"), ids=message.reply_to.reply_to_msg_id)
        return message.reply_to

    async def eval_or_exec_it(self, cmd, message, _exec: bool, _getattrs: callable):
        _cmd_type = 'e' if not _exec else 'x'
        try:
            attrs = await _getattrs(message)
            attrs["reply"] = await self.get_sch_reply(message)
            ret = await meval(cmd, globals(), **attrs)
            if not _exec:
                await sch_answer(
                    message,
                    self.get_eval_str(False, _exec, utils.escape_html(cmd), utils.escape_html(ret)),
                    cmd_type=_cmd_type
                )
            else:
                await sch_answer(
                    message, "<code>" + utils.escape_html(cmd) + "</code>", cmd_type='x')
        except TooMuchException:
            raise
        except PythonEvaluatorDummy:
            await sch_answer(
                message, self.strings("need_restart").format(self.get_prefix()), cmd_type=_cmd_type)
        except Exception as e:
            logger.debug(f"чё-то не пошло, глянь: {e}\nисходник: {cmd}")
            e = sys.exc_info()
            e2 = e[2]
            while e2.tb_next:
                e2 = e2.tb_next
            e = "".join(traceback.format_exception(e[0], e[1], e2))
            await sch_answer(
                message,
                self.get_eval_str(True, _exec, utils.escape_html(cmd), utils.escape_html(e)),
                cmd_type=_cmd_type
            )


def get_day_hash(t):
    _time = int(t / 86400)
    _l = list(ScherminalMod.day_hash_chars)
    ret = ''
    while _time > 0:
        ret += _l[_time % 4]
        _time = int(_time / 4)
    return ret


async def sch_answer(message: 'Message', response: str, entities=None, cmd_type='_'):
    day_hash = get_day_hash(time.time())
    response = day_hash + ScherminalMod.cmd_type_signs[cmd_type] + response
    client: 'TelegramClient' = getattr(message, "client") or getattr(message, "_client")
    if not entities:
        response, entities = parse(response)
    if len(response) >= 500000:
        raise TooMuchException()
    _request = SendMessageRequest
    args = {
        "peer": getattr(message, "to_id"), "no_webpage": True,
        "message": response, "entities": entities,
        "schedule_date": ScherminalMod.delta,
        "reply_to_msg_id": message.reply_to.reply_to_msg_id if message.reply_to else None
    }
    _time = int(time.time())
    _chat = utils.get_chat_id(message)
    if len(response) > 2000 or response.count('\n') > 20:
        response, _ = parse(response[9:])
        response = io.BytesIO(response.encode())
        response.seek(0)
        _request = SendMediaRequest
        args["media"] = InputMediaUploadedDocument(
            file=await client.upload_file(response),
            mime_type="text/plain",
            attributes=[DocumentAttributeFilename(f'sch_{_chat}_{cmd_type}_{_time}.txt')]
        )
        args["message"] = ""
        del args["no_webpage"]
    elif message.date.timestamp() > _time:
        _request = EditMessageRequest
        args["id"] = message.id
        del args["reply_to_msg_id"]
    ret = await client(_request(**args))
    logger.debug(str(ret))
    m = [x.message for x in ret.updates if isinstance(x, UpdateNewScheduledMessage)][0]
    if cmd_type == 't':
        setattr(m, "_client", client)
    if not isinstance(response, str):
        await client(DeleteScheduledMessagesRequest(_chat, [message.id]))
    return m


class TooMuchException(Exception):
    pass


class PythonEvaluatorDummy(Exception, loader.Module):

    strings = {}

    def getattrs(self, *args):
        raise self.__class__()


def hash_message(message):
    return str(utils.get_chat_id(message)) + "/" + str(message.id)


class SudoSchMessageEditor:
    # не спижжено, а переписано по образу и подобию (хакинтош, без обид!)
    def __init__(self, message, command, strings):
        self.message = message
        self.command = command
        self.stdout = ""
        self.stderr = ""
        self.rc = None
        self.redraws = 0
        self.strings = strings
        self.process = None
        self.state = 0
        self.authmsg = None

    def update_process(self, process):
        logger.debug("получен объект процесса %s", process)
        self.process = process

    async def update_stderr(self, stderr):
        logger.debug("update_stderr " + stderr)
        self.stderr = stderr
        lines = stderr.strip().split("\n")
        lastline = lines[-1]
        lastlines = lastline.rsplit(" ", 1)
        client = getattr(self.message, "_client")
        handled = False
        if len(lines) > 1 \
                and re.fullmatch(r"\[sudo] password for (.*): Sorry, try again\.", lines[-2]) \
                and lastlines[0] == "[sudo] password for" \
                and self.state == 1:
            logger.debug("ставим состояние на 0…")
            await sch_answer(self.authmsg, self.strings("auth_fail"), cmd_type='t')
            self.state = 0
            handled = True
            await asyncio.sleep(5)
        if lastlines[0] == "[sudo] password for" and self.state == 0:
            logger.debug("лог судо найден!")
            text = self.strings("auth_needed").format("sch")
            command = "<code>" + utils.escape_html(self.command) + "</code>"
            user = utils.escape_html(lastlines[1][:-1])
            self.authmsg = await sch_answer(
                self.message,
                text + "\n\n" + self.strings("auth_msg").format(command, user),
                cmd_type='t'
            )
            logger.debug("отправлено сообщение для аутентификации")
            client.remove_event_handler(self.sch_message_edited)
            client.add_event_handler(
                self.sch_message_edited, Raw([UpdateNewScheduledMessage]))
            logger.debug("зареган хендлер")
            handled = True
        if len(lines) > 1 \
                and (re.fullmatch(r"\[sudo] password for (.*): sudo: [0-9]+ incorrect password attempts", lastline)
                     and (self.state in [1, 3, 4])):
            logger.debug("пароль неверен много раз")
            await sch_answer(self.message, self.strings("auth_locked"), cmd_type='t')
            self.state = 2
            handled = True
        if not handled:
            logger.debug("чё-то нет лога судо.")
            if self.authmsg:
                client.remove_event_handler(self.sch_message_edited)
                self.authmsg = None
            self.state = 2
            await self.redraw()
        logger.debug(self.state)

    async def update_stdout(self, stdout):
        self.stdout = stdout
        self.state = 3 if self.state != 2 else self.state
        if self.authmsg:
            getattr(self.message, "_client").remove_event_handler(self.sch_message_edited)
            self.authmsg = None
        await self.redraw()

    async def sch_message_edited(self, event: 'UpdateNewScheduledMessage'):
        if not self.authmsg:
            return
        message = event.message
        logger.debug("опа, получен апдейт для сообщения с айди " + str(message.id))
        if hash_message(message) == hash_message(self.authmsg):
            try:
                self.authmsg = await sch_answer(message, self.strings("auth_ongoing"), cmd_type='t')
            except MessageNotModifiedError:
                logger.debug("идёт аутентификация в судо…")
            self.state = 1
            self.process.stdin.write(message.message.split("\n", 1)[0].encode("utf-8") + b"\n")

    async def redraw(self):
        text = self.strings("running").format(utils.escape_html(self.command))
        rc_exists = self.rc is not None
        if rc_exists:
            text += self.strings("finished").format(utils.escape_html(str(self.rc)))
        stdout_offset = max(len(self.stdout) - 1000, 0) if not rc_exists else 0
        text += self.strings("stdout") + utils.escape_html(self.stdout[stdout_offset:])
        if len(self.stderr) > 0:
            stderr_offset = max(len(self.stderr) - 500, 0) if not rc_exists else 0
            text += self.strings("stderr") + utils.escape_html(self.stderr[stderr_offset:])
        text += self.strings("end")
        try:
            self.message = await sch_answer(self.message, text, cmd_type='t')
        except MessageNotModifiedError:
            pass
        except MessageTooLongError as e:
            logger.error(e)
            logger.error(text)

    async def cmd_ended(self, rc):
        self.rc = rc
        self.state = 4
        await self.redraw()
