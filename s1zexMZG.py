import random #line:3:import random
from telethon import types #line:5:from telethon import types
from ..import loader ,utils #line:7:from .. import loader, utils
@loader .tds #line:10:@loader.tds
class MZGMod (loader .Module ):#line:11:class MZGMod(loader.Module):
    strings ={'name':'s1zexMZG','pref':'<b>[MZG]</b> ','need_arg':'{}Нужен аргумент','status':'{}{}','on':'{}Включён','off':'{}Выключен',}#line:20:}
    _db_name ='MZG'#line:21:_db_name = 'MZG'
    async def client_ready (O0O0O00O00OOOO00O ,_OO0OOO000O0OOO0OO ,O00O0O0O000000000 ):#line:23:async def client_ready(self, _, db):
        O0O0O00O00OOOO00O .db =O00O0O0O000000000 #line:24:self.db = db
    @staticmethod #line:26:@staticmethod
    def str2bool (OO0O00O000O000O0O ):#line:27:def str2bool(v):
        return OO0O00O000O000O0O .lower ()in ("yes","y","ye","yea","true","t","1","on","enable","start","run","go","да")#line:28:return v.lower() in ("yes", "y", "ye", "yea", "true", "t", "1", "on", "enable", "start", "run", "go", "да")
    async def mzgcmd (O0000OO00OO0OOOOO ,OO0OOO0O0OOOOOO0O :types .Message ):#line:31:async def mzgcmd(self, m: types.Message):
        '.mzg <on/off/...> - Переключить режим дурачка в чате'#line:32:'.mzg <on/off/...> - Переключить режим дурачка в чате'
        O000O00O00O0OOOO0 =utils .get_args_raw (OO0OOO0O0OOOOOO0O )#line:33:args = utils.get_args_raw(m)
        if not OO0OOO0O0OOOOOO0O .chat :#line:34:if not m.chat:
            return #line:35:return
        OOOO0OO00OOO00OOO =OO0OOO0O0OOOOOO0O .chat .id #line:36:chat = m.chat.id
        if O0000OO00OO0OOOOO .str2bool (O000O00O00O0OOOO0 ):#line:37:if self.str2bool(args):
            O0OOO0O0O0O0O0O0O :list =O0000OO00OO0OOOOO .db .get (O0000OO00OO0OOOOO ._db_name ,'chats',[])#line:38:chats: list = self.db.get(self._db_name, 'chats', [])
            O0OOO0O0O0O0O0O0O .append (OOOO0OO00OOO00OOO )#line:39:chats.append(chat)
            O0OOO0O0O0O0O0O0O =list (set (O0OOO0O0O0O0O0O0O ))#line:40:chats = list(set(chats))
            O0000OO00OO0OOOOO .db .set (O0000OO00OO0OOOOO ._db_name ,'chats',O0OOO0O0O0O0O0O0O )#line:41:self.db.set(self._db_name, 'chats', chats)
            return await utils .answer (OO0OOO0O0OOOOOO0O ,O0000OO00OO0OOOOO .strings ('on').format (O0000OO00OO0OOOOO .strings ('pref')))#line:42:return await utils.answer(m, self.strings('on').format(self.strings('pref')))
        O0OOO0O0O0O0O0O0O :list =O0000OO00OO0OOOOO .db .get (O0000OO00OO0OOOOO ._db_name ,'chats',[])#line:43:chats: list = self.db.get(self._db_name, 'chats', [])
        try :#line:44:try:
            O0OOO0O0O0O0O0O0O .remove (OOOO0OO00OOO00OOO )#line:45:chats.remove(chat)
        except :#line:46:except:
            pass #line:47:pass
        O0OOO0O0O0O0O0O0O =list (set (O0OOO0O0O0O0O0O0O ))#line:48:chats = list(set(chats))
        O0000OO00OO0OOOOO .db .set (O0000OO00OO0OOOOO ._db_name ,'chats',O0OOO0O0O0O0O0O0O )#line:49:self.db.set(self._db_name, 'chats', chats)
        return await utils .answer (OO0OOO0O0OOOOOO0O ,O0000OO00OO0OOOOO .strings ('off').format (O0000OO00OO0OOOOO .strings ('pref')))#line:50:return await utils.answer(m, self.strings('off').format(self.strings('pref')))
    async def mzgchancmd (O0O0OOOOOO0OOO0O0 ,OO0OO0OO0O000O0OO :types .Message ):#line:52:async def mzgchancmd(self, m: types.Message):
        '.mzgchan <int> - Устанвоить шанс 1 к N.\n0 - всегда отвечать'#line:53:'.mzgchan <int> - Устанвоить шанс 1 к N.\n0 - всегда отвечать'
        OO0OOOOO0O0000O0O :str =utils .get_args_raw (OO0OO0OO0O000O0OO )#line:54:args: str = utils.get_args_raw(m)
        if OO0OOOOO0O0000O0O and OO0OOOOO0O0000O0O .isdigit ():#line:55:if args and args.isdigit():
            O0O0OOOOOO0OOO0O0 .db .set (O0O0OOOOOO0OOO0O0 ._db_name ,'chance',int (OO0OOOOO0O0000O0O ))#line:56:self.db.set(self._db_name, 'chance', int(args))
            return await utils .answer (OO0OO0OO0O000O0OO ,O0O0OOOOOO0OOO0O0 .strings ('status').format (O0O0OOOOOO0OOO0O0 .strings ('pref'),OO0OOOOO0O0000O0O ))#line:57:return await utils.answer(m, self.strings('status').format(self.strings('pref'), args))
        return await utils .answer (OO0OO0OO0O000O0OO ,O0O0OOOOOO0OOO0O0 .strings ('need_arg').format (O0O0OOOOOO0OOO0O0 .strings ('pref')))#line:59:return await utils.answer(m, self.strings('need_arg').format(self.strings('pref')))
    async def watcher (OO00OO00OOOO000OO ,O000O0000O000000O :types .Message ):#line:61:async def watcher(self, m: types.Message):
        if not isinstance (O000O0000O000000O ,types .Message ):#line:62:if not isinstance(m, types.Message):
            return #line:63:return
        if O000O0000O000000O .sender_id ==(await O000O0000O000000O .client .get_me ()).id or not O000O0000O000000O .chat :#line:64:if m.sender_id == (await m.client.get_me()).id or not m.chat:
            return #line:65:return
        if O000O0000O000000O .chat .id not in OO00OO00OOOO000OO .db .get (OO00OO00OOOO000OO ._db_name ,'chats',[]):#line:66:if m.chat.id not in self.db.get(self._db_name, 'chats', []):
            return #line:67:return
        O000OOO0O00OOOOOO =OO00OO00OOOO000OO .db .get (OO00OO00OOOO000OO ._db_name ,'chance',0 )#line:68:ch = self.db.get(self._db_name, 'chance', 0)
        if O000OOO0O00OOOOOO !=0 and random .randint (0 ,O000OOO0O00OOOOOO )!=0 :#line:69:if ch != 0 and random.randint(0, ch) != 0:
            return #line:70:return
        OOOOOOO00OO00OO00 =O000O0000O000000O .raw_text #line:71:text = m.raw_text
        OOO0O00O000000OO0 ={random .choice (list (filter (lambda OO000O0OO00000O0O :len (OO000O0OO00000O0O )>=3 ,OOOOOOO00OO00OO00 .split ())))for _O0O0O00O0000OOO00 in ".."}#line:73:list(filter(lambda x: len(x) >= 3, text.split()))) for _ in ".."}
        OO0O000O0OOOO0O00 =[]#line:74:msgs = []
        for OO00O0000OOO0O0O0 in OOO0O00O000000OO0 :#line:75:for word in words:
            [OO0O000O0OOOO0O00 .append (O000O000OO00O0O00 )async for O000O000OO00O0O00 in O000O0000O000000O .client .iter_messages (O000O0000O000000O .chat .id ,search =OO00O0000OOO0O0O0 )if O000O000OO00O0O00 .replies and O000O000OO00O0O00 .replies .max_id ]#line:76:[msgs.append(x) async for x in m.client.iter_messages(m.chat.id, search=word) if x.replies and x.replies.max_id]
        OOOOO0OOO0000000O =random .choice (OO0O000O0OOOO0O00 )#line:77:replier = random.choice(msgs)
        OO00O0O0O0O00O0OO =OOOOO0OOO0000000O .id #line:78:sid = replier.id
        O0O0OO0OO0O00O000 =OOOOO0OOO0000000O .replies .max_id #line:79:eid = replier.replies.max_id
        OO0O000O0OOOO0O00 =[O0000OOO00OOOOOO0 async for O0000OOO00OOOOOO0 in O000O0000O000000O .client .iter_messages (O000O0000O000000O .chat .id ,ids =list (range (OO00O0O0O0O00O0OO +1 ,O0O0OO0OO0O00O000 +1 )))if O0000OOO00OOOOOO0 and O0000OOO00OOOOOO0 .reply_to and O0000OOO00OOOOOO0 .reply_to .reply_to_msg_id ==OO00O0O0O0O00O0OO ]#line:80:msgs = [x async for x in m.client.iter_messages(m.chat.id, ids=list(range(sid+1, eid+1))) if x and x.reply_to and x.reply_to.reply_to_msg_id == sid]
        O0OOOO0O0OOO0OO0O =random .choice (OO0O000O0OOOO0O00 )#line:81:msg = random.choice(msgs)
        if O000O0000O000000O .chat .id not in OO00OO00OOOO000OO .db .get (OO00OO00OOOO000OO ._db_name ,'chats',[]):#line:82:if m.chat.id not in self.db.get(self._db_name, 'chats', []):
            return #line:83:return
        await O000O0000O000000O .reply (O0OOOO0O0OOO0OO0O )