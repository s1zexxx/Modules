import io ,inspect ,logging #line:2:import io, inspect, logging
from ..import loader ,utils #line:3:from .. import loader, utils
logger =logging .getLogger (__name__ )#line:5:logger = logging.getLogger(__name__)
@loader .tds #line:7:@loader.tds
class MDLMod (loader .Module ):#line:8:class MDLMod(loader.Module):
    ""#line:9:"""получить ссылку на модуль"""
    strings ={'name':'s1zexMDL'}#line:10:strings = {'name': 's1zexMDL'}
    @loader .unrestricted #line:12:@loader.unrestricted
    async def mdlcmd (OO0O00OOO0OOO0O0O ,OO0OO00000OO0OO00 ):#line:13:async def mdlcmd(self, message):
        """получить ссылку на модуль"""#line:14:"""получить ссылку на модуль"""
        O0OOOOO0O0000OO00 =utils .get_args_raw (OO0OO00000OO0OO00 )#line:15:args = utils.get_args_raw(message)
        if not O0OOOOO0O0000OO00 :return await utils .answer (OO0OO00000OO0OO00 ,'<b>название модуля</b>')#line:16:if not args: return await utils.answer(message, '<b>название модуля</b>')
        OO0OO00000OO0OO00 =await utils .answer (OO0OO00000OO0OO00 ,'<b>ищу...</b>')#line:17:message = await utils.answer(message, '<b>ищу...</b>')
        try :#line:18:try:
            OO000O0OO0O0000OO =' '.join ([O0O0O0O00000O0OO0 .strings ["name"]for O0O0O0O00000O0OO0 in OO0O00OOO0OOO0O0O .allmodules .modules if O0OOOOO0O0000OO00 .lower ()==O0O0O0O00000O0OO0 .strings ["name"].lower ()])#line:20:[x.strings["name"] for x in self.allmodules.modules if args.lower() == x.strings["name"].lower()])
            OO00O0O0O000OO0OO =inspect .getmodule (next (filter (lambda O00OOOO00OOOOO0OO :O0OOOOO0O0000OO00 .lower ()==O00OOOO00OOOOO0OO .strings ["name"].lower (),OO0O00OOO0OOO0O0O .allmodules .modules )))#line:22:next(filter(lambda x: args.lower() == x.strings["name"].lower(), self.allmodules.modules)))
            OOOO00OOO0O000O0O =str (OO00O0O0O000OO0OO ).split ('(')[1 ].split (')')[0 ]#line:23:link = str(r).split('(')[1].split(')')[0]
            if "http"not in OOOO00OOO0O000O0O :#line:24:if "http" not in link:
                OO0O0OOO00O0000OO =f"File {OO000O0OO0O0000OO}:"#line:25:text = f"File {f}:"
            else :#line:26:else:
                OO0O0OOO00O0000OO =f"<a href=\"{OOOO00OOO0O000O0O}\">ссылка:</a> for {OO000O0OO0O0000OO}: \n<code>{link}</code>"#line:27:text = f"<a href=\"{link}\">ссылка:</a> for {f}: \n<code>{link}</code>"
            O0O0OOOOOO00OO0O0 =io .BytesIO (OO00O0O0O000OO0OO .__loader__ .data )#line:28:out = io.BytesIO(r.__loader__.data)
            O0O0OOOOOO00OO0O0 .name =OO000O0OO0O0000OO +".py"#line:29:out.name = f + ".py"
            O0O0OOOOOO00OO0O0 .seek (0 )#line:30:out.seek(0)
            await utils .answer (OO0OO00000OO0OO00 ,O0O0OOOOOO00OO0O0 ,caption =OO0O0OOO00O0000OO )#line:32:await utils.answer(message, out, caption=text)
        except Exception as OO00O0O00O00O0O0O :#line:33:except Exception as e:
            logger .info (f"не получилось {O0OOOOO0O0000OO00} ошибка:",exc_info =True )#line:34:logger.info(f"не получилось {args} ошибка:", exc_info=True)
            await utils .answer (OO0OO00000OO0OO00 ,"<b>модуль не найден</b>")#line:35:await utils.answer(message, "<b>модуль не найден</b>")
    async def mlccmd (O00OO0O00O0000OO0 ,OO0O00OO0OO00OOOO ):#line:37:async def mlccmd(self, message):
        """получение ссылки командой"""#line:38:"""получение ссылки командой"""
        OOO0000O000O0O000 =utils .get_args_raw (OO0O00OO0OO00OOOO )#line:39:args = utils.get_args_raw(message)
        if not OOO0000O000O0O000 :return await utils .answer (OO0O00OO0OO00OOOO ,'<b>название модуля и аргумент</b>')#line:40:if not args: return await utils.answer(message, '<b>название модуля и аргумент</b>')
        if OOO0000O000O0O000 in O00OO0O00O0000OO0 .allmodules .commands .keys ():#line:41:if args in self.allmodules.commands.keys():
            OOO0000O000O0O000 =O00OO0O00O0000OO0 .allmodules .commands [OOO0000O000O0O000 ].__self__ .strings ["name"]#line:42:args = self.allmodules.commands[args].__self__.strings["name"]
        else :#line:43:else:
            return await utils .answer (OO0O00OO0OO00OOOO ,'<b>комманда не найдена</b>')#line:44:return await utils.answer(message, '<b>комманда не найдена</b>')
        OO0O00OO0OO00OOOO =await utils .answer (OO0O00OO0OO00OOOO ,'<b>ищу...</b>')#line:45:message = await utils.answer(message, '<b>ищу...</b>')
        try :#line:46:try:
            OOOO000OO0OO0OOOO =' '.join ([O0OO00O00OOOO0O0O .strings ["name"]for O0OO00O00OOOO0O0O in O00OO0O00O0000OO0 .allmodules .modules if OOO0000O000O0O000 .lower ()==O0OO00O00OOOO0O0O .strings ["name"].lower ()])#line:48:[x.strings["name"] for x in self.allmodules.modules if args.lower() == x.strings["name"].lower()])
            O0OOOO0O0O000000O =inspect .getmodule (next (filter (lambda OO00000OO00OOO000 :OOO0000O000O0O000 .lower ()==OO00000OO00OOO000 .strings ["name"].lower (),O00OO0O00O0000OO0 .allmodules .modules )))#line:50:next(filter(lambda x: args.lower() == x.strings["name"].lower(), self.allmodules.modules)))
            O0000O00OO00O000O =str (O0OOOO0O0O000000O ).split ('(')[1 ].split (')')[0 ]#line:51:link = str(r).split('(')[1].split(')')[0]
            if "http"not in O0000O00OO00O000O :#line:52:if "http" not in link:
                O0O00O0O00O000000 =f"File {OOOO000OO0OO0OOOO}:"#line:53:text = f"File {f}:"
            else :#line:54:else:
                O0O00O0O00O000000 =f"<a href=\"{O0000O00OO00O000O}\">ссылка:</a> for {OOOO000OO0OO0OOOO}: \n<code>{link}</code>"#line:55:text = f"<a href=\"{link}\">ссылка:</a> for {f}: \n<code>{link}</code>"
            O0O0O000OO0OOOOOO =io .BytesIO (O0OOOO0O0O000000O .__loader__ .data )#line:56:out = io.BytesIO(r.__loader__.data)
            O0O0O000OO0OOOOOO .name =OOOO000OO0OO0OOOO +".py"#line:57:out.name = f + ".py"
            O0O0O000OO0OOOOOO .seek (0 )#line:58:out.seek(0)
            await utils .answer (OO0O00OO0OO00OOOO ,O0O0O000OO0OOOOOO ,caption =O0O00O0O00O000000 )#line:61:await utils.answer(message, out, caption=text)
        except Exception as O0O000O0O00O00O0O :#line:62:except Exception as e:
            logger .info (f"не получилось {OOO0000O000O0O000} ошибка:",exc_info =True )#line:63:logger.info(f"не получилось {args} ошибка:", exc_info=True)
            await utils .answer (OO0O00OO0OO00OOOO ,"<b>модуль не найден</b>")