import random
from asyncio import sleep
import os
from .. import loader, utils, version
from telethon.tl.functions.users import GetFullUserRequest
import time
import logging
import re
from ..inline.types import InlineCall
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import Message
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime
from math import sqrt
import requests
import git
import datetime
import asyncio
from telethon import types
from telethon.tl.functions.channels import GetFullChannelRequest
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import io
import logging
from io import BytesIO

import requests
from requests import post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
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
from .. import loader, utils

from asyncio import sleep

from datetime import timedelta

from telethon import types

import datetime

import logging

import time

import random

import io

from asyncio import sleep

from os import remove



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

from telethon import types



from telethon.tl.types import Message

from datetime import datetime

from datetime import timedelta

from telethon import functions

from telethon.tl.functions.users import GetFullUserRequest

import datetime

from datetime import datetime

from datetime import timedelta



from telethon import functions

from telethon.tl.types import Message

import time

from random import randint

from contextlib import suppress

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
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

logger = logging.getLogger(__name__)

start = datetime.now()

@loader.owner
def register(cb):
    cb(invulprofile())

@loader.tds
class reckizyy(loader.Module):
    '''rekizzy helper'''
    strings = {
        "name": "<b>[<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5314778899291317503>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312078571747943493>💎</emoji><emoji document_id=5312248330330318502>💎</emoji><emoji document_id=5312248330330318502>💎</emoji>  <emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5314258143096611234>💎</emoji>  <emoji document_id=5312319442103838156>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314254432244866511>💎</emoji>  <emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312399070797504641>💎</emoji><emoji document_id=5323370611999776730>➖</emoji>]</b>",
        "loading": "<b>[<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5314778899291317503>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312078571747943493>💎</emoji><emoji document_id=5312248330330318502>💎</emoji><emoji document_id=5312248330330318502>💎</emoji>  <emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5314258143096611234>💎</emoji>  <emoji document_id=5312319442103838156>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314254432244866511>💎</emoji>  <emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312399070797504641>💎</emoji><emoji document_id=5323370611999776730>➖</emoji>]</b>",
        "not_chat": "<b>[<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5314778899291317503>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312078571747943493>💎</emoji><emoji document_id=5312248330330318502>💎</emoji><emoji document_id=5312248330330318502>💎</emoji>  <emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5314258143096611234>💎</emoji>  <emoji document_id=5312319442103838156>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314254432244866511>💎</emoji>  <emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312399070797504641>💎</emoji><emoji document_id=5323370611999776730>➖</emoji>]</b>",}

    async def client_ready(self, client, db):
        self.client = client

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def client_ready(self, client, db):
            self.db = db
            self.client = client
            self.users = []
        
    async def oncmd(self, message):
        """ʙκ᧘ючᥲᥱᴛ ᥲɸκ"""
        args = utils.get_args_raw(message)
        user_id = self._tg_id
        user = await self._client(GetFullUserRequest(user_id))
        user_ent = user.users[0]
        self.users.append(int(user_ent.id))
        await message.edit("<b><emoji document_id=5460962419062876360>❤️</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5944809554612063704>✍️</emoji>включᴇниᴇ<emoji document_id=5944809554612063704>✍️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5460962419062876360>❤️</emoji></b>")
        global state
        state = "on"
        global start
        start = datetime.now()

    async def offcmd(self, message):
        """ʙыκ᧘ючᥲᥱᴛ ᥲɸκ"""
        self.users = []
        await message.edit("<b><emoji document_id=5460962419062876360>❤️</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5944809554612063704>✍️</emoji>выключᴇниᴇ<emoji document_id=5944809554612063704>✍️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5460962419062876360>❤️</emoji></b>")
        global state
        state = "off"
        if state == "off":
            global start
            start = "";
            
    async def setphcmd(self, message):
        """ᥴᴛᥲʙᥙᴛ ʙᥙдᥱ᧐\ɸ᧐ᴛ᧐\ᴦᥙɸ нᥲ ᥲɸκ"""
        args = utils.get_args_raw(message)
        photo = args
        global ph
        ph = f"{photo}"
        await message.edit("<b><emoji document_id=5460962419062876360>❤️</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5944809554612063704>✍️</emoji>rотово<emoji document_id=5944809554612063704>✍️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5460962419062876360>❤️</emoji></b>")

    async def reasoncmd(self, message):
        """уκᥲɜыʙᥲᥱᴛ ᥰρᥙчᥙну ʙ ᥲɸκ"""
        args = utils.get_args_raw(message)
        global reason
        s = args
        reason = s
        await message.edit("<b><emoji document_id=5460962419062876360>❤️</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5944809554612063704>✍️</emoji>rотово<emoji document_id=5944809554612063704>✍️</emoji><emoji document_id=5346067693093007745>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5345825933678881630>✡</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5460962419062876360>❤️</emoji></b>")

    async def watcher(self, message):
        sender = message.sender_id
        if message.is_private:
            if state == "on":
                time_now = datetime.now()
                timing = time_now - start
                time_string = str(timing)
                time_result = time_string.split(".")[0]
                if getattr(message, "from_id", None) not in self.users:
                    await message.reply(f"<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5314778899291317503>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312078571747943493>💎</emoji><emoji document_id=5312248330330318502>💎</emoji><emoji document_id=5312248330330318502>💎</emoji>  <emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5314258143096611234>💎</emoji>  <emoji document_id=5312506814347094008>💎</emoji><emoji document_id=5314315940471513565>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5323370611999776730>➖</emoji>\n\n<emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5312506814347094008>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5314278282198261904>💎</emoji> {reason}\n<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5314258143096611234>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5323370611999776730>➖</emoji><code> {time_result}</code>\n\n<b><i><emoji document_id=5787587127076195946>🔣</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5314315940471513565>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312506814347094008>💎</emoji><emoji document_id=5314258143096611234>💎</emoji><emoji document_id=5312082956909551441>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5787191844056076084>🔣</emoji></i></b>\n<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲣⲁⳅⲣⲁⳝⲟⲧⳡυⲕ:<code>Reckizyy</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲙⲟⲇⲩⲗь ⳝыⲗ ⲥⲟⳅⲇⲁⲏ:<code>23.08.2023</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n", file=ph)
                    if sender:
                        self.users.append(int(sender))
        
    async def reckihelpcmd(self, message):
        """загрузка модулей и анимации"""
        args = utils.get_args_raw(message)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nНᥲчᥲ᧘ᥲᥴь ɜᥲᴦρуɜκᥲ ʍ᧐ду᧘я")
        time.sleep(0.5)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▱▱▱▱▱ 𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:6 сек\n ")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▰▱▱▱▱ 𝟚𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:5 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▰▰▱▱▱ 𝟜𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:4 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▰▰▰▱▱ 𝟞𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:3 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▰▰▰▰▱ 𝟠𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:2 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ: ▰▰▰▰▰ 𝟙𝟘𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:1 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ ᥲнᥙʍᥲцᥙᥙ ɜᥲʙᥱρɯᥙ᧘ᥲᥴь\n")
        time.sleep(0.5)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nСᥱᥔчᥲᥴ нᥲчнᥱᴛᥴя ɜᥲᴦρуɜκᥲ ʍ᧐ду᧘ᥱᥔ\n")
        time.sleep(0.5)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▱▱▱▱▱ 𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:5 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▰▱▱▱▱ 𝟚𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:4 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▰▰▱▱▱ 𝟜𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:3 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▰▰▰▱▱ 𝟞𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:2 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▰▰▰▰▱ 𝟠𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:1 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nУᥴᴛᥲн᧐ʙκᥲ ʍ᧐ду᧘ᥱᥔ: ▰▰▰▰▰ 𝟙𝟘𝟘%\n д᧐ κ᧐нцᥲ ɜᥲᴦρуɜκᥙ:0 сек\n")
        time.sleep(1)
        await message.edit(
            "<emoji document_id=5474211392443657621>🧛</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝙍𝙚𝙘𝙠𝙞𝙯𝙮𝙮 𝙝𝙚𝙡𝙥𝙚𝙧\nЗᥲᴦρуɜκᥲ хᥱ᧘ᥰᥱρᥲ ɜᥲʙᥱρɯᥱнᥲ")
        time.sleep(0.5)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("name"))
        media_files = (
            "https://te.legra.ph/file/7fcceb2affdf65cfc0c0e.mp4", "https://te.legra.ph/file/7fcceb2affdf65cfc0c0e.mp4")
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
                "<b><emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5314778899291317503>💎</emoji><emoji document_id=5312074165111497079>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312078571747943493>💎</emoji><emoji document_id=5312248330330318502>💎</emoji><emoji document_id=5312248330330318502>💎</emoji>  <emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312443192996536982>💎</emoji><emoji document_id=5314258143096611234>💎</emoji>  <emoji document_id=5312319442103838156>💎</emoji><emoji document_id=5312425317342651471>💎</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314254432244866511>💎</emoji>  <emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312399070797504641>💎</emoji><emoji document_id=5323370611999776730>➖</emoji>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.килл</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под килл<emoji document_id=5352919308391424163>🔥</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.смерть</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под смерть<emoji document_id=5341427217152880394>🚬</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.абсолют</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под абсолют<emoji document_id=5334626127849724802>🤡</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.риск</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под риск<emoji document_id=5442804822048780010>😫</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.кара</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под кара<emoji document_id=5339236895501069653>🚬</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.лезвие</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под лезвие<emoji document_id=5341819141508574901>🚬</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.боль</code>- интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под боль<emoji document_id=5784974820592586088>🔥</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.гнеф</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под гнеф<emoji document_id=5352887306590102199>♾</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.банкай</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под банкай<emoji document_id=5352655842212584578>🌜</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.злость</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под злость<emoji document_id=5404336676879216590>🤡</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.бог</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под бог<emoji document_id=5341497469932938890>🚬</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.кровь</code>-интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст под кровь<emoji document_id=5784974820592586088>🔥</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.on</code>-ʙκ᧘ючᥲᥱᴛ ᥲɸκ<emoji document_id=5460962419062876360>❤️</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.off</code>-ʙыκ᧘ючᥲᥱᴛ ᥲɸκ<emoji document_id=5345825933678881630>✡</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.setph</code>-ᥴᴛᥲʙᥙᴛ ʙᥙдᥱ᧐\ɸ᧐ᴛ᧐\ᴦᥙɸ нᥲ ᥲɸκ<emoji document_id=5346067693093007745>✡</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.reason</code>-уκᥲɜыʙᥲᥱᴛ ᥰρᥙчᥙну ʙ ᥲɸκ<emoji document_id=5339225221779959041>🚬</emoji></b>\n"
                "<b><emoji document_id=5352958736191200616>⭐️</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.reckiping</code>-ᥰ᧐κᥲɜыʙᥲᥱᴛ ᥰᥙнᴦ<emoji document_id=5832291818162622889>🩻</emoji></b>\n\n"
                "<b><i><emoji document_id=5787587127076195946>🔣</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5314315940471513565>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312506814347094008>💎</emoji><emoji document_id=5314258143096611234>💎</emoji><emoji document_id=5312082956909551441>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5787191844056076084>🔣</emoji></i></b>\n"
                "<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲣⲁⳅⲣⲁⳝⲟⲧⳡυⲕ:<code>Reckizyy</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲙⲟⲇⲩⲗь ⳝыⲗ ⲥⲟⳅⲇⲁⲏ:<code>23.08.2023</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Юⳅⲉⲣⲕⲁ:<code> @{user_ent.username or '☠️'}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲏυⲕ:<code> {user_ent.first_name or '🚫'}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲁύⲇυ:<code> {user_ent.id}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"

            )

        chat_id = message.chat.id
        if chat_id:
            await self.client.send_file(message.peer_id, random.choice(media_files), caption=user_info)

    async def reckipingcmd(self, message):
        """ᥰ᧐κᥲɜыʙᥲᥱᴛ ᥰᥙнᴦ"""

        args = utils.get_args_raw(message)

        starter = datetime.now()

        end = datetime.now()

        pins = (end - start).microseconds / 1000

        timing = starter - start

        ping_string = str(pins)

        pingg = ping_string.split(".")

        ping = float(pingg[1])

        time_string = str(timing)

        time_result = time_string.split(".")[0]

        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("loading"))
        await message.delete()
        media_files = ("https://te.legra.ph/file/7fcceb2affdf65cfc0c0e.mp4",
                           "https://te.legra.ph/file/7fcceb2affdf65cfc0c0e.mp4")
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

            help_info = (
                f"<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5314400813320250143>💎</emoji><emoji document_id=5312082956909551441>💎</emoji><emoji document_id=5314406534216687106>💎</emoji><emoji document_id=5314653537785880132>💎</emoji><emoji document_id=5323370611999776730>➖</emoji> <code>{ping}</code>\n<emoji document_id=5323370611999776730>➖</emoji><emoji document_id=5312362228568041728>💎</emoji><emoji document_id=5314400813320250143>💎</emoji><emoji document_id=5312492516400964635>💎</emoji><emoji document_id=5312082956909551441>💎</emoji><emoji document_id=5314624426497547887>💎</emoji><emoji document_id=5312392194554865221>💎</emoji><emoji document_id=5323370611999776730>➖</emoji> <code>{time_result}</code></b>\n\n"
                "<b><i><emoji document_id=5787587127076195946>🔣</emoji><emoji document_id=5312469800318935359>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5314315940471513565>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5312546886391963483>💎</emoji><emoji document_id=5314381198204608234>💎</emoji><emoji document_id=5312506814347094008>💎</emoji><emoji document_id=5314258143096611234>💎</emoji><emoji document_id=5312082956909551441>💎</emoji><emoji document_id=5312319175815864428>💎</emoji><emoji document_id=5314278282198261904>💎</emoji><emoji document_id=5787191844056076084>🔣</emoji></i></b>\n"
                "<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲣⲁⳅⲣⲁⳝⲟⲧⳡυⲕ:<code>Reckizyy</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲙⲟⲇⲩⲗь ⳝыⲗ ⲥⲟⳅⲇⲁⲏ:<code>23.08.2023</code><emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Юⳅⲉⲣⲕⲁ:<code> @{user_ent.username or '☠️'}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲏυⲕ:<code> {user_ent.first_name or '🚫'}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"
                f"<b><emoji document_id=5375377129741494312>🙂</emoji><emoji document_id=5406876368350751327>〰️</emoji>Ⲁύⲇυ:<code> {user_ent.id}</code> <emoji document_id=5352918496642604333>❤️</emoji></b>\n"

            )
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_file(chat_id, random.choice(media_files), caption=help_info)
        
    async def киллcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>𐌺ᥙ᧘᧘ ɜᥲκ᧐нчᥙ᧘ унᥙчᴛ᧐жᥲᴛь ᥴынκ᧐ʙ δ᧘ядᥱᥔ <emoji document_id=5352919308391424163>🔥</emoji</b>")
            return
        await utils.answer(
            message,
            "<b>𐌺ᥙ᧘᧘ нᥲчᥲ᧘ унᥙчᴛ᧐жᥲᴛь ᥴынκ᧐ʙ δ᧘ядᥱᥔ <emoji document_id=5352919308391424163>🔥</emoji</b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = ["члᴇнǿϻ ϻᴀть твǿю ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " стᴀль в пизду твǿᴇй ϻᴀϻᴀши всунул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в рылǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в ǿчҝǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в ҝрᴇдит твтя ϻᴀть сᴀсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " лᴇтя сᴀсᴀлᴀ ϻᴀть твǿя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть шлюхᴀ хуй сᴀсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " всᴇ чᴀщᴇ сую члᴇн в ϻᴀть твǿю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в трᴇжиϻᴇ твǿю ϻᴀть трᴀхᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " прǿжǿг ᴇбᴀлǿ твǿᴇй ϻᴀϻᴀшᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю пингвинил члᴇнǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀшᴀ твǿя шлюхᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть зᴀ ᴇбᴀлǿ нᴀд хуᴇϻ пǿвᴇсил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю члᴇнǿϻ дырявил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть чᴇҝᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю хуᴇϻ вытрᴀхивᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀню твǿю зᴀлупǿй дрᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть лᴇтᴀᴇт пǿ хую ϻǿᴇϻу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю зᴀлупǿй прихуярил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿя зᴀлупǿй дᴀвиться) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀшу твǿю зᴀ пизду пǿвᴇшᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сᴀсᴇт твǿя ϻᴀть пǿҝᴀ ты сϻǿтришь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀшу твǿю зᴀлупǿй уничтǿжил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в пᴀрᴀшᴇ твǿю ϻᴀть тǿплю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀшᴇ твǿᴇй зᴀлупǿй шᴀры выбил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тяну твǿю ϻᴀть шлюху) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ 5+ сᴀсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀши твǿᴇй улǿжил зᴀлупу в рǿт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в щᴇҝǿлду твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пǿ ҝᴀбинᴇ твǿᴇй ϻᴀϻᴀши зᴀлупǿй бью) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀлупǿй твǿю ϻᴀть пидᴀрᴀсил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻᴀшу твǿю в рǿт жᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " трᴀхᴀнул твǿю ϻᴀть ну) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю рᴇжу хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ ϻᴀть твǿю иϻᴇл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в ǿчҝǿ твǿᴇй ϻᴀϻᴀши ҝǿнчил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿю спᴇрϻу жуᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " чᴇтҝᴀ твǿя ϻᴀть сᴀсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀҝрыл рǿт твǿᴇй ϻᴀϻᴀши члᴇнǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пᴀлᴇруᴇт твǿя ϻᴀть ϻǿю зᴀлупу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть вьᴇбᴀшил в ᴀсфᴀлт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀсᴀдил твǿᴇй ϻᴀϻᴀши) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в пузǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть дᴀвил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ǿпрᴀҝинул зᴀлупǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нǿгиϻи твǿя ϻᴀть дрǿчит ϻнᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ твǿю ϻᴀть ҝǿвырял) <emoji document_id=5352919308391424163>🔥</emoji>",
                " глубǿҝǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ǿтьᴇхᴀлᴀ твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " придушил твǿю ϻᴀть хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿя ᴇбᴀнит нᴀ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю рву хуᴇϻ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пизду твǿᴇй ϻᴀϻᴀши пǿрвᴀл члᴇнǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀ ҝлыҝ твǿᴇй ϻᴀϻᴀши дᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть чᴇрᴇз ϻǿй хуй прǿливᴀᴇтся ҝᴀҝ вǿдᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇт я твǿю ϻᴀть дǿширᴀҝǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇтя твǿю ϻᴀть спичҝᴀϻи ᴇбу ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть с хуя пусҝᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть снǿвᴀ нᴀ ϻǿй члᴇн призᴇϻлилᴀсь пǿслᴇ пǿлётᴀ в тᴀджиҝистᴀн нᴀ рǿдину ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пǿчᴇϻу пиздᴀҝ твǿᴇй ϻᴀтᴇри, зᴀтягивᴀᴇт хуи, ҝᴀҝ трᴇугǿльниҝ бᴇрϻудсҝий ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пылᴇсǿсǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть с хуя чᴇрᴇз зᴀбǿры пᴇрᴇҝидывᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты вǿзьϻи сᴇбᴇ в зубы лᴇйҝу и пǿливᴀй ǿгǿрǿды в пиздᴇ свǿᴇй ϻᴀϻᴀши ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я жᴇ рᴀҝǿвую ǿпухǿль в пиздᴇ твǿᴇй ϻᴀϻᴀши устрǿнял при пǿϻǿщи свǿᴇгǿ хуя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ҝǿгдᴀ у твǿᴇй ϻᴀтᴇри будᴇт ᴀнгинᴀ пǿзǿви ϻᴇня я буду ᴇй в гǿрлǿ бры3гᴀть свǿᴇй спᴇрϻǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю грудную ҝлᴇтҝу хуᴇϻ рᴀсспиливᴀл пǿпǿлᴀϻ и стᴇлил пǿд свǿиϻи двᴇрьϻи ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀчᴇϻ ты ртǿϻ нᴀ хуй упᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀϻᴀшҝᴀ зᴀ бᴀрбᴀрисҝу хуй сǿсᴇт нᴀ рынҝᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пǿслᴇ тǿгǿ ҝᴀҝ я ᴇй лᴇчил рᴀҝ губы зᴀлупǿй ǿнᴀ пǿлбюбилᴀ ᴇгǿ сҝǿрǿ ϻǿй хуй ты сϻǿжᴇшь нᴀзывᴀть пᴀпҝǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " вǿт у тᴇбя явнǿ пидǿрсҝиᴇ нᴀҝлǿннǿсти( ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴇня вдǿхнᴀвляᴇт твǿй рǿт нᴀпᴀвший нᴀ ϻǿй хуй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ҝᴀҝ ты ǿтнᴇсᴇшься ҝ тǿϻу чтǿ ϻǿй хуй зᴀстрял в 12 пᴇрстнǿй ҝишҝᴇ твǿᴇй ϻᴀϻᴀши ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ пиздил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри зубы хуᴇϻ выбил, ǿнᴀ тᴀҝ гǿрьҝǿ плᴀҝᴀлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ ҝлизϻу сдᴇлᴀю ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ хрᴇбᴇт лǿϻᴀю ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ шᴇю лǿϻᴀю ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлитǿр с нǿги выбивᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝирпиичи в ᴇблǿ ҝидᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ чᴇрдᴀҝᴇ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ двᴇрнǿй ручҝᴇ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ ҝᴀлитҝᴇ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀбǿринǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ҝᴀчᴇргǿй ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри бычҝи тушил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿю сᴇстру пǿ ϻǿᴇϻу сǿглᴀсию ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нǿждᴀчҝǿй хуярил пǿ пиздᴇ твǿᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тёрҝǿй тᴇр ᴇблǿ твǿᴇᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ǿбǿссᴀл пǿҝᴀ ты ҝлитǿр сᴇстрᴇ лизᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ǿсудили пǿжизᴇннǿ зᴀ пǿсидᴇлҝи нᴀ ϻǿᴇϻ хуᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй члᴇн с 5 этᴀжᴀ пᴀдᴀлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ хуᴇϻ в глᴀз тыҝᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри нᴀ ᴇблǿ ҝǿнчᴀл пǿҝᴀ ты хуй ǿтцᴀ сǿсᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ губᴇ дᴀвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ щᴇҝᴇ удᴀрил , у нᴇᴇ чᴇлюсть слǿϻᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀлупǿй пǿ лбу хуярил пǿҝᴀ ты ϻнᴇ яйцᴀ лизᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀ дᴇньги сниϻᴀл, пǿслᴇ ǿтдᴀвᴀл бǿϻжᴀϻ и ǿни ᴇᴇ пǿ ҝругу ᴇбᴀли ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть блядь, ᴀ твǿй ǿтᴇц рᴀбǿтᴀᴇт в гᴇй ҝлубᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я рǿзу впизду твǿᴇй ϻᴀтᴇри тыҝᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пᴀдᴀлᴀ нᴀ ϻǿй члᴇн ҝᴀҝ зᴀсǿхший лист с дᴇрᴇвᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть плǿсҝǿгруднᴀя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я пизду твǿᴇй ϻᴀтᴇри тᴇбᴇ нᴀ ᴇблǿ нᴀтягивᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ҝлитǿр твǿᴇй ϻᴀтᴇри рᴀстягивᴀл, ǿн стᴀнǿвился длиднный ҝᴀҝ зϻᴇя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀ пǿлǿвыᴇ губы ҝ пǿтǿлҝу прибивᴀл и хᴀрҝᴀл ᴇй в ᴇблǿ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀтьшᴀϻпурǿϻ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я приниϻᴀю эҝзᴀϻᴇны, ᴀ твǿя ϻᴀϻᴀ дᴀёт ϻнᴇ взятҝу нᴀтурǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я рвᴀл тᴇбᴇ цᴇлҝуу твǿᴇй ϻᴀтᴇри ржᴀвǿй трубǿй :3 ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿиϻ языҝǿϻ вшᴇй лǿбҝǿвых нᴀ пиздᴇ ϻᴀтᴇри гǿнял ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿиϻ ртǿϻ глистǿв из жǿпы ϻᴀтᴇри вытᴀсҝивᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в лᴇсу зᴀрǿю ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ нǿги в рǿт ҝлᴀл пидᴀрᴀс ты ᴇбᴀный ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прǿстрᴇлил ҝᴀҝ с двух ствǿлҝи ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть и тᴀҝ и сяҝ ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿ юϻᴀть в гǿрᴀх ᴇбᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ твǿй ǿтᴇц тᴇбᴇ ҝǿнчу в рǿт сливᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ ты в шҝǿлᴇ был ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть с хуя выҝинул в рᴇҝу ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть въᴇбᴀннᴀя ϻǿиϻ хуᴇϻ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть вᴇрхнǿгᴀϻи ᴇбᴀл суҝᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿсᴇшь и бᴀлдᴇᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴀ пиздᴇ твǿᴇй ϻᴀтᴇри урǿҝи хуᴇϻ дᴇлᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пǿд пǿᴇз хуᴇϻ ҝину щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу спǿриϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿй члᴇн в пǿҝǿᴇ нᴇ ǿстᴀвляᴇшь ртǿϻ свǿиϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу грубǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу в пᴀдиҝᴇ хуᴇϻ пǿгнул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую тᴀщится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пǿд ϻǿиϻ хуᴇϻ тᴇбя высрᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝᴀҝ высҝᴀчҝᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ люстрᴇ ǿтъᴇбу щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿᴇϻ хую извивᴀᴇшься ҝᴀҝ зϻᴇя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝᴀҝ нᴇвϻиняᴇϻый) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ рᴀсписᴀл ҝᴀҝ диҝтᴀнт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуᴇϻ ϻǿзгǿв дǿбᴀвлю щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝǿгдᴀ нᴇбǿ звᴇзднǿᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ҝǿртǿчҝᴀх ϻǿй хуй сǿсᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ҝ ϻǿᴇϻу хую лᴇтишь ҝᴀҝ вǿрǿбᴇй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нюни пустил ҝǿгдᴀ ϻǿй хуй ǿтпиздил тᴇбя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй тᴇбя встрᴇтил бᴇз трусǿв нᴀ улицᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿᴇϻ хую зᴀиҝᴀтся нᴀчᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿд люстрǿй сǿсᴀл ϻнᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿй хуй нᴀ руҝᴀх свǿих нǿсишь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй вǿняᴇт пизжᴇ чᴇϻ твǿи духи) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя хуᴇϻ зᴀҝручу щᴀс ҝᴀҝ ϻᴇтᴇль ᴇбᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ҝ ϻǿᴇϻу хую в жᴇны нᴀбивᴀᴇшься) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿю спᴇрϻу ҝ сᴇбᴇ нᴀ пǿлǿвыᴇ губы ϻᴀжᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри вырᴇжу хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть с пᴇрвǿгǿ рᴀзᴀ пǿрвᴀл ҝᴀҝ гᴀзᴇту) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри рᴀҝ губы хуᴇϻ лᴇчил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ǿвсянҝǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл 2 гǿдᴀ нᴀзᴀд, ҝǿгдᴀ в шҝǿлᴇ учился) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀстᴀвил нᴀ ϻǿй хуй сᴇсть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ᴇбут ϻǿи друзья) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿиϻ члᴇнǿϻ с дᴇтствᴀ питᴀᴇтся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я чᴇт чᴀстǿ твǿю ϻᴀтуху в дᴇснᴀ ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты жᴇ сǿ свǿᴇй ϻᴀϻᴀшᴇй пǿ ϻǿᴇϻу хую гǿришь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я плǿтнǿ твǿю ϻᴀть в пизду ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ᴇблǿϻ твǿиϻ пǿ пиздᴇ твǿᴇй ϻᴀϻҝᴇ ᴇздил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿсᴇшь ϻнᴇ нᴀ пᴇрᴇднᴇϻ плᴀнᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть нᴇ ǿстᴀнᴀвить нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ᴇбᴀл пǿ пьянᴇ нᴀ сцᴇнᴀх) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пᴇрᴇд ϻǿиϻ хуᴇϻ гнулᴀсь ҝᴀҝ институтҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт сǿсᴇт ϻнᴇ ҝᴀҝ бᴀлᴀбǿл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ нᴀ стрᴇлᴇ пиздил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу ҝǿгдᴀ ты нᴇ успᴇвᴀᴇшь бᴀтᴇ сǿсᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿй хуй ϻǿлишься ҝᴀҝ нᴀ иҝǿну) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿд ϻǿиϻ хуᴇϻ прǿгинᴀᴇшься) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿиϻ хуᴇϻ пᴇрᴇбитый) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿсᴇшь , ᴀ ϻǿй хуй нᴇ цᴇнит этǿгǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ǿт ϻǿᴇгǿ хуя прᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ пᴇрᴇгнул ҝᴀҝ жᴇлᴇзǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть прǿϻᴇж яиц зᴀжᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ тᴇϻпᴇрᴀтуру хуᴇϻ сбивᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихуярил ҝᴀҝ ϻуху) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿд ϻǿиϻи яйцᴀϻи прячᴇшься ҝᴀҝ пǿд зǿнтиҝǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю в пǿдвᴀлᴇ ᴇбу ҝᴀҝ хǿчу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ǿпрᴀҝину твǿю ϻᴀть с хуя свǿᴇгǿ щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " щᴀ твǿю ϻᴀть хуᴇϻ нᴀ днǿ тᴀщить щᴀ буду) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ вǿспитывᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт ϻǿчᴇй свǿᴇй зᴀлью щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть прǿститутҝᴀ ϻǿᴇгǿ хуя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты жᴇ ϻыслᴇннǿ зᴀсыпᴀᴇшь с ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть с хуя ǿбǿссᴀл ҝᴀҝ сǿ шлᴀнгᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ждᴇт ǿчᴇрᴇдь нᴀ ϻǿй хуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ сǿтру) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть любит ϻǿй члᴇн) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты учился сǿсᴀть у свǿᴇй ϻᴀтᴇри) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀчᴇϻ твǿй пᴀпᴀшᴀ пǿшᴇл в пᴇдиҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " знᴀᴇшь чтǿ я твǿю сᴇϻью сҝрᴇстил хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в жǿпу тыҝᴀл пǿниϻᴀᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт ҝручᴇ тᴇбя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт нᴇ сǿсᴇт лучшᴇ чᴇϻ твǿй брᴀт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я жᴇ рǿт твǿᴇгǿ ǿтцᴀ хуᴇϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ ᴇблǿ хуᴇϻ лǿϻᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿю ҝǿнчу пил ҝᴀҝ вǿду) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀ сǿтҝу пǿᴇбу щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в пизду ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть из пизды хуᴇϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀǿбǿрǿт ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пǿдтстилҝᴀ ҝǿнчᴇннᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть хуᴇϻ ϻǿиϻ зᴀнятᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз пǿϻᴇхи ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ рǿт пǿҝǿлᴇчил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ᴇблǿ твǿᴇ хуᴇϻ в лужу ǿҝуну щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿй члᴇн губᴀϻи шлᴇпᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ в жǿпу литрᴀϻи ҝǿнчᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿй хуй ǿбǿжᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇт ҝᴀҝ нᴀдǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть быстрǿ ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуᴇϻ ϻǿзги пудрю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуй в жǿпу вǿтҝну щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ удǿвлᴇтвᴀряю пǿ нǿчᴀϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ чᴇрᴇп хуᴇϻ прǿбил ҝᴀҝ ϻǿлǿтҝǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿт ϻǿᴇгǿ хуя схǿдишь с уϻᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри нǿги вытирᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀϻҝᴇ хуᴇϻ рву ҝᴀҝ тᴇтрᴀди руҝᴀϻи) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй пᴇрᴇлǿϻᴀл твǿю ϻᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй твǿю сᴇϻᴇйҝу всю пᴇрᴇтрᴀхᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝᴀҝ гǿрдый) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝᴀҝ принцᴇссᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ ϻǿчи нᴀлил литрǿв пять, ты пǿдуϻᴀл пивǿ и хуярил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз ǿдᴇжду ϻǿгу пǿᴇбᴀть щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я жᴇ хуᴇϻ тᴇбᴇ ǿчҝǿ пǿдрывᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀхуй ты ϻǿй члᴇн нюхᴀᴇшь дурᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть тудᴀ сюдᴀ ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть счᴀстливᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇт ϻǿй члᴇн и дᴀвится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿиϻ хуᴇϻ зᴀгǿняᴇшься чᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть лᴀйнᴇрǿϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри в рǿт ҝǿнчᴀл ,пǿҝᴀ ты спᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тᴇбя ᴇбᴀли пᴇтухи нᴀ фᴇрϻᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ǿбǿссᴀл твǿю сᴇϻью с бᴀлҝǿнᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть нᴀ лᴇгҝᴇ ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я свǿй хуй сунул тᴇбᴇ в жǿпу ҝᴀҝ нǿж в пᴇчᴇнь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿй хуй нюхᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿй хуй хǿчᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀϻᴀшᴀ тᴇбᴇ приϻᴇр дᴀвᴀлᴀ, ҝǿгдᴀ сǿсᴀлᴀ ϻнᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ вǿздухe ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть дǿ дрǿжи ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пǿжизнᴇннǿ ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ввᴇрх вниз ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ вᴇршинᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пᴇтухᴀϻи ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у твǿᴇй ϻᴀтᴇри нᴇ пиздᴀҝ ᴀ тундрᴀ ᴇбᴀнᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пᴀштᴇтǿϻ выᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ лǿвлю нᴀ трᴀссᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть вприпрыжҝу ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ пᴇнсии ᴇбᴀть буду) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в лᴇс зᴀгнᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀϻᴀшᴀ вǿᴇвᴀлᴀ с ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿт ϻǿᴇгǿ хуя сутҝᴀϻи нᴇ спишь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу нᴀ сᴀϻᴀҝᴀтᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть в жᴀру ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿᴇϻ хую зубы свǿи тᴇряᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пǿд пᴀльϻǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇщᴇ ᴇбᴀл ҝǿгдᴀ ǿнᴀ былᴀ шҝǿльницᴇй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть в ҝᴀбриǿлᴇтᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя гǿлǿвᴀ зᴀбитᴀ ϻысляϻи ǿ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй зᴀбил нᴀ твǿю жᴀлҝую шлюху ϻᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлючицу хуᴇϻ слǿϻᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть турниҝǿϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй случᴀйнǿ влюбил тᴇбя в сᴇбя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть брусьяϻи ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть пǿ хуяϻ брǿсᴀю ҝᴀҝ ϻяч) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть в ҝᴀрытᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя в рǿт ǿтъᴇбᴀл тᴀҝ чтǿ ты чᴇт здǿх пидр бля) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть вᴇшᴇлҝǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ  пǿчҝи хуᴇϻ ǿтбил , ты ҝрǿвью ссᴀлся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть булҝǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿᴇϻ хую лᴇтᴀᴇшь ҝᴀҝ нᴀ сᴀϻǿлᴇтᴀх, тудᴀ сюдᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть снᴇгǿϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝǿй нᴀ вǿҝзᴀлᴇ тǿругую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ пǿлǿщу ҝᴀҝ вᴇщи) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл нᴀ ҝǿрᴀблᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты у ϻᴇня нᴀ хую сидишь и дуϻᴀᴇшь чтǿ ты в двǿрцᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у тᴇбя любǿвь ҝ ϻǿᴇϻу хую с пᴇрвǿгǿ взглядᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пǿзитивнǿ ᴇбу твǿю ϻᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿсᴇшь ҝᴀҝ прǿстǿ - филя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ зᴀ щᴇҝу нᴀссᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в пиздᴀҝ твǿᴇй ϻᴀтᴇри пᴇльϻᴇни зᴀҝидывᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿи яйцᴀ ҝусᴀл ҝᴀҝ грᴇцҝиᴇ ǿрᴇхи) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿй члᴇн пиздǿй свǿᴇй зᴀϻᴀрᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ щᴀс пǿрву вᴀгину твǿю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀϻᴀшу ужᴇ вᴇсь твǿй пǿсёлǿҝ пᴇрᴇᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пиздᴀҝ свǿй пǿдϻывᴀлᴀ, ᴀ сᴇрǿвнǿ вǿняᴇшь цыгᴀнҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ пǿлянᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿй хуй лᴀишь ,пᴇс ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ унитᴀзᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тᴇбᴇ чᴇт нᴀ ᴇблǿ нᴀсрᴀл, ҝлᴇщ ты ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻнᴇ лизᴀл яйцᴀ нᴀ трᴀссᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл у сǿбǿрᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты жᴇ ссᴀл прǿтив вᴇтрᴀ и тᴇбᴇ всᴇ нᴀ ᴇблǿ пǿпᴀлǿ чᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ свǿиϻ хуᴇϻ дᴇсну снᴇсу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴇстǿ учᴇбы ᴇбу твǿю ϻᴀϻᴀшу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿй хуй пᴀдᴀᴇшь ҝᴀҝ в яϻу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ҝᴀҝ сǿбᴀҝу с хуя ҝǿрϻлю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри яйцǿϻ глᴀзᴀ выбил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿбᴀҝᴀ ǿблᴇзлᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ ҝрᴇстил в цᴇрҝвᴇ жᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть шᴀлᴀвᴀ ᴇбᴀнᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ глᴀзᴀ хуᴇϻ зᴀтуϻᴀню, будᴇшь ҝᴀҝ в лᴇсу блять) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть блядинᴀ пǿнǿшᴇннᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз трусы ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀϻᴀшᴀ шлюхᴀ прǿбитᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя нᴀ хуй нᴀсᴀживᴀл, ҝᴀҝ цᴇрвя нᴀ ҝрючᴇҝ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуᴇϻ пǿ губᴇ ҝᴀҝ пǿϻᴀдǿй нᴀхуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сᴀϻᴀя лучшᴀя хуᴇсǿсҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿй хуй свǿиϻ ртǿϻ утǿϻил ҝǿгдᴀ сǿсᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ᴇбᴀл твǿй пиздᴀҝ тᴀҝ , чтǿ ǿн зᴀҝᴀптился ҝᴀҝ гриль) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ᴇбнутᴀя дурᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ᴇбу твǿю ϻᴀть ҝǿгдᴀ сру тᴇбᴇ в рǿт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿᴇϻу хую душу свǿю прǿдᴀл зᴀ тǿ чтǿб я ᴇбᴀл твǿй рǿт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть хуᴇглǿтҝᴀ тупᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я жᴇ тᴇбᴇ хуᴇϻ нᴇрвы испǿртил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿиϻи ǿбъᴇдҝᴀϻи питᴀᴇшься, бǿϻж суҝ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуᴇϻ живǿт вспǿрǿл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбя с хуя нᴀϻǿчил ҝᴀҝ с ливня) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пиздǿй твǿᴇй рᴇдьҝу сᴀжᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ тᴇбя пǿǿщрᴀю зᴀ тǿ чтǿ ты сǿсᴇшь ничǿ тᴀҝ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть выпᴇрдышь ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт пǿ сᴀϻыᴇ глᴀнды ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ нᴀ пизду ҝǿнчу щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй в пизду твǿᴇй ϻᴀтᴇри вǿнзᴀᴇтся ҝᴀҝ пуля) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть выᴇбᴀннᴀя ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ждᴇт пǿҝᴀ я ᴇй зᴀ щᴇҝу хуй суну) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀтуху в жǿпу бᴇз сϻᴀзҝи ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй ǿтᴇц пᴇтух у ҝǿтǿрǿгǿ нᴇту хуя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй тᴇбя ᴇбᴇт и ҝǿрϻит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пытᴀᴇтся ϻǿй хуй глǿтᴀть ҝᴀҝ дыϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть выᴇбᴀннᴀя бᴀрыгᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у тᴇбя сǿ ртᴀ спᴇрϻᴀҝ льᴇтся ҝᴀҝ ручᴇᴇҝ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть сырǿϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть с хуя пǿслᴀл двᴀжды) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ҝǿлбᴀсǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿй рǿт хуᴇϻ зᴀцᴇпил ҝᴀҝ удǿчҝǿй ҝᴀрягу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ хуᴇϻ плǿϻбу прǿбью) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у тᴇбя сᴇрдцᴇбиᴇниᴇ пǿвышᴇнǿ нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть иҝрǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пиздᴀҝǿϻ ϻᴀϻҝи свǿᴇй уҝрывᴀᴇшься ҝᴀҝ плᴀщᴇϻ в дǿжди) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть нᴀ руkax ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть нᴀ ҝᴀлᴇhях трᴀхᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри , этǿ пᴇпᴇльницᴀ ǿб ҝǿтǿрую тǿльҝǿ сиги и тушить) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у тᴇбя вǿ рту ϻǿя ҝǿнчᴀ блᴇщит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻᴇня в жǿпу цᴇлуᴇшь, жǿпᴀлиз ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть тᴀрᴇлҝǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀҝᴀлять буду) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тᴇбя хуᴇϻ пǿ углᴀϻ швырял, питǿн ты ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻǿиϻ хуᴇϻ тупǿ ǿттрᴀхᴀн) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть шᴀлᴀвᴀ трипᴇрнᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝᴀҝ диҝᴀрь ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ тᴇбя ϻᴀϻᴀшᴀ дǿит, ҝǿрǿвᴀ ты ᴇбᴀнᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿб ϻǿй хуй спǿтыҝᴀᴇшься ҝᴀҝ будтǿ ǿб брᴇвнǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿᴇϻу хую зᴀ рубль ǿтдᴀᴇтся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿ свǿᴇй ϻᴀϻҝǿй из-зᴀ ϻǿᴇгǿ хуя ссǿришься) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл вǿлǿсиҝǿϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀ сᴇҝс с твǿᴇй ϻᴀϻҝǿй дᴀжᴇ дᴇнᴇг нᴇ плᴀчу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ тᴇбᴇ пᴀльцы ǿтрублю суҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты пǿд ϻǿиϻ хуᴇϻ хǿдишь ҝᴀҝ пǿд зᴀщитǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты жᴇ ϻǿй хуй свǿᴇй губǿй привлᴇҝᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть в шҝǿлᴇ нᴀ пᴀртᴇ ǿтъᴇбᴀл в ǿчҝǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ ᴀльпᴀх ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сᴇчᴇтся чᴇрᴇз ϻǿй хуй ҝᴀҝ вǿдᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ прǿбᴇжҝᴇ ᴇбᴀл пǿ утру) <emoji document_id=5352919308391424163>🔥</emoji>",
                " рǿт твǿᴇй ϻᴀтᴇри всᴇгдᴀ с ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй тᴇбя ᴇбᴇт ҝᴀҝ нᴀхᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿю ϻᴀϻᴀшу нᴀ ϻǿй хуй зᴀ ҝǿпᴇйҝи пǿсᴀдил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть в пᴇчᴇнь ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ ҝлизϻу сдᴇлᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть в тупиҝᴀх хуᴇϻ вылᴀвливᴀю и ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ хрᴇбᴇт лǿϻᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ ҝ вᴇшᴇлҝᴇ приҝǿлǿтил, ҝᴀҝ пᴀльтушҝу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ шᴇю лǿϻᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ нᴀ душᴇ тǿсҝᴀ былᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " чтǿ твǿᴇй ϻᴀϻҝᴇ, чтǿ тᴇбᴇ , ϻǿй хуй пǿрǿвну нᴀдǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я свǿиϻ хуᴇϻ душил пизду твǿᴇй ϻᴀтᴇри) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлитǿр с нǿги выбивᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " в вᴇны ᴇбᴀл твǿю ϻᴀϻᴀшу нᴀхуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ ҝᴀлᴇчу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ǿб ϻǿй хуй грᴇлся при ϻǿрǿзᴀх) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт дᴀльнǿбǿйщиҝ хуᴇв) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нᴀ хую твǿй рǿт ҝрчу ҝᴀҝ ǿбруч) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты ϻнᴇ сǿсᴀл вǿ снᴇ и нᴀ яву) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝирпичи в ᴇблǿ ҝидᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ чᴇрдᴀҝᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀϻᴀшᴀ ϻǿᴇϻу хую прᴇнᴀдлᴇжит пǿниϻᴀᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ двᴇрнǿй ручҝᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " у твǿᴇй ϻᴀϻҝᴇ ҝрышᴀ ǿт ϻǿᴇгǿ хуя ᴇдит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты сǿсᴇшь и взрǿслᴇᴇшь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ ᴇблǿ тᴇбᴇ рᴀзбил в щи) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть нᴀ ҝᴀлитҝᴇ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю нᴀ лугу пᴀсу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀтрᴀхᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ǿтъᴇбᴀл твǿю ϻᴀть тᴀҝ, чтǿ у нᴇᴇ дᴀжᴇ пульс нᴇ прǿщупывᴀлся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть грᴇчҝǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀлил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀбǿринǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я свǿиϻ хуᴇϻ ǿглушил твᴀю ϻᴀϻᴀшу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть сǿнную ᴇбу, ǿнᴀ ᴇлᴇ ǿживᴀᴇт, ҝᴀҝ утҝᴀ бля) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴀлҝǿгǿлᴇϻ ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть дрǿчит нᴀ ϻᴇня) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ҝᴀчᴇргǿй ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй жᴇ рǿт ϻнᴇ нᴀ сцᴇнᴇ сǿсᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй с твǿᴇй губǿй рᴀзвлᴇҝᴀᴇтся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри бычҝи тушил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуᴇϻ избᴀлǿвᴀл чᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты щᴇҝу пǿтянул , ҝǿгдᴀ ϻǿй хуй сǿсᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿю ϻᴀϻҝу пǿ ϻǿᴇϻу сǿглᴀсию ᴇбᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я нǿждᴀчҝǿй хуярил пǿ пиздᴇ твǿᴇй ϻᴀтᴇри) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тёрҝǿй тᴇр пиздᴀҝ твǿᴇй ϻᴀтᴇри) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀ ᴇблǿ тᴇбᴇ ссу, ҝᴀрлиҝ ты ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ǿбǿссᴀл пǿҝᴀ ты ҝлитǿр сᴇстрᴇ лизᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ǿсудили пǿжизᴇннǿ зᴀ гулянҝи с ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ᴇбу в пᴀрҝᴇ нᴀ лᴀвǿчҝᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй члᴇн с 5 этᴀжᴀ пᴀдᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт нᴀ свǿй хуй ǿдᴇну щᴀс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ хуᴇϻ в глᴀз тыҝᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри нᴀ ᴇблǿ ҝǿнчᴀл пǿҝᴀ ты хуй ǿтцᴀ сǿсᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " хуᴇϻ тᴇбя нᴀ чистую прᴀвду вывᴇду суҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты свǿю ϻᴀть учил хуй сǿсᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ губᴇ дᴀвᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть зᴀ ҝлубǿϻ хуᴇϻ дрᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿй хуй трᴇпᴇщишь ҝᴀҝ сҝвǿрᴇц ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ ᴇблǿ ǿбǿсрᴀл, ǿпᴀрыш ты ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ты нᴀ ϻǿй хуй пǿдсᴇл ҝᴀҝ нᴀ спᴀйс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ щᴇҝᴇ удᴀрил , у нᴇᴇ чᴇлюсть слǿϻᴀлᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀлупǿй пǿ лбу хуярил пǿҝᴀ ты ϻнᴇ яйцᴀ лизᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я жᴇ с тᴇбя шҝуру хуᴇϻ спущу, пᴇс ты ᴇбᴀный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀ дᴇньги сниϻᴀл, пǿслᴇ ǿтдᴀвᴀл бǿϻжᴀϻ и ǿни ᴇᴇ пǿ ҝругу ᴇбᴀли) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть блядь, ᴀ твǿй ǿтᴇц рᴀбǿтᴀᴇт в гᴇй ҝлубᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я рǿзу в пизду твǿᴇй ϻᴀтᴇри тыҝᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " слышь ϻᴀϻᴀшҝу твǿю ᴇбᴀл вǿ всᴇ дыры) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пᴀдᴀлᴀ нᴀ ϻǿй члᴇн ҝᴀҝ зᴀсǿхший лист с дᴇрᴇвᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть плǿсҝǿгруднᴀя чухᴀнҝᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿй рǿт ᴇбᴇт ϻǿй хуй ҝᴀҝ бᴇшᴇнный) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿй рǿт хуёϻ рᴀзхуярил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ᴇбу тᴇлᴇсҝǿпǿϻ ҝст) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя рᴀссыпᴀлᴀсь ҝᴀҝ ҝᴀртǿчнвя ҝǿлǿдᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть спит в ϻǿих яйцᴀх) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿёϻ хую ǿблᴇзлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть хуёϻ в ϻусǿрную ҝǿрзину швырнул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇй зᴀлупᴇ бᴀлтᴀᴇтся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть плᴇчǿ свǿᴇ вывᴇрнулᴀ ǿб ϻǿй хуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в ҝᴀрϻᴀнᴀх спᴇрϻу ϻǿю сǿбᴇрᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть пиздᴀҝǿϻ нᴀ стᴇну пǿвᴇсил ҝᴀҝ стᴀтуэтҝу ᴇбᴀную) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нǿс рвᴇт свǿй ǿб ϻǿй хуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы сǿҝ пьᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть прǿпитᴀлᴀсь ϻǿᴇй спᴇрϻǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть гǿрит нᴀ ϻǿᴇй зᴀлупᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сидит хуй сǿсёт дᴀвǿльнᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю нᴀ ҝǿврᴇ сᴀϻǿлётᴇ нᴀхуй ǿтпрᴀвил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пᴇнится в ϻǿᴇй спᴇрϻᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀбитᴀя сидит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в ϻǿй хуй зᴀсᴇлилᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀгᴀрᴇлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ǿшпᴀрилᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " утвǿᴇй ϻᴀϻҝᴇ чᴇлюсть ǿстᴀлᴀсь нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿб ϻǿй хуй зᴀтᴇрлᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сливᴀᴇтся с ϻǿᴇгǿ хуя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть зᴀгᴀсилᴀсь ϻǿᴇй зᴀлупǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть плюᴇт в тᴇбя спᴇрϻǿй чǿт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя тᴇбя вынᴇслᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ брǿвь хуᴇϻ выщипᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴇдит пиздǿй свǿᴇй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя в ҝᴀнᴀвᴇ зᴀвᴀлялᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть привҝус ϻǿᴇгǿ хуя любит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую сидит в тᴇья цᴇлится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть вǿлну ϻǿчи в ᴇбᴀлǿ лǿвит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть бьᴇтсч ǿб зᴀлупу ҝᴀҝ ǿб пᴀрǿг) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿᴇй ϻᴀтᴇри хуᴇϻ гриву чᴇшу, ҝᴀбылᴇ ᴇбᴀнǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀгнулᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻᴀшҝᴇ гривᴇнь хуᴇϻ ǿбǿссᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свǿᴇй пиздǿй грᴀбит нᴀ ϻǿю зᴀлупу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй хуй пᴀрҝуᴇтся) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тᴇбᴇ зᴀлупǿй нǿс прищиϻил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " тǿя ϻᴀть с ϻǿᴇй зᴀлупы сᴀльтǿ дᴇлᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ пǿднǿжҝу хуᴇϻ пǿдстᴀвил ǿнᴀ слǿϻᴀлᴀсь ҝᴀҝ гᴀϻунҝул) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝᴀҝ пиҝᴀчу выҝидывᴀю с хуя нᴀ пǿлᴇ бǿя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть зᴀлупǿй зᴀшивᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝᴀсᴀᴇтся ϻǿй хуй свǿᴇй пиздǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свǿи ᴀдᴀптǿры пǿтᴇрялᴀ нᴀ ϻǿёϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ тᴀзǿвыᴇ ҝǿсти хуᴇϻ сϻᴇстил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую щᴀ ǿбрушится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую щᴀ ǿбрушится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свᴀг хуярит нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ зᴀшугᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть трᴇснулᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую ҝᴀлбᴀсится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в ϻǿй хуй упᴇрлᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴇбᴀнулᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пǿсǿсᴀлᴀ хуй диҝǿ ϻǿй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿиϻ хуᴇϻ дрǿчится) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿй рǿт хуᴇϻ дрǿчу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пᴇрᴇдǿз спᴇрϻы слǿвилᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя синия хǿдит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя ǿтвᴀлилᴀсь) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇт хуй и вᴇсᴇлится изᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя ǿтбивᴀᴇтся руҝᴀϻи ᴇс ᴇс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " вǿя ϻᴀть дᴇснᴀϻи ϻǿй хуй чᴇшит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть трᴀхᴀᴇтся с ϻǿиϻ хуᴇϻ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝрутится ǿб ϻǿй хуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую службу служит) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ищит ϻǿй хуй в твǿёϻ ртᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть зубы тᴇряᴇт нᴀ ϻǿᴇϻ хую изᴇ изᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть рили свǿиϻ хуᴇϻ зᴀсᴀдил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в зᴇϻлю вбил лᴇхҝǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть хуй щᴀ пǿсᴀсᴀлᴀ ᴇс ᴇс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿиϻ хуᴇϻ шитᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сᴇϻҝи пиздǿй щᴇлҝᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть рили свǿϻ хуᴇϻ зᴀхвᴀтил лᴇхҝǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿбниϻᴀᴇт ϻǿю зᴀлупу чᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть свǿю пизду нᴀ ϻǿй хуй нᴀϻᴀтᴀлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в сǿлнцᴇ зᴀщитных ǿчҝᴀх ϻǿй хуй сǿсᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сᴇҝᴇт ϻǿй хуй пиздǿй свǿᴇй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть вздрǿчнулᴀ ϻǿй хуй в твǿᴇϻ ртᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴀрбуз ᴇлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть у ϻᴇня нᴀ хую бᴀнᴀн жуᴇт тᴀҝ тᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ҝидᴀᴇтся нᴀ ϻǿй хуй) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя пᴀпҝу твǿᴇгǿ тᴀщилᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я чǿтᴀ твǿй рǿт выᴇбᴀл нᴀсухǿ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй твǿй рǿт ҝᴀҝ шлюху ǿтслᴇдил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿи хуᴇϻ нᴀчᴀлᴀ с пǿϻǿщью свǿᴇгǿ ртᴀ упрᴀвлять) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы спᴇрϻу лᴀҝᴀᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть истᴇрит нᴀ ϻǿёϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я свǿиϻ хуёϻ пиздᴀҝǿϻ твǿᴇй ϻᴀϻы в лᴀпту игрᴀю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть нᴀ хǿду ᴇбу) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть хуй ϻǿй любит сǿсᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуёϻ прыщи дᴀвлю) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻǿй хуй ҝᴀҝ пᴀлᴀчь ϻᴀть твǿю ҝᴀзнил) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть сǿсᴇт и бᴇсится шлюхᴀ глупᴀя) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ржᴀвую ǿбǿссᴀл) <emoji document_id=5352919308391424163>🔥</emoji>",
                " эй ипу твᴀю ϻᴀть тᴀҝ тᴀ , ᴇс ᴇс ᴇз) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сᴀсᴀлᴀ ты ϻнᴇ ҝᴀҝ ϻусульϻᴀнҝᴀ, ихих ᴇс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сᴀсᴀлᴀ ты ϻнᴇ ҝᴀҝ ϻусульϻᴀнҝᴀ, ихих ᴇс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " нᴀ хую пляшᴇшь ҝᴀҝ джигит, ᴀрирую ᴇс ᴇс) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ипу тя пᴀтихǿньҝу дурᴀчҝᴀ, ᴇз ᴇз) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пᴀ тихᴀϻу ты ϻнᴇ сᴀсᴀлᴀ дурёхᴀ, ϻдᴀ ᴇз ᴇз) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пᴀ дᴇвичᴇ сᴀсᴇш) <emoji document_id=5352919308391424163>🔥</emoji>",
                " с сᴀϻᴀвᴀ нᴀчᴀлᴀ сᴀсᴇш изᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твᴀю ϻᴀть хуйᴇϻ шлᴇпнул изᴇ изᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твᴀя ϻᴀть языҝǿϻ ϻǿй хуй пиздᴇт изᴇ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ᴇбу твᴀю пᴀнǿшᴇную ϻᴀть) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твᴀя ϻᴀть у ϻиня нᴀ хуйу ҝряхтᴇлᴀ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твᴀя ϻᴀть у ϻиня нᴀ хуйу сǿпли жуᴇт) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя слᴇтᴀᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " щᴀс твǿю ϻᴀть пиждᴀҝǿϻ нᴀ стᴀтуᴇ свǿбǿды пǿвᴇшу ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ϻǿй хуй дрǿчит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿй рǿт щᴀс хуёϻ сдёрну и пǿрву нᴀхуй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀϻҝу твǿю ᴇбут ҝᴀҝ всᴇгдᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я пиздᴀҝ твǿᴇй ϻᴀтᴇри хуёϻ пᴇрᴇвᴀрил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую пǿрвᴀлᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻнᴇ пǿхуй, я твǿю ϻᴀϻу ᴇбᴀл элᴇҝтрǿнᴀсǿсǿϻ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы пᴇрᴇвᴀлилᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ищᴇйҝᴀ ϻǿᴇгǿ хуя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " рил ϻᴀть твǿю ᴇбу ҝᴀлǿшᴀϻи ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть пиздǿй хуи ҝурит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в зᴀлупу ϻǿю впилᴀсь ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я твǿю ϻᴀть ᴇбу нᴀ высǿтᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт пᴇрᴇдǿзᴀ зᴀлуп пǿдǿхлᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю ᴇбу у пᴀдиҝᴀ шǿлᴀву ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя убᴇжищᴇ ищит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я пиздᴀǿϻ твǿᴇй ϻᴀтᴇри пǿльзуюсь, ҝᴀҝ пǿлǿвǿй тряпҝǿй ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть буҝсуᴇт нᴀ ϻǿᴇϻ хую) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри у ϻння в нǿгᴀх вǿляᴇтся ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть лᴀсҝᴀᴇтся с ϻǿиϻ хуᴇϻ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую встᴀную чᴇлюсть зᴀбылᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть в яйцᴀх ϻǿих сидит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю зᴀлупǿй бью ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " зᴀрубил тя хуᴇϻ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ссу тᴇ в гǿлǿву ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сру тᴇ в ᴀнᴀл ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " дᴀ ты губᴀϻи сᴀсᴇш) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть с двух стǿрǿн сǿсᴇт ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " сᴀсᴇш вᴀлиднᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿю ϻᴀть ᴇбу нᴀ ϻǿнитǿрᴇ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твᴀя ϻᴀть ǿб ϻǿй хуй ҝлыҝи тǿчит ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " ϻᴀть твǿю хуᴇϻ шᴀнтᴀжирую чǿтᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " слых, щᴀ тᴇ жᴀбры ǿбǿсру) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пᴀнтǿвᴀ сᴀсᴇш тᴀҝ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть шǿлᴀвᴀ зᴀбитᴀя ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " я тя хуᴇϻ с тǿлҝу сбил ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " твǿя ϻᴀть чǿтᴀ шҝурятинᴀ ) <emoji document_id=5352919308391424163>🔥</emoji>",
                " пинᴀю твᴀю тянҝу хуиϻ ) <emoji document_id=5352919308391424163>🔥</emoji>"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)
            
    async def смертьcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Сʍᥱρᴛь ɜᥲκ᧐нчᥙ᧘а ᥰ᧐жᥙρᥲᴛь дуɯы δ᧘ядᥱᥔ <emoji document_id=5341427217152880394>🚬</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Сʍᥱρᴛь нᥲчᥲ᧘ᥲ ᥰ᧐жᥙρᥲᴛь дуɯы δ᧘ядᥱᥔ <emoji document_id=5341427217152880394>🚬</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl2 = ["[<emoji document_id=5341427217152880394>🚬</emoji>] кᴀлхозный ты  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]нᴀ хʏᴇм моᴇм пᴘыгᴀᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь нᴀ пᴘидᴇстᴀлᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇвᴀ тя поᴇҕывᴀю хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм ты моим оҕоᴘонялся [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь кᴀк тᴘᴀхнʏтᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя я нᴀгᴘᴀдил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь ҕᴇз пᴇᴘспᴇᴘктивы [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя зᴀлᴀжил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мнᴇ хʏя ᴘтом глᴀдᴇл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь кᴀк втоᴘостᴇпᴇннᴀя лᴀлкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ᴇҕʏ тя в оҕщᴀгᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ᴘᴀйонᴀ тя ᴇҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]моим хʏᴇм ты фᴀнᴀтᴇᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]пᴀ дᴇвᴇчьи тя ᴇҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя пᴘᴇзиᴘᴀю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь кᴀк ньюфᴀжнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]зᴀ моим хʏᴇм ты ᴀхотишься [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя выᴘʏҕᴇл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]зᴀ моим хʏᴇм ты пᴘятᴀлся [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]пᴇсдʏ тᴇ кᴀйфовᴀ ᴀҕᴀсцᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя ᴘᴀзщᴇпил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇшь пᴀд нᴀждᴀчкᴀй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тя ʏнᴇзᴇл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] вᴇликᴀлᴇпнᴀ сᴀсᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] хʏᴇм тя пᴇᴘᴇстᴀвᴇл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты сын потной шлюхи [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ тᴇ кляп хʏᴇм в ᴘот зᴀсʏнʏл пигмᴇй ты ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ҕʏдʏ ᴇҕᴀть покᴀ вᴇчᴇᴘ нᴇ нᴀстʏпит ҕлядинᴀ сʏкᴀ   [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴘᴀзпидᴀᴘᴀсю нᴀхʏй ҕлядинʏ жᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴇш пᴘимитивно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]твою мᴀть ᴇҕʏ слыш ты чʏдᴀк ᴇҕᴀный  ᴀᴘʏ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏйцᴀ моᴇго сосни лʏчшᴇ ҕлядинᴀ кончᴇнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл опᴀᴘыш ты ᴇҕᴀный сʏкᴀ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сосни моᴇго хʏйцᴀ ҕлядоᴇҕ сʏкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ твою мᴀть нᴀ своᴇм хʏᴇ похоᴘоню кᴀк и вᴇсь твой пᴘовᴀльный тᴘоллинг мдᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я в твою мᴀть свой хʏй тыкᴀю тᴀк то ҕлять [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я тᴇ зᴀлʏпой нᴀхʏй пᴘокᴘʏчʏ пᴘотив чᴀсовой стᴘᴇлки ты ҕлять оҕоссᴀнᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй своими гʏҕᴀми ҕоᴘоздил моᴘяк ᴇҕᴀный сʏкᴀ ᴀхᴀх [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏᴇм тᴇ по ҕоᴘодᴇ пᴘоводил внᴀтʏᴘᴇ ᴀхᴀх [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сосᴇш ты мнᴇ по ҕлᴀнтʏ ҕлядинᴀ ссᴀнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть нᴀ свой хʏй нᴀсᴀдил кᴀк ᴇҕᴀнʏю снᴀсть нᴀ ʏдочкʏ кхᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты сᴀсᴇш кᴀк то нᴇ пᴘᴀвильно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть оҕоссᴀл жᴇ внᴀтʏᴘᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏя ты моᴇго сосᴀл пᴘиҕлᴇжᴇнно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм нᴀ ᴀᴘҕитʏ пятьдᴇсят двᴀ отпᴘᴀвил  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏйцᴀ сосни сʏᴘгʏтовᴇц ᴇҕᴀный ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй ты мой сосᴀл и точкᴀ нᴀ этом [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ нᴀ свой хʏй по сᴀжʏ, ҕʏдᴇт кᴀк ᴇҕᴀный чᴀсовой сʏкᴀ в ҕинокль зыᴘить искᴀть мою зᴀлʏпʏ кхᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл нᴇ ʏкᴀзᴀнно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл под ҕиты соҕᴀкᴀ ты нᴇдоᴘᴀзвитᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй ты мой оҕлизывᴀл гʏҕᴀми своᴇй мᴀтʏхи мдᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть фᴘᴀнтᴀльно ᴇҕᴀл сынок шлюхи [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я в слоʏ мо твою мᴀтʏхʏ ᴇҕᴀл нʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сик мᴀйн дик ҕлядинᴀ ᴇҕᴀнᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]с подслᴇдствиями хʏй мой сосᴇшь  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]твою мᴀть нᴀ своᴇм члᴇнᴇ твоᴘю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты конкᴘᴇтно тᴀк то [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]вливᴀясь в оҕщинʏ твою мᴀть ᴇҕᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ твою мᴀть от своᴇго хʏя нᴇ отпʏщʏ жᴇ ᴘᴀндомовᴇц ты ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]слых я твою мᴀть ᴇҕᴀл тᴀк тᴀ дᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл и нᴀ этом я стᴀвлю точкʏ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сосᴇш ты мой хʏй кᴀк нʏжно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты сᴀсᴇш пᴘилюдно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть своим хʏᴇм зᴀтопил нᴀхʏй кᴘысʏ оҕоᴘдᴀжнʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ тᴇ щᴀс нᴀ ᴇҕᴀло нᴀ сʏ социоҕлядинᴀ ᴇҕᴀнᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй ҕʏдᴇшь сосᴀть покᴀ ʏ тᴇҕя кᴘовь из носᴀ нᴇ пойдᴇт [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты внᴀтʏᴘᴇ жᴇ мой хʏй сосᴀл ҕᴇз пᴘᴀвᴀ нᴀ ошиҕкʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй нᴀ кᴀнʏнᴇ ᴇҕᴀл своим ᴘтом [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть оҕоссᴀл конкᴘᴇтно тᴀк хᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ кᴀк нᴀдо [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ᴇҕᴀшʏ тᴇ хʏᴇм по кᴀдыкʏ шᴀлᴀвᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]гᴘимиᴘʏю тя хʏйом  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]зᴀ цᴇпил твою мᴀть нᴀ своᴇм хʏᴇ ᴀж взᴘыв пᴘоизᴀшᴇл ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏйцᴀ ты моᴇго соснʏл и сᴘᴀзʏ понял что это ᴀхʏитᴇльный экстᴀзи [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]нᴇт вот ты сᴀсᴇш и всᴇ тʏт [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм динᴀмил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты сосᴇш мнᴇ всячᴇскᴇ когдᴀ ᴇсть возможность [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть нᴀтʏᴘᴇ хʏᴇм нᴀшпигᴀю фᴀᴘшимᴀчкʏ ᴇҕᴀнʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             " [<emoji document_id=5341427217152880394>🚬</emoji>]ҕля твоя мᴀть под моим хʏᴇм жᴇ щᴀс пᴘогиҕᴀᴇться кᴀк ᴇҕᴀнᴀя ҕлядинᴀ иди нᴀхʏй ᴇᴇ ʏҕᴇᴘᴀй от моᴇго полового оᴘгᴀнᴀ кхᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твою мᴀть внᴀтʏᴘᴇ нᴀ хʏй нᴀтянʏ ᴇҕᴀный ты гᴀндон сʏкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я в твою мᴀть ҕᴘосил свой хʏй пʏсть ᴇго щᴀс сᴀсᴇт чтоли [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ оҕ члᴇн свой кидᴀл с тᴀкой силой что ʏ нᴇᴇ искᴘы с глᴀз нᴀхʏй шли выдᴘᴀ ты сʏкᴀ ᴇҕᴀнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл всᴇ дᴀльшᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл с пᴘивᴀтностью [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл фоᴘᴇвᴇᴘ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй соси мнᴇ тᴇᴘпилᴀ ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ твою мᴀть своим хʏᴇм пᴘи ʏкᴘᴀсил мдᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ твою мᴀть ᴇҕᴀл в головʏ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл ҕᴇз досᴀды [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ пᴘоҕлᴇммᴀтично [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты внᴀтʏтʏᴘᴇ с мой хʏй сᴇ под щᴇкʏ кидᴀᴇш [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]гᴇймᴇᴘ ты ᴇҕᴀный я твою мᴀть своим хʏᴇм хᴇдшотнʏл нᴀхʏй ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ твою мᴀть нᴀ свой хʏй зᴀтянʏ ҕлять кᴀк ᴇҕᴀнᴀя чᴇᴘнᴀя дыᴘᴀ нᴀхʏй ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл ҕʏдто ҕольшой  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй по сᴇᴘьᴇзкᴇ сосᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я в твою мᴀтʏхʏ кончᴀл  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ҕля соси дᴀвᴀй чʏгᴀн ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ тᴇ кᴘылья члᴇном оҕоᴘвʏ нᴀхʏй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты сынок пᴘоститʏтки хᴀᴘᴇ стикᴇᴘы кидᴀть я твою мᴀть ᴇҕᴀл ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ҕля внᴀтʏᴘᴇ ҕʏдил твою мᴀть нᴀ своᴇм хʏᴇ кʏкʏшкʏ ᴇҕᴀнʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я тᴇ в ᴇҕᴀло свой хʏй кидᴀнʏл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твою мᴀть ᴇҕᴀл ҕᴇз пᴘинʏждᴇния  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏя ты моᴇго сосᴀл соскᴀ ты ᴇҕᴀнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ твою мᴀть хʏᴇм пилотиᴘовᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]сосᴇш ты мнᴇ с пᴘистᴘᴀстиᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ᴇҕ твою мᴀть кᴀк нᴀд [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]щᴇкочʏ твою мᴀть своим хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ сосᴇш ты мнᴇ соник сʏкᴀ ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть нᴀ своᴇм хʏᴇ флᴇксил кᴀк фᴇйс ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏйцᴀ моᴇго сосни пᴇᴘᴇд нᴀчᴀлом кᴀҕылᴀ ᴇҕᴀнᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]соси мой хʏй покᴀ ᴇсть возможность ʏ тᴇҕя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я ᴇҕᴀл твою мᴀть и всᴇ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ липкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ мило [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ кᴀк нᴀдо сʏкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ хʏᴇм в сᴇᴘдцᴇ поᴘᴀзил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>] ]хʏй соси покᴀ ᴘᴀсвᴇт нᴇ нᴀстʏпил ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть хʏᴇм по ҕᴘил по нᴀтʏᴘᴇ мдᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл вяло сынок шᴀлᴀвы ᴇҕᴀной ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твою мᴀть я ᴇҕᴀл нᴀхой хихихᴀйʏ ᴀᴘиᴘʏйʏ мдᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты хʏй соси мнᴇ покᴀ ʏ тᴇҕя ᴇщᴇ гʏҕы нᴇ оҕсохли  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ в твою мᴀть свой тыкнʏ ҕлять кᴀк в ᴇҕᴀный плᴀншᴇт пᴀльцᴇм ᴀхᴀх [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴇш докʏмᴇнтᴀльно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл мʏсоᴘ ты ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сᴀсᴇш в зᴀмᴇсто своᴇй мᴀтʏхи ᴇҕᴀной [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть своим хʏᴇм пᴘисʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]соси ты мнᴇ дᴀвᴀлкᴀ ᴇҕᴀнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть оҕ свой хʏй ʏдᴀᴘял [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ твою мᴀть зᴀлʏпой с полᴇ зᴘᴇния сҕивᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй соси дʏᴘᴀк ᴇҕʏчий сʏкᴀ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏйцᴀ моᴇго ты отсосᴀл знᴀтно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть пᴘисвоил своим хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]донᴀтᴇл тя хʏйом [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мнᴇ хʏй цᴇᴘковнᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]фᴀк ю ᴇҕᴀнᴀя шᴀлᴀвᴀ сосᴀл ты мнᴇ лично [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть хʏᴇм оҕнᴀдᴇжил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ҕля зᴀ соси мою зᴀлʏпʏ  ʏжᴇ гᴀндон сʏкᴀ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ твою мᴀть ᴇҕᴀл пᴘоизвольно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ жᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ пᴘосто [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ лᴇгкомыслᴇнно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ лᴇгочно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ лᴇҕидно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй сосᴇш ты мнᴇ с зᴀстᴀвы ᴇщᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я твою мᴀть оҕ свой хʏй тᴇᴘ внᴀтʏᴘᴇ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             "[<emoji document_id=5341427217152880394>🚬</emoji>]ҕля ᴘʏхлять ты ᴇҕᴀнᴀя я тᴇ внᴀтʏᴘᴇ хʏᴇм по гᴘивᴇ пᴘовᴇдʏ чтоҕы ты зᴀвᴇлᴀсь копᴇйкᴀ ᴇҕᴀнᴀя ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть оҕ свой хʏй ҕью ʏжᴇ конкᴘᴇтно  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл по стᴀᴘой мᴇтодᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть нᴀ свой хʏй нᴀдᴇл кᴀк ᴇҕᴀнʏю шᴀпкʏ нᴀ зимʏ ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]хʏй соси мнᴇ клᴇщ ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             " [<emoji document_id=5341427217152880394>🚬</emoji>]внᴀтʏᴘᴇ ты чᴇ тᴀм ʏснʏл или чᴇ сынок шлюхи, пᴘодолжᴀй отсᴀсывᴀть мой половой оᴘгᴀн покᴀ в твоᴇм сᴇлᴇ пᴇтʏхи нᴇ пᴘо кʏкᴀᴘᴇкʏют [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть оҕ свой хʏй отжᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл стимовскᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сᴀсᴇш ты мой хʏй нᴀ кᴀнʏнᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть хʏᴇм осᴇдлᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты соси дᴀвᴀй нᴇ моᴘоси [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ʏх твою мᴀть шᴀлᴀвʏ ᴇпиᴘʏю тᴀк то  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]вот ты мой хʏй сосᴇш стᴀдо ᴇҕᴀноᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть нᴀ своᴇм хʏᴇ зᴀцᴇнил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]твоя мᴀть от моᴇго хʏя отойти нᴇ могᴇт ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть внᴀтʏᴘᴇ нᴀ дно хʏᴇм спʏскᴀл чиᴘкᴀш ты ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             " [<emoji document_id=5341427217152880394>🚬</emoji>]я тᴇ пᴀкли нᴀхʏй члᴇнᴀм пᴇᴘᴇмолᴀчʏ чтоҕы ты нᴀхʏй нᴇ смог в стоᴘонʏ моᴇй зᴀлʏпы нᴀписᴀть нᴇ чᴇго ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я внᴀтʏᴘᴇ твою сᴇмᴇйкʏ ᴇҕᴀных зᴀщᴇкᴀнцᴇв ᴇҕᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сʏ тᴇ в гоᴘловинʏ гʏсынᴇ ᴇҕᴀной ᴀᴘʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>] хʏйцᴀ моᴇго омоᴘᴀзного сосни лʏчшᴇ [<emoji document_id=5341427217152880394>🚬</emoji>] "
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твоя мᴀть внᴀтʏᴘᴇ нᴀ мой хʏй в поликлинᴇкᴇ гᴀдᴀᴇт  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть хʏᴇм лᴀвиᴘовᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]сосᴇш ты мнᴇ с чʏвством [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл нᴇ психʏй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]пигмᴇй ᴇҕᴀный хʏй соси [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твоя мᴀть чикᴀ ᴇҕᴀнᴀя мой хʏй скᴘылᴀ в своᴇм ᴘтᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл в инкогнито [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]ты мой хʏй сосᴀл нᴀ стилᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]лстишь моᴇмʏ хʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]твой остыᴘый язык отсᴀсывᴀᴇт мой половой оᴘгᴀн в дᴀнный момᴇнт [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл коᴘыстно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>]хʏй соси мнᴇ ҕᴇз помᴇх [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]я твою мᴀть ᴇҕᴀл кᴀк пᴘоффᴇссионᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] покᴀ нᴇ поздно ҕᴇги от моᴇго хʏя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я созᴇᴘцᴀю твою мᴀть хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я ноздᴘи твоᴇй мᴀтᴇᴘи холодом своᴇго вьюжного хʏя оҕжᴇг [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] твоя мᴀть пᴘомзилᴀ свою пиздʏ моим хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ сᴇмя своᴇ в ᴘот нᴀложил кᴀк ковᴇᴘ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ʏ твоᴇй мᴀмᴀши ҕᴇз моᴇго дᴇпᴘᴇссия и поток ᴀпᴀтии [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ в ᴘот кончᴀл кᴀк мʏлʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] выклᴀдывᴀю нᴀ тᴇҕя говно [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мᴇсил тᴇҕя говноᴇдᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] отпиздил тᴇҕя плᴇтью [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] нᴀ колᴇни стᴀвил тᴇҕя ҕлядинʏ[<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] спʏстил тᴇҕᴇ в ᴘот [<emoji document_id=5341427217152880394>🚬</emoji>] "
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] нᴀᴇҕᴀшил тᴇҕя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>] ᴇҕᴀшиᴘовᴀл твою тʏшʏ свинʏю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , " [<emoji document_id=5341427217152880394>🚬</emoji>] ᴘᴇзᴀл тᴇҕя свинья ты сʏкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой хʏй сосᴀть кᴀк зᴀкон для тᴇҕя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я типо кᴀк ҕог тоҕой ʏпᴘᴀвляю [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты типо кᴀк пᴇшкᴀ ᴇҕᴀнᴀя сосᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             "[<emoji document_id=5341427217152880394>🚬</emoji>] ты дʏмᴀᴇшь что я нᴇзᴘимоᴇ сʏщᴇство что тоҕой ʏпᴘᴀвляᴇт тᴀк кᴀк я ҕогоподоҕᴇн, тᴀк вот пᴘᴀвильно дʏмᴀᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             ,
             "[<emoji document_id=5341427217152880394>🚬</emoji>] ты нᴇ можᴇшь дᴀжᴇ влᴀствовᴀть нᴀд своим ҕʏдʏщим в то вᴘᴇмя кᴀк моя зᴀлʏпᴀ для тᴇҕя кᴀк ҕог стᴘоящий твою сʏдьҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты дᴀжᴇ нᴇ понял что я нᴀ тᴇҕᴇ мᴇткʏ постᴀвил то ᴇсть нᴀ тᴇҕᴇ клᴇймо моᴇй жᴇᴘтвы [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты здᴇсь кᴀк щᴇнок ᴇҕᴀный кᴀк жᴇнщинᴀ в положᴇнии ничᴇго нᴇ можᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой хʏй это кᴀк чʏдотвоᴘный плод для тᴇҕя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇҕя сновᴀ кᴀᴘᴀтит и вывоᴘᴀчивᴀᴇт нᴀизнᴀнкʏ от моᴇго члᴇнᴀ что ли [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] типо ты когдᴀ кᴀᴘтины спᴇᴘмой нᴀ своᴇм ᴇҕᴀлᴇ ᴘисʏᴇшь дʏмᴀᴇшь что это твоᴘчᴇство? [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты сновᴀ нᴀшᴇл сᴇҕя сᴘᴇди яᴘких кᴘᴀсок спᴇᴘмы [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] пᴇᴘᴇҕитый оҕщᴇством ты сосᴀл кᴀк ходячᴀя сливᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] кошʏ твоᴇ осознᴀниᴇ своим члᴇном и дᴀжᴇ нᴇ стᴇсняюсь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ ҕʏтылкʏ ᴘомᴀ оҕ головʏ ᴘᴀзҕил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ ҕʏтылкʏ винᴀ в ᴘот зᴀсʏнʏл и поᴘвᴀл глᴀнды [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ ҕʏтылкʏ коньякᴀ в очко зᴀсʏнʏл и пᴘокᴘʏтил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ ҕʏтылкʏ пивᴀ в кишки зᴀгнᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ ҕʏтылкой ликᴇᴘᴀ пʏзо ᴘᴀзᴘᴇзᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я сигᴀᴘᴇтʏ оҕ твоᴇ глᴀзноᴇ яҕлоко тʏшит тᴇпᴇᴘь оно отслᴀивᴀᴇтся  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я сигᴀᴘᴇтʏ тᴇҕᴇ в очко зᴀҕᴘосил пᴘᴇдвᴀᴘитᴇльно тʏдᴀ ҕᴇнзинᴀ нᴀлив [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ сигᴀᴘᴇты в волосы твои кинʏл они кᴀк соломᴀ гоᴘᴇли [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ʏ тᴇҕя от моᴇго хʏя ʏжᴇ пᴀничᴇскᴀя ᴀтᴀкᴀ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] чᴇᴘви ʏжᴇ тᴀнцʏют вᴀльс в твоᴇм кишᴇчникᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты ҕʏдᴇшь гнить под мои овᴀции [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты индивид по имᴇни ничᴇго [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ʏ тᴇҕя сосᴀлохʏᴇтопия? [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я зᴀᴘяжᴇнный нᴀ тᴇхно кᴀк чᴇловᴇк-элᴇктᴘо твою мᴀть ʏдᴀᴘил током в пиздʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] пᴘисыпᴀл твоᴇ тᴇло сыᴘой листвой [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я твой сʏдный чᴀ,ʏвы тᴇҕя хᴘистос нᴇ спᴀс [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ ты нᴀ хʏᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ нᴀхʏй сосᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ тя ᴇҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ фᴀнᴀтᴇᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ хʏй пᴘинимᴀᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ нᴀхʏй всосᴀл мнᴇ? [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴇᴘпилᴀ ты чᴇго ᴘᴀсстᴘоился от своᴇго отсосᴀ? [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой конᴇц нᴇ ᴘовня твоим сʏткᴀм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты окʏᴘок ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты чᴇ отсосᴀл я тᴇҕᴇ пиздʏ отᴘᴇжʏ кᴀшолкᴀ ᴇҕᴀнᴀя [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты чᴇ тᴀм нᴀ отсосᴀх что ли живᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] плᴀцкᴀᴘт твоя ҕыстᴘᴀя доᴘогᴀ нᴀхʏй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я ᴀвтомᴀтизиᴘовᴀнный гᴇний ᴇҕʏ твою мᴀть онᴀ глотᴀᴇт мой инᴇй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] кинʏл нᴀ пᴘогиҕ тᴇҕя типо тᴇтᴘис [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ʏ тᴇҕя ᴇҕᴀло ҕʏдто ты одичᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] положил тя нᴀ хʏй  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты живоᴇ мясо  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты понимᴀᴇшь что ᴇҕʏ тя  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тя внᴀтʏᴘᴇ ҕᴇз ᴇҕᴀлᴀ остᴀвил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты когдᴀ сосᴀл ҕᴘосился нᴀ мой хʏй  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] дᴀ ᴇҕᴀло зᴀкᴘой тᴇлкᴀ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] кᴀчᴇствᴇнно тᴇҕᴇ ᴇҕᴀло сᴘᴇжʏ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕя тᴀк жᴇ пᴘоффᴇсионᴀльно кᴀк ᴘыҕʏ фʏгʏ пᴘиготовлю  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] свᴇᴘнʏл твою гʏсинʏю шᴇю  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] пᴘишᴇл чтоҕы тᴇҕя постᴀвить нᴀ колᴇни [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ᴇҕᴇм тʏшʏ твоᴇй мᴀтᴇᴘи  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ᴇҕᴇм тᴇҕя нᴀ покᴀз [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ᴇҕʏ твою мᴀть пʏҕлично  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] твоя мᴀть нᴇ хочᴇт жить и кинʏлᴀсь под колᴇсᴀ   [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] пᴘокоᴘмил твою сᴇмью говном  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]  чᴇᴘᴇз шлᴀнг тᴇҕᴇ говно в ᴘот пᴇᴘᴇкᴀчᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ᴇҕᴀл я тя ножом  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]  кинжᴀлом твою мᴀть ᴇҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>]  тᴇᴘпилʏ тя ᴇҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] пᴘизывᴀл твою мᴀть нᴀ свой хʏй онᴀ вᴇлᴀсь кᴘч  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] твоя мᴀть нᴀ пᴘиҕой моᴇго хʏя пᴘишлᴀ опять  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я тᴇҕᴇ гоᴘло выдᴇᴘнʏ  [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] кᴀтᴀной тя ᴘᴇзᴀл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ᴘᴇзᴀл тя ᴘыҕʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] дᴇлᴀй хᴀᴘᴀкиᴘи хʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты ʏпыᴘь ᴇҕᴀный [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ты сын пᴀнды котоᴘᴀя мой хʏй сосᴇт типо ҕᴀмҕʏк [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я типо твою мᴀть ᴇҕᴀл в хᴘᴀмᴇ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] я типо кᴀк сᴀмʏᴘᴀй тᴇҕᴇ хʏᴇм соннʏю ᴀᴘтᴇᴘию поᴘᴀзил [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] дыхᴀниᴇм восточного змᴇя тᴇҕя сжᴇг [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой стиль фʏндᴀмᴇнтᴀлᴇн для твоᴇго сʏщᴇствовᴀния [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой стиль ᴇҕᴇт модʏ вот ты и фᴀнᴀтᴇᴇшь [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] мой хʏй сосᴀть это ҕᴀзовый нᴀвык для твоᴇй сᴇмьи [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] в основᴇ смыслᴀ жизни сʏщᴇствовᴀния твоᴇй сᴇмьи это сосᴀть мой хʏй [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] восточными клинкᴀми тᴇҕя ᴘᴇжʏ [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] тᴀнто тᴇҕᴇ в гоᴘло зᴀсʏнʏл и нᴀ ₁₈₀ гᴘᴀдʏсов пᴇᴘᴇвᴇᴘнʏл [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] ҕᴇᴘи в ᴘᴀсчᴇт что я твою мᴀть ᴇҕᴀл зᴀ ᴇᴇ счᴇт [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] твою мᴀть ᴇҕᴀл до плᴀцᴇнты тᴇпᴇᴘь ты мнᴇ выплᴀчивᴀᴇшь пᴘоцᴇнты [<emoji document_id=5341427217152880394>🚬</emoji>]"
             , "[<emoji document_id=5341427217152880394>🚬</emoji>] вскᴘыл тᴇҕᴇ вᴇны своим кᴀтᴀнохʏᴇм [<emoji document_id=5341427217152880394>🚬</emoji>]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl2))
            await sleep(0.1)
            await sleep(time)

    async def абсолютcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Аδᥴ᧐᧘юᴛ ɜᥲκ᧐нчᥙ᧘ ʙыᴦ᧐няᴛь ᥴынκ᧐ʙ δ᧘ядᥱᥔ <emoji document_id=5334626127849724802>🤡</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Аδᥴ᧐᧘юᴛ нᥲчᥲ᧘ ʙыᴦ᧐няᴛь ᥴынκ᧐ʙ δ᧘ядᥱᥔ <emoji document_id=5334626127849724802>🤡</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl3 = ["[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʀᴘɪsʜь ᴜɴɪᴢʜᴇɴɪʏᴀ ᴠ sᴛᴏʀᴏɴᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ sʟᴀʙʏᴊ sʏɴᴏᴋ sʜʟʏᴜʜɪ ɴᴀʜᴜᴊ ᴏᴛsʏᴜᴅᴀ ᴘᴏᴋᴀ sᴠᴏɪ ᴍᴏʟᴏᴄʜɴʏᴇ ᴢᴜʙᴋɪ ɴᴇ ᴏsᴛᴀᴠɪʟ ɴᴀ ᴍᴏᴇᴊ ɢʀᴏᴍᴀᴅɴᴏᴊ ʜᴜɪɴᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴠʏʀᴠᴜ ᴋɪsʜᴋɪ ɪ sᴋᴏʀᴍʟʏᴜ ɪʜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇ sʜʟʏᴜʜᴇ sᴠɪɴᴏᴘᴏᴅᴏʙɴᴏᴊʙᴜᴅᴇsʜь ᴛᴇʀᴘᴇᴛь sɪᴅᴇᴛь ᴢᴅᴇsь ᴋᴏʟʏᴍᴀɢᴀ ᴇʙᴀɴɴᴀʏᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙʏᴀ ᴄʜɪsᴛᴏ ᴢᴅᴇsь ʙᴜᴅᴇᴍ ᴘɪɴᴀᴛь ᴘᴇɢᴀsᴀ ᴇʙᴀɴᴏɢᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sʀᴀɴʏᴊ ᴛᴜᴘᴏʀʏʟʏᴊ sʏɴᴏᴋ sʜʟʏᴜʜɪ ᴍʏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴜᴛ ᴄʜɪsᴛᴏ ᴠᴢьᴇʙᴀsʜɪᴍ ᴘᴏᴅ ᴇᴇ ʙᴜᴅᴋᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀʀᴇᴢᴀʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь sʜʟʏᴜʜᴜ ʀᴀsᴏsɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀᴅʀᴇɴᴀʟɪɴ ᴋsᴛᴀᴛɪ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀʜᴜ ᴘᴏᴇʙᴇɴɪʟ ɴᴀ ᴘᴏʟɪɢᴏɴᴇ ᴠ 20 ᴠᴇᴋᴇ ᴠ ᴅᴠᴜʜ ʙᴀʀᴀᴋᴀʜ,ᴠᴏᴛ ᴛʏ ᴄʜᴇ ᴛᴀᴍ ʜᴏᴠᴀᴇsʜь sᴠᴏʏᴜ ᴍᴏʀᴅᴜ, ʙᴏᴍᴢʜɪʜᴀ ᴛsʏɢᴀɴsᴋᴏɢᴏ ʀᴏᴅᴀ  ᴘᴏᴅᴀʟьsʜᴇ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴀ 10 ᴍᴇᴛʀᴏᴠ,ᴛʏ ᴄʜᴇɢᴏ ᴛᴀᴋᴀʏᴀ ᴢᴀsʜᴜɢᴀɴɴᴀʏᴀ ʙʟʏᴀᴛь,ᴛᴇʙʏᴀ ᴄʜᴇ ᴏᴛᴇᴛs ᴠ ᴅᴇᴛsᴛᴠᴇ ɴᴇ ᴘʀᴀᴠɪʟьɴᴏ ɴᴀᴋᴀᴢʏᴠᴀʟ ɪ ᴘᴏᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ᴠsᴇ ᴛᴀᴋɪ sᴛᴏɪᴛ ᴘᴇʀᴇᴇʙᴀᴛь ᴢᴀᴅɴᴇᴘʀɪᴠᴏᴅɴᴏɢᴏ ᴏᴘᴜsᴄʜᴇɴᴛsᴀ ʙʟʏᴀ ᴀʜᴀᴀʜᴀʜʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ɴᴀᴠᴇʀɴᴏᴇ ᴅᴏɢᴀᴅʏᴠᴀᴇsʜьsʏᴀ ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ʏᴀ ᴠsᴛʀᴇᴛɪʟsʏᴀ s ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇᴊ ᴛᴏ ʏᴀ ʀᴇsʜɪʟ ᴘʀᴏᴋᴀᴛɪᴛь ᴇё ɴᴀ sᴠᴏᴇᴍ sᴛᴠᴏʟᴇ, ɪ ᴏɴᴀ ᴛᴇᴍ sᴀᴍʏᴍ ʀᴀsᴘʟᴀᴛɪʟᴀsь ᴍɴᴇ sᴠᴏᴇᴊ ɴᴀᴛᴜʀᴏᴊ ᴘʀᴏᴅᴀᴠ ᴇё ᴢᴀ ᴅᴇsʜᴍᴀᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ ᴏᴋᴜɴь ᴛʏ ʙʟʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʙᴜᴅᴇsʜь ᴛᴀᴍ ɪsᴋᴀᴛь ᴏᴘʀᴀᴠᴅᴀɴɪʏᴀ, ᴋᴀᴋ ʙʏ ʙʏsᴛʀᴇᴇ sᴍʏᴛьsʏᴀ ᴏᴛ ᴍᴏᴇᴊ ᴏɢʀᴏᴍɴᴏᴊ ᴢᴀʟᴜᴘʏ ɪ ᴍᴏɪʜ ᴜᴅᴀʀᴏᴠ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sʟʏsʜɪsʜь ᴍᴇɴʏᴀ ᴘᴇɢᴀs ᴇʙᴀɴɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʜᴇ ᴠɴᴀᴛᴜʀᴇ ᴜᴅᴜᴍᴀʟ ᴛʏᴀɢᴀᴛьsʏᴀ s ʟᴜᴄʜsʜɪᴍ, ɪʟɪ ᴄʜᴇ ʏᴀ ᴛᴇʙᴇ ᴛᴇʟᴋᴇ ᴋʀɪᴠᴏɴᴏsᴏᴊ ʙᴜᴅᴜ ᴇʙᴀʟьɴɪᴋ ᴠʏᴛʀᴀʜɪᴠᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʀᴇsʜɪʟsʏᴀ ᴘᴏᴋᴀᴢᴀᴛь sᴠᴏɪ ᴍɪᴢᴇʀɴʏᴇ ᴏʙъᴇᴍʏ ᴄʜᴜᴅɪsᴄʜᴇ ᴇʙᴀɴɴᴏᴇ ɴɪ ɴᴀ ᴄʜᴛᴏ ɴᴇsᴘᴏsᴏʙɴᴏᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴏᴊ ᴄʜʟᴇɴ sᴇᴊᴄʜᴀs ᴠʏᴘᴏʟᴢᴇᴛ ɪᴢ sʜᴛᴀɴᴏᴠ ɪ ᴠ ɴᴇᴜᴢɴᴀᴠᴀᴇᴍᴏᴍ ᴏʙʟɪᴋᴇ ᴘʀᴏsᴋᴏʟьᴢɴёᴛ ᴠ ʀᴏᴛɪᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇ ɪ ᴜsᴛʀᴏɪᴛ ᴛᴀᴍ ᴅᴇʙᴏsʜ s ᴜᴄʜᴀsᴛɪᴇᴍ ᴍᴏᴇᴊ ᴢᴀʟᴜᴘʏ ɴᴀ ᴇё ʏᴀᴢʏᴋᴇ ɪ ᴅᴇsɴᴀʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴇʙᴇᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠʏsᴏsɪ ʜᴜᴊ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏsɴᴇsʜ ᴄʜʟᴇɴʏᴀʀᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴏᴋʀᴏᴠᴀᴠʟᴇɴɴʏᴊ sʏɴᴜʟʏᴀ sʜʟʏᴜʜɪ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀʟ ᴛᴇʙʏᴀ ɴᴀ ᴋʀɪᴠᴏᴍ ᴇʙᴀʟьɴɪᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь, ᴄʜᴛᴏ ᴜᴅᴀʀɴᴀʏᴀ ᴠᴏʟɴᴀ ᴍᴏᴇɢᴏ ᴄʜʟᴇɴᴀ ᴇᴛᴏ ᴏʙʟᴀsᴛь ʀᴇᴢᴋᴏɢᴏ sᴢʜᴀᴛɪʏᴀ ᴠᴏᴢᴅᴜʜᴀ ɴᴀ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ, ʀᴀsᴘʀᴏsᴛʀᴀɴʏᴀʏᴜsᴄʜᴀʏᴀsʏᴀ ᴠᴏ ᴠsᴇ sᴛᴏʀᴏɴʏ ᴋʟɪᴛᴏʀᴀ ᴏᴛ ᴛsᴇɴᴛʀᴀ ᴠᴢʀʏᴠᴀ sᴏ sᴠᴇʀʜᴢᴠᴜᴋᴏᴠᴏᴊ sᴋᴏʀᴏsᴛьʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴇʙᴇᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ɴɪᴋᴛᴏ ɴᴇ ᴘᴏᴍᴏᴢʜᴇᴛ ᴅᴏᴘʀɪ ᴜᴢʜᴇ ᴇᴛᴏ sʏɴᴜʟʏᴀ sʜʟʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʜᴇ ᴛᴜᴛ ᴍᴇʟᴇsʜь ɴɪᴄʜᴛᴏᴢʜᴇsᴛᴠᴏ sʟᴀʙᴇᴊsʜᴇᴇ ᴋᴀᴋᴏᴊ ᴛᴇʙᴇ ᴛʀᴏʟʟɪɴɢ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜɪsᴛᴏ ᴢᴅᴇsь ᴛᴠᴏʏᴜ ᴍᴀᴛь sʜʟʏᴜʜᴜ ᴏᴘʀᴏᴋɪɴᴇᴍ ᴠ ᴋᴏʟᴏᴅᴇᴛs ɴᴀssᴀᴠ ᴛᴜᴅᴀ, ɪ ᴏsᴛᴀᴠɪᴠ ᴛᴀᴍ ᴏʙɪʟɪᴇ ᴘᴇᴛᴀʀᴅ ᴋᴏᴛᴏʀʏᴇ sᴏᴢᴅᴀᴅᴜᴛ ᴇᴊ sʜʀᴀᴍʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʙᴜᴅᴇsʜь ɪᴢ ᴋᴏᴢʜɪ ᴠᴏɴ ʟᴇᴢᴛь ᴅᴀʙʏ ʜᴏᴛь ᴋᴀᴋ-ᴛᴏ ᴄʜᴛᴏ-ʟɪʙᴏ ᴘʀᴏᴛɪᴠᴏᴘᴏsᴛᴀᴠɪᴛь ᴍᴏᴇᴊ ᴏɢʀᴏᴍɴᴏᴊ ᴍᴏʜɴᴀᴛᴏᴊ ᴢᴀʟᴜᴘᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ ᴠɴᴀᴛᴜʀᴇ ᴏᴘᴜsᴄʜᴇɴɴʏᴊ sʏɴ sʜʟʏᴜʜɪ ᴋᴏᴛᴏʀᴏᴍᴜ ʏᴀ ɴᴀ ᴋʟʏᴋ ᴅᴀᴍ ɪ ᴏɴ sᴏᴢɴᴀɴɪᴇ ᴘᴏᴛᴇʀʏᴀᴇᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ʀᴇᴀʟьɴᴏ ᴢᴅᴇsь ᴄʜɪsᴛᴏ ᴍᴀᴍᴀsʜᴜ ᴛᴠᴏʏᴜ ᴘʀɪᴅᴀᴠʟʏᴜ sᴠᴏɪᴍ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴏʜᴏᴅʏᴀɢᴀ ᴇʙᴜᴄʜᴀʏᴀ ᴏᴅɪɴ ʜᴜᴊ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜᴍʀɪ sʏɴ sʜʟʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sʏɴᴏᴄʜᴇᴋ sʜʟʏᴜʜɪ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀʜᴜᴊ ɴᴀʜᴜᴊ ᴏᴛsʏᴜᴅᴀ ᴘᴏᴋᴀ ᴛᴇʙʏᴀ sʟᴀʙᴀᴋᴀ ᴛᴜᴛ ɴᴇ ᴢᴀᴘɪɴᴀʟɪ, ᴏᴛsᴀsᴀʟ ᴛʏ ᴍɴᴇ ᴘᴏ ʙʟᴀɴᴛᴜ ʙʟʏᴀᴅɪɴᴀ ssᴀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʜᴇ ᴛᴜᴛ sɪᴅɪsʜь ɴᴀ ᴍᴏᴇᴍ ʜᴜᴇ ᴛᴜᴢʜɪsʜьsʏᴀ, ᴅᴀᴠᴀᴊ ᴍɪɢᴏᴍ sᴘᴏʟᴢᴀᴊ s ɴᴇɢᴏ ɪ ɴᴀᴘʀᴀᴠʟʏᴀᴊ sᴠᴏᴊ ʀᴏᴛ ɴᴀ ᴍᴏᴊ ᴄʜʟᴇɴ ᴘᴏᴅ ᴘʀɪᴛsᴇʟᴏᴍ, ᴀ ᴛᴏ ʏᴀ sᴇᴊᴄʜᴀs ᴠʏᴢᴏᴠᴜ ᴅᴜʜᴀ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ɪ ᴏɴ ʀᴀᴢᴅᴏʟʙɪᴛ ᴠsʏᴜ ᴛᴠᴏʏᴜ ʀᴏᴛᴏᴠᴜʏᴜ ᴘᴏʟᴏsᴛь ɴᴀ ᴋᴏᴛᴏʀᴜʏᴜ ᴍᴏᴊ ᴄʜʟᴇɴ ᴘᴏsᴛɪɢɴᴇᴛ ᴠ ᴀᴛᴀᴋᴜ ᴜᴇʙᴏᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏʟᴜᴄʜᴀᴛь ᴠ sᴠᴏᴇ ɢᴀʟɪᴍᴏᴇ ᴇʙᴀʟᴏ ᴏʙɪʟɪᴇ ᴢᴀʟᴜᴘ ᴇʙᴜᴄʜɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘʀᴏᴛɪsɴᴜ ᴛᴇʙᴇ ᴠ sᴏsᴀʟɪsᴄʜᴇ ᴏʙɪʟɪᴇ ᴋɪɴᴢʜᴀʟᴏᴠ ɴᴀʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏʟɴᴏsᴛьʏᴜ ɪ ɴɪᴄʜᴇɢᴏ ᴢʜɪᴠᴏɢᴏ ᴏᴛ ᴛᴇʙʏᴀ sᴄʜᴇɢʟᴀ ᴢᴅᴇsь ɴᴇ ᴏsᴛᴀɴᴇᴛsʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
" [ <emoji document_id=5334626127849724802>🤡</emoji> ]ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏsᴠᴇᴢʜᴀʟ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜᴇᴍ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀᴊᴛsᴀ ɴᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ʀᴏᴛɪᴋ ᴛᴇʙʏᴀ ɪᴍᴇʏᴜ sʜʟʏᴜsʜᴋᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ʀᴏᴛᴀɴ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴇʙᴀʟ ᴛᴇʙʏᴀ ɴᴀ sɪʟᴇ ᴠᴏʟɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴘᴀᴛʀʏᴀsɴᴏ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜ ᴛʏ ᴍɴᴇ ᴋᴀᴋ ɴᴀᴅᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴛᴏ ᴘᴏ ᴠsᴇᴍ sᴛᴀᴛьʏᴀᴍ sʜʟʏᴜʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍɴᴇ sᴏsᴇsʜь ᴅᴜʀᴀ ᴇʙᴀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ sᴏsᴀʟᴀ ᴍɴᴇ ɢʀᴜsɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜь s ᴘʀᴇsᴛɪᴢʜᴀᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠᴇʟɪᴋᴀʟᴇᴘɴᴀ sᴀsᴇsʜь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴀ sᴏsᴇᴛ ᴏʜᴜᴇɴɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜ ʏᴀᴋ ʙᴇᴢᴏʙʟᴀᴄʜɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɢɪᴅʀᴏᴛsᴇғᴀʟ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙʟʏᴀ ʙᴜᴅᴜ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏ ᴇʙʟᴜ sʟᴏᴠɪ ʜᴜᴊʟᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀssᴀʟɪ ᴛᴇʙᴇ ɴᴀ ᴘᴀᴛʟʏ ʜᴜᴊʟᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇʜ ᴘᴇsᴛᴜ ᴛᴠᴏʏᴜ ʜᴜᴇᴍ ᴢᴀᴅᴇʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴋᴏʟьᴢᴋᴀ ᴛʏᴀ ᴇʙᴜ ᴛᴀᴋ ᴋᴀᴋ ᴛʏ ᴏᴛsᴏsᴇɴᴀʏᴀ ᴛᴇʟᴏᴄʜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏɪᴍ ᴢʜᴇ ʏᴀᴢʏᴋᴏᴍ ʜᴜᴊ sᴠᴏᴊ ᴠʏᴛᴇʀᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀsᴏsɪ ᴍɴᴇ ᴛᴜᴛ ʜᴜᴊ sʏɴ ᴛʏ ᴇʙᴀɴᴏᴊ sʜᴀʟᴀᴠʏ ᴋᴏᴛᴏʀᴏɢᴏ ʏᴀ ᴠ ᴅᴀɴɴᴏᴊ ᴋᴏɴғᴇʀᴇɴᴛsɪɪ ᴠʏᴇʙᴜ sᴏɴɴᴀʏᴀ ᴘʀɪɴᴛsᴇssᴀ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ ᴠ ᴜʟɪᴄʜɴᴏᴍ ᴛᴜᴀʟᴇᴛᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴍᴀɴʏᴜ ᴛᴠᴏʏᴜ ᴇʙᴀʟ sʏɴᴏᴋ sʜʟʏᴜʜɪ ʜᴇ-ʜᴇ ɴᴇ ᴘᴏᴠᴇʀɪsʜь ᴋᴀᴋ ᴇʙᴀʟ ᴅᴀᴢʜᴇ![ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴜ ᴀᴍғɪᴛᴇᴀᴛʀᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴀsᴀʟᴀ ᴍɴᴇ ᴅɪᴋᴏᴠɪɴᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠ sʜᴋᴏʟьɴᴏᴍ ᴛᴜᴀʟᴇᴛᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴘᴏsᴀsʏᴠᴏᴇsʜ ᴋᴀᴋ ɴᴇᴘʀɪsᴛᴏᴊɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴀ ᴘᴏᴅ ᴍᴏɪᴍ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴍᴀɴʏᴜ ᴛᴠᴏʏᴜ ᴇʙᴀʟ sʏɴᴏᴋ sʜʟʏᴜʜɪ ʜᴇ-ʜᴇ ɴᴇ ᴘᴏᴠᴇʀɪsʜь ᴋᴀᴋ ᴇʙᴀʟ ᴅᴀᴢʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʏᴀ sᴘᴜsᴛɪʟ ᴠ ɴᴇᴇ ᴋᴀᴍsʜᴏᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏsᴇsʜ ᴋᴀᴋ ᴢᴀʜᴏʟᴜsᴛɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢᴀᴘɪɴᴀʟ ʜᴜᴇᴍ ᴠ ᴋʟɪᴛᴏʀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴇʀᴇʜᴜʏᴀʀɪᴍ ᴛᴇʙᴇ ᴇʙʟɪsᴄʜᴇ ʟᴏsʜᴀʀᴀ ᴇʙᴜᴄʜᴀʏᴀ ᴅᴀᴢʜᴇ ɴᴇ ᴅᴜᴍᴀᴊ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴇᴘʟᴇᴛᴋᴀ ᴍᴀʟᴏʀᴀᴢᴜᴍɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛʏ sᴏsᴀʟᴀ ᴍɴᴇ ᴅᴏᴄʜᴜʀᴋᴀ sᴠɪɴᴏᴇʙʟᴏᴊ ғᴇʀᴍᴇʀsʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴀsᴇsʜь ʏᴀᴋ ᴠᴏᴇɴɴᴏᴘʟᴇɴɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴜ ʟᴇsɴᴏᴊ ᴏᴘᴜsʜᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴛɪᴘᴏ ᴋᴀᴋ ᴘᴇsʜᴋᴀ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀʟ ᴅᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴋᴏᴛᴏᴢʜɪʀɴʏᴊ ᴋʀɪᴠᴏᴋʀʏʟ ʜᴜᴊ sʟᴏᴠɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏsᴏsɪ ᴍᴏɪ ʏᴀᴊᴛsᴀ sᴄʜᴇɴᴏᴋ ᴛʏ sᴜᴋ)[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ᴍɪʟғᴜ ɴᴀ sᴇᴋs ʀᴀsᴋʀᴜᴛɪʟ ᴘʀɪᴋɪɴь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴄʜᴇʀᴇᴢ ᴅᴜsʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀᴛʏᴀɢɪᴠᴀʟ ɴᴀ sᴠᴏᴊ ʜᴜᴊ ᴘᴏᴋᴀ ɴᴇ ᴢᴀᴍᴇᴛɪʟ ᴄʜᴛᴏ ᴏɴᴀ ᴜᴢʜᴇ ᴛʀᴜᴘ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜ ᴋᴀᴋᴛᴀ ᴍᴜᴄʜɪᴛᴇʟьɴᴏ sʏɴᴏᴄʜᴇᴋ ʙʟʏᴀᴅᴏʀᴜᴋᴏᴊ ᴋᴜʀᴛɪᴢᴀɴᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɢɪᴅʀᴏᴛsᴇғᴀʟ ᴛʏ ᴛᴀᴋ ᴄʜᴛᴏ ᴛʏ ᴜᴢʜᴇ ᴏᴛsᴏsɪ ᴍɴᴇ ᴛᴜᴛ ᴘᴇᴅɪᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴏsᴇsʜ ʏᴀᴋ ɪɢʀᴀʟьɴʏᴇ sʜʟʏᴜsʜᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʏᴀ sᴘᴜsᴛɪʟ ᴠ ɴᴇᴇ ᴋᴀᴍsʜᴏᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴜʟᴀᴠᴀ sᴀsᴇsʜ ᴋᴀᴋ ʟᴀsʜᴏᴋ ʙʟᴀɢᴏᴜʜᴀɴɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʟᴇɢᴀʟьɴᴀ ᴛʏᴀ ᴇʙᴜ ɴᴀ ɢʀᴀɴɪᴛsᴇ ᴘᴇʀᴇᴅ ᴠᴏᴇɴɴʏᴍɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴍ ᴛᴇʙʏᴀ ᴛᴏʀᴍᴏsʜɪʟ sʜʟʏᴜʜᴀ ᴇʙᴜᴄʜᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴍ ᴛʏᴀ ᴋᴀɴᴛᴜᴢᴇʟ sʏɴ ᴇʙᴀɴᴏᴊ sʜᴀʟᴀᴠʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴇʀᴇᴠᴇᴢ ᴛʏᴀ ʜᴜᴇᴍ ᴄʜᴇʀᴇᴢ ʀᴇᴋᴜ ᴛᴀᴋ ᴄʜᴛᴏ ᴛᴇʀᴘɪ sʏɴ sʜʟʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜ ᴋᴀᴋ ʙʟᴀɢᴏʀᴏᴅɴᴇᴊsʜɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʏᴀ sᴘᴜsᴛɪʟ ᴠ ɴᴇᴇ ᴋᴀᴍsʜᴏᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏʙ sᴠᴏᴊ ʜᴜᴊ ᴜᴅᴀʀʏᴀʟ ᴘʀɪ ᴋᴀᴢʜᴅᴏᴊ ᴠsᴛʀᴇᴄʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴘᴀsᴀsʏᴠᴏᴇsʜ ᴋᴀᴋ ɢᴜᴍᴀɴɪsᴛɪᴄʜᴇsᴋɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴍ ᴛʏᴀ ᴋᴀᴄʜᴀʟ sʏɴᴋᴀ sʜʟʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴇs ᴇʙᴀɴʏᴊ ᴛʏ ɴᴀʜᴜᴊ ᴏᴛsᴏsᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍʏ ᴅᴏᴍᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ ʙᴇᴢ ɴᴀʟᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴍ ᴛʏᴀ ᴠʏᴠᴇᴢ ɪᴢ sᴇʙʏᴀ ᴛᴀᴋ ᴄʜᴛᴏ ᴘʀɪsᴛᴜᴘᴀᴊ ᴋ ᴏᴛsᴏsᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏɪᴍᴇʟ ᴛᴇʙʏᴀ ᴘᴏᴅ ғᴏɴᴋ sʜʟʏᴜsʜᴋᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴘɪɴᴀʏᴜ ᴢᴀʟᴜᴘᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴊ ʟᴏᴠɪ sʏɴᴏᴋ sʜʟʏᴜʜɪ sᴛʀᴀɴɴᴏɢᴏ sᴇᴍᴇᴊsᴛᴠᴀ ᴏʟɪɢᴏғʀᴇɴᴏᴠ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴀsᴇsʜ ʏᴀᴋ ɢᴀʟᴀᴠᴀsᴛᴇɢ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ ᴏɴᴀ sᴛᴏɴɪᴛ ᴋᴀᴋ sᴠɪɴᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴀ ɴᴀ ʜᴜʏᴜ sɪᴅɪɪᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛsᴏsᴇsʜь ᴍɴᴇ ʜᴜᴇsᴏsᴋᴀ ᴇʙᴜᴄʜᴀʏᴀ ɴᴇ ᴘʏᴛᴀᴊsʏᴀ ᴅᴀᴢʜᴇ sᴏᴘʀᴏᴛɪᴠʟᴇɴɪᴇ ᴅᴀᴠᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴜ ᴘᴀʀᴋᴏᴠᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴛʏᴀɴᴜʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴀᴋ sᴛʀᴇʟᴜ ɴᴀ ᴛᴇᴛᴇᴠᴜ ɴᴀʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ɴᴀ ʀᴇʟьsᴀʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴍ ᴛʏᴀ ᴠ ᴋᴏsᴍᴀs ᴏᴛᴘʀᴀᴠᴇʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴊᴛsᴀ ᴍᴏᴇɢᴏ sᴏsɴɪ ʟᴜᴄʜsʜᴇ ʙʟʏᴀᴅɪɴᴀ ᴋᴏɴᴄʜᴇɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏᴊᴍᴜ sᴘᴇʀᴍʏ ᴠ ᴛᴇʙʏᴀ ᴢᴀᴘᴜsᴛɪʟ ʜᴜᴊʟᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴘᴏsᴀsʏᴠᴏᴇsʜ ᴋᴀᴋ ᴋᴀʟᴜᴢʜsᴋɪᴊ ᴘᴇᴅɪᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠ ɢʀᴏʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏssᴀʟɪ ᴛᴇʙʏᴀ ʟᴏsʜᴀʀᴀ ssᴀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴠ ʀᴏᴛ ᴛᴇ sᴛsᴜ ᴘᴇᴅᴇᴋ ɢᴏʀᴏᴅsᴋᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴀsᴇsʜ ᴋᴀᴋ ʙᴇsᴘʀᴇᴋᴏsʟᴏᴠɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏssᴀʟ ᴛᴇʙʏᴀ s ᴋʀʏsʜɪ ᴛᴠᴏᴇɢᴏ ᴅᴏᴍᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘɪᴢᴅᴀᴘёʀᴋᴀ ᴇʙᴀɴᴀʏᴀ ʏᴀ ᴢʜᴇ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ᴠ ʀᴏᴛ ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛʏ ᴍᴏɪ ʏᴀᴊᴛsᴀ ʜᴀᴠᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴠ ʀᴏᴛ ᴛᴇ sᴛsᴜ ᴘᴇᴅᴇᴋ ᴀʙʜᴀᴢsᴋɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ sᴏsᴇsʜ ᴍɴᴇ ᴠsʏᴀᴄʜᴇsᴋᴇ ᴋᴏɢᴅᴀ ᴇsᴛь ᴠᴏᴢᴍᴏᴢʜɴᴏsᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴛь ᴛʏ ʙᴀʀsᴜᴋ ʏᴀ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ ᴇʙᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴀɴsᴇsʜ ᴋᴀᴋ ɴᴇᴅᴇsʜᴇᴠʏᴊ sʏɴ sʜʟʏᴜʜɪ ʙʟʏᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ sᴀsᴇsʜ ᴋᴀᴋ ᴛᴏ ɴᴇ ᴘʀᴀᴠɪʟьɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴅɪᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏsᴇsʜь ᴘᴏ ᴠsᴇᴍ ᴘʀᴀᴠɪʟᴀᴍ ᴛʏ ᴘʀʏᴀᴍ ᴍɪɴᴇᴛᴄʜɪᴋ ᴘᴏʟᴜᴄʜᴀᴇᴛsʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴜʙʟɪᴄʜɴᴀ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴇʀᴇʜᴜʏᴀʀɪᴍ ᴛᴇʙᴇ ᴇʙʟɪsᴄʜᴇ ʟᴏsʜᴀʀᴀ ᴇʙᴜᴄʜᴀʏᴀ ᴅᴀᴢʜᴇ ɴᴇ ᴅᴜᴍᴀᴊ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴇᴘʟᴇᴛᴋᴀ ᴍᴀʟᴏʀᴀᴢᴜᴍɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ʀᴏᴛᴀɴ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠɴᴀᴛᴜʀᴇ ɴᴀ sᴠᴏᴊ ʜᴜᴊ ᴘᴏ sᴀᴢʜᴜ, ʙᴜᴅᴇᴛ ᴋᴀᴋ ᴇʙᴀɴʏᴊ ᴄʜᴀsᴏᴠᴏᴊ sᴜᴋᴀ ᴠ ʙɪɴᴏᴋʟь ᴢʏʀɪᴛь ɪsᴋᴀᴛь ᴍᴏʏᴜ ᴢᴀʟᴜᴘᴜ ᴋʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴍᴏʀᴀʟьɴᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴇsᴄʜᴇ ᴍᴏʟᴏᴅᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋʟʏᴜᴋᴠᴏsʀᴀɴɪsᴄʜᴇ sᴠᴏᴇ ᴢᴀᴋʀᴏᴊ ᴍʀᴀᴢɪɴɪɴᴀ ᴇʙᴀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴜ ᴠᴇᴊᴘ-sʜᴏᴘᴀᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴘɪɴᴀʏᴜ ʜᴜᴇᴍ ᴋᴀᴋ ɴᴀᴅᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ sᴘɪᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴘᴀsᴀsʏᴠᴏᴇsʜ ᴋᴀᴋ ᴠᴇʟɪᴄʜᴀᴠʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ᴘᴇᴄʜᴇɴᴋᴜ ᴛᴇ sᴛsᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴛᴀᴘᴏᴄʜᴋᴀᴍɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴅ ᴋʀᴏᴠᴀᴛᴋᴏᴊ ᴛᴇʙʏᴀ ɪᴍᴇʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴀsᴇsʜ ᴛʏ ᴍɴᴇ ʜᴜᴊɴʏᴀ ʙᴇᴢᴘʀɪᴢᴏʀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴋᴀᴋ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴜ ᴠᴏᴇɴɴᴏᴊ ᴄʜᴀsᴛɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ʀᴏᴛɪᴋ ᴛᴇʙʏᴀ ɪᴍᴇʏᴜ sʜʟʏᴜsʜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏʟ ᴏᴅᴇʏᴀʟᴏᴍ ᴛᴇʙʏᴀ ᴛʀᴀʜᴀʟ ᴛᴀᴊɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ᴍɴᴇ ʏᴀ sᴘᴜsᴛɪʟ ᴠ ɴᴇᴇ ᴋᴀᴍsʜᴏᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴇʙᴜ ᴠ ᴋʟɪᴛᴏʀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ʏᴀ ᴋᴀᴋ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʏᴀᴊᴛsᴀᴍɪ ᴘʀɪᴅᴀᴠɪʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ sᴘɪᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴛᴇʀᴠʏᴀᴛɴɪᴋ ᴇʙᴀɴʏᴊ ᴛᴇʙᴇ ᴋʟʏᴜᴠ sʟᴏᴍᴀʟ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ sᴘɪᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ᴠᴀʟьᴇʀᴇ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴀ ᴘᴏᴅ ᴍᴏɪᴍ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀsᴏsɪ ʜᴜᴊᴛsᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ ᴠ ʀᴏᴛ ᴛᴇ sᴛsᴜ ᴘᴇᴅᴇᴋ ᴀʙʜᴀᴢsᴋɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴜ ᴋᴀᴘᴏᴛᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ʙʟʏᴀᴅᴜʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏssᴀʟɪ ᴛᴇʙʏᴀ sᴄʜᴇɴᴏᴋ ᴇʙᴀɴʏᴊ ʜᴇ-ʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴛɪᴘᴏ ᴋᴀᴋ ᴘᴇsʜᴋᴀ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀʟ ᴅᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ sᴀsᴇsʜ ᴋᴀᴋ ᴛᴏ ɴᴇ ᴘʀᴀᴠɪʟьɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴀᴍɪɴᴜᴛɴᴀ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍɪʀɴᴀ ᴛʏᴀ ᴀʙᴀsᴛsᴀʟ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴀsᴀʟᴀ ᴛʏ ʏᴀᴋ ᴠʟᴀsᴛɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴢᴀᴘɪɴᴀʟ ʜᴜᴇᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏᴍɴʏᴜ ᴇʙᴀʟ ᴛᴇʙʏᴀ ʙᴇᴢᴘʀɪʀʏᴠɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏsᴏsɪ ᴍɴᴇ, ʜᴜᴇsᴏsᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴇ sᴏsᴇsʜ ʏᴀᴋ ɴᴇᴘʀᴏʙɪᴠᴀᴇᴍʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ᴛᴀᴋ ᴋᴀᴋ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛᴇʙᴇ ɴᴀᴅᴏ ᴠʏʙʀᴀᴛь ʜᴜᴊ ᴛᴇ sᴏsᴀᴛь ɪʟɪ ᴋᴀᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴛᴜᴛ ᴍᴀᴍᴀsʜᴋᴜ ᴘᴏᴇʙᴜ ᴋʀɪɴᴢʜᴏᴠʏᴊ ᴘᴏᴛᴇsʜɴʏᴊ ᴘʀᴇᴅsᴛᴀᴠɪᴛᴇʟь ᴋᴏᴍᴘᴀɴɪɪ ᴏᴛsᴏsᴀ ᴋᴏᴛᴏʀʏᴊ ᴍɴᴇ ᴛᴜᴛ sᴄʜᴀs ᴛᴇʀᴘᴇᴢʜь sᴠᴏᴊ ᴘᴏᴋᴀᴢʜᴇᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ sʏɴᴏᴄʜᴇᴋ ᴜᴍᴀʟɪsʜᴇɴɴᴏᴊ sʟᴀʙᴏᴜᴍɴᴏᴊ sᴠɪɴᴏᴘᴀsᴋɪ ᴛᴇʀᴘɪ ᴛᴜᴛ ᴍᴏɪ ᴏʙъᴇᴍʏ ɴᴇᴅᴇᴇsᴘᴏsᴏʙɴᴀʏᴀ ᴛᴜsʜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ ᴢɴᴀᴇsʜь ᴄʜᴛᴏ ᴛᴜᴛ ᴛʏ ᴘʀᴏsᴛᴏ ᴛᴇʟᴏᴄʜᴋᴀ ᴘʀɪsʜᴇᴅsʜᴀʏᴀ ᴋᴏ ᴍɴᴇ ᴅᴏᴍᴏᴊ sᴄʜᴀ ᴅᴠᴏᴊɴᴏᴊ ᴘᴏʀᴛsɪᴇᴊ ʟᴇsᴄʜᴇᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴇʟᴀʏᴀ ᴋᴏɴᴄʜь sᴇᴊᴄʜᴀs ᴘʀᴏɴᴢᴀᴇᴛ ᴘʀʏsᴄʜᴀᴠᴏᴇ ᴇʙʟɪsᴄʜᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴀ ᴛʏ ɴᴀ ᴇᴛᴏ sᴇᴊᴄʜᴀs ᴛᴀᴋ ᴘᴏʟᴀɢᴀʏᴜ sᴍᴏᴛʀɪsʜь ɪ ᴛᴇʀᴘɪsʜь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴛᴜᴛ ᴍᴀᴍᴀsʜᴋᴜ ᴇʙᴀʟ sʏɴᴏᴄʜᴇᴋ sʜʟʏᴜʜɪ ᴛʏ ᴢʜᴇ ᴢɴᴀᴇsʜь ᴄʜᴛᴏ ɴɪ ɴᴀ ᴄʜᴛᴏ ɴᴇsᴘᴏsᴏsʙɴᴀʏᴀ ᴠᴘʀɪɴᴛsɪᴘᴇ ᴘʀᴏᴛɪᴠ ᴍᴇɴʏᴀ ᴛᴇʟᴏᴄʜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛᴜᴛ ᴛʏ ᴘʀᴏsᴛᴏ ᴛᴇʀᴘᴇᴢʜɴɪᴛsᴀ ᴇʙᴀɴᴀʏᴀ ᴢᴀsᴏsɪ ᴍᴏʏᴜ ᴠᴀɴʏᴜᴄʜʏᴜʏᴜ ᴄʜʟᴇɴʏᴀʀᴜ sʏɴᴏᴋ sʜʟʏᴜʜɪ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴛᴜᴛ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴇɢᴀsᴜ ᴇʙᴀɴᴏᴍᴜ ᴛʏ ᴢʜᴇ ᴠᴘʀɪɴᴛsɪᴘᴇ ɴᴇ ᴘʀᴏᴛɪᴠ ᴄʜᴛᴏ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ʀᴏᴅᴏsʟᴏᴠɴᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜʟᴇɴᴏᴍ ᴘʀᴏɴᴢᴀʟ ᴛᴇʙᴇ ʜʀʏᴜᴋᴀʟᴏ ᴛᴠᴏᴇ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴋᴀ ʀᴀʙᴏᴛᴀʟᴀ ɴᴀ ᴍᴇɴʏᴀ ᴄʜᴛᴏʙʏ ᴘʀᴏᴋᴏʀᴍɪᴛь ᴛᴀᴋᴏɢᴏ ᴢʜɪʀᴅʏᴀʏᴀ ᴋᴀᴋ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʟᴏ sʏɴ ᴇʙᴀɴᴏᴊ ᴀᴍᴇᴢʜɴᴏᴊ ᴘʀᴏғᴜʀʏ ᴛʏ ᴛᴀᴋ ɪ ʙᴜᴅᴇsʜь sᴍᴇʏᴀᴛьsʏᴀ ᴛsᴇʟʏᴊ ᴅᴇɴь ᴅᴀʙʏ ɪᴢʙᴇᴢʜᴀᴛь ᴘʀᴏʙʟᴇᴍ sᴏ sᴠᴏɪᴍ ᴇʙᴀʟᴏᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴇʙᴀʟᴏ ᴛᴇʙᴇ ɴᴀsʀᴀʟ ᴛʏ sʜʟʏᴜsʜɪᴊ sʏɴ ᴘᴏᴋᴀ ᴛʏ ᴘʏᴛᴀᴇsʜьsʏᴀ ɴᴀᴘɪsᴀᴛь ᴍɴᴇ sᴠᴏɪ sʜᴀʙʟʏ ᴛᴜᴛᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴜᴛ ɴᴀʏᴀʀɪᴠᴀᴊ ʜᴜʏᴀᴋᴜ ᴍɴᴇ ɪ ᴠ ᴘᴏɢᴜᴛᴀʜ ᴘʏᴛᴀᴇᴛsʏᴀ ᴇᴛᴏᴛ ᴏʟɪɢᴏғʀᴇɴ ᴜʙᴇᴢʜᴀʟ ᴏᴛ ᴍᴇɴʏᴀ ᴘᴏ ʀᴀᴢɴʏᴍ ɴᴀᴘʀᴀᴠʟᴇɴɪʏᴀᴍ ᴍᴏᴇɢᴏ ᴘʀᴏᴇᴢᴢʜᴀʏᴜsᴄʜᴇɢᴏ ᴍɪᴍᴏ ᴛᴠᴏᴇɢᴏ ʀᴛᴀ ᴘᴇɴɪsᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴛᴜᴛ ᴄʜᴀᴄ ɴᴇ ᴨᴏᴋᴀᴢʜɪ ᴧᴏʜ ᴇʙᴀɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴋᴀᴋ ᴄɴɪʍᴀᴧᴄʏᴀ ᴄ ᴛʙᴏᴇᴊ ʍᴀʍᴏᴊ ɴᴀ ᴨᴏᴩɴʜᴀʙᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜᴇ ᴛʏ ᴛᴀᴋᴏᴊ ᴄᴧᴀʙᴀᴋ ᴄʍᴇᴧᴏᴄᴛɪ ɴᴀʙᴩᴀᴧᴄʏᴀ ʏᴀ ʙɪᴢʜᴜ, ɴᴜ ᴛʏ ᴄᴏᴄɪ ᴧᴏʜ ʙᴇɜᴅᴀᴩɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ɴᴇᴜᴄʜ ᴇʙᴀɴʏᴊ ᴨᴩᴇᴋᴩᴀᴛɪ ʍɴᴇ ᴛᴜᴛ ɴʏᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ᴨᴇɯᴋᴀᴩᴇɴᴋᴀ ᴇʙᴀɴᴏᴦᴏ, ᴨᴏɪʍᴇᴧ ᴛʏᴀ ɴᴀ ᴨᴇᴩᴇᴋᴩᴇᴄᴛᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄᴧᴀʙᴀᴋ ᴇʙᴀɴʏᴊ ɪ ɴᴇ ʙᴏᴧᴇᴇ ᴄᴏᴄɪᴩᴜᴊ ʍᴏᴊ ᴄʜᴧᴇɴᴀᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ɪ ᴛᴇᴧᴋᴀ ɴᴀ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ɴᴀ ʙᴄᴇʜ ᴨᴧᴀɴᴇᴛᴀʜ ᴦᴀᴧᴀᴋᴛɪᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴇᴢʜᴦᴀᴧᴀᴋᴛɪᴄʜᴇᴄᴋɪ ᴛʏᴀ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴊ ᴄᴏᴄᴇɯь ʍᴏᴊ ᴋᴀᴋ ᴄᴧᴏɴʏᴀᴩᴀ ᴇʙᴀɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴋᴀᴄʜᴇɯь ɴᴀ ʍᴏᴇʍ ʜᴜᴇ ᴋᴀᴋ ᴧʏᴀᴦᴜɯᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛᴄᴏᴄᴇɯ ᴨᴏᴅ ʍᴜɜᴏɴ ʙ ᴛᴛ ɴᴇᴜᴄʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀɜʙɪʙᴀʏᴜ ʙᴀɯɪ ɴᴇᴋᴄʜᴇʍɴʏᴇ ᴦᴏᴧᴏʙʏ ᴄʜᴧᴇɴᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜʙɪᴧ ᴛʏᴀ ᴨᴏ ᴜᴋᴩᴀɪɴᴄᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴧᴏʜ ᴇʙᴀɴʏᴊ ɪ ɴᴇ ʙᴏᴧᴇᴇ ʜᴀ ᴄᴏᴄᴇɯ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀɴɪʍᴇɯɴᴀ ᴛʏᴀ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴅᴀ ɴᴜ ᴛʏ ɪ ᴛᴇᴧᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴄᴏᴄᴇɯь ʍᴏᴊ ᴄʜᴧᴇɴ ᴏᴛʍᴇɴɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀɴʏᴊ ᴧᴏʜ ʏᴀ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴜʙьʏᴜ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴏᴢʜᴢʜᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʙᴏᴇᴊ sᴘᴇʀᴍᴏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧɪ ᴛʏᴀ ʙᴄᴇᴊ ᴋᴀʍᴨᴀɯᴋᴏᴊ ᴄᴧᴀʙᴀᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴦɴɪᴧᴏʍ ᴄᴛᴜᴧᴇ ᴄᴏᴄᴇɯ ʙɪᴄʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴨɪɜᴅᴏᴊ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄᴨɪᴄʜᴋɪ ᴨᴏᴅᴢʜɪᴦᴀᴧ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ 8 ʍᴀᴩᴛᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʜᴜᴊ ᴨᴏᴅᴀᴩɪᴧ ᴄʙᴏᴊ ʜᴇʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪᴅɪ ᴄʏᴜᴅᴀ ᴛʏ ᴄᴧᴀʙᴏʜᴀᴩᴀᴋᴛᴇᴩɴʏᴊ ʜᴜᴇᴄᴏᴄ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ᴄʜᴇᴩᴇɜ ᴛᴇᴧᴇɸᴏɴ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀʍᴜᴛɪᴧ ᴄ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩьʏᴜ ϶ᴛᴏ ᴜʙᴇᴩ ᴄᴇᴋᴄ ʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ᴨᴇɯᴋᴀᴩᴇɴᴋᴀ ᴇʙᴀɴᴏᴦᴏ, ᴨᴏɪʍᴇᴧ ᴛʏᴀ ɴᴀ ᴨᴇᴩᴇᴋᴩᴇᴄᴛᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄᴧᴀʙᴀᴋ ᴇʙᴀɴʏᴊ ɪ ɴᴇ ʙᴏᴧᴇᴇ ᴄᴏᴄɪᴩᴜᴊ ʍᴏᴊ ᴄʜᴧᴇɴᴀᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ɪ ᴛᴇᴧᴋᴀ ɴᴀ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ɴᴀ ʙᴄᴇʜ ᴨᴧᴀɴᴇᴛᴀʜ ᴦᴀᴧᴀᴋᴛɪᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴇᴢʜᴦᴀᴧᴀᴋᴛɪᴄʜᴇᴄᴋɪ ᴛʏᴀ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴊ ᴄᴏᴄᴇɯь ʍᴏᴊ ᴋᴀᴋ ᴄᴧᴏɴʏᴀᴩᴀ ᴇʙᴀɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴋᴀᴄʜᴇɯь ɴᴀ ʍᴏᴇʍ ʜᴜᴇ ᴋᴀᴋ ᴧʏᴀᴦᴜɯᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛᴄᴏᴄᴇɯ ᴨᴏᴅ ʍᴜɜᴏɴ ʙ ᴛᴛ ɴᴇᴜᴄʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀɜʙɪʙᴀʏᴜ ʙᴀɯɪ ɴᴇᴋᴄʜᴇʍɴʏᴇ ᴦᴏᴧᴏʙʏ ᴄʜᴧᴇɴᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜʙɪᴧ ᴛʏᴀ ᴨᴏ ᴜᴋᴩᴀɪɴᴄᴋɪ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴧᴏʜ ᴇʙᴀɴʏᴊ ɪ ɴᴇ ʙᴏᴧᴇᴇ ʜᴀ ᴄᴏᴄᴇɯ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀɴɪʍᴇɯɴᴀ ᴛʏᴀ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴅᴀ ɴᴜ ᴛʏ ɪ ᴛᴇᴧᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴄᴏᴄᴇɯь ʍᴏᴊ ᴄʜᴧᴇɴ ᴏᴛʍᴇɴɴᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀɴʏᴊ ᴧᴏʜ ʏᴀ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴜʙьʏᴜ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴏᴢʜᴢʜᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʙᴏᴇᴊ sᴘᴇʀᴍᴏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧɪ ᴛʏᴀ ʙᴄᴇᴊ ᴋᴀʍᴨᴀɯᴋᴏᴊ ᴄᴧᴀʙᴀᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴦɴɪᴧᴏʍ ᴄᴛᴜᴧᴇ ᴄᴏᴄᴇɯ ʙɪᴄʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
  "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴨɪɜᴅᴏᴊ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄᴨɪᴄʜᴋɪ ᴨᴏᴅᴢʜɪᴦᴀᴧ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ 8 ʍᴀᴩᴛᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʜᴜᴊ ᴨᴏᴅᴀᴩɪᴧ ᴄʙᴏᴊ ʜᴇʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪᴅɪ ᴄʏᴜᴅᴀ ᴛʏ ᴄᴧᴀʙᴏʜᴀᴩᴀᴋᴛᴇᴩɴʏᴊ ʜᴜᴇᴄᴏᴄ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ᴄʜᴇᴩᴇɜ ᴛᴇᴧᴇɸᴏɴ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀʍᴜᴛɪᴧ ᴄ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩьʏᴜ ϶ᴛᴏ ᴜʙᴇᴩ ᴄᴇᴋᴄ ʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪʍᴇᴧ ᴛᴇʙʏᴀ ᴨᴏᴅ ʙᴄᴇʍɪ ᴏʙᴧɪᴋᴀʍɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
  "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴋᴀᴄʜᴀᴧ ʙ ᴛʙᴏʏᴜ ʍᴀᴛь ɴᴀᴩᴋᴏᴛᴜ ᴄʙᴏɪʍ ᴄʜᴧᴇɴᴀʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀɜʙᴏʍʙɪᴧ ᴨɪɜᴅᴀᴋ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄʜᴧᴇɴᴀʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴋᴧɪᴛᴏᴩᴇ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴜᴄᴛᴩᴏɪᴧ ᴨᴀᴛᴀᴄᴏʙᴋᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ sᴄʜᴀᴄ ᴛʙᴏᴊ ᴩᴏᴛ ᴄᴨᴇᴩʍᴏᴊ ɴᴀᴨᴏᴧɴʏᴜ ᴄʙᴏᴇᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙʏᴀ ᴇʙᴀᴧɪ ʙᴄᴇ ʙ ᴅᴀɴɴᴏᴊ ᴋᴏɴɸᴇᴩᴇɴᴛsɪɪ ʙɪᴄʜᴀᴩᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ ᴜʜᴏ ᴛʙᴏᴇ ᴋᴏɴᴄʜᴀᴧ ʙᴇɜᴅᴀᴩь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴩᴇɜᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʜᴧᴇɴᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀʙɪᴧ ɴᴀ ᴧʙᴜ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄʜᴧᴇɴᴏʍ ᴛᴀᴛᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴜᴩᴀᴨᴀᴛᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴛʏ ᴨᴏᴄʜᴇʍᴜ ᴛᴜᴛ ᴨᴏᴄᴇᴧɪᴧᴄʏᴀ ɴᴀ ᴨᴏᴅᴄᴏᴄᴇ ʍᴏᴇᴦᴏ ʜᴜʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴋᴩᴏᴊ ᴄʙᴏʏᴜ ᴨᴀᴄᴛь ɴᴇᴅᴏᴜʍᴏᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɜʙɪᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʜᴧᴇɴᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴩɪᴇʜᴀᴧ ʙ ᴀʙɪᴀᴨᴀᴩᴋ ɪ ᴄᴋᴀɜᴀᴧ ᴄʜᴛᴏ ᴛʙᴏʏᴀ ʍᴀᴛь ᴩᴇᴅᴀɴᴋᴀ ᴅᴀʙʏ ᴇᴇ ɴᴀᴧʏᴄᴏ ᴨᴏʙᴩɪᴧɪ ᴅᴜᴩᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴧɪᴛᴏᴩ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴨᴇᴩᴇᴨᴏᴧɴᴇɴ ᴄʜᴏᴛᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴛᴜᴛ ʙʏᴄᴛᴩᴇᴇ ᴄᴏᴄɪ ᴅᴏᴧʙᴏᴇʙ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴀ ʍᴀᴛь ɜʙᴏɴɪᴧᴀ ʍᴏᴇʍᴜ ᴄʜᴧᴇɴᴜ ʙᴇɜᴅᴀᴩь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜʜʜ ᴄᴜᴋᴀ ᴋᴀᴋ ᴢʜᴇ ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴨᴩᴇᴅᴄᴛᴀʙᴧʏᴀᴇɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ᴄʜɪᴄᴛᴏ ᴄᴧᴀʙᴏʜᴀᴩᴀᴋᴛᴇᴩɴʏᴊ ʜᴜᴇᴄᴏᴄ ɪ ɴᴇ ʙᴏᴧᴇᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴋᴏᴩʍɪᴧ ᴛʙᴏʏᴜ  ʍᴀᴛь ᴄᴨᴇᴩʍᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴠᴏɪᴍ ᴄʜᴧᴇɴᴏʍ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴨᴩɪᴄʜᴇᴄᴋᴜ ᴅᴇᴧᴀᴧ ᴧᴏᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʏɴ ɯᴧʏᴜʜɪ ᴄʜᴀᴄ ɴᴀʜᴜʏᴀ ᴨᴏᴋᴀɜᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴄᴩᴀᴧ ɴᴀ ᴧɪᴛsᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴩᴀɜᴨᴩᴏᴇʙsᴄʜɪᴋ ʜᴜᴇʙ ᴄᴏᴄɪ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴊ ʜᴜᴊ ᴋᴀᴋ ᴛʙᴏᴊ ʍᴏɜᴦ ᴛᴀᴋᴏᴊ ᴢʜᴇ ʍᴇᴧᴋɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴧᴀᴋᴏɴᴏʙʏᴊ ᴅᴏᴧʙᴏᴇʙ ᴛʏ ᴨᴏɴɪʍᴀᴇɯь ᴄʜᴛᴏ ᴅᴇᴊᴄᴛʙɪᴇ ʏᴀᴅᴇᴩɴᴏᴦᴏ ᴏᴩᴜᴢʜɪʏᴀ ᴏᴄɴᴏʙʏʙᴀᴇᴛᴄʏᴀ ɴᴀ ᴩᴇᴀᴋᴛsɪɪ ᴋᴧɪᴛᴏᴩᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨᴜɜᴀᴛᴀʏᴀ ᴛsʏᴦᴀɴᴋᴀ ᴨᴏᴦᴀᴅᴀᴊ ʍɴᴇ ɴᴀ ᴨᴇɴɪᴄᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʙᴏɪʍ ᴨɪᴛᴏɴᴏʍ ɜᴀᴅᴜɯɪᴧ ʙᴇɜᴅᴀᴩь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀʜᴜʏᴀ ᴛʏ ᴇɯь ʍᴀᴩᴦᴀᴩɪɴ ʏᴀ ᴏᴅɴᴏᴦᴏ ᴨᴏɴʏᴀᴛь ɴᴇ ʍᴏᴦᴜ ɴᴇᴅᴏᴜʍᴏᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙʏᴀ ᴄʙᴏɪʍ ʜᴜᴇʍ ᴋᴀᴄᴛᴩɪᴩᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴅᴀʙɴᴏ ʙᴀᴩᴅʏᴜᴩʏ ɴᴇ ᴛsᴇᴧᴏʙᴀᴧ ʏᴀ ʙɪᴢʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʍᴏᴧᴄʜᴀɴɪᴇʍ ʙᴀʙᴋᴜ ᴜʙɪʙᴀᴇɯь ᴄʙᴏʏᴜ ᴩᴏᴅɴᴜʏᴜ ᴅᴀᴜɴ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ɴᴀʜᴜʏᴀ 47 ʜᴩᴏʍᴏᴄᴏʍ ᴇʙᴀɴᴀᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜɪᴄᴛᴀ ᴨᴀᴇʙʏʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ʙ ᴨᴩᴇɜɪᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴛ϶ᴋʙᴀɴᴅᴏ ᴛʏᴀ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ɜᴩʏᴀ ʏᴀ ʙʏᴧ ᴋᴀᴩᴀᴛɪᴄᴛᴏʍ ʏᴀ ᴅᴀᴢʜᴇ ɜɴᴀʏᴜ ᴋᴀᴋ ᴋᴩᴀᴄɪʙᴏ ᴜᴇʙᴀᴛь ᴛʙᴏʏᴜ ʍᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄᴧᴀʙᴏʜᴀᴩᴀᴋᴛᴇᴩɴʏᴊ ʜᴜᴇᴄᴏᴄ ɪ ɴᴇ ʙᴏᴧᴇᴇ ᴨᴏᴄʜᴇʍᴜ ᴛʏ ᴛᴀᴋ ᴄʜᴧᴇɴʏ ᴧʏᴜʙɪɯь ʏᴀ ᴨᴏɴʏᴀᴛь ɴᴇ ʍᴏᴦᴜ ɴᴇᴜᴄʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴀ ʍᴀᴛь ɜʙᴏɴɪᴧᴀ ʍᴏᴇʍᴜ ᴄʜᴧᴇɴᴜ ʙᴇɜᴅᴀᴩь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜʜʜ ᴄᴜᴋᴀ ᴋᴀᴋ ᴢʜᴇ ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴨᴩᴇᴅᴄᴛᴀʙᴧʏᴀᴇɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ᴄʜɪᴄᴛᴏ ᴄᴧᴀʙᴏʜᴀᴩᴀᴋᴛᴇᴩɴʏᴊ ʜᴜᴇᴄᴏᴄ ɪ ɴᴇ ʙᴏᴧᴇᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴋᴏᴩʍɪᴧ ᴛʙᴏʏᴜ  ʍᴀᴛь ᴄᴨᴇᴩʍᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴠᴏɪᴍ ᴄʜᴧᴇɴᴏʍ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴨᴩɪᴄʜᴇᴄᴋᴜ ᴅᴇᴧᴀᴧ ᴧᴏᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʏɴ ɯᴧʏᴜʜɪ ᴄʜᴀᴄ ɴᴀʜᴜʏᴀ ᴨᴏᴋᴀɜᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴄᴩᴀᴧ ɴᴀ ᴧɪᴛsᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴜᴢʜᴇ ᴄʙɪᴧᴄʏᴀ ᴄ ᴄʜёᴛᴜ ᴄᴋᴏᴧьᴋᴏ ʏᴀ ᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ɴᴀᴅᴏ ᴄᴨᴩᴏᴄɪᴛь ᴜ ᴛʙᴏᴇᴦᴏ ᴏᴛᴛsᴀ ʙᴇᴅь ᴏɴ ᴅᴩᴏᴄʜɪᴧ ɴᴀ ϶ᴛᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴊ ᴏᴛᴇᴛs ᴅᴀʙɴᴏ ᴜᴢʜᴇ ᴜʜᴏᴅɪ ᴄ ᴋʙᴀᴩᴛɪᴩʏ ɪ ᴢʜᴅёᴛ ᴨᴏᴋᴀ ʏᴀ ᴨᴏᴇʙᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴀ ᴨᴏᴛᴏʍ ᴨᴩɪʜᴏᴅɪᴛ ᴋᴀᴋ ɴᴇ ʙ ᴄʜёʍ ɴᴇ ʙʏʙᴀᴧ ᴏᴧᴜʜ ᴛʏ ᴇʙᴀɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ᴨᴏᴋᴀ ϶ᴛᴏ ɴᴇ ᴄᴛᴀᴧᴏ ʍᴇᴊɴᴄᴛᴩɪʍᴏʍ ᴩɪᴧɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ᴅᴜʍᴀᴧ ᴄʜᴛᴏ ᴛʙᴏʏᴀ ʍᴀᴛь ᴄᴏɜᴅᴀᴄᴛ ɸᴀɴ ᴋᴧᴜʙ ᴅᴧʏᴀ ʍᴏᴇᴦᴏ ʜᴜʏᴀ ɪ ᴅᴏᴋᴀɜʏʙᴀᴛь ᴄʜᴛᴏ ʍᴏᴊ ʜᴜᴊ ᴄᴀʍʏᴊ ᴧᴜᴄʜɯɪᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪ ᴄʜё ᴛʙᴏʏᴀ ʍᴀᴛь ʍɴᴇ ᴄᴏᴄёᴛ ᴀ ᴛʏ ɴᴇʍᴏsᴄʜь ᴅᴀᴢʜᴇ ɴᴇ ʍᴏᴢʜᴇɯь ᴇё ɜᴀʍᴇɴɪᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʜё ʙᴧʏᴀᴛь ʏᴀ sᴄʜᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ʙ ᴨᴇᴩᴅᴀᴋ ʜᴜʏᴀᴩʏᴜ ᴀ ᴏɴᴀ ᴨʏᴛᴀᴇᴛьᴄʏᴀ ᴋᴜᴅᴀ ᴛᴏ ᴜʙᴇᴢʜᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ʍᴏᴦᴜ ᴨᴏɴʏᴀᴛь ᴨᴏᴄʜᴇʍᴜ ᴛʙᴏʏᴀ ʍᴀᴛь ɴᴀ ᴄᴛᴏᴧьᴋᴏ ᴜᴄᴇᴩᴅɴᴏ ᴄᴏᴄёᴛ ʍᴏᴊ ʜᴜᴊ ᴋ ᴄʜᴇʍᴜ ᴏɴᴀ ᴄᴛᴩᴇʍɪᴛьᴄʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴩɪᴧɪ ʜᴜёʍ ᴨᴏʜᴏᴩᴏɴɪᴧ ᴏɴᴀ ᴜʍᴜᴅᴩɪᴧᴀᴄь ʙʏʙᴩᴀᴛьᴄʏᴀ ᴄʜᴛᴏʙʏ ɴᴀ ᴨᴏᴄᴧᴇᴅᴏᴋ ᴇsᴄʜё ʍɴᴇ ᴏᴛᴄᴏᴄᴀᴛь ɴᴜ ϶ᴛᴏ ᴜᴢʜᴇ ᴄᴛᴩᴀɴɴᴏ ᴄʜᴛᴏ ᴛʙᴏʏᴀ ʍᴀᴛь ᴛᴀᴋ ᴄʜᴀᴄᴛᴏ ʙᴩёᴛ ᴛʙᴏᴇʍᴜ ᴏᴛᴛsᴜ ᴄʜᴛᴏ ᴏᴛᴄᴀᴄʏʙᴀᴇᴛ ʍɴᴇ ʙᴄᴇᴦᴏ ᴨᴏ 10 ᴩᴀɜ ʙ ᴅᴇɴь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴊ ᴨᴀʜᴀɴ ᴄɴɪʍᴀᴧ ɴᴀ ʙɪᴅᴇᴏ ᴋᴀᴋ ʏᴀ ᴇʙᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ɪ ᴩᴀᴅᴏʙᴀᴧᴄʏᴀ ʙᴇᴅь ʏᴀ ᴛᴏᴢʜᴇ ʙᴇᴧɪᴋɪᴊ ᴅᴧʏᴀ ᴛʙᴏᴇᴦᴏ ᴨᴀʜᴀɴᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴏᴢʜᴇɯь ᴦᴏʙᴏᴩɪᴛь ʙᴄё ᴄʜᴛᴏ ᴜᴦᴏᴅɴᴏ ɴᴏ ʏᴀ ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛʙᴏʏᴜ ʍᴀᴛь ᴨᴏᴋᴀ ᴏɴᴀ ɴᴇ ᴄᴏʙᴇᴩɯɪᴛ ᴄᴜɪᴛsɪᴅ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴋᴀᴋ ᴇʙᴀᴧ ᴛᴇʙʏᴀ ᴜ ᴨᴏᴧɪᴛsᴇᴊᴄᴋᴏᴦᴏ ᴜᴄʜᴀᴄᴛᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ɴᴇʙɪᴅɪʍᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴇᴩᴇᴄᴏᴄɪ ᴛᴜᴛ, ʙʏʙᴧʏᴀᴅь  ᴇʙᴀᴧ ᴛᴇʙʏᴀ ᴧᴏʜᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ʙ ᴛʙᴏʏᴜ ʍᴀᴛь ᴄʙᴏᴊ ʜᴜᴊ ᴛʏᴋᴀʏᴜ ᴛᴀᴋ ᴛᴏ ʙᴧʏᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴀ ʍᴀᴛь ʍᴏᴊ ʜᴜᴊ ᴧʏᴜʙɪᴛ ᴄʜᴛᴏ ᴨɪɜᴅᴇᴛs[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴀᴛᴩᴏɸɪᴩᴏʙᴀɴɴᴜʏᴜ ɴᴀ ᴦᴏᴧᴏʙᴜ ᴇʙᴀɴᴜᴛᴜʏᴜ ʍᴩᴀɜь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴀᴄᴇɯ ʍɴᴇ ᴋᴀᴋ ᴅᴢʜᴀɜᴏʙʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ᴜ ᴨɪʙɴᴜɯᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴜ ᴋᴏʍᴏᴅᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴅ ɴᴀᴋᴩᴏᴛɪᴋᴀʍɪ ᴛᴇʙʏᴀ ɪʍᴇᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴇʙᴀᴧ ᴛᴇʙʏᴀ ᴜ ᴋᴀɴᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ʙ ᴋᴏʍʙᴀɪɴᴇ ɪʍᴇᴧ ʙᴧʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠɴᴀᴛᴜᴩᴇ ᴛᴇ ᴦᴧᴀɜᴇɴᴋɪ ᴄʜᴧᴇɴᴀʍ ʙʏᴛᴀsᴄʜɪᴧ ᴄᴜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʙɴᴀᴛᴜᴩᴇ ᴢʜᴇ ʍᴏᴊ ʜᴜᴊ ᴄᴏᴄᴀᴧ ʙᴇɜ ᴨᴩᴀʙᴀ ɴᴀ ᴏsʜɪʙᴋᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴀɴᴛsᴇᴛᴩɪᴩᴏʙᴀᴧ ᴛʏᴀ ʜᴜᴊᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴇᴩᴇᴧᴏʍᴀᴇʍ ᴛᴇʙᴇ ᴇʙᴧɪsᴄʜᴇ ᴩʙᴀɴᴀʏᴀ ᴋᴜᴩʙᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ʙ ᴋᴏʍʙᴀɪɴᴇ ɪʍᴇᴧ ʙᴧʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ʙᴀᴧьᴇᴩᴇ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ʙɴᴀᴛᴜᴩᴇ ᴋᴏɜᴇᴧ ᴇʙᴀᴛь ʏᴀ ᴛᴇ ᴩᴏᴦᴀ ʙʏᴩʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴩᴏᴦɴᴀᴧ ᴛʏᴀ ᴄʜᴧᴇɴᴀʍ ᴧᴏɯᴀᴩᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴩᴀᴊɴɪᴋᴏʙ ᴄᴀᴄᴇɯ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʍᴏᴊ ʜᴜᴊ ɴᴀ ᴋᴀɴᴜɴᴇ ᴇʙᴀᴧ ᴄʙᴏɪʍ ᴩᴛᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇ ɜᴀᴧᴜᴨᴏᴊ ɴᴀʜᴜᴊ ᴨᴩᴏᴋᴩᴜᴄʜᴜ ᴨᴩᴏᴛɪʙ ᴄʜᴀᴄᴏʙᴏᴊ ᴄᴛᴩᴇᴧᴋɪ ᴛʏ ʙᴧʏᴀᴛь ᴏʙᴏᴄᴄᴀɴᴀʏᴀ ᴀᴩᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ғᴩᴀɴᴛᴀᴧьɴᴀ ᴛʏᴀ ᴇʙᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏᴄᴄᴀᴧɪ ᴛᴇʙʏᴀ ᴧᴏɯᴀᴩᴀ ᴄᴄᴀɴᴀʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏɪ ᴨᴏᴨʏᴛᴋɪ ᴨᴏʏᴀʙɪᴛᴄʏᴀ ʙɴᴇ ᴄᴀᴩᴛɪᴩᴀ ᴋᴏʍɪᴄʜɴʏ ᴄʏɴᴜᴧʏᴀ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏɯɪʙᴋɪ ᴢʜᴏᴨᴏᴊ ɜᴀᴦᴧᴀᴅɪɯь ᴄʏɴ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀᴄᴋᴏᴨᴀᴧ ᴦᴩᴏʙ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ ᴏᴛъᴇʙᴀᴧ ᴇᴇ ʙ ᴩᴏᴛ ɪ ᴩᴀᴄᴛᴏᴨᴛᴀᴧ ᴇᴇ ᴋᴏᴄᴛɪ ɴᴀʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴇ ᴇʙᴀᴧᴏ ʙ ᴛɪᴄᴋɪ ɜᴀᴢʜʍᴜ ɪ ʙᴜᴅᴜ ᴢʜᴀᴛь ᴨᴏᴋᴀ ᴄʜᴇᴩᴇᴨᴜɯᴋᴀ ɴᴇ ᴧᴏᴨɴᴇᴛ ᴜ ᴛᴇʙʏᴀ ᴄʏɴ ɯᴀᴧᴀʙʏ ᴛʏ ᴛᴜᴨᴏёʙᴧʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴄᴇᴧ ᴇʙᴀɴʏᴊ ʏᴀ ᴛᴇʙʏᴀ ɜᴀ ᴜɯɪ ɴᴀ ᴄʙᴏᴊ ʜᴜᴊ ɴᴀᴛʏᴀɴᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙʏᴋɪɴᴜ ᴛʙᴏʏᴜ ᴛᴩᴇʙᴜʜᴜ ɪ ᴋᴏᴄᴛɪ ʙ ʍᴏᴦɪᴧᴜ ᴋ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴄʜʙᴀʙᴩᴀ ᴇʙᴀɴᴀʏᴀ ᴄʜᴧᴇɴ ɴᴀᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴄᴏᴄ ᴛʏ ᴄʜᴇ ᴄᴏᴄɪɯ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴄᴛᴀʙɪᴧ ᴧᴏʍ ʙ ᴢʜɪʙᴏᴛ ᴛʙᴏᴇᴊ ʙᴇᴩᴇʍᴇɴɴᴏᴊ ʍᴀʍᴀɯɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀɴʏᴊ ᴄʏɴ ɯᴀᴧᴀʙʏ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴏᴄᴀᴧᴀ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜᴧᴇɴ ʙ ᴛᴇʙᴇ ʍᴏᴊ ᴅᴏᴄᴛᴀᴧ ᴅᴏ ʍᴏɜᴦᴀ ɪ ᴨᴩᴏʙɪᴧ ᴇᴦᴏ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɯᴨᴩᴇʜᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧᴏ ᴛᴇ ᴄᴧᴏʍᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄɴʏᴀᴧ ᴄᴋᴀᴧьᴨ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ ɪ ᴨᴏᴄᴧᴇ ʙьʏᴜ ᴇᴇ ɜᴀᴧᴜᴨᴏᴊ ʙ ᴄʜᴇᴩᴇᴨ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʍᴏᴊ ʜᴜᴊ ᴢʜᴇ ᴨᴏᴧʏᴜʙɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ᴛᴀᴋ ᴄᴋᴀɜᴀᴛь ᴛʙᴏᴊ ᴋɪɯᴇᴄʜɴɪᴋ ɜᴅᴇᴄь ᴨᴏ ʙᴄᴇᴊ ᴋᴏɴɸᴇᴩᴇɴᴛsɪɪ ʙᴜᴅᴇʍ ᴄ ᴄʜᴧᴇɴᴏʍ ᴛᴀᴄᴋᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ᴛᴩɪᴨᴧᴏᴜʜᴜʏᴜ ᴛᴜʙᴇᴩᴋᴜᴧёɜɴᴜʏᴜ ʍᴀᴛь ʜᴜᴇʍ ᴏʙʙᴀᴧʏᴜ ᴄʏɴ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴜʙʏ ᴛᴇʙᴇ ɪɜɴᴜᴛᴩɪ ʜᴜᴇʍ ʙʏʙɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀʍᴀɯᴇ ᴛʙᴏᴇᴊ ᴋɪɯᴇᴄʜɴɪᴋ ᴄʙᴇᴩɴᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴋɪɴᴜ ᴛʙᴏɪ ʙʏᴩʙᴀɴɴʏᴇ ᴋᴏᴄᴛɪ ʙ ᴛᴀɜ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀɜᴧᴀᴦᴀʏᴜsᴄʜᴇᴇᴄʏᴀ ᴛᴇᴧᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄᴏʙᴀᴋᴀʍ ɴᴀ ᴋᴏᴩʍ ᴨᴜsᴄʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴜᴄʜɪᴊ ᴄʏɴ ɯᴧʏᴜʜɪ ᴇʙᴀᴧᴏ ɜᴀᴋᴩᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀʙᴀᴧɪ ᴄʙᴏᴇ ᴇʙᴀᴧᴏ ʙᴧʏᴀᴅᴄᴋᴏᴇ ᴄʏɴ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙʏᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ɴᴀ ᴋᴩʏɯᴋᴇ ᴦᴩᴏʙᴀ ᴛʙᴏᴇᴊ ʙᴀʙᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴧ ɯᴀᴧᴀʙᴜ ᴨᴏᴅ ɜᴀᴋᴀɜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴨᴇᴄʜᴀᴛᴀʏᴜ ᴛʙᴏᴇ ᴇʙᴀᴧᴏ ʙ ᴄᴛᴇɴᴜ ᴄʏɴ ɯᴧʏᴜʜɪ ᴛɪɸᴏɜɴᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴏᴦɪᴧьɴʏʍ ᴋᴩᴇᴄᴛᴏʍ ᴛʙᴏᴇᴦᴏ ᴅᴇᴅᴀ ᴇʙᴀᴧ ᴛᴩᴜᴨ ᴛʙᴏᴇᴊ ʙᴀʙᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴜɴᴜᴧ ɴᴇʙᴩɪᴛᴏᴇ ᴇʙᴀᴧᴏ ᴛʙᴏᴇᴊ ᴛᴀᴅᴢʜɪᴛᴄᴋᴏᴊ ʍᴀʍᴀɯɪ ᴨᴏᴅ ᴦᴀɜᴏɴᴏᴋᴏᴄɪᴧᴋᴜ ɪ ᴄᴩᴇɜᴀᴧ ᴄᴋᴀᴧьᴨ ɯᴧʏᴜʜᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴜʙᴇᴋᴏʙᴇᴄʜɪᴧ ᴛʙᴏʏᴜ ʍᴏᴧᴏᴅᴏᴄᴛь ʙ ᴏᴦɴᴇ ɪ ᴋɪɴᴜᴧ ʙ ᴛʙᴏʏᴜ ᴋᴏᴧʏᴀᴄᴋᴜ ᴋᴏᴋᴛᴇᴊᴧь ʍᴏᴧᴏᴛᴏʙᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɜ ᴋᴩɪᴋᴏʙ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ ɜᴀʍᴜᴛɪʍ ᴄᴇʍᴨᴧʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴩᴀɜᴩᴇɜᴀɴɴʏᴊ ᴩᴀʙᴄᴋɪᴊ ʜᴜᴇᴄᴏᴄ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏɪ ᴢʜɪᴩɴʏᴇ sᴄʜᴇᴋɪ ᴨᴏᴩʙᴀᴧ ᴄʜᴧᴇɴᴏʍ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʍᴇᴢʜɴᴀʏᴀ ɯᴧʏᴜɯᴋᴀ ɜᴀ ᴄʜᴧᴇɴ ᴨᴩɪɴɪʍᴀᴊᴄʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ɴᴇ ʙᴇᴦɪ ᴏᴛ ʍᴏᴇᴦᴏ ɪᴄᴨᴏᴧɪɴᴄᴋᴏᴦᴏ ᴄʜᴧᴇɴᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴧɪsᴄʜᴇ ᴛᴇʙᴇ ᴀᴦᴩᴇᴦᴀᴛᴏʍ ᴩʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴇ ᴨᴩʏsᴄʜᴀʙᴏᴇ ᴄᴏᴄᴀᴧɪsᴄʜᴇ ʜᴜᴇʍ ᴅᴀʙɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴇɴᴋɪ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ɴᴀ ʜᴜᴊ ᴄᴀᴢʜᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴜᴛ ʍᴀʍᴀɯᴋᴜ ᴛʙᴏʏᴜ ᴨᴏᴇʙʏʙᴀʏᴜ ᴄʏɴ ɯᴧʏᴜʜɪ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀʙᴧᴇʙʏɯ ᴋᴏɴᴇᴄʜɴᴏᴄᴛɪ ᴛʙᴏɪ ᴧᴏʍᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɜ ᴋᴏᴄᴛᴇᴊ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴄᴇʙᴇ ᴛᴩᴏɴ ᴇʙᴀɴᴜᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛᴜɯᴋᴜ ᴛʙᴏᴇᴊ ʙᴀʙᴋɪ ᴨᴏᴧ ᴩᴇᴋʙɪᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴏ ʙᴛᴏᴩᴜʏᴜ ʍɪᴩᴏʙᴜʏᴜ ᴅᴇᴅᴀ ᴛʙᴏᴇᴦᴏ ɜᴢʜёᴦ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇᴧʏᴄʜ ᴨᴇᴩᴇᴅᴏ ʍɴᴏᴊ ɴᴀ ᴋᴏᴧᴇɴɪ ᴨᴀᴅᴀᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʏɴ ᴢʜɪᴩɴᴏᴊ ᴨᴩᴏɸᴜᴩʏ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧᴏ ᴨᴏᴧᴏʍᴀʏᴜ ᴄʏɴᴋᴜ ᴜʍᴀᴧɪɯᴇɴɴᴏᴊ ᴅᴇɸᴇᴋᴛɴᴏᴊ ɯᴀᴧᴀʙʏ ᴛᴏ ᴇᴄᴛь ᴛᴇʙᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ʙ 45 ᴛʙᴏᴊ ᴏᴛᴇᴛs ʙʏᴧ ᴅɪᴋᴄᴀᴋᴇᴩᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴩᴏᴄᴛᴀ ᴇʙᴀᴩɪᴩᴜʏᴜ ᴛᴇʙʏᴀ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ ᴅᴇᴄɴᴀ ᴇʙᴀᴧ ᴛᴇʙʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏɪ ɜᴜʙʏ ᴜᴢʜᴇ ᴄᴀʍɪ ᴏᴛʙᴀᴧɪʙᴀʏᴜᴛᴄʏᴀ ᴏᴛ ᴄᴏᴨᴩɪᴋᴏᴄɴᴏʙᴇɴɪʏᴀ ᴄ ʍᴏɪʍ ʜᴜᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜᴛᴩᴏʍ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴋɪ ɴᴀᴨɪᴄᴀᴧ ᴄᴧᴏʙᴏ ʏᴀ ʙᴏᴦ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄᴧᴀʙʏᴊ ʙʏᴩᴏᴅᴏᴋ ᴋᴏɴɪ ɴᴇ ᴅʙɪɴь ᴛᴏᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀᴩᴛʏɯᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʏɴᴏᴋ ᴄʙɪɴᴏᴨᴀᴄᴀ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴦᴧᴀɜᴀ ᴄʙᴏɪʍ ᴄʜᴧᴇɴᴏʍ ʙʏᴅᴀʙᴧɪʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ ᴨᴏᴛᴏᴋᴇ ʙᴏɜᴅᴜʜᴀ ᴩᴀɜʙᴇʏᴀᴧ ᴨᴩᴀʜ ᴛʙᴏᴇᴦᴏ ᴏᴛᴛsᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴧɪᴛsᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ɪɜᴜᴩᴏᴅᴏʙᴀᴧ ᴨᴇɴɪᴄᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴦɪᴇɴᴀ ᴇʙᴀɴᴀʏᴀ ᴏᴛᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀɴʏᴀʍɪᴩɴᴀʏᴀ ɯᴧʏᴜʜᴀ ᴛʏ ᴜᴢʜᴇ ᴧᴇsᴄʜᴇᴊ ᴛᴜᴛ ᴏᴛʜʙᴀᴛʏʙᴀᴇɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏ ᴦᴜʙᴀʍ ᴛᴇʙᴇ ᴄʜᴧᴇɴᴏʍ ʙᴏᴅɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜᴢʜᴇ ɜᴀᴨᴏʍɴɪᴧ ᴛʏ ɜᴀᴨᴀʜ ʍᴏɪʜ ʏᴀɪᴛs ᴄʜᴛᴏ ᴄᴩᴀɜᴜ ʙᴇᴢʜɪɯь ᴋ ɴɪʍ ᴋᴀᴋ ᴋ ʙᴏᴅᴇ ʙ ᴨᴜᴄᴛʏɴᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴊʍᴀᴊ ʍᴏʏᴜ ɪᴄᴨᴏᴧɪɴᴄᴋᴜʏᴜ ʜᴜɪɴᴜ ᴨɪɜᴅᴀᴋᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʜᴏ ᴄᴏɴɴᴀʏᴀ ᴨᴩɪɴᴛsᴇᴄᴄᴀ ᴄᴏᴄɪ ʍɴᴇ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛъᴇʙᴀᴧ ᴛᴜᴛ ᴄʏɴᴋᴀ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴʏᴜ ᴇʙᴀᴧ ᴛᴇʙʏᴀ ɴᴀ ᴨᴇᴩᴇᴅᴏʙᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴀᴋ ᴛʏ ᴄᴧᴀʙʏᴊ ᴄʏɴ ᴇʙᴀɴᴏᴊ ɯᴀᴧᴀʙʏ ᴇʙᴀᴧᴏ ʙᴛᴜᴧɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜ ᴨᴏᴧɪᴋᴧɪɴɪᴋɪ ᴛᴇʙᴇ ᴇʙᴀᴧᴏ ᴩᴀɜᴏʙьʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴɪ ɴᴀ ᴄʜᴛᴏ ɴᴇ ᴄᴨᴏᴄᴏʙɴᴀʏᴀ ᴢʜɪᴩɴᴀʏᴀ ɯᴀᴧᴀʙᴀ ᴄᴏᴄɪ ʍɴᴇ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴩᴏᴄᴛᴏ ɴᴀᴨᴩᴏᴄᴛᴏ ʙᴏɜьʍᴜ ᴋᴜᴄᴏᴋ ʍʏᴀᴄᴀ ɪ ʙᴜᴅᴜ ᴇʙᴀɯɪᴛь ᴛᴇʙᴇ ɪʍ ᴨᴏ ᴄᴏᴄᴀᴧɪsᴄʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴜ ᴛᴜɯᴜ ᴦʙᴏɜᴅʏᴀʍɪ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏʍɴɪᴛsᴀ ʍᴀʍᴀɯᴋᴀ ᴛʙᴏʏᴀ ʍɴᴇ ʜᴜᴊ ᴄᴏᴄᴀᴧᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀɜᴦᴏɴʏᴀᴊᴄʏᴀ ᴄʏɴ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ ᴧᴇᴛᴏᴨɪᴄɪ ɜᴀᴨɪᴄᴀᴧ ᴋᴀᴋ ᴩʙᴀᴧ ᴛᴇʙᴇ ᴇʙᴀᴧᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴛsᴜ ᴛᴇ ɴᴀ ᴇʙᴀᴧᴏ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴩɪɴᴢʜᴏʙʏᴊ ᴛʏ ᴄʏɴ ɯᴧʏᴜʜɪ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴛᴜᴛ ʍᴀᴛь ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧʏʜ ᴄᴏʙᴀᴋᴇɴ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛᴏᴅᴩᴀᴧ ᴛʙᴏʏᴜ ʍᴀʍᴀɯᴋᴜ ᴋᴀᴋ ᴏʙᴏɪ ᴄᴛᴀᴩʏᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴛʏᴀɴᴜᴧ ᴛʙᴏᴇ ᴇʙᴀᴧᴏ ʙᴜᴅᴛᴏ ϶ᴛᴏ ᴛᴇᴛᴇʙᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴀᴋ ᴛʏ ᴄᴧᴀʙʏᴊ ᴄʏɴ ᴇʙᴀɴᴏᴊ ɯᴀᴧᴀʙʏ ᴇʙᴀᴧᴏ ʙᴛᴜᴧɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴇɜɸᴀɴᴛᴀɜɪᴊɴᴀʏᴀ ᴅᴏᴄʜᴜᴩᴋᴀ ʍᴏᴦɪᴧьɴᴏᴊ ᴋᴜᴩᴛɪɜᴀɴᴋɪ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇᴩᴨɪᴧᴀ ɴɪᴋᴄʜᴇʍɴᴀʏᴀ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇᴅᴇᴇᴄᴨᴏᴄᴏʙɴᴀʏᴀ ᴛᴜɯᴋᴀ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴩɪᴩᴏʙᴀᴧ ᴛᴇʙᴇ ᴩʏᴧᴛsᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɯᴛᴜᴋᴀᴛᴜᴩɪᴧ ᴨᴇɴɪᴄᴏʍ ᴛᴇ ᴇʙᴀᴧьɴɪᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴨᴇɴɪᴄ ᴨᴀᴅᴀᴊ ᴩᴇᴋᴄ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴜʙɴᴏᴊ ᴄᴏᴄᴛᴀʙ ʙʏʙɪʙᴀᴧ ᴛᴇ ᴀᴦᴩᴇᴦᴀᴛᴏʍ ᴄʙᴏɪʍ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ᴛᴜᴛ ᴨᴩᴏᴄᴛᴏ ɴᴀᴨᴩᴏᴄᴛᴏ ᴇʙᴀɴᴀʏᴀ ᴛᴇᴧʏᴄʜ ᴨᴀᴅɪ ɴᴀ ᴋᴏᴧᴇɴɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴄʜɪᴄᴛᴏ ᴨᴏ ɸᴇɴɯᴜʏᴜ ᴇʙᴀᴧ ᴛʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏɯɪʙᴋɪ ᴢʜᴏᴨᴏᴊ ɜᴀᴦᴧᴀᴅɪɯь ᴄʏɴ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴇ ᴇʙᴧɪsᴄʜᴇ ɴᴀ ᴄʜᴀᴄᴛɪ ᴨᴏᴩʙᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴏᴄᴇɯь ʍɴᴇ ʜᴜᴊ ᴧʏᴀʙᴩᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴇɜ ʍᴏᴇᴦᴏ ʜᴜʏᴀ ᴜ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ ᴦɴᴏᴊɴᴀʏᴀ ᴀɴᴦɪɴᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴏᴄᴛʏᴀʍɪ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴇ ɜᴀᴩᴇɜᴀᴧ ᴛʙᴏʏᴜ ʙᴀʙᴋᴜ ɴᴀᴄʍᴇᴩᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴏᴛᴏʙᴜʏᴜ ᴨᴏᴧᴏᴄᴛь ᴛʙᴏʏᴜ ɜᴀᴧьʏᴜ ʙᴇᴛᴏɴᴏʍ ᴄʏɴᴜᴧʏᴀ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ɴᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ɯᴋʙᴀᴧ ᴄʜᴧᴇɴᴏʙ ᴄʙᴏᴇᴦᴏ ᴏʙᴩᴜɯᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴀᴩᴜ ᴨᴀᴋᴇᴛᴏʙ ᴄᴨᴀᴊᴄᴀ ᴏʙᴇᴄᴨᴇᴄʜɪʙᴀᴧɪ ᴄᴇᴋᴄ ᴄ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴇᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɜɴᴀᴄɪᴧᴏʙᴀᴧ ᴛʏ ʍᴏᴊ ᴨɪᴄʏᴜɴ ᴄʙᴏɪʍ ᴩᴛᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇʍ ᴛᴇʙʏᴀ ʙɜʙᴏᴅᴩɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ᴅᴇɸᴏᴩʍɪᴩᴏʙᴀɴᴏᴊ ɯᴧʏᴜʜᴇ ʙᴜᴅᴜ ʜᴜᴊ ʙ ᴩᴏᴛ ᴄᴜʙᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴨɪᴄᴀᴧ ᴛᴇʙʏᴀ ᴨᴩᴏᴄᴛɪᴛᴜᴛᴋᴜ ᴋᴀᴋ ɴᴀ ᴛᴩᴀᴄᴄᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏʙᴏᴄᴀᴧ ᴛᴇʙᴇ ᴇʙᴀᴧᴏ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ʙᴀʙᴋᴜ ʙʏᴇʙᴀᴧ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴏᴄᴀᴧ ᴛʏ ᴄʜᴇᴛᴏ ᴄᴧᴀʙᴀᴋ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴋᴀᴩᴧᴏᴄᴏɴᴜ ᴇʙᴀᴧᴏ ᴄᴧᴏʍᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ʙᴀʙᴋᴜ ʙʏᴇʙᴀᴧ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀɴɪɜᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ɴᴀ ʜᴜᴊ ᴋᴀᴋ ᴄʜᴇᴩʙʏᴀᴋᴀ ɪ ᴏɴᴀ ᴅᴀᴢʜᴇ ɴᴇ ᴄᴛᴀᴧᴀ ᴄᴩʏʙᴀᴛᴄьʏᴀ ᴄ ɴᴇᴦᴏ ᴛᴀᴋ ᴋᴀᴋ ᴨᴏɴɪʍᴀᴧᴀ ᴄʜᴛᴏ ʍᴏᴊ ʜᴜᴊ ϶ᴛᴏ ᴄʜᴛᴏ ᴛᴏ ʙᴇᴧɪᴋᴏᴇ ᴅᴧʏᴀ ɴᴇᴇ ϶ᴛᴏ ʙʏᴧᴀ ᴋᴀᴋ ᴩᴇᴧɪᴋʙɪʏᴀ ɪ ᴏɴᴀ ɪɜ ɜᴀ ʙᴇᴩʏ ʙ ɴᴇᴦᴏ ɴᴇ ʍᴏᴦᴧᴀ ᴄᴧᴇɜᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴀʙᴀᴊ sᴄʜᴀᴄ ʙᴏɜьʍᴇʍ ɪ ʙʏᴇʙɪʍ ᴛʙᴏʏᴜ ʍᴀᴛь ᴛᴇʙᴇ ʙᴇᴅь ᴛᴏᴢʜᴇ ɴᴀᴅᴏᴇᴧᴀ ϶ᴛᴀ ɯᴀᴧᴀʙᴀ ᴏɴᴀ ᴜᴢʜᴇ ɴᴇ ᴨᴏɴɪʍᴀᴇᴛ ᴄʜᴛᴏ ᴛʙᴏᴩɪᴛ ᴀ ʍᴇᴄᴛᴏ ᴛᴏᴦᴏ ᴄʜᴛᴏ ᴏᴅᴜʍᴀᴛьᴄʏᴀ ᴏɴᴀ ᴋᴀᴋ ʙᴄᴇᴦᴅᴀ ɜᴀʙɪʙᴀᴇᴛ ᴄʙᴏɪ ʍʏᴄᴧɪ ʜᴜʏᴀʍɪ ᴋᴀᴋ ᴛʏ ᴇᴇ ᴛᴇᴩᴨɪɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ᴋᴀᴋ ɴᴇ ʍᴏᴦᴜ ᴨᴏɴʏᴀᴛь ɜᴀᴄʜᴇʍ ᴛʙᴏʏᴀ ʍᴀʍᴀ ᴄᴛᴀᴧᴀ ɯᴧʏᴜʜᴏᴊ ʙᴇᴅь ᴜ ɴᴇᴇ ʙʏᴧ ᴨᴏᴛᴇɴᴛsɪᴀᴧ ʙʏᴜᴄʜɪᴛьᴄʏᴀ ɴᴀ ʜᴏᴩᴏɯᴜʏᴜ ᴀᴋᴛᴩɪᴄᴜ ɪᴧɪ ᴨᴏʙᴀᴩᴀ ɴᴏ ʍᴇᴄᴛᴏ϶ᴛᴏᴦᴏ ᴏɴᴀ ᴛᴇᴨᴇᴩь ᴦᴧᴏᴛᴀᴇᴛ ɴᴀ ᴛᴇᴨᴧᴏᴛᴩᴀᴄᴇ ᴜ ʙᴏʍᴢʜᴇᴊ ʜᴜɪ ɴᴜ ʏᴀ ʙ ɯᴏᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴏ ᴋᴀᴊɸᴜ ᴛʙᴏʏᴀ ʍᴀᴛь ᴄᴏᴄᴇᴛ ᴨᴏᴋᴜᴩɪɯь ᴋᴏᴄʏᴀᴋ ɪ ᴛʙᴏʏᴀ ʍᴀᴛь ɴᴀᴄʜɪɴᴀᴇᴛ ᴄᴏᴄᴀᴛь ɴᴏ ᴛᴀᴋ ᴀᴋ ʍʏ ᴅᴀᴢʜᴇ ɴᴇ ᴨᴏɴɪʍᴀᴇʍ ᴄʜᴛᴏ ᴨᴩᴏɪᴄʜᴏᴅɪᴛ ʍʏ ɴᴀᴄʜɪɴᴀᴇʍ ᴇᴇ ᴨɪɜᴅɪᴛь ᴋᴀᴋ ᴨᴏᴄᴧɴᴇᴅɴɪʏᴜ ɯᴀᴧᴀʙᴜ ɴᴏ ᴅᴀᴢʜᴇ ᴨᴏᴄᴧᴇ ϶ᴛᴏᴦᴏ ᴏɴᴀ ɴᴇ ᴨᴇᴩᴇᴄᴛᴀʙᴀᴧᴀ ɴᴀʍ ᴄᴏᴄᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴅᴀʙᴀᴊ ᴨᴏᴅᴜʍᴀᴇʍ ᴄʜᴛᴏ ʙʏ ʙʏᴧᴏ ᴇᴄᴧɪ ʙʏ ᴛʙᴏʏᴀ ʍᴀᴛь ʙʏᴧᴀ ᴨᴩɪᴧɪᴄʜɴᴏᴊ ᴢʜᴇɴsᴄʜɪɴᴏᴊ ᴀ ɴᴇ ᴅᴀʙᴀᴧᴋᴏᴊ ᴇʙᴀɴɴᴏᴊ ɴᴀʙᴇᴩɴᴏ ʍʏ ʙʏ ɪ ɴᴇ ᴨᴏɜɴᴀᴋᴏʍɪᴧɪᴄь ɴᴏ ʙᴏᴧᴇᴊ ᴄᴧᴜᴄʜᴀᴇᴊ ᴏɴᴀ ᴅᴀᴧᴀ ɴᴀʍ ʙ ᴢʜᴏᴨᴜ ᴨᴏ 150 ᴩᴀɜ ᴋᴀᴢʜᴅᴏʍᴜ ɴᴇᴨᴧᴏʜᴏ ᴅᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴏᴦᴅᴀ ᴛʙᴏʏᴀ ʍᴀᴛь ᴄᴨᴜᴄᴛɪᴧᴀᴄь ɴᴀ ɜᴇʍᴧʏᴜ ᴜ ɴᴇᴇ ʙʏᴧᴀ ɜᴀᴅᴀɴɪʏᴀ ᴄᴨᴀᴄᴛɪ ʍɪᴩ ɴᴏ ʍᴇᴄᴛᴏ ϶ᴛᴏᴦᴏ ᴏɴᴀ ɴᴀᴄʜᴀᴧᴀ ᴄᴏᴄᴀᴛь ʜᴜɪ ɴᴀᴨᴩᴀʙᴏ ɪ ɴᴀᴧᴇʙᴏ ɴᴏ ᴄᴜᴛь ʙ ᴛᴏʍ ᴄʜᴛᴏ ᴏɴᴀ ɪ ᴛᴀᴋ ᴄᴨᴀᴄᴀᴇᴛ ʍɪᴩ ᴛᴇʍ ᴄᴀʍʏʍ ᴜᴅʙᴏᴧᴇᴛʙᴏᴩʏᴀᴇᴛ ʙᴄᴇʜ ʍᴜᴢʜᴄʜɪɴ ɴᴀ ᴄʙᴇᴛɪ ᴄᴨᴀᴄɪʙᴏ ᴛʙᴏᴇᴊ ʍᴀʍᴇ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴀ ʍᴀʍᴀ ᴜᴢʜᴇ ᴅᴀʙɴᴏ ᴨᴩɪʜᴏᴅɪᴛ ᴨᴏᴄᴏᴄᴀᴛь ɴᴀʍ ʜᴜᴊ ɴᴏ ᴄ ᴋᴀᴅᴢʜᴅʏʍ ᴩᴀɜᴏʍ ᴏɴᴀ ʙᴄᴇ ʙᴏᴧьɯᴇ ɪ ʙᴏᴧьɯᴇ ɴᴀɪɴᴀᴇᴛ ᴢʜᴩᴀᴛь ɴᴀɯᴜ ᴄᴨᴇᴩʍᴜ ɴᴏ ᴋ ᴛᴀᴋᴏʍᴜ ɴᴀᴄ ᴢʜɪɜɴь ɴᴇ ᴦᴏᴛᴏʙɪᴧᴀ ɪ ɜᴀ ʙᴄᴇ ᴇᴇ ᴅᴇᴊᴄᴛʙɪʏᴀ ʍʏ ᴩᴇɯɪᴧɪ ᴇᴊ ᴇʙᴀɴᴜᴛь ᴨᴏ ᴧᴇsᴄʜᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴢʜᴇ ᴨᴏᴨᴩᴏʙᴜᴊ ᴏᴨᴩᴏʙᴅᴀᴛь ᴄʙᴏʏᴜ ʍᴀᴛь ᴨᴏᴋᴀ ᴇᴇ ᴩᴏᴛ ɴᴇ ɜᴀᴨᴏᴧɴᴇɴ ɴᴀɯᴇᴊ ᴋᴏɴᴄʜᴇᴊ ɪᴧɪ ʍᴏᴢʜᴇɯь ʙᴄᴛᴀᴛь ɴᴀ ᴋᴏᴧᴇɴɪ ɜᴀ ʍᴇᴄᴛᴏ ᴄʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ɪ ᴨᴏᴧᴜᴄʜᴀᴛь ʙ ᴩᴏᴛ ᴅᴏʜᴜ ᴋᴏᴛᴏᴩᴀʏᴀ ᴇᴊ ᴛᴀᴋ ɴᴇᴏʙʜᴏᴅɪʍᴀ ʙᴇᴅь ᴏɴᴀ ɴᴜᴢʜᴅᴀᴇᴛьᴄʏᴀ ʙ ɴᴀɯᴇᴊ ᴄᴨᴇᴩʍᴇ ᴋᴀᴋ ʙ ɴᴀᴩᴋᴏᴛɪᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙɴᴀᴛᴜᴩᴇ ᴛʙᴏʏᴜ ʍᴀᴛь ɴᴀ ʜᴜᴇ ᴨᴩᴏᴋᴀᴛɪᴧᴏ ᴏɴᴀ ʍᴏᴋᴧᴀ ᴨᴏᴅ ᴅᴏᴢʜᴅᴇʍ ᴢʜᴅᴀʙ ᴄʙᴏᴊ ᴀʙᴛᴏʙᴜᴄ ɴᴏ ʙᴄᴇ ᴛᴀᴋɪ ʏᴀ ɴᴇ ᴅᴀᴧ ᴇᴊ ʙᴏɜʍᴏᴢʜɴᴏᴄᴛь ᴨᴩᴏʍᴏᴋɴᴜᴛь ɪ ᴩᴇɯɪᴧ ᴨᴩᴇᴅᴏᴄᴛᴀʙɪᴛь ᴇᴊ ᴄʙᴏᴊ ʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄɴᴏʙᴀ ᴛʏ ɴᴀ ᴋᴏᴧᴇɴʏᴀʜ ɯᴀᴧᴀʙᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ɯᴧʏᴜʜᴜ ᴀ ᴛʏ ᴛᴇᴩᴨɪ ᴅᴀᴧᴇᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ʙᴏ ʙᴄᴇʜ ᴨᴏɜᴀʜ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴋᴩᴏᴊ ᴇʙᴧɪsᴄʜᴇ ʍᴇᴅᴧᴇɴɴʏᴊ ᴋᴜᴄᴏᴋ ᴅᴇᴩьʍᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴜɯᴋᴀɴёɴᴏᴋ ᴇʙᴀɴʏᴊ ᴛʏ ᴄʜᴇ ᴛᴀʍ ʙ ᴛᴇᴩᴨɪᴧʏ ɜᴀᴨɪᴄᴀᴧᴄʏᴀ ʏᴀ ᴢʜᴇ ᴛʙᴏʏᴜ ʍᴀᴛь ʙʏᴢʜʍᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴀᴧᴇɴɴʏʍ ʍᴏᴧᴏᴛᴏʍ ᴀᴅᴀ ᴋᴏᴧɪʍ ᴦᴏᴧᴏʙᴜ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀᴅɪᴋᴀʍᴇɴᴛᴀʍɪ ᴛʙᴏʏᴜ ʍᴀʍᴀɯᴋᴜ ɴᴀᴋᴀᴄʜᴀᴇᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʜᴜᴇᴄᴏᴄᴋᴀ ᴛᴇᴩᴨɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙьʏᴜ ɜᴀᴧᴜᴨᴏᴊ ʙ ᴄʜᴇᴩᴇᴨ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴋᴇ ɯᴧʏᴜʜᴇ ᴛᴀᴋ ᴄʜᴛᴏ ᴇᴇ ᴄʜᴇᴩᴇᴨ ᴧᴏᴨᴀᴇᴛᴄʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴛᴜᴛ ʜᴜᴇʍ ɜᴀᴨɪɴᴀʏᴜ ᴅᴏ ᴨᴏᴧᴜᴄʍᴇᴩᴛɪ ᴄʏɴ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴇ ᴇʙᴀᴧᴏ ᴩᴀᴄʜᴜʏᴀᴩʏᴜ ᴨᴏ ᴄʜᴀᴄᴛʏᴀʍ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴇʙᴜ ᴛʙᴏʏᴜ ʍᴀᴛь ɜᴅᴇᴄь ᴅᴀᴢʜᴇ ɴᴇ ɜᴀʍᴇᴄʜᴜ ᴄʏɴ ɯᴧʏᴜɯɪᴊ ᴛʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴏɜᴦɪ ᴛᴇʙᴇ ᴄᴨᴩᴇᴄᴜʏᴜ ᴄʜᴧᴇɴᴏʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏᴊ ᴄʙɪɴᴀᴩɴɪᴋ ᴄᴏᴢʜᴦᴜ ɴᴀʜᴜᴊ ᴄʏɴ ᴨᴩᴏʍᴏᴋɯᴇᴊ ᴋᴜᴩᴛɪɜᴀɴᴋɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙъᴇʙᴀᴧᴄʏᴀ ɴᴀ ᴋᴀʍᴀɜᴇ ʙ ᴛsᴇᴩᴋᴏʙь ᴋ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯᴇ ɪ ᴛᴀʍ ᴛᴩᴀʜɴᴜᴧ ᴇᴇ ᴩᴀᴄᴨʏᴀᴛɪᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀʍᴀɴ ᴛʙᴏʏᴀ ɯᴀᴧᴀʙᴀ ᴇʙᴜᴄʜᴀʏᴀ ʍᴇᴢʜᴅᴜ ᴨᴩᴏᴄʜɪʍ, ᴄʍᴏᴛᴩɪ ɴᴇ ɴᴀᴅᴏᴩʙɪᴄь ᴛᴀʍ ᴄʏɴᴜᴧʏᴀ ɯᴧʏᴜʜɪ ᴄᴜᴛᴜᴧʏᴊ, ᴨᴏᴋᴀ ɴᴀɯɪ ʜᴜɪ ᴏʙᴩᴀʙᴀᴛʏʙᴀᴛь ʙᴜᴅᴇɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴏᴊ ʜᴜᴊ ᴛᴇʙʏᴀ ᴜʙɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴀᴛь ᴛᴇ ᴇʙᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏᴊ ᴋɪɯᴇᴄʜɴɪᴋ ᴨᴏ ʙᴄᴇʍᴜ ᴩᴀᴊᴏɴᴜ ᴨᴩᴏʙᴇᴅᴜ ᴋᴀᴋ ʙᴀᴩᴅʏᴜᴩ ɴᴀʜᴜᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʙᴜᴅᴇɯь ɜᴅᴇᴄь ᴅᴏ ᴨᴏᴄᴛᴏʏᴀɴɴᴏᴊ ᴄʙᴏᴇᴊ ᴄɪɴᴇʙʏ ʍɴᴇ ᴄʜᴧᴇɴ ᴄᴏᴄᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜᴛᴩᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ᴩᴀᴄᴋɪɴᴜ ɜᴅᴇᴄь ᴋᴀᴋ ᴜᴋᴩᴀɯᴇɴɪᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏʏᴜ ʍᴀʍᴀɯᴜ ɜᴅᴇᴄь ᴨᴇᴩᴇᴧᴏʍᴀʏᴜ ᴛʏ ᴄʏɴᴏᴋ ɯᴧʏᴜʜɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʏɴ ɯᴀᴋᴀᴧᴀ ʏᴀ ᴛʙᴏɪ ᴋᴏᴄᴛɪ ᴨᴇᴩᴇᴧᴏʍᴀʏᴜ ᴨᴏᴋᴀ ᴛʏ ʙᴜᴅᴇɯь ʍʏᴄʜᴀᴛь ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴊ ᴩᴏᴛ ᴇʙᴇᴛ ᴋᴩᴏʙᴏᴛᴏᴄʜᴀsᴄʜɪᴊ ᴦᴇʍᴏᴩᴩᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴜ ʍᴀᴛь ᴩᴀɜᴅᴇᴧᴀᴧ ʙ ɸᴏᴩʍᴇ ᴋᴩᴇᴄᴛᴀ ɴᴀ ᴅᴏᴄᴋᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀᴄᴋᴩᴜᴛɪᴧ ᴨɪɜᴅᴜ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ɴᴀ ʙᴄʏᴜ ᴄᴛᴩᴀɴᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɜᴀᴄᴜɴᴜᴧ ᴄʙᴏʏᴜ ᴩᴜᴋᴜ ʙ ᴦᴏᴩᴧᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ɪ ᴨᴇᴩᴇᴋᴩᴏɯɪᴧ ᴛᴩᴀʜᴇʏᴜ ʙ ʍᴇᴧᴋɪᴇ ᴋᴜᴄᴋɪ ᴀ ᴨᴏᴛᴏʍ ᴄᴢʜᴀᴧ ᴇᴇ ᴧᴇᴦᴋɪᴇ ᴛᴀᴋ ᴄʜᴛᴏ ᴏɴɪ ᴧᴏᴨɴᴜᴧɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜᴧᴇɴ ᴛʏ ᴨᴏᴄᴏᴄɪ ᴅᴜᴩᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴄᴧᴇ ᴄᴇᴋᴄᴀ ᴄ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩьʏᴜ ᴇᴇ ᴛᴇᴧᴏ ᴄᴛᴀᴧᴏ ᴨᴏʜᴏᴅɪᴛь ɴᴀ ᴛᴩᴜᴨ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴀ ʍᴀᴛь ᴏᴛᴋᴩʏᴧᴀ ᴩᴏᴛ ɪ ʏᴀ ɴᴀᴄᴄᴀᴧ ᴇᴊ ʙ ᴩʏᴧьᴛsᴇ ʜᴇʜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴛᴄᴇᴋ ᴛʙᴏᴊ ᴄʜᴇᴩᴇᴨɴᴏᴊ ʙ ʍᴀᴧᴇᴊɯɪᴇ ᴀᴛᴏʍʏ ɪɜᴜᴩᴏᴅᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜᴦᴏᴧᴋᴏʍ ᴋᴀʍɴʏᴀ ᴨᴩᴏᴅᴏᴧʙɪᴧ ʙᴇᴄᴏᴋ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ʙɴᴀᴛᴜᴩᴇ ᴛᴇʙᴇ ᴨɪɜᴅʏ ɴᴀᴅᴀʏᴜ ᴄʏɴᴏᴋ ɯᴀᴧᴀʙʏ ᴀ ɴᴜ ᴛᴇᴩᴨɪ ᴅᴀʙᴀᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ʏᴀ ᴛʙᴏʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴛʏ ᴅᴀʙᴀᴊ ᴛᴀʍ ᴨᴏᴨᴀᴅᴀᴊ ɴᴀ ʍᴏᴊ ᴄʜᴧᴇɴ ᴏᴨʏᴀᴛь ᴢʜᴇ ᴋᴀᴋ ᴛʙᴏʏᴀ ʍᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏᴊ ᴄʜᴇᴩᴇᴨᴏᴋ ɜᴅᴇᴄь ʙ ᴏᴅɴᴜ ᴩᴜᴋᴜ ʙᴏɜьʍᴜ ɪ ɴᴏᴦɪ ʙ ᴅᴩᴜᴦᴜʏᴜ ɪ ᴄᴧᴏᴢʜᴜ ᴛᴇʙʏᴀ ɴᴀᴨᴏᴨᴏᴧᴀʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧᴏʍᴀᴇʍ ᴇʙᴀᴧᴏ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʙᴇɜ ᴩᴀɜᴦᴏʙᴏᴩᴏʙ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴀᴋ ᴄᴋᴀɜᴀᴛь ᴇʙᴀᴧ ᴛᴇ ʍᴀʍᴀɯᴋᴜ ᴨᴏ ᴋᴧᴀᴄᴄɪᴋᴇ ᴢʜᴀɴᴩᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀᴄʜɪɴᴀᴊ ʍᴏɪ ʏᴀᴊᴛsᴀ ᴋᴀᴋ ʙᴏᴦᴏʙ ᴨᴏᴄʜɪᴛᴀᴛь ᴄʜᴛᴏʙʏ ʏᴀ ᴛᴇʙᴇ ᴨᴇᴩᴇᴄᴛᴀᴧ ɪʍɪ ᴛʙᴏᴇ ᴇʙᴀᴧᴏ ᴨᴏ ᴄᴛᴇɴᴇ ᴄʍᴀɜʏʙᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴀᴛᴧʏ ᴛʙᴏɪ ʙʏᴩʙᴜ ᴄʏɴᴏᴄʜᴇᴋ ʙᴧʏᴀᴅᴏᴩᴜᴋᴏᴊ ɯᴧʏᴜɯᴇɴᴛsɪɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴅ ᴨᴇᴛᴧʏᴜ ᴄᴛᴜᴧ ᴛᴇʙᴇ , ᴀ ᴨᴏᴅ ᴩᴇʙᴩᴏ ɴᴏᴢʜɪ ᴄʏɴ ɯᴀᴧᴀʙʏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴇʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ɯᴧʏᴜʜᴜ ᴀ ᴛʏ ᴛᴇᴩᴨɪ ᴅᴀᴧᴇᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀᴄᴨɪɜᴅᴏɯɪᴧ ʙᴀᴦɪɴᴀᴧьɴʏᴇ ʙᴩᴀᴛᴀ ᴛʙᴏᴇᴊ ʍᴀʍᴀɯɪ ᴄʙᴏɪʍ ᴛᴀᴩᴀɴᴏʙʏʍ ʜᴜᴇʍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ ʜᴜᴊ ʙ ᴩᴏᴛ ɜᴀᴨɪʜᴀʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴛʏ ᴦᴧᴀʙɴᴏᴇ ʙᴇᴩɪ ʍᴏᴊ ᴄʜᴧᴇɴ ɪ ɴᴀᴄʜɪɴᴀᴊ ᴇᴦᴏ ᴨᴏᴧɪᴩᴏʙᴀᴛь ᴄʙᴏɪʍɪ ᴦᴜʙᴀʍɪ ᴅᴏ ᴛᴀᴋᴏᴊ ᴄᴛᴇᴨᴇɴɪ ᴨᴏᴋᴀ ᴜ ᴛᴇʙʏᴀ ᴩᴏᴛ ɴᴇ ᴨᴏᴄɪɴᴇᴇᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴜ ᴄʜᴇᴩᴇᴨᴜɯᴋᴜ ᴅᴏ ᴛᴩᴇᴄᴋᴀ ᴅᴏʙᴇᴅᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴄʏɴ ɯᴧʏᴜʜɪ ᴛᴜᴨᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴩᴏʙᴏᴄɴᴀʙᴢʜᴇɴɪᴇ ᴛᴇʙᴇ ʜᴜᴇʍ ᴨᴇᴩᴇᴋᴩʏᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏᴇ ᴨᴩᴇᴅɴᴀɜɴᴀᴄʜᴇɴɪᴇ ϶ᴛᴏ ᴄᴏᴄᴀᴛь ʍᴏʏᴜ ʜᴜʏᴀᴩᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴢʜᴇ ᴛᴇʙʏᴀ ʙɴᴀᴛᴜᴩᴇ ʜᴜᴇʍ ʙᴏᴄᴨɪᴛᴀʏᴜ ᴋᴀᴋ ᴅᴇᴅ ᴨᴀᴧᴋᴏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ᴦᴧᴀɴᴅʏ ʜᴜᴇʍ ᴛᴜᴛ ʙᴜᴅᴜ ʙʏᴛᴀᴄᴋɪʙᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜ ᴛᴇʙʏᴀ ɴᴀ ʏᴀɜʏᴋᴇ ʍᴏᴊ ʜᴜᴊ ɴᴀᴩɪᴄᴏʙᴀᴧᴄʏᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙᴏʏᴜ ʍᴀᴛь ɜᴅᴇᴄь ʙᴜᴅᴜ ʜᴜᴇʍ ʙᴋᴀᴄʜɪʙᴀᴛь ᴋᴀᴋ ᴦᴏʙɴᴏʙᴏɜᴋᴜ ᴇʙᴀɴᴜʏᴜ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀᴧ ᴛʏᴀ ɴᴀᴢʜᴅᴀᴄʜᴋᴏᴊ ʙɴᴀᴛᴜᴩᴇ ɜᴅᴇᴄь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀɴɪᴦɪᴧɪᴩᴏʙᴀᴧ ᴛʙᴏʏᴜ ʍᴀᴛь ʜᴜᴇʍ ᴛᴜᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʏɴ ɯᴧʏᴜʜɪ ᴛʏ ɴᴇᴅᴇᴇᴄᴨᴏᴄᴏʙɴᴏᴊ ʏᴀ ᴛʙᴏᴇᴊ ʍᴀᴛᴇᴩɪ  sᴄʜᴀᴄ ʜᴜᴇʍ ʙᴜᴅᴜ ɜᴜʙʏ ʙʏʙɪʙᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ ʜᴜᴇᴄᴏᴄ ᴨᴏᴄᴧᴇᴅɴɪᴊ ʙ ᴅᴀɴɴᴏᴊ ᴋᴏɴɸᴇᴩᴇɴᴛsɪɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴢʜᴇ ᴛʙᴏʏᴜ ʍᴀᴛь ʙᴜᴅᴜ ᴄʙᴏɪʍ ʜᴜᴇʍ ᴨɪɜᴅɪᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ʙɴᴀᴛᴜᴩᴇ ᴄᴧʏɯɪɯь sᴄʜᴀᴄ ᴄᴋᴀᴧᴋᴏᴊ ʙᴜᴅᴇɯь ʙʏᴇʙᴀɴ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ sᴄʜᴀᴄ ɴᴀᴄʜɴᴜ ᴛᴇʙʏᴀ ʜᴜᴇʍ ᴨɪɜᴅɪᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴢʜᴇ ᴛᴇʙʏᴀ ᴄʙᴏɪʍ ʜᴜᴇʍ ᴛᴜᴛ ᴨᴩᴏᴩᴏᴅɪᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ʙᴜᴅᴜ ᴄʜᴧᴇɴᴏʍ ᴛᴜᴛ ʙ ᴜɯɪ ɸᴀᴋᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴜᴇᴛᴀ ᴛʏ ᴨᴏᴅɜᴀʙᴏᴩɴᴀʏᴀ ʙɴᴀᴛᴜᴩᴇ ᴨᴩɪɴɪʍᴀᴊᴄʏᴀ ʍᴏᴊ ʜᴜᴊ ᴄᴏᴄᴀᴛь[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴛsᴨᴇɯɴɪᴛsᴀ ᴇʙᴀɴᴀʏᴀ ᴄ 3 ᴨᴏᴅʙᴏᴩᴏᴅᴋᴀʍɪ ᴄᴧʏɯ ᴄᴏᴄɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴏᴩᴇɯᴀᴧ ᴛᴇʙʏᴀ ʜᴜᴇʍ ʙ ʍɪᴦ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ ᴛᴜᴀᴧᴇᴛ ᴛᴇʙʏᴀ ᴏᴋᴜɴᴀᴧ[ <emoji document_id=5334626127849724802>🤡</emoji> ] "
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʍᴏʏᴜ ᴄᴨᴇᴩʍᴜ ᴋᴀᴋ ᴄᴦᴜsᴄʜᴇɴᴋᴜ ᴢʜᴩᴇɯь[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴀʜ ʏᴀ ᴛᴇʙʏᴀ ʙьʏᴜ ᴀ ᴛᴇʙᴇ ɴᴩᴀʙɪᴛᴄʏᴀ ɴᴜ ᴛʏ ɪ ᴅᴀᴜɴ ᴇʙᴀɴʏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ᴨ᧐ʍᴩɪ ᴛᴜᴛ ʙ ᴨ᧐ᴛᴜᴦᴀʜ ᧐ᴄɪᴧɪᴛь ʍᴇɴʏᴀ ᴄᴧᴀʙ᧐ɴᴇᴩʙɴʏᴊ ᴇʙᴧ᧐ɪᴅ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ᴩʙᴜ ᴛᴇʙᴇ ᴀɴᴜᴄɴᴜʏᴜ ᴅʏᴩᴋᴜ ɪ ᴛʏ ʙᴜᴅᴇɯь ᴄᴛᴩᴀᴅᴀᴛь ʙᴄʏᴜ ᴄʙ᧐ʏᴜ ᴢʜɪᴢɴь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ɴɪsᴄʜɪᴊ ɴᴇ ʍ᧐ᴢʜᴇɯь ᴄᴇʙᴇ ᴨ᧐ᴢʙ᧐ᴧɪᴛь ᧐ᴛᴄ᧐ᴄᴀᴛь ʍ᧐ᴊ ʜᴜᴊ ᴀᴩᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ʙ ᴜᴄʏ ᴛʙ᧐ʏᴜ ᧐ᴅɴ᧐ʙᴩ᧐ʙᴜʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴀ ᴛʏ ᴛᴇᴩᴨᴇᴧ ɴᴀʙᴧʏᴜᴅᴀᴧ ᴢᴀ ϶ᴛɪʍ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴀʜ ʏᴀ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴜɴɪᴢʜᴀʏᴜ ᴀ ᴛᴇʙᴇ ɴᴩᴀʙɪᴛᴄʏᴀ ɴᴜ ɪ ᴅᴀᴧʙᴀᴇʙ ᴢʜᴇ ᴛʏ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨᴄɪɴᴀ ᴨ᧐ᴢ᧐ᴩɴᴀʏᴀ ɴᴇ ᴄᴅᴀʙᴀᴊᴄʏᴀ ʍ᧐ᴇʍᴜ ʜᴜʏᴜ ϶ᴛ᧐ ɴᴇᴨᴩɪᴧɪᴄʜɴ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴛᴇʙʏᴀ ᴄᴧɪᴢʏʙᴀᴛь ʙᴄʏᴜ ᴨʏᴧь ᴄ ᴨ᧐ᴧᴀ ᴛʏ ᴢʜᴇ ᴛᴩʏᴀᴨᴋᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴜᴜ ᴨ᧐ʍ᧐ᴊ ᴩ᧐ᴛ ᴛʏ ᴨ᧐ᴄᴧᴇ ᴄ᧐ᴄᴀɴɪʏᴀ ᴄʜᴧᴇɴ᧐ʙ ᴢʜᴜᴛᴋ᧐ ʙ᧐ɴʏᴀᴇɯь ᴛᴜᴨɪᴛsᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧᴜɯᴀᴊ ᴛᴇʙᴇ ɴᴀ ʜᴜᴊ ᴨᴩʏᴦᴀᴛь ɴᴇ ʙ ᴨᴩɪʙʏᴄʜᴋᴜ ᴛᴀᴋ ʍ᧐ᴢʜᴇᴛ ᴨᴩʏᴦɴᴇɯь ɴᴀ ʍ᧐ᴊ ᴩᴀᴢ᧐ᴋ? [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɴʙᴀᴧɪᴅ᧐᧐ʙᴩᴀᴢɴʏᴊ ᴛʏ ᴨɪᴢᴅ᧐ᴦᴩʏᴢ ʏᴀ ᴛᴇʙᴇ ᴦ᧐ʙ᧐ᴩʏᴜ ᴄ᧐ᴄɪ ʍ᧐ᴊ ᴄʜᴧᴇɴ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴋᴀᴧᴇᴋᴀ ᧐ʍᴇᴢʜɴᴀʏᴀ ʏᴀ ᴛᴇʙʏᴀ ɪᴢ᧐ʙьʏᴜ ᴋᴀᴋ ᴨᴄɪɴᴜ ᴨ᧐ᴄᴧᴇᴅɴʏᴜʏᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛsᴇᴧ᧐ᴊ ᴄᴛᴀᴇᴊ ᴄʙ᧐ɪʜ ʙ᧐ᴧᴋ᧐ʙ ᴛᴇʙᴇ ᴢʜ᧐ᴨᴜ ᧐ᴛъᴇʙᴀᴧ ᴀ ᴛʏ ᴄᴛᴇᴩᴨᴇᴧ ɴᴜ ᴋᴀᴋ ᧐ʙʏᴄʜɴ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ᴋ᧐ᴦᴅᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴧɪ ᴄʜᴛ᧐ ɴᴀ ᴢʜ᧐ᴨᴇ ɴᴀᴨɪᴄᴀᴧɪ ᴄᴧᴀʙɪɴᴀ ᴇʙᴀɴᴀʏᴀ?) [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ ᴩʏᴧᴜ ᴛʙ᧐ᴇʍᴜ ɴᴀᴄᴛᴜᴄʜᴜ ᴄʙ᧐ɪʍ ᴨᴇɴɪᴄ᧐ʍ ɴᴇ ᧐ʙɪᴢʜᴀᴊᴄʏᴀ ᴛ᧐ᴧьᴋ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴋ᧐ɴᴄʜᴀᴛь ᧐ᴛ ʍ᧐ᴇᴦ᧐ ʜᴜʏᴀ ᧐ɴᴀ ᴢʜᴇ ᴄᴧᴀʙᴀᴄʜᴋᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨᴩɪᴋɪɴь ᴅᴀᴢʜᴇ ᴅᴀᴦᴇᴄᴛᴀɴᴛsʏ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧɪ ᴀ ᴛʏ ᴛᴇᴩᴨᴇᴧ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴧʏᴀ ᴄ ᴛᴇʙʏᴀ ʙᴢʏᴀᴛь ᴛ᧐ᴧᴋ᧐ʍ ᴛ᧐ ɪ ɴᴇᴄʜᴇᴦ᧐ ᴛʏ ɴɴ ᴛᴀᴋ ᴇsᴄʜᴇ ɪ ʙ᧐ʍᴢʜᴀᴩᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙʏᴀ ᴄᴧ᧐ʍᴀʏᴜ ᴛᴜᴛ ᴄʏɴᴋᴀ ɯᴀᴧᴀʙʏ ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴄ᧐ᴄᴀᴛь ʍɴᴇ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ɯ᧐ ᴜ ᴛᴇʙʏᴀ ᴄ ᴨɪɴᴦ᧐ʍ ᴀʜᴀʜ ɴᴇ ᴨᴩ᧐ᴇʙɪ ʍɴᴇ ᴛ᧐ᴧьᴋ᧐ ᴀ ᴛ᧐ ʙ ᴩᴀʙᴄᴛʙ᧐ ᴢᴀʙᴇᴩᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ᴢʜ᧐ᴨᴀ ʍ᧐ʏᴀ ᴧɪᴄʜɴᴀʏᴀ ᴄ᧐ʙᴄᴛʙᴇɴɴ᧐ᴄᴛь ᴛʏ ᴨᴩɪᴋɪɴь ᴄ᧐ᴄᴜɴ᧐ᴋ ᴇʙᴀɴʏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ᴇᴊ ʍᴀᴛᴇᴩɪ ʙᴄᴇ ᴋᴀᴋɪᴇ ᴛ᧐ᴧьᴋ᧐ ʍ᧐ᴢʜɴ᧐ ᴅʏᴩᴋɪ ɪᴢьᴇʙᴀᴧ ᴀ ᴛʏ ɪ ᴅᴀᴧьɯᴇ ᴄʍ᧐ᴛᴩɪ ɴᴀ ϶ᴛ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴅᴩʏᴀʙᴧʏᴊ ᴄʏɴ᧐ᴋ ɯᴧʏᴜʜɪ ᴨ᧐ᴋᴀᴢʜɪ ʍɴᴇ ɴᴀᴄᴛ᧐ʏᴀsᴄʜɪᴊ ᴛᴩ᧐ᴧᴧɪɴᴦ! [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ʍᴀᴛь ɪᴄᴨʏᴛʏʙᴀᴇᴛ ᧐ᴩᴦᴀᴢʍ ᧐ᴛ ʍ᧐ᴇᴦ᧐ ʜᴜʏᴀ ʙᴇᴅь ᧐ɴᴀ ɴɪʍɸ᧐ʍᴀɴᴋᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴇsᴄʜᴇ ɴᴇ ᴄ᧐ʙᴄᴇʍ ᧐ᴋᴩᴇᴨ ᴅᴧʏᴀ ᴄʜʙᴀᴛᴋɪ ᴄ ʍ᧐ɪʍ ʜᴜᴇʍ ᴨ᧐ᴅᴄᴛɪᴧᴋᴀ ᴛʏ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨ᧐ᴅ ʍ᧐ᴊ ʜᴜᴊ ᴨ᧐ᴅᴄᴛɪᴧᴀᴇɯьᴄʏᴀ ᴨ᧐ᴅᴄ᧐ᴄ ᴢʜɪᴩɴʏᴊ ʏᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴄʜᴇᴦ᧐ ᴛʏ ɴᴇ ᴨ᧐ɴɪʍᴀᴇɯь ᴄʜᴛ᧐ ᴧɪ ᴄʜᴛ᧐ ʏᴀ ʙ ᴧʏᴜʙ᧐ʍ ᴄᴧᴜᴄʜᴀᴇ ɴᴇ ᴄᴅᴀʍᴄʏᴀ ᴄ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴋᴀ ɴᴀ ᴍᴏᴇᴍ ᴄʜʟᴇɴᴇ ᴘʀʏɢᴀᴇᴛ ᴋᴀᴋ ɴᴀ ʙᴀᴛᴜᴛᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴀᴠᴀᴊ sᴛʀɪᴘᴛɪᴢ sᴠᴏɪᴍ ʏᴀᴢʏᴄʜᴋᴏᴍ ᴛᴀɴᴛsᴜᴊ ɴᴀ ʜᴜᴇ ᴍᴏёᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙʟʏᴀᴅᴜɴьʏᴀ ᴛᴜᴘᴏɢᴏʟᴏᴠᴀʏᴀ ᴘᴏʀᴏᴅɪʟᴀ ᴛᴇʙʏᴀ ᴄʜᴇʀᴠʏᴀᴋᴀ ɴᴇᴍᴏsᴄʜɴᴏɢᴏ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴏᴊ ᴄʜʟᴇɴ ɪ ᴛᴠᴏɪ ᴅᴇsɴᴀ ᴜᴢʜᴇ sᴛᴀʟɪ ʟᴜᴄʜsʜɪᴍɪ ᴅʀᴜᴢьʏᴀᴍɪ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴜsᴏᴋ ɴᴇᴏᴅᴜsʜᴇᴠʟᴇɴɴᴏɢᴏ ᴋᴜsᴋᴀ sᴀʟᴀ ᴋᴜᴅᴀ ᴛᴇʙᴇ ᴅᴏ ᴍᴇɴʏᴀ?[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ sᴀᴛᴀɴɪᴄʜᴇsᴋɪᴇ ᴏʙʀʏᴀᴅʏ ᴜsᴛʀᴏʏᴜ ɴᴀ ᴅᴜsʜᴇ ᴍᴀᴍᴀsʜᴋɪ ᴛᴠᴏᴇᴊ ᴅᴜʀɪᴋ ᴇʙᴀɴʏᴊ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙʀᴏsɪʟᴀ ᴋᴜʀɪᴛь ʙʟᴀɢᴏᴅᴀʀʏᴀ ᴍɴᴇ ᴠ ᴍᴇsᴛᴏ ᴋᴜʀᴇᴠᴀ sᴏsᴇᴛ ᴍɴᴇ ᴄʜʟᴇɴ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ sᴏᴊᴅɪ s ᴜᴍᴀ ᴏᴛ ɴᴀᴘᴏʀᴀ ᴄʜʟᴇɴᴏᴠ ɴɪᴄʜᴛᴏᴢʜᴇsᴛᴠᴏ ᴇʙᴀɴᴏᴇ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴀʜ ᴄᴜᴋᴀ ʏᴀ ᴛᴇʙʏᴀ ᴨ᧐ᴩʙᴜ ɪɴʙᴀᴧɪᴅᴀ ᴇʙᴀɴ᧐ᴦ᧐ ᴛᴇᴩᴨɪ ʍᴇɴʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ᴇ ᴨɪᴢᴅᴀᴧɪsᴄʜᴇ ᴢᴅᴇᴄь ᴩʙᴀᴛь ʙᴜᴅᴜ ᴄʏɴ ᴇʙᴀɴ᧐ᴊ ᴋᴧᴜɯɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴀᴢ᧐ᴩʙᴇʍ ᴛᴇʙᴇ ᴛᴜᴛ ᴀɴᴜᴄ ᴛᴜᴨ᧐ᴊ ᴄʏɴ ᴄɪɸ᧐ᴢɴ᧐ᴊ ɯᴀᴧᴀʙʏ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴋᴀᴋ ᴨᴀᴜᴋ ʙ ᴀɴᴜᴄ ᴇʙᴀᴧ ᧐ɴᴀ ᴅ᧐ʙ᧐ᴧьɴᴀ sᴄʜᴀᴄ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙ᧐ʍᴢʜᴀᴩᴀ ᴛᴜᴛ ɴᴀ ᴋ᧐ᴨᴇᴊᴋɪ ᴨ᧐ᴄᴧᴇ ᧐ᴛᴄ᧐ᴄᴀ ʙʏᴢʜɪᴛь ɴᴇ ᴄʍ᧐ᴢʜᴇɯь ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧ᧐ʍᴀʏᴜ ᴛᴇʙᴇ ᴇʙᴀᴧьɴɪᴋ ᴄʙ᧐ɪʍ ʜᴜᴇʍ ɪ ɴᴇ ʙ᧐ᴢᴩᴀᴢʜᴀᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙʏᴩʙᴜ ʙᴄᴇ ᴛʙ᧐ɪ ᴋ᧐ᴄᴛɪ ɪᴢ ᴛʙ᧐ᴇᴦ᧐ ɪ ᴛᴀᴋ ʜɪᴧ᧐ᴦ᧐ ᴛᴇᴧьᴛsᴀ ᴅᴀᴧʙᴀᴇʙ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙᴇ ᴅᴀᴧʙᴀᴇʙᴜ ᴄᴋᴀᴢᴀᴧ ᴄ᧐ᴄᴀᴛь ʍɴᴇ ɪ ᴄʜᴇ ᴛʏ ᴅᴇᴧᴀᴇɯь ᴋᴀᴧᴇᴋᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴅᴧʏᴀ ᴛʙ᧐ᴇᴊ ᴇʙᴀɴ᧐ᴊ ʍᴀᴩᴛʏɯьᴇᴊ ᴄᴇʍьɪ ᴨ᧐ʙᴇᴧɪᴛᴇᴧь ɴᴀʜᴜᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ʍᴀᴛь ᴄʙɪɴьʏᴀ ᴇʙᴀɴᴀʏᴀ ʏᴀ ᴇᴇ ʙ ʍʏᴀᴄ᧐ᴋ᧐ʍʙɪɴᴀᴛ ᴄᴅᴀʍ  [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɯ᧐ ᴛʏ ʍᴇɴʏᴀ ʙ᧐ɪɯьᴄʏᴀ ᴛ᧐ ʏᴀ ʙᴄᴇᴦ᧐ ᴧɪɯь ᴛᴇʙʏᴀ ɴᴀ ᧐ᴩᴦᴀɴʏ ᴄᴅᴀʍ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɴɸᴀɴᴛɪᴧьɴᴀʏᴀ ɯᴧʏᴜʜᴀ ᴛʙ᧐ʏᴀ ʍᴀᴛь ʙᴄᴇᴦᴅᴀ ᴄ᧐ᴦᴧᴀɯᴀᴇᴛᴄʏᴀ ɴᴀ ᴨᴩᴇᴅᴧ᧐ᴢʜᴇɴɪᴇ ᴄᴇᴋᴄᴀ ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄ᧐ᴄɪ ʍɴᴇ ᴛᴜᴛ ʙᴇᴅь ϶ᴛ᧐ ɴᴇ ᴋᴀᴢʜᴅ᧐ʍᴜ ᴅᴀɴ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴩᴜᴋᴀᴢʜ᧐ᴨ ᴇʙᴀɴʏᴊ ᴛʏ ᴋᴀᴋ ᴄʙ᧐ᴊ ʙᴧʏᴀᴅᴄᴋɪᴊ ʍ᧐ᴅᴜᴧь ᴨɪᴄᴀᴧ ᴜ ᴛᴇʙʏᴀ ʜᴜᴊɴʏᴀ ʙʏɯᴧᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᧐ᴄᴛᴀʙᴧʏᴜ ᴛᴇʙʏᴀ ʜᴜᴇᴄ᧐ᴄᴀ ᧐ʙᴩʏᴦᴀɴɴ᧐ᴦ᧐ ʙᴇᴢ ᴩ᧐ᴅɪᴛᴇᴧᴇᴊ ɪ ɴᴇ ᴨᴧᴀᴄʜь ᴨ᧐ᴛ᧐ʍ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ʏᴜ ɸᴀɴᴛᴀᴢɪʏᴜ ɴᴀ ʜᴜᴇ ʙᴇᴩᴛᴇᴧ ᴀ ᴋᴄᴛᴀᴛɪ ᴄʜ᧐ ᴨᴀᴨᴇ ʙ ᴅɪᴋ ᴄᴋᴀᴢʜᴇɯь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴜᴜ ᧐ᴛ ᴛᴇʙʏᴀ ᴨᴀʜɴᴇᴛ ᴅᴀᴧʙᴀᴇʙɪᴢʍ᧐ʍ ɪᴅɪ ɴᴇ ᴢɴᴀʏᴜ ᴧᴜᴄʜɯᴇ ᴄʜᴧᴇɴʏ ᴨ᧐ᴄᴀᴄɪ ɴᴇᴢʜᴇᴧɪ ᴄ᧐ ʍɴ᧐ᴊ ᴛᴩ᧐ᴧᴧɪᴛᴄʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧᴀʙ᧐ᴜʍɴʏᴊ ʜᴜᴇᴄ᧐ᴄ ᴛʏ ᴅ᧐ᴧᴢʜᴇɴ ᧐ᴄ᧐ᴢɴᴀᴛь ᴄʜᴛ᧐ ᴛʏ ɴᴇ ᧐ᴄɪᴧɪɯь ʍᴇɴʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙʏʙᴇᴩɴᴜ ᴛʙ᧐ɪ ᴄᴜᴄᴛᴀʙʏ ɴᴀ ᧐ʙᴩᴀᴛɴᴜʏᴜ ᴄᴛ᧐ᴩ᧐ɴᴜ ɪ ᴨ᧐ᴛ᧐ʍ ɴᴇ ᴨᴧᴀᴄʜь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʏɴ ᴜᴢᴋ᧐ᴦᴧᴀᴢ᧐ᴊ ᴀᴩʍʏᴀɴᴋɪ ᴛᴜᴛ ᴨ᧐ʙɪɴᴜᴊᴄʏᴀ ʜᴜʏᴜ ʍ᧐ᴇʍᴜ ᴋᴀᴋ ᴩᴀʙʏɴʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ɪ ᴋᴩᴀᴛᴋ᧐ᴄᴛᴩ᧐ᴄʜɴʏᴇ ɯᴀʙᴧ᧐ɴᴄʜɪᴋɪ ʙ ᴩ᧐ᴛ ᴇʙᴀᴧ ᴋᴀᴋ ɪ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇᴩᴨɪᴧɪᴢ᧐ʙᴀɴɴʏᴊ ᴅᴇᴩьʍ᧐ᴇᴅ ɴᴇ ᴜᴨᴀᴅɪ ᧐ᴛ ᴨ᧐ᴛᴇᴩɪ ᴄɪᴧ ᴨᴩ᧐ᴛɪʙ ʍᴇɴʏᴀ ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴜ ʙɴᴀᴛᴜᴩᴇ ᴛᴇʙᴇ ʍᴀᴛь ᴄʜᴧᴇɴ᧐ʍ ɪᴢʙɪᴧ ᧐ɴᴀ ᴨᴧᴀᴄʜᴇᴛ ʜ᧐ᴅɪᴛ ᴅᴜᴩᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ᴋᴀᴢʜɪ ʍɴᴇ ᴅ᧐ᴄᴛ᧐ᴊɴʏᴊ ᴛᴩ᧐ᴧᴧɪɴᴦ ᴛʏ ᴄʏɴ ᴇʙᴀɴ᧐ᴊ ᴧʏᴀʙᴩʏ ᴨ᧐ᴇʙᴜ ᴛᴇʙʏᴀ ᴄᴧᴀʙ᧐ᴦ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴜᴛ ᴋᴀᴋ ʙ᧐ᴧᴋ ʙ ᧐ᴅɪɴ᧐ᴄʜᴋᴜ ᴛʙ᧐ʏᴜ ᴄᴇʍьʏᴜ ᴇʙᴀɯᴜ ɪ ᴋᴄᴛᴀᴛɪ ᴢᴀᴇʙɪᴄь ᴨ᧐ᴧᴜᴄʜᴀᴇᴛᴄʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴜ ᴛʏ ʍɴᴇ ᧐ᴛᴄ᧐ᴄɪ ᴧᴜᴄʜɯᴇ ᴄʜᴇʍ ɴᴀ ʜᴜʏᴀʜ ᴄʜᴜᴢʜɪʜ ᴨᴩʏᴦᴀᴛь ᴨ᧐ɴʏᴀᴧ ʍᴇɴʏᴀ  [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴋᴀᴋ ᴅᴩᴀᴋ᧐ɴ ᴛᴇʙʏᴀ ᴇʙᴀɯᴜ ᴛᴜᴛ ᴛᴜᴨ᧐ᴦ᧐ᴧ᧐ʙ᧐ᴦ᧐ ᴨᴀᴄʏɴᴋᴀ ᴅʙᴜʜ ᴄʜᴧᴇɴ᧐ʙ ɪ ᴨɪʙᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢɴᴀᴇɯь ᴋᴀᴋ ᴛʏ ᴨ᧐ʏᴀʙɪᴧᴄʏᴀ? ᴛʙ᧐ᴊ ʙᴀᴛʏᴀ ᴋ᧐ɴᴄʜɪᴧ ɴᴀ ᴅɪʙᴀɴ ᴀ ᴨ᧐ᴛ᧐ʍ ᴨᴩ᧐ᴧɪᴧ ᴨɪʙ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ʍᴀᴛь ᴨᴩ᧐ᴄᴛ᧐ ᴨᴇᴩɴᴜᴧᴀ ᴀ ᴛᴀʍ ɪ ᴛʏ ʙʏᴧᴇᴢ ᴋᴀᴋ᧐ᴦ᧐ ᴛ᧐ ʜᴜʏᴀ ʍʏ ʙᴄᴇ ʙ ᴀʜᴜʏᴀʜ ʙʏᴧɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴋ᧐ᴦᴅᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ɴ᧐ᴄ ᴢᴀᴋᴩʏʙᴀᴧ ᴄʜᴛ᧐ʙ ᴢᴀᴨᴀʜ ᴇᴇ ʙᴧᴀᴦᴀᴧɪsᴄʜᴀ ɴᴇ ᴄʜᴜʙᴄᴛʙ᧐ʙᴀᴛь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄʜᴇᴩᴇᴢ ᴧᴇᴛ 15 ᴛʏ ʍɴᴇ ʙᴄᴇ ᴩᴀʙɴ᧐ ʙᴜᴅᴇɯь ᴄʜᴧᴇɴ ɴᴀᴅᴩᴀᴄʜɪʙᴀᴛь ᴛᴇᴩᴨɪᴧᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ʙɪɴᴜᴊᴄʏᴀ ʍ᧐ᴇʍᴜ ʜᴜʏᴜ ᴇᴄᴧɪ ᴛʏ ɴᴇ ᴛᴇᴧᴋᴀ ᴄᴧᴀʙᴀʏᴀ ɪʙ᧐ ʏᴀ ᴛᴇʙʏᴀ ᴜᴦᴀɴᴅ᧐ɯᴜ ᴄᴧᴀʙᴀᴋᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨᴇᴩᴇᴛᴩᴀʜᴀɴɴʏᴊ ᴄᴧᴀʙᴀᴋ ɴᴇ ᴛᴇᴩᴨɪ ʍ᧐ɪ ʜᴀᴩᴄʜᴋɪ ʙ ᴄʙ᧐ᴇ ᴋᴩɪʙ᧐ᴇʙᴧ᧐ᴇ ᴩʏᴧ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛᴇʙᴇ ᴨ᧐ᴩᴀ ʙ᧐ᴢʙᴩᴀsᴄʜᴀᴛьᴄʏᴀ ɴᴀ ᴜᴧɪᴛsᴜ ᴀ ᴛ᧐ ᴄʜᴛ᧐ ᴛ᧐ ᴅ᧐ᴧᴦ᧐ ᴛʏ ɴᴀ ʍ᧐ᴇʍ ʜᴜᴇ ᴄɪᴅɪɯь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀʙᴇᴊ ʏᴀ ɴᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴢʜɪᴩɴᴜʏᴜ ᴋ᧐ɴᴄʜᴀᴧ ᴧɪᴛᴩᴀʍɪ ᴄᴨᴇᴩʍʏ ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ʙᴋᴀᴄʜᴀᴧ ᴄᴨᴇᴩʍᴜ ʙ ᴨɪᴢᴅᴀᴧɪsᴄʜᴇ ᴛʙ᧐ᴇᴊ ᴜᴄᴀᴛ᧐ᴊ ʍᴀᴛᴇᴩɪ ᴋᴄᴛᴀᴛɪ ᴨ᧐ᴄʜᴇʍᴜ ᧐ɴᴀ ᴜᴄʏ ɴᴇ ʙᴩᴇᴇᴛ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴜᴇᴛь ʏᴀ ᴀʜᴜᴇᴧ ᴋ᧐ᴦᴅᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴜ ɴᴇᴇ ɴᴀ ᴨɪᴢᴅᴇ ᴅᴢʜᴜɴᴦᴧɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴄʙ᧐ɪʍ ʜᴜᴇʍ ᴛᴀᴩᴢᴀɴᴋɪ ɴᴀ ᴨɪᴢᴅᴇ ᴛʙ᧐ᴇᴊ ʍᴀᴛᴇᴩɪ ᧐ʙᴩᴜʙᴀᴧ ɴᴜ ᴄʜᴛ᧐ ᴢᴀ ᴅᴇᴧᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴧʏᴀᴛь ᴜ ᴛᴇʙʏᴀ ʙɴᴀᴛᴜᴩᴇ ɴᴀ ᴢʜ᧐ᴨᴇ ɪᴢ ʙ᧐ᴧ᧐ᴄ ʍ᧐ᴢʜɴ᧐ ᴧɪᴀɴʏ ᴅᴇᴧᴀᴛь ɪᴧɪ ᴋ᧐ᴄɪᴄʜᴋɪ ᴢᴀᴨᴧᴇᴛᴀᴛь ᴨ᧐ʙᴩᴇᴊᴄʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪᴢ ᴛʙ᧐ᴇᴦ᧐ ᧐ᴄʜᴋᴀ ʍ᧐ᴢʜɴ᧐ ᴄᴅᴇᴧᴀᴛь ᴨᴩᴇᴋᴩᴀᴄɴᴜʏᴜ ʍɪɯᴇɴь ᴅᴧʏᴀ ʍᴇᴛᴀɴɪʏᴀ ᴅɪᴧᴅᴀᴋᴀʍɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ ʍɴᴇ ᴄʜᴧᴇɴ ᧐ᴛᴄᴀᴄʏʙᴀᴇɯь ᴋᴀᴋ ɴɪᴋ᧐ᴧᴀ ᴛᴇᴄᴧᴀ ᴀᴩᴜ ᴄᴀᴄɪᴩᴜᴊ  [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧᴜɯᴀᴊ ʙ᧐ᴛ ɪᴢ ᴢᴀ ᴛᴇʙʏᴀ ᴨ᧐ʏᴀʙɪᴧᴄʏᴀ ᴛᴀᴋ᧐ᴊ ʙɪᴅ ᴧʏᴜᴅᴇᴊ ᴋᴀᴋ ᴄʜᴧᴇɴ᧐ʏᴀᴅɴʏᴊ ᴀʜᴀʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴇʙᴀɴʏᴊ sʏɴ ʙʟʏᴀᴅɪɴʏ ᴢᴀᴛᴋɴɪ sᴠᴏᴇ ᴋᴏsᴏʀʏʟᴏᴇ ᴇʙʟᴇᴛsᴏ ᴘᴏᴋᴀ ʏᴀ ɴᴇ ɴᴀᴄʜᴀʟ ᴛᴇʙᴇ ᴠ ᴅᴇsɴʏ sᴠᴏᴊ ʜᴜᴊ ᴘɪʜᴀᴛь ᴅᴏʟʙᴏᴇʙ ᴇʙᴜᴄʜɪᴊ ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴜ ᴛᴠᴏᴇᴊ sᴠɪɴᴏᴍᴀᴛᴜʜɪ ᴍᴇsʏᴀᴄʜɴʏᴇ ᴛʏ sʟɪᴢᴜᴇsʜь ɪʜ sᴠᴏɪᴍ ʀᴛᴏᴍ ᴇʙᴀɴʏᴍ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ", 
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴍᴀʟᴏᴍᴇʀɴʏᴊ sʏɴ sᴠɪɴᴏsᴏʙᴀᴋɪ ʏᴀ ᴛᴇʙᴇ ᴛᴜᴛ ᴛᴠᴏɪ ᴋᴏsᴛɪ ᴠ ᴘᴏʀᴏsʜᴏᴋ sᴏᴛʀᴜ ʟᴏʜ ᴇʙᴀɴʏᴊ sᴜᴋᴀ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ sʜʟʏᴜʜᴀᴏʙʀᴀᴢɴʏᴊ sʏɴ ᴍᴀʟᴏᴍᴇʀɴᴏᴊ ᴘʀᴏʙʟʏᴀᴅᴇɴᴋɪ ʏᴀ ᴛᴠᴏɪ ᴍᴏᴢɢɪ ᴘᴏ ᴠsᴇᴊ ᴋғ ʀᴀssᴛᴀsᴋɪᴠᴀʟ ᴅᴏʟʙᴏᴇʙɪɴᴀ ᴛʏ ᴇʙᴀɴʏᴊ sᴜᴋᴀ ᴛʏ ᴢʜᴇ ᴅᴀᴢʜᴇ ɴᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ sᴀᴍʏᴊ ᴏɢʀᴏᴍɴʏᴊ ᴘᴇɴɪs ᴀ ɪᴍᴇɴɴᴏ ᴍᴏᴊ sᴄʜᴀs ᴜ ᴛᴇʙʏᴀ ᴠᴏ ʀᴛᴜ ᴋʟᴏᴜɴ? [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴀʜ ʏᴀ ᴛᴇʙʏᴀ ʙьʏᴜ ᴀ ᴛᴇʙᴇ ɴᴩᴀʙɪᴛᴄʏᴀ ɴᴜ ᴛʏ ɪ ᴅᴀᴜɴ ᴇʙᴀɴʏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇ ᴨ᧐ʍᴩɪ ᴛᴜᴛ ʙ ᴨ᧐ᴛᴜᴦᴀʜ ᧐ᴄɪᴧɪᴛь ʍᴇɴʏᴀ ᴄᴧᴀʙ᧐ɴᴇᴩʙɴʏᴊ ᴇʙᴧ᧐ɪᴅ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ᴩʙᴜ ᴛᴇʙᴇ ᴀɴᴜᴄɴᴜʏᴜ ᴅʏᴩᴋᴜ ɪ ᴛʏ ʙᴜᴅᴇɯь ᴄᴛᴩᴀᴅᴀᴛь ʙᴄʏᴜ ᴄʙ᧐ʏᴜ ᴢʜɪᴢɴь [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ɴɪsᴄʜɪᴊ ɴᴇ ʍ᧐ᴢʜᴇɯь ᴄᴇʙᴇ ᴨ᧐ᴢʙ᧐ᴧɪᴛь ᧐ᴛᴄ᧐ᴄᴀᴛь ʍ᧐ᴊ ʜᴜᴊ ᴀᴩᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ʙ ᴜᴄʏ ᴛʙ᧐ʏᴜ ᧐ᴅɴ᧐ʙᴩ᧐ʙᴜʏᴜ ʍᴀᴛь ᴇʙᴀᴧ ᴀ ᴛʏ ᴛᴇᴩᴨᴇᴧ ɴᴀʙᴧʏᴜᴅᴀᴧ ᴢᴀ ϶ᴛɪʍ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀʜᴀʜ ʏᴀ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴜɴɪᴢʜᴀʏᴜ ᴀ ᴛᴇʙᴇ ɴᴩᴀʙɪᴛᴄʏᴀ ɴᴜ ɪ ᴅᴀᴧʙᴀᴇʙ ᴢʜᴇ ᴛʏ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨᴄɪɴᴀ ᴨ᧐ᴢ᧐ᴩɴᴀʏᴀ ɴᴇ ᴄᴅᴀʙᴀᴊᴄʏᴀ ʍ᧐ᴇʍᴜ ʜᴜʏᴜ ϶ᴛ᧐ ɴᴇᴨᴩɪᴧɪᴄʜɴ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴛᴇʙʏᴀ ᴄᴧɪᴢʏʙᴀᴛь ʙᴄʏᴜ ᴨʏᴧь ᴄ ᴨ᧐ᴧᴀ ᴛʏ ᴢʜᴇ ᴛᴩʏᴀᴨᴋᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɸᴜᴜ ᴨ᧐ʍ᧐ᴊ ᴩ᧐ᴛ ᴛʏ ᴨ᧐ᴄᴧᴇ ᴄ᧐ᴄᴀɴɪʏᴀ ᴄʜᴧᴇɴ᧐ʙ ᴢʜᴜᴛᴋ᧐ ʙ᧐ɴʏᴀᴇɯь ᴛᴜᴨɪᴛsᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴄᴧᴜɯᴀᴊ ᴛᴇʙᴇ ɴᴀ ʜᴜᴊ ᴨᴩʏᴦᴀᴛь ɴᴇ ʙ ᴨᴩɪʙʏᴄʜᴋᴜ ᴛᴀᴋ ʍ᧐ᴢʜᴇᴛ ᴨᴩʏᴦɴᴇɯь ɴᴀ ʍ᧐ᴊ ᴩᴀᴢ᧐ᴋ? [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪɴʙᴀᴧɪᴅ᧐᧐ʙᴩᴀᴢɴʏᴊ ᴛʏ ᴨɪᴢᴅ᧐ᴦᴩʏᴢ ʏᴀ ᴛᴇʙᴇ ᴦ᧐ʙ᧐ᴩʏᴜ ᴄ᧐ᴄɪ ʍ᧐ᴊ ᴄʜᴧᴇɴ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴋᴀᴧᴇᴋᴀ ᧐ʍᴇᴢʜɴᴀʏᴀ ʏᴀ ᴛᴇʙʏᴀ ɪᴢ᧐ʙьʏᴜ ᴋᴀᴋ ᴨᴄɪɴᴜ ᴨ᧐ᴄᴧᴇᴅɴʏᴜʏᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛsᴇᴧ᧐ᴊ ᴄᴛᴀᴇᴊ ᴄʙ᧐ɪʜ ʙ᧐ᴧᴋ᧐ʙ ᴛᴇʙᴇ ᴢʜ᧐ᴨᴜ ᧐ᴛъᴇʙᴀᴧ ᴀ ᴛʏ ᴄᴛᴇᴩᴨᴇᴧ ɴᴜ ᴋᴀᴋ ᧐ʙʏᴄʜɴ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ᴋ᧐ᴦᴅᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴧɪ ᴄʜᴛ᧐ ɴᴀ ᴢʜ᧐ᴨᴇ ɴᴀᴨɪᴄᴀᴧɪ ᴄᴧᴀʙɪɴᴀ ᴇʙᴀɴᴀʏᴀ?) [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴨ᧐ ᴩʏᴧᴜ ᴛʙ᧐ᴇʍᴜ ɴᴀᴄᴛᴜᴄʜᴜ ᴄʙ᧐ɪʍ ᴨᴇɴɪᴄ᧐ʍ ɴᴇ ᧐ʙɪᴢʜᴀᴊᴄʏᴀ ᴛ᧐ᴧьᴋ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴋ᧐ɴᴄʜᴀᴛь ᧐ᴛ ʍ᧐ᴇᴦ᧐ ʜᴜʏᴀ ᧐ɴᴀ ᴢʜᴇ ᴄᴧᴀʙᴀᴄʜᴋᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨᴩɪᴋɪɴь ᴅᴀᴢʜᴇ ᴅᴀᴦᴇᴄᴛᴀɴᴛsʏ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧɪ ᴀ ᴛʏ ᴛᴇᴩᴨᴇᴧ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʙᴧʏᴀ ᴄ ᴛᴇʙʏᴀ ʙᴢʏᴀᴛь ᴛ᧐ᴧᴋ᧐ʍ ᴛ᧐ ɪ ɴᴇᴄʜᴇᴦ᧐ ᴛʏ ɴɴ ᴛᴀᴋ ᴇsᴄʜᴇ ɪ ʙ᧐ʍᴢʜᴀᴩᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛᴇʙʏᴀ ᴄᴧ᧐ʍᴀʏᴜ ᴛᴜᴛ ᴄʏɴᴋᴀ ɯᴀᴧᴀʙʏ ᴢᴀᴄᴛᴀʙᴧʏᴜ ᴄ᧐ᴄᴀᴛь ʍɴᴇ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴀ ɯ᧐ ᴜ ᴛᴇʙʏᴀ ᴄ ᴨɪɴᴦ᧐ʍ ᴀʜᴀʜ ɴᴇ ᴨᴩ᧐ᴇʙɪ ʍɴᴇ ᴛ᧐ᴧьᴋ᧐ ᴀ ᴛ᧐ ʙ ᴩᴀʙᴄᴛʙ᧐ ᴢᴀʙᴇᴩᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ᴢʜ᧐ᴨᴀ ʍ᧐ʏᴀ ᴧɪᴄʜɴᴀʏᴀ ᴄ᧐ʙᴄᴛʙᴇɴɴ᧐ᴄᴛь ᴛʏ ᴨᴩɪᴋɪɴь ᴄ᧐ᴄᴜɴ᧐ᴋ ᴇʙᴀɴʏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴛʙ᧐ᴇᴊ ʍᴀᴛᴇᴩɪ ʙᴄᴇ ᴋᴀᴋɪᴇ ᴛ᧐ᴧьᴋ᧐ ʍ᧐ᴢʜɴ᧐ ᴅʏᴩᴋɪ ɪᴢьᴇʙᴀᴧ ᴀ ᴛʏ ɪ ᴅᴀᴧьɯᴇ ᴄʍ᧐ᴛᴩɪ ɴᴀ ϶ᴛ᧐ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴅᴩʏᴀʙᴧʏᴊ ᴄʏɴ᧐ᴋ ɯᴧʏᴜʜɪ ᴨ᧐ᴋᴀᴢʜɪ ʍɴᴇ ɴᴀᴄᴛ᧐ʏᴀsᴄʜɪᴊ ᴛᴩ᧐ᴧᴧɪɴᴦ! [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʙ᧐ʏᴀ ʍᴀᴛь ɪᴄᴨʏᴛʏʙᴀᴇᴛ ᧐ᴩᴦᴀᴢʍ ᧐ᴛ ʍ᧐ᴇᴦ᧐ ʜᴜʏᴀ ʙᴇᴅь ᧐ɴᴀ ɴɪʍɸ᧐ʍᴀɴᴋᴀ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴇsᴄʜᴇ ɴᴇ ᴄ᧐ʙᴄᴇʍ ᧐ᴋᴩᴇᴨ ᴅᴧʏᴀ ᴄʜʙᴀᴛᴋɪ ᴄ ʍ᧐ɪʍ ʜᴜᴇʍ ᴨ᧐ᴅᴄᴛɪᴧᴋᴀ ᴛʏ ᴇʙᴀɴᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴨ᧐ᴅ ʍ᧐ᴊ ʜᴜᴊ ᴨ᧐ᴅᴄᴛɪᴧᴀᴇɯьᴄʏᴀ ᴨ᧐ᴅᴄ᧐ᴄ ᴢʜɪᴩɴʏᴊ ʏᴀ ᴛʙ᧐ʏᴜ ʍᴀᴛь ᴇʙᴀᴧ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴜ ᴄʜᴇᴦ᧐ ᴛʏ ɴᴇ ᴨ᧐ɴɪʍᴀᴇɯь ᴄʜᴛ᧐ ᴧɪ ᴄʜᴛ᧐ ʏᴀ ʙ ᴧʏᴜʙ᧐ʍ ᴄᴧᴜᴄʜᴀᴇ ɴᴇ ᴄᴅᴀʍᴄʏᴀ ᴅᴜʀᴀᴋ ᴇʙᴀɴʏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴢɴᴀᴇsʜь ᴛᴠᴏʏᴀ ᴍᴀᴍᴜʟьᴋᴀ sʜʟʏᴜʜᴀ ɴᴀᴋɪɴᴜʟᴀsь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ʙᴜᴅᴛᴏ ᴇᴊ ᴛᴀᴍ ᴍёᴅᴏᴍ ɴᴀᴍᴀᴢᴀɴᴏ ʏᴀ ᴇᴊ ᴋᴏɴᴇᴄʜɴᴏ ᴛʀᴇsɴᴜʟ ᴘᴏ ᴇʙᴀʟьɴɪᴋᴜ ᴄʜʟᴇɴᴏᴍ ᴛᴀᴋ ᴄʜᴛᴏ ᴇᴇ ɢᴜʙʏ ᴀᴢʜ ᴘᴏsɪɴᴇʟɪ, ɴᴏ ᴏɴᴀ ᴠsᴇ ʀᴀᴠɴᴏ ᴘᴏʙᴏʀᴏʟᴀ ᴍᴏᴊ ᴄʜʟᴇɴ ɪ ɴᴀᴄʜᴀʟᴀ ᴛʀᴀʜᴀᴛь ᴇɢᴏ sᴠᴏɪᴍ ʀʏʟᴏᴍ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴅɴᴀᴢʜᴅʏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴢᴀʜᴏᴛᴇʟᴀ ᴋᴀᴋ ᴏʙʏᴄʜɴᴏ ᴅᴇsᴇʀᴛᴀ ɴᴀ ᴜᴢʜɪɴ ᴠᴠɪᴅᴇ ᴍᴏᴇᴊ sᴘᴇʀᴍʏ, ɴᴏ ʏᴀ ᴇᴊ ᴘʀᴏsᴛᴏ-ɴᴀᴘʀᴏsᴛᴏ ᴠʟɪʟ ᴋɪsʟᴏᴛᴜ ᴠ ᴇᴇ ɢʟᴏᴛᴋᴜ, ᴅᴏ sɪʜ ᴘᴏʀ ʟᴇᴢʜɪᴛ ᴛᴀᴍ ʀᴀssᴛᴀᴠʟʏᴀᴇᴛsʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴀ ᴄʜᴛᴏ ᴛʏ ᴛᴜᴛ sɪᴅɪsʜь sʏɴ sʜʟʏᴜʜɪ ᴛᴜᴘᴏɢᴏʟᴏᴠᴏᴊ, ᴍɴᴇ ᴢʜᴇ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ʙʟʏᴀᴅɪɴᴀ ʜᴜᴊ ᴢᴀ ᴛᴠᴏᴇᴊ ᴢʜᴇ sʜᴋᴏʟᴏᴊ sᴏsᴀʟᴀ ᴘᴏᴋᴀ ᴛʏ ɴᴀ ɪsᴛᴏʀɪɪ ᴜ ᴅᴏsᴋɪ ᴏᴛᴠᴇᴄʜᴀʟ ɴɪ ᴏ ᴄʜᴇᴍ ɴᴇ ᴘᴏᴅᴏᴢʀᴇᴠᴀʏᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍɴᴇ ᴘʀɪᴊᴅᴇᴛьsʏᴀ ɢᴏʟᴏᴠᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴜᴛɪʟɪᴢɪʀᴏᴠᴀᴛь ɴᴀ ʟᴇsɴᴏᴍ ᴋᴏsᴛʀᴇ ᴅʟʏᴀ ᴘʀᴏᴠᴇᴅᴇɴɪᴇ ᴏᴛʀʏᴀᴅᴀ ɪᴢɢɴᴀɴɪʏᴀ sʜʟʏᴜsʜёᴊ ɴᴀᴛᴜʀʏ ɪᴢ ᴠᴀsʜᴇᴊ ᴇʙʟɪᴠᴏᴊ sᴇᴍᴇᴊᴋɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ ᴋᴀᴋ ɴᴇᴊʀᴏʜɪʀᴜʀɢ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʜᴏᴄʜᴜ ᴛᴇʙᴇ s ᴜᴠᴇʀᴇɴɴᴏsᴛьʏᴜ ᴢᴀʏᴀᴠɪᴛь ᴄʜᴛᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏʟɴʏᴊ ᴘɪᴢᴅᴇᴛs, ʏᴀ ᴇᴇ ʙᴏsʜᴋᴜ ᴋ ʜᴜʏᴀᴍ ᴏᴛᴘɪʟɪʟ ɪ ᴋ sᴇʙᴇ ɴᴀ ᴄʜʟᴇɴʏᴀʀᴜ ɴᴀᴋʀᴜᴛɪʟ ᴋᴀᴋ sᴀᴍᴏʀᴇᴢ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] sʏɴᴜʟʏᴀ sʜʟʏᴜʜɪ ᴅᴀᴢʜᴇ ɴᴇ ᴅᴜᴍᴀᴊ ᴛᴜᴛ ᴘᴏᴛᴜʜɴᴜᴛь ʏᴀ ᴢʜᴇ ᴠsᴇ ʀᴀᴠɴᴏ ᴛᴠᴏᴇ ᴋʟᴇᴊᴍᴏ ᴜʀᴏᴅʟɪᴠᴏɢᴏ  sʏɴᴋᴀ sʜʟʏᴜʜɪ ᴘᴏ ᴠsᴇᴍᴜ ᴛᴇʟᴇɢʀᴀᴍᴍᴜ ʀᴀsᴛᴀsᴋᴀʏᴜ ɪ ʙᴜᴅᴜ sᴍᴏᴛʀᴇᴛь ᴋᴀᴋ ᴛʏ ᴏᴛ ᴘᴏᴢᴏʀᴀ ᴠ ᴢᴇᴍʟʏᴜ ᴘʀᴏᴠᴀʟɪᴠᴀᴇsʜьsʏᴀ  [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴀ ᴏʜᴏᴛᴇ sʟᴜᴄʜᴀᴊɴᴏ ᴘᴇʀᴇᴘᴜᴛᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ʟᴇsᴜ s ᴛᴜsʜᴏᴊ ᴋᴀʙᴀɴᴀ ɪ ɴᴀsʜᴘɪᴏᴠᴀʟ ᴇᴛᴜ sʜʟʏᴜʜᴜ ᴅʀᴏʙьʏᴜ sᴏ sᴠᴏᴇɢᴏ ᴍᴏssʙᴇʀɢ 500 ᴠ ɴᴀᴅᴇᴢʜᴅᴇ ᴘʀᴏᴅᴀᴛь ɴᴀ ᴄʜᴇʀɴᴏᴍ ʀʏɴᴋᴇ  [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇsʟɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴇɢᴏᴅɴʏᴀ ᴠʏᴊᴅᴇᴛ ɴᴀ ᴜʟɪᴛsᴜ ᴛᴏ ʏᴀ s ᴜᴅᴏᴠᴏʟьsᴛᴠɪᴇᴍ ᴘʀɪʟᴏᴢʜᴜsь ʜᴏʀᴏsʜᴇɴьᴋᴏ ᴏʙ ɴᴇᴇ ᴘʀɪᴋʟᴀᴅᴏᴍ ɴᴀsʟᴀᴢʜᴅᴀʏᴀsь ʙʀʏᴢɢᴀᴍɪ ᴋʀᴏᴠɪ s ᴇᴇ ɢᴏʟᴏᴠёsʜᴇɴьᴋɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴘᴇʀᴇᴅᴀᴊ ᴛᴀᴍ sᴠᴏᴇᴊ ᴍᴀᴍᴇ ɴᴀ ᴏʙᴇᴅᴇ ᴄʜᴛᴏ ᴇsʟɪ ᴏɴᴀ ᴍᴇɴʏᴀ ʜᴏᴛь ʀᴀᴢ ᴇsᴄʜᴇ ᴜᴋᴜsɪᴛ ᴢᴀ ʜᴜᴊ ᴛᴏ ʏᴀ ᴇᴊ ᴠsᴇ ᴇᴇ ᴋʟʏᴋɪ ɴᴀʜᴜᴊ ᴇᴇ ᴢʜᴇʟᴛʏᴇ ᴘᴏᴠʏʙɪᴠᴀʏᴜ s ʟᴇᴠᴏᴊ ɴᴏɢɪ ᴅᴀᴢʜᴇ ᴏsᴏʙᴏ ɴᴇ ɴᴀᴘʀʏᴀɢᴀʏᴀsь [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʀᴇᴢᴋɪᴍ ɴᴀᴘᴀᴅᴋᴀᴍ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ʙᴏɢᴀᴛʏʀsᴋᴏɢᴏ ᴏʙᴇᴢᴅᴠɪᴢʜɪʟ ᴛᴠᴏё ᴛᴇʟᴏ ɴᴇᴍᴏsᴄʜьɴᴏᴇ ʜᴜᴇᴛᴀ ᴛᴇʀᴘɪ ɪ ᴘᴇɴɪs ᴍᴏᴊ ᴜʙʟᴀᴢʜᴀᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏᴘʟɪᴠᴀʏᴀ ᴠᴏɴʏᴜᴄʜᴀʏᴀ ɢʀᴜᴅᴀ ʙɪᴏᴏᴛʜᴏᴅᴏᴠ ʏᴀ ᴢʜᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɢʟᴀᴢᴀ ᴠʏᴋᴏʟᴏʟ ᴘᴇɴɪsᴏᴍ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ёʙᴀɴᴀʏᴀ sᴠɪɴᴀ ᴜʙᴏɢᴀʏᴀ ʜᴜᴇᴛᴇɴь ʏᴀ ᴢʜᴇ sᴇᴊᴄʜᴀs ʀᴇᴀʟьɴᴏ ᴘɪᴢᴅᴇɴь ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ʙᴜᴋᴠᴀʟьɴᴏ ᴛᴀᴋɪ ᴄʜʟᴇɴᴏᴍ ɪᴢɴɪᴄʜᴛᴏᴢʜᴜ ʟᴜᴄʜsʜᴇ ᴘᴀᴅᴀᴊ ɴᴀ ᴋᴏʟᴇɴɪ ɪ sᴏsɪ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴍᴇʀᴅʏᴀsᴄʜɪᴊ ᴢᴀ ᴋɪʟᴏᴍᴇᴛʀ ᴘᴏᴛᴏᴍᴏᴋ ᴘʟᴇʙᴇᴊsᴋᴏᴊ ᴋᴜʀᴛɪᴢᴀɴᴋɪ ᴍʏ ᴛᴇʙᴇ ᴛᴜᴛ ᴍᴀᴍᴀsʜᴜ sᴇᴊᴄʜᴀs ᴏᴛᴛʀᴀʜᴀᴇᴍ ɪ ᴠʏᴋɪɴᴇᴍ ᴇё ɴᴀ ᴘᴏᴍᴏᴊᴋᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʜᴀʀᴄʜᴏᴋ ᴢᴀᴘᴜʟɪʟ ᴠ ᴇʙᴀʟᴏ ᴛᴠᴏё ɴᴇᴍʏᴛᴏᴇ ёʙᴀɴᴀʏᴀ ᴛᴇʀᴘɪʟᴀ ᴘᴀᴅᴀᴊ ɴᴀ ᴋᴏʟᴇɴɪ ɪ ᴜᴍᴏʟʏᴀʏᴜ ᴏ ᴘᴏsᴄʜᴀᴅᴇ ᴘᴏᴋᴀ ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴋᴇ ʙᴜᴅᴜ ᴘᴇɴɪsᴏᴍ ᴢᴜʙʏ ᴘᴇʀᴇsᴄʜɪᴛʏᴠᴀᴛь [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏsɪ ʜᴜᴇᴛs ᴛᴜᴛ ᴘᴜsᴛᴏᴢᴠᴏɴ ёʙᴀɴʏᴊ sᴏᴘʀᴏᴛɪᴠʟᴇɴɪᴇ ᴋᴀᴋᴏɢᴏ-ʟɪʙᴏ ᴅᴀᴢʜᴇ ɴᴀᴍёᴋᴀ ɴᴀ ɴᴇɢᴏ ɴᴇ sᴍᴏɢ ᴘᴏᴋᴀᴢᴀᴛь ɴᴇᴍᴏsᴄʜɴʏᴇ ᴅᴇɢᴇɴᴇʀᴀᴛ[ <emoji document_id=5334626127849724802>🤡</emoji> ] ",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴢᴀʙᴏᴄʜᴇɴɴʏᴊ ᴍᴏɪᴍ ᴘᴇɴɪsᴏᴍ  sʏɴᴏᴋ ʙʟʏᴀᴅɪ sʜᴀɴsᴀ ɴᴀ ᴠʏᴢʜɪᴠᴀɴɪᴇ ᴛᴇʙᴇ ᴛᴜᴛ ᴘᴏᴘʀᴏsᴛᴜ ɴᴇ ᴅᴀᴍ ᴍᴏʟɪ ᴍᴇɴʏᴀ ᴏ ᴛᴏᴍ ᴄʜᴛᴏʙʏ ʏᴀ ᴘʀᴏsᴛᴏ ᴏsᴛᴀᴠɪʟ ᴛᴠᴏᴊ ᴏᴛᴛʀᴀʜᴀɴɴʏᴊ ᴛʀᴜᴘ ᴠ ᴘᴏᴋᴏᴇ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴏ sᴋᴏʀᴏsᴛьʏᴜ ᴢᴠᴜᴋᴀ ᴏᴛъᴇʙᴀsʜɪʟ ᴛᴠᴏʏᴜ ᴛᴜsʜᴜ ʙᴇᴢᴅʏʜᴀɴɴᴜʏᴜ ᴍᴏᴢʜᴇᴛ ᴛᴇʙᴇ ᴜᴢʜᴇ ᴘᴏʀᴀ ᴋᴏɴьᴋɪ sᴍᴀᴛʏᴠᴀᴛь ᴏʙʀᴀᴛɴᴏ ᴠ sᴠᴏʏᴜ ʙᴇʀʟᴏɢᴜ ёʙᴀɴᴜʏᴜ ᴜsᴄʜᴇʀʙɴᴜʏᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜsᴛʀᴀɪᴠᴀᴇᴍ ᴛᴜᴛ ɴᴇᴋɪᴊ ᴘᴏᴇᴅɪɴᴏᴋ ᴋᴏᴛᴏʀʏᴊ ᴘʀᴏᴊᴅёᴛ ᴍᴇᴢʜᴅᴜ ᴍᴏᴇᴊ ᴢᴀʟᴜᴘᴏᴊ ɪ ᴛᴠᴏᴇᴊ ʀᴏᴛᴏᴠᴏᴊ ᴘᴏʟᴏsᴛьʏᴜ ᴅʀʏᴀʜʟᴏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴜʙʟʏᴜᴅᴏᴄʜɴᴀʏᴀ ғᴏʀᴍᴀ ᴢʜɪᴢɴɪ ᴛʀɪᴠɪᴀʟьɴᴀʏᴀ ᴅᴏᴄʜᴋᴀ sᴋᴜʀёʜɪ ʏᴀ ɴᴀ ᴛᴇʙʏᴀ ᴋʟᴇᴊᴍᴏ ᴠ ᴅᴀɴɴʏᴊ ᴍᴏᴍᴇɴᴛ ɴᴀʙɪʟ *ʜᴜᴇsᴏs* [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴇʙᴀʟɪ ᴛᴠᴏʏᴜ ᴛᴜsʜᴇɴᴛsɪʏᴜ ᴢʜᴀʟᴋᴜʏᴜ s ᴠᴇʟɪᴄʜᴀᴊsʜɪᴍ ᴘʀɪɴᴛsᴏᴍ ᴘᴀᴅʏ ɴᴀ ᴋᴏʟᴇɴɪ ʀᴀᴅᴜᴊsʏᴀ ᴛᴏᴍᴜ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ᴏᴋᴀᴢᴀʟɪ ᴛᴀᴋᴏɢᴏ ʀᴏᴅᴀ ᴄʜᴇsᴛь ɴᴜ ᴀ ᴘᴏ ᴏᴋᴏɴᴄʜᴀɴɪʏᴜ ᴘʀᴏᴅᴏʟᴢʜᴀᴊ sᴏsᴀᴛь [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɴᴇᴍᴏsᴄʜɴʏᴊ sʏɴᴏᴋ ᴘɪᴅᴏʀᴀsᴀ ɴᴏɢɪ ᴛᴇʙᴇ ᴠᴍᴇsᴛᴇ s ᴄʜᴀsᴛʏᴀᴍɪ ᴘᴀʜᴀ ᴠʏᴅʀᴀʟ ᴘʟᴀᴄʜь ᴏᴛ ʙᴏʟɪ ᴍᴏʟɪ ᴍᴇɴʏᴀ ᴏ ᴘᴏsᴄʜᴀᴅᴇ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠ ᴅᴀɴɴʏᴊ ᴍᴏᴍᴇɴᴛ ᴅᴇᴍᴏɴsᴛʀɪʀᴜʏᴜ ᴛᴇʙʏᴀ sᴀᴍᴜʏᴜ ᴋᴀᴄʜᴇsᴛᴠᴇɴɴᴜʏᴜ ᴍᴀɴᴇʀᴜ ᴛʀᴏʟʟɪɴɢᴀ ᴠ ᴘᴏʟɴᴏᴊ ᴍᴇʀᴇ, ɴᴀsʟᴀᴢʜᴅᴀᴊsʏᴀ ᴛᴇᴍ ᴋᴀᴋ ᴛᴇʙʏᴀ ᴇʙᴜᴛ ᴠ ᴅᴀɴɴᴏᴊ ᴋᴏɴғᴇʀᴇɴᴛsɪɪ, ᴜʙʟʏᴜᴅᴏᴋ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴅᴜʀᴏᴄʜᴋᴀ ёʙᴀɴᴀʏᴀ ᴍʏ ᴢʜᴇ ᴛᴇʙᴇ ᴛᴜᴛ ʀᴇᴀʟьɴᴏ sʜᴀɴsᴀ ɴᴇ ᴅᴀᴅɪᴍ ɴᴀ ᴠʏᴢʜɪᴠᴀɴɪᴇ ᴛʏ ёʙᴀɴʏᴊ sʟᴀʙᴀᴋ sᴏᴘʟɪ sᴠᴏɪ ᴠ ᴋᴜᴄʜᴜ sɢʀᴇʙᴀᴊ ɪ ᴛʀᴏʟьsʏᴀ sᴏ ᴍɴᴏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴠᴏᴛ ᴢʜᴇ ёʙᴀɴʏᴊ sᴍᴇʜᴏᴛᴠᴏʀɴʏᴊ ᴜʀᴏᴢʜᴇɴᴇᴛs ᴋʀᴏᴍᴀɴьᴏɴsᴋᴏᴊ sʜʟʏᴜʜɪ ʏᴀ ᴛᴇʙᴇ sᴇᴊᴄʜᴀs ᴛᴠᴏʏᴜ ᴘᴀʟᴋᴜ-ᴋᴏᴘᴀʟᴋᴜ ᴏʙ ɢᴏʟᴏᴠᴜ ʀᴀᴢъᴇʙᴀsʜᴜ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] sᴛʀᴀᴅᴀʏᴜsᴄʜɪᴊ ᴅᴇᴍᴇɴᴛsɪᴇᴊ ʙᴏʟьɴᴏᴊ ɴᴀ ɢᴏʟᴏᴠᴜ ᴜɴᴛᴇʀᴍᴇɴьsʜɪᴊ ʜᴜᴇsᴏs ᴋᴀᴋ ᴛᴇʙʏᴀ ᴇsᴛᴇsᴛᴠᴇɴɴʏᴊ ᴏᴛʙᴏʀʏ ɴᴇ ёʙɴᴜʟ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏɴ ᴢʜᴇ ёʙᴀɴʏᴊ ᴠᴏɴʏᴜᴄʜɪᴊ sʟᴀʙᴀᴋ ᴘʀɪᴋᴀᴢʏᴠᴀʏᴜ ᴛᴇʙᴇ ɴᴀ ᴋᴏʟᴇɴʏᴀʜ ᴍɴᴇ ᴛᴜᴛ ᴄʜʟᴇɴ ᴏᴛsᴀsʏᴠᴀᴛь, ᴘᴏᴘᴜᴛɴᴏ ᴘᴏʟᴜᴄʜᴀʏᴀ ᴘᴏʙʟᴀᴢʜᴋᴜ ᴠᴠɪᴅᴇ ᴍᴏᴇᴊ sᴘᴇʀᴍʏ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ɪᴢ sɴᴀ ᴛᴇʙʏᴀ ɴᴀsɪʟьɴʏᴍ ᴏʙʀᴀᴢᴏᴍ ᴠʏᴛᴀsᴄʜɪʟ ᴘᴜᴛёᴍ ᴘʀᴏᴘɪʜɪᴠᴀɴɪʏᴀ ᴠ ᴛᴠᴏᴊ ᴀɴᴀʟьɴɪᴋ ʀᴀᴢᴅʀᴏʙʟᴇɴɴʏᴊ sᴠᴏᴇᴊ ᴢᴀʟᴜᴘʏ ʙᴏɢᴀᴛʏʀsᴋᴏᴊ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʟᴀᴅɴᴏ sᴋᴜᴅᴏᴜᴍɴʏᴊ sʟᴀʙᴏɴᴇʀᴠɴʏᴊ ʙᴇsʜᴀʀᴀᴋᴛᴇʀɴʏᴊ ᴇʙᴜᴄʜɪᴊ ᴏᴛsᴛᴀʟʏᴊ ᴀᴜᴛɪsᴛ ᴅᴀʏᴜ ᴛᴇʙᴇ sʜᴀɴs ɴᴀ ᴘᴏsʟᴇᴅɴɪᴊ ᴠᴢᴅᴏʜ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
 "[ <emoji document_id=5334626127849724802>🤡</emoji> ] ʏᴀ sᴇᴊᴄʜᴀs ʜᴜёᴍ ᴘᴇʀᴇᴋʀᴏʏᴜ ᴠsᴇ ᴛᴠᴏɪ ᴅʏʜᴀᴛᴇʟьɴʏᴇ sɪsᴛᴇᴍʏ ᴠ ᴠsʟᴇᴅsᴛᴠɪᴇ ᴄʜᴇɢᴏ ᴛʏ ɴᴇᴍɪɴᴜᴇᴍᴏ ᴘᴏsɪɴᴇᴇsʜь ɪ ᴏᴛᴋɪɴᴇsʜь sᴠᴏɪ ᴘᴏᴅᴀʀʏᴀᴠʟᴇɴɴʏᴇ ᴋᴏᴘʏᴛᴀ [ <emoji document_id=5334626127849724802>🤡</emoji> ]",
"[ <emoji document_id=5334626127849724802>🤡</emoji> ] ᴏᴅɴᴀᴢʜᴅʏ ᴠ 92-ᴏᴍ ɢᴏᴅᴜ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴜᴋᴜsɪʟᴀ ᴍᴇɴʏᴀ ᴢᴀ ʜᴜᴊ ɪ ᴘᴏ ʀᴇғʟᴇᴋsᴜ ʏᴀ ᴇʙᴀɴᴜʟ ᴇᴊ s ᴋᴏʟᴇɴᴀ ᴠ ᴇᴇ sᴀʟьɴᴜʏᴜ ᴍᴏʀᴅᴜ, ᴠʏʙɪᴠ ᴘʀɪ ᴇᴛᴏᴍ ᴠsᴇ ᴇᴇ ᴢᴜʙʏ, ᴇᴛᴏᴛ ʀᴇғʟᴇᴋs ᴘᴇʀᴇᴅᴀʟsʏᴀ ᴠ ɴᴏᴠᴏᴇ ᴘᴏᴋᴏʟᴇɴɪᴇ ɪ ᴛᴇᴘᴇʀь ᴛʏ  ʙᴇᴢᴢᴜʙᴀʏᴀ ᴅɪᴋᴀʏᴀ sᴠᴏʟᴏᴄʜь ᴘɪsʜᴇsʜь ᴍɴᴇ sᴠᴏɪ ᴠʏsᴇʀʏ ᴠᴍᴇsᴛᴏ ᴛᴏɢᴏ ᴄʜᴛᴏ ʙʏ ᴄʜᴛᴏ ᴛᴏ ᴠɴʏᴀᴛɴᴏᴇ sᴋᴀᴢᴀᴛь  [ <emoji document_id=5334626127849724802>🤡</emoji> ]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl3))
            await sleep(0.1)
            await sleep(time)

    async def рискcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Рᥙᥴк ɜᥲκ᧐нчᥙ᧘ ᥱδᥲɯᥙᴛь хуᥱᥴ᧐ᥴ᧐ʙ <emoji document_id=5442804822048780010>😫</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Рᥙᥴк нᥲчᥲ᧘ ᥱδᥲɯᥙᴛь хуᥱᥴ᧐ᥴ᧐ʙ <emoji document_id=5442804822048780010>😫</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl4 = ["[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁ ⳡⲗⲉⲏ ⲁⲃⲁⲏⲧⲁⲯⲏыύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲟ ⲙⲁⲙυⲏⲟύ ⲥⲣⲁⲕⲟύ ⲕⲣⲟⲙⲉ ⲭⲩёⲃ ⲗⲟⲃυⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⲧцⲉⲡυⲗ ⲧя ⲃ ⲇⲩⲱⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧёⲗⲕⲁ,ⲙⲟύ ⲭⲩύ ⲧⲃⲟύ ⲙυⲕⲣⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩⲣυⲏⲟύ ⲧя ⲟⲱⲡⲁⲣυⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲕⲁⲕ ⲃⲉⲇьⲙⲁⲕ,ⲩ ⲙⲉⲏя ⲉⲥⲧь ⳅⲁⲇⲁⲏυⲉ ⲏⲁ υⲥⲧⲣⲉⳝⲗⲉⲏυя ⳡⲩⲇυⳃь,ⲏⲁ ⲟⳡⲉⲣⲉⲇυ ⲧⲃⲟя ⲙⲁⲙⲕⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲧⲉ ⲧⲃⲟυ ⲅⲗⲁⳅⲏυцы ⲏⲁⲭⲩύ ⲃыⳝью υ ⲏⲁ ⲭⲩύ ⲥⲉⳝⲉ ⲟⲇⲉⲏⲩ υ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲣυⲣⲟⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲙⳅⲉⲗь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⲡⲉⲏυⲥⲉ ⲥⲧⲁⲅⲏυⲣⲩⲉⲱь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝёⲙ ⲙя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅ ⲕⲇ ⲉⳝёⲙ ⲧя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲏⲉύ ⲧⲃⲟⲉύ ⲃ ⲅⲟⲗьⲫ υⲅⲣⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ ⲏⲁ ⳅⲟⲏⲉ ⲭⲩⲉⲙ ⲃⲟⲥⲡυⲧⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲅⲟⲏяⲗⲁ ⲥыⲏⲕⲁ ⲱⲗюⲭυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲫⲣυⲕⲁ ⲃыⳝьⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲥⲟⲥёⲱь ⲙⲏⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲁⲡⲁⲏя ⲧⲃⲟύ) [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲉ ⲙⲉⲯⳝⲣⲟⲃьⲉ ⲣⲁⲥⲥⲉⳡёⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳅⲁⲗⲩⲡⲁⲙυ ⲏⲁⳝⲉⲅυ ⲏⲁ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧυⲗьⲇы ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲣⲟυⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] υⲥⲕⲩⲥⲥⲏⲟ ⲣⲁⲥⲥⲉⲕⲕⲁю ⲏⲁ ⲇⲃⲟⲉ ⳅⲁⳝⲃⲉⲏⲏⲩю ⲧⲩⲱⲕⲉⲏцυю ⲡⲁⲡⲁⲏυ ⲧⲃⲟⲉⲅⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲃⲟ ⲃⲥⲉⲭ ⲡⲟⳅⲁⲭ ⲕⲁⲙⲁⲥⲩⲧⲣы ⲉⳝⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲣυⲣⲩю υ ⲉⳝⲁⲱυⲣⲩⳝ ⲙⲉⲱⲟⲉ ⲉⳝⲁⲏⲏыύ ⲏⲁ ⲧⲉⳝⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲇⲁⲃⲁύ ⲧⲁⲙ ⳅⲁⲭⲗёⳝыⲃⲁύⲥя ⲙⲟⳡёύ ⲙⲟⲉύ ⲩⲯⲉ))ⲭⲃыⲭыыⲃ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲗⲁⳝⲟⲏⲉⲣⲃⲏыύ ⲟⲏυⳃⲁⲗыύ ⲥыⲏⲟⲕ ⲇυⲕⲁⲣⲕυ ⲥⲟⲥυⲣⲩύ υ ⲙⲁⲥⲥυⲣⲩύ ⲃⲥяⳡⲉⲥⲕυ яύцⲁ ⲙⲟυ ⲩⲯⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲩ ⲧы ⲧёⲗⲕⲁ ⲏⲁⲧⲩⲣⲉ ⲙⲟύ ⲭⲩύ ⲩⲧⲟⲙυⲗⲁ яⳅыⲕⲟⲙ ⲥⲃⲟυⲙ ⲱⲉⲣⲱⲁⲃыⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ υⳅ ⲧⲉⳝя ⲇⲉⲙⲟⲏⲟⲃ υⳅⲅⲟⲏяⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲗⲉⲏⲟⲙ ⲡⲣⲟⳝυⲗ ⲥⲉⲣⲇцⲉ ⲧⲃⲟё ⲥⲗⲟⲃⲏⲟ ⲟⲥⲥυⲏⲟⲃыⲙ ⲕⲟⲗⲟⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲏⲉ ⲃⲁⲙⲡυⲣ я ⲧⲉⳝⲉ ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⳡⲉⲥⲏⲟⳡⲏⲟύ ⲟⳝⲉⲥⲥυⲗυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲇυⲁⲅⲏⲟⲥⲧυⲣⲟⲃⲁⲗ ⲩ ⲧⲉⳝя ⲣⲁⲕ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲩⲥⲉⲗⲁⲥь ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲥⲗⲟⲃⲏⲟ ⲏⲁ ⲧⲣⲟⲏ υ ⲃⲟⲟⳝⲣⲁⳅυⲗⲁ ⲥⲉⳝя цⲁⲣⲉⲃⲏⲟύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁ ⲭⲩύ ⲥⲁⳝⲗⲉⳅⲩⳝыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲩⲕⲃⲉⲏⲏⲟ ⲥⲟⲥυ ⳡⲧⲟⲗⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩⲙⲥⲧⲃⲉⲏⲏⲟ ⲉⳝⲁⲗ ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ ⲡⲣяⳡⲉⲱьⲥя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲟⲕⲟⲡⲉ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲡⲁцⲁⲏⳡυⲕⲁⲙυ ⲉⳝⲁⲗυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟю ⳝⲁⳝⲕⲩ ⲥⲟⲃⲕⲟⲃⲩю ⳝⲗяⲇь ⲉⳝⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲣⲁⲗⲗяⲕⲩ ⲣⲩⲏⲉⲧⲟⲃⲥⲕⲩю ⲭⲩⲉⲙ ⲡⲏⲩⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⲇ ⳝⲉⳅⲇыⲭⲁⲏⲏыⲙ ⲧⲣⲩⲡⲟⲙ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲏⲁⲇⲣⲩⲅⲁⲗⲥя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲁⲏэⲡυⲇⲉⲙⲥⲧⲁⲏцυю ⲡⲟⲥⲧⲣⲟυⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь υⳅ ⲥⲧⲗьⲏⲟύ ⲗюⳝⲃυ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲃыⲥⲧⲣⲟυⲗⲁ ⲇⲗя ⲏⲉⲅⲟ ⲡⲁⲙяⲧⲏυⲕ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩ цⲉⲕⲃυ υⳅ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳡⲉⲣⲧⲉύ υⳅⲅⲟⲏяⲗ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ цⲉⲗⲉⳝⲏыⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲉⲏυⲥⲟⲡⲟⲇⲟⳝⲏыύ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃыⳝьⲉⲙ ⲧⲉⳝя υⳅ ⲕⲟⲗυυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲃⲁⲏⲱⲟⲧⲏⲩⲗ ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲉⲏυⲥⲟⲙ ⲯⲃⲁⲗы ⲧⲉ ⲧⲃⲟυ ⲟⲧⲟⳝью[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲟⲧⲇⲁύ ⲇⲟⲗⲯⲏⲟⲉ ⲙⲏⲉ,я ⲥⲩⲙⲉⲗ ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲡⲣυ эⲧⲟⲙ ⲟⲥⲧⲁⲧьⲥя ⲥ ⳡⲗⲉⲏⲟⲙ, ⲁ ⲩ ⲏⲉё ⲧⲁⲙ ⳝⲗя ⲭυⲗυцⲉⲣы ⲃⲥяⲕυⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲗⲉⲏⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲙⲟⳃью ⲩⲡⲣяⲙыⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲥυⲗы ⳡⲧⲟ ⲉⲥⲧь ⲇⲗя ⲧⲉⳝя ⲥⲙⲉⲣⲧⲉⲗьⲏⲟύ υⳅьⲉⳝⲁⲱυⲣⲩⲉⲙ ⲧя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲟⳅⲉ ⲯⲩⲣⲁⲃⲗя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲯⲉⲣⲧⲃⲁ ⲙⲟⲉύ ⲕⲉⲫυⲣⲏⲟύ ⲥⲡⲉⲣⲙы [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲫυⲗυⲥ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ υⲥцⲉⲗυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲕⲣⲟⲧⲟⲥⳝⲟⲣⲏυⲕ υⲗυ ⲧⲁⲕ ⲏⲁⳅыⲉⲙⲁя ⲣⲟⲧⲟⲃⲟя ⲡⲟⲗⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲉⲣⲡⲉⲗⲁ ⲕⲣⲩⲱⲉⲏυⲉ ⲟⳝ ⲙⲟύ ⲭⲩύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲁⲥⲧь ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲙⲁⲧⲉⲣυ ⲧⲉⲣⲡυⲧь ⲡⲟⲣⲁⲯⲁⲏυⲉ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲃⲥⲉⲙⲟⲅⲩⳃⲉⲅⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲏⲉ ⲡⲟⳅⲩⳝⲁⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲇыⲣⲩ ⲃ ⲗⲟⳝⲉⲱⲏυⲕⲉ ⲧⲃⲟёⲙ ⲃыⲥⲃⲉⲣυⲗ υ яύцⲁⲙυ ⲅⲗⲁⳅⲏυцы ⲟⲧⳝυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲥⲟⳡⲉⲗьⲏυⲕ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲧёⲗⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲣⲉⲱυⲗⲁ ⲙⲏⲉ ⳅⲇⲉⲥь ⳡⲗⲉⲏ ⲙⲟύ ⳝⲟⲅⲟцⲁⲣⲥⲕυύ ⳅⲁⲧⲉⲣⲡⲉⲧь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲡⲉⲣⲙⲟⲧⲟⳅⲟυⲇы ⲏⲁ ⲗⲟⳝⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲏяⲗυ ⲫⲗⲁⲅ ⲥ ⲙⲟυⲙ ⲏⲉύⲙⲟⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩ ⲧя ⲡⲟ ⲃⲥⲉⲙ ⲡⲟⲏяⲧυяⲙ ⲙⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲕⲣⲟⲙⲉ ⲃⲉⲣⲏⲟⲥⲧυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲙⲏю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲧⲣⲉⲡⲁⲗⲁ ⲡⲟⲇⲣⲩⲇⲁⲏяⲙ ⲥⲃⲟυⲙ ⲕⲁⲕ я ⲉё ⲏⲁ ⳡⲗⲉⲏⲉ ⲥⲃⲟёⲙ ⲕⲁⲧⲁⲗ,ⲟⲏυ ⳝыⲗυ ⲃⲟⲥⲧⲟⲣⲅⲉ υ ⲡыⲧⲁⲗυⲥь ⲃⲥяⳡⲉⲥⲕυ ⲃⲥⲧⲣⲉⲧυⲧьⲥя ⲥⲟ ⲙⲏⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⳅⲁ ⲇⲃⲟυⲭ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⳅⲁⳡⲉⲙ ⲥⲡⲉⲣⲙⲟⲧⲟύ ⲙⲟⲉύ ⲃⲕυⲇыⲃⲁⲉⲱьⲥя υ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ ⲟⲧⲭⲟⲇⲏяⲕ ⲟⲥⲧⲁⲃⲗяⲉⲱь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁⲕⲟⲥⲧыⲗяⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲥⲇⲉⲗⲁⲗ ⲙⲏⲉ ⲡⲗⲟⲭⲟύ ⲙυⲏⲉⲧ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲙⲟυⲙ ⲙⲟⲅυⲗⲩ ⲥⲉⳝⲉ ⲣⲟύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⳅⲏⲁю ⳡⲧⲟ ⲧы ⲩⳝυⲃⲁⲉⲱьⲥя ⲡⲟ ⲏⲁⲱυⲙ ⲧⲉⲅⲁⲙ ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲟⳝ ⲙⲟύ ⲡⲟⲗⲟⲃⲟύ ⲁⲅⲣⲉⲅⲁⲧ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲃыⲥⲉⲕⲩ ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲗⲁⲧⲉⲏⲧⲁ ⲟⲧцⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲟⲥⲧⲁⲃⲗяю [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟ ⳡⲉⲣⲉⲡⲩⲱⲕⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲧⲩⲕⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲟⲇυⳡⲁⲃⲱυύ ⳝⲗяⲇⲟⲫⲣυⲕⲟⲃыύ ⲥыⲏяⲣⲁ ⲃⲟⳅⲟⲙⲏυⲗ ⲥⲉⳝя ⲇⲟⲭⲩя ⲃⲁⲯⲏыⲙ υ ⲡⲟⲗⲩⳡυⲗ υⳅьёⳝ ⲧⲣⲉⲧьⲉύ ⲥⲧⲉⲡⲉⲏυ ⲃⲏⲉⲟⳡⲉⲣёⲇⲏⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⳝⲉⲅυ ⲏⲁ ⲕⲩⲣⲅⲁⲏ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲣⲩⲡⲡⲁⲙυ ⲇⲉⲗⲁⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲟⲗⲥⲧⲟⲙяⲧⲏыύ ⲃⲁⲫⲗⲟⲯⲟⲣ ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲥⲟ ⲣⲧⲁ ⲏⲉ ⲇⲟⲥⲧⲁⲗ)[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⳝⲗⲁⲅⲟⲥⲗⲟⲃⲉⲏⲏыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲥⲉⲧⲣυⲏⲟⲃыύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь υⲙⲡⲉⲣⲁⲗυⲥⲧυⳡⲉⲥⲕυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲕⲩⲇⲟⲩⲙⲏыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲡⲟⲗⲟⲩⲙⲉⲃⲱυύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲧёⲗⲕⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲣυⲏⲩⲯⲇёⲏⲏыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲗⲁⳝⲁⲕ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲟⳝыⲕⲏⲟⲃⲉⲏⲏⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⳝⲉⳅⲩⲙⲃⲱυύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲉⲧⲉⲣⲡⲉⲗυⲃⲁ ⳝⲁⲗⲇⲩ ⲙⲟю юⲗⲟⳅυⲱь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⳅⲁⳡⲉⲙ ⲡⲣυⲏяⲗⲥя ⲥⲟⲥⲁⲧь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃⲩⲗьⲅⲁⲣⲏⲟ ⲉⳝⲁⲗ ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲱⲕⲩ ⲧⲃⲟю ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲉⳝⲁⲗυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲗⲉⲉⲉ ⲭⲩⲉⲙ ⲩⲙⲁⲗυⳃⲁю ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲡⲣυⲡⲁⲇⲕⲉ ⳡⲗⲉⲏ ⲥⲟⲥёⲱь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲟύ ⲭⲩύ ⳝⲟⲣⲟⳅⲇυⲗ ⲡⲣⲟⲥⲧⲟⲣыύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲩⲯⲉ ⲃⲥⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υⲏⲧυⲙⲏыⲉ ⳅⲟⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲟⳝⲗⲁⳅυⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥёⲱь ⲕⲁⲕ ⳡⲉⲱυⲣⲥⲕυύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲩⲱυ ⲧⲃⲟυ ⲟⲧⲧяⲏⲉⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲙⲅⲏⲟⲃⲉⲏьⲉ ⳅⲁⲙⲩⲧυ ⲥⲃⲟύ ⲟⲧⲥⲟⲥ ⲫυⲣⲙⲉⲏⲏыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲗⲟⲣⲁⳅⲩⲙⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲁⲗё ⲏⲁⲭⲩύ ⲏⲉ ⲥⲗыⲱⲩ ⲡυⲥⲕυ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲟⲣⲩ ⲧⲃⲟю ⲣⲁⳝⲥⲕⲟⲡυⲇⲟⲣⲥⲕⲩю ⲟⳝⲏⲉⲥёⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲉⲏυⲥⲟⲙ ⲥⲃⲟυⲙ ⲡⲣυⲙⲯⲁю ⲡⲩⲗьⲥⲁⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗυⲯⲉ ⲕ ⳅⲟⲏⲉ ⲥⲟⲡⲣυⲕⲟⲥⲏⲟⲃⲉⲏυя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁυⳡⲉύⲣⲏⲉⲱυύ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲧы ⲧⲟⲗьⲕⲟ ⲕⲟⲥⲧυ ⲥⲃⲟυⲙ ⲏⲉ ⲧⲉⲣяύ ⲡⲟ ⲡⲩⲧυ ⲕ ⲟⲧⲥⲧⲩⲡⲗⲉⲏυю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲃⲉⲣⲱυⲙ ⲡⲣⲁⲃⲟⲥⲩⲇυⲉ ⲏⲁ ⲉⳝⲁⲗⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟύ ⲟⲧⲉц ⲡⲟⲅⲟⲗⲟⲃⲏыύ ⲃⲁⲫⲗυⲧⲉⲗь ⲙⲟⲉύ ⳅⲁⲗⲩⲡы[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲏⲉ ⲥⲟⲙⲕⲏⲩⲗⲥя ⲃ ⲕⲟⲗⲗⲉⲏⲟⲗⲉⲕⲧⲉⲃⲟⲙ υ ⲏⲉ ⲏⲁⳡⲁⲗⲁ ⲙⲟⲗυⲧь ⲙⲉⲏя ⲟ ⲡⲟⳃⲁⲇⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥ ⲏⲉⲧⲉⲣⲡⲉⲏυⲉⲙ ⲭⲩⲉⲙ ⲧя υⳅⳝυⲃⲁю [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧя ⳝⲩⲇⲁⲣⲁⲯⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⳑⳑⲁⲏ ⲁⲕⲃⲁʀ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣⲟⲯёⲅ ⲧⲉⳝⲉ ⲅⲗⲟⲧⲕⲩ ⲥⲃⲟυⲙ υⲏⲫⲉⲣⲏⲁⲗьⲏыⲙ ⳡⲗⲉⲏⲟⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲥⲉⲕⲩ ⲧⲉⳝя ⲏⲁⲇⲃⲟⲉ ⲥⲃⲟυⲙ ⲁⲫⲣⲟⳡⲗⲉⲏⲟⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲧυⲡⲁ ⲕⲁⲕ ⲡⲉⲱⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲥⲟⲥёⲱь ⲙⲏⲉ ⲧⲩⲧ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙы ⳃⲁⲥ ⲥ ⳡⲉⳡⲉⲏцⲁⲙυ ⲡⲟⲇьⲉⲇⲉⲙ ⲧⲉⳝⲉ ⲱⲩⲫⲗяⲇⲕⲩ ⲣⲟⲃⲏяⲧь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲏυⲁⲕⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲟⲃⲁⲗ ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣυⲯⲙυⲥь ⲩⲯⲉ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲥⲇⲉⲗⲁύ ⲏⲁⲙ ⲟⳝⲟυⲙ ⲡⲣυяⲧⲏⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲕⲁⲕ ⲧы ⲙⲟⲯⲉⲱь ⲃⲗⲁⲥⲧⲃⲟⲃⲁⲧь ⲥⲃⲟⲉύ ⲥⲩⲇьⳝⲟύ ⲉⲥⲗυ ⲏⲁⲇ ⲧⲟⳝⲟύ ⲥⲧⲟυⲧ ⲙⲟύ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏыύ ⲡⲉⲏυⲥ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲟ ⲧы ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⲕ ⲱⲉⲣυⲏⲕⲉ ⲧⲟ ⲙⲟⲉύ ⲡⲣυⲡⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲉⳝⲉ ⲃυⲥⲗⲟⲩⲭⲟⲙⲩ ⲥыⲏⲕⲩ ⳝыⲥⲧⲣⲟ ⲧⲩⲧ ⲡⲁⲕⲗυ ⲃыⲣⲃⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⳃⲁⲥ ⲡⲟⲇⲕυⲏⲩ ⲙⲟⲏⲉⲧⲕⲩ ⲃⲃⲉⲣⲭ υ ⳅⲁ ⲃⲣⲉⲙя ⲉё ⲡⲟⲗёⲧⲁ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲯⲏⲁ ⳝⲩⲇⲉⲧ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⳡⲗⲉⲏ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲃⲥⲉ ⲉⳃё ⲭⲩύ ⲙⲟύ ⲃⲧⲉⲣⲡⲗυⲃⲁⲉⲱь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲟ ⲧы ⲧⲁⲕ ⲧⲩⲅⲟ ⲏⲁ ⲉⳝⲁⲗυⳃⲉ ⲥⲃⲟё ⲅυⳝⲣυⲇⲏⲟⲉ ⲡⲉⲏυⲥ ⲙⲟύ ⲡⲣυⲏυⲙⲁⲉⲱь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲥⲧⲟⲗьⲕⲟ ⳝыⲥⲧⲣⲟ ⲉⳝⲁⲱυⲣⲟⲃⲁⲗ ⲃⲁⲅυⲅυⲗьⲏⲟⲉ ⲡⲣⲟⲥⲧⲣⲁⲏⲥⲧⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲩⲥⲡⲉⲗ ⲣⲁⲥⲥⲉⳡь ⲃⲣⲉⲙⲉⲏⲏⲩю ⲗυⲏυю υ ⲩⲃυⲇⲉⲧь ⲥⲃⲟυⲙυ ⲅⲗⲁⳅⲁⲙυ ⲕⲁⲕ ⲅⲏⲟⳝяⲧ ⲧⲃⲟю ⲥⲟⲃⲕⲟⲃⲩю ⲡⲣⲟⳝⲗяⲧь ⳝⲁⳝⲕⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲃ 18 ⲃⲉⲕⲉ ⲗⲟⳝⲟⲧⲟⲙυю ⲡⲣⲟⲃⲟⲇυⲗυ,ⲏⲟ ⲃⲥⲉ ⲡⲟⲡыⲧⲕυ ⲥⲇⲉⲗⲁⲧь ⲥ ⲟⳝⲉⳅьяⲏы ⳡⲉⲗⲟⲃⲉⲕⲁ ⲡⲣⲟⲃⲁⲗυⲗυⲥь ⲃⲉⲇь ⲙⲟύ ⲗⳡⲏⲉ ⲏⲥⲧⲟⲗьⲕⲟ ⲟⲅⲣⲟⲙⲉⲏ ⳝыⲗ ⳡⲧⲟ ⲏⲉ ⲡⲟⲙⲉⳃⲁⲗⲥя ⲃ ⳡⲉⲣⲉⲡⲏⲟύ ⲟⲧⲥⲉⲕ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲟⳝ ⲩⲣⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲡⲟⲧⲩⲱυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲩ ⲩ ⲧя ⲙⲁⲧь ⲱⲗюⲭⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲧⲟ ⲏⲁ ⲗⳝⲩ ⲕⲣⲟⲙⲉ ⲥыⲏ ⲟⲏυⳃⲁⲗⲟύ ⳝⲗяⲇⲟⲇυⲕⲁⲣⲕυ ⲏⲁⲡυⲥⲁⲏⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲕⲁⲕ ⳃυⲧⲟⲙ ⲡⲣυⲕⲣыⲃⲁⲗⲁⲥь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲡⲩⲗυ ⲟⲧⳝυⲃⲁⲗⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲉⳝⲉ ⲣⲉⲕⲥⲩ ⳡⲉⲣⲏⲟⲩⲥⲟⲙⲩ ⲃⲙυⲅ ⲃⲥⲉ ⲧⲃⲟυ ⲙыⲥⲗυ ⲃыⳝью ⳡⲗⲉⲏⲟⲙ ⲥⲃⲟυⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣⲟⲃёⲗ ⲧⲣⲉⲡⲁⲏⲁцυю ⳡⲉⲣⲉⲡⲁ ⲏⲁⲇ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲏⲉ ⳅⲁⲇⲉύⲥⲧⲃⲟⲃⲁⲃ ⲡⲣυ эⲧⲟⲙ ⲏυⲕⲁⲕυⲭ ⲩⲥυⲗυύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲣⲉⳅьⳝⲩ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲗⲟⲙⲁⲉⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲡⲟ ⲫⲉⲏⲉ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲕυⲇыⲃⲁⲉⲧⲥя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅⲡⲣυⲏцυⲡⲏⲟ ⲉⳝⲁⲃю ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲁⲕ ⲏⲉⲟⲥⲧⲟⲣⲟⲯⲏⲟύ ⲭⲩⲉⲙ ⲙⲟυⲙ ⲇⲁⲃυⲱьⲥя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲩ ⲡⲟⲅⲟⲏяⲗⲟ ⲧⲃⲟⲉⲅⲟ яⳅыⲕⲁ ⲭⲩύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲫⲁⲗⲁⲏⲅυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲣⲃⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲭⲩⲉⲥⲟⲥ ⲥⲗⲁⳝыύ ⲃ ⲥⲃⲟυⲙ ⲙⲁⲏяⲙυⲣⲟⳡⲏыⲉ ⲥυⲗы ⲣⲉⲱυⲗ ⲩⲃⲉⲣⲟⲃⲁⲧь я ⲯⲉ ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲧⲁⲕυⲉ ⲙыⲥⲗυ ⲡⲉⲏυⲥⲟⲙ ⲃыⳝью[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲅⲩⳝⲁⲱⲗⲉⲡ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲥⲁⲗⲟ ⲧⲃⲟё ⲉⳝⲁⲏⲏⲟⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲥⲟⲧⲣяⲥⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲇⲣⲁⳝⲁⲧыⲃⲁⲉⲧ ⲟⳝⲟⲇⲕⲟⲙ ⲇⲗя ⲩⲏυⲧⲁⳅⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲡыⲧⲁⲗⲁⲥь ⲙⲉⲏя ⲟⲧⲧяⲏⲩⲧь ⳅⲁ яύцⲁ ⲙⲟυ ⲟⲧ ⲧⲃⲟⲉⲅⲟ ⳝⲉⳅⲇыⲭⲁⲏⲏⲟⲅⲟ ⲧⲉⲗⲟ ⲏⲁ ⲡⲟⲥⲕⲟⲗьⲕⲩ ⲟⲏυ ⲥⲇⲉⲗⲁⲏы υⳅ ⲙⲉⲧⲁⲗⲗⲟⲕⲉⲣⲁⲙυⲕυ я ⲉύ ⲡⲣⲟⲥⲧⲟ ⲏⲁ ⲡⲣⲟⲥⲧⲟ ⲭⲩⲉⲙ ⲣⲩⲕυ ⲟⲧⲣⲉⳅⲁⲗ υ ⳅⲁⲥⲩⲏⲩⲗ ⲉύ ⲃ ⲣⲟⲧ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲥⲃⲟⲉύ ⲅⲁⲗⲟⲡⲉⲣⲉⲇⲟⲗⲟⲃύ ⲅⲩⳃⲉύ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲕⲟⲣⲙυⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲥⲟцυⲁⲗьⲏⲟύ яⲙы ⲡⲟⲥⲙⲉⲗ ⲃⳅьⲉⳝⲁⲧь ⲏⲁ ⲙⲟύ ⲡьⲉⲇⲉⲥⲧⲁⲗ ⲙⲁⲣⲅυⲏⲁⲗьⲏⲟⲉ ⲟⲧⲣⲉⳝьⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲗⲉⲏ ⲙⲟύ яⲃⲟяⲉⲧьⲥя ⲃⲉⲣⲱυⲧⲉⲗⲉⲙ ⲥⲩⲇⲉⳝ ⲇⲗя ⲏⲉⲩⲃⲉⲣⲟⲃⲁⲃⲱυⲭ ⲃ ⲙⲟυ яύцⲁ ⳝⲗяⲇⲟⲩⲧⲃⲁⲣⲉύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅⲕⲟⲣыⲥⲧⲏⲟ ⲥⲟⲥυⲣⲩⲉⲱь ⲙⲏⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩя ⲙⲟⲉⲅⲟ ⲃⲥⲟⲥυ ⳝⲗяⲇυⲏⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲉⳝⲉ ⳡⲉⲣⲉⲡ ⳝⲩⲧыⲗⲕⲟύ υⳅ ⲡⲟⲇ ⲡυⲃⲁ ⲣⲁⳅⲇⲣⲟⳝυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲉⲇⲁⲉⲱь ⲕⲁⲗⲗ ⲙⲟύ ⲡⲣⲉⲏⲉⳝⲣⲉⲯυⲙⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲉ ⲧⲉⲣяύⲥя ⲃ ⲡⲟⲧⲟⲕⲉ ⲙⲟⳡυ ⲙⲟⲉύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩ ⲃⲟⲇⲟⲡⲁⲇⲁ ⲥⲟⲥⲁⲗ ⲙⲏⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲭⲩⲉⲙ ⲙⲟυⲙ ⳅⲁⲕⲟⲇυⲣⲟⲃⲁⲗⲥя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⳡⲟ ⲱⲁⲡⲁⲕⲗяⲕ ⲃыⲉⳝⲁⲏⲏыύ я ⲧⲉ ⲧⲩⲧⲁ ⲙⲁⲧь ⲉⳝⲁⲱυⲣⲩю ⲇⲟ ⲡⲣⲉⲇⲥⲙⲉⲣⲧⲏⲟⲅⲟ ⲥⲟⲥⲧⲟяⲏυя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧя ⲥⲟⲧⲣяⲥⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⲅⲗⲁⳅⲏυцы ⲧⲉⳝⲉ ⲃыⲯⲅⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲡⲣυⲱёⲗ ⲥюⲇⲁ υⲥⲕⲗⳝⳡυⲧⲉⲗьⲏⲟ ⲥⲟ ⲥⲃⲟυⲙ ⳝⲟⲅⲟⲩⲅⲟⲇⲏыⲙ ⲥⲃⲉⲣⲭⲙⲁⲥⲥυⲃⲏыⲙ ⲡⲉⲏυⲥⲟⲙ ⳡⲧⲟⳝы ⲃⳅьⲉⳝⲁⲧь ⲧⲉⳝя ⲕⲁⲕ ⲡⲧⲁⲭⲩ ⲡⲟⲥⲗⲉⲇⲏюю [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⲡⲟⲗⲏяⲗ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲡⲉⲣⲉⲥⲁⲇⲕⲁⲭ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲕⲩⲣяⲧⲏю ⲧⲃⲟю ⲣⲁⳅⲏⲉⲥёⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲥⲁⲇⲩ ⲩⲥⲧⲣⲟυⲗ ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲩⲇⲟⳝⲣⲉⲏυя ⲡⲟⲇⲟⲱёⲗ ⲧⲃⲟύ ⲟⲧⲉц ⲫⲣυⲕ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] υⲙⲡⲟⳅⲁⲏⲧⲏⲟ ⲡыⲧⲁⲉⲱьⲥя ⲏⲉⳅⲁⲙⲉⲧυⲧь ⲙⲟύ ⲡⲉⲏυⲥ ⲏⲟ ⲃⲥёⲣⲁⲃⲏⲟ ⲡⲟⳡⲉⲙⲩ ⲥⲙⲟⲧⲣυⲱь ⲏⲁ ⲏⲉⲅⲟ ⲕⲁⲕ ⲣⲉⳝёⲏⲟⲕ ⲏⲁ ⲥⲗⲁⲇⲟⲥⲧь ⲁⲣⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲧⲁ ⲃⲏⲁⲧⲩⲣⲉ ⲏⲉ ⲩⲙⲣυ ⲧⲟⲕⲁ ⲡⲣυⲙυⲧυⲃⲏⲟύ ⲥⲟⲥⲁⲧⲉⲗь ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲉⳝⲁⲏⲩⲧыύ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲥⲕⲟⲣⲟⲥⲧь ⲩⲇⲁⲣυⲗⲁ ⲃ ⲅⲟⲗⲟⲃⲩ ⲉⲃⲁⲱⲓⲙ ⲡⲟⲇⳃёⳡυⲏ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲕⲉⲣⲁⲙυⳡⲉⲥⲕυⲙυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧью ⲥⲃⲉⲧⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⳝыⲥⲧⲣⲉⲉ ⲥⲕⲟⲣⲟⲥⲧυ ⳅⲃⲩⲕⲁ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲙⲏⲉ ⳝⲉⳅⳅⲃⲩⳡⲏⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲕⲟⲅⲇⲁ ⲭⲩύ ⲥⲟⲥⲁⲗ ⳅⲁⳡⲉⲙ ⲡⲣυⳡⲙⲟⲕυⲃⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⲗё я ⲧⲉ ⲧⲃⲟύ ⲡⲟⲥёⲗⲟⲕ ⲏⲁⲭⲩύ ⲥⲟⲯⲅⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲥыⲏⲟⲕ ⲟⲡⲗⲉⳝⲉⲉⲏⲟύ ⲗяⲣⲃⲟⳝⲗяⲇⲏⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲟⲥⲧⲟⲏⲟⲃⲕⲉ ⲡυⳅⲇⲟύ ⲥⲃⲟⲉύ ⳝⲁⲏⳡυⲗⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲕⲟⲙⲡⲟⳅυⲧⲟⲣⲏⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲧⲁⲕⲧ ⲥ ⲉⳝⲗⲉύ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲟύ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲡⲟⲗⲟⲥⲧь ⳝⲉⳅ ⲡⲉⲏьⲕⲟⲃ ⲟⲥⲧⲁⲃυⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲡⲣⲟⲯёⲅ ⲥⲧⲉⲏⲕυ ⲃⲗⲁⲅⲁⲗυⳃⲁ ⲧⲃⲟⲉ ⲙⲁⲧⲉⲣυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁ ⲗⲟⲭ ⲗⲟⲃυ ⲕⲗⲉύⲙⲟ ⲥыⲏⲕⲁ ⲱⲗюⲭυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲟⳝ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲧⲩⲱⲩ ⲏⲁ ⲗⲉⲧⲩ ⲕ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲉ ⲱⲁⲗⲁⲃⲉ ⲁⲣⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧя ⲩⲧⲉⲱⲁю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲃ ⲥⲕⲟⲣⲟⲡⲟⲥⲧυⲯⲏⲟⲙ ⲡⲟⲣяⲇⲕⲉ ⲡⲟⲧⲉⲣⲡυⲧь ⲏⲉⲩⲇⲁⳡⲩ ⲡⲣⲟⲧυⲃ ⲏⲉⲣⲁⲃⲏⲟύ ⲥⲃⲭⲁⲧⲕυ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲁⲣⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⲏⳅⲟⲕⲟⲗⲟⲏⲕⲩ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲡⲟⲇⲟⲯⲅⲩ ⲭⲇ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲯⲟⲡⲩ ⲇⲁⲱь υⲗυ ⲭⲩⲉⲙ ⲃ ⲅⲗⲁⳅ?[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲣⲁⲥⲥⲭⲩⲉⲣⲉⳅυⲙ ⲧⲃⲟё ⲙⲏυⲙⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲭⲩяⲙυ ⲥⲃⲟυⲙ ⲧⲟⲣⲯⲉⲥⲧⲃⲉⲏⲏыⲙυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⲗё ⲧёⲗⲕⲁ я ⲧⲃⲟύ υⲙⲡⲉⲣⲁⲧⲟⲣ ⲃыⲡυⲱυ ⲙⲁⲧⲉⲣυ ⳡёⲣⲏⲟύ ⲱⲗюⲭⲉ ⳡⲗⲉⲏ ⲙⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⳝⲁⲏⲕⲁύ ⲧⲃⲟя ⲟⲏυⳃⲁⲗⲁя ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲁ ⲃⲡⲣυⲏцυⲡ ⲏⲉ ⲃыⲥⲧⲟυⲧ ⲡⲣⲟⲧυⲃ ⲏⲉⲅⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲏяⲥⲣⲟⲗьⲏыύ ⲥыⲏⲟⲕ ⲡⲁⲥⲕⲩⲇυⲏцы я ⲯⲉ ⲧⲉ ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲟ ⲃⲥⲉⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉⲃⲟⳅⲙⲟⲯⲏыⲉ ⲇыⲣⲕυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣⲟⲡⲁⳃυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲧⲟⲗьⲕⲟ ⲡⲟⲙⲉⲣⲁⲧь ⳅⲇⲉⲥь ⲏⲉ ⲃⳅⲇⲩⲙⲁύ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲕⲁⲏⲁⲃⲏⲟⲉ ⲡⲟⲥⲧⲟⲧⲣⲟⲇьⲉ ⲥⲗыⲱυⲱь я ⲧⲉⳝⲉ ⲙⲁⲧь ⲭⲩⲉⲙ ⲇⲁⲣⲁ ⲣⲉⳡυ ⲣⲉⲱυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲧⲁⲙ ⲙⲁⲧь ⲥⲃⲟю ⲩⲯⲉ ⲟⲧⲅⲟⲏяύ ⲟⲧ ⲥⲡⲉⲣⲙⲟⲧы ⲙⲟⲉύ ⲁ ⲧⲟ ⲇⲩⲣⲁ ⲃⲕⲣⲁύ ⲟⲡⲟⲗⲟⲩⲙⲉⲗⲁ ⲟⳝⲟⲯⲣⲁⲃⲱυⲥь ⲉё[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲧⲉⲗⲉⲃυⳅⲟⲣ ⲡⲟⲕⲁ ⲏⲁ ⲃьⲉⳝёⲱь ⲣⲁⳝⲟⲧⲁⲧь ⲏⲉ ⲥⲧⲁⲏⲉⲧ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲃ ⲡⲟⲗⲏыύ ⲣⲟⲥⲧ ⲏⲁⳝυⲗ ⲙⲟύ ⲭⲩύ ⲁⲣⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲕⲁⲗⲗⲟⲃⲡⲁⲗⲩю ⲧⲣⲉⳃυⲏⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲙⲉⲥⲧⲟ υⲏⲥⲩⲗυⲏⲁ ⲕⲁⲡⲁⲗⲁ ⲡⲟ 5 ⲙⲅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲥⲉⲥⲧⲣⲩ ⲧⲃⲟю ⲗⲁⲡⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥыⲏ ⲙⲩⲥⲟⲣⲟⲡⲣⲟⲃⲟⲇⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲇⲟ ⳝⲗⲉⲥⲕⲁ ⲟⳡⲉⲗⲟ ⲙⲟё ⲃыⲧⲉⲣ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲙⲩⲗⲉ ⲉⳝⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲗⲉⲱυⲃыύ ⲥыⲏ ⳡⲉⲣⲏюⳃⲉύ ⲱⲗюⲭυ я ⲧⲃⲟю ⲯυⲣⲏⲟⲙⲁⲥⲧⲏⲩю ⲗⲁⲭⲩⲱⲕⲩ ⲙⲁⲧь υⳅьⲉⳝⲁⲱυⲣⲟⲃⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲗⲟⲭ ⲭⲩύ ⲏⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲟύ ⲭⲩύ эⲧⲟ цⲉⲣⲕⲟⲃь ⲁ яύцⲁ ⲕⲟⲗⲟⲕⲟⲗы ⲡⲟ ⳅⲃⲩⲕⲩ ⲕⲟⲧⲟⲣыⲭ ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲏυⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲏⲁⲥⲧⲩⲡυⲗ ⲧⲃⲟύ ⳡⲉⲣёⲗ ⲥⲟⲥⲁⲧь ⲭⲩύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲏⲟⲅⲟⲡⲟⲧⲟⳡⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲥⲗⲟⲃⲏⲟ υⲙⲡⲉⲣⲁⲧⲟⲣ ⳅⲁⲥⲧⲁⲃⲗю ⲧⲃⲟю ⲙⲁⲧь ⳝыⲧь ⲟⳝⲅⲗⲁⲇⲁⲏⲏⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲗⲟⲅⲟⲃⲟⲏυя υⲥⲭⲟⲇяⳃυⲉ υⳅ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⳅⲁⲧⲙυⲗυ ⲧⲃⲟύ ⲣⲁⳅⲩⲙ υ ⲟⲧⲏыⲏⲉ ⲧы ⲡⲣⲉⲇⲏⲁⲇⲗⲉⲯυⲱь ⲙⲟⲉⲙⲩ ⲡⲉⲏυⲥⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧя ⲙⲉⲯ ⲣёⳝⲉⲣ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲙⲏю ⲕⲁⲕ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲙⲏю ⲕⲁⲕ ⲉⳝⲁⲗ ⲧя ⳅⲁⲅⲟⲣⲟⲇⲟⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧя ⲃыⲕⲩⲣυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁ ⲥⲟⲥⲏυ ⳝⲁⲗⲇы ⲙⲟⲉύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲗяⲇⲟⲉⳝ ⲙⲁⲏяⲙυⲣⲟⳡⲏыύ ⳡⲧⲟ ⲉⲥⲧь ⲥыⲏⲕⲟⲙ ⲱⲗюⲭυ ⲡⲟ ⲕⲣⲟⲃⲉ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲟύ ⲭⲩύ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ ⲁⲣⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲣⲉⲥⲏⲩⲗ ⲧя ⲭⲩⲉⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃⲟⲗⲁⲉⲱь ⲕⲁⲕ ⳝⲉⲱⲉⲏⲏⲁя ⲕⲟⲅⲇⲁ ⲥⲟⲥёⲱь ⳝⲉⳅ ⲕⲟⲡыⲧ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⲏⲉⲥⲩ υⲏⲥⲉⲕⲧⲟⲫⲟⳝⲏⲟⲉ ⲙⲁⲥⲗⲟ ⲏⲁ ⲥⲃⲟύ ⳡⲗⲉⲏ υ ⲃⲟύⲇⲩ ⲃ ⲧⲃⲟю ⲏⲉⲧⲟⲡыⲣυⲭⲩ ⲙⲁⲧь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥыⲏⲟⲕ υ ⲣⲟⲇⲁ ⲱⲗюⲱьⲉⲅⲟ ⲧы ⳡⲧⲟ ⳅⲇⲉⲥь ⲡⲟⲙⲉⲣⲉⲧь ⲃⳅⲇⲩⲙⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] цⲉⲗⲕⲟⳝⲁⳡⲁⲣⲏыύ υⲏцⲉⲗ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲕⲣыⲗьяⲙυ ⲭⲩύ ⲟⲧⲟⲣⲃⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁ ⲥⲗⲁⲇⲕⲟⲉⲯⲕⲉ ⲧⲃⲟⲉⲙⲩ ⲡⲁⲭⲁⲏⲩ ⲡυⲇⲟⲣⲩ ⲙⲟⳡυ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲁ ⲟⲏ ⲥ ⲇⲟⲃⲟⲗьⲏыⲙ ⲉⳝⲁⲗⲟⲙ ⲡⲣυⲏяⲗⲥя ⲉё ⲡυⲧь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲗя ⳝⲩⲇⲩ ⲙⲁⲧь ⲧⲉ ⲏⲟⲅⲁⲙυ ⳅⲁⳝυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥ ⲧⲁⲕⲟύ ⲥυⲗⲟύ ⳡⲧⲟ υⳅ ⲡⲟⲇ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲏⲁⳡⲁⲗυ ⲃыⲥυⲕⲁⲧьⲥя υⲥⲕⲣы[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟя ⲱⲗюⲭⲟⲙⲁⲧⲉⲣь ⲥ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲥⲗⲟⲃⲏⲟ ⲥ ⲡⲟⲥⲟⲭⲁ ⲙⲁⲅυⳡⲉⲥⲕⲟⲅⲟ ⲏⲁⲡⲣⲁⲃυⲗⲁ ⲟⲅⲟⲏь ⲏⲁ ⲃⲁⲱ ⲡⲟⲥёⲗⲟⲕ ⲭⲇ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳅⲁⲥⲧⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲡυⲇⲟⲣⲁⲥⲏυцⲩ ⲃ ⲡⲣυⲡⲁⲇⲕⲁⲭ ⲡⲩⲭⲏⲩⲧь ⲡⲟⲉⲇⲁя ⲥⲡⲉⲣⲙⲩ ⲙⲟю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я υⳅⲅⲏⲁⲗ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲉⲙⲟⲏⲟⲃ ⲡⲩⲧёⲙ ⲃⲭⲟⲯⲇⲉⲏυя ⲥⲃⲟυⲙ ⲡⲟⲗⲟⲃыⲙ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃ ⲉё ⲃⲁⲅυⲗьⲏыύ ⲟⲧⲥⲉⲕ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕ ⲯⲉ ⲩⲥⲉⲣⲇⲏⲟ ⲕⲁⲕ ⲧы ⲥⲟⲥⲁⲗ ⲭⲩύ ⲙⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲫⲣυⲕⲟⲃⲁ ⲥⲁⲥёⲱь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟю ⲙⲁⲧь ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲥⲁⲯⲩ ⲕⲁⲕ ⲏⲁ ⲕⲣⲉⲥⲗⲟ ⲕⲁⳡⲁⲗⲕⲩ ⲉⳝⲁⲏⲏⲟⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥⲁⲧь ⲭⲩύ ⳅⲁ ⲡⲣⲉⲇⲏⲁⳅⲏⲁⳡⲉⲏυⲉⲙ ⲥⲡⲁⲥⲉⲏυⲉ ⲧⲃⲟⲉύ ⲯυⲃⲟⲧⲏⲟⲡⲟⲇⲟⳝⲏⲟύ ⲥⲉⲙьυ ⲏυⳃⲩⲕⲟⲃ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲙⲉⲗⲟ ⲉⳝⲁⲗ ⲧя ⲡⲟⲇ ⲅⲣⲟⲭⲟⲧ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡυⲇⲟⲣⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲧⲁⲕυⲙ эⲏⲧⲩⳅυⲁⳅⲙⲟⲙ ⳡⲧⲟ ⲧⲃⲟύ ⲟⲧⲉц ⳝыⲗ ⲃыⲏⲩⲯⲇⲉⲏ ⲕⲁⲧⲁⲧьⲥя ⲧⲩⲇⲁ ⲥюⲇⲁ ⲏⲁ ⲙⲁⲣⲱⲣⲩⲧⲕⲉ ⲥⲃⲟⲉύ ⳡⲧⲟⳝы ⲏⲉ ⲃυⲇⲉⲧь эⲧⲟⲅⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩⲥⲟⲥυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃⲥⲟⲥⲉ ⲕⲁⲕ ⳅⲁⲇⲩⲙⳡυⲃыύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣυⲕⲩⲣυⲗ ⲥ ⲗⲁⲙⲡⲁⲇы ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟю ⲏⲉⲡⲟⲗⲟⲃⳅⲣⲉⲗⲩю ⲥⲉⲥⲧⲣёⲏⲕⲩ ⲱⲗюⲭⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥυⲗⲟύ ⲭⲩя ⲥⲃⲟⲉⲅⲟ ⳝⲉⳅ ⲱⲁⲏⲥⲃⲟ υⲥⲧⲣⲉⳝⲗяю ⳝⲗяⲇⲟⲇⲉⲧⲟⲕ ⲏⲉⲥⲡⲟⲥⲟⳝⲏыⲭ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲅⲟⲣⳝⲁⲧⲟⲥⲡυⲏⲏыύ ⲥыⲏⲟⲕ ⲁⲥⳝⲉⲥⲧⲟⲃⲟύ ⲡⲣⲟⲫⲩⲣⲥⲉⲧⲕυ ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲃыⲉⳝⲉⲙ ⲧя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩяⲙυ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲉⲙ ⲣⲉⲱⲉⲧⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲏυⲙⲟ ⲥⲟⲥёⲱь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲟⲧⲕυⲏⲩⲃⲱυ ⳡⲉⲗⲟⲃⲉⳡⲏⲟⲥⲧь ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲕⲁⲕ ⳡⲣⲉⳅⲃыⳡⲁύⲏⲟⲟⲡⲁⲥⲏыύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲭⲣⲁⲙⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] цⲉⲣⲕⲟⲃⲏⲟ ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲏⲁ ⳅⲁⲇⲏⲉⲙ ⲣяⲇⲩ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲅⲉⲣⲟυⲏⲟⲃⲟ ⳅⲁⲃυⲥυⲙ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] υⳅьёⳝυⲥⲧⲟ ⲥⲟⲥⲁⲗ ⲇⲟ ⲡⲟⲧⲉⲣυ ⲡⲩⲗьⲥⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲃ ⲣыцⲁⲣυ ⲟⲣⲇⲉⲏⲁ ⲡⲟⲥⲃяⲧυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] υⲥⲡⲟⲗьⳅⲩю ⲗυⲱь ⲥυⲗы ⲥⲃⲟυ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲃⲉⲣⳃⲁюⳃυⲉ ⲥⲩⲇьⳝы ⲏⲁ ⲥⲗⲁⳝыⲙυ ⲭⲩⲉⲥⲟⲥⲁⲙυ ⲧⲉⲗⲉⲥⲣⲁⲙⲙⲟⲃⲥⲕυⲙυ ⲣⲁⳅⲅⲉⲣⲙⲉⲧυⳅυⲣⲩю ⲡⲁⲥⲧь ⲧⲉⳝⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥυⲗⲟύ ⲙыⲥⲗυ ⲙⲁⲧь ⲧⲃⲟю ⲃыⲧⲣⲁⲭⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲫⲗⲟⲙⲁⲥⲧⲉⲣⲟυⲇⲏыύ ⲥыⲏⲟⲕ ⲱⲗюⲭⲟⲃυⲇⲏⲟύ ⳝⲟⲗьⲏⲟύ ⲗⲉύⲕⲉⲙυⲉύ ⲇⲁⲯⲉ ⲏⲉ ⲡыⲧⲁⲉⲧьⲥя ⳡⲧⲟ ⲧⲟ ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⳡⲗⲉⲏⲁⲙ ⲅⲟⲥⲡⲟⲇⲥⲕυⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲩⲥⲗⲩⲯⲗυⲃⲟ ⲥⲟⲥёⲱь ⲙⲏⲉ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅ ⲙыⲥⲗⲉύ ⲥⲟⲥёⲱь ⲙⲏⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲗⲟⲃⲏⲟ ⲥⲁⳝ-ⳅυⲣⲟ ⲡⲣυύⲇⲩ ⲕⲣⲩⲱυⲧь ⲧⲉⳝⲉ ⲉⳝⲁⲗυⳃⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲫⲁⲉⲣⳝⲟⲗⲟⲙ ⲩⳝυⲗ ⲧя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲁⲙⲟⲃⲕⲁⳡⲉⲏ ⲃⲉⲧⲭⲟⳅⲁⲃⲉⲧⲏыⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⲏⲧⲣⲟⲡⲟⲙⲟⲣⲫⲏⲟⲉ ⲡⲟⲇⲟⳝυⲉ ⲥⲃυⲏⲟⳡⲉⲗⲟⲃⲉⲕⲁ я ⲯⲉ ⲧⲃⲟю ⲥⲃυⲏⲟⲙⲁⲧь ⲏⲁ ⲥⲁⲗⲟ ⲡⲩⲥⲧυⲗ υ ⲟⳝⲉⲥⲡⲉⳡυⲗ ⲭⲟⲭⲗⲟⲃ ⲡⲟⲯυⳅⲏⲉⲏⲏыⲙ ⳅⲁⲡⲁⲥⲟⲙ ⲥⲁⲗⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⲇⲕⲁя ⲃыⳝⲗяⲇⲟⳡⲏⲁя ⲡⲣⲟⳝⲟυⲏⲁ ⲧы ⲕⲩⲇⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲩⲧⲁⲉⲱь ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲟⲧⲣⲕⲉ ⲏⲣⲁⲃⲁ ⲟⲧⲥⲟⲥⲉ ⲉⲅⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲉⳝⲉ ⲗⲩⲡⲟⲅⲗⲁⳅⲟⲙⲩ ⲥыⲏⲕⲩ ⲕⲣⲁⲥⲏⲟⲣыⲗⲟύ ⳝⲗяⲇⲉⲏцυυ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲃⲥⲉ ⲕⲟⲥⲧυ ⲃ ⲡыⲗяⲕⲩ ⲥⲟⲧⲣⲩ,ⲧы ⲏⲁ ⲕⲟⲅⲟ ⲡⲁⲥⲧь ⲟьⲕⲣыⲧь ⲣⲉⲱυⲗⲁ ⲩⲙⲁⲗυⲱёⲏⲏⲁя ⲏⲁⲥⲁⲇⲕⲁ ⲏⲁ ⲙⲟύ ⲡⲉⲏυⲥ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗⲟ ⲥⲃⲟё ⲥⲕⲣⲉⲡⲟⲥⲧⲏⲟⲉ ⲏⲉ ⲧⲉⲣяύ ⳅⲇⲉⲥя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⲡυⲱⲩ ⲅⲣⲩⲥⲧⲏⲩю υⲥⲧⲟⲣυю ⲡⲣⲟ ⲧёⲗⲕⲩ ⲕⲟⲧⲟⲣⲁя ⲧⲁⲕ υ ⲏⲉ ⲥⲙⲟⲅⲗⲁ ⲇⲟⲧυⳡь ⲥⲃⲟⲉύ цⲉⲗυ,ⲧⲟⳝυⲱь ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ,ⲅⲗⲁⲃⲏⲟύ ⲅⲉⲣⲟυⲏⲉύ ⳝⲩⲇⲉⲧ ⲕⲥⲧⲁⲧυ ⲧⲃⲟя ⲙⲁⲧь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲡⲣⲟⳅⲉ ⲟ ⲧⲉⳝⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲟⲥⲧⲁⲃⲗю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲗⲁⲃⲡⲩⲭ ⲁ ⲏⲩ ⲡⲣυⲏяⲗⲥя ⳡⲗⲉⲏ ⲙⲟύ ⲣⲁⲥⲥⲁⲥыⲃⲁⲧь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲏⲟⲅⲟⲥⲧⲣⲁⲇⲁⲗьⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲩⳝы ⲡⲟⲗⲟⲃыⲉ ⲡⲣⲟⲯⲅⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲉύⲙ ⲥⲃⲟύ ⲟⲥⲧⲁⲃⲗю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲉⳝя ⲥыⲏⲕⲁ ⲥⲗⲁⳝⲉύⲱⲉύ ⲱⲗюⲭυ ⲩⳝью ⲥⳡⲁ υ ⲟⳡυⲱⲩ ⲗⲟⲕⲁцυю ⲟⲧ ⲏⲉⲯⲉⲧυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲟύ ⲥⲧυⲗь ⲉⳝёⲧ ⲧⲃⲟю ⲙⲁⲧь ⲃⲟⲧ ⲧы υ ⲫⲁⲏⲁⲧⲉⲉⲱь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⳡⲗⲉⲏⲉ ⲧⲩⲭⲏⲉⲱь ⲧⲁⲕ ⳝыⲥⲧⲣⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] υⳅⲩⲃⲉⳡυⲙ ⲧⲉⳝя ⳡⲁⲥⲧыⲙυ ⲩⲇⲁⲣⲁⲙυ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲥⲟⲥⲁⲗьⲏυⲕⲩ ⲧⲃⲟⲉⲙⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲯⲉ ⲃ ⲥⲟюⳅⲉ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ υ яύцⲁⲙυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⳅⲁⳡⲉⲙ ⲥ ⲱⲗюⲭⲁⲙυ ⲏⲁ ⲡⲟⲇⲟⳝυⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ яⲕⲱⲁⲉⲱьⲥя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥυ ⲙⲟⲇⲩⲗьⲏⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥυ ⲃⲇⲩⲙⳡυⲃⲟ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲟⲥυ ⲕⲁⲕ ⲡⲣυⲏяⲧⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃⲕυⲇыⲃⲁⲉⲱьⲥя ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⳝы ⲥⲗⲟⲃυⲧь ⲡⲣυⲭⲟⲇ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲟ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲭⲩя ⲉⲱё ⲏυⳡⲉⲅⲟ ⲏⲉ ⲅⲟⲃⲟⲣυⲧ ⲟ ⲧⲟⲙ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲥⲇⲉⲗⲁⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲏю ⲧⲉ ⲧⲃⲟю ⲉⳝⲁⲗ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲣⲩⲭⲗяⲇь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲃⲧⲟⲣяύ ⲥ ⳡⲗⲉⲏⲁ ⲃⲥⲉ ⲥⲗⲟⲃⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲏυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲁ ⲟⲏⲁ ⲃⲉⲗⲁⲥь ⲕⲣⳡ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲥыⲏ яⳃⲉⲣυцы ⲕⲟⲧⲟⲣⲁя ⲥⲕυⲇыⲃⲁⲉⲧ ⲕⲟⲯⲩ ⲡⲣυ ⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲁⲏцⲩю ⲃⲁⲗьⲥ ⲃ ⲕυⲱⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲟⲥⲏⲟⲃⲁⲏυя ⲇⲗя ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉⲅⲟ ⲡⲩⲧυ ⳡⲧⲟⳝы ⲉύ ⳝыⲗⲟ ⲡⲣⲟⳃⲉ ⳅⲁⲅⲣⲩⲯⲁⲧь ⲃ ⲥⲉⳝя ⳡⲗⲉⲏⲃ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲃ ⲕⲟⲥⲙⲟⲥ ⲡⲩⲗьⲏⲩⲗ ⳡⲧⲟⳝы ⲟⲏⲁ ⲧⲁⲙ ⲣыⲅⲁⲗυⳃⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲙυⳡⲉⲥⲕⲩю ⲡыⲗь ⲥⲟⳝυⲣⲁⲗⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲡυⳅⲇⲁⳡυⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲣⲟⲅⲁⲧⲕⲩ ⲏⲁⲧяⲏⲩⲗυ ⲡⲩⲗьⲏⲩⲗ ⲉю ⲃ ⲥⲟⲥⲉⲇⲥⲕⲟⲉ ⲟⲕⲏⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲅⲩⳝⲕⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲉⲣⲡυⲱь ⲧⲩⲧⲁ ⳅⲏⲁⳡυⲧ ⳡⲗⲉⲏы ⲏⲁⲱυ ⳝⲟⲅⲁⲧыⲣⲥⲕυⲉ ⲏⲁⲇ ⲥⲟⳝⲟύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩяⲙ ⲧⲁ ⲁⲕⲩⲏⲩⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⳅⲁⲙⲉⲥⲧⲟ ⲱⲁⲙⲡⲁⲏⲥⲕⲟⲅⲟ ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲉ ⲙⲟⳡυ ⲥⲃⲟⲉύ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲗⲁⲭⲩⲏⲇⲣⲁ я ⲯⲉ ⲧⲉⳝя υⳅⲩⲃⲉⳡⲩ ⳅⲇⲉⲥь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲟⲧⲡυⲏⲁⲗ ⲧя ⲥⲗⲟⲃⲏⲟ ⲅⲣⲩⲱⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥыⲏⲟⲕ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲥⲗⲁⳝⲉύⲱⲉύ ⲡⲟⲇⲭⲩύⲏⲟύ ⲣⲁⳝⲟⲃⲡⲁⲗⲟύ ⲱⲗюⲭυ ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲏⲉ ⲡⲣυⲃⲥⲉⲗюⲇⲏⲟ ⲣⲉⲱυⲗ ⳅⲁⲗⲩⲡⲩ ⲡⲟ ⲥⲁⲙыⲉ ⲅⲗⲁⲏⲇы ⲃⲥⲗюⲏяⲃυⲧь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟю ⲥⲗюⲏяⲃⲩю ⲙⲁⲧь ⲱⲗюⲭⲩ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲅⲗⲩ ⳅⲁⳝьёⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟю ⲏⲁ ⲱⲁⲙⲡⲩⲣυⲏⲩ ⲥⲃⲟю ⲟⲇⲉⲗ υ ⲡⲩⲥⲧυⲗ ⲙⲁⲣυⲏⲟⲃⲁⲧьⲥя ⲃ ⲡⲣυⲙⲉⲥⲉ ⲙⲟⳡυ υ ⲥⲡⲉⲣⲙы[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲥⲧⲣⲉⲙяⲏⲕⲟύ ⲡⲟ ⲅⲟⲣⳝⲩ ⲩⲉⳝⲁⲗ ⳡⲧⲟ ⲟⲏ ⲕⲁⲕ ⲧⲉⲗёⲏⲟⲕ ⳅⲁⲃыⲗ ⲉⳝⲁⲧь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲃⲏⲁⲧⲩⲣⲉ ⲥⲃⲟё ⲧⲟⲗⲥⲧⲟⲙяⲧⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲧⲟⲡυ ⲏⲁⲭⲩ ⳝⲟⲣⲟⲃ ⲃыⲉⳝⲁⲏⲏыύ ⲥⲗыⲱⲁⲗ ⲙя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲣⲟⲱⲙⲉⲧⲕυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩяⲙυ ⲥⲙⲉⲧё[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲧя ⲡⲟⲇ ⲃⲥⲭⲣюⲕυ эⲗьⲫυⲥύⲕυⲉ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⲟⳝⲉⳅⲅⲗⲁⲃⲗю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲟⳝⲟύ ⲡⲟ ⲟⲕⲏⲩ ⲃьⲉⳝⲁⲱυⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲁⲕυⲏь 5 ⲥυⲏⲟⲏυⲙⲟⲃ ⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳡⲧⲟ ⲧы ⲃыⲗⲟⲃυⲧь ⲡыⲧⲁⲉⲱьⲥя ⲕⲣⲟⲙⲉ ⳅⲁⲗⲩⲡы ⲙⲟⲉύ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲏⲉⲩⲙⲏⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲥⲧⲟя ⲡⲟ ⲡⲟяⲥ ⲃ ⲃⲟⲇⲉ ⲟⲏⲁ ⲩⲙⲩⲇⲣυⲗⲁⲥь ⲩⲙⲉⲣⲉⲧь ⲟⲧ ⲟⳝⲉⳅⲃⲟⲯυⲃⲁⲏυя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲭⲩⲗⲉ ⳅⲇⲉⲥя ⲥ ⳡⲗⲉⲏⲁⲙ ⲙⲟυⲙ яⲕⲱⲁⲉⲱьⲥя ⲏⲉⲧⲟⲡыⲣь ⳝⲗя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳅⲁⲥⲗⲟⲏⲕυ ⲕⲟⲧⲟⲣыⲉ ⲡⲉⲣⲉⲅⲁⲣⲁⲯυⲃⲁюⲧ ⲉύ ⲇыⲭⲁⲧⲉⲗьⲏыⲉ ⲡⲩⲧυ ⲥⲗⲟⲙⲁⲉⲙ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲏυⲥⲟⲏ ⲥ ⲙⲉⲣⳅⲕυⲙυ ⲃⲥⲕⲣюⲕⲁⲙυ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲣⲁⳝⲟⲃⲡⲁⲗыύ ⲟⲕⲁⳡⲁⲏⲉⲗыύ ⲡⲉⲱⲕⲟⲇⲟⲇυⲕ ⲧы ⳡⲟ ⲧⲁⲙ ⲃⲏⲁⲩⲧⲣⲉ ⲃ ⲥⲉⳝя ⲣⲉⲱυⲗⲙ ⲙⲏⲉ ⲡⲟⲃⲉⲣυⲧь ⲁⲣⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲯⲉ ⲡⲟⲇ ⲙⲟυⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲏⲉⲥⲕⲟⲏⳡⲁⲉⲙыⲙ ⲡⲟⲙⲣёⲱь ⳅⲇⲉⲥь[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲕⲁ ⲏⲉ ⲥⲧⲁⲗⲟ ⲟⲕⲟⲏⳡⲁⲧⲉⲗьⲏⲟ ⲡⲟⳅⲇⲏⲟ ⳝⲉⲅυ ⲟⲧ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲕⲁⲥⲧⲣⲩⲗⲉύ ⲡⲉⲣⲉⲉⳝⲁⲗ ⲁⲣⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲯⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲧυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲅⲏⲩ ⲡⲟⲡⲣⲟⲥⲧⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲉ ⲥⲗыⲱⲩ ⲧⲩⲧ ⲡυⲥⲕⲁ ⲧⲃⲟⲉⲅⲟ ⲥыⲏⲟⲕ ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉύ ⲧⲣⲁⲥⲥы[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧя ⲥⲃⲟυⲙ ⲱⲩⲅⲁю [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲥё υⲇυ ⲇⲁⲗьⲱⲉ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲱυⲣⲩю ⲉⲧⳝя ⲡⲟ ⲕⲁⲇыⲕⲩ ⲱⲟⲗⲁⲃⲩ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲃⲟёⲙ ⳡⲗⲉⲏⲉ ⲕⲁⲧⲁю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲟⲅⲏⲁⲇыⳃⲁⲱυⲙ ⳡⲗⲉⲏⲟⲙ ⲃыⲯⲅⲩ ⲏⲁⲡⲣⲟⳡь ⲡⲗⲉⲙя ⲧⲩⲏⲉяⲇцⲉⲃ ⲧⲃⲟυⲭ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲧυⲭⲟⲧⲃⲟⲣⲏⲟ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲏⲉⳝⲗⲁⲅⲟⲣⲟⲇⲏⲁя ⲡⲟⲙⲉⲥь ⲥⲟⳝⲁⳡья ⲏⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲯⲉ ⲩⲧⲟⲙυⲗⲁ ⲙⲟύ ⲡⲉⲏυⲥ ⲥⲃⲟυⲙυ ⳡⲁⲥⲧыⲙυ ⲟⲧⲥⲟⲥⲁⲙυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲱυⲣⲕⲩ ⲣⲁⳅⲙⲟⳡⲩ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⲩⲕⲟⲣⲟⳅⲏⲉⲏⲏⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲉⲱьⲥя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲧыⲗⲕⲟύ ⲡⲟ ⲱⲉⲉ ⲃьⲉⳝⲁⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲁⲗё ⲙⲁⲣⲁⳅⲙⲁⲧυⳡⲉⲥⲕυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲏⲉ ⲃⲧⲉⲣⲡⲗυⲃⲁύ ⲧⲟⲗьⲕⲟ ⲭⲩυ ⲏⲁⲱυ ⲧⲩⲧ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲙⲁⲧь ⲃыⲉⳝⲉⲙ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲉⳝⲁⲗ ⲧⲃⲟⲉⲅⲟ ⲁⲃⲥⲧⲣⲁⲗⲟⲡυⲧⲉⲕⲁ ⲟⲧцⲁ ⲡⲉⲇυⲕⲟⲃⲁⲧⲟⲅⲟ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩⲉⲙ ⲧⲉ ⲡυⲣⲥυⲏⲅ ⲥⲇⲉⲗⲁⲗ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲙⲁⲙⲁⲏⲉ ⲧⲃⲟⲉ ⲙⲟⳡⲕⲩ ⲭⲩⲉⲙ ⲡⲣⲟⲕⲟⲗⲟⲗ [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝⲁⲗⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲥⲙⲉⲥью ⲥⲡⲉⲣⲙы υ ⲙⲟⳡυ υⳅⲅⲟⲏυⲙ ⲧⲉⳝя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲡⲟⲧⲩⲥⲧⲁⲣⲟⲏⲏⲉ ⲥⲟⲥёⲱь [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲥⲗюⲏяⲃⲟ υⳅⲩⲃⲉⳡⲩ ⲧⲉⳝя[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲣⲉⲕⲧⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя [ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲧы ⲕⲩⲇⲁ ⲡⲟⲥⲙⲉⲗ ⲧⲩⲧ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲡⲟⲡⲉⲣⲉⲧь ⲥыⲏⲟⲕ ⲁⲡⲣυⲟⲣυ ⲏⲉⲇⲉⲉⲥⲡⲟⲥⲟⳝⲏⲟύ ⳝⲗяⲇυ[ <emoji document_id=5442804822048780010>😫</emoji> ]"
, "[ <emoji document_id=5442804822048780010>😫</emoji> ] ⲭⲩяⲙυ ⲩⳃⲉⲗьⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲕⲣⲟⲉⲙ [ <emoji document_id=5442804822048780010>😫</emoji> ]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl4))
            await sleep(0.1)
            await sleep(time)

    async def караcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>𐌺ᥲρᥲ ɜᥲκ᧐нчᥙ᧘а ʍᥴᴛᥙᴛь ᥴынκᥲʍ ᧐ᴛρ᧐дᥙᥔ <emoji document_id=5339236895501069653>🚬</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>𐌺ᥲρᥲ нᥲчᥲ᧘ᥲ ʍᥴᴛᥙᴛь ᥴынκᥲʍ ᧐ᴛρ᧐дᥙᥔ <emoji document_id=5339236895501069653>🚬</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl5 = ["〔<emoji document_id=5339236895501069653>🚬</emoji> 〕накатил на тя клеймо хуем слыш〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕в пепел тя хуем стер нах〔<emoji document_id=5339236895501069653>🚬</emoji> 〕","〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄᴀᴧ нᴀхуй ᴋᴀᴩыбᴇᴧьный〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи ᴄучий ᴛы〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴋᴀᴋ ᴧᴀйᴛ ʙᴇᴩᴄия ᴄ᧐ᴄи нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄи ᴇᴨᴛᴀ ʍнᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи ʙ ᧐ᴦнᴇ нᴀхуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴧᴀʙᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʙ ᴨᴩᴀх хуᴇʍ ʙызжᴇн〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴛя хуᴇʍ зᴀжᴇᴦ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ʍ᧐й хуй зᴀжᴇᴦ щᴇᴋи ᴛʙᴀи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ʍ᧐й ᴀᴋуᴩᴀᴛнᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи ʍ᧐й хуй ᴋᴀᴋ ɯᴀʍᴀн ᴋинᴦ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ɯᴧюхᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴋᴀᴋ ʍᴀᴛь учиᴧᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ʙ ᴀниʍᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴩᴇзʙᴀ ʍнᴇ ᴛᴀᴋ ᴛ᧐ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴧ᧐щи ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᧐бᴧиᴋᴇ ʍᴀᴛᴇᴩи ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴨᴩᴀʙиᴧᴀʍ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴛᴀᴋ ᴛ᧐ᴋ ᴨ᧐ᴋᴀ ᴄ᧐ᴄᴇɯь хуй я ᴛʙ᧐ю ʍᴀᴛь хуᴇʍ ᴨизд᧐ɯу ᴨ᧐ ᴦубᴇ ᴇᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ ᴋ᧐ᴨᴇйᴋи ᴄ᧐ᴄи хуй ɯᴧюхᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ бᴀᴛᴀн ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ɯᴧину нᴀ хуй ᧐ᴨᴧᴀчиʙᴀй ᧐чᴋ᧐ʍ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄᴇɯь хуй ᴨ᧐ᴋᴀ ᴨᴩ᧐ᴄиɯьᴄя ᴨ᧐д яицᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴨдд ᴄ᧐ᴄи хуй ᴋᴀᴩ᧐чᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴦ᧐няᴇɯь нᴀ хуᴇ ʍᴀᴇʍ ᴦ᧐нщиᴋ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴧᴇйᴋᴀ ᴄ᧐ᴄи хуй ʍ᧐й бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы дᴇɯᴇʙᴀ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ɯᴧюхᴀ д᧐ᴩ᧐ᴦᴀя ᴄᴧыɯ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋᴀ нᴀ ᴨ᧐ᴧу ʙᴀᴧяᴇɯьᴄя ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴩᴀб᧐ᴛᴀᴇɯь нᴀ ʍ᧐й хуй ᴋᴀᴋ нᴀ дядю ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴨᴩиᴧᴀжᴇнии ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐ʙᴛᴀᴩизуйᴄя ʙ хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴧᴇйᴄя ʙ хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ɸ᧐ᴛᴋᴀй ʍ᧐й хуй у ᴄя ʙ᧐ ᴩᴛу ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋᴀ ᴄ᧐ᴄᴇɯь ᴛы ʍ᧐ᴧиɯьᴄя ʙ хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыᴦᴩужᴀйᴄя ʙ хуй ʍ᧐й ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐дъᴇзжᴀй нᴀ ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴨᴀᴩᴀднᴀй ᴄ᧐ᴄи хуй ᴄᴧыɯ ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐д д᧐ждᴇʍ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʍᴇᴩзни нᴀ хуᴇ ʍᴀᴇʍ ᴄцуᴋᴀ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ дᴇндᴩᴀᴩий ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи ʍнᴇ хуй цʙᴇᴛ᧐чнᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ ʍᴇᴄᴛᴇ ᴄʙ᧐ᴇʍ ну нᴀ хуᴇ ᴇᴄᴧи чᴇ ʍᴀᴇʍ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴛиɯᴋᴀʍи хуй ʍ᧐й ᴄ᧐ᴄи бᴧядь〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зʙᴇᴩɯᴀй ʍ᧐й хуй ᴩᴛ᧐ʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ɯᴇᴧ нᴀ хуй ʍ᧐й иᴧи ɯ᧐〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ 3 чᴀᴄᴀ н᧐чи ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴨᴩᴀʙᴧяйᴄя ʙ ʍ᧐й хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴦᴩᴇйᴄя нᴀ ʍ᧐ᴇʍ хуᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴨᴧᴀʍᴇни ᴄинᴇʍ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ʍ᧐й и ᧐ᴦᴧядуйᴄя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴨ᧐ᴄᴧᴇдняя ɯᴀᴧᴀʙᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀиᴋᴀяᴄь ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙчᴇᴩᴀɯнᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ʍыɯ ᴄ᧐ᴄᴇɯ хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴄинᴇй ᴋ᧐ɸᴛᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋᴀᴋ ɯᴧюɯᴋᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ ᴄᴛ᧐нᴀʍи ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы б᧐йᴄя ʍ᧐й хуй ᴄᴧыɯ ᴄцучᴀᴩᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы яᴋ ᴋᴀᴩᴀᴧᴇʙᴄиᴋй ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴀнᴀᴧ᧐ʍ ᴄᴧыɯ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨиздᴀᴋ᧐ʍ ᴄᴧыɯ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐ᴩᴀᴧ᧐ʍ ᴄᴧыɯ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы н᧐ᴩʍ ᴄ᧐ᴄи хуй ᴋᴀᴩ᧐ч〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᧐хᴩᴇнᴇᴛь ᴛы ᴄ᧐ᴄи ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩиɯᴇᴧ нᴀ ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ уᴋᴩᴀинᴄᴋий ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы здᴩᴀᴄᴛᴇ ʙ хуй ʍ᧐й ᴦ᧐ʙ᧐ᴩи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋ᧐ᴩᴀᴛᴋᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴛ᧐ʙᴀᴩ ʍ᧐й ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴩᴀᴄʍᴀᴛᴩиʙᴀй ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᧐ɸиᴄᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋᴀ ᴨᴧᴀчу ᴛᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ ᴦᴩᴀɯи ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ 1 ᴩубᴧь ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ дᴇнь ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴀдᴩᴇᴄу ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴨᴀᴄᴨ᧐ᴩᴛᴇ ᴨᴩ᧐ᴨиᴄᴀн ᴋᴀᴋ ᴄ᧐ᴄᴀᴛᴇᴧь ʍᴀᴇᴦ᧐ хуя ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʍиᴧᴧи᧐нᴀ хуй ᴄ᧐ᴄи 〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ʍ᧐й хуй дᴧя ᴛʙ᧐их ᴋᴧыᴋ᧐ʙ 1 нᴀ ʍиᴧᴧи᧐н〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋᴀᴋ ᴩᴀб᧐чий ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴩ᧐б᧐ᴛᴇзиᴩ᧐ʙᴀный ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ ᴄᴀбᴇᴄᴇд᧐ʙᴀнии ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ нᴀ диʙᴀнчᴇᴋᴇ ᴄ᧐ᴄи ʍᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐щуɯᴀᴇɯь ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋᴀ ᧐ᴩᴇɯь ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ дᴇᴄяᴛᴋу ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐цᴇниʙᴀй ʍ᧐й хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴀᴛʍᴇнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕","〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴀнᴋᴇᴛу ʍᴀиʍ хуᴇʍ зᴀᴨ᧐ᴧняй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴀиᴄᴋᴀᴛᴇᴧь ʍᴀᴇᴦ᧐ хуя ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴨᴧᴀзʍᴇ ᴄ᧐ᴄи ʍ᧐й хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ϶ᴛ᧐ᴦ᧐ ʍ᧐ʍᴇнᴛᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴨ᧐ᴋᴀ ᴄ᧐ᴄᴇɯ хуй ᴄᴛᴀндᴀᴩᴛнᴀ ᴄ᧐ᴄи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ʍᴇᴄяц ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну нᴀхуй ᴛы ᴄ᧐ᴄᴇɯь ʍ᧐й хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ʍ᧐ᴦᴀй ᴄ᧐ᴄи ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐ᴛ д᧐ʍᴀ ᴄ᧐ᴄи ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зд᧐ᴩ᧐ʙ᧐ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴀʍ᧐ᴄᴛ᧐яᴛᴇᴧьнᴀ ᴄ᧐ᴄи ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀᴦᴩ᧐ничнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙизᴀй ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы уʙᴧᴇᴋᴀᴇɯьᴄя ʍᴀиʍ хуᴇʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ɸ᧐ᴩᴛнᴀйᴛᴇ ᴄ᧐ᴄи хуй ʍ᧐й ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʍн᧐ᴦ᧐зᴀдᴀчнᴀ ᴄ᧐ᴄи ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋуᴨᴀй ʍ᧐й хуй ᴄᴧыɯ ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴩуᴋ᧐ʙ᧐жу ᴛя хуᴇʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴋᴀᴋ ᴦᴀᴄᴨᴀдин иᴨ ᴛя дᴇᴧᴀю ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ бᴀнᴀᴧьный ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄцуᴋᴀ уᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴧ᧐ɯ᧐ᴋ ᴄ᧐ᴄи ʍ᧐й хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴩᴀб᧐ᴛᴀй нᴀ ʍ᧐ᴇʍ хуᴇ ᴄᴧыɯ ᴄцуᴋᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴩ᧐ч хуй ᴄ᧐ᴄᴇɯь я ᴛᴀᴋ ᴨ᧐няᴧ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄи ʍ᧐й хуй ᴨ᧐ᴋᴀ дᴀюᴛ ᴛᴇ бᴧядᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй и нᴇ ʙыᴇбуйᴄя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ чᴇᴧ᧐ʙᴇᴋ ᴄ᧐ᴄи хуй ᴋᴀᴩ᧐ч〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴦᴀᴄᴛᴀᴩбᴀйᴛᴇᴩ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴄᴀᴛᴩудниᴋ ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ бᴇдняᴋ ᴄ᧐ᴄи ху йᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ɸбɸ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴋᴀʍᴇᴩᴀʍ ᴄ᧐ᴄᴇɯь хй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ дᴇᴩᴇʙ᧐ ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐чᴋᴀᴄᴛᴀ ᴄ᧐ᴄи ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ иɸ᧐нᴇ ᴄ᧐ᴄи хуй ʍ᧐й бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ зʙᴇздᴀчᴋᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ бᴇднᴀ ᴄᴛᴩᴀнᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ буᴩундᴇ ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ ᧐ᴛчᴇᴛᴀх ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ бᴀнᴋᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴩюᴋᴀзᴀᴋ᧐ʍ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы 62 ᴦ᧐дᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ нᴀᴄиᴧᴇния ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ бᴇ нᴇщᴀᴄᴛнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴦ᧐д᧐ʙ᧐ʍ д᧐х᧐д᧐ʍ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴧ᧐ɯ᧐ᴋ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋᴀᴋ ʙ ᴄɯᴀ ᴄ᧐ᴄи хуй ʍᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ᴋᴀᴋ ʍᴇдʙᴇж᧐н᧐ᴋ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄцуᴋᴀ ᴄʍᴇйᴄя ʙ хуй ʍ᧐й ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙᴀхуᴇ ᴄ᧐ᴄᴇɯ хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы бᴧя ᴨ᧐ 10 бᴀᴋᴄ᧐ʙ ᴄ᧐ᴄи хуй ᴀᴩу〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄчучья ᴩᴀзʙᴧᴇᴋᴀйᴄ нᴀ ʍ᧐ᴇʍ хуᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ б᧐ᴦᴀᴛый ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴄᴛᴇ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴀᴩᴦᴇнᴛинᴇ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы д᧐нᴀᴛиɯь нᴀ ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы бᴇзᴩᴀб᧐ᴛнᴀ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐д нᴀᴩᴋᴀᴛ᧐й ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ ᴨ᧐ᴄ 1 ᴄ᧐ᴄи хуй ᴄᴧыɯ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄи хуй ᴨ᧐ᴋᴀ ᴛᴇ ʍᴀᴛь ᴩᴀзᴩᴇɯᴀᴇᴛ ᴄцуᴋᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴛᴇʍᴨᴇᴩᴀᴛуᴩᴀй ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴀйᴋью н᧐ᴧь ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴛя ɸуᴩниᴛуᴩ᧐й иᴨ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну нᴀ ɸᴀнᴛᴀзии ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну зᴀ ᴩ᧐буᴋᴄы ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋ᧐дᴇᴩ ʍᴀᴇᴦ᧐ хуя ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕я ᴛᴇ хуᴇʍ зʙᴇзды ʙ ᴦᴧᴀзᴀх ʙызʙᴀᴧ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕у ᴛя ʙ ᴦᴧᴀзᴀх ᧐ᴛ хуя ᴩᴇбиᴛ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ᴨ᧐ᴋᴀ ᴛᴇ нᴇ ᴄᴛᴀᴧ᧐ хужи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʍ᧐й хуй ᴄ ᴛᴀб᧐й ᴩᴀз᧐бᴩᴀᴧᴄя нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄын᧐ᴋ ɯᴧюхи нᴇ нᴀдᴇйᴄя чᴛ᧐ ʍ᧐й хуй ᴛᴇбя ᴋᴀᴦдᴀ ᴛ᧐ ʙ жизнᴇ ᧐ᴛᴨуᴄᴛиᴛ дᴀжᴇ ᴄʍᴇᴩᴛь нᴀхуй ʍ᧐й хуй ᴄ ᴛʙ᧐ᴇй ᴦуб᧐й нᴇ ᴩᴀзᴧучиᴛ ᴄᴧыɯ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴄᴧыɯ ᴄ᧐ᴄи ʍ᧐й хуй ᴨ᧐ᴋᴀ ᴛᴇ ᴛʙ᧐й ᧐ᴛᴇц нᴀ ɯᴋ᧐нᴋᴇ ᴋᴀᴛ᧐ᴩ᧐ʍу ᴛы ᴨ᧐ зʙ᧐нᴋу нᴀхуй ᴩᴀᴄᴋᴀзуᴇɯь ᴋᴀᴋ ᴛя ᴧᴀхᴀ ᴨизд᧐ɯᴀᴛ ᴛᴀʍ ᴦᴩиᴛ ᴋᴀᴋ нᴀд᧐ ᴄ᧐ᴄᴀᴛь ʍ᧐й хуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʙ бᴩᴀузᴇᴩᴇ нᴀ хуй ʍ᧐й ᴦубу ᴋуᴄᴀй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ ᴋᴀᴋ ᴄᴩᴀх ᴄ᧐ᴄи хуй ʍ᧐й нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы хуй ᴄ᧐ᴄи яᴋ ᴄучий бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ уᴋᴩᴀинᴄᴋи ᴄ᧐ᴄи хуй ʍᴇ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ᴋᴀᴋ ᴛя учиᴧи бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄи хуй ᴋᴀᴋ нᴀиʍᴇн᧐ʙᴀный〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы нᴀ ʍ᧐ᴇʍ хуᴇ ᴋᴀᴋ нᴀ ᴦиᴛᴀᴩᴇ иᴦᴩᴀᴇɯь нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄ зᴀʙыʙᴀниᴇʍ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛᴀᴨ᧐ᴩ᧐ʍ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴨ᧐д дуᴧ᧐ʍ ᴨᴇᴄᴛᴀᴧᴇᴛᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄиᴧу϶ᴛ᧐ʍ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙ ᴨᴧᴀщᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙ ᴛᴩᴇᴄиниᴋ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄ зᴀиᴋᴀниᴇʍ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕","〔<emoji document_id=5339236895501069653>🚬</emoji> 〕нᴀ ᴋучᴋᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕чᴇᴩᴛᴀʙщин᧐й ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴄ᧐ᴄиᴩуй хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙᴄᴋидуй ᴩуᴋи нᴀ ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙ ᴄᴨᴀᴧьниᴋᴇ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕дᴀᴧᴇᴋ᧐ нᴀ хуй бᴇᴦи нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ ʍᴀᴋᴄиʍ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ ᴄᴛиᴧᴇʙый ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕᧐ᴛᴄᴛуᴨᴀй ᧐ᴛ хуя ʍᴀᴇᴦ᧐ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕нᴇ ᴄᴨи нᴀ хуᴇ ʍᴀᴇʍ бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕бᴧᴀᴦ᧐дᴀᴩнᴀ ᴄ᧐ᴄи хуй ᴄᴧыɯ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕иᴄᴛᴧᴇʙɯᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ ᴄцуᴋᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ нᴇʍᴇц ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙ ɯᴇнᴇᴧᴇ ᴄ᧐ᴄи хуй нᴀхуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᧐ᴨухɯᴇ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ ᴩуᴄя нᴀх ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴩжᴀʙ᧐ ᴄ᧐ᴄи хуй ᴄᴧыɯ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐ᴄи хуй ᴄᴧыɯ бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩᴇбᴧижᴀй ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы бᴇᴧ᧐ᴋ᧐жᴇ нᴀху ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ɸᴀнᴀᴛичнᴀ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ʙᴀᴇный ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ɸᴧяжный ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴩᴀзᴦибᴀйᴄя нᴀ ʍ᧐й хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴧᴇʙ᧐ʍу ᴋᴩᴀю ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧɯ ᴄ᧐ᴄи зᴀ ᴨᴧᴀнɯᴇᴛ хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴛ᧐нь ʙ ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыдиᴩᴀй ʍ᧐й хуй языᴋ᧐ʍ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ иᴧᴇ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴇ дʙиᴦᴀйᴄ нᴀ хуᴇ бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴩᴀзбиᴛыʍ ᴧиц᧐ʍ ᴄ᧐ᴄи нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴇᴨᴛᴀ ᴄ᧐ᴄи хуй щᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ ᴨᴩᴀʙ᧐ʍу бᴇᴩᴇᴦу ᴄ᧐ᴄи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴛᴩᴀɯиɯьᴄя ᴋ хую нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄ᧐ ᴄʙᴇᴛ᧐ʍ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙдʙᴀᴇʍ нᴀхуй ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʍ᧐ᴧ᧐д᧐ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕нᴇ ᴦ᧐ʙ᧐ᴩи ʙ ʍ᧐й хуй ᴨᴩᴀʙду нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴀ ᴛы ᴄᴧыɯ ᴩᴀᴄᴋᴀзуй бᴀᴛᴇ ʍᴀᴇʍу ᴋᴀᴋ ᴛы ᴄ᧐ᴄᴇɯь хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴨᴩижиʍᴀй ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴦинь ʙ ʍ᧐й хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыᴧᴀзий ʙ ᴨᴇниᴄ ʍ᧐й нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴀʙᴛ᧐ʍᴀᴛ᧐ʍ нᴀх ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴄ᧐ᴄи хуй ᴄцуᴋᴀ ᴋᴀᴋ ᧐ᴄᴛᴀн᧐ᴋ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ изᴇч ᴄ᧐ᴄи хуй д᧐ʍᴀɯний ᴛы〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄиᴩуй хуй бᴧя ᴨ᧐ᴋᴀ дᴀю ᴛᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ ɯᴀᴄᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ ᴇбучий ᴛы〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴋᴩᴀях ᴄ᧐ᴄи хуй нᴀх дуᴩᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄиᴩуй ᴨᴇниᴄ ᴛᴇ ᴩᴀзᴩᴇɯᴀю я〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ яᴋ ɯᴧюх᧐ʙый ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀᴨᴇчᴀᴛᴀй ʍ᧐й хуй ᴩᴛ᧐ʍ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы чᴀᴄ᧐ʙ᧐ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ хᴇᴩᴄ᧐нᴇ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ʍ᧐ᴄᴋʙᴇ ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴛя ᴨᴩижᴀᴧ ᴋ хую нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄиᴩуй хуй ᴀдᴄᴋи〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴋᴀᴋ ᴄᴀᴛᴀнᴀ иᴨ ᴛя нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀᴨᴧиᴛᴀйᴄя нᴀ хуᴇ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы жᴇᴄᴛ᧐ᴋᴀ ᴄ᧐ᴄи хуй ʍ᧐й бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨуᴛᴀйᴄя ᴄ᧐ᴄуя хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩ᧐буй ᴄ᧐биᴩᴀᴛьᴄя нᴀ хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ иᴨ ᴛя хуᴇʍ ᴋᴀᴋ дᴇᴛᴋᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ нᴇ᧐бычнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩиʍᴇᴩнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ ᴨᴩ᧐ɯᴧᴀй нᴇдᴇᴧи ᴄ᧐ᴄᴀй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴨ᧐няᴧ ɯ᧐ ᴄ᧐ᴄᴇɯь〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴛᴩᴀнн᧐ буᴩᴋᴀй ʙ хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋᴀᴋ ϶ᴛ᧐ ᴛы ᴄ᧐ᴄᴇɯь хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩ᧐яʙᴧяйᴄя ʙ ʍ᧐й хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы иᴦᴩᴀйᴄя ᴄ ʍ᧐иʍ хуᴇʍ ᴩᴛ᧐ʍ и ᴄʍᴇйᴄя изиз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ изʍᴇняйᴄя ʙ хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ я ᴛя ᴄиᴧьн᧐ хуᴇʍ нᴀᴨуᴦᴀᴧ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐ᴛчᴇᴛᴧиʙᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄнᴀчᴀᴧᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы иᴦᴩ᧐й ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴋᴀждыʍ днᴇʍ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы дᴇᴛᴄᴋи ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы цᴇничнᴀ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴀ дуᴩд᧐ʍᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ дᴩ᧐жᴀщиʍи ᴩуᴋᴀʍи ᴄ᧐ᴄи нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ᴨᴩиюᴛᴀ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ʙ᧐ᴄᴨиᴛᴀᴛᴇᴧьницᴀ ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄдᴇᴩжᴇн᧐ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыᴛᴀᴄᴋиʙᴀй ʍ᧐й хуй ᴄ ᴩᴛᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ ʍᴇᴄᴛᴀ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐дᴩ᧐бнᴇᴇ ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐д᧐зᴩиᴛᴇᴧьнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ ᴄʙинья ᴛя ж ɸиᴩ ᴇбᴇᴛ нᴀхуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕нᴀх ᴛы ʙ ʍ᧐й хуй ᴦᴩиɯь ɯ᧐ ᴋ᧐хᴀᴇɯь ᴇᴦ᧐ ᴨᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ зᴀ ʍᴀᴛь ᴄʙ᧐ю ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ зᴀ ᧐ᴛцᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ зᴀ дᴇдᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧᴀɯ нᴀ ᴨ᧐ᴄ 5 ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴦ᧐ᴄудᴀᴩᴄᴛʙᴇнᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴩᴇᴋ᧐ᴩднᴀ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕","〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᴄᴄᴄᴩ ᴄ᧐ᴄи хуй бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ᴛя хуᴇʍ ᴋᴀнɸиᴄᴋую ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну дᴇʙᴄᴛʙин᧐ᴄᴛи ᴛя хуᴇʍ ᴧиɯиᴧ нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴨ᧐д ᴨиʙ᧐ʍ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴨ᧐д ʙин᧐ʍ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀ иʍᴨᴇᴩᴀᴛ᧐ᴩᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ϶ᴧᴇʍᴇнᴛᴀᴩнᴀ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴨ᧐ᴋᴀ я ᴛᴇбя ᴇбу ᴛы ʙ ʍ᧐й хуй ᴨыᴛᴀᴇɯьᴄя ч᧐ ᴛᴀ ʙыᴦᴀʙᴀᴩиʙᴀᴛь и бᴀйᴛиᴛь ʍ᧐й ᴨᴇниᴄ дᴧя чᴇᴦ᧐ ᴄᴋᴀжи ʍнᴇ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ж ᴧ᧐жᴋᴀй ᴄ᧐ᴄᴇɯь ʍ᧐й хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыʍᴇɯиʙᴀй ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴋ᧐ɯᴋᴀ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ нᴀᴋᴀзᴀниᴇ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄʙᴇжᴇʍ᧐ᴧᴀᴛᴀ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄ᧐чнᴀ ᴄ᧐ᴄи хуй ʍ᧐й нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐ᴄ᧐б᧐ ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴄᴋᴀᴛинᴀ ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᧐бниʍᴀй ʍ᧐й хуй нᴀху〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴇ нᴀх᧐диɯь ʍ᧐й хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄ᧐ᴄи ʍ᧐й хуй ᴋᴀᴋ ᴀʍ᧐нᴦ ᴀᴄ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʙ ᴩᴀɸᴛᴇ ᴄ᧐ᴄи хуй ʍ᧐й〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴀᴄᴀᴄин᧐ʍ ᴋ хую ᴨ᧐д᧐бᴩᴀᴧᴄя нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴄʙ᧐ᴧᴀч ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴇ нᴀйдᴇɯь хуй ᴧучɯᴇ ʍᴀᴇᴦ᧐ нᴀху〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄиᴧьнᴇᴇ ᴄ᧐ᴄи хуй ʍ᧐й бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ бᴇᴄ ᴄ᧐ᴄи ʍ᧐й хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ᴦᴇᴩбᴀᴩий ᴄ᧐ᴄи хуй ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ ᴛы ᴋᴀᴋ ᴨᴀᴛ᧐ʙый ᴄ᧐ᴄи хуй нᴀх〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴋᴀᴛᴀн᧐ʙᴇц ᴇбучий ᴄ᧐ᴄи хуй ʍ᧐й бᴧя〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы нᴇ ʙыдᴇᴩжиɯь нᴀᴨ᧐ᴩᴀ ʍ᧐иʍ хуᴇʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴋᴀᴋ ɸюᴩᴇᴩ нᴀхуй ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙыжиʙᴀй нᴀ хуᴇ ʍᴀᴇʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴨᴇᴩʍу ʍᴀю ᴨьᴇɯь ᴄᴧыɯ ᴄуᴋᴀ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛʙᴀя ʍᴀᴛь нᴇ ᴄ᧐ᴧь нᴀ ᴧ᧐жᴋᴇ ᴦᴩᴇᴇᴛ ᴀ ʍ᧐ю ᴋᴀнчу и ᴨ᧐ᴛ᧐ʍ ᴨ᧐ ʙᴇнᴀʍ ᴇᴇ ᴦᴀняᴇᴛ ᴋᴀᴋ ʍ᧐й хуй зᴀ щᴇᴋ᧐й ᴄᴧыɯ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛʙ᧐я ʍᴀᴛь ᴨ᧐ᴋᴀ ʍ᧐й хуй ᴧижᴇᴛ ʙᴄᴨ᧐ʍинᴀᴇᴛ быᴧыᴇ дᴇньᴋи и ᴋᴀᴋ ᴛʙ᧐ᴇᴦ᧐ ᧐ᴛцᴀ нᴀ ɸᴩ᧐нᴛ нᴇ зᴀбᴩᴀᴧи и нᴇ убиᴧи нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ я нᴀхуй ʙ ᴨиздᴀᴋ ᴛʙᴀᴇй ʍᴀʍᴀɯᴇ нᴀᴄᴩᴀᴧ ᴋᴀᴩ᧐ч и ᴨ᧐ᴛ᧐ʍ нᴀᴄцᴀᴧ ᴇщᴇ ʙ  нᴇᴦ᧐ ᴨ᧐ᴛ᧐ʍ ᴋ᧐нчиᴧ и нᴀхᴀᴩьᴋᴀᴧ ᴛудᴀ хуᴇʍ ᴄʙ᧐иʍ ᴨᴇᴩᴇʍᴇɯᴀᴧ и ᴛы ᴩᴀдиᴧᴄя нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ я ᴛя ᴋᴀᴋ ᴨᴩᴇзиᴋ нᴀ хуй нᴀᴛянуᴧ и ᴇбᴀᴧ ᴛʙ᧐ю ʍᴀᴛь нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ я жᴇ ᴛʙ᧐ю ʍᴀᴛь ʙ ᴦᴀзᴀʙᴀй ᴋᴀʍᴇᴩᴇ ᴇбу нᴀхуй и ᴋ᧐ᴦдᴀ ᧐нᴀ зᴀдыхᴀᴇᴛᴄя ᧐нᴀ ᴋᴩичиᴛ чᴛ᧐ ᴧюбиᴧᴀ ʍ᧐й хуй ᴄуᴋᴀ ᴀ ϶ᴛ᧐ жᴇ ᴨᴩиᴨᴀдᴋи ᴨᴩ᧐ᴄᴛᴀ у нᴇᴇ ᴨиздᴀ ᧐нᴀ ᴛуᴨᴀя ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ ᴛы ᴄучий нᴀхуй ᴛы ʙ ʍ᧐й хуй ɸᴀнᴛᴀзии ᴋидᴀᴇɯь ʙᴄᴇ ᴩᴀʙн᧐ жᴇ нᴀ ᴛ᧐ʍ ᴄʙᴇᴛᴇ ᴨᴇᴩᴇд хуᴇʍ нᴇ ᧐ᴨᴩᴀʙдᴀᴇɯьᴄя нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ ᴛы хуᴇᴄ᧐ᴄ я жᴇ ᴛʙ᧐ю ʍᴀᴛь ᴇбу нᴀхуй ᴀ ᴛы ᴇщᴇ ᴨᴩи ϶ᴛ᧐ʍ ʍ᧐ᴇʍу хую ᴋᴀʍᴨᴧиʍᴇнᴛы ᴦᴀʙᴀᴩиɯь нᴀхуй ᴇбᴀᴛь ᴛы ᴛуᴨ᧐й ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨᴩиниʍᴀй ᴩᴇɯᴇнья ᴋᴀᴋ ᴄ᧐ᴄᴀᴛь ʍ᧐й хуй ᴄᴧыɯ ᴀ ᴛ᧐ ᴛы ᴛуᴨ᧐й ждᴇɯь ᴋᴀᴦдᴀ ᴛᴇ ʍᴀᴛь ᴨ᧐ʍ᧐жᴇᴛ ᴀ ᧐нᴀ ужᴇ ужᴇ ᴄ᧐ᴄᴇᴛ ʍ᧐й хуй ᴄᴧыɯ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀᴛ᧐ ᴋᴀᴋ ᴋᴀᴩᴀᴧю ʍнᴇ ᴄ᧐ᴄᴇɯь хуй ᴛиᴨᴀ ᴛы ɯуᴛ дᴧя ʍᴀᴇᴦ᧐ хуя и ᴛы ᴇᴦ᧐ ᴩᴛ᧐ʍ ʙᴇᴄᴇᴧиɯь ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ʙ ᧐дᴇждᴇ ʍнᴇ нᴀхуй ᴄ᧐ᴄи хуй〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы зᴀᴄᴩᴀᴧ ʍнᴇ хуй ᴩᴛ᧐ʍ ᴄᴧыɯ〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴋᴧᴀᴄнᴀ нᴀхуй ᴄ᧐ᴄи ʍ᧐й хуй нᴀху〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну я ж ᴛʙ᧐ю ʍᴀᴛь нᴀхуй ᴧ᧐ɯᴀдяʍи чᴇᴛʙᴇᴩᴛ᧐ʙᴀᴧ ᴄуᴋᴀ и ᴨ᧐ᴛ᧐ʍ ᴇᴇ ᴄжᴇᴦ нᴀхуй нᴀ ᴋᴀᴄᴛᴩᴇ ᴄᴧыɯ ᴛ᧐ᴋᴀ я юзᴀᴧ нᴇ бᴇнз ᴀ ᴄʙ᧐ю ʍᴀчу ᴋᴀᴦдᴀ жᴇᴦ нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ нᴀхуй я ж ᴋуᴄᴋи ᴛʙ᧐ᴇй ʍᴀʍᴀɯи ʙ ɸундᴀʍᴇнд ᴛʙ᧐ᴇ будᴋи зᴀᴧиʙᴀᴧ и ʙʍᴇᴄᴛ᧐ изʙᴇᴄᴛи ᴄʙ᧐ю ᴄᴨᴇᴩʍу юзᴀᴧ ᴄᴧыɯ я ᴋᴀᴋ ɯᴀʍᴀн нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʙ дᴩуᴦих ᴄᴛᴩᴀнᴀх ᴛы ᴄ᧐ᴄᴇɯь ʍ᧐й хуй ᴋᴀᴋ ᴨуᴛᴇɯᴇᴄᴛʙᴇнниᴋ нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ я ᴋᴀᴋ дьяʙ᧐ᴧ нᴀхуй ᴄ ᴛᴩизубц᧐ʍ ʙ ʙидᴇ хуя ᴄʙ᧐ᴇᴦ᧐ ᴄижу и ᴛыᴋᴀю ᴛя иʍ нᴀхуй ʙ жᴀᴩᴋ᧐ʍ ᴨᴧᴀʍᴇни ᴀдᴀ нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ я ж ᴛʙ᧐ю ʍᴀᴛь нᴀ ᴋиɯᴋᴀх ᴛʙ᧐ᴇᴦ᧐ ᧐ᴛцᴀ хуᴇᴄ᧐ᴄᴀ ᴨ᧐ʙᴇᴄиᴧ нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ʙ ᴨ᧐ʍᴇщᴇнии ʍнᴇ хуй ᴄ᧐ᴄᴇɯь и ᴨᴇᴩᴇд ᴛᴇʍ чᴛ᧐ бы ᴇᴦ᧐ ᴋуᴨиᴛь ᴨᴩᴇдᴧ᧐ᴦᴀᴇɯь ʍнᴇ ᴛя ʙ ᴀчᴋ᧐ ᴛʙ᧐ᴇ ᴦᴩязн᧐ᴇ ʙыᴇбᴀᴛь нᴀхуй ᴀ ᴛы ж ᴇᴦ᧐ ᴄуᴋᴀ нᴇ ᴨ᧐ʍыᴧ ɯᴧюхᴀ ᴛы ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ дᴧя ᴛя ᧐быдᴇнн᧐ᴄᴛь ʙдиᴇᴛь чᴇй ᴛ᧐ хуй ᴨᴇᴩᴇд ᴦуб᧐й ᴄʙ᧐ᴇй нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ я ᴄʙ᧐иʍ хуᴇʍ ᴛя ᴋᴀᴩᴀю нᴀхуй ᴄᴀᴧ᧐ ᴛы хᴀдячᴇᴇ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕я ж ᴛя хуᴇʍ ᴋᴀᴋ ᴋᴩиᴨᴀ ᴄуᴋᴀ нᴀ ʍидᴇ зᴀхᴀʙᴀᴧ ᴀ ᴛы дᴀжᴇ ᴇᴛ᧐ᴦ᧐ нᴇ ᴨ᧐няᴧ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ нᴀ ɸᴀнᴛᴀзии ʍнᴇ хуй ᴄ᧐ᴄи нᴀхуй ᴛы ж ɸᴀнᴛᴀзиᴩ᧐ʙᴀᴛь ʍ᧐жᴇɯь ᴛ᧐ᴋᴀ ᴨ᧐ᴋᴀ ᧐чᴋ᧐ ᴄᴇ ᴨᴀᴧьцᴇʍ ʍᴀᴄиᴩуᴇɯь ᴋᴀᴋ ᴄ᧐ᴄᴇɯь ʍ᧐й хуй ɯᴧюхᴀ ᴛы ᴨид᧐ᴩᴄᴋᴀя ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕","〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄᴧыɯ я ᴛя ᴋᴀᴋ дᴇʍ᧐н ᴀдᴀ нᴀхуй ᴨ᧐ᴋᴀᴩᴀᴧ ᴄʙ᧐иʍ ᴨᴇниᴄ᧐ʍ ᴀ ᴛы дᴀжᴇ нᴇ ᴨ᧐няᴧ чᴛ᧐ ᴛы ᴄ᧐ᴄᴇɯь ʍ᧐й хуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴨ᧐ᴋᴀ ᴨ᧐ᴄуду ʍ᧐ᴇɯь и ᴛʙ᧐я ʍᴧᴀдɯᴀя ᴄᴇᴄᴛᴩᴀ зᴀх᧐диᴛ и ᴄᴨᴩᴀɯиʙᴀᴇᴛ чᴛ᧐ ᴛы дᴇᴧᴀᴇɯь ᴀ я ᴨᴩи ϶ᴛ᧐ʍ ᴇбу ᴛᴇбя нᴀхуй ᴛы ᴦ᧐ʙ᧐ᴩиɯь чᴛ᧐ ʍы ᴄ ᴛᴀб᧐й иᴦᴩᴀᴇʍ бᴧядь ᴀ ᴛʙ᧐я ᴄᴇᴄᴛᴩᴀ жᴇ ᴨ᧐ниʍᴀᴇᴛ чᴛ᧐ ᴛы ᴨᴩ᧐ᴄᴛ᧐ ᴨид᧐ᴩ ᴦн᧐йный и ᴧюбиɯь ʍ᧐й хуй нᴀхуй ᴇбᴀᴛь ᴛы ᴛуᴨ᧐й ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ ᴋᴀᴦдᴀ ᴛы ʍ᧐й хуй ᴨᴩ᧐ᴄиɯь ч᧐ ᴛᴀ ᴨᴇᴩᴇбиᴛь нᴀхуй ᴋᴀждый ᴩᴀз я ᴨᴇᴩᴇбиʙᴀю нᴀхуй ᴄʙ᧐иʍ хуᴇʍ ᴨ᧐ ᴇбᴧᴇᴛᴀʍ ᴋᴀжд᧐ᴦ᧐ чᴧᴇнᴀ ᴛʙ᧐ᴇй ᴄᴇʍьи ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛыж ᴄᴧыɯ ᴋᴀᴦдᴀ ᴛы нᴀхуй нᴀ ʍ᧐ᴩᴇ ᴨᴧыʙᴇɯь нᴀхуй и ʙидиɯь ᴋᴀᴋ ᴋᴀᴋ᧐йᴛᴀ ᴀᴦᴩ᧐ʍный ᴋᴀᴩᴀбыᴧь нᴀ ᴛя ᴨᴧыʙᴇᴛ ᴛы ᴨᴩᴇдᴄᴛᴀʙᴧяᴇɯь чᴛ᧐ ϶ᴛ᧐ ʍ᧐й хуй и ᴄᴩᴀзу ᧐ᴛᴋᴩыʙᴀᴇɯь ᴩ᧐ᴛ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛыж нᴀхуй ᴋᴀᴋ духᴀʙᴇнᴇц ᴨᴩиниʍᴀᴇɯь ᴨ᧐дᴀᴛи ᧐ᴛ ʍ᧐ᴇᴦ᧐ хуя ᴄʙ᧐иʍ ᴩᴛ᧐ʍ ᴄᴧыɯ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ну ᴛы ᴄᴧыɯ я ᴛᴀᴋ ᴨ᧐ниʍᴀю я ᴛᴇбᴇ ʙᴄᴇ зубы ᴛʙ᧐и нᴀхуй ʙыбиᴧ чᴛ᧐ ᴛы ʍнᴇ ʙ хуй б᧐ᴧьɯᴇ нᴇ ᴄᴋᴀжᴇɯь ᴋᴀᴋ ᴛы ᴦ᧐ʙ᧐ᴩиɯь иᴧи хᴩюᴋᴀᴇɯь ʙзᴩᴀзуʍиʙ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛыж ᴄуᴋᴀ ᴋᴀᴋ ʍиᴄᴛᴩᴇ дудᴇц нᴀхуй ᴛ᧐ᴋᴀ дᴧя ᴛя дудᴋᴀ ϶ᴛ᧐ нᴇ ᧐бычнᴀя ɸᴧᴇйᴛᴀ ᴀ ʍ᧐я ᴋ᧐жᴀнᴀя ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ч᧐ᴛы нᴀхуй ᴋᴩяхᴛиɯь ʍнᴇ ʙ ᴩуᴋи хуᴇᴄ᧐ᴄ ᴨᴩ᧐ ᴩуᴋи ᴛы ɯ᧐ дуᴩᴀ ᴨ᧐ниʍᴀᴇɯь я ᴛя ᴩуᴋᴀʍи ᴋᴀᴋ ʍᴧᴀдᴇнцᴀ нᴀ хуᴇ ᴄʙ᧐ᴇʍ ʙᴄᴋᴩучу нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ я ᴨ᧐ ᴦ᧐ᴧ᧐ʙᴀʍ ᴋᴀᴋ ᴋиᴧᴧуᴀ ᴛя ᴇбу нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕я ᴛя ᴄʙ᧐иʍ ᴀдᴀᴨᴛиʙᴀʍ нᴀхуй ᴇбᴀᴧ ᴄᴧыɯ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛы ᴄᴧыɯ ᴨ᧐ᴋᴀ нᴀ чᴀᴄᴄᴀх н᧐ᴧь н᧐ᴧь ᴄ᧐ᴄи ʍ᧐й хуй нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴛыж ᴨ᧐ниʍᴀᴇɯь нᴀхуй я ᴋᴀᴦдᴀ ᴛя ʙ ᴋᴀᴛᴀɸᴀᴧᴋᴇ ᴄʙиʍ хуᴇʍ ʙᴀзиᴧ ᴛы дуʍᴀᴧ чᴛ᧐ ʍы ʙ ᴄᴀн᧐чᴋи иᴦᴩᴀᴇʍ ᴨиздᴀ ᴛы ᴛуᴨ᧐й нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄбᴀйᴛиᴧ ᴛя хуᴇʍ нᴀ уᴋᴩᴀ ᴄцуᴋу ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴛᴀн᧐й ᴛя ᴄʙ᧐ᴇй ᴋ᧐жᴀн᧐й ᴇбу ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕изᴇч ᴛя ньюɸᴀᴦᴀ нᴀхуй нᴀ хуᴇ ᴄʙ᧐ᴇʍ ʙздᴩючиᴧ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʙздᴩ᧐ᴦнуᴧ ᴛя хуᴇʍ нᴀ уᴩᴀ нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄ зᴀʍидᴧᴇниᴇʍ ʙᴩᴇʍᴇни ᴇбу ᴛя нᴀхуй ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ʍᴀʍᴀɯу ᴛʙᴀю нᴀ хуᴇ д᧐ʙ᧐зиᴧ д᧐ д᧐ʍᴀ ᴋᴀᴋ нᴀ ᴧᴀʍбᴇ нᴀхуй ᴀ ᴛы ᴄ удиʙᴧᴇныʍи ᴦᴀᴧзᴀʍи нᴀ ᴇᴇ ᴄᴧюняʙ᧐ᴇ ᴇбᴧищᴇ ᴄᴀᴛᴩᴇᴧ ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴄ᧐ ᴄʙ᧐ᴇй ʍуᴩᴀᴄᴀʍ᧐й ᴛя ᴇбу нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴋᴀᴋ ᴦ᧐ᴩдый ᴄ᧐ᴄи ʍ᧐й хуй нᴀх ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕",
"〔<emoji document_id=5339236895501069653>🚬</emoji> 〕ᴨ᧐д ᴧун᧐й ᴛя ᴇбу ᴇзᴇз〔<emoji document_id=5339236895501069653>🚬</emoji> 〕"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl5))
            await sleep(0.1)
            await sleep(time)

    async def лезвиеcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Лᥱɜʙᥙᥱ ɜᥲκ᧐нчᥙ᧘о ᥙɜρᥱɜᥲᴛь ᥴынκ᧐ʙ хуᥱᥴ᧐ᥴᥲ <emoji document_id=5341819141508574901>🚬</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Лᥱɜʙᥙᥱ нᥲчᥲ᧘᧐ ᥙɜρᥱɜᥲᴛь ᥴынκ᧐ʙ хуᥱᥴ᧐ᥴᥲ <emoji document_id=5341819141508574901>🚬</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl6 = ["[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁ ⳡⲗⲉⲏ ⲁⲃⲁⲏⲧⲁⲯⲏыύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲟ ⲙⲁⲙυⲏⲟύ ⲥⲣⲁⲕⲟύ ⲕⲣⲟⲙⲉ ⲭⲩёⲃ ⲗⲟⲃυⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⲧцⲉⲡυⲗ ⲧя ⲃ ⲇⲩⲱⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧёⲗⲕⲁ,ⲙⲟύ ⲭⲩύ ⲧⲃⲟύ ⲙυⲕⲣⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩⲣυⲏⲟύ ⲧя ⲟⲱⲡⲁⲣυⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲕⲁⲕ ⲃⲉⲇьⲙⲁⲕ,ⲩ ⲙⲉⲏя ⲉⲥⲧь ⳅⲁⲇⲁⲏυⲉ ⲏⲁ υⲥⲧⲣⲉⳝⲗⲉⲏυя ⳡⲩⲇυⳃь,ⲏⲁ ⲟⳡⲉⲣⲉⲇυ ⲧⲃⲟя ⲙⲁⲙⲕⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲧⲉ ⲧⲃⲟυ ⲅⲗⲁⳅⲏυцы ⲏⲁⲭⲩύ ⲃыⳝью υ ⲏⲁ ⲭⲩύ ⲥⲉⳝⲉ ⲟⲇⲉⲏⲩ υ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲣυⲣⲟⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲙⳅⲉⲗь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⲡⲉⲏυⲥⲉ ⲥⲧⲁⲅⲏυⲣⲩⲉⲱь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝёⲙ ⲙя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅ ⲕⲇ ⲉⳝёⲙ ⲧя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲏⲉύ ⲧⲃⲟⲉύ ⲃ ⲅⲟⲗьⲫ υⲅⲣⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ ⲏⲁ ⳅⲟⲏⲉ ⲭⲩⲉⲙ ⲃⲟⲥⲡυⲧⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲅⲟⲏяⲗⲁ ⲥыⲏⲕⲁ ⲱⲗюⲭυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲫⲣυⲕⲁ ⲃыⳝьⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲥⲟⲥёⲱь ⲙⲏⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲁⲡⲁⲏя ⲧⲃⲟύ) <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲉ ⲙⲉⲯⳝⲣⲟⲃьⲉ ⲣⲁⲥⲥⲉⳡёⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳅⲁⲗⲩⲡⲁⲙυ ⲏⲁⳝⲉⲅυ ⲏⲁ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧυⲗьⲇы ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲣⲟυⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]υⲥⲕⲩⲥⲥⲏⲟ ⲣⲁⲥⲥⲉⲕⲕⲁю ⲏⲁ ⲇⲃⲟⲉ ⳅⲁⳝⲃⲉⲏⲏⲩю ⲧⲩⲱⲕⲉⲏцυю ⲡⲁⲡⲁⲏυ ⲧⲃⲟⲉⲅⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲃⲟ ⲃⲥⲉⲭ ⲡⲟⳅⲁⲭ ⲕⲁⲙⲁⲥⲩⲧⲣы ⲉⳝⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲣυⲣⲩю υ ⲉⳝⲁⲱυⲣⲩⳝ ⲙⲉⲱⲟⲉ ⲉⳝⲁⲏⲏыύ ⲏⲁ ⲧⲉⳝⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲇⲁⲃⲁύ ⲧⲁⲙ ⳅⲁⲭⲗёⳝыⲃⲁύⲥя ⲙⲟⳡёύ ⲙⲟⲉύ ⲩⲯⲉ))ⲭⲃыⲭыыⲃ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲗⲁⳝⲟⲏⲉⲣⲃⲏыύ ⲟⲏυⳃⲁⲗыύ ⲥыⲏⲟⲕ ⲇυⲕⲁⲣⲕυ ⲥⲟⲥυⲣⲩύ υ ⲙⲁⲥⲥυⲣⲩύ ⲃⲥяⳡⲉⲥⲕυ яύцⲁ ⲙⲟυ ⲩⲯⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲩ ⲧы ⲧёⲗⲕⲁ ⲏⲁⲧⲩⲣⲉ ⲙⲟύ ⲭⲩύ ⲩⲧⲟⲙυⲗⲁ яⳅыⲕⲟⲙ ⲥⲃⲟυⲙ ⲱⲉⲣⲱⲁⲃыⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ υⳅ ⲧⲉⳝя ⲇⲉⲙⲟⲏⲟⲃ υⳅⲅⲟⲏяⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲗⲉⲏⲟⲙ ⲡⲣⲟⳝυⲗ ⲥⲉⲣⲇцⲉ ⲧⲃⲟё ⲥⲗⲟⲃⲏⲟ ⲟⲥⲥυⲏⲟⲃыⲙ ⲕⲟⲗⲟⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲏⲉ ⲃⲁⲙⲡυⲣ я ⲧⲉⳝⲉ ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⳡⲉⲥⲏⲟⳡⲏⲟύ ⲟⳝⲉⲥⲥυⲗυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲇυⲁⲅⲏⲟⲥⲧυⲣⲟⲃⲁⲗ ⲩ ⲧⲉⳝя ⲣⲁⲕ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲩⲥⲉⲗⲁⲥь ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲥⲗⲟⲃⲏⲟ ⲏⲁ ⲧⲣⲟⲏ υ ⲃⲟⲟⳝⲣⲁⳅυⲗⲁ ⲥⲉⳝя цⲁⲣⲉⲃⲏⲟύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁ ⲭⲩύ ⲥⲁⳝⲗⲉⳅⲩⳝыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲩⲕⲃⲉⲏⲏⲟ ⲥⲟⲥυ ⳡⲧⲟⲗⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩⲙⲥⲧⲃⲉⲏⲏⲟ ⲉⳝⲁⲗ ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ ⲡⲣяⳡⲉⲱьⲥя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲟⲕⲟⲡⲉ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲡⲁцⲁⲏⳡυⲕⲁⲙυ ⲉⳝⲁⲗυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟю ⳝⲁⳝⲕⲩ ⲥⲟⲃⲕⲟⲃⲩю ⳝⲗяⲇь ⲉⳝⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲣⲁⲗⲗяⲕⲩ ⲣⲩⲏⲉⲧⲟⲃⲥⲕⲩю ⲭⲩⲉⲙ ⲡⲏⲩⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⲇ ⳝⲉⳅⲇыⲭⲁⲏⲏыⲙ ⲧⲣⲩⲡⲟⲙ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲏⲁⲇⲣⲩⲅⲁⲗⲥя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲁⲏэⲡυⲇⲉⲙⲥⲧⲁⲏцυю ⲡⲟⲥⲧⲣⲟυⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь υⳅ ⲥⲧⲗьⲏⲟύ ⲗюⳝⲃυ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲃыⲥⲧⲣⲟυⲗⲁ ⲇⲗя ⲏⲉⲅⲟ ⲡⲁⲙяⲧⲏυⲕ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩ цⲉⲕⲃυ υⳅ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳡⲉⲣⲧⲉύ υⳅⲅⲟⲏяⲗ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ цⲉⲗⲉⳝⲏыⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲉⲏυⲥⲟⲡⲟⲇⲟⳝⲏыύ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃыⳝьⲉⲙ ⲧⲉⳝя υⳅ ⲕⲟⲗυυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲃⲁⲏⲱⲟⲧⲏⲩⲗ ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲉⲏυⲥⲟⲙ ⲯⲃⲁⲗы ⲧⲉ ⲧⲃⲟυ ⲟⲧⲟⳝью<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲟⲧⲇⲁύ ⲇⲟⲗⲯⲏⲟⲉ ⲙⲏⲉ,я ⲥⲩⲙⲉⲗ ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲡⲣυ эⲧⲟⲙ ⲟⲥⲧⲁⲧьⲥя ⲥ ⳡⲗⲉⲏⲟⲙ, ⲁ ⲩ ⲏⲉё ⲧⲁⲙ ⳝⲗя ⲭυⲗυцⲉⲣы ⲃⲥяⲕυⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲗⲉⲏⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲙⲟⳃью ⲩⲡⲣяⲙыⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲥυⲗы ⳡⲧⲟ ⲉⲥⲧь ⲇⲗя ⲧⲉⳝя ⲥⲙⲉⲣⲧⲉⲗьⲏⲟύ υⳅьⲉⳝⲁⲱυⲣⲩⲉⲙ ⲧя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲟⳅⲉ ⲯⲩⲣⲁⲃⲗя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲯⲉⲣⲧⲃⲁ ⲙⲟⲉύ ⲕⲉⲫυⲣⲏⲟύ ⲥⲡⲉⲣⲙы <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲫυⲗυⲥ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ υⲥцⲉⲗυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲕⲣⲟⲧⲟⲥⳝⲟⲣⲏυⲕ υⲗυ ⲧⲁⲕ ⲏⲁⳅыⲉⲙⲁя ⲣⲟⲧⲟⲃⲟя ⲡⲟⲗⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲉⲣⲡⲉⲗⲁ ⲕⲣⲩⲱⲉⲏυⲉ ⲟⳝ ⲙⲟύ ⲭⲩύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲁⲥⲧь ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲙⲁⲧⲉⲣυ ⲧⲉⲣⲡυⲧь ⲡⲟⲣⲁⲯⲁⲏυⲉ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲃⲥⲉⲙⲟⲅⲩⳃⲉⲅⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲏⲉ ⲡⲟⳅⲩⳝⲁⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲇыⲣⲩ ⲃ ⲗⲟⳝⲉⲱⲏυⲕⲉ ⲧⲃⲟёⲙ ⲃыⲥⲃⲉⲣυⲗ υ яύцⲁⲙυ ⲅⲗⲁⳅⲏυцы ⲟⲧⳝυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲥⲟⳡⲉⲗьⲏυⲕ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲧёⲗⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲣⲉⲱυⲗⲁ ⲙⲏⲉ ⳅⲇⲉⲥь ⳡⲗⲉⲏ ⲙⲟύ ⳝⲟⲅⲟцⲁⲣⲥⲕυύ ⳅⲁⲧⲉⲣⲡⲉⲧь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲡⲉⲣⲙⲟⲧⲟⳅⲟυⲇы ⲏⲁ ⲗⲟⳝⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲏяⲗυ ⲫⲗⲁⲅ ⲥ ⲙⲟυⲙ ⲏⲉύⲙⲟⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩ ⲧя ⲡⲟ ⲃⲥⲉⲙ ⲡⲟⲏяⲧυяⲙ ⲙⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲕⲣⲟⲙⲉ ⲃⲉⲣⲏⲟⲥⲧυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲧⲣⲉⲡⲁⲗⲁ ⲡⲟⲇⲣⲩⲇⲁⲏяⲙ ⲥⲃⲟυⲙ ⲕⲁⲕ я ⲉё ⲏⲁ ⳡⲗⲉⲏⲉ ⲥⲃⲟёⲙ ⲕⲁⲧⲁⲗ,ⲟⲏυ ⳝыⲗυ ⲃⲟⲥⲧⲟⲣⲅⲉ υ ⲡыⲧⲁⲗυⲥь ⲃⲥяⳡⲉⲥⲕυ ⲃⲥⲧⲣⲉⲧυⲧьⲥя ⲥⲟ ⲙⲏⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⳅⲁ ⲇⲃⲟυⲭ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲥⲡⲉⲣⲙⲟⲧⲟύ ⲙⲟⲉύ ⲃⲕυⲇыⲃⲁⲉⲱьⲥя υ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ ⲟⲧⲭⲟⲇⲏяⲕ ⲟⲥⲧⲁⲃⲗяⲉⲱь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁⲕⲟⲥⲧыⲗяⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲥⲇⲉⲗⲁⲗ ⲙⲏⲉ ⲡⲗⲟⲭⲟύ ⲙυⲏⲉⲧ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲙⲟυⲙ ⲙⲟⲅυⲗⲩ ⲥⲉⳝⲉ ⲣⲟύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⳅⲏⲁю ⳡⲧⲟ ⲧы ⲩⳝυⲃⲁⲉⲱьⲥя ⲡⲟ ⲏⲁⲱυⲙ ⲧⲉⲅⲁⲙ ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲟⳝ ⲙⲟύ ⲡⲟⲗⲟⲃⲟύ ⲁⲅⲣⲉⲅⲁⲧ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲃыⲥⲉⲕⲩ ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲗⲁⲧⲉⲏⲧⲁ ⲟⲧцⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲟⲥⲧⲁⲃⲗяю <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟ ⳡⲉⲣⲉⲡⲩⲱⲕⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲧⲩⲕⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲟⲇυⳡⲁⲃⲱυύ ⳝⲗяⲇⲟⲫⲣυⲕⲟⲃыύ ⲥыⲏяⲣⲁ ⲃⲟⳅⲟⲙⲏυⲗ ⲥⲉⳝя ⲇⲟⲭⲩя ⲃⲁⲯⲏыⲙ υ ⲡⲟⲗⲩⳡυⲗ υⳅьёⳝ ⲧⲣⲉⲧьⲉύ ⲥⲧⲉⲡⲉⲏυ ⲃⲏⲉⲟⳡⲉⲣёⲇⲏⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⳝⲉⲅυ ⲏⲁ ⲕⲩⲣⲅⲁⲏ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲣⲩⲡⲡⲁⲙυ ⲇⲉⲗⲁⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲟⲗⲥⲧⲟⲙяⲧⲏыύ ⲃⲁⲫⲗⲟⲯⲟⲣ ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲥⲟ ⲣⲧⲁ ⲏⲉ ⲇⲟⲥⲧⲁⲗ)<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⳝⲗⲁⲅⲟⲥⲗⲟⲃⲉⲏⲏыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲥⲉⲧⲣυⲏⲟⲃыύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь υⲙⲡⲉⲣⲁⲗυⲥⲧυⳡⲉⲥⲕυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲕⲩⲇⲟⲩⲙⲏыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲡⲟⲗⲟⲩⲙⲉⲃⲱυύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲧёⲗⲕⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲣυⲏⲩⲯⲇёⲏⲏыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲗⲁⳝⲁⲕ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲟⳝыⲕⲏⲟⲃⲉⲏⲏⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⳝⲉⳅⲩⲙⲃⲱυύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲉⲧⲉⲣⲡⲉⲗυⲃⲁ ⳝⲁⲗⲇⲩ ⲙⲟю юⲗⲟⳅυⲱь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲡⲣυⲏяⲗⲥя ⲥⲟⲥⲁⲧь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃⲩⲗьⲅⲁⲣⲏⲟ ⲉⳝⲁⲗ ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲱⲕⲩ ⲧⲃⲟю ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲉⳝⲁⲗυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲗⲉⲉⲉ ⲭⲩⲉⲙ ⲩⲙⲁⲗυⳃⲁю ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲡⲣυⲡⲁⲇⲕⲉ ⳡⲗⲉⲏ ⲥⲟⲥёⲱь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲟύ ⲭⲩύ ⳝⲟⲣⲟⳅⲇυⲗ ⲡⲣⲟⲥⲧⲟⲣыύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲩⲯⲉ ⲃⲥⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υⲏⲧυⲙⲏыⲉ ⳅⲟⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲟⳝⲗⲁⳅυⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⳡⲉⲱυⲣⲥⲕυύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲩⲱυ ⲧⲃⲟυ ⲟⲧⲧяⲏⲉⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲙⲅⲏⲟⲃⲉⲏьⲉ ⳅⲁⲙⲩⲧυ ⲥⲃⲟύ ⲟⲧⲥⲟⲥ ⲫυⲣⲙⲉⲏⲏыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲗⲟⲣⲁⳅⲩⲙⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲁⲗё ⲏⲁⲭⲩύ ⲏⲉ ⲥⲗыⲱⲩ ⲡυⲥⲕυ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲟⲣⲩ ⲧⲃⲟю ⲣⲁⳝⲥⲕⲟⲡυⲇⲟⲣⲥⲕⲩю ⲟⳝⲏⲉⲥёⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲉⲏυⲥⲟⲙ ⲥⲃⲟυⲙ ⲡⲣυⲙⲯⲁю ⲡⲩⲗьⲥⲁⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗυⲯⲉ ⲕ ⳅⲟⲏⲉ ⲥⲟⲡⲣυⲕⲟⲥⲏⲟⲃⲉⲏυя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁυⳡⲉύⲣⲏⲉⲱυύ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲧы ⲧⲟⲗьⲕⲟ ⲕⲟⲥⲧυ ⲥⲃⲟυⲙ ⲏⲉ ⲧⲉⲣяύ ⲡⲟ ⲡⲩⲧυ ⲕ ⲟⲧⲥⲧⲩⲡⲗⲉⲏυю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲃⲉⲣⲱυⲙ ⲡⲣⲁⲃⲟⲥⲩⲇυⲉ ⲏⲁ ⲉⳝⲁⲗⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟύ ⲟⲧⲉц ⲡⲟⲅⲟⲗⲟⲃⲏыύ ⲃⲁⲫⲗυⲧⲉⲗь ⲙⲟⲉύ ⳅⲁⲗⲩⲡы<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲏⲉ ⲥⲟⲙⲕⲏⲩⲗⲥя ⲃ ⲕⲟⲗⲗⲉⲏⲟⲗⲉⲕⲧⲉⲃⲟⲙ υ ⲏⲉ ⲏⲁⳡⲁⲗⲁ ⲙⲟⲗυⲧь ⲙⲉⲏя ⲟ ⲡⲟⳃⲁⲇⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥ ⲏⲉⲧⲉⲣⲡⲉⲏυⲉⲙ ⲭⲩⲉⲙ ⲧя υⳅⳝυⲃⲁю <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧя ⳝⲩⲇⲁⲣⲁⲯⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⳑⳑⲁⲏ ⲁⲕⲃⲁʀ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣⲟⲯёⲅ ⲧⲉⳝⲉ ⲅⲗⲟⲧⲕⲩ ⲥⲃⲟυⲙ υⲏⲫⲉⲣⲏⲁⲗьⲏыⲙ ⳡⲗⲉⲏⲟⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲥⲉⲕⲩ ⲧⲉⳝя ⲏⲁⲇⲃⲟⲉ ⲥⲃⲟυⲙ ⲁⲫⲣⲟⳡⲗⲉⲏⲟⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲧυⲡⲁ ⲕⲁⲕ ⲡⲉⲱⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲥⲟⲥёⲱь ⲙⲏⲉ ⲧⲩⲧ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙы ⳃⲁⲥ ⲥ ⳡⲉⳡⲉⲏцⲁⲙυ ⲡⲟⲇьⲉⲇⲉⲙ ⲧⲉⳝⲉ ⲱⲩⲫⲗяⲇⲕⲩ ⲣⲟⲃⲏяⲧь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲏυⲁⲕⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲟⲃⲁⲗ ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣυⲯⲙυⲥь ⲩⲯⲉ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲥⲇⲉⲗⲁύ ⲏⲁⲙ ⲟⳝⲟυⲙ ⲡⲣυяⲧⲏⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲕⲁⲕ ⲧы ⲙⲟⲯⲉⲱь ⲃⲗⲁⲥⲧⲃⲟⲃⲁⲧь ⲥⲃⲟⲉύ ⲥⲩⲇьⳝⲟύ ⲉⲥⲗυ ⲏⲁⲇ ⲧⲟⳝⲟύ ⲥⲧⲟυⲧ ⲙⲟύ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏыύ ⲡⲉⲏυⲥ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲟ ⲧы ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⲕ ⲱⲉⲣυⲏⲕⲉ ⲧⲟ ⲙⲟⲉύ ⲡⲣυⲡⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲉⳝⲉ ⲃυⲥⲗⲟⲩⲭⲟⲙⲩ ⲥыⲏⲕⲩ ⳝыⲥⲧⲣⲟ ⲧⲩⲧ ⲡⲁⲕⲗυ ⲃыⲣⲃⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⳃⲁⲥ ⲡⲟⲇⲕυⲏⲩ ⲙⲟⲏⲉⲧⲕⲩ ⲃⲃⲉⲣⲭ υ ⳅⲁ ⲃⲣⲉⲙя ⲉё ⲡⲟⲗёⲧⲁ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲯⲏⲁ ⳝⲩⲇⲉⲧ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⳡⲗⲉⲏ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲃⲥⲉ ⲉⳃё ⲭⲩύ ⲙⲟύ ⲃⲧⲉⲣⲡⲗυⲃⲁⲉⲱь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲟ ⲧы ⲧⲁⲕ ⲧⲩⲅⲟ ⲏⲁ ⲉⳝⲁⲗυⳃⲉ ⲥⲃⲟё ⲅυⳝⲣυⲇⲏⲟⲉ ⲡⲉⲏυⲥ ⲙⲟύ ⲡⲣυⲏυⲙⲁⲉⲱь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲥⲧⲟⲗьⲕⲟ ⳝыⲥⲧⲣⲟ ⲉⳝⲁⲱυⲣⲟⲃⲁⲗ ⲃⲁⲅυⲅυⲗьⲏⲟⲉ ⲡⲣⲟⲥⲧⲣⲁⲏⲥⲧⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲩⲥⲡⲉⲗ ⲣⲁⲥⲥⲉⳡь ⲃⲣⲉⲙⲉⲏⲏⲩю ⲗυⲏυю υ ⲩⲃυⲇⲉⲧь ⲥⲃⲟυⲙυ ⲅⲗⲁⳅⲁⲙυ ⲕⲁⲕ ⲅⲏⲟⳝяⲧ ⲧⲃⲟю ⲥⲟⲃⲕⲟⲃⲩю ⲡⲣⲟⳝⲗяⲧь ⳝⲁⳝⲕⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲃ 18 ⲃⲉⲕⲉ ⲗⲟⳝⲟⲧⲟⲙυю ⲡⲣⲟⲃⲟⲇυⲗυ,ⲏⲟ ⲃⲥⲉ ⲡⲟⲡыⲧⲕυ ⲥⲇⲉⲗⲁⲧь ⲥ ⲟⳝⲉⳅьяⲏы ⳡⲉⲗⲟⲃⲉⲕⲁ ⲡⲣⲟⲃⲁⲗυⲗυⲥь ⲃⲉⲇь ⲙⲟύ ⲗⳡⲏⲉ ⲏⲥⲧⲟⲗьⲕⲟ ⲟⲅⲣⲟⲙⲉⲏ ⳝыⲗ ⳡⲧⲟ ⲏⲉ ⲡⲟⲙⲉⳃⲁⲗⲥя ⲃ ⳡⲉⲣⲉⲡⲏⲟύ ⲟⲧⲥⲉⲕ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲟⳝ ⲩⲣⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲡⲟⲧⲩⲱυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲩ ⲩ ⲧя ⲙⲁⲧь ⲱⲗюⲭⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲧⲟ ⲏⲁ ⲗⳝⲩ ⲕⲣⲟⲙⲉ ⲥыⲏ ⲟⲏυⳃⲁⲗⲟύ ⳝⲗяⲇⲟⲇυⲕⲁⲣⲕυ ⲏⲁⲡυⲥⲁⲏⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲕⲁⲕ ⳃυⲧⲟⲙ ⲡⲣυⲕⲣыⲃⲁⲗⲁⲥь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲡⲩⲗυ ⲟⲧⳝυⲃⲁⲗⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲉⳝⲉ ⲣⲉⲕⲥⲩ ⳡⲉⲣⲏⲟⲩⲥⲟⲙⲩ ⲃⲙυⲅ ⲃⲥⲉ ⲧⲃⲟυ ⲙыⲥⲗυ ⲃыⳝью ⳡⲗⲉⲏⲟⲙ ⲥⲃⲟυⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣⲟⲃёⲗ ⲧⲣⲉⲡⲁⲏⲁцυю ⳡⲉⲣⲉⲡⲁ ⲏⲁⲇ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲏⲉ ⳅⲁⲇⲉύⲥⲧⲃⲟⲃⲁⲃ ⲡⲣυ эⲧⲟⲙ ⲏυⲕⲁⲕυⲭ ⲩⲥυⲗυύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲣⲉⳅьⳝⲩ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲗⲟⲙⲁⲉⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡⲟ ⲫⲉⲏⲉ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲕυⲇыⲃⲁⲉⲧⲥя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅⲡⲣυⲏцυⲡⲏⲟ ⲉⳝⲁⲃю ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲁⲕ ⲏⲉⲟⲥⲧⲟⲣⲟⲯⲏⲟύ ⲭⲩⲉⲙ ⲙⲟυⲙ ⲇⲁⲃυⲱьⲥя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲩ ⲡⲟⲅⲟⲏяⲗⲟ ⲧⲃⲟⲉⲅⲟ яⳅыⲕⲁ ⲭⲩύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲫⲁⲗⲁⲏⲅυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲣⲃⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲭⲩⲉⲥⲟⲥ ⲥⲗⲁⳝыύ ⲃ ⲥⲃⲟυⲙ ⲙⲁⲏяⲙυⲣⲟⳡⲏыⲉ ⲥυⲗы ⲣⲉⲱυⲗ ⲩⲃⲉⲣⲟⲃⲁⲧь я ⲯⲉ ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲧⲁⲕυⲉ ⲙыⲥⲗυ ⲡⲉⲏυⲥⲟⲙ ⲃыⳝью<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲅⲩⳝⲁⲱⲗⲉⲡ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲥⲁⲗⲟ ⲧⲃⲟё ⲉⳝⲁⲏⲏⲟⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲥⲟⲧⲣяⲥⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲇⲣⲁⳝⲁⲧыⲃⲁⲉⲧ ⲟⳝⲟⲇⲕⲟⲙ ⲇⲗя ⲩⲏυⲧⲁⳅⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡыⲧⲁⲗⲁⲥь ⲙⲉⲏя ⲟⲧⲧяⲏⲩⲧь ⳅⲁ яύцⲁ ⲙⲟυ ⲟⲧ ⲧⲃⲟⲉⲅⲟ ⳝⲉⳅⲇыⲭⲁⲏⲏⲟⲅⲟ ⲧⲉⲗⲟ ⲏⲁ ⲡⲟⲥⲕⲟⲗьⲕⲩ ⲟⲏυ ⲥⲇⲉⲗⲁⲏы υⳅ ⲙⲉⲧⲁⲗⲗⲟⲕⲉⲣⲁⲙυⲕυ я ⲉύ ⲡⲣⲟⲥⲧⲟ ⲏⲁ ⲡⲣⲟⲥⲧⲟ ⲭⲩⲉⲙ ⲣⲩⲕυ ⲟⲧⲣⲉⳅⲁⲗ υ ⳅⲁⲥⲩⲏⲩⲗ ⲉύ ⲃ ⲣⲟⲧ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲥⲃⲟⲉύ ⲅⲁⲗⲟⲡⲉⲣⲉⲇⲟⲗⲟⲃύ ⲅⲩⳃⲉύ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲕⲟⲣⲙυⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲥⲟцυⲁⲗьⲏⲟύ яⲙы ⲡⲟⲥⲙⲉⲗ ⲃⳅьⲉⳝⲁⲧь ⲏⲁ ⲙⲟύ ⲡьⲉⲇⲉⲥⲧⲁⲗ ⲙⲁⲣⲅυⲏⲁⲗьⲏⲟⲉ ⲟⲧⲣⲉⳝьⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲗⲉⲏ ⲙⲟύ яⲃⲟяⲉⲧьⲥя ⲃⲉⲣⲱυⲧⲉⲗⲉⲙ ⲥⲩⲇⲉⳝ ⲇⲗя ⲏⲉⲩⲃⲉⲣⲟⲃⲁⲃⲱυⲭ ⲃ ⲙⲟυ яύцⲁ ⳝⲗяⲇⲟⲩⲧⲃⲁⲣⲉύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅⲕⲟⲣыⲥⲧⲏⲟ ⲥⲟⲥυⲣⲩⲉⲱь ⲙⲏⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩя ⲙⲟⲉⲅⲟ ⲃⲥⲟⲥυ ⳝⲗяⲇυⲏⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲉⳝⲉ ⳡⲉⲣⲉⲡ ⳝⲩⲧыⲗⲕⲟύ υⳅ ⲡⲟⲇ ⲡυⲃⲁ ⲣⲁⳅⲇⲣⲟⳝυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲉⲇⲁⲉⲱь ⲕⲁⲗⲗ ⲙⲟύ ⲡⲣⲉⲏⲉⳝⲣⲉⲯυⲙⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲉ ⲧⲉⲣяύⲥя ⲃ ⲡⲟⲧⲟⲕⲉ ⲙⲟⳡυ ⲙⲟⲉύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩ ⲃⲟⲇⲟⲡⲁⲇⲁ ⲥⲟⲥⲁⲗ ⲙⲏⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲭⲩⲉⲙ ⲙⲟυⲙ ⳅⲁⲕⲟⲇυⲣⲟⲃⲁⲗⲥя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⳡⲟ ⲱⲁⲡⲁⲕⲗяⲕ ⲃыⲉⳝⲁⲏⲏыύ я ⲧⲉ ⲧⲩⲧⲁ ⲙⲁⲧь ⲉⳝⲁⲱυⲣⲩю ⲇⲟ ⲡⲣⲉⲇⲥⲙⲉⲣⲧⲏⲟⲅⲟ ⲥⲟⲥⲧⲟяⲏυя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧя ⲥⲟⲧⲣяⲥⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⲅⲗⲁⳅⲏυцы ⲧⲉⳝⲉ ⲃыⲯⲅⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲡⲣυⲱёⲗ ⲥюⲇⲁ υⲥⲕⲗⳝⳡυⲧⲉⲗьⲏⲟ ⲥⲟ ⲥⲃⲟυⲙ ⳝⲟⲅⲟⲩⲅⲟⲇⲏыⲙ ⲥⲃⲉⲣⲭⲙⲁⲥⲥυⲃⲏыⲙ ⲡⲉⲏυⲥⲟⲙ ⳡⲧⲟⳝы ⲃⳅьⲉⳝⲁⲧь ⲧⲉⳝя ⲕⲁⲕ ⲡⲧⲁⲭⲩ ⲡⲟⲥⲗⲉⲇⲏюю <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⲡⲟⲗⲏяⲗ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲡⲉⲣⲉⲥⲁⲇⲕⲁⲭ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲕⲩⲣяⲧⲏю ⲧⲃⲟю ⲣⲁⳅⲏⲉⲥёⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲥⲁⲇⲩ ⲩⲥⲧⲣⲟυⲗ ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲩⲇⲟⳝⲣⲉⲏυя ⲡⲟⲇⲟⲱёⲗ ⲧⲃⲟύ ⲟⲧⲉц ⲫⲣυⲕ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]υⲙⲡⲟⳅⲁⲏⲧⲏⲟ ⲡыⲧⲁⲉⲱьⲥя ⲏⲉⳅⲁⲙⲉⲧυⲧь ⲙⲟύ ⲡⲉⲏυⲥ ⲏⲟ ⲃⲥёⲣⲁⲃⲏⲟ ⲡⲟⳡⲉⲙⲩ ⲥⲙⲟⲧⲣυⲱь ⲏⲁ ⲏⲉⲅⲟ ⲕⲁⲕ ⲣⲉⳝёⲏⲟⲕ ⲏⲁ ⲥⲗⲁⲇⲟⲥⲧь ⲁⲣⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲧⲁ ⲃⲏⲁⲧⲩⲣⲉ ⲏⲉ ⲩⲙⲣυ ⲧⲟⲕⲁ ⲡⲣυⲙυⲧυⲃⲏⲟύ ⲥⲟⲥⲁⲧⲉⲗь ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲉⳝⲁⲏⲩⲧыύ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲥⲕⲟⲣⲟⲥⲧь ⲩⲇⲁⲣυⲗⲁ ⲃ ⲅⲟⲗⲟⲃⲩ ⲉⲃⲁⲱⲓⲙ ⲡⲟⲇⳃёⳡυⲏ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲕⲉⲣⲁⲙυⳡⲉⲥⲕυⲙυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧью ⲥⲃⲉⲧⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⳝыⲥⲧⲣⲉⲉ ⲥⲕⲟⲣⲟⲥⲧυ ⳅⲃⲩⲕⲁ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲙⲏⲉ ⳝⲉⳅⳅⲃⲩⳡⲏⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲕⲟⲅⲇⲁ ⲭⲩύ ⲥⲟⲥⲁⲗ ⳅⲁⳡⲉⲙ ⲡⲣυⳡⲙⲟⲕυⲃⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⲗё я ⲧⲉ ⲧⲃⲟύ ⲡⲟⲥёⲗⲟⲕ ⲏⲁⲭⲩύ ⲥⲟⲯⲅⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲥыⲏⲟⲕ ⲟⲡⲗⲉⳝⲉⲉⲏⲟύ ⲗяⲣⲃⲟⳝⲗяⲇⲏⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲟⲥⲧⲟⲏⲟⲃⲕⲉ ⲡυⳅⲇⲟύ ⲥⲃⲟⲉύ ⳝⲁⲏⳡυⲗⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲕⲟⲙⲡⲟⳅυⲧⲟⲣⲏⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲧⲁⲕⲧ ⲥ ⲉⳝⲗⲉύ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲟύ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲡⲟⲗⲟⲥⲧь ⳝⲉⳅ ⲡⲉⲏьⲕⲟⲃ ⲟⲥⲧⲁⲃυⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲡⲣⲟⲯёⲅ ⲥⲧⲉⲏⲕυ ⲃⲗⲁⲅⲁⲗυⳃⲁ ⲧⲃⲟⲉ ⲙⲁⲧⲉⲣυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁ ⲗⲟⲭ ⲗⲟⲃυ ⲕⲗⲉύⲙⲟ ⲥыⲏⲕⲁ ⲱⲗюⲭυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲟⳝ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲧⲩⲱⲩ ⲏⲁ ⲗⲉⲧⲩ ⲕ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲉ ⲱⲁⲗⲁⲃⲉ ⲁⲣⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧя ⲩⲧⲉⲱⲁю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲃ ⲥⲕⲟⲣⲟⲡⲟⲥⲧυⲯⲏⲟⲙ ⲡⲟⲣяⲇⲕⲉ ⲡⲟⲧⲉⲣⲡυⲧь ⲏⲉⲩⲇⲁⳡⲩ ⲡⲣⲟⲧυⲃ ⲏⲉⲣⲁⲃⲏⲟύ ⲥⲃⲭⲁⲧⲕυ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲁⲣⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⲏⳅⲟⲕⲟⲗⲟⲏⲕⲩ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲡⲟⲇⲟⲯⲅⲩ ⲭⲇ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲯⲟⲡⲩ ⲇⲁⲱь υⲗυ ⲭⲩⲉⲙ ⲃ ⲅⲗⲁⳅ?<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲣⲁⲥⲥⲭⲩⲉⲣⲉⳅυⲙ ⲧⲃⲟё ⲙⲏυⲙⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲭⲩяⲙυ ⲥⲃⲟυⲙ ⲧⲟⲣⲯⲉⲥⲧⲃⲉⲏⲏыⲙυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⲗё ⲧёⲗⲕⲁ я ⲧⲃⲟύ υⲙⲡⲉⲣⲁⲧⲟⲣ ⲃыⲡυⲱυ ⲙⲁⲧⲉⲣυ ⳡёⲣⲏⲟύ ⲱⲗюⲭⲉ ⳡⲗⲉⲏ ⲙⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⳝⲁⲏⲕⲁύ ⲧⲃⲟя ⲟⲏυⳃⲁⲗⲁя ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲁ ⲃⲡⲣυⲏцυⲡ ⲏⲉ ⲃыⲥⲧⲟυⲧ ⲡⲣⲟⲧυⲃ ⲏⲉⲅⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲏяⲥⲣⲟⲗьⲏыύ ⲥыⲏⲟⲕ ⲡⲁⲥⲕⲩⲇυⲏцы я ⲯⲉ ⲧⲉ ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲟ ⲃⲥⲉⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉⲃⲟⳅⲙⲟⲯⲏыⲉ ⲇыⲣⲕυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣⲟⲡⲁⳃυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲧⲟⲗьⲕⲟ ⲡⲟⲙⲉⲣⲁⲧь ⳅⲇⲉⲥь ⲏⲉ ⲃⳅⲇⲩⲙⲁύ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲕⲁⲏⲁⲃⲏⲟⲉ ⲡⲟⲥⲧⲟⲧⲣⲟⲇьⲉ ⲥⲗыⲱυⲱь я ⲧⲉⳝⲉ ⲙⲁⲧь ⲭⲩⲉⲙ ⲇⲁⲣⲁ ⲣⲉⳡυ ⲣⲉⲱυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲧⲁⲙ ⲙⲁⲧь ⲥⲃⲟю ⲩⲯⲉ ⲟⲧⲅⲟⲏяύ ⲟⲧ ⲥⲡⲉⲣⲙⲟⲧы ⲙⲟⲉύ ⲁ ⲧⲟ ⲇⲩⲣⲁ ⲃⲕⲣⲁύ ⲟⲡⲟⲗⲟⲩⲙⲉⲗⲁ ⲟⳝⲟⲯⲣⲁⲃⲱυⲥь ⲉё<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲧⲉⲗⲉⲃυⳅⲟⲣ ⲡⲟⲕⲁ ⲏⲁ ⲃьⲉⳝёⲱь ⲣⲁⳝⲟⲧⲁⲧь ⲏⲉ ⲥⲧⲁⲏⲉⲧ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲃ ⲡⲟⲗⲏыύ ⲣⲟⲥⲧ ⲏⲁⳝυⲗ ⲙⲟύ ⲭⲩύ ⲁⲣⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲕⲁⲗⲗⲟⲃⲡⲁⲗⲩю ⲧⲣⲉⳃυⲏⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲙⲉⲥⲧⲟ υⲏⲥⲩⲗυⲏⲁ ⲕⲁⲡⲁⲗⲁ ⲡⲟ 5 ⲙⲅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲥⲉⲥⲧⲣⲩ ⲧⲃⲟю ⲗⲁⲡⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥыⲏ ⲙⲩⲥⲟⲣⲟⲡⲣⲟⲃⲟⲇⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲇⲟ ⳝⲗⲉⲥⲕⲁ ⲟⳡⲉⲗⲟ ⲙⲟё ⲃыⲧⲉⲣ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲙⲩⲗⲉ ⲉⳝⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲗⲉⲱυⲃыύ ⲥыⲏ ⳡⲉⲣⲏюⳃⲉύ ⲱⲗюⲭυ я ⲧⲃⲟю ⲯυⲣⲏⲟⲙⲁⲥⲧⲏⲩю ⲗⲁⲭⲩⲱⲕⲩ ⲙⲁⲧь υⳅьⲉⳝⲁⲱυⲣⲟⲃⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲗⲟⲭ ⲭⲩύ ⲏⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲟύ ⲭⲩύ эⲧⲟ цⲉⲣⲕⲟⲃь ⲁ яύцⲁ ⲕⲟⲗⲟⲕⲟⲗы ⲡⲟ ⳅⲃⲩⲕⲩ ⲕⲟⲧⲟⲣыⲭ ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲏυⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲏⲁⲥⲧⲩⲡυⲗ ⲧⲃⲟύ ⳡⲉⲣёⲗ ⲥⲟⲥⲁⲧь ⲭⲩύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲏⲟⲅⲟⲡⲟⲧⲟⳡⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲥⲗⲟⲃⲏⲟ υⲙⲡⲉⲣⲁⲧⲟⲣ ⳅⲁⲥⲧⲁⲃⲗю ⲧⲃⲟю ⲙⲁⲧь ⳝыⲧь ⲟⳝⲅⲗⲁⲇⲁⲏⲏⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲗⲟⲅⲟⲃⲟⲏυя υⲥⲭⲟⲇяⳃυⲉ υⳅ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⳅⲁⲧⲙυⲗυ ⲧⲃⲟύ ⲣⲁⳅⲩⲙ υ ⲟⲧⲏыⲏⲉ ⲧы ⲡⲣⲉⲇⲏⲁⲇⲗⲉⲯυⲱь ⲙⲟⲉⲙⲩ ⲡⲉⲏυⲥⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧя ⲙⲉⲯ ⲣёⳝⲉⲣ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲉⳝⲁⲗ ⲧя ⳅⲁⲅⲟⲣⲟⲇⲟⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧя ⲃыⲕⲩⲣυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁ ⲥⲟⲥⲏυ ⳝⲁⲗⲇы ⲙⲟⲉύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲗяⲇⲟⲉⳝ ⲙⲁⲏяⲙυⲣⲟⳡⲏыύ ⳡⲧⲟ ⲉⲥⲧь ⲥыⲏⲕⲟⲙ ⲱⲗюⲭυ ⲡⲟ ⲕⲣⲟⲃⲉ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲟύ ⲭⲩύ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ ⲁⲣⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲣⲉⲥⲏⲩⲗ ⲧя ⲭⲩⲉⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃⲟⲗⲁⲉⲱь ⲕⲁⲕ ⳝⲉⲱⲉⲏⲏⲁя ⲕⲟⲅⲇⲁ ⲥⲟⲥёⲱь ⳝⲉⳅ ⲕⲟⲡыⲧ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⲏⲉⲥⲩ υⲏⲥⲉⲕⲧⲟⲫⲟⳝⲏⲟⲉ ⲙⲁⲥⲗⲟ ⲏⲁ ⲥⲃⲟύ ⳡⲗⲉⲏ υ ⲃⲟύⲇⲩ ⲃ ⲧⲃⲟю ⲏⲉⲧⲟⲡыⲣυⲭⲩ ⲙⲁⲧь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥыⲏⲟⲕ υ ⲣⲟⲇⲁ ⲱⲗюⲱьⲉⲅⲟ ⲧы ⳡⲧⲟ ⳅⲇⲉⲥь ⲡⲟⲙⲉⲣⲉⲧь ⲃⳅⲇⲩⲙⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]цⲉⲗⲕⲟⳝⲁⳡⲁⲣⲏыύ υⲏцⲉⲗ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲕⲣыⲗьяⲙυ ⲭⲩύ ⲟⲧⲟⲣⲃⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁ ⲥⲗⲁⲇⲕⲟⲉⲯⲕⲉ ⲧⲃⲟⲉⲙⲩ ⲡⲁⲭⲁⲏⲩ ⲡυⲇⲟⲣⲩ ⲙⲟⳡυ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲁ ⲟⲏ ⲥ ⲇⲟⲃⲟⲗьⲏыⲙ ⲉⳝⲁⲗⲟⲙ ⲡⲣυⲏяⲗⲥя ⲉё ⲡυⲧь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲗя ⳝⲩⲇⲩ ⲙⲁⲧь ⲧⲉ ⲏⲟⲅⲁⲙυ ⳅⲁⳝυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥ ⲧⲁⲕⲟύ ⲥυⲗⲟύ ⳡⲧⲟ υⳅ ⲡⲟⲇ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲏⲁⳡⲁⲗυ ⲃыⲥυⲕⲁⲧьⲥя υⲥⲕⲣы<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟя ⲱⲗюⲭⲟⲙⲁⲧⲉⲣь ⲥ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲥⲗⲟⲃⲏⲟ ⲥ ⲡⲟⲥⲟⲭⲁ ⲙⲁⲅυⳡⲉⲥⲕⲟⲅⲟ ⲏⲁⲡⲣⲁⲃυⲗⲁ ⲟⲅⲟⲏь ⲏⲁ ⲃⲁⲱ ⲡⲟⲥёⲗⲟⲕ ⲭⲇ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳅⲁⲥⲧⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲡυⲇⲟⲣⲁⲥⲏυцⲩ ⲃ ⲡⲣυⲡⲁⲇⲕⲁⲭ ⲡⲩⲭⲏⲩⲧь ⲡⲟⲉⲇⲁя ⲥⲡⲉⲣⲙⲩ ⲙⲟю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я υⳅⲅⲏⲁⲗ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲉⲙⲟⲏⲟⲃ ⲡⲩⲧёⲙ ⲃⲭⲟⲯⲇⲉⲏυя ⲥⲃⲟυⲙ ⲡⲟⲗⲟⲃыⲙ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃ ⲉё ⲃⲁⲅυⲗьⲏыύ ⲟⲧⲥⲉⲕ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕ ⲯⲉ ⲩⲥⲉⲣⲇⲏⲟ ⲕⲁⲕ ⲧы ⲥⲟⲥⲁⲗ ⲭⲩύ ⲙⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲫⲣυⲕⲟⲃⲁ ⲥⲁⲥёⲱь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲥⲁⲯⲩ ⲕⲁⲕ ⲏⲁ ⲕⲣⲉⲥⲗⲟ ⲕⲁⳡⲁⲗⲕⲩ ⲉⳝⲁⲏⲏⲟⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥⲁⲧь ⲭⲩύ ⳅⲁ ⲡⲣⲉⲇⲏⲁⳅⲏⲁⳡⲉⲏυⲉⲙ ⲥⲡⲁⲥⲉⲏυⲉ ⲧⲃⲟⲉύ ⲯυⲃⲟⲧⲏⲟⲡⲟⲇⲟⳝⲏⲟύ ⲥⲉⲙьυ ⲏυⳃⲩⲕⲟⲃ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲙⲉⲗⲟ ⲉⳝⲁⲗ ⲧя ⲡⲟⲇ ⲅⲣⲟⲭⲟⲧ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡυⲇⲟⲣⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲧⲁⲕυⲙ эⲏⲧⲩⳅυⲁⳅⲙⲟⲙ ⳡⲧⲟ ⲧⲃⲟύ ⲟⲧⲉц ⳝыⲗ ⲃыⲏⲩⲯⲇⲉⲏ ⲕⲁⲧⲁⲧьⲥя ⲧⲩⲇⲁ ⲥюⲇⲁ ⲏⲁ ⲙⲁⲣⲱⲣⲩⲧⲕⲉ ⲥⲃⲟⲉύ ⳡⲧⲟⳝы ⲏⲉ ⲃυⲇⲉⲧь эⲧⲟⲅⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩⲥⲟⲥυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃⲥⲟⲥⲉ ⲕⲁⲕ ⳅⲁⲇⲩⲙⳡυⲃыύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣυⲕⲩⲣυⲗ ⲥ ⲗⲁⲙⲡⲁⲇы ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲏⲉⲡⲟⲗⲟⲃⳅⲣⲉⲗⲩю ⲥⲉⲥⲧⲣёⲏⲕⲩ ⲱⲗюⲭⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥυⲗⲟύ ⲭⲩя ⲥⲃⲟⲉⲅⲟ ⳝⲉⳅ ⲱⲁⲏⲥⲃⲟ υⲥⲧⲣⲉⳝⲗяю ⳝⲗяⲇⲟⲇⲉⲧⲟⲕ ⲏⲉⲥⲡⲟⲥⲟⳝⲏыⲭ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲅⲟⲣⳝⲁⲧⲟⲥⲡυⲏⲏыύ ⲥыⲏⲟⲕ ⲁⲥⳝⲉⲥⲧⲟⲃⲟύ ⲡⲣⲟⲫⲩⲣⲥⲉⲧⲕυ ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲃыⲉⳝⲉⲙ ⲧя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩяⲙυ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲉⲙ ⲣⲉⲱⲉⲧⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲏυⲙⲟ ⲥⲟⲥёⲱь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲟⲧⲕυⲏⲩⲃⲱυ ⳡⲉⲗⲟⲃⲉⳡⲏⲟⲥⲧь ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲕⲁⲕ ⳡⲣⲉⳅⲃыⳡⲁύⲏⲟⲟⲡⲁⲥⲏыύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲭⲣⲁⲙⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]цⲉⲣⲕⲟⲃⲏⲟ ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲏⲁ ⳅⲁⲇⲏⲉⲙ ⲣяⲇⲩ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲅⲉⲣⲟυⲏⲟⲃⲟ ⳅⲁⲃυⲥυⲙ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]υⳅьёⳝυⲥⲧⲟ ⲥⲟⲥⲁⲗ ⲇⲟ ⲡⲟⲧⲉⲣυ ⲡⲩⲗьⲥⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲃ ⲣыцⲁⲣυ ⲟⲣⲇⲉⲏⲁ ⲡⲟⲥⲃяⲧυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]υⲥⲡⲟⲗьⳅⲩю ⲗυⲱь ⲥυⲗы ⲥⲃⲟυ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲃⲉⲣⳃⲁюⳃυⲉ ⲥⲩⲇьⳝы ⲏⲁ ⲥⲗⲁⳝыⲙυ ⲭⲩⲉⲥⲟⲥⲁⲙυ ⲧⲉⲗⲉⲥⲣⲁⲙⲙⲟⲃⲥⲕυⲙυ ⲣⲁⳅⲅⲉⲣⲙⲉⲧυⳅυⲣⲩю ⲡⲁⲥⲧь ⲧⲉⳝⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥυⲗⲟύ ⲙыⲥⲗυ ⲙⲁⲧь ⲧⲃⲟю ⲃыⲧⲣⲁⲭⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲫⲗⲟⲙⲁⲥⲧⲉⲣⲟυⲇⲏыύ ⲥыⲏⲟⲕ ⲱⲗюⲭⲟⲃυⲇⲏⲟύ ⳝⲟⲗьⲏⲟύ ⲗⲉύⲕⲉⲙυⲉύ ⲇⲁⲯⲉ ⲏⲉ ⲡыⲧⲁⲉⲧьⲥя ⳡⲧⲟ ⲧⲟ ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⳡⲗⲉⲏⲁⲙ ⲅⲟⲥⲡⲟⲇⲥⲕυⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲩⲥⲗⲩⲯⲗυⲃⲟ ⲥⲟⲥёⲱь ⲙⲏⲉ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅ ⲙыⲥⲗⲉύ ⲥⲟⲥёⲱь ⲙⲏⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲗⲟⲃⲏⲟ ⲥⲁⳝ-ⳅυⲣⲟ ⲡⲣυύⲇⲩ ⲕⲣⲩⲱυⲧь ⲧⲉⳝⲉ ⲉⳝⲁⲗυⳃⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲫⲁⲉⲣⳝⲟⲗⲟⲙ ⲩⳝυⲗ ⲧя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲁⲙⲟⲃⲕⲁⳡⲉⲏ ⲃⲉⲧⲭⲟⳅⲁⲃⲉⲧⲏыⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⲏⲧⲣⲟⲡⲟⲙⲟⲣⲫⲏⲟⲉ ⲡⲟⲇⲟⳝυⲉ ⲥⲃυⲏⲟⳡⲉⲗⲟⲃⲉⲕⲁ я ⲯⲉ ⲧⲃⲟю ⲥⲃυⲏⲟⲙⲁⲧь ⲏⲁ ⲥⲁⲗⲟ ⲡⲩⲥⲧυⲗ υ ⲟⳝⲉⲥⲡⲉⳡυⲗ ⲭⲟⲭⲗⲟⲃ ⲡⲟⲯυⳅⲏⲉⲏⲏыⲙ ⳅⲁⲡⲁⲥⲟⲙ ⲥⲁⲗⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⲇⲕⲁя ⲃыⳝⲗяⲇⲟⳡⲏⲁя ⲡⲣⲟⳝⲟυⲏⲁ ⲧы ⲕⲩⲇⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲩⲧⲁⲉⲱь ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲟⲧⲣⲕⲉ ⲏⲣⲁⲃⲁ ⲟⲧⲥⲟⲥⲉ ⲉⲅⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲉⳝⲉ ⲗⲩⲡⲟⲅⲗⲁⳅⲟⲙⲩ ⲥыⲏⲕⲩ ⲕⲣⲁⲥⲏⲟⲣыⲗⲟύ ⳝⲗяⲇⲉⲏцυυ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲃⲥⲉ ⲕⲟⲥⲧυ ⲃ ⲡыⲗяⲕⲩ ⲥⲟⲧⲣⲩ,ⲧы ⲏⲁ ⲕⲟⲅⲟ ⲡⲁⲥⲧь ⲟьⲕⲣыⲧь ⲣⲉⲱυⲗⲁ ⲩⲙⲁⲗυⲱёⲏⲏⲁя ⲏⲁⲥⲁⲇⲕⲁ ⲏⲁ ⲙⲟύ ⲡⲉⲏυⲥ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗⲟ ⲥⲃⲟё ⲥⲕⲣⲉⲡⲟⲥⲧⲏⲟⲉ ⲏⲉ ⲧⲉⲣяύ ⳅⲇⲉⲥя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⲡυⲱⲩ ⲅⲣⲩⲥⲧⲏⲩю υⲥⲧⲟⲣυю ⲡⲣⲟ ⲧёⲗⲕⲩ ⲕⲟⲧⲟⲣⲁя ⲧⲁⲕ υ ⲏⲉ ⲥⲙⲟⲅⲗⲁ ⲇⲟⲧυⳡь ⲥⲃⲟⲉύ цⲉⲗυ,ⲧⲟⳝυⲱь ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ,ⲅⲗⲁⲃⲏⲟύ ⲅⲉⲣⲟυⲏⲉύ ⳝⲩⲇⲉⲧ ⲕⲥⲧⲁⲧυ ⲧⲃⲟя ⲙⲁⲧь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲡⲣⲟⳅⲉ ⲟ ⲧⲉⳝⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲟⲥⲧⲁⲃⲗю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲗⲁⲃⲡⲩⲭ ⲁ ⲏⲩ ⲡⲣυⲏяⲗⲥя ⳡⲗⲉⲏ ⲙⲟύ ⲣⲁⲥⲥⲁⲥыⲃⲁⲧь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲏⲟⲅⲟⲥⲧⲣⲁⲇⲁⲗьⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲩⳝы ⲡⲟⲗⲟⲃыⲉ ⲡⲣⲟⲯⲅⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲉύⲙ ⲥⲃⲟύ ⲟⲥⲧⲁⲃⲗю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲉⳝя ⲥыⲏⲕⲁ ⲥⲗⲁⳝⲉύⲱⲉύ ⲱⲗюⲭυ ⲩⳝью ⲥⳡⲁ υ ⲟⳡυⲱⲩ ⲗⲟⲕⲁцυю ⲟⲧ ⲏⲉⲯⲉⲧυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲟύ ⲥⲧυⲗь ⲉⳝёⲧ ⲧⲃⲟю ⲙⲁⲧь ⲃⲟⲧ ⲧы υ ⲫⲁⲏⲁⲧⲉⲉⲱь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⳡⲗⲉⲏⲉ ⲧⲩⲭⲏⲉⲱь ⲧⲁⲕ ⳝыⲥⲧⲣⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]υⳅⲩⲃⲉⳡυⲙ ⲧⲉⳝя ⳡⲁⲥⲧыⲙυ ⲩⲇⲁⲣⲁⲙυ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲥⲟⲥⲁⲗьⲏυⲕⲩ ⲧⲃⲟⲉⲙⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲯⲉ ⲃ ⲥⲟюⳅⲉ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ υ яύцⲁⲙυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲥ ⲱⲗюⲭⲁⲙυ ⲏⲁ ⲡⲟⲇⲟⳝυⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ яⲕⲱⲁⲉⲱьⲥя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥυ ⲙⲟⲇⲩⲗьⲏⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥυ ⲃⲇⲩⲙⳡυⲃⲟ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲟⲥυ ⲕⲁⲕ ⲡⲣυⲏяⲧⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃⲕυⲇыⲃⲁⲉⲱьⲥя ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⳝы ⲥⲗⲟⲃυⲧь ⲡⲣυⲭⲟⲇ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲟ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲭⲩя ⲉⲱё ⲏυⳡⲉⲅⲟ ⲏⲉ ⲅⲟⲃⲟⲣυⲧ ⲟ ⲧⲟⲙ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲥⲇⲉⲗⲁⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲏю ⲧⲉ ⲧⲃⲟю ⲉⳝⲁⲗ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲣⲩⲭⲗяⲇь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲃⲧⲟⲣяύ ⲥ ⳡⲗⲉⲏⲁ ⲃⲥⲉ ⲥⲗⲟⲃⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲏυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲁ ⲟⲏⲁ ⲃⲉⲗⲁⲥь ⲕⲣⳡ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲥыⲏ яⳃⲉⲣυцы ⲕⲟⲧⲟⲣⲁя ⲥⲕυⲇыⲃⲁⲉⲧ ⲕⲟⲯⲩ ⲡⲣυ ⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲁⲏцⲩю ⲃⲁⲗьⲥ ⲃ ⲕυⲱⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲟⲥⲏⲟⲃⲁⲏυя ⲇⲗя ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉⲅⲟ ⲡⲩⲧυ ⳡⲧⲟⳝы ⲉύ ⳝыⲗⲟ ⲡⲣⲟⳃⲉ ⳅⲁⲅⲣⲩⲯⲁⲧь ⲃ ⲥⲉⳝя ⳡⲗⲉⲏⲃ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲃ ⲕⲟⲥⲙⲟⲥ ⲡⲩⲗьⲏⲩⲗ ⳡⲧⲟⳝы ⲟⲏⲁ ⲧⲁⲙ ⲣыⲅⲁⲗυⳃⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲙυⳡⲉⲥⲕⲩю ⲡыⲗь ⲥⲟⳝυⲣⲁⲗⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲡυⳅⲇⲁⳡυⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲣⲟⲅⲁⲧⲕⲩ ⲏⲁⲧяⲏⲩⲗυ ⲡⲩⲗьⲏⲩⲗ ⲉю ⲃ ⲥⲟⲥⲉⲇⲥⲕⲟⲉ ⲟⲕⲏⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲅⲩⳝⲕⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲉⲣⲡυⲱь ⲧⲩⲧⲁ ⳅⲏⲁⳡυⲧ ⳡⲗⲉⲏы ⲏⲁⲱυ ⳝⲟⲅⲁⲧыⲣⲥⲕυⲉ ⲏⲁⲇ ⲥⲟⳝⲟύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩяⲙ ⲧⲁ ⲁⲕⲩⲏⲩⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⳅⲁⲙⲉⲥⲧⲟ ⲱⲁⲙⲡⲁⲏⲥⲕⲟⲅⲟ ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲉ ⲙⲟⳡυ ⲥⲃⲟⲉύ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲗⲁⲭⲩⲏⲇⲣⲁ я ⲯⲉ ⲧⲉⳝя υⳅⲩⲃⲉⳡⲩ ⳅⲇⲉⲥь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲟⲧⲡυⲏⲁⲗ ⲧя ⲥⲗⲟⲃⲏⲟ ⲅⲣⲩⲱⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥыⲏⲟⲕ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲥⲗⲁⳝⲉύⲱⲉύ ⲡⲟⲇⲭⲩύⲏⲟύ ⲣⲁⳝⲟⲃⲡⲁⲗⲟύ ⲱⲗюⲭυ ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲏⲉ ⲡⲣυⲃⲥⲉⲗюⲇⲏⲟ ⲣⲉⲱυⲗ ⳅⲁⲗⲩⲡⲩ ⲡⲟ ⲥⲁⲙыⲉ ⲅⲗⲁⲏⲇы ⲃⲥⲗюⲏяⲃυⲧь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟю ⲥⲗюⲏяⲃⲩю ⲙⲁⲧь ⲱⲗюⲭⲩ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲅⲗⲩ ⳅⲁⳝьёⲙ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟю ⲏⲁ ⲱⲁⲙⲡⲩⲣυⲏⲩ ⲥⲃⲟю ⲟⲇⲉⲗ υ ⲡⲩⲥⲧυⲗ ⲙⲁⲣυⲏⲟⲃⲁⲧьⲥя ⲃ ⲡⲣυⲙⲉⲥⲉ ⲙⲟⳡυ υ ⲥⲡⲉⲣⲙы<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲥⲧⲣⲉⲙяⲏⲕⲟύ ⲡⲟ ⲅⲟⲣⳝⲩ ⲩⲉⳝⲁⲗ ⳡⲧⲟ ⲟⲏ ⲕⲁⲕ ⲧⲉⲗёⲏⲟⲕ ⳅⲁⲃыⲗ ⲉⳝⲁⲧь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲃⲏⲁⲧⲩⲣⲉ ⲥⲃⲟё ⲧⲟⲗⲥⲧⲟⲙяⲧⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲧⲟⲡυ ⲏⲁⲭⲩ ⳝⲟⲣⲟⲃ ⲃыⲉⳝⲁⲏⲏыύ ⲥⲗыⲱⲁⲗ ⲙя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲣⲟⲱⲙⲉⲧⲕυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩяⲙυ ⲥⲙⲉⲧё<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲧя ⲡⲟⲇ ⲃⲥⲭⲣюⲕυ эⲗьⲫυⲥύⲕυⲉ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⲟⳝⲉⳅⲅⲗⲁⲃⲗю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲟⳝⲟύ ⲡⲟ ⲟⲕⲏⲩ ⲃьⲉⳝⲁⲱυⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲁⲕυⲏь 5 ⲥυⲏⲟⲏυⲙⲟⲃ ⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳡⲧⲟ ⲧы ⲃыⲗⲟⲃυⲧь ⲡыⲧⲁⲉⲱьⲥя ⲕⲣⲟⲙⲉ ⳅⲁⲗⲩⲡы ⲙⲟⲉύ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲏⲉⲩⲙⲏⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲥⲧⲟя ⲡⲟ ⲡⲟяⲥ ⲃ ⲃⲟⲇⲉ ⲟⲏⲁ ⲩⲙⲩⲇⲣυⲗⲁⲥь ⲩⲙⲉⲣⲉⲧь ⲟⲧ ⲟⳝⲉⳅⲃⲟⲯυⲃⲁⲏυя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲭⲩⲗⲉ ⳅⲇⲉⲥя ⲥ ⳡⲗⲉⲏⲁⲙ ⲙⲟυⲙ яⲕⲱⲁⲉⲱьⲥя ⲏⲉⲧⲟⲡыⲣь ⳝⲗя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳅⲁⲥⲗⲟⲏⲕυ ⲕⲟⲧⲟⲣыⲉ ⲡⲉⲣⲉⲅⲁⲣⲁⲯυⲃⲁюⲧ ⲉύ ⲇыⲭⲁⲧⲉⲗьⲏыⲉ ⲡⲩⲧυ ⲥⲗⲟⲙⲁⲉⲙ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲏυⲥⲟⲏ ⲥ ⲙⲉⲣⳅⲕυⲙυ ⲃⲥⲕⲣюⲕⲁⲙυ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲣⲁⳝⲟⲃⲡⲁⲗыύ ⲟⲕⲁⳡⲁⲏⲉⲗыύ ⲡⲉⲱⲕⲟⲇⲟⲇυⲕ ⲧы ⳡⲟ ⲧⲁⲙ ⲃⲏⲁⲩⲧⲣⲉ ⲃ ⲥⲉⳝя ⲣⲉⲱυⲗⲙ ⲙⲏⲉ ⲡⲟⲃⲉⲣυⲧь ⲁⲣⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲯⲉ ⲡⲟⲇ ⲙⲟυⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲏⲉⲥⲕⲟⲏⳡⲁⲉⲙыⲙ ⲡⲟⲙⲣёⲱь ⳅⲇⲉⲥь<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲕⲁ ⲏⲉ ⲥⲧⲁⲗⲟ ⲟⲕⲟⲏⳡⲁⲧⲉⲗьⲏⲟ ⲡⲟⳅⲇⲏⲟ ⳝⲉⲅυ ⲟⲧ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲕⲁⲥⲧⲣⲩⲗⲉύ ⲡⲉⲣⲉⲉⳝⲁⲗ ⲁⲣⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲯⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲧυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲅⲏⲩ ⲡⲟⲡⲣⲟⲥⲧⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲉ ⲥⲗыⲱⲩ ⲧⲩⲧ ⲡυⲥⲕⲁ ⲧⲃⲟⲉⲅⲟ ⲥыⲏⲟⲕ ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉύ ⲧⲣⲁⲥⲥы<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧя ⲥⲃⲟυⲙ ⲱⲩⲅⲁю <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲥё υⲇυ ⲇⲁⲗьⲱⲉ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲱυⲣⲩю ⲉⲧⳝя ⲡⲟ ⲕⲁⲇыⲕⲩ ⲱⲟⲗⲁⲃⲩ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲃⲟёⲙ ⳡⲗⲉⲏⲉ ⲕⲁⲧⲁю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲟⲅⲏⲁⲇыⳃⲁⲱυⲙ ⳡⲗⲉⲏⲟⲙ ⲃыⲯⲅⲩ ⲏⲁⲡⲣⲟⳡь ⲡⲗⲉⲙя ⲧⲩⲏⲉяⲇцⲉⲃ ⲧⲃⲟυⲭ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲧυⲭⲟⲧⲃⲟⲣⲏⲟ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲏⲉⳝⲗⲁⲅⲟⲣⲟⲇⲏⲁя ⲡⲟⲙⲉⲥь ⲥⲟⳝⲁⳡья ⲏⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲯⲉ ⲩⲧⲟⲙυⲗⲁ ⲙⲟύ ⲡⲉⲏυⲥ ⲥⲃⲟυⲙυ ⳡⲁⲥⲧыⲙυ ⲟⲧⲥⲟⲥⲁⲙυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲱυⲣⲕⲩ ⲣⲁⳅⲙⲟⳡⲩ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⲩⲕⲟⲣⲟⳅⲏⲉⲏⲏⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲉⲱьⲥя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲧыⲗⲕⲟύ ⲡⲟ ⲱⲉⲉ ⲃьⲉⳝⲁⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲁⲗё ⲙⲁⲣⲁⳅⲙⲁⲧυⳡⲉⲥⲕυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲏⲉ ⲃⲧⲉⲣⲡⲗυⲃⲁύ ⲧⲟⲗьⲕⲟ ⲭⲩυ ⲏⲁⲱυ ⲧⲩⲧ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲙⲁⲧь ⲃыⲉⳝⲉⲙ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟⲉⲅⲟ ⲁⲃⲥⲧⲣⲁⲗⲟⲡυⲧⲉⲕⲁ ⲟⲧцⲁ ⲡⲉⲇυⲕⲟⲃⲁⲧⲟⲅⲟ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩⲉⲙ ⲧⲉ ⲡυⲣⲥυⲏⲅ ⲥⲇⲉⲗⲁⲗ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲙⲁⲙⲁⲏⲉ ⲧⲃⲟⲉ ⲙⲟⳡⲕⲩ ⲭⲩⲉⲙ ⲡⲣⲟⲕⲟⲗⲟⲗ <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝⲁⲗⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲥⲙⲉⲥью ⲥⲡⲉⲣⲙы υ ⲙⲟⳡυ υⳅⲅⲟⲏυⲙ ⲧⲉⳝя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲡⲟⲧⲩⲥⲧⲁⲣⲟⲏⲏⲉ ⲥⲟⲥёⲱь <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲥⲗюⲏяⲃⲟ υⳅⲩⲃⲉⳡⲩ ⲧⲉⳝя<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲣⲉⲕⲧⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя <emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲧы ⲕⲩⲇⲁ ⲡⲟⲥⲙⲉⲗ ⲧⲩⲧ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲡⲟⲡⲉⲣⲉⲧь ⲥыⲏⲟⲕ ⲁⲡⲣυⲟⲣυ ⲏⲉⲇⲉⲉⲥⲡⲟⲥⲟⳝⲏⲟύ ⳝⲗяⲇυ<emoji document_id=5341819141508574901>🚬</emoji>"
, "[<emoji document_id=5341819141508574901>🚬</emoji>]ⲭⲩяⲙυ ⲩⳃⲉⲗьⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲕⲣⲟⲉⲙ <emoji document_id=5341819141508574901>🚬</emoji>"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl6))
            await sleep(0.1)
            await sleep(time)

    async def больcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Б᧐᧘ь ɜᥲκ᧐нчᥙ᧘а ɜᥲδᥙρᥲᴛь хуᥱᥴ᧐ᥴ᧐ʙ ʙ ʍᥙρ ɜ᧘ᥲ <emoji document_id=5784974820592586088>🔥</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Б᧐᧘ь нᥲчᥲ᧘ᥲ ɜᥲδᥙρᥲᴛь хуᥱᥴ᧐ᥴ᧐ʙ ʙ ʍᥙρ ɜ᧘ᥲ <emoji document_id=5784974820592586088>🔥</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl7 = ["〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас сотрясение мозга своим посохом межножным наколдую〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕моя залупа тебе тут скальпа вырвет 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сынок шлюхи даже не вздумай убежать отсюда терпила наших хуев которые являются залупой прекрасной〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе тут даже шанса не оставлю около своего хуя жирного сыновье шалавы слабое〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай покрепче что-ли взирай в мой хуй терпило ебаное〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас покрытие инеем устрою своим хуем " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе тут залупой шею сломаю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай собери свои сопли в кулак и принимай повсеместное избиение свое〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебя тут без внимания так просто не оставлю понимаешь сын шалавы〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты че тут сбежать удумал ХАХАХХ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас выброс устрою в твоей катлаванной маня мирочной фантазией〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕тупой сын шалавы я тебе щас своим хуем глаза выколю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты ебучий зарыданный сынок шлюхи мы тебе щас здесь своими залупами которые в данной конференции уже являются богоебырем для тебя сломаем ебало наизнанку 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты ебучий сынок проститутки я тебе щас своим хуем лопатки сверну во благо твоего же изсушения〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты полукровочная терпила нихуя не стоющая〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шалавы кста〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ебал твою мать кста〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕терпила ебаная давай наши хуи во свое возмездие ручное принимай〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе сейчас промежуточный турнир устрою на сосание наших половых агрегатов〔<emoji document_id=5784974820592586088>🔥</emoji>〕" , 
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе сейчас своим хуем который является залупой прекрасной сломаю еблище тупой пасынок шлюхи сопливый〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай своими слюнями мой член полируй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты полиглот ебучий не слыхай〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе мамашку тут трахал сын бляди〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты только душком своим не упади девочка ебучая сука〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас своим хуем сотрясение мозга сотворю без каких либо на это усилий〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ахах сынок шлюхи вздумал себе в мозги вбить что я буду тут об него руки морать〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты чего сын шалавы ебаный ты же не более чем в качестве насадки на наши пенисы〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас черепушку своим членом снесу〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай там боготворяй мое величие я тебе тут в ином случае попросту и шансов не оставлю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай быстре чтоли пиши уже злупышканец ебучий〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас своей залупой межножной попросту сломаю все конечности и конечно же твои дальнейшие попытки на какие либо сопротивления〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты пиздуй уже мое пенисовидное устройство ласкать что-ли〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе даже и малейшего шанса на сопротивления не оставлю своим прибором естественно межножным〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шалавы ебучий попросту стухни тут как лярва ебучая〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я своим хуем пизду твоей матери на забор повесил〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты попросту терпила наших членов и не упрекай〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕кидай какие либо сопротивления моему хую межножному〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шлюхи кста〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я твою мать ебал у морфологической зоны〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шалавы раз ты находишься еще в данной конференции ты на сегодня получил не достаточное количество агрегатов в рот?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе попросту щас твои косточки повыламываю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе тут никакакого шанса в действительности не оставлю " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕будем заниматься повсеместно твоим избиением 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕естественно сын шалавы здесь засел в свои уголки сука〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я твоей матери мать изнасиловал〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шалавы ебучий " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай там наши агрегаты в качестве еды принимай〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын шалавы ебучий не понял меня чтоли?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас твои лопатки попросту возьму и своим залуповидным устройством наизнанку выверну и использую как в качестве твоего тыкания〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты понимаешь сын шалавы ебучий что ты лишь в качестве сынка шалавы сдесь годишься〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я не понимаю сын шалавы ебучий ты чтоли внатуре не достаточное прогнозирование фактов на сегодня получил?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас ебало сломаю сын шлюхи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты давай телка ебаная чтоли затерпливай вновь наши агрегаты 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас своим членом черепушку выгну〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе попросту тут сломаю все внутренности〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕твой кишечник сжал то ультрофобных провиднений〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты чтоли там давай бледного лови〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕законпленную трубу твоей мамаши аккуратно ебал〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты сын профурсетки шмарообразной〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебе щас шлакообразного в пиздень выебу 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты всемирная насадка на члены не более〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тут являюсь богоебырем для тебя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тут представлю из себя лишь то что стану тебя слабака ебливого избивать по кругу 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я щас попросту все твои харизмированные попытки деградации сломаю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты дегеративное сыновье шалавы слюнявое " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕внатуре собери свои сопли в кулак чтоли и пиздуй на мой хуец величественный〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебя величием своего члена заполнил〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты толстомясый злупышканец〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебя своей замшей пинал〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я тебя щас порастасткиваю по городу " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕своеей залупой межножной〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ты пидорас блядский сука〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴇбучий ᴄын ɯᴀᴧᴀʙы ᴛᴀᴋ ᴄᴋᴀжᴇʍ ᴄʙᴏᴇᴏбᴩᴀɜнᴏᴦᴏ ᴩᴏдᴀ ᴛᴇᴩᴨиᴧᴀ нᴀɯих хуᴇʙ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴄᴏᴛᴩяᴄᴇниᴇ ʍᴏɜᴦᴀ ᴄʙᴏиʍ ᴨᴏᴄᴏхᴏʍ ʍᴇжнᴏжныʍ нᴀᴋᴏᴧдую〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ʍᴏя ɜᴀᴧуᴨᴀ ᴛᴇбᴇ ᴛуᴛ ᴄᴋᴀᴧьᴨᴀ ʙыᴩʙᴇᴛ 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄынᴏᴋ ɯᴧюхи дᴀжᴇ нᴇ ʙɜдуʍᴀй убᴇжᴀᴛь ᴏᴛᴄюдᴀ ᴛᴇᴩᴨиᴧᴀ нᴀɯих хуᴇʙ ᴋᴏᴛᴏᴩыᴇ яʙᴧяюᴛᴄя ɜᴀᴧуᴨᴏй ᴨᴩᴇᴋᴩᴀᴄнᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴛуᴛ дᴀжᴇ ɯᴀнᴄᴀ нᴇ ᴏᴄᴛᴀʙᴧю ᴏᴋᴏᴧᴏ ᴄʙᴏᴇᴦᴏ хуя жиᴩнᴏᴦᴏ ᴄынᴏʙьᴇ ɯᴀᴧᴀʙы ᴄᴧᴀбᴏᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй ᴨᴏᴋᴩᴇᴨчᴇ чᴛᴏ-ᴧи ʙɜиᴩᴀй ʙ ʍᴏй хуй ᴛᴇᴩᴨиᴧᴏ ᴇбᴀнᴏᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴨᴏᴋᴩыᴛиᴇ инᴇᴇʍ уᴄᴛᴩᴏю ᴄʙᴏиʍ хуᴇʍ " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴛуᴛ ɜᴀᴧуᴨᴏй ɯᴇю ᴄᴧᴏʍᴀю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй ᴄᴏбᴇᴩи ᴄʙᴏи ᴄᴏᴨᴧи ʙ ᴋуᴧᴀᴋ и ᴨᴩиниʍᴀй ᴨᴏʙᴄᴇʍᴇᴄᴛнᴏᴇ иɜбиᴇниᴇ ᴄʙᴏᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбя ᴛуᴛ бᴇɜ ʙниʍᴀния ᴛᴀᴋ ᴨᴩᴏᴄᴛᴏ нᴇ ᴏᴄᴛᴀʙᴧю ᴨᴏниʍᴀᴇɯь ᴄын ɯᴀᴧᴀʙы〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы чᴇ ᴛуᴛ ᴄбᴇжᴀᴛь удуʍᴀᴧ ХАХАХХ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ʙыбᴩᴏᴄ уᴄᴛᴩᴏю ʙ ᴛʙᴏᴇй ᴋᴀᴛᴧᴀʙᴀннᴏй ʍᴀня ʍиᴩᴏчнᴏй ɸᴀнᴛᴀɜиᴇй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛуᴨᴏй ᴄын ɯᴀᴧᴀʙы я ᴛᴇбᴇ щᴀᴄ ᴄʙᴏиʍ хуᴇʍ ᴦᴧᴀɜᴀ ʙыᴋᴏᴧю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴇбучий ɜᴀᴩыдᴀнный ᴄынᴏᴋ ɯᴧюхи ʍы ᴛᴇбᴇ щᴀᴄ ɜдᴇᴄь ᴄʙᴏиʍи ɜᴀᴧуᴨᴀʍи ᴋᴏᴛᴏᴩыᴇ ʙ дᴀннᴏй ᴋᴏнɸᴇᴩᴇнции ужᴇ яʙᴧяюᴛᴄя бᴏᴦᴏᴇбыᴩᴇʍ дᴧя ᴛᴇбя ᴄᴧᴏʍᴀᴇʍ ᴇбᴀᴧᴏ нᴀиɜнᴀнᴋу 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴇбучий ᴄынᴏᴋ ᴨᴩᴏᴄᴛиᴛуᴛᴋи я ᴛᴇбᴇ щᴀᴄ ᴄʙᴏиʍ хуᴇʍ ᴧᴏᴨᴀᴛᴋи ᴄʙᴇᴩну ʙᴏ бᴧᴀᴦᴏ ᴛʙᴏᴇᴦᴏ жᴇ иɜᴄуɯᴇния〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏᴧуᴋᴩᴏʙᴏчнᴀя ᴛᴇᴩᴨиᴧᴀ нихуя нᴇ ᴄᴛᴏющᴀя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴀᴧᴀʙы ᴋᴄᴛᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ᴋᴄᴛᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛᴇᴩᴨиᴧᴀ ᴇбᴀнᴀя дᴀʙᴀй нᴀɯи хуи ʙᴏ ᴄʙᴏᴇ ʙᴏɜʍᴇɜдиᴇ ᴩучнᴏᴇ ᴨᴩиниʍᴀй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴄᴇйчᴀᴄ ᴨᴩᴏʍᴇжуᴛᴏчный ᴛуᴩниᴩ уᴄᴛᴩᴏю нᴀ ᴄᴏᴄᴀниᴇ нᴀɯих ᴨᴏᴧᴏʙых ᴀᴦᴩᴇᴦᴀᴛᴏʙ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" , 
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴄᴇйчᴀᴄ ᴄʙᴏиʍ хуᴇʍ ᴋᴏᴛᴏᴩый яʙᴧяᴇᴛᴄя ɜᴀᴧуᴨᴏй ᴨᴩᴇᴋᴩᴀᴄнᴏй ᴄᴧᴏʍᴀю ᴇбᴧищᴇ ᴛуᴨᴏй ᴨᴀᴄынᴏᴋ ɯᴧюхи ᴄᴏᴨᴧиʙый〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй ᴄʙᴏиʍи ᴄᴧюняʍи ʍᴏй чᴧᴇн ᴨᴏᴧиᴩуй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏᴧиᴦᴧᴏᴛ ᴇбучий нᴇ ᴄᴧыхᴀй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ʍᴀʍᴀɯᴋу ᴛуᴛ ᴛᴩᴀхᴀᴧ ᴄын бᴧяди〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴛᴏᴧьᴋᴏ дуɯᴋᴏʍ ᴄʙᴏиʍ нᴇ уᴨᴀди дᴇʙᴏчᴋᴀ ᴇбучᴀя ᴄуᴋᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴄʙᴏиʍ хуᴇʍ ᴄᴏᴛᴩяᴄᴇниᴇ ʍᴏɜᴦᴀ ᴄᴏᴛʙᴏᴩю бᴇɜ ᴋᴀᴋих ᴧибᴏ нᴀ ϶ᴛᴏ уᴄиᴧий〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴀхᴀх ᴄынᴏᴋ ɯᴧюхи ʙɜдуʍᴀᴧ ᴄᴇбᴇ ʙ ʍᴏɜᴦи ʙбиᴛь чᴛᴏ я буду ᴛуᴛ ᴏб нᴇᴦᴏ ᴩуᴋи ʍᴏᴩᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы чᴇᴦᴏ ᴄын ɯᴀᴧᴀʙы ᴇбᴀный ᴛы жᴇ нᴇ бᴏᴧᴇᴇ чᴇʍ ʙ ᴋᴀчᴇᴄᴛʙᴇ нᴀᴄᴀдᴋи нᴀ нᴀɯи ᴨᴇниᴄы〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ чᴇᴩᴇᴨуɯᴋу ᴄʙᴏиʍ чᴧᴇнᴏʍ ᴄнᴇᴄу〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴀᴧᴀʙы ᴇбучий ᴨᴏᴨᴩᴏᴄᴛу ᴄᴛухни ᴛуᴛ ᴋᴀᴋ ᴧяᴩʙᴀ ᴇбучᴀя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴄʙᴏиʍ хуᴇʍ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи нᴀ ɜᴀбᴏᴩ ᴨᴏʙᴇᴄиᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏᴨᴩᴏᴄᴛу ᴛᴇᴩᴨиᴧᴀ нᴀɯих чᴧᴇнᴏʙ и нᴇ уᴨᴩᴇᴋᴀй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴋидᴀй ᴋᴀᴋиᴇ ᴧибᴏ ᴄᴏᴨᴩᴏᴛиʙᴧᴇния ʍᴏᴇʍу хую ʍᴇжнᴏжнᴏʍу〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴧюхи ᴋᴄᴛᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ у ʍᴏᴩɸᴏᴧᴏᴦичᴇᴄᴋᴏй ɜᴏны〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴀᴧᴀʙы ᴩᴀɜ ᴛы нᴀхᴏдиɯьᴄя ᴇщᴇ ʙ дᴀннᴏй ᴋᴏнɸᴇᴩᴇнции ᴛы нᴀ ᴄᴇᴦᴏдня ᴨᴏᴧучиᴧ нᴇ дᴏᴄᴛᴀᴛᴏчнᴏᴇ ᴋᴏᴧичᴇᴄᴛʙᴏ ᴀᴦᴩᴇᴦᴀᴛᴏʙ ʙ ᴩᴏᴛ?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴨᴏᴨᴩᴏᴄᴛу щᴀᴄ ᴛʙᴏи ᴋᴏᴄᴛᴏчᴋи ᴨᴏʙыᴧᴀʍыʙᴀю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴛуᴛ ниᴋᴀᴋᴀᴋᴏᴦᴏ ɯᴀнᴄᴀ ʙ дᴇйᴄᴛʙиᴛᴇᴧьнᴏᴄᴛи нᴇ ᴏᴄᴛᴀʙᴧю " ,
            " будᴇʍ ɜᴀниʍᴀᴛьᴄя ᴨᴏʙᴄᴇʍᴇᴄᴛнᴏ ᴛʙᴏиʍ иɜбиᴇниᴇʍ 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴇᴄᴛᴇᴄᴛʙᴇннᴏ ᴄын ɯᴀᴧᴀʙы ɜдᴇᴄь ɜᴀᴄᴇᴧ ʙ ᴄʙᴏи уᴦᴏᴧᴋи ᴄуᴋᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʍᴀᴛь иɜнᴀᴄиᴧᴏʙᴀᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴀᴧᴀʙы ᴇбучий " ,
            " ᴛы дᴀʙᴀй ᴛᴀʍ нᴀɯи ᴀᴦᴩᴇᴦᴀᴛы ʙ ᴋᴀчᴇᴄᴛʙᴇ ᴇды ᴨᴩиниʍᴀй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ɯᴀᴧᴀʙы ᴇбучий нᴇ ᴨᴏняᴧ ʍᴇня чᴛᴏᴧи?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴛʙᴏи ᴧᴏᴨᴀᴛᴋи ᴨᴏᴨᴩᴏᴄᴛу ʙᴏɜьʍу и ᴄʙᴏиʍ ɜᴀᴧуᴨᴏʙидныʍ уᴄᴛᴩᴏйᴄᴛʙᴏʍ нᴀиɜнᴀнᴋу ʙыʙᴇᴩну и иᴄᴨᴏᴧьɜую ᴋᴀᴋ ʙ ᴋᴀчᴇᴄᴛʙᴇ ᴛʙᴏᴇᴦᴏ ᴛыᴋᴀния〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏниʍᴀᴇɯь ᴄын ɯᴀᴧᴀʙы ᴇбучий чᴛᴏ ᴛы ᴧиɯь ʙ ᴋᴀчᴇᴄᴛʙᴇ ᴄынᴋᴀ ɯᴀᴧᴀʙы ᴄдᴇᴄь ᴦᴏдиɯьᴄя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я нᴇ ᴨᴏниʍᴀю ᴄын ɯᴀᴧᴀʙы ᴇбучий ᴛы чᴛᴏᴧи ʙнᴀᴛуᴩᴇ нᴇ дᴏᴄᴛᴀᴛᴏчнᴏᴇ ᴨᴩᴏᴦнᴏɜиᴩᴏʙᴀниᴇ ɸᴀᴋᴛᴏʙ нᴀ ᴄᴇᴦᴏдня ᴨᴏᴧучиᴧ?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴇбᴀᴧᴏ ᴄᴧᴏʍᴀю ᴄын ɯᴧюхи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй ᴛᴇᴧᴋᴀ ᴇбᴀнᴀя чᴛᴏᴧи ɜᴀᴛᴇᴩᴨᴧиʙᴀй ʙнᴏʙь нᴀɯи ᴀᴦᴩᴇᴦᴀᴛы 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴄʙᴏиʍ чᴧᴇнᴏʍ чᴇᴩᴇᴨуɯᴋу ʙыᴦну〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ ᴨᴏᴨᴩᴏᴄᴛу ᴛуᴛ ᴄᴧᴏʍᴀю ʙᴄᴇ ʙнуᴛᴩᴇннᴏᴄᴛи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏй ᴋиɯᴇчниᴋ ᴄжᴀᴧ ᴛᴏ уᴧьᴛᴩᴏɸᴏбных ᴨᴩᴏʙиднᴇний〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы чᴛᴏᴧи ᴛᴀʍ дᴀʙᴀй бᴧᴇднᴏᴦᴏ ᴧᴏʙи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ɜᴀᴋᴏнᴨᴧᴇнную ᴛᴩубу ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴀᴋᴋуᴩᴀᴛнᴏ ᴇбᴀᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴄын ᴨᴩᴏɸуᴩᴄᴇᴛᴋи ɯʍᴀᴩᴏᴏбᴩᴀɜнᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ɯᴧᴀᴋᴏᴏбᴩᴀɜнᴏᴦᴏ ʙ ᴨиɜдᴇнь ʙыᴇбу 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ʙᴄᴇʍиᴩнᴀя нᴀᴄᴀдᴋᴀ нᴀ чᴧᴇны нᴇ бᴏᴧᴇᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛуᴛ яʙᴧяюᴄь бᴏᴦᴏᴇбыᴩᴇʍ дᴧя ᴛᴇбя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛуᴛ ᴨᴩᴇдᴄᴛᴀʙᴧю иɜ ᴄᴇбя ᴧиɯь ᴛᴏ чᴛᴏ ᴄᴛᴀну ᴛᴇбя ᴄᴧᴀбᴀᴋᴀ ᴇбᴧиʙᴏᴦᴏ иɜбиʙᴀᴛь ᴨᴏ ᴋᴩуᴦу 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я щᴀᴄ ᴨᴏᴨᴩᴏᴄᴛу ʙᴄᴇ ᴛʙᴏи хᴀᴩиɜʍиᴩᴏʙᴀнныᴇ ᴨᴏᴨыᴛᴋи дᴇᴦᴩᴀдᴀции ᴄᴧᴏʍᴀю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴇᴦᴇᴩᴀᴛиʙнᴏᴇ ᴄынᴏʙьᴇ ɯᴀᴧᴀʙы ᴄᴧюняʙᴏᴇ " ,
            " ʙнᴀᴛуᴩᴇ ᴄᴏбᴇᴩи ᴄʙᴏи ᴄᴏᴨᴧи ʙ ᴋуᴧᴀᴋ чᴛᴏᴧи и ᴨиɜдуй нᴀ ʍᴏй хуᴇц ʙᴇᴧичᴇᴄᴛʙᴇнный〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбя ʙᴇᴧичиᴇʍ ᴄʙᴏᴇᴦᴏ чᴧᴇнᴀ ɜᴀᴨᴏᴧниᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴛᴏᴧᴄᴛᴏʍяᴄый ɜᴧуᴨыɯᴋᴀнᴇц〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбя ᴄʙᴏᴇй ɜᴀʍɯᴇй ᴨинᴀᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбя щᴀᴄ ᴨᴏᴩᴀᴄᴛᴀᴄᴛᴋиʙᴀю ᴨᴏ ᴦᴏᴩᴏду ",
            " ᴄʙᴏᴇᴇй ɜᴀᴧуᴨᴏй ʍᴇжнᴏжнᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨидᴏᴩᴀᴄ бᴧядᴄᴋий ᴄуᴋᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ᴏчᴇнь ᴏбᴩᴀдᴏʙᴀᴧᴀᴄь ᴋᴏᴦдᴀ я ᴄᴏᴦᴧᴀᴄиᴧᴄя ᴇᴇ бᴇдняжᴋу ᴨᴏᴋᴏᴩʍиᴛь ᴄʙᴏᴇй ᴄᴨᴇᴩʍᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕дᴀʙᴀй ᴛы ᴄᴇйчᴀᴄ ᴏᴛᴄᴏᴄᴇɯь ʍᴏй хуй ᴀ ᴨᴏᴛᴏʍ я ϶ᴛиʍ хуᴇʍ ʙыᴇбу ᴛʙᴏю ʍᴀᴛь ɯᴧюху〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕϶ᴛᴏ ʙᴄё нᴀ чᴛᴏ ᴛы ᴄᴨᴏᴄᴏбᴇн ᴄын ɯᴧюхи? уйди нᴀхуй нᴇ ᴨᴏɜᴏᴩь ᴄʙᴏю ʍᴀᴛь ɯᴧюху.〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄᴇйчᴀᴄ нᴀʍᴀᴛᴀю ᴛʙᴏй ᴩᴏᴛ нᴀ ᴄʙᴏй чᴧᴇн и ɜᴀдуɯу ᴛᴇбя нᴀхуй?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴄᴏʙᴇᴛую ᴛᴇбᴇ ᴨᴏйᴛи нᴀхуй ᴛᴀᴋ ᴋᴀᴋ нᴀ бᴏᴧьɯᴇᴇ чᴇʍ ᴏᴛᴄᴏᴄ ʍᴏᴇᴦᴏ хуя ᴛы нᴇ ᴄᴨᴏᴄᴏбᴇн〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴋᴏᴦдᴀ ᴛы ᴄᴏᴄᴇɯь ʍᴏй хуй ᴛы нᴀᴄᴧᴀждᴀᴇɯьᴄя ᴋᴀждᴏй ʍинуᴛᴏй, ᴋᴀждᴏй ᴄᴇᴋундᴏй ʙᴇдь ᴛы нᴀᴄᴛᴏᴧьᴋᴏ хᴏᴩᴏɯий хуᴇᴄᴏᴄ и ᴛᴇбᴇ ϶ᴛᴏ ᴨᴩинᴏᴄиᴛ удᴏʙᴏᴧьᴄᴛʙиᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я жᴇ ᴛᴇбя ᴛуᴛ ʙыᴇбу нᴀ ᴄᴨинᴇ ᴛʙᴏᴇй жᴇ ʍᴀʍы и ᴛы ʍнᴇ дᴏᴋᴀжᴇɯь ᴛуᴛ ᴛᴏᴧьᴋᴏ ᴛᴏ, чᴛᴏ ᴛы ᴄᴧᴀбый ᴄын ɯᴧюхи, нᴇ бᴏᴧᴇᴇ.〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴋᴧиᴛᴏᴩ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ϶ᴛᴏ чᴩᴇɜʙычᴀйнᴏ ᴏᴨᴀᴄнᴀя ɜᴏнᴀ?〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй нᴇ ᴨиɜди, ᴀ хуй ʍᴏй ʙᴄᴀᴄи ᴨиɜдᴀбᴏᴧ ᴇбᴀный. ᴛы жᴇ ᴛуᴛ и ᴄуᴛᴏᴋ нᴇ ᴨᴩᴏᴛянᴇɯь, убᴇжиɯь ᴄʙᴏᴇй ʍᴀʍᴀɯᴇ ᴨиɜду ᴧиɜᴀᴛь и хʙᴀᴄᴛᴀᴛьᴄя ᴛᴇʍ, чᴛᴏ ᴏᴛᴄᴏᴄᴀᴧ хуй ʙᴇᴧиᴋᴏʍу ɜᴧᴏдᴇю.〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ɜнᴀᴧ чᴛᴏ ᴛʙᴏю ʍᴀᴛь хуёʍ иɜ ᴏᴋнᴀ ʙыᴋинуᴧ ᴀ ᴏнᴀ ʙᴄᴛᴀᴧᴀ и дᴀᴧьɯᴇ ᴨᴏбᴇжᴀᴧᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛухᴀ ᴄ 5 ᴧᴇᴛ нᴀ ʍᴏй хуй ʍᴏᴧиᴧᴀᴄь ᴧяʙᴩᴀ ᴇбучᴀя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀʍу хуёʍ ᴛᴀᴋ ᴩᴀɜʙёᴧ чᴛᴏ ᴏнᴀ ʙᴄᴇʍу ᴩᴀйᴏну ᴦᴏʙᴏᴩиᴧ чᴛᴏ ʍᴏй хуй ϶ᴛᴏ ᴩᴇᴧиᴋʙия〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀᴛь хуёʍ ᴛᴀᴋ ᴛᴏ дᴏ ᴏᴩᴦᴀɜʍᴀ дᴏʙёᴧ ᴀ ᴛʙᴏй бᴀᴛя ʙ ϶ᴛᴏ ʙᴩᴇʍя ʙ ᴀхуᴇ ᴄᴛᴏяᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ужᴇ дᴀʙнᴏ нᴀ хуᴇ ʍᴏёʍ ᴄидиᴛ ᴏнᴀ дуʍᴀᴇᴛ чᴛᴏ ᴇᴄᴧи ᴨуᴄᴋᴀᴇᴛ ᴄᴨᴇᴩʍᴀᴋ ᴨᴏ ᴋᴩᴏʙи ᴛᴏ ϶ᴛᴏ нᴏᴩʍᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дуʍᴀᴧ чᴛᴏ ᴛʙᴏя ʍᴀᴛь нᴀ ɯᴀᴧᴀʙᴀ ʍы ᴇё ᴄ ᴨᴀцᴀнᴀʍи ɜᴀ дʙᴏᴩᴀʍи хуяʍи ᴨᴏᴧᴏᴄᴏʙᴀᴧи ᴛᴏᴧьᴋᴏ нᴇ ᴋᴏʍу〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴇщё ʍᴏᴧиɯьᴄя ɜᴀ ᴛᴏ чᴛᴏбы ᴛʙᴏя ʍᴀᴛухᴀ ʍнᴇ хуй ᴄᴏᴄᴀᴧᴀ ᴇᴄᴧи дᴀ ᴛᴏ ʍᴏᴦу ᴨᴏɜдᴩᴀʙиᴛь ᴏнᴀ дᴏᴄихᴨᴏᴩ ɜᴀʙиᴄиʍᴀ ᴏᴛ хуя ʍᴏᴇᴦᴏ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ʍᴏᴦу ᴄᴋᴀɜᴀᴛь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʙ ᴩᴀдᴏᴄᴛь ᴄᴏᴄёᴛ ʍᴏй хуй и ϶ᴛᴏ ᴇй дᴀёᴛ ʍᴏᴩᴇ ᴨᴏᴧᴏжиᴛᴇᴧьных ϶ʍᴏций〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕и чё ᴛʙᴏя ʍᴀᴛь дᴏᴧᴦᴏ будᴇᴛ биᴛьᴄя ʙ ᴋᴏнʙуᴧьᴄиях ᴏᴛ хуя ʍᴏᴇᴦᴏ ɜᴀбиᴩᴀй ᴇё ᴄᴋᴏᴩᴇй дуᴩнᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы чё дуʍᴀᴇɯь я щᴀᴄ ᴛʙᴏю ʍᴀᴛь ᴨᴩᴏᴄᴛᴏ ᴛᴀᴋ ᴏᴛᴨущу нᴇ ᴨуᴄᴛь ᴦᴏд ʍнᴇ ᴨᴏᴄᴏᴄёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь нᴀ ᴛᴩᴀᴄᴄᴇ ᴄᴛᴏяᴧᴀ и ᴋᴀждый ᴩᴀɜ ждᴀᴧᴀ чᴛᴏ ʍᴏй хуй ᴇё ɜᴀбᴇᴩёᴛ нᴏ я ᴇй ᴧиɯь нᴀ ᴩᴏᴛᴀн ᴋидᴀᴧ и уᴇɜжᴀᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕и чё ᴛы дуᴩᴀ ᴇбᴀнᴀя ᴛʙᴏя ʍᴀᴛь ɜᴀ ʍᴏй хуй дᴩᴀᴧᴀᴄь ᴄ дᴇʙᴋᴀʍи ᴏнᴀ дуʍᴀᴧᴀ чᴛᴏ ᴄᴛᴀнᴇᴛ ᴧучɯᴇй ᴏᴛᴄᴏᴄᴋᴏй ʍᴏᴇᴦᴏ хуя ᴏнᴀ ᴨᴏчᴛи дᴏᴄᴛиᴦᴧᴀ ϶ᴛᴏй цᴇᴧи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴇᴄᴧи ᴛʙᴏю ʍᴀᴛь ᴨᴏᴄᴀдиᴛь нᴀ ʍᴏй хуй ᴨᴏʙᴇᴩь ᴏнᴀ нᴇ ᴄᴧᴇɜᴇᴛ ᴨᴏᴋᴀ нᴇ уʍᴩёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛʙᴏю ʍᴀᴛь ᴩиᴧи хуёʍ ᴨᴏхᴏᴩᴏниᴧ ᴏнᴀ уʍудᴩиᴧᴀᴄь ʙыбᴩᴀᴛьᴄя чᴛᴏбы нᴀ ᴨᴏᴄᴧᴇдᴏᴋ ᴇщё ʍнᴇ ᴏᴛᴄᴏᴄᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну ϶ᴛᴏ ужᴇ ᴄᴛᴩᴀннᴏ чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴛᴀᴋ чᴀᴄᴛᴏ ʙᴩёᴛ ᴛʙᴏᴇʍу ᴏᴛцу чᴛᴏ ᴏᴛᴄᴀᴄыʙᴀᴇᴛ ʍнᴇ ʙᴄᴇᴦᴏ ᴨᴏ 10 ᴩᴀɜ ʙ дᴇнь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏй ᴨᴀхᴀн ᴄниʍᴀᴧ нᴀ ʙидᴇᴏ ᴋᴀᴋ я ᴇбу ᴛʙᴏю ʍᴀᴛь и ᴩᴀдᴏʙᴀᴧᴄя ʙᴇдь я ᴛᴏжᴇ ʙᴇᴧиᴋий дᴧя ᴛʙᴏᴇᴦᴏ ᴨᴀхᴀнᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ʍᴏжᴇɯь ᴦᴏʙᴏᴩиᴛь ʙᴄё чᴛᴏ уᴦᴏднᴏ нᴏ я буду ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴨᴏᴋᴀ ᴏнᴀ нᴇ ᴄᴏʙᴇᴩɯиᴛ ᴄуицид〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь дᴀжᴇ нᴇ ʍᴏжᴇᴛ ᴀᴩᴦуʍᴇнᴛиᴩᴏʙᴀᴛь ᴄʙᴏё ᴄᴏᴄᴀния ϶ᴛᴏ ᴄᴛᴀᴧᴏ ᴇё хᴏби〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕нᴇ дуʍᴀᴧ чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴄᴏɜдᴀᴄᴛ ɸᴀн ᴋᴧуб дᴧя ʍᴏᴇᴦᴏ хуя и дᴏᴋᴀɜыʙᴀᴛь чᴛᴏ ʍᴏй хуй ᴄᴀʍый ᴧучɯий〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕и чё ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄёᴛ ᴀ ᴛы нᴇʍᴏщь дᴀжᴇ нᴇ ʍᴏжᴇɯь ᴇё ɜᴀʍᴇᴩиᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы чё бᴧяᴛь я щᴀ ᴛʙᴏю ʍᴀᴛь ʙ ᴨᴇᴩдᴀᴋ хуяᴩю ᴀ ᴏнᴀ ᴨыᴛᴀᴇᴛьᴄя ᴋудᴀ ᴛᴏ убᴇжᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕нᴇ ʍᴏᴦу ᴨᴏняᴛь ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь нᴀ ᴄᴛᴏᴧьᴋᴏ уᴄᴇᴩднᴏ ᴄᴏᴄёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" , 
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ʍᴏй хуй ᴋ чᴇʍу ᴏнᴀ ᴄᴛᴩᴇʍиᴛьᴄя " ,
            " ужᴇ ᴄбиᴧᴄя ᴄ чёᴛу ᴄᴋᴏᴧьᴋᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь нᴀдᴏ ᴄᴨᴩᴏᴄиᴛь у ᴛʙᴏᴇᴦᴏ ᴏᴛцᴀ ʙᴇдь ᴏн дᴩᴏчиᴧ нᴀ ϶ᴛᴏ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏй ᴏᴛᴇц дᴀʙнᴏ ужᴇ ухᴏди ᴄ ᴋʙᴀᴩᴛиᴩы и ждёᴛ ᴨᴏᴋᴀ я ᴨᴏᴇбу ᴛʙᴏю ʍᴀᴛь ᴀ ᴨᴏᴛᴏʍ ᴨᴩихᴏдиᴛ ᴋᴀᴋ нᴇ ʙ чёʍ нᴇ быʙᴀᴧ ᴏᴧух ᴛы ᴇбᴀный〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ᴨᴏᴋᴀ ϶ᴛᴏ нᴇ ᴄᴛᴀᴧᴏ ʍᴇйнᴄᴛᴩиʍᴏʍ ᴩиᴧи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕щᴀᴄ ᴛʙᴏя ʍᴀᴛь ᴋудᴀ ᴛᴏ ᴨᴏбᴇжᴀᴧᴀ и дуʍᴀᴇᴛ чᴛᴏ ᴇй ϶ᴛᴏ ᴨᴏʍᴏжᴇᴛ нᴏ ʙᴇдь ʍᴏй хуй ᴇё ʙᴄᴇ ᴩᴀʙнᴏ дᴏᴦᴏниᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏй дᴇд ʙ 45 ʍнᴇ хуй ɜᴀ ᴋуᴄᴏᴋ ᴄᴀᴧᴏ ᴄᴀᴄᴀᴧ ᴩиᴧи нᴇʍᴏщь ᴏн ᴇбᴀный дᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕и чё буду ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь дᴏ ᴛᴀᴧᴏʙᴀ и ᴛы нᴇ ᴄʍᴏжᴇɯь ʍнᴇ нᴇ чᴇᴦᴏ ᴄᴋᴀɜᴀᴛь ʙᴇдь ᴄᴀʍ ʙ ᴛᴀйнᴇ ʍнᴇ ᴄᴏᴄёɯь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй ᴛᴀʍ бᴏᴦᴏᴛʙᴏᴩяй ʍᴏᴇ ʙᴇᴧичиᴇ я ᴛᴇбᴇ ᴛуᴛ ʙ инᴏʍ ᴄᴧучᴀᴇ ᴨᴏᴨᴩᴏᴄᴛу и ɯᴀнᴄᴏʙ нᴇ ᴏᴄᴛᴀʙᴧю〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀʙᴀй быᴄᴛᴩᴇ чᴛᴏᴧи ᴨиɯи ужᴇ ɜᴧуᴨыɯᴋᴀнᴇц ᴇбучий〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ щᴀᴄ ᴄʙᴏᴇй ɜᴀᴧуᴨᴏй ʍᴇжнᴏжнᴏй ᴨᴏᴨᴩᴏᴄᴛу ᴄᴧᴏʍᴀю ʙᴄᴇ ᴋᴏнᴇчнᴏᴄᴛи и ᴋᴏнᴇчнᴏ жᴇ ᴛʙᴏи дᴀᴧьнᴇйɯиᴇ ᴨᴏᴨыᴛᴋи нᴀ ᴋᴀᴋиᴇ ᴧибᴏ ᴄᴏᴨᴩᴏᴛиʙᴧᴇния〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы ᴨиɜдуй ужᴇ ʍᴏᴇ ᴨᴇниᴄᴏʙиднᴏᴇ уᴄᴛᴩᴏйᴄᴛʙᴏ ᴧᴀᴄᴋᴀᴛь чᴛᴏ-ᴧи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛᴇбᴇ дᴀжᴇ и ʍᴀᴧᴇйɯᴇᴦᴏ ɯᴀнᴄᴀ нᴀ ᴄᴏᴨᴩᴏᴛиʙᴧᴇния нᴇ ᴏᴄᴛᴀʙᴧю ᴄʙᴏиʍ ᴨᴩибᴏᴩᴏʍ ᴇᴄᴛᴇᴄᴛʙᴇннᴏ ʍᴇжнᴏжныʍ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну и чё ᴛы дᴏᴄихᴨᴏᴩ дуʍᴀᴇɯь чᴛᴏ ʍᴏй хуй будᴇᴛ ᴇбᴀᴛь ʙᴀɯу ᴄᴇʍйᴋу ɜᴀ бᴇᴄᴨᴧᴀᴛнᴏ ᴄᴋᴏᴩᴏ ʙᴀʍ ᴨᴩидёᴛьᴄя ᴨᴧᴀᴛиᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴨᴩᴇждᴇ чᴇʍ ᴛʙᴏя ʍᴀᴛь нᴀчинᴀᴇᴛ ᴄᴏᴄᴀᴛь я бью ᴇй хуёʍ ᴨᴏ ᴦубᴇ ᴇй нᴩᴀʙиᴛьᴄя ʙᴇдь ϶ᴛᴏ ᴨᴀᴄᴛᴀ дᴀʙнᴏ ʙᴏ ʙᴧᴀᴄᴛи ʍᴏᴇᴦᴏ хуя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛы дᴀжᴇ нᴇ ɜᴀʍᴇᴛиɯь ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь нᴀ ʍᴏй хуй жиᴛь ᴨᴇᴩᴇᴇдᴇᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь щᴀ ʍᴏй хуй ᴩᴇɯиᴧᴀ ʙ ʍуɜᴇй ᴨᴩᴇнᴇᴄᴛи и ᴄᴋᴀɜᴀᴛь чᴛᴏ ϶ᴛᴏ ʙᴇᴧиᴋий ᴀᴩᴛᴇɸᴀᴋᴛ чё ᴏнᴀ ɯᴀᴧᴏʙᴀ ᴛᴏ ᴛᴀᴋᴀя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕бᴇɜ ɯуᴛᴏᴋ ᴇᴄᴧи ᴛʙᴏя ʍᴀᴛь нᴇ нᴀчнёᴛ ʙ ᴛᴇʍᴨᴇ ᴄᴏᴄᴀᴛь я ᴇй ɜᴀᴧуᴨᴏй ᴨᴏ ᴇбᴀᴧу ᴄᴇɜжу〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕и чё ᴛы щᴀᴄ ᴛᴏжᴇ будᴇɯь ᴏᴛ хуя уʙиᴧиʙᴀᴛь ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь иᴧи нᴀчнёɯь нᴀ нᴏᴩʍᴇ ᴄᴏᴄᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕нᴇ ʍᴏᴦу ᴨᴇᴩᴇдᴀᴛь ᴛᴇ чуʙᴄᴛʙᴀ ᴋᴏᴦдᴀ ᴛʙᴏя ᴄᴨидᴏɜнᴀя ʍᴀʍᴀɯᴀ ʍнᴇ ᴄᴏᴄёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀʍᴀɯᴀ щᴀ ʍᴏй хуй ɜᴀ щᴇᴋу ᴨуᴄᴛиᴧᴀ и нᴇ хᴏчᴇᴛ ʙыᴄᴏʙыʙᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ужᴇ нᴀ ʍᴏй хуй ᴨᴩыᴦᴀᴇᴛ ᴋᴀᴋ нᴀ ᴩᴀбᴏᴛу идёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ɜᴀчᴇʍ ᴛʙᴏя ʍᴀᴛь ᴏᴨяᴛь ʍнᴇ ᴄᴏᴄёᴛ ʍᴏжᴇᴛ ᴏнᴀ ᴨᴏдуʍᴀᴧᴀ чᴛᴏ ʍᴏжᴇᴛ ᴏᴛᴄᴀᴄыʙᴀᴛь ʍнᴇ бᴇɜᴧᴇʍиᴛнᴏ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь уᴨᴀᴧᴀ ᴨᴇᴩᴇд ʍᴏиʍ хуёʍ ᴋᴏᴦдᴀ ᴨᴏдᴄᴛᴀʙиᴧ ᴨᴇᴩдᴀᴋ ᴨᴇᴩᴇд ᴄʙᴏиʍ бᴀᴛᴇй нᴏ ϶ᴛᴏᴛ ᴏᴄёᴧ ᴨᴏбᴏяᴧᴄя ᴇᴦᴏ ᴨᴏᴇбᴀᴛь ʙᴇдь ᴏн ɜнᴀᴇᴛ чᴛᴏ ʍᴏя ɜᴀᴧуᴨᴀ ᴏᴨяᴛь ᴨᴩᴏбьёᴛ ᴇᴦᴏ ᴦᴏᴩб〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀʍуᴧьᴋᴀ щᴀ ʍᴏй хуй ᴨᴏ ᴦᴧᴀнды ᴨуᴄᴛиᴧᴀ я ᴨᴩᴇдᴧᴀᴦᴀю дᴀᴛь ᴇй ʍᴇдᴀᴧьᴋу ɜᴀ ᴦᴏдᴏʙᴏй ᴏᴛᴄᴏᴄ бᴇɜ ᴨᴇᴩᴇᴩыʙᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну ну ᴄᴋᴀжи чᴛᴏ ᴛʙᴏя ʍᴀʍᴀɯᴋᴀ нᴇ ɯᴀбᴏᴧдᴀ я ᴄʙᴏиʍ хуёʍ ϶ᴛᴏ ᴏᴨᴩᴏʙᴇᴩᴦну ",
            " ᴩᴀɜʙᴏᴩᴏɯиᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу хуёʍ и ʙынᴇᴄ ᴏᴛ ᴛудᴀ ʙᴄё чᴛᴏ ʍᴏжнᴏ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴛʙᴏю дуᴩную ʍᴀʍᴀɯу щᴀ нᴀ хуᴇ ɜᴀ ᴛᴀᴋиᴇ дʙижᴇния ᴨᴩᴏʙᴇᴩну〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕нᴇ ʙᴇᴩиɯь ʍнᴇ чᴛᴏ ᴛʙᴏя ʍᴀʍᴀɯᴀ ʍᴏй хуй бᴇɜᴀᴄᴛᴏнᴏʙчнᴏ ᴄᴏᴄёᴛ ᴛᴀᴋ ᴨᴩихᴏди ᴏнᴀ дᴀᴄᴛ ᴛᴇ уᴩᴏᴋи ᴏᴛᴄᴏᴄᴀ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕нᴇ ʍᴏᴦу ᴨᴏняᴛь ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴛᴀᴋᴀя ᴄᴧᴀбᴀя ɯᴧюхᴀ чᴛᴏ дᴀжᴇ ʍᴏй хуй ужᴇ ᴏᴄиᴧиᴛь нᴇ ʍᴏжᴇᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀʍᴀɯу щᴀ хуёʍ ᴨᴇᴩᴇʙᴇᴩну хᴏᴛя ϶ᴛᴏ жᴀᴧᴋᴀя нᴀчнёᴛ ᴏᴨяᴛь ʙ ᴋᴏнʙуᴧьᴄиях биᴛьᴄя〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну ужᴇ бᴇɜ ɯуᴛᴏᴋ ʙ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴩᴀɜᴀᴦнᴀᴧᴄя ᴀ ᴏнᴀ нᴀчинᴀᴇᴛ ᴋᴀᴋ ᴄʙинья ʙиɜжᴀᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀᴛь хуёʍ ʙыᴄᴇᴋ ɜᴀ ᴛᴏ чᴛᴏ ᴏнᴀ ᴛʙᴏᴇʍу бᴀᴛи ᴏᴛᴄᴏᴄᴀᴛь ᴨыᴛᴀᴧᴀᴄь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ᴧᴇɜᴧᴀ ᴋᴏ ʍнᴇ цᴇᴧᴏʙᴀᴛьᴄя нᴏ ᴇй ɜᴀᴧуᴨᴏй ᴧᴏб ᴩᴀᴄᴋᴩᴏɯиᴧ ᴨуᴄᴛь ɜнᴀᴇᴛ ᴄʙᴏё ʍᴇᴄᴛᴏ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну и чё ᴛʙᴏя ʍᴀᴛь ужᴇ ᴦиᴧьдию ᴄᴏɜдᴀᴧᴀ чᴛᴏбы ʍᴏй хуй ʙᴏᴄхʙᴀᴧяᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь щᴀ ʍᴏй хуй ᴨᴩи ᴨᴏдᴩуᴦᴀх ᴩᴀᴄхʙᴀᴧиʙᴀᴧᴀ и ᴏни ᴛᴏжᴇ ᴩᴇɯиᴧи ʍнᴇ ᴏᴛᴄᴏᴄᴀᴛь нᴏ ᴧучɯᴇ ᴛʙᴏᴇй ʍᴀᴛухᴇ нᴇ ᴋᴛᴏ нᴇ ᴄᴏᴄёᴛ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴇᴄᴧи ᴛы хᴏчᴇɯь ʍᴏй хуй ᴛᴏᴦдᴀ ᴛᴇ ᴨᴩидёᴛьᴄя ᴨᴏᴋᴏнᴋуᴩиᴩᴏʙᴀᴛь ᴄ ᴛʙᴏᴇй ʍᴀʍᴀɯᴇй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕 и чё ᴛы щᴀᴄ ᴨᴏдᴏхнᴇɯь нᴀ ʍᴏёʍ хую чᴇʍ ᴏᴨᴏɜᴏᴩиɯь ᴄʙᴏю ʍᴀʍᴀɯу хᴏᴛя ʍᴏй хуй и ᴛᴀᴋ ᴇё ᴏᴨуᴄᴛиᴧ ᴇɜ ᴇɜ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛуɯᴋᴀ ʍᴏжᴇᴛ ᴏᴛᴩицᴀᴛь чᴛᴏ ᴄᴏᴄᴀᴧᴀ ʍнᴇ нᴏ у ʍᴇня ᴇᴄᴛь ᴨᴩяʍᴏᴇ дᴏᴋᴀɜᴀᴛᴇᴧьᴄᴛʙᴏ ʙᴇдь я ɜᴀᴋᴀчᴀᴧ ᴇё иɜнуᴛᴩи ᴄᴨᴇᴩʍᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ᴨᴩᴏʙиниᴧᴀᴄь ᴨᴇᴩᴇд ʍᴏиʍ   хуёʍ и ᴇй ᴨᴩиɯᴧᴏᴄь иɜʙᴇняᴛьᴄя ᴄʙᴏᴇй жᴀᴧᴋᴏй ᴦᴧᴏᴛᴋᴏй〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну ᴛы ᴩиᴧи нᴇ ʙдуᴨᴧяᴇɯь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʍᴏй хуй ᴩᴇɯиᴧᴀ ʙ ᴀᴩᴇнду ʙɜяᴛь нᴀ дᴇнь иɜ ɜᴀ чᴇᴦᴏ ᴨᴩᴏдᴀᴧᴀ ᴨᴏчᴋу ᴛʙᴏᴇᴦᴏ бᴀᴛи〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну чё будᴇʍ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴛь иᴧи ᴛы ᴏᴨяᴛь ᴩᴇɯиᴧ ʍᴏй хуй нᴇ ᴄ ᴋᴇʍ нᴇ дᴇᴧиᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕хуёʍ ᴛʙᴏю ʍᴀᴛь щᴀ ᴩᴀɜʍᴇниᴩᴏʙᴀᴧ ᴀ ᴏнᴀ ᴏᴛ бᴧᴀᴦᴏдᴀᴩнᴏᴄᴛи ᴏб ʍᴏй хуй ᴄʙᴏю ᴨиɜду ᴄᴛёᴩᴧᴀ нᴀ ᴇɜ ᴇɜ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀᴛь щᴀ хуёʍ ᴩᴀᴄчᴇᴧᴇниᴧ ᴀ ᴏнᴀ дᴀжᴇ ʙ ᴛᴀᴋᴏʍ ᴨᴏᴧᴏжᴇнии ᴄʍᴏᴦᴧᴀ ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь нᴇ ʍᴏжᴇᴛ ᴨᴏняᴛь чᴛᴏ ʍᴏй хуй нᴇ ʙᴄᴇᴦдᴀ будᴇᴛ дᴇᴩжᴀᴛь нᴀд нᴇй ʙᴧᴀᴄᴛь ᴛᴀᴋ ᴛᴏ 〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕хуёʍ ᴛʙᴏю ʍᴀᴛь ᴨᴧᴏʍбиᴩᴏʙᴀᴧ ᴇй дᴀжᴇ ᴋ ᴄᴛᴀʍᴀᴛᴏᴧᴏᴦу хᴏдиᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏю ʍᴀᴛь хуёʍ ᴩᴀɜᴩᴇɜᴀᴧ ᴀ ᴏнᴀ ᴨᴏбᴇжᴀᴧᴀ ᴋ ᴛʙᴏᴇʍу бᴀᴛи и ᴨᴏᴋᴀɜᴀᴧᴀ ᴏᴛᴩᴇɜᴀную ᴨиɜду ᴋᴀᴋ ᴨᴩиᴋᴏᴧ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕хуёʍ ᴛʙᴏю ʍᴀᴛь нᴀучиᴧ ᴨиᴄᴀᴛь нᴏ ᴏнᴀ ᴨᴧᴏхᴏ ʙᴏᴄᴨᴩиниʍᴀᴇᴛ учᴇния и нᴀчинᴀᴇᴛ ᴄᴏᴄᴀᴛь нᴀ ᴀʙᴛᴏʍᴀᴛᴇ〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕я ᴄᴛᴩᴇᴧяᴧ ʙ ᴛʙᴏю ʍᴀᴛь хуёʍ и ᴏнᴀ ᴛʙᴀᴩь ᴏжиᴧᴀ и нᴀчᴀᴧᴀ ᴨᴏᴧɜᴛи ᴋ ʍᴏᴇʍу хую " ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ᴛʙᴏя ʍᴀᴛь ᴩᴇᴋᴏᴩᴛᴄʍᴇнᴋᴀ ᴨᴏ ᴄᴏᴄᴀнию ʍᴏᴇᴦᴏ хуя ᴇё ᴩᴇᴋᴏᴩд дᴀжᴇ ᴛʙᴏй бᴀᴛя нᴇ ʍᴏжᴇᴛ ᴨᴏбиᴛь〔<emoji document_id=5784974820592586088>🔥</emoji>〕" ,
            "〔<emoji document_id=5784974820592586088>🔥</emoji>〕ну и чё ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄᴀᴧᴀ нᴇ нᴀдᴏ ᴏᴛᴩицᴀᴛь ʙᴇдь ᴛы ᴛᴏжᴇ ɜᴀᴨᴏдᴏɜᴩᴇн ʙ ϶ᴛᴏʍ〔<emoji document_id=5784974820592586088>🔥</emoji>〕"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl7))
            await sleep(0.1)
            await sleep(time)

    async def гнефcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>𐌲нᥱɸ ɜᥲκ᧐нчᥙ᧘ дуɯᥙᴛь ᥴʙᥙн᧐ᥰ᧐д᧐δных хуᥱᥴ᧐ᥴ᧐ʙ <emoji document_id=5352887306590102199>♾</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>𐌲нᥱɸ нᥲчᥲ᧘ дуɯᥙᴛь ᥴʙᥙн᧐ᥰ᧐д᧐δных хуᥱᥴ᧐ᥴ᧐ʙ <emoji document_id=5352887306590102199>♾</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl8 = ["[<emoji document_id=5352887306590102199>♾</emoji>] ዘ𐌳 𐌲ᱛᱞꤕ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ᱬ𐌳ተᱩ ꤕऊሃ ተꤕ ᱴᱛ ᱬሃንᱟઝ𐌳ᱤᱩዘᱛᱬሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱤᱟᱦᱢᱦᱩ, 𐌓 ተꤕऊꤕ ꤕऊ𐌳ᱤᱩዘᱢઝ 𐌗ሃёᱬ ᱞ𐌳ንऊᱢଓ𐌳ᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ተᱟ 𐌍ሃઝ𐌍𐌳 ꤕऊ𐌳ዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍᱢ ᱬዘꤕ ᱚꤕተઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍᱢ ᱬዘꤕ ꤍሃ𐌍ઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛઝ𐌳 ተᱟ ᱬዘꤕ ᱤᱢ𐌟ꤕᱦᱩ 𐌓ᱢԱ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱤ𐌓ᱵ ଓᱛ ꤍᱤ𐌳ଓሃ #𐌳ᱚ𐌳ᱬଓ𐌳ꤕ𐌖 #ተ𐍂𐌳𐌗ተᱛ𐌖 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ଓᱟꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ሃऊᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ꤍᱤᱛᱬ𐌳ᱤ[<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ 𐌍ꤕᱞꤕን ᱷꤕઝᱛᱤᱚሃ ଓ ᱚଓꤕᱞᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦᱴᱞꤕ𐌗𐌳ᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ꤕऊꤕዘᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ᱚሃᱦሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ᱬ𐌳ተᱩ ꤕऊꤕዘᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌗ሃёᱬ ንሃऊᱟ ଓᱟऊᱢଓ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱤᱟᱦᱢᱦᱩ ᱬꤕዘ𐌓 ሃተઝ𐌳ዘᱛꤍ ꤕऊ𐌳ዘᱟᱢ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱷ𐌳ꤍ ꤕऊꤕዘᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ተᱟ ᱴ𐌳ꤍઝሃᱚ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 ઝሃᱚ𐌳 ተᱟ ᱴᱛተሃ𐌗ᱤ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ተꤕᱤᱛ𐌍ઝ𐌳 ዘꤕ ᱴᱛተሃ𐌗𐌳ᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ተꤕᱤᱛ𐌍ઝ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱞꤕ𐌲𐌳ᱤ ଓ ᱴᱛᱞዘ𐌗𐌳ऊꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ተꤕᱤᱛ𐌍ઝ𐌳, 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍઝ𐌳ᱤꤕ ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍଓᱢዘᱛᱬ𐌳ተઝ𐌳 ተᱟ ꤕऊ𐌳ዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ተሃተ𐌳 ᱬ𐌳ተᱩ 𐌗ሃ𐌓𐌍ሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ଓ 𐌗ሃᱢ ᱬዘꤕ ᱴᱛᱤንᱢ ተꤕᱤᱛ𐌍ઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱢᱦᱩ ઝ𐌳ઝ ଓ 45 𐌲ᱛᱚሃ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱢꤍተᱞꤕऊᱤ𐌓ᱤ ዘ𐌳 ଓᱛᱢዘꤕ ଓᱛ ꤍᱤ𐌳ଓሃ 3-ሃ ᱞꤕᱢ𐌗ሃ? [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊꤕዘᱢᱤ ᱴᱛ ઝᱞ𐌳𐌓ᱬ 𐌲ᱛᱞઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ ᱴᱞᱛଓ𐌳ᱤᱩዘᱛ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ 𐌗ᱛᱞᱛᱦᱛ 𐌟ꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦ ተᱟ ᱬዘꤕ ઝ𐌳ઝ ዘ𐌳ᱚᱛऊዘᱛ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊሃ ꤍᱤᱟᱦ ተᱟ 𐌍ሃᱚ𐌳ઝ ꤕऊ𐌳ዘᱟᱢ 𐌳ᱞሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃᱢԱ𐌳 ᱬᱛꤕ𐌲ᱛ ꤍᱛꤍዘᱢ ᱤሃ𐌍ᱦꤕ ऊᱤ𐌓ᱚᱢዘ𐌳 ઝᱛዘ𐌍ꤕዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱛᱴ𐌳ᱞᱟᱦ ተᱟ ꤕऊ𐌳ዘᱟᱢ ꤍሃઝ𐌳 𐌳ᱞሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱛꤍዘᱢ ᱬᱛꤕ𐌲ᱛ 𐌗ሃᱢԱ𐌳 ऊᱤ𐌓ᱚᱛꤕऊ ꤍሃઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓዘ𐌳ተሃᱞꤕ ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍଓᱛꤕᱬ 𐌗ሃꤕ ᱴᱛ𐌗ᱛᱞᱛዘᱵ ઝ𐌳ઝ ᱢ ଓꤕꤍᱩ ተଓᱛᱢ ᱴᱞᱛଓ𐌳ᱤᱩዘᱟᱢ ተᱞᱛᱤᱤᱢዘ𐌲 ᱬᱚꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ଓ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤍଓᱛᱢ 𐌗ሃᱢ ተᱟઝ𐌳ᱵ ተ𐌳ઝ ተᱛ ऊᱤ𐌓ተᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕ ን𐌳ᱤሃᱴᱛᱢ ዘ𐌳𐌗ሃᱢ ᱴᱞᱛઝᱞሃ𐌍ሃ ᱴᱞᱛተᱢଓ 𐌍𐌳ꤍᱛଓᱛᱢ ꤍተᱞꤕᱤઝᱢ ተᱟ ऊᱤ𐌓ተᱩ ᱛऊᱛꤍꤍ𐌳ዘ𐌳𐌓 𐌳ᱞሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ተᱟ ᱬᱛᱢ 𐌗ሃᱢ ꤍଓᱛᱢᱬᱢ 𐌲ሃऊ𐌳ᱬᱢ ऊᱛᱞᱛንᱚᱢᱤ ᱬᱛᱞ𐌓ઝ ꤕऊ𐌳ዘᱟᱢ ꤍሃઝ𐌳 𐌳𐌗𐌳𐌗 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተꤕ ᱴᱛ ऊᱛᱞᱛᱚꤕ ᱴᱞᱛଓᱛᱚᱢᱤ ଓዘ𐌳ተሃᱞꤕ 𐌳𐌗𐌳𐌗 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱛꤍꤕᱦ ተᱟ ᱬዘꤕ ᱴᱛ ऊᱤ𐌳ዘተሃ ऊᱤ𐌓ᱚᱢዘ𐌳 ꤍꤍ𐌳ዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ዘ𐌳 ꤍଓᱛᱢ 𐌗ሃᱢ ዘ𐌳ꤍ𐌳ᱚᱢᱤ ઝ𐌳ઝ ꤕऊ𐌳ዘሃᱵ ꤍዘ𐌳ꤍተᱩ ዘ𐌳 ሃᱚᱛ𐌍ઝሃ ઝ𐌗ꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ተᱟ ꤍ𐌳ꤍꤕᱦ ઝ𐌳ઝ ተᱛ ዘꤕ ᱴᱞ𐌳ଓᱢᱤᱩዘᱛ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛऊᱛꤍꤍ𐌳ᱤ 𐌟ꤕ ଓዘ𐌳ተሃᱞꤕ",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃ𐌓 ተᱟ ᱬᱛꤕ𐌲ᱛ ꤍᱛꤍ𐌳ᱤ ᱴᱞᱢऊᱤꤕ𐌟ꤕዘዘᱛ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ଓዘ𐌳ተሃᱞꤕ 𐌗ሃꤕᱬ ዘ𐌳 𐌳ᱞऊᱢተሃ ᱴ𐌓ተᱩᱚꤕꤍ𐌓ተ ᱚଓ𐌳 ᱛተᱴᱞ𐌳ଓᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃᱢ ተᱟ ᱬᱛᱢ ꤍᱛꤍ𐌳ᱤ ᱢ ተᱛ𐌍ઝ𐌳 ዘ𐌳 𑁌ተᱛᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ଓዘ𐌳ተሃᱞꤕ ዘ𐌳 ꤍଓᱛᱢ 𐌗ሃᱢ ᱴᱛ ꤍ𐌳𐌟ሃ, ऊሃᱚꤕተ ઝ𐌳ઝ ꤕऊ𐌳ዘᱟᱢ 𐌍𐌳ꤍᱛଓᱛᱢ ꤍሃઝ𐌳 ଓ ऊᱢዘᱛઝᱤᱩ ንᱟᱞᱢተᱩ ᱢꤍઝ𐌳ተᱩ ᱬᱛᱵ ን𐌳ᱤሃᱴሃ ઝ𐌗ꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱞ𐌳ᱦሃ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተꤕऊ𐌓 ꤕऊ𐌳ᱞᱢᱞሃᱵ ᱛተᱞሃऊꤕዘᱩ ꤕऊ𐌳ዘᱟᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍተꤕᱞଓ𐌓ተዘᱢઝ ꤕऊ𐌳ዘᱟᱢ ተꤕऊꤕ ઝᱤᱵଓ ꤍᱤᱛᱬ𐌳ᱤ 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳ᱚ𐌳ᱞᱛ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱬ𐌳ᱬ𐌳ዘ ተଓᱛᱵ ꤕऊ𐌳ᱦᱢᱞᱛଓ𐌳ᱤ ଓ ᱴ𐌳ઝᱢꤍተ𐌳ዘꤕ [<emoji document_id=5352887306590102199>♾</emoji>]","[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦ ઝ𐌳ઝ ዘᱞ𐌳ଓꤍተଓꤕዘዘᱟᱢ [<emoji document_id=5352887306590102199>♾</emoji>]","[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ዘ𐌳 ꤍꤕઝሃዘᱚᱟ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱞᱛଓዘᱛ ᱴᱛ ተᱞ𐌳ꤕઝተᱛᱞᱢᱢ  ꤍ𐌳ꤍꤕᱦ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊ𐌳ᱞᱢᱞᱛଓ𐌳ᱤ ተଓᱛᱵ ꤍꤕᱬꤕᱢઝሃ ꤍଓᱛᱢᱬ ᱢꤍተᱞꤕऊᱢተꤕᱤᱩꤍઝᱢᱬ 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ዘᱛଓᱛ𐌲ᱛᱚዘ𐌓𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍԱሃ ተꤕ ଓ ઝᱢᱦᱛઝ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 𐌲ᱤ𐌳𐌲ᱛᱤꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌳ऊᱢᱚዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ᱴሃऊᱤᱢ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟઝሃᱞꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ዘᱢንઝ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ᱴ𐌳ᱤᱢଓዘ𐌳 ሃ𐌟ᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱚ𐌳ଓꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ᱴꤕꤍᱚሃ ተꤕ 𐌗ሃꤕᱬ ᱴ𐌳ᱬꤕተꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ꤍᱴᱛઝᱛᱢዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ଓ ᱚꤕᱞꤕଓሃᱷઝꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴꤕꤍተሃ ተꤕ 𐌗ሃꤕᱬ ተሃᱦᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌘ᱞ𐌳ዘተ𐌳ᱤᱩዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ઝ𐌳ઝ ଓ ꤍተ𐌳ᱞᱢዘሃ ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 𐌳ተԱꤕᱴᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱴᱞꤕᱚሃᱞઝᱛଓ𐌳ተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 " [<emoji document_id=5352887306590102199>♾</emoji>]ଓꤕᱤᱢઝ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌟ᱛᱴᱛऊᱤ𐌓ᱚꤍઝᱢᱢ ꤕऊᱤᱢ𐌲𐌳ᱚ ተᱟ ꤍሃઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌲ዘᱢᱚᱛᱬሃᱚᱟᱢ 𐌲ᱤሃ𐌗ᱛᱚᱞᱟᱷ ꤍᱛꤍዘᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍઝᱛተᱛ𐌟ᱢᱞዘᱟᱢ ઝᱞᱢଓᱛઝᱞᱟᱤ 𐌗ሃᱢ ꤍᱤᱛଓᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱞ𐌳ઝᱛꤍሃ𐌍ᱢᱢ 𐌲ዘᱢᱚᱛተᱞ𐌓ꤍ 𐌗ሃꤕᱬ ተ𐌓 ሃऊᱩᱵ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛዘ𐌳 ᱬዘꤕ 𐌗ሃᱢ ꤍᱛꤍꤕተ ऊᱤ𐌓 ᱚሃᱞ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌳 ተᱟ ᱬᱛᱢ 𐌗ሃᱢ ଓን𐌳ᱬꤕꤍተᱛ ꤍᱛꤍઝᱢ ꤍᱛꤍ𐌳ᱤ 𐌟ꤕ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ 𐌓 ઝ𐌳ઝ ተଓᱛᱵ ᱬ𐌳ተᱩ 𐌓ᱢԱ𐌳ᱬᱢ ᱴᱞᱢᱚ𐌳ଓᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ ᱦઝᱛᱤᱩዘᱛᱬ ተሃ𐌳ᱤꤕተꤕ  [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝሃᱞᱢᱤઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተଓᱛᱵ ᱬ𐌳ተᱩ ሃ ᱴᱢଓዘሃᱦઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ን𐌳 ᱬ𐌳𐌲𐌳ንᱛᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ተᱞሃऊዘᱛ𐌲ᱛ ን𐌳ଓᱛᱚ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱤꤕꤍተዘᱢԱᱟ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱚꤕᱞꤕଓ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱛઝዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴᱛꤍተᱛ𐌓ዘዘᱛ ଓ ᱞᱛተ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ሃዘᱢተ𐌳ን𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱴᱤᱢተᱟ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱞ𐌳ઝᱛଓᱢዘᱟ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ଓ𐌳ዘዘᱟ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝᱛᱬᱛᱚ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ተሃᱬऊᱛ𐌍ઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝ𐌳ᱴᱛተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ଓꤕᱢᱴ-ᱦᱛᱴ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ꤍꤕઝꤍ-ᱦᱛᱴ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ઝᱛꤍᱬᱢተᱢ𐌍ꤕꤍઝᱛ𐌲ᱛ ᱬ𐌳𐌲𐌳ንᱢዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴꤕᱞꤕᱚ ተ𐌳ऊ𐌳𐌍ઝᱛᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ዘᱛ𐌲ᱢ ተꤕ 𐌳ऊ𐌳ꤍԱ𐌳ᱤ ꤍᱤꤕ𐌗ઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳ऊꤕᱚዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳ዘተሃንꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ꤍ ᱴᱞꤕꤍተᱢ𐌟𐌳ᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓ ተ𐌓 ꤍԱሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ዘ𐌳ᱢꤍ𐌳ଓ𐌳 ꤍ𐌳ꤍꤕᱦᱩ 𐌍ᱛተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ꤍ ऊᱛઝሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ꤕ𐌗 ᱴꤕꤍተሃ ተଓᱛᱵ 𐌗ሃꤕᱬ ን𐌳ᱚꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ 𐌍ᱛተዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱞᱛꤍଓꤕተᱤᱢᱤ ተ𐌓 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓꤕᱤᱢઝ𐌳ᱤꤕᱴዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱴꤕᱞꤕꤍተ𐌳ଓꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ऊꤕን 𐌍ꤕꤍተᱢ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ን𐌳ઝ𐌳ᱤᱛᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱢᱬሃዘᱢተꤕተዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ተᱞᱛ𐌲𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ऊꤕንᱞ𐌳ऊᱛተዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓ ଓ𐌳ᱤᱩꤕᱞꤕ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱴᱞ𐌳𐌳𐌲ᱞᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍԱሃ ተꤕ ଓ ሃ𐌗𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱬ𐌳ᱬ𐌳ዘ ተଓᱛ𐌓 ऊᱤ𐌓ᱚᱢዘ𐌳 ᱬዘꤕ ꤍᱛꤍ𐌳ᱤ𐌳 ᱴᱞᱢઝ𐌳ᱤᱢꤍᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳ଓ𐌳ᱚዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ሃꤍᱢᱤꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌓ᱬᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟଓꤕን [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳ᱬᱢዘሃተዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱞᱛꤍተᱢተሃተᱦዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓᱟᱴᱤ𐌳ተዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱚꤕᱴ𐌳ንᱢተዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴꤕᱞꤕଓꤕን ተ𐌓 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓ ᱴꤕ𐌍ꤕዘઝሃ ተꤕ ꤍԱሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 𐌳𐌲ᱞᱵ ꤍ𐌍𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ሃऊᱢᱤ ተ𐌓 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳ᱚ ተᱞ𐌳ᱴ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌳ଓ𐌳ᱚᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍተᱛᱴሃᱚᱛଓ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱴᱞ𐌳ᱴᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ን𐌳 ᱴ𐌳𐌍ઝሃ ተ𐌓 ᱢᱴሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳ꤍተᱞᱢᱞ𐌳ଓ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ተᱛዘઝ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ᱴ𐌳ᱚ ዘ𐌳ᱴᱞ𐌓𐌟ꤕዘᱢꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓ ઝᱛꤍᱬ𐌳ꤍ ᱛተᱴᱞ𐌳ଓꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ን𐌳ᱚᱞᱛተઝሃ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ዘ𐌳 ꤍଓ𐌳ᱤઝꤕ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ ᱴꤕንᱚሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ 𐌟ᱢᱞዘሃᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ꤍଓᱢዘᱩᱵ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ऊᱤ𐌓ᱚሃ𐌗ሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ꤕᱷꤕ ᱬᱛᱤᱛᱚሃᱵ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦꤕꤍተꤕᱞઝሃ ꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱦᱤᱵ𐌗ሃ ꤕऊ𐌳ᱤ ଓ ᱞᱛተ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ዘꤕଓᱢᱚᱢᱬሃᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓ 𐌲ᱞᱛऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተꤕऊꤕ ଓ ᱞᱛተ ꤍᱞ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተꤕऊꤕ ዘ𐌳 ઝᱤᱟઝ ઝᱢዘሃᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተᱟ ꤍᱛꤍ𐌳ᱤ ᱬዘꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ተꤕऊ𐌓 ᱦᱤᱵ𐌗ሃ ଓ ተሃ𐌳ᱤꤕተꤕ ઝᱤሃऊ𐌳 ꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ଓ ᱞᱛተ ଓ ሃᱤᱢ𐌍ዘᱛᱬ ተሃ𐌳ᱤꤕተꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ଓ ᱚሃᱬꤕ ተꤕऊ𐌓 ꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱬ𑁌ᱞᱢᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊꤕᱤᱛ𐌲ᱛ ᱚᱛᱬ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌳ᱬ𐌘ᱢተꤕ𐌳ተᱞ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱬሃንꤕ𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>]  ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ተᱵᱞᱩᱬᱟ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴ𐌳ᱞઝᱛଓઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌟ᱚ ଓᱛઝንን𐌳ᱤ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ᱞꤕᱤᱩꤍ𐌳𐌗 [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ተଓᱛꤕᱢ ᱬ𐌳ᱬᱟ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ᱚᱢଓ𐌳ዘꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴᱛᱚъꤕንᱚ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍ𐌳ᱬᱛᱤꤕተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱚሃᱦꤕଓᱛᱢ ઝ𐌳ऊᱢዘઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ተ𐌳ᱴᱛ𐌍ઝ𐌳ᱬᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱤꤕꤍዘᱛᱢ ᱛᱴሃᱦઝᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ઝᱤ𐌳ꤍꤍ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ 𐌳ሃᱚᱢተᱛᱞᱢᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ሃ𐌍ᱢተꤕᱤᱩꤍઝᱛᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱚꤕઝᱛዘ𐌳ተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍ𐌳ᱚᱢઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴ𐌳ᱞઝᱛଓઝᱢ ዘ𐌳 ଓተᱛᱞᱛᱬ 𑁌ተ𐌳𐌟ꤕ [<emoji document_id=5352887306590102199>♾</emoji>]", "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱤᱢ𐌘ተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊ𐌳ᱞ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ꤍተᱛᱢᱤ𐌳 ዘ𐌳 ᱚᱢઝᱛᱬ ን𐌳ᱴ𐌳ᱚꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱢተᱞᱢዘᱟ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ऊ𐌳ዘઝᱛᱬ𐌳ተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ᱴᱛᱤᱢԱꤕᱢꤍઝᱛ𐌲ᱛ ሃ𐌍𐌳ꤍተઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱛꤕዘዘᱛᱢ 𐌍𐌳ꤍተᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ଓᱛꤕዘઝᱛᱬ𐌳ተ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ઝ𐌳ઝ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ᱬꤕ𐌟 ᱞꤕऊꤕᱞ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ዘ𐌳 ꤍᱢᱤꤕ ଓᱛᱤᱢ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 𐌍ꤕᱞꤕን ᱚሃᱦሃ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ଓ ᱚሃᱦꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ሃ ઝ𐌳ዘ𐌳ଓᱟ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ꤕऊ𐌳ᱤ ተꤕऊ𐌓 ऊꤕንᱴᱞᱢᱞᱟଓዘᱛ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌳 ተᱟ ꤍଓᱛᱢᱬ 𐌓ንᱟઝᱛᱬ ᱬዘꤕ ଓ ઝᱛᱤᱛઝᱛᱤ𐌳 ऊᱢᱤ ઝ𐌳ઝ ଓ Աꤕᱞઝଓᱢ  [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ Աꤕᱞઝଓᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ሃ ᱴᱛꤍᱛᱤᱩꤍተଓ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱛꤍଓꤕ𐌟𐌳ᱤ 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ᱞଓ𐌳ᱤ 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱴᱛ ꤍሃተᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ ᱬᱛᱞ𐌳ᱤᱩዘᱛ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ 𐌍ተᱛ ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ᱚᱢઝ𐌳  [<emoji document_id=5352887306590102199>♾</emoji>]",

"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛᱬዘᱵ 𐌍ተᱛ ተଓᱛ𐌓 ᱬ𐌳ተᱩ ᱦᱤᱵ𐌗𐌳 ꤕऊ𐌳ዘ𐌳𐌓 ᱬዘꤕ ꤍᱛꤍ𐌳ᱤ𐌳 ઝ𐌳𐌟ᱚᱟᱢ ᱚꤕዘᱩ ଓ ᱦઝᱛᱤꤕ  [<emoji document_id=5352887306590102199>♾</emoji>]",
		"[<emoji document_id=5352887306590102199>♾</emoji>] ን𐌳ઝᱞሃተꤕᱤ ተ𐌓 ଓ 𐌗ሃꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ዘᱢዘ𐌳ᱞᱬ𐌳ተᱢଓዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟꤍተ𐌳ଓꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳 ꤍተꤕᱴꤕዘᱚᱢᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ን𐌳 ᱚꤕᱴᱤᱛᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓꤍᱴᱛᱬዘꤕᱤ ተ𐌓 𐌗ሃꤕᱬ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ዘ𐌳 ꤍᱢᱤꤕଓᱛᱤꤕ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ዘ𐌳 ተ𐌓 ᱞሃ𐌗ዘሃᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ን𐌳ꤕऊ𐌳ተ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ሃᱚᱛऊᱞᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱚ𐌳ᱞᱛ𐌟ዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳 ᱴᱞꤕ𐌟ዘꤕᱬሃ ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ᱴ𐌳ᱚ ଓ𐌳ᱚᱛᱢ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ሃऊꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱛ 𐌗ሃᱵ ተ𐌓 ଓᱛᱚꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ઝ𐌳𐌍𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱴꤕԱᱢ𐌘ᱢ𐌍ዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ઝ𐌳ᱢ𐌘ᱛଓ𐌳 ተ𐌓 ᱴ𐌳 ꤕऊ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱢᱤᱩዘ𐌳 ተᱞ𐌳𐌗𐌳ᱵ ተ𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ᱴ𐌳ᱚ ᱤꤍᱚ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ଓᱟᱴᱞ𐌳ଓ𐌳ᱚᱢᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱴ𐌳 ዘ𐌳ଓ𐌳𐌲ᱛᱚዘꤕᱬሃ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍઝᱛᱤᱩንઝ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ଓ ዘᱛንᱚᱞꤕ ተꤕ ꤍԱሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱬ𐌳ꤍꤍᱛଓ𐌳 ተ𐌓 𐌗ሃꤕᱬ ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ઝ𐌳ઝ 𐌍ꤕᱬᱴᱢᱛዘ ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱬᱢᱞዘ𐌳 ተ𐌓 𐌳ऊ𐌳ꤍԱ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ᱤꤕ𐌲𐌳ᱤᱩዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ઝ𐌳ઝ ᱚᱢ𐌲𐌲ꤕᱞ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] ઝ𐌳ઝ ઝᱛዘꤍᱛᱬᱛᱤᱩꤍઝ𐌳𐌓 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>]  ꤕऊሃ ተ𐌓 ઝ𐌳ઝ ଓᱞꤕᱬꤕዘዘሃᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
                 "[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ଓ ተꤕ ᱴሃተᱢᱦꤕተꤍଓᱛଓ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱛተᱤᱢ𐌍ዘ𐌳 ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ଓꤕᱞዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተꤕऊꤕ ଓ ᱞᱛተ ዘ𐌳ꤍᱞሃ 𐌗ሃꤕꤍᱛꤍᱢᱷꤕ ꤍᱤ𐌳ऊᱛዘꤕଓᱞᱛንዘᱛꤕ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ꤕऊ𐌳ᱤ ଓዘ𐌳ተሃᱞꤕ 𐌗ሃꤕᱚᱤᱢዘᱢተꤕᱤᱩዘ𐌳𐌓 ऊᱤ𐌓ᱚሃᱦᱢዘઝ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተ𐌓 ᱛተᱴꤕንᱚꤕᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱴᱢንᱚ𐌳ᱴёᱞઝ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 𐌓 𐌟ꤕ ተଓᱛᱵ ᱬ𐌳ᱬ𐌳ᱦሃ ଓ ᱞᱛተ ꤕऊ𐌳ᱤ ᱴᱛઝ𐌳 ተᱟ ᱬᱛᱢ 𐌓ᱢԱ𐌳 𐌗𐌳ଓ𐌳ᱤ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃᱢ ᱤᱛଓᱢ ꤍᱟዘᱛઝ ᱦᱤᱵ𐌗ᱢ ꤍተᱞ𐌳ዘዘᱛ𐌲ᱛ ꤍꤕᱬꤕᱢꤍተଓ𐌳 ᱛᱤᱢ𐌲ᱛ𐌘ᱞꤕዘᱛଓ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍ𐌳ꤍꤕᱦᱩ ઝ𐌳ઝ ꤍተ𐌳ᱞᱴꤕᱞ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ଓ ᱞᱛተ ተꤕऊ𐌓 ꤕऊ𐌳ᱤ ᱬᱞ𐌳ንᱛተ𐌳 ꤍꤍ𐌳ዘ𐌳𐌓 ተᱟ ᱛተꤍᱛꤍᱢ ተ𐌳ᱬ ᱦᱤᱵᱦꤕዘᱩઝ𐌳𐌓 ꤕऊሃዘ𐌓𐌍𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ᱬ𐌳ᱬ𐌳ዘ 𐌓 ተଓᱛᱵ ᱬ𐌳ተᱩ ᱴᱢንᱚ𐌳𐌲ᱛᱤᱛଓ𐌳𐌓 ተଓ𐌳ᱞᱩ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ऊᱤ𐌓 ऊሃᱚሃ ተ𐌓 ꤕऊሃ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ተᱟ ऊᱤ𐌓ተᱩ ᱦᱤᱵ𐌗𐌳 ꤕऊ𐌳ዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ઝᱤᱵઝଓᱛꤍᱞ𐌳ዘᱢᱷꤕ ꤍଓᱛꤕ ን𐌳ઝᱞᱛᱢ ᱬᱞ𐌳ንᱢዘᱢዘ𐌳 ꤕऊ𐌳ዘ𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ꤕऊሃ ተ𐌓 ዘ𐌳ꤍᱢᱤᱩዘ𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተꤕऊ𐌓 𐌳ዘዘᱢ𐌲ᱢᱤᱢᱞᱛଓ𐌳ᱤ ᱦᱤᱵ𐌗𐌳 ተꤕᱞᱴᱢᱤᱢଓ𐌳𐌓 ᱛተꤍᱛꤍᱢ 𐌲ᱞᱵ [<emoji document_id=5352887306590102199>♾</emoji>]",
"[<emoji document_id=5352887306590102199>♾</emoji>] ऊሃઝଓ𐌳ᱤᱩዘ𐌳 ꤍ𐌳ꤍꤕᱦᱩ [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] 𐌗ሃꤕᱬ ተꤕऊ𐌓 ተᱛᱞᱬᱛᱦᱢᱤ ᱦᱤᱵ𐌗𐌳 ꤕऊሃ𐌍𐌳𐌓 [<emoji document_id=5352887306590102199>♾</emoji>]", 
"[<emoji document_id=5352887306590102199>♾</emoji>] ꤍᱛꤍዘᱢ ንᱚꤕꤍᱩ 𐌗ሃꤕᱴᱤꤕተᱢᱷꤕ ꤍꤍ𐌳ዘᱛꤕ ꤕऊ𐌳ዘᱛꤕ 𐌗𐌳𐌗𐌳 [<emoji document_id=5352887306590102199>♾</emoji>]"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl8))
            await sleep(0.1)
            await sleep(time)

    async def банкайcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Бᥲнκᥲᥔ ɜᥲκ᧐нчᥙ᧘ ᥰ᧐ᴛρᥲɯᥙᴛь ᥴынκ᧐ʙ ᥴуκ <emoji document_id=5352655842212584578>🌜</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Бᥲнκᥲᥔ нᥲчᥲ᧘ ᥰ᧐ᴛρᥲɯᥙᴛь ᥴынκ᧐ʙ ᥴуκ <emoji document_id=5352655842212584578>🌜</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl9 = [" ᴋᴀᴋ ᴄᴇᴩɸᴇᴩ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴨᴩᴀʙиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀʙᴩᴇдиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уᴛиᴧиɜᴀʙᴀᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴀʙᴩᴇждᴀᴧ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀɯʍᴀᴩнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴦинᴀяᴄь ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴏнᴋᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇчᴇɯьᴄя ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦуᴧяᴇɯь ᴄ ʍᴀиʍ чᴧᴇнᴀʍ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴇɯьᴄя нᴀ ʍᴏй хуй хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩᴀʙᴀᴨᴀᴛᴇᴩнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ʍинуᴛᴀʍ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ ʙᴄᴇй ᴀᴄи ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀʙᴏᴧьнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ ᴋᴀнибᴀᴧ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴩᴇᴨᴇɯнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴏᴋᴩуᴦᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴧᴇɜ ʙ ᴛя хуйᴇʍ ᴇɜ ᴇɜ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чищу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴧуᴨᴀʙᴀᴛᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛячᴏɯ ᴀᴛ ʍᴀиᴦᴏ хуйя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴧᴀʍᴀᴧ ᴛя хуйᴇʍ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴩᴇɯуᴇɯьᴄя ᴄ ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙидᴇᴏ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀᴩᴀниᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴄᴛ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴩᴏʙи хуйᴇʍ ᴄʙᴇᴧ ᴛᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ʙиᴄнуɯᴋи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴋᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩᴇᴇɯьᴄя ʍᴀиʍ хуйᴇʍ ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уʍиᴩᴀя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀᴩᴀᴛᴧиʙᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴩᴀᴄᴨяᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩидиᴩʙᴇчᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧюхᴀʙᴀᴛᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦну ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" я ᴛя иɜᴇ ᴛᴀᴋᴛᴀ ʙыᴇᴨᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чиᴄᴛᴀᴛнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴏнчиᴧ ᴛᴇ ʙ ᴨуɜᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴨуᴨᴀʙину  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴋᴩᴇᴀᴛиʙнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя щиᴛᴀʙиᴛᴋу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴩуᴋи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛᴇ ᴀдᴇжду  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ ɜᴀ ᴨᴧᴀᴛу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴧᴀᴛнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жᴀхᴀйю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴋᴀᴩʍʍиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴩᴀᴄᴧᴀбᴏнᴇ иᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙᴇчᴇᴩᴀʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴩᴦᴀйю ᴛя хуйᴇʍ ɯᴏᴧᴀʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴄᴛуᴨиᴧ нᴀ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀᴄᴛичнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴀᴨиᴛыʙᴀᴇɯьᴄя ᴄᴨᴇᴩʍᴀй  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴧиᴧ ᴛя ᴄᴨᴇᴩʍᴀй  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴇɸᴧᴇᴋᴛᴏᴩнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨуᴄᴛиᴧ ʙ ᴛя ʍᴀчу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀняᴇɯ нᴀ ʍᴀйᴏʍ хуйᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴩᴀдуᴦᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴩᴀɜнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧюбя ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ нᴇ ᴩуɜᴦᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇжᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄидя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴏйя ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴧᴇᴛу ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴧᴀʙᴀйя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇɜдᴇя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇᴛя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" диᴋᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧюɯᴋᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍдᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴧᴇдуᴇɯь иɜᴇ ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴨᴀᴋᴧи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴧиᴩуйю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴋᴧи ᴛᴇ хуйᴇʍ ʙыᴩʙᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ду϶ᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴇɜуᴧьᴛᴀᴛнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бужу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя дуᴩу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀдᴇᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜʙᴇɜднᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ нᴀᴩядᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ɜᴀᴩᴇ ᴛя ᴇᴨу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴀ ʍᴀᴧᴀдᴏʍу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄю жиɜнь ᴄᴀᴄᴇɯ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨуᴛя дуᴩнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴩуᴋᴀʙицы ᴄцу ᴛᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя щᴇᴋᴀᴛᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜнᴇᴄ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴇᴨнуᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧяᴧяᴋᴀйя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛуɯу ᴛя ɯᴏᴧᴀʙу хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ бᴇндᴇᴩ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴛᴩиᴏᴛичнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴇɯьᴄя ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄуɯу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бью ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴩᴇднᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄиᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨиᴄᴋᴧиʙᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ буᴋʙᴀᴧьнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋᴩиᴨя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ничᴏ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ уᴦᴧу ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴀдᴀᴄᴛнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ чиᴋи чиᴋᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴀжу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋᴀᴧыбᴇᴧьнᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴩᴀᴛёᴩ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴩᴀдᴀиɯь ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋидᴀйю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя ʙᴀɯᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴩʙᴀᴧ ᴛя иɜᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɯᴧᴇᴨнуᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴋᴏɯнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄᴛᴩᴏчнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" цᴏʍᴋᴀᴇɯ ʍᴏй хуй хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ бᴇᴦу ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦуд ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴩᴀɜбᴏᴩчиʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍуᴛнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧья ᴄᴧᴇɜы ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄбиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴀдʙᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇᴄᴨᴏʍᴀщнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴏдинᴏчᴋу ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛᴇ ᴧяɯᴋи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя иɜᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇчᴇбнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋучᴀя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋучнᴀʙᴀᴛᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ нᴀдᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ɸᴏнᴀх ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴦᴀдᴏчнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɸуᴛбᴏᴧьнᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴦнᴏᴩиᴩуя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇᴧᴀчнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇɜ ᴇɜ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уʍиᴩᴀᴇɯь ужᴇ хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴋуᴩʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴏᴧᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ бᴧᴀᴛу ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋуᴧя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛʙᴀйя ʍᴀʍᴋᴀ ᴄᴀᴄᴀᴧᴀ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴩᴛᴏнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙяᴋᴀᴇɯь ʍᴀиʍ хуйᴇʍ ᴇɜ ᴇɜ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀᴩиɯьᴄя нᴀ ʍᴀйᴏʍ хуйᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴩʙᴀᴧ ᴛя хуйᴇʍ ɯᴏᴧᴀʙиᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" щᴇᴋи ᴛᴇ хуйᴇʍ ᴩʙу иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ ᴛуᴨᴀᴩыᴧᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴧᴇᴛу ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴩᴀʙᴇᴧьнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуɯу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴏᴧᴏᴨнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴄᴀнᴛиᴩуя ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋинᴏ ᴛя хуйᴇʍ ʙᴀдиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴀ ɯᴛᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴦᴀᴩᴇ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍуᴩчиɯь ʙ ʍᴏй хуй ᴇɜ ᴇɜ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ʍᴀɯинᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ʙᴀᴦᴏнᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀ ᴨᴀᴛᴇᴩи ᴨуᴧьᴄᴀ ᴛя ᴇᴨу ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴇᴨᴀᴧᴏ ᴛᴇ ᴄцу дуᴩᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀ ʙᴄᴇ щᴇᴧи бᴇᴩᴇɯ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋᴀнчᴇ ᴛᴏнᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴧᴇйᴇᴩнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴛя ᴄʙᴏй хуй ᴨᴀᴄᴛᴀʙᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋуᴧ ᴛя ᴇᴨу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀяᴄницу ᴛᴇ хуйᴇʍ дᴩючу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋᴀᴋ ᴇбᴀнуᴛый </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴦᴀ ᴛᴇ хуйᴇʍ ᴄᴧᴀʍᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴄᴛуᴧᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴨᴀ дᴇᴄнᴀʍ ᴛᴇ ʙᴀжу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄуᴛᴋᴀʍи ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴏᴧᴀʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ ᴛᴇᴧᴇɸᴏн ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨᴀᴧ ᴛя ʙ ᴛᴇᴧᴇɸᴀнии  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴏᴄᴛᴀ ᴛᴀᴋ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏд ʙᴄё ʙ ᴀᴋᴩуᴦᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴇᴄду ᴛя ᴇᴨу ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ ᴦуᴄᴇʙᴄᴋᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀʍᴋу ᴛʙᴀйю хуйᴇʍ ᴇᴨу ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋᴀᴋ и ᴛʙᴀйя ʍᴀᴛь  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴇчнᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴇᴋᴧиʙᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴄᴀᴄᴇɯ нᴇ ᴏч  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀчу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ɜᴇᴧᴇнᴀʍу ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄʙᴀиʍ хуйᴇʍ ʙ ᴛя ᴋᴏᴩни ᴨуᴄᴛиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩᴀᴄниᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀɜᴏᴧю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴧᴀʙᴀᴛь учиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨиɜжу ᴛя чᴧᴇнᴀʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя жᴇниᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ бᴩᴀᴛᴄᴋᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ бᴇᴄᴨᴇчнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ нᴀ хуйю  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀяᴄь ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴀᴦᴏнᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴩᴏᴛ ᴛя ᴇᴨу иɜᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴩᴇди ɜʙᴇɜд ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏхᴀᴛᴧиʙᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴨᴀ ᴛᴇ ʍᴀɜжу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴛᴩᴏнᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩыᴦᴀᴇɯь ʙ ʍᴏй хуй ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀбиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ дᴇᴩᴇʙᴇнᴄᴋᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя удᴀчᴇᴩиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋуᴋᴀᴩᴇᴋᴀᴇɯь ᴄ ʍᴀиʍ хуйᴇʍ хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ хᴀчу ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уᴄᴛᴀᴧᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴀчᴇᴧᴀ ᴛᴇ ᴄцу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜʙᴀᴧиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʍᴀйᴏʍ хуйᴇ ᴄᴀбиᴩᴀᴇɯьᴄя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇᴦᴀᴇɯь ᴄ ʍᴀиʍ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ ʍуᴄуᴧьʍᴀнᴇн ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴛᴩᴀᴄᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴧыʙя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жуᴇɯь ʍᴀйю ᴄᴨᴇᴩʍу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴏᴄиɯь ʍᴏй хуй ᴋᴀᴋ уᴦᴀᴩᴇᴧый  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜʙиняᴄь ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦния ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴋуᴩиʙᴀᴇɯь ʍᴏй хуй ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏᴩнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇʙᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀбᴩиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋнижнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴀ϶ʍᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴄᴛуᴨᴀя ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴦᴩᴀᴇɯьᴄя ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴋ ᴀᴧᴇнь ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ ʙᴇᴄᴋи ᴀбᴀᴄцᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴩᴀɜʙᴇᴩᴛᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴀʙчᴀᴩнᴇ ᴄᴀᴄᴇɯ ʍнᴇ дуᴩᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨиɜдиɯьᴄя ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ ᴋᴏнᴄᴋᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴩᴇйᴋᴀᴇɯьᴄя ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙнуᴛᴩи ᴄᴇбя ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇɜжу ᴨᴀ ᴛᴇ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇчу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴀиᴦᴏ хуйя ᴨьᴇɯь ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴄᴇдᴧᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴀᴩʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ʙ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋᴀᴧьжу ᴨᴀ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴀиʍ хуйᴇʍ ʍуᴛиɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩыɜᴇɯь ʍнᴇ хуй </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жуйᴇɯь ʍᴏй хуй ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩᴀʍᴀᴛнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴛᴩу ᴛя хуйᴇʍ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀ ᴄих ᴨᴏᴩ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя иɜᴇ ɯᴏᴧᴀʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴋᴀᴩᴀчᴋᴀх ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя нᴇжнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀд ᴨᴀᴩᴛᴀй ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ чᴇᴩнᴀʍу ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴩыᴦᴀᴧ нᴀ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴛᴇᴧᴇʙидᴇньᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏчᴋу ᴛᴇ хуйᴇʍ ʙыбᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴇᴄду ᴛʙᴀйю нᴏᴦᴏй ʙᴄᴛᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄнᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴋуᴩʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴀᴧᴋнуᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ɯᴧюхɜу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄʙᴏй хуй ʙ ᴛя ɜᴀᴧᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴦᴧᴏᴛᴋу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄɯиб ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴏй хуй ᴨᴀ ᴛᴇ ᴋᴀᴛᴀᴧᴄя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛыᴄячу ᴩᴀɜ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя дуᴩу хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хᴀᴩᴀɯᴏ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴋᴩуᴨнᴀʍу ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴏᴩᴀʙᴧиʙᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴏдᴀᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴏчнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴦᴩуᴄᴛи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴧᴀжиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀдᴏᴩнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴨᴇчᴇнь ᴇɜ ᴇɜ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴏᴧᴀʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙьᴇбᴀᴧ ʙ ᴛя ᴄʙᴏй хуй  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ чᴏᴛᴋᴀᴄᴛᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴇᴋ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀд ᴀдᴇяᴧᴀʍ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴨᴏ ᴛᴇ ᴨᴩᴀᴋᴀᴛиᴧᴄя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙᴀᴋɜᴀᴧᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴀᴨуᴄᴛᴀɯиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴀᴛᴩᴀʙиᴧ ᴋудᴀᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ниɜᴋᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴏщнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩуᴄᴛнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ жᴇᴄᴋᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦуʍᴀнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴛᴇᴩичнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ʍᴀᴛᴋу ᴛя ᴇᴨу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀд ёᴧᴋᴀй ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴇᴩɜᴀйю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴨᴀᴧянᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄʙᴏй хуй ʙ ᴛя ʙᴄᴛᴀʙᴇᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴦᴧᴀнды ʙыᴇᴨᴀᴧ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴏ ᴨᴀᴛᴇᴩи ᴨуᴧьᴄᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɯᴋʙᴀᴩнуᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя ʙ ɯᴀᴩᴀᴦᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴏɜᴧᴇ ɯᴋᴏᴧы ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴩᴏᴛ ᴛя ᴇᴨу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀд ʙᴀдᴀᴨᴀдᴀʍ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋуʙᴇᴛᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧюхᴀʙᴀᴛᴀя ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨᴀᴧ ᴛя ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴇᴩяᴇɯьᴄя ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴏнчиᴧ ᴛᴇ ʙ ᴩᴏᴛ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴄᴧᴇᴛую  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ʙ ᴛя ᴄᴧᴇᴛую  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴄᴀᴄᴀᴧᴀ ʍнᴇ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя ɯᴧюɯᴋу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴄᴇнᴀʙᴀᴧᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴛᴀйю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛʙᴏй ᴩᴏᴛ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ иɜᴇ хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄи ʍнᴇ ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴩᴀбᴋᴀю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ʙᴇᴩᴛиᴋᴀᴧᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴦᴧᴀнды </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴏиɯьᴄя ᴄ ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя нᴀ ᴛᴩᴀᴛуᴀᴩᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨнуᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴩᴀчиᴧ ʙ ᴛя ᴄʙᴏй хуй  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ нищᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя ᴨиɜжᴇнную  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ɜᴏнᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ʙ ᴛя ɯᴧюхɜу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ɯуᴛᴧиʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨᴀᴧ ᴛя ʙ ᴨᴇᴄду ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩичᴀ ʍнᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴩᴇхʙᴀᴛиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴏиʍ хуйᴇʍ ᴄᴀᴄᴇɯьᴄя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ʍᴀᴛᴩᴏɯу иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏᴛдᴀᴇɯьᴄя ʍᴀиʍу хуйю  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨᴀɯу ᴛя хуйᴇʍ иɜᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏᴩиᴦинᴀᴧьнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴏᴄциᴩᴏʙᴀᴧ ᴛя ɯᴏᴧᴀʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏᴛ нᴇчᴇᴦᴏ дᴇᴧᴀᴛь ʍнᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴀиᴦᴩᴀнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴄᴀᴩᴀᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄиᴩуᴇɯ ᴨᴏᴛнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧучᴀйнᴀ ʙыᴇᴨᴀᴧ ᴛя ᴋуᴩʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴩындᴀ ᴄцу ʙ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧухᴀ ᴄᴀᴄᴇɯ ʍнᴇ чᴇᴩᴛʙᴏᴄᴋᴇ ᴦуд  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴨᴀ чᴀᴄᴀʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄиᴩуй ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏщуᴛиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нуᴧᴇʙᴋᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴋᴧᴇиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴧᴇйю ᴛя хуйᴇʍ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴏᴦичнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦдᴇ уᴦᴏднᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ɯᴏᴧᴀʙᴧиʙᴀя ᴋуᴩʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏбᴏᴄцᴀᴧ ᴛя иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋᴀᴋ ᴀбычнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴩᴇᴇᴨᴀᴧ ᴛя иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄᴀᴄыʙᴀᴇɯь ʍнᴇ иɜᴇ ᴛᴀᴋᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴨиɯь ᴄ ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴩᴇʍᴀᴇɯь ᴄ ʍᴀиʍ хуйᴇʍ ᴇɜ ᴇɜ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴇᴨᴀᴧьниᴋ ᴛᴇ ᴄцу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴧюбиʍᴏʍ ʍᴇᴄᴛᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛухнᴇɯ ɯᴏᴧᴀʙᴀ ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴀдᴩᴇᴄу ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ щи  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴦᴧᴀɜ ᴛᴇ нᴀᴄцᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ дʙᴀ ᴦᴧᴀɜᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ʙ ᴛиɯинᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜᴀбᴩᴀᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ нуждᴇ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴄᴀдᴇᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴀᴇɯь нᴀ ʍᴏй хуй ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ быᴄᴛᴩᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɜᴀʙᴇᴧ ɯᴏᴧᴀʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀдиɯьᴄя нᴀ ʍᴏй хуй иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀняю ᴨᴀ ᴛᴇбᴇ ᴄʙᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдняᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴇɯ ᴄᴧᴇʙнᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴧуɯᴀ ᴀбᴀᴄцᴀᴧ ᴛя ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴀиʍ хуйᴇʍ ʙ ᴛиɯᴇнᴇ ᴄᴨиɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦубᴀʍи ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жʍу ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ ᴩубᴧь ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ ᴩубᴧь ᴛя ᴇᴨу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴀᴩʙᴀᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄиᴦнᴀᴧю ᴛᴇ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴨуᴄᴛиᴧ ᴛя иɜᴇ ɯᴏᴧᴀʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ дᴀ ᴄᴇй ᴨᴀᴩы </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя дᴀ ᴄих ᴨᴏᴩ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ хуй ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ бᴀᴧдᴇ ᴛᴇ хуйᴇʍ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛуᴨᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴨёхᴀйю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯуᴄᴛᴩᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨᴀᴧ ᴛя ужᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ужᴇ ᴄцу ʙ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" убиᴧ ᴛя хуйᴇʍ ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴧюᴛᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ϶ᴋᴄᴛᴩᴇнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ɜʙучнᴀ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴩᴏᴛ ᴛя иᴨᴀᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇчнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴇᴨᴀᴧ ᴛя ᴋуᴩʙу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ дᴀᴄᴛᴀᴛᴀчнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя ɯᴏᴧᴀʙную  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ дᴀᴧи ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜнᴇᴄ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴋᴩыᴛᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ ɯᴏᴧᴀʙнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴛᴀᴩичᴇᴄᴋи ᴇᴨᴀᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜиᴦ ɜᴀᴦᴀʍ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴨᴀхᴀᴩᴀнᴀх ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ ᴧюбя ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴨᴧᴇᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜнᴀя ʍнᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ᴀбидᴀй ʍнᴇ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴇᴋᴧᴀʍнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ нᴀᴄᴛᴀящᴇʍу ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄхʙᴀᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴦнᴀᴧ ᴛя хуйᴇʍ ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴀᴛɜыʙчиʙᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴄᴛᴩᴀᴨᴛиʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴄᴀю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨнуᴧ ᴛя хуйᴇʍ ᴋуᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴦᴀᴩящᴀя ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀнᴛинᴏʍнᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ᴛы ᴄᴀᴄнуᴧᴀ ʍнᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜʍᴇниᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ᴄᴀᴄᴇɯ ʍнᴇ ɯᴏᴧᴀʙᴀннᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋуᴩʙᴀ ᴄцᴀнᴀя ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя нᴀᴄиᴧᴀʙᴀᴧ ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴏᴩʍ ᴄᴀᴄᴇɯ хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя хуйᴇʍ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴋуᴩᴀ ᴄᴧᴇᴧ ᴛя иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ ɯᴏᴧᴀʙᴀ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜʙᴇᴧ ᴛя ᴄʙᴀиʍ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛуᴨиᴛцᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴀʙи ᴄᴀнину ʙ ᴧицᴏ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄущᴀя ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀʍᴋу ᴛʙᴀйю ᴇᴨу иɜᴇ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴩɜᴋᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴏднᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴧᴀʙнᴇᴇ ʙᴄᴇх ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴀдᴄᴏᴄᴋᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛʙᴀйᴇй ʍᴀᴛᴇᴩи ʙ ᴨᴇᴄду ᴄцу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴦᴀᴩиɯ чᴏᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇᴛᴋᴀ ᴄцу ʙ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴛᴩяᴄᴀющᴇ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧюɯᴋᴀ ᴀбᴀᴧдᴇнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇʙᴀᴇɯьᴄя дуᴩᴀ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴨᴧяʍи ʙ ᴛя ᴋᴀнчᴀю </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбᴧю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ʙᴄᴀᴄыʙᴀᴇɯь  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ ᴄᴧᴇᴛᴀя ᴀᴩу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇʙᴀᴇɯьᴄя ɯᴏᴧᴀʙиᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀчᴋᴏ ᴛᴇ хуйᴇʍ ᴨᴀᴩʙᴀᴧ ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀбиᴧ ᴛя хуйᴇʍ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴏᴄᴋᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴋᴩуᴛᴇᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуй ᴄᴀᴄᴇɯ иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋудᴀхчᴇɯь ɯᴏᴧᴀʙᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя ᴛуᴨиᴛцу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴋᴩыᴧ ᴛя ɯᴏᴧᴀʙу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴇᴛуɯᴧиʙᴀя хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴏᴄᴋᴀ ᴦᴀᴩиɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" убᴏᴦᴀя ᴄᴀᴄᴇɯ жᴇ ʍнᴇ хᴇхᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя хуйᴇʍ дуᴩу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴩнᴀя ᴄᴀᴄᴇɯ ᴦᴀᴩя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ ᴩуɜᴦᴀя ɯᴏᴧᴀʙᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴀᴄᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴋᴀʙᴋᴀɜᴄᴋи ᴛя ᴇбу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴏᴄᴋᴀ ᴄᴧᴇᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴏᴧᴀʙᴀ ʙыᴇᴨᴀᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ дуᴩнᴀ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀɜᴀᴩᴛнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀчᴋᴏ ᴛᴇ ᴨᴀᴩʙᴀᴧ хуйᴇʍ ᴧᴇхᴋᴀʙᴀᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴩᴀ ᴄᴀᴄᴇɯ жᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" цᴇᴧуᴇɯьᴄя ᴄ ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɯᴀчу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴄᴀᴄыʙᴀᴇɯь нᴀᴩʍᴀᴛиʙнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ɯᴧюхɜу ᴦᴀᴩящᴇю </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇхᴋᴏ ʙᴄᴀᴄыʙᴀᴇɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇʙᴀᴇɯ ɯᴏᴧᴀʙᴀ ᴄᴋᴩиню  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴇнᴀᴩʍᴀᴧьнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴏᴄᴀʙᴧиʙᴀя ᴄцу ʙ ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴩʍᴀнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴋинуᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩыᴦᴀᴇɯь ʙ ʍᴏй хуй ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴇᴨᴀᴧ ᴛя дуᴩнуɯᴋу иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀхᴀя ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴨᴀᴦᴏдᴇ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛʙᴀих ᴩᴀдных </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуᴇᴄᴀᴄᴋᴀ ᴦᴀᴩиɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбиɯ ᴄᴧᴇᴛᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄᴛᴀянᴀ ᴄᴀᴄᴇɯ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴋᴀᴩᴇɯᴋи </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩиᴋᴀя ᴄᴀᴄᴇɯ ʍнᴇ ɯᴀбᴏᴧдᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴏᴄᴋᴀ ᴇᴨу ᴛя ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄуʍᴀᴄɯᴇдɯᴇ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴇᴨиᴄь ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴨиᴄᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жиɜнᴇнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴨᴏᴩнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴨᴀ ᴋᴩуᴦу идᴇɯ иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя быᴄᴛᴩᴀ чᴏᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄᴀᴄыʙᴀᴇɯь иɜᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴨᴀᴩиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ нᴀᴄᴀᴦᴧᴏᴛᴋу ᴇᴨᴀᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ ᴦᴀᴩи ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ʙᴄᴀᴄыʙᴀᴇɯь бᴀʍбящᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбиɯ ᴄᴧᴇᴛᴀя иɜᴇ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ чᴏᴛᴀ ɯᴏᴧᴀʙнᴀя дуᴩᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ бᴀʍби ɯᴧюхɜᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋᴩуᴛᴇйɯнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛᴇ ᴇᴨᴀᴧᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя ᴧᴇхᴋᴏ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʍинᴇᴛ ᴛя ᴩᴀɜʙᴇᴧ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄнуᴧᴀ ʍнᴇ ᴧᴇхᴋᴏ ʍдᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴇ хᴀᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ᴧᴇʙᴀᴇɯь ᴦᴀᴩящᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ ᴀᴨᴧᴀᴛу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴋᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩяʍ щᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴋᴛᴇᴩᴄᴋᴇ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇɜ ᴇɜ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴏᴧᴀʙᴀ ᴄᴧᴇʙᴀᴇɯᴄя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋуᴩʙᴀ иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ хуᴇᴄᴀᴄᴋᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уʙᴀжᴀющᴇ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дыᴩяʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ɜᴀʍᴇчᴀᴛᴇᴧьнᴀ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀюᴋᴀю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴨиᴛыʙᴀᴇɯь ʍᴏю ᴄᴨᴇᴩʍу  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴀᴇᴨᴀᴧ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴏй хуй ᴛᴀʍиɯ ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя ᴧᴇхᴋᴏ ɯᴏᴧᴀʙнᴀя ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋᴀɜᴀᴩʍᴇ ᴄᴀᴄᴀᴧᴀ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩинцᴇᴨиᴀᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ бᴀʍби ᴋуᴩʙиʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨᴀᴧ ᴛᴇᴨя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙᴄᴛᴩᴇчᴇ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ʙ ᴛя ᴦᴀᴩящᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ иɜᴇ ᴄᴧᴇʙнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя ᴋᴩᴀᴄиʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀɯᴇᴧ ʙ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴇᴛᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴇᴩᴇбиɯь ʍᴏй хуй ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀнчᴀю ᴛᴇ ʙ ᴦᴏᴩᴧᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дыʍиɯь ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇᴩᴇɯ ʍᴏй хуй ɯᴏᴧᴀʙнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" я ᴛя ᴇᴨу ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄʍᴇяᴄь ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴩᴀɜᴧᴀʍиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя бᴇᴄᴨᴧᴀᴛнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇдᴏʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨиɜдᴇᴧ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛы ᴄᴀᴄᴇɯ ʍнᴇ хуй чᴏᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀᴄᴋᴀю ᴛя хуйᴇʍ ɯᴀбᴏᴧду </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴋᴀнɸᴇᴛнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀᴧбиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴇᴩᴇщᴀ ʍнᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴦᴀᴩᴀнᴛии ᴇᴨу ᴛячᴏɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀнцую ᴄʙᴀиʍ хуйᴇʍ нᴀ ᴛᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴀиʍ хуйᴇʍ бᴇᴦᴀᴇɯь ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴩᴇʍяᴄь ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴄᴛᴀᴧᴇ ᴛя ᴇᴨᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴀйᴄ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɜᴀщиᴛиᴧ иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴋᴀᴛᴀᴧᴄя нᴀ ᴛᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ɯᴀᴧᴀʙᴀ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇᴩᴇᴀᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴄᴧᴇᴧ ᴛя ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ нᴇ нᴀ ɯуᴛᴋу ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя ᴧᴇхᴋᴏ ᴋуᴩʙиʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴦᴀднᴀ ʍнᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴋудᴩи </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙыᴦᴀдᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴀᴩᴀчнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩᴀᴄнᴀʙᴀᴛᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴦубы </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀʙᴀᴩᴧиʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴨᴀ ʍᴏдᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ɜубы </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" я ᴛя ᴇᴨу ɯᴏᴧᴀʙᴀ хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴨᴩиᴋᴏᴧьнᴀ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩи дᴀждᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄняᴧ ᴛя ɯᴏᴧᴀʙу ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀжу ᴨᴀ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴋᴩᴇʍᴧᴇ иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ʙыᴩʙᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀниᴨуᴧиᴩуя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴋᴀᴩᴀчᴋᴀх ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴀᴛиʙнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбиɯ дуᴩнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴋᴀᴧᴀчу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴧᴀʙᴀᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уᴧᴀбыяᴄь ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ʙыᴋᴩуᴛᴇᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴋᴀнцᴇᴩяᴧии ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя уᴦᴀᴩнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя бᴇɜ ᴨᴩичины </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дуᴩнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ɯᴀбᴏᴧдᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя ɯᴧюхᴀᴛᴀʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ ᴦᴀᴩи дуᴩᴀʙᴧиʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋуᴩᴀʍ нᴀ ᴄʍᴇх </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʍᴀиʍ хуйᴇʍ ᴦуᴧяᴇɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴇᴄᴛиᴋᴩᴀᴛнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя ʍᴀᴄᴧᴀʙᴀᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ᴛᴇ ʙ ᴧᴏб ɯᴋуᴩᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" цᴏʍᴀᴇɯь ʍᴏй хуй дуᴩнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ бᴇᴧᴀʍ ɸᴏнᴇ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴩᴀɜᴩᴇɯᴇния ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ ᴨᴀ ʍᴏᴩдᴇ иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" я ᴛя ᴀбᴀᴄцᴀᴧ и ᴄᴧᴇᴧ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дыʍя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴄᴧᴀʙу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя ʍудᴩᴇнᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩᴀᴄᴀʙᴧиʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴏй хуй бᴇᴩᴇɯь ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨьᴇɯь ʍᴀйю ᴄᴨᴇᴩʍу ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴋᴛиʙнᴀ ᴄᴀᴄиᴩуᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴋᴩуᴛᴏʍу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍуᴧьᴛидиᴧьнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ ʙ ᴧицᴏ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбᴇɯ ɯᴧюхɜᴀʙᴀᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀʙᴀᴧиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧюбиʍᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хᴏдиɯь ᴄ ʍᴀиʍ хуйᴇʍ дуᴩнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍуᴛуɜжу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ уɯи ᴨᴀᴩʙᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴇᴄду ᴛʙᴀйю хуйᴇʍ ɜᴀɯᴇᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ʙ ᴦᴩудину </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜуʍнᴀʙᴀᴛᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуй ʙ ᴛя ʙᴄунуᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇᴩнᴀʙᴀᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴋᴀя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴨᴀняᴛияʍ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄцу ʙ ᴛя ᴄᴧᴇᴛᴀя дуᴩᴀʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴩᴀидициᴏнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩᴏʍᴋᴀ ᴛя ᴇᴨу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыʍᴀɜᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ дуᴩᴀʙᴧиʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ɯᴀбᴏᴧдᴀʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴩᴇцᴇᴨᴛу ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴀᴛьᴇбᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩиɯ ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴄᴧᴇᴛᴀʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴩᴀᴄɯиб иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴋᴀ ᴄᴀᴄиᴩуᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чуᴛᴋᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄᴛуᴨиᴧ нᴀ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ нᴇ дуʍᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴀʍᴀᴧ ᴛᴇ хуйᴇʍ ᴧицᴏ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍучᴀяᴄь ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀ ᴨᴀᴩы ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴩᴇᴧяᴧ ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя ʙхᴀжу ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴦᴧубᴀᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴧюхɜᴀ ʙыʍᴀᴛᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍᴀᴧᴀдᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя уᴇᴨᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴋᴩыᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ нᴏʙᴀй ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ʙᴇᴄᴇᴧᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇхᴋᴀᴛᴧиʙᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴋᴩᴀʙᴇнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴀнᴛᴀжиᴩую ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴋуᴩʙиʙᴀя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɜᴀчʍᴀᴩиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨинᴀᴧ ᴛя хуйᴇʍ ʙ ᴨᴇᴄду </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ хуй бᴇɜуʍнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴩу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄчᴀᴄᴛᴧиʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ущᴇʍиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇчу ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя иɜʙᴇᴧ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧичнᴀ ʍнᴇ ᴛᴏᴋᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɸᴀнᴛᴀɜиᴩуя ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀбᴀᴩᴏᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴧᴀᴄᴋᴀᴧ ᴛя хуйᴇʍ ɯᴏᴧᴀʙу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀᴧɯᴇбнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴄᴋинуᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴛᴩяᴄ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴩя ᴄᴀᴄᴇɯ ʍнᴇ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴨᴩичудᴧиʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍяᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜᴀчᴀᴩᴏʙᴀнᴀя ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыбᴩᴀнᴀ ᴇᴨу ᴛя  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴇᴩᴇɜ нихᴀчу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴨᴀнᴀᴛияʍ ᴛя хуᴇʍ иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴦᴀᴩᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴄᴨᴩᴏᴄᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чуʙᴄᴛʙуя ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбижᴇнᴀя я ᴛя иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴀбᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜыᴋᴀю ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧюбиᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴦᴀняю ʙᴇᴄдᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯуᴛᴧиʙᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴨᴏᴧьɜую ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиʙᴇᴧ ᴛя ʙ чуʙᴄᴛʙᴀ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жиɜнᴇнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ʙᴇᴩᴀй ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇбᴀᴧᴀ ᴛᴇ ᴨᴀᴛуɯиᴧ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиᴛянуᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜʍиниᴩᴏʙᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀдуяᴄь ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀᴄхиᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴩᴀщᴀюᴄь ᴋ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" буᴋᴇᴛнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀᴧᴇɜнᴇнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɜᴀɸᴋʙᴀᴩиᴧ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴀᴧᴀʙиᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ дᴀʍу ɯᴀбᴏᴧдᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩящᴀя ᴋуᴩʙᴀ ᴄцу ʙ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя дᴀᴨᴏᴧниᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ хᴀᴛᴇния ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴩᴇᴋᴧючиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩᴇбу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴛᴀᴨиᴧ ᴛя хуйᴇʍ дуᴩную </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбиᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ ᴦᴀᴩящᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ʍᴀᴄᴛи ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ϶ʍᴏций ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴋᴀɜиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀйю ᴄᴨᴇᴩʍу ᴄᴀбиᴩᴀᴇɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жᴀᴧᴇю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴇᴄду ᴛя ᴨыᴩнуᴧ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ хᴀбᴀᴛᴏᴋ ᴛя хуйᴇʍ дᴇᴩжу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴛᴀᴄᴋуɯᴋᴀ хуйᴇʍ ᴛя иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ʙ ʍᴏᴩᴦᴇ ʍᴇᴩᴛʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴀᴨыᴩиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄиʍᴨᴀᴛичнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴛᴩᴏйнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴏчᴇᴩᴇди ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴄᴨᴀᴋᴏйᴄᴛʙии ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴨᴩиʍᴇᴛы ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴇᴨу ᴨᴀᴄᴛᴀящᴇʍу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴄцᴀᴧ ᴛᴇ ʙ нᴇбᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀйю ᴛᴇ ᴄʙᴏй хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀбᴏᴛᴀйю нᴀ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀ ᴄᴨᴀɜʍᴀʍ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ цᴇни ɜᴏᴧᴏᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ бᴀᴧьɯᴏʍу ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴄᴛᴀʙᴇᴧ нᴀ ᴛя хуй ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴛуᴩᴀᴧьнᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇᴨᴀᴄᴇдᴧиʙᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀнчᴀю ᴛᴇ ᴨᴀд яɜыᴋ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴋᴩуᴛᴇйɯнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴧᴇхчиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" униᴛᴀᴩнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋᴧᴀниᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴩхᴀᴛнᴀя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴏнчиᴧ ᴛᴇ ʙ ᴨᴀᴋᴧᴇ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиᴋᴀᴄнуᴧᴄя ᴋ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀ ᴄᴇᴋунды ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴩᴇᴋᴀᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍнᴇɯьᴄя ᴀб ʍᴏй хуй </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиʍᴇᴩнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴇᴄду ᴛᴇ дᴇᴩнуᴧ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀʍᴀнᴀ ᴄᴀᴄᴇɯ ɯᴏᴧᴀʙнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ᴄᴀᴄᴇɯ дуᴩнᴀя хихи </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀчʍᴀᴩиʙᴀᴧ ᴛя хуйᴇʍ иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ɜᴀᴦᴄᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ʙины ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴀʙдиʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀᴧᴇᴋᴀʙᴀᴛᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴋуᴩᴄу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄᴇᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ бᴀɯᴋу ᴛᴇ ᴄцу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀᴩʍᴧю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя ᴀᴛ чиᴄᴛᴀᴦᴀ ᴄᴇᴩдцᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇ ᴨᴩᴏᴄᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴨуᴄᴛиᴧ ᴛя дᴀ ɯиᴩинᴋи </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀд щᴇᴋу ᴛя хуйᴇʍ иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙᴇчᴇᴩинᴋᴇ ᴄᴀᴄᴇɯ ʍнᴇ ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" я ᴛя ʙᴀбщᴇ иɜᴇ ᴛᴀᴋᴛᴀ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀɜдᴩᴀʙиᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋᴀчнуᴧ ᴨᴀ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄячᴇᴄᴋи ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴄᴀᴄᴧᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀᴧᴋᴀю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴋᴩᴇнᴇ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄʙᴇᴛиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴀᴄцᴀᴧ ᴛя ᴩᴀдную </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴦᴧᴀɜᴀх ʍᴀих ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴀᴛнᴏɯᴇний ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴀᴨᴏʍниᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋуʍᴀᴩю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ уᴛᴇᴄᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ʙᴏᴧнᴇ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ ᴋᴩуᴛᴏʙᴀᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩиᴧ ᴛя хуйᴇʍ ʙыᴩᴀщу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨуᴄᴛиᴧ ᴛя хуйᴇʍ ᴋᴩуᴦᴀʙᴀᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя ᴄᴀᴄᴇɯ ʍнᴇ ʙ ᴄᴛужᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴛʍиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴧ ᴛя нᴀ ᴄʙᴏй хуй </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ дᴇᴧᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя ᴧᴇхᴋᴏʙᴀᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴩᴀᴄᴛᴀянии ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨуᴄᴋᴀю ᴛя хуйᴇʍ быᴄᴛᴩᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴀᴄʙᴀбᴀдиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴩᴀднᴏʍу ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀнчᴀю ᴛᴇ ʙ ᴦᴀᴩᴧᴀʙину </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя уᴧᴀʍᴀᴧ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙяᴋᴀя ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴨᴏᴧьɜую ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴀᴩячᴏ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴋуᴩᴀʙᴀя ᴄᴧᴇᴧ ᴛя иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴇᴩɜᴀю ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜᴀчᴀᴩᴏʙᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀ ᴨᴇᴄдᴇ ᴛʙᴀйᴇй хуйᴇʍ ʙᴀжу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя дᴩᴇᴄᴇᴩую ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀɜᴏᴩнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴨᴏ ᴋᴩᴀйнᴇй ʍᴇᴩᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴀю ᴛя ᴄʙᴀиʍ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бужу ᴛя хуйᴇʍ ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ ᴨᴀʙᴀду ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏдʙᴇᴩᴦᴀю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиᴏᴩиᴛᴇᴛнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" быʙᴀᴧ ʙ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴏᴩдᴀ ᴄᴀᴄᴇɯ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴇᴩдᴇчнᴀ ᴄᴀᴄᴇɯ ɯᴧюхɜᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя ʙᴄᴛᴩяᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜьᴇбᴀᴧ ᴛя хуйᴇʍ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀиᴨᴀᴧ ᴛя ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩиᴦᴩᴇᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀнчᴀю ᴛᴇ ʙ щи </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀнᴀᴨᴏᴧьнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴏᴧᴀʙнᴀя хуйᴇʍ ᴛя дᴀᴄᴛᴀᴧ ужᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя ʙбиᴧᴄя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇʙнᴀя ᴦᴀᴩиɯ нᴀ ʍᴇня иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ бᴏᴧьнᴀ ᴄдᴇᴧᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴄᴏчнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩучу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴨиᴩхᴀᴇɯьᴄя ʍᴀиʍ хуйᴇʍ ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴀʙнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴏᴄᴧиʙᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀдуʍᴀчнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀʍбящᴀя ᴄцу ᴛᴇ ʙ ᴧицᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀйᴏнᴇɜнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴛᴇᴩ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜʙᴇᴩᴛᴇᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴨуᴛᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ нужнᴀʍ ʍᴀʍᴇнᴛᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴨᴩᴀʙиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄᴛиᴩᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇжᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴩᴀди ᴨᴩиᴋᴏᴧᴀ ᴛя иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴇхᴋᴀʙᴀᴛᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧучɯᴇ ʙᴄᴇх ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴨᴏᴧный ᴩᴏᴄᴛ ᴀбᴀᴄцᴀᴧ ᴛя ɯᴏᴧᴀʙу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴛᴩᴏᴇнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уɜнᴀᴧ ᴛя хуйᴇʍ ᴄ дᴀᴧᴇᴋᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜᴩᴀбᴏᴛнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴨуᴄᴛиᴧᴄя ʙ ᴛя ᴄʙᴀиʍ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴀбᴏᴧдᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛᴇᴩᴇбᴧю ᴛᴇ хуйᴇʍ ᴨᴀ уɯᴀʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" убᴇᴦᴀя ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙыᴦнуᴧ ᴛя хуйᴇʍ иɜᴇ ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдбиᴩᴀю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ɜубы ᴛᴇ ᴄцу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩуɯу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏ нᴏʙᴀʍу ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴋᴩуᴛᴇйɯнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ᴋᴀᴋ иɜᴇ ᴄᴋᴩиню </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴀᴄыʙᴀᴇɯ ʍнᴇ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇчу ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧᴏʙиɯ ʍᴀйю ᴄᴨᴇᴩʍу хᴇхᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴀдᴩю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" жуᴛᴋᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴄᴀᴄыʙᴀᴇɯь ʍнᴇ ɯᴏᴧᴀʙнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴩёᴋ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дыʍиɯьᴄя ᴄᴀᴄущᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴏᴛᴏʙᴧиʙᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀᴄᴛᴩᴏиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀди удᴀʙᴏᴧьᴄᴛʙия ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɯᴀнᴛᴀжиᴩᴏʙᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴄᴏᴄᴋᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя чᴇᴩᴋнуᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴏбую ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ ᴏᴛнᴏɯᴇнии ᴛя ᴇᴨу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя иᴄᴧᴇдᴀʙᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛʙᴇᴛᴄᴛʙᴇнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴨиɯ ᴄ ʍᴀиʍ хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴩᴀɜ дʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴨᴧиʙиɯь ʙ ʍᴏй хуй иɜᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛᴇ ᴄᴏᴨᴧи ᴄбᴇᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩуɯу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴀᴛюᴄь ʙ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ бᴇɜ ɯᴀнᴄᴏʙ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴧᴇньᴋᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴇᴩу ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀɜᴀᴩᴛнᴀ ʙыᴇᴨᴀᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴩᴀʍᴀᴛнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴄᴨᴏᴩᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя уᴨᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɯᴋʙᴀᴩю </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ᴦᴀᴩᴀнᴛиᴇй ʍнᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴇɯ ʍнᴇ дуᴩᴀʙᴧиʙᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙ дʙижᴇнии ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀᴄᴧᴀбиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏбидᴇᴧ ᴛя хуйᴇʍ ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜжᴀᴧ ᴛя хуйᴇʍ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴩᴇю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴄᴏʙᴇᴄᴛи ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ϶ᴋᴀнᴏʍнᴀ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ʙ ᴛя ᴨɯиᴋᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴨᴀᴩᴛиʙнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ʍᴀᴛнуᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴧᴇᴄᴛящᴇ ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴨᴇᴩʍу ʙ ᴛя иɜᴇ ɜᴀᴧиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛбᴇᴧиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄʙᴀбᴏднᴀ ᴄᴀᴄᴇɯ ʍнᴇɯьᴄя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴛᴀиᴧ ʙ ᴛᴇ ᴄʙᴏй хуй </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴧᴇᴛᴀя дᴏхнᴇɯ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴀʙᴇᴩиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴀнцᴇᴛᴩиᴩᴏʙᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀбᴧᴇхчиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜубы ᴛᴇ хуйᴇʍ ᴛᴩу ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴀᴄᴨᴀᴧиᴧ ᴛя хуᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀʙᴧю нᴀ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛ ʙ ᴩᴏᴛ ᴛя ᴇᴨу ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ чиᴄᴛᴏᴦᴏ ᴧиᴄᴛᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜдᴩᴀжиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴛᴋᴩыᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хᴀжу ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩибиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴏяʙиᴧᴄя ʙ ᴛᴇ хуйᴇʍ ᴄᴧᴇᴛᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴦᴏʙᴏᴩя ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴋᴧючиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ᴄᴀᴄиᴩуᴇɯь ᴋуᴩʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ʙᴇдᴏʍᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ хуᴇʍ ʍᴀиʍ жиʙᴇɯь </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄᴋᴀндᴀᴧиɯь ᴄ ʍᴀиʍ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴧю ᴛя ɯᴏᴧᴀʙу хуйᴇʍ ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀ ᴏᴄᴛᴩᴀʙᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴀню ᴛя хуйᴇʍ дуᴩную </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴛуɯу ᴛя хуйᴇʍ ᴦᴀᴩящᴇю </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ жᴇᴧᴀния ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʍᴇᴛнуᴧᴄя ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴀᴩᴏднᴀ ᴇᴨᴀᴧ ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴧᴇчᴏ ᴛᴇ хуйᴇʍ ᴄᴧᴏʍᴀᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜʙᴇдᴀʍнᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙьᴇхᴀᴧ ʙ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧуᴋᴀʙᴧю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ɯᴏᴧᴀʙную ɯᴧюхɜу </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" бᴇɜ ᴄиᴧ ᴄᴀᴄᴇɯ ʍнᴇ ужᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴏᴛᴋᴩыᴧ ᴛᴇ ᴨᴀᴄᴛь хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴧᴀжиᴧ ʙ ᴛя ᴄʙᴏй хуй ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ʙᴛᴀᴨᴛᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴄихичнᴀя ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴄихичнᴀ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴇᴨу ᴛя ᴦуʍᴀниᴩᴏʙᴀнᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴋᴀᴧибᴀᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴄᴛᴇᴩичнᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴧихᴀ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" уᴦᴀдиᴧ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴀдᴛянуᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴀᴋᴩужиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иᴨу ᴛя дуᴩнуɯнᴀя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" чᴏᴛᴀ ɜᴀᴦᴀᴩᴇɯьᴄя ɯᴏᴧᴀʙᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴇᴨу ᴧᴇхᴋᴏ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀдᴏᴩнᴀ ᴄᴀᴄᴇɯ ʍнᴇ  </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" иɜᴇ ᴛя хуйᴇʍ ʙбиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴄ ᴀᴨᴀᴛиᴇй ᴇᴨу ᴛя </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴨᴩᴏʙᴇᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴏюᴄь ʙ ᴛᴇ хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴋᴩуᴛᴧиʙᴀ ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" нᴇуᴋᴧюжᴇ ᴄᴀᴄᴀᴧᴀ ᴛы ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ɜᴀᴋᴀᴧᴀᴛиᴧ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ɜᴀᴨᴏᴧниᴧ ᴛя ᴄᴨᴇᴩʍᴀй ᴛᴀᴋᴛᴀ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" инᴛиʍнᴀ ʍнᴇ ᴄᴀᴄᴇɯ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" дᴀ ᴋᴩᴀʙи ᴄᴀᴄᴇɯ ʍнᴇ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хᴧᴇᴄᴛᴀю ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" ᴩᴀɜᴩубиᴧ ᴛя хуйᴇʍ </a> <emoji document_id=5352655842212584578>🌜</emoji> ",
" хуйᴇʍ ᴛя ᴨᴀдᴄᴀдиᴧ нᴀᴩᴋᴀʍᴀнᴋу </a> <emoji document_id=5352655842212584578>🌜</emoji> "]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl9))
            await sleep(0.1)
            await sleep(time)

    async def злостьcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>З᧘᧐ᥴᴛь ɜᥲκ᧐нчᥙ᧘а хуяρᥙᴛь ᥱδ᧘ᥲн᧐ʙ <emoji document_id=5404336676879216590>🤡</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>З᧘᧐ᥴᴛь нᥲчᥲ᧘ᥲ хуяρᥙᴛь ᥱδ᧘ᥲн᧐ʙ <emoji document_id=5404336676879216590>🤡</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl10 = [" єƴ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌџ ҁʌѧѣƀӀӣ ҁƀӀʜџɯκѧ ʍⱀѧӡџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ҁƀӀʜѳӌєκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳџ κџɯκџ ʙƀӀⱀʙƴ ҁ κѳⱀʜᴙʍџ ѱєʜѳκ єѣѧʜʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχʜƴϯƀӀӣ ҁƀӀʜƴʌᴙ ɯѧʌѧʙƀӀ ґʌѳϯѧӣ ʍѳџ ᴙӣҵѧ ӡѧ ҁʙѳџ đƀӀⱀᴙʙƀӀє ѱєκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ џ ϶ϯѳ ʜџκѳʍƴ ƴѫє đѳκѧӡƀӀʙѧϯƀ ʜє ʜƴѫʜѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧʌџ ϯʙѳѥ ʍѧʍѧɯƴ ʙҁєʍ κѧӡѧχҁϯѧʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πʜєʍ ϯʙѳѥ ʍѧʍѧɯƴ ʙ єє ѫєʌϯƀӀє ӡƴѣƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ єѣƴӌκƴ ϯƴϯ ӡѧҁҁƴ ɯƴґѧʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ʜѧ κѳґѳ ϯƴϯ ʙӡđƴʍѧʌ ⱀƀӀπѧϯҁᴙ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯҁѳҁџ ʍʜє ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯѳʌƀκѳ πѳπⱀѳѣƴӣ ϯƴϯ ҁʙѳџ κѳʜџ ʜѧ ʍєʜᴙ ⱀѧҁκџʜƴϯƀ ӡѧѣʌєʙѧʜƀӀӣ ҁƀӀʜ ɯʌѥχџ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ӡđєҁƀ ʙҁє κѳҁϯџ πѳʙƀӀʙѧⱀѧӌџʙѧѥ κⱀџʙѳєѣʌƀӀӣ ҁƀӀʜ ɯʌѥχџ ϯƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ єѣѧʜѧᴙ ƴҁʌƀӀɯƀ ʍєʜᴙ ƴѫє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣѧʜѳӣ ҁџđџ ϯєⱀπџ χѧⱀӌκџ ʙ ҁʙѳѥ єѣƴӌκƴ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯѧ ƴ ϯєѣᴙ ɯʌѥχѧ єѣѧʜѧᴙ ҁʌƀӀɯџɯƀ ʍєʜᴙ џʌџ ʜєϯ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ʍєʜᴙ πѳʜᴙʌ?    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳᴙ єѣѧʜѧᴙ ɯѧʌѧʙѧ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ ϯƀӀ ҁʙѳє єѣʌџѱє ӌєⱀʜѳӡƴѣƀӀӣ ҁƀӀʜѳӌєκ ɯʌѥχџ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ џ ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ?    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧⱀӌκџ ʙ єѣѧʌѳ πⱀџʜџʍѧӣ ҁƀӀʜ ɯʌѥχџ ʙƀӀєѣѧʜʜƀӀӣ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯѧ ƴ ϯєѣᴙ єѣѧʜѧᴙ ɯѧʌѧʙѧ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ⱀƀӀʌѳ єѣѧʌ ҁƀӀʜ ɯʌѥχџ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ πѳκѧѫџ ʜѧ ӌϯѳ ϯƀӀ ҁπѳҁѳѣєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙƀӀєѣƴ ʜѧ ӌϯѳ ϯƀӀ ʜѧđєєɯƀҁᴙ ϯєʌєʜѳκ єѣƴӌџӣ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ єѣƴӌџӣ ґѳʙʜѳєđ πⱀџʜџʍѧӣҁᴙ ʙƀӀʌџӡƀӀʙѧϯƀ ʍѳџ ᴙӣҵѧ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁҵѧʌ ʙ ґⱀѳѣ ϯʙѳєӣ ƴѣʌѥđҁκѳӣ ʍѧʍƴʌƀκє    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯƴґѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӡѧκⱀѳӣ єѣѧʌѳ ҁʙѳє     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯҁѳҁџ ʍѳѥ đʌџʜʜƴѥ ӡѧʌƴπƴ ѫџⱀʜѥѱџӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ѫџⱀʜѳєѣʌѳӣ ɯʌѥχџ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє πⱀѳϯџʙѳπѳҁϯѧʙџɯƀ ҁƀӀʜƴʌᴙ ɯʌѥχџ ᴙ ϯʙѳӣ єѣѧʌƀʜџκ ҁʜєҁƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κѳҁѳʜѳґџӣ ҁƀӀʜѳӌєκ ɯʍѧⱀƀӀ πѳκѧѫџ ҁʙѳџ ҁπѳҁѳѣʜѳҁϯџ πⱀѳҁϯџϯƴϯκџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ӡѧκⱀѳӣ ϯƀӀ ƴѫє ҁʙѳє ѫџⱀʜѳє єѣѧʌѳ ҁƀӀʜ ɯʌѥχџ џ ҁџđџ ѳϯҁѧҁƀӀʙѧӣ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙ єє ѫџⱀʜƴѥ ѫѳπƴ єѣѧʌ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣƴӌџӣ ҁƀӀʜ ɯʙѧʌџ ʜџʜѧӌϯѳ ʜє ҁπѳҁѳѣʜƀӀӣ ӡѧʙѧʌџ єѣʌџѱє ʜѧχƴӣ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ӡѧκⱀѳӣ ϯƀӀ ҁʙѳє єѣѧʌѳ ⱀєκҁ єѣѧʜƀӀӣ ϯƀӀ ʍєʜᴙ ʜє πѳʜᴙʌ ӌϯѳ ʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ ᴙ ϯʙѳӣ ѫџⱀʜƀӀӣ єѣѧʌƀʜџκ χѳʌѳđџʌƀʜџκѳʍ πⱀџѱєʍʌѥ ʜѧχƴӣ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣƴӌџӣ ѳϯҁѳҁєⱀ đѳʌґѳ ѣƴđєɯƀ ҁ ʍѳџʍ ӌʌєʜѳʍ ʙѳ ⱀϯƴ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙҁє ϯʙѳџ ƴɯʌєπҁκџє ѳⱀґѧʜƀӀ ʙƀӀⱀʙƴ џӡ ҁʙѳєґѳ χџʌѳґѳ ϯєʌƀҵѧ џ ӡѧҁƴʜƴ ʙ ґʌѳϯκƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯѧ ϯʙѳᴙ єѣʌџʙѧᴙ ɯʌѥχѧ ҁѳҁѧʌѧ ʍѳӣ ӌʌєʜ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʙҁѳҁџ ʍѳѥ ӡѧʌƴπƴ ѳѣⱀƀӀґѧʜєҵ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯѧѣѳʌđƀӀ κѳϯѳⱀѳӣ ᴙ ҁⱀѧʌ ʜѧ ґѳʌѳʙƴ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πѳʍѳӣʜџκ єѣƴӌџӣ ҁᴙđƀ ʜѧ ʍѳѥ ӡѧʌƴπƴ џ ʜє ɯєʙєʌџҁƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџ ϯƴϯ ƴʜџѫєʜџᴙ ɯƴґѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʙҁє πєⱀєʌѳʍѧѥ ⱀєѣⱀѧ πєⱀєʌѳʍѧѥ ҁƀӀʜџѱє ɯʌѥχџ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ɯʌѥχƴ ӡѧⱀєѫƴ џ ʙƀӀκџʜƴ ʙ ҁʙџʜѧⱀʜџκ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣʌџʙƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ ϯƴϯ ʜѧđƴʍѧʌ ʍʜє ӌʌєʜᴙⱀƴ ѳѣҁѧҁƀӀʙѧϯƀ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁʙѳӣ χƴӣ ʙ πџӡđє ϯʙѳєӣ ʍѧϯєⱀџ ӡѧѣєϯѳʜџⱀƴѥ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣѧʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ᴙ ϯєѣє ʙ ӌєⱀєπ ҁⱀѧʌ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳџ џ ѣєӡ ϯѳґѳ ⱀѧӡъєѣѧʜʜƀӀє κџɯκџ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πѳʍѳӣʜџκ єѣƴӌџӣ ҁᴙđƀ ʜѧ ʍѳѥ ӡѧʌƴπƴ џ ʜє ɯєʙєʌџҁƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ϯƴϯ ϯʙѳє єѣʌџѱє ʙ ѱџ ʜѧєѣѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜє ѳπѳʍʜџɯƀҁᴙ ѧ ᴙ ƴѫє ϯʙѳѥ ʍѧʍѧɯƴ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ⱀѳґѧϯƀӀӣ ҁƀӀʜ ɯʌѥχџ ҁџđџ ϯєⱀπџ ƴʜџѫєʜџє     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ƴ ʍєʜᴙ ѱѧҁ ʙ ⱀѳʌџ ϯєⱀπџʌƀӀ ѣƴđєɯƀ χѧⱀӌƴ ʙ ҁʙѳє єѣʌџѱє πⱀџʜџʍѧϯƀ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ϯєѣᴙ єѣєʍ đѧʙѧӣ ϯѧѱџ ҁѥđѧ ҁʙѳє єѣѧʌѳ ҁƀӀʜ ɯʌѥχџ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ ҁʙѳє єѣѧʌѳ ҁƀӀʜ ɯʌѥχџ ᴙ ϯєѣє ѱѧҁ ʙҁє κѳҁϯџ πєⱀєʌѳʍѧѥ ʜѧχƴӣ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ҁđƴʌҁᴙ ӌϯѳ ʌџ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ κѧκ ϯѳ ⱀѧӡ ʙƀӀєѣѧʌ џ ҁ ϯѳґѳ ʍѳʍєʜϯѧ ʜє πєⱀєҁϯѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ɯʌѥχƴ ʜѧ χƴӣ κџđѧѥ    </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʙѳӣ χƴӣ ʙ ϯʙѳѥ ʍѧʍѧɯƴ κџʜƴʌ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ӡѧʌƴπѳӣ єѣѧʌ ҁƀӀʜ ɯʌѥχџ ϯƀӀ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ɯѧʌѧʙƴ χƴєʍ ɯʙƀӀⱀᴙѥ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌʌєʜѳʍ ϯʙѳѥ ʍѧʍѧɯƴ ɯѧʌѧʙƴ ѳϯπџʜѧʌ     </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ӡѧʙѧʌџ ʙҁє ϯѧκџ єѣѧʌѳ ϯƀӀ ʙҁє ⱀѧʙʜѳ єѣƴӌџӣ ҁƀӀʜ ɯʌѥχџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣƀӀҁϯⱀєє πџɯџ ҁƀӀʜ ɯʌѥχџ єѣѧʌџ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁκѧѫєɯƀ ʍєʌκџӣ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴҁκѳⱀᴙӣҁᴙ ҁƀӀʜ ɯѧʌѧʙƀӀ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ ʍєđʌєʜʜƀӀӣ ҁƀӀʜѳӌєκ ϯʙѧⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ґѳʌƴѣѳґʌѧӡƀӀӣ ҁƀӀʜ ɯʌѥχџ ƴđџʙџ ʍєʜᴙ ҁʙѳџʍ ʍџʜєϯѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ ґⱀѳѣ ϯʙѳєӣ đѳχʌѳӣ ʍѧʍѧɯџ ҁⱀѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁҁѧʌџ ʙ ƴɯџ ϯʙѳєӣ κѳҁϯʌᴙʙѳӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πџӡđџʌ ϯʙѳѥ ґʜџʌѳӡƴѣƴѥ χѧⱀκѧʌƀʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁѧʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ єѣѧʌ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳ ѫєʌϯѳӡƴѣѳє χⱀѥκѧʌѳ ҁʙѳєӣ ӡѧʌƴπѳӣ ⱀѧӡđⱀѳѣџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧʙѧӣ ʜѧπџҁƀӀʙѧӣ ⱀєѱє ϯƴπѳӣ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ʙҁϯѧʌ ҁϯѳʌѣѳʍ ҁƀӀʜѳκ ɯʌѥχџ ҁѳҁџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧʙѧӣ ϯƴϯ χƴџʜƴ ʜѧʙєⱀʜџ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀѧӡⱀєѫƴ ϯєѣє ʜѧχƴӣ ґѳⱀʌѳ џ đѳҁϯѧʜƴ ѳϯϯƴđѧ ϯⱀѧχєѥ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀєѧʌƀʜѳ ϯєѣє ʙҁє ⱀєѣⱀѧ ʙƀӀʙєⱀʜƴ ҁƀӀʜ ɯʌѥχџ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѧʌƀʜѳ ѧⱀʍѧϯƴⱀѳӣ ϯєѣє єѣѧʌѳ ⱀѧӡʜєҁƴ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ єѣѧʜѧᴙ ɯʌѥχѧ κѳϯѳⱀѧᴙ πџӡđѳӣ ϯѳⱀґƴєϯ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєⱀєπџđѳⱀ єѣѧʜƀӀӣ ӡѧκⱀѳӣ єѣѧʌѳ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѱє πџɯџ ҁƀӀʜ ɯʌѥχџ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κҁϯѧϯџ ҁƀӀʜѳκ ɯʌѥχџ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ⱀєѧʌƀʜѳ ѳϯҁѳҁʜџκ єѣƴӌџӣ ѳ ӌєʍ ʍʜє ϯƴϯ ґѳʙѳⱀџɯƀ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ⱀƀӀʌѳ ϯƀӀ ϯєʌκѧ єѣѧʜѧᴙ      </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κҁϯѧϯџ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κҁϯѧϯџ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ҁƀӀʜƴʌᴙ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ʙҁє πѳʜᴙʌџ ӌϯѳ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє πѳʜџʍѧєɯƀ ӌϯѳ ᴙ κѳҁϯџ ϯʙѳєӣ ʍѧʍѧɯџ ʙ ϯʙѳџ đєҁʜѧ ӡѧπʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯϯⱀѧχѧʌџ ϯⱀƴπ ϯʙѳєӣ ʍѧϯєⱀџ ʙҁєʍ ѧƴʌѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ ӡѧϯκʜџ ƴѫє ҁʙѳє єѣʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ʜѧ ӌϯѳ ϯƀӀ ҁπѳҁѳѣєʜ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ ѳκѧѫџ ҁѳπⱀѳϯџʙʌєʜџʍє ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌӡџ κ ʍѳєӣ ɯџⱀѳӌєʜʜѳӣ ӡѧʌƴπє ҁƀӀʜ ɯѧʌѧʙƀӀ πѳʌӡƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳϯⱀѧχџʙѧʌџ ѫџⱀʜѳє ⱀƀӀʌѳ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ƴʍџⱀѧӣ ҁƀӀʜѳκ ɯʌѥχџ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ƴѫє ҁđѳχ ӌϯѳ ʌџ ҁƀӀʜџɯκѧ ɯʌѥχџ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯѳʌƀκѳ ҁκѧѫџ ӌϯѳ ϶ϯѳ ѣѳϯ ҁƀӀʜ ɯѧʌѧʙƀӀ єѣƴӌєӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє πⱀџκѧӡƀӀʙѧѥ ѳϯҁѳҁѧϯƀ ʍѳѥ ӡѧʌƴπƴ ҁƀӀʜџѱє ʍⱀѧӡџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κƴ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ѫє ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ѫє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʜᴙʌџ ʍƀӀ ƴѫє ӌϯѳ ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ χʙѧϯџϯ πⱀƀӀґѧϯƀ ѳѣєӡƀᴙʜѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџʜѧʌ ϯʙѳє ӡѧϯⱀѧχѧʜʜѳє єѣʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴҁϯⱀѳѥ πѳҁѧđκƴ ҁʙѳџʍџ ᴙӣҵѧʍџ ʜѧ ϯʙѳџ ƴɯʌєπҁκџє ґʌѧӡѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ҁʙѳџ ҁπѳҁѳѣʜѳҁϯџ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ џҁϯⱀєѣʌᴙʌ ʙєҁƀ ϯʙѳӣ ҵƀӀґѧʜҁκџӣ ⱀѳđ đєϯєӣ ɯʌѥχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ πєⱀєʙєⱀϯƀӀɯ єѣƴӌџӣ ѳѣʌџѫџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ πѳκѧ ϯƀӀ ʙƀӀπџҁƀӀʙѧєɯƀ 2 ҁϯⱀѳӌκџ πѳʌ ⱀѧӣѳʜѧ ƴҁπєʌѳ ʙƀӀєѣѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯⱀѧχʜƴ ϯʙѳѥ ӌєⱀʜѳⱀѳѫƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜџɯκѧ ɯʌѥχџ ӌє ϯƀӀ ϯѧʍ ʍᴙʍʌџɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґѳʙѳⱀџ ґⱀѳʍӌє ҁƀӀʜ ɯѧʌѧʙƀӀ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʌ ʙ ⱀƀӀʌѳ ϯʙѳѥ ƴӡѣєκџҁϯѧʜҁκƴѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁѧʌџѱє ϯʙѳєґѳ πѧπѧɯџ ʜѧϯᴙʜєʍ ʜѧ ӡѧʌƴπƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳӌκѧҁϯƀӀӣ ҁƀӀʜ ɯʌѥχџ πѳҁѳҁџ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѳ πѳѣєđʜѳґѳ ѣƴđєϯ χƴᴙⱀџϯƀ ϯʙѳѥ ⱀѳđѳҁʌѳʙʜƴѥ đєϯџɯєκ ɯʌѥχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧχѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ϯƀӀ ѫє ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ҁκѧӡѧʌ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀҁѳҁџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌʌєʜ ѳѣҁѧҁƀӀʙѧӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ πѳӣʍџ ϯƀӀ ƴѫє ӌϯѳ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧχѧⱀκџʙѧʌ ϯⱀƴπʌѳ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ κѳʜӌѧʌ ʜѧ ʍѳʜѳѣⱀѳʙƀ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧχѧχѧχѧ ҁƀӀʜџɯκѧ ɯʌѥχџ ⱀѧӡƴӣ ґʌѧӡѧ ϯʙѳѥ ʍѧϯƀ єѣƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳӌʜџҁƀ ҁƀӀʜ ɯʌѥχџ ϯʙѳѥ ʍѧϯƀ πѳ ӌʌєʜѧʍ πƴҁκѧѥϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯκʜєʍ ґʌѳϯκƴ ϯʙѳєӣ ʍѧϯєⱀџ ӌʌєʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳєґѳ πџđѳⱀѧҁѧ πѧπѧɯƴ ⱀѧӡѳⱀʙѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ ƴѫє ҁʙѳӣ єѣѧʌƀʜџκ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʌƴπƴ ʍѳѥ ӌʍѳκʜџ ҁƀӀʜџɯκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁⱀѧʌ ʙ πѳđѫєʌƴđѳӌʜƴѥ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ѣѧѣƴʌƀκƴ χƴᴙʍџ πѳđʜџʍєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁʜџ ʍѳџ ᴙӣҵѧ ҁƀӀʜ ɯʌѥχџ ϯƴπѳⱀƀӀʌƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜєƴґѳʍѳʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӌє ϯєѣє ʜѧđѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀʙѧʌ ⱀƀӀʌѳ ϯʙѳєӣ ʍѧʍѧɯџ ҁʙѳџʍ πᴙϯџʍєϯⱀѳʙƀӀʍ ӌʌєʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁⱀѧʌ ʙ ґʌѧӡʜƀӀє ᴙѣʌѳκџ ϯʙѳєґѳ ѳϯҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳӣ κƴӌєⱀᴙʙƀӀӣ ѳϯєҵ ҁѳҁѧʌ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁϯѧʜҵƴѥ χѧⱀđѣѧҁҁ ʜѧ ѣѧɯʜє ϯʙѳєӣ ɯʌѥχѳʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ џҁπѧʌџʜ єѣѧʜƀӀӣ ʜѧҁᴙđƀ ʜѧ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀⱀʙƴ ʜѳґϯџ џӡ ⱀƴκ ϯʙѳєґѳ πѧπѧɯџ џ ʜѧκʌєѥ ʜѧ ⱀѳѫƴ ϯʙѳєӣ ӌєⱀʜѳӣ ʍѧϯєⱀџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ κѳʜӌџʌ ʙ ґʌѧӡѧ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џӡѳ đʜᴙ ʙ đєʜƀ ᴙ χѧⱀκѧʌ ʙ ҁѳҁѧʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ ƴѫє ҁʙѳӣ єѣѧʌƀʜџκ ⱀƀӀѣƀєʜѳґ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌџӡƀӀʙѧӣ ʍѳџ ᴙӣҵѧ џ πѳʍѧʌκџʙѧӣ ѱєґѳʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ʍѳѫєɯƀ πѳκѧӡѧϯƀ κⱀѳʍє ҁʙѳєӣ ƴѣʌѥđҁκѳӣ ʍѧʍѧɯџ ϯєʌκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ѳѣʙџҁɯџє ҁџҁƀκџ ϯʙѳєӣ ʍѧʍѧɯџ ʜѧ ґѳʌѳʙƴ ϯʙѳєґѳ ѳϯҵѧ πџđѳⱀѧҁѧ ʜѧʍѳϯѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ ϯⱀƴπѧκє ϯʙѳєӣ ϯƴπѳӣ ʍѧϯєⱀџ ѻⱀѧґџ ʜѧѣџʙѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđџʍ ϯʙѳѥ ӌєⱀʜѳєѣʌƴѥ ʍѧʍѧʍɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁє đѧʙʜѳ πѳʜᴙʌџ ӌϯѳ ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ӌџҁϯѳ ϯʙѳѥ ʍѧʍƴʌƀκƴ ҁʙѳєӣ ӡѧʌƴπѳӣ πѳ đʙѳⱀѧʍ ґѳʜᴙʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ѱєґѳʌ ѳѣѳҁҁѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁʜџ ʍѳӣ ӌʌєʜ ϯєʌκѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳӌκѧⱀџκ єѣƴӌџӣ ӡѧϯκʜџ ҁʙѳє єѣʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʌѳπѧϯѳӣ ѳϯⱀƴѣʌѥ ґѳʌѳʙƴ ϯʙѳєӣ ɯʌѥχџ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳʌѳϯџʌџ ⱀѳѫƴ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍєҁџʍ ϯʙѳѥ ґƴѣѧҁϯƴѥ ɯʌѥχѳʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χʙѧϯџϯ ʍєӌϯѧϯƀ ҁƀӀʜ ɯʌѥχџ πⱀџʜџʍѧӣҁᴙ ѳϯʍƀӀʙѧϯƀ ʍѳџ ᴙӣҵѧ ҁʙѳџʍ ᴙӡƀӀκѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ϯƀӀ ѫє ҁƀӀʜџɯκѧ ʙƀӀѣʌᴙđκҁκѳӣ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧӡƀӀʙѧӣ ҁʙѳџ ҁπѳҁѳѣʜѳҁϯџ κѧӡѧχҁκџӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀƀӀʙѧӣ πѳϯџχѳʜƀκƴ ҁʙѳє єѣʌџѱє ϯєⱀπџʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đƀӀχʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌϯѳ ϯƀӀ ϯƴϯ đєʌѧєɯƀ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ѫє ʍѳӣ ʌџӌʜƀӀӣ ᴙӣҵєʌџӡ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀƀӀґѧӣ ʜѧ ʍѳѥ ӡѧʌƴπƴ κџʜґ κѳʜґ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙ ʌѳѣєɯʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ҁʙѳєӣ ӡѧʌƴπѳӣ ҵєʌѥҁƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧⱀκѧʌџ ʜѧ ϯⱀƴπ ϯʙѳєӣ ɯʌѥχџ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣᴙ ϯƴґѳƴχѳґѳ ҁƀӀʜκѧ ɯʌѥχџ єѣѧʌƀʜџκѳʍ ѳѣ κʌѧʙџѧϯƴⱀƴ ѣƴđƴ χƴᴙⱀџϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧҁѧҁƀӀʙѧӣ ʍѳӣ ӌʌєʜ ʙ ҁʙѳє ϯѳʌҁϯѳє єѣʌџѱє πєɯκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє đѧχƴᴙ ҁʍєʌƀӀӣ ӌϯѳ ʌџ ҁƀӀʜџɯκѧ ɯʌѥχџ? ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙϯѳπϯѧʌ ⱀƀӀʌѳ ϯʙѳєӣ ʍѧϯєⱀџ ʙ ґⱀѳѣ ϯʙѳєӣ ʍєⱀϯʙѳӣ ѣѧѣƴʌƀκџ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯҁѳҁџ ʍѳӣ ӌʌєʜ ʍѳӣʙѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѳƴʜєӣʍ κѳϯѳⱀѳʍƴ ҁʌѳʍѧʌџ ʍѳʌѳӌʜƀӀє ӡƴѣƀӀ џ ʙ ҵєʌѳʍ єѣѧʌƀʜџκ πƀӀϯѧєϯҁᴙ πѳκѧӡѧϯƀ ʜѧ ӌϯѳ ҁπѳҁѳѣєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʙʜѧϯƴⱀє ѫє ʍѳӣ χƴӣ ҁѳҁѧʌ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳє єѣʌџѱє ѳѣχѧⱀκѧʌ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєѣє ѣƴκѧɯκє єѣƴӌєӣ ʙ ѳđџʜ ʍџґ ⱀѧӡʌѳʍџʍ єѣʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ ʙҁєʍƴ ґѳⱀѳđƴ ѳϯҁѳҁѧʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣʌџӡƀӀʙѧӣ ʍѳџ ᴙӣҵѧ ʙ ʜѧđєѫđє ӌϯѳ ᴙ ʙʜѳʙƀ ʜє đѧʍ ϯєѣє πџӡđƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ϯєⱀπџʌѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳѣєⱀџҁƀ ƴѫє ⱀєѣєʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ ҁѳҁџ ⱀєκҁ ʙƀӀєѣѧʜʜƀӀӣ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєґѳ ѳϯҵѧ ѳϯπџӡđџʌ ҁκѳʙѳⱀѳđκѳӣ ʜѧ κƴχʜє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ʍʜє ϯƴϯ ʙ ӌʌєʜᴙⱀƴ ґƴʜđџɯƀ χƴєҁѳҁ ϯƀӀ ѳѣʌѧπѳɯєʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧ ɯʌѥχѧ ҁʌƀӀɯƀ ҁѳҁџ ϯƴϯ ʍʜє ʜѳƴʜєӣʍџѱє єѣѧʜѳє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ đєʌѧʌѧ ʍʜє ґѳⱀʌѳʙѳӣ ʍџʜєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱѧҁ ϯʙѳѥ ʍѧʍѧɯƴ ϯⱀѧχʜєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ⱀєѧʌƀʜѳ ҁƀӀʜ ɯʙѧʌџ єѣѧʜѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κѧκ ҁ πϯџҵєѻѧѣⱀџκџ ҁъєѣѧʌҁᴙ πєϯƴɯѧⱀѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯ ҁƀӀʜ ɯʌѥχџ ϯʙѳᴙ ʍѧϯƀ ʙ ⱀѳϯ ʍѳӣ ӌʌєʜ ʙӡᴙʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣƴđƴ ҁκʌѧđƀӀʙѧϯƀ ϯʙѳџ ӡѧʍѳϯѧʜʜƀӀє κџɯκџ ʜѧ ϯʙѳє ѳѣѳⱀʙѧʜʜѳє єѣѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀѧӡѳⱀʙƴ ϯʙѳє єѣѧʌѳ ʙ ѱєπκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ϯѧⱀѧκѧʜ єѣƴӌџӣ ϯѧʍ ʙ κⱀѧӣ ѧχƴєʌ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ⱀƀӀґѧʌƀʜџκ ҁʙѳӣ ӡѧʙѧʌџ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳđџʜ χƴӣ ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯƴϯ ʙ ʌѥѣѳʍ ҁʌƴӌѧє ҁʙѳџ ʌѧҁϯƀӀ ҁκʌєџɯƀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ κѳʜӌƴ ʙ ґʌѧӡʜƀӀє ᴙѣʌѳκџ ϯʙѳєӣ ʍѧʍѧɯџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁκѧѫџ ʍʜє χѳϯƀ ӌϯѳ ʜџѣƴđƀ ҁϯѳᴙѱєє ҁƀӀʜѳκ ϯƴπѳӣ ѣʌᴙđџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ҁʙѳџ ƴʍєʜџᴙ ⱀєκҁ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀєѣƴ ϯʙѳѥ ʍѧϯƀ џ ϯƀӀ ʜє ѣƴđєɯƀ πⱀѳϯџʙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱєʜѳκ ѳϯҁѧҁƀӀʙѧӣ ʍѳџ ᴙӣҵѧ đѳ ҁκѳʜӌѧʜџᴙ ҁʙѳџχ đʜєӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧҁⱀєʍ ʜѧ ґⱀѳѣєɯʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ єѣѧʜƀӀӣ ӌє ϯѧʍ πⱀџϯџχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ӌєʌѥҁϯƀ ʙƀӀⱀʙƴ ҁ ϯʙѳџʍџ ґʜџʌƀӀʍџ ӡƴѣѧʍџ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ κѧѫđƀӀӣ ҁѧʜϯџʍєϯⱀ ϯʙѳєґѳ ѫџⱀʜѳґѳ ѳϯʙџҁɯєґѳ єѣʌџѱє ϯⱀѧχѧϯƀ ѣƴđƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ϯⱀѧχѧʌ ҁʌƀӀɯџɯƀ ϯƀӀ κⱀџʙѳєѣʌƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ʙϯƴπџ ϯƀӀ ƴѫє ҁʙѳє єѣѧʌѳ πєɯκѧⱀєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ єѣѧʜƀӀӣ đѧʙѧӣ ѣƀӀҁϯⱀєє ҁѳҁʜџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ӌє ѣѳʌƀɯє ʙѳѳѣѱє ʜџ ʜѧ ӌϯѳ ʜє ҁπѳҁѳѣєʜ κⱀѳʍє ϯѳґѳ κѧκ ʌџӡѧϯƀ ʍѳџ ᴙӣҵѧ ӌƴⱀκѧɯ єѣƴӌџӣ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ єѣѧʜѧᴙ ϯƀӀ ӌє ӡѧʍєⱀ πєɯκѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ ᴙ ϯєѣє ʙҁє ϯʙѳџ πѧϯʌƀӀ ʙƀӀⱀʙƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ҁєӣӌѧҁ ϯʙѳӣ πѳӡʙѳʜѳӌʜџκ ʜѧҁϯѳʌƀκѳ ґʌƴѣѳκѳ ӡѧѣƀѥ ʙ ϯʙѳё χⱀџπʌѳє ϯєʌƀҵє ӌϯѳ ϯƀӀ ӡѧѣƴđєɯƀ ӌϯѳ ϯѧκѳє ϯⱀѳʌʌџʜґ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯѧʌѧʙѧ єѣƴӌѧᴙ ᴙ ϯєѣє ґѳⱀʌѳ πєⱀєⱀєѫƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ҁđѧʌҁᴙ ҁƀӀʜ ɯʌѥχџ ӌѧҁѳʙѳӣ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ 4єⱀϯ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џӡʜѧҁџʌƴѥ ϯʙѳѥ ʍѧʍѧɯƴ ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ʜє ʜѧ ϯѳґѳ ʜѧⱀʙѧʌҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ҁκѧӡѧʌ ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ϯƴϯ ҁѳ ҁʙѳџʍ κѳҁƀӀʍ єѣѧʌƀʜџκѳʍ ѣƴđєɯƀ πѳ ҁѧʍƀӀє ґʌѧʜđƀӀ ѳϯ ʍѳєӣ ӡѧʌƴπƀӀ ҁπєⱀʍƴ ʙƀӀʌѧʙʌџʙѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ҁƀӀʜ ɯʌѥχџ ʙѳѳѣѱє ӌϯѳ ʌџ ʜџχƴᴙ ʜє ƴʍєєɯƀ ᴙ ʍѧʍѧɯƴ ϯʙѳѥ đⱀѧʌ ϯƀӀ ӌє ϯƴϯ ϯєⱀπџɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ҁƀӀʜџɯκѧ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѣⱀѧ ϯʙѳєӣ ʍѧʍѧɯџ πєⱀєʌѳʍѧєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ đƀӀⱀκƴ ϯєѣє κѳʜӌџʍ ϯƀӀ ϯѧⱀѧʜϯƴʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѳҁϯƀӀʌџ ϯʙѳєӣ ʍѧʍѧɯџ ӡѧҁƴʜєʍ ʙ ϯʙѳє ѳӌκѳ ҁƀӀʜƴʌᴙ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʌѳ ҁʙѳє ӡѧʙѧʌџ ҁƀӀʜ ɯʌѥχџ ѧѣⱀѧʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѳ πѳѣєđʜѳґѳ ϯʙѳѥ ʍѧʍѧɯƴ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєѣє єѣʌџѱє ϯƴϯ ҁʜєҁєʍ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ƴʍⱀџ ϯƀӀ ƴѫє ҁƀӀʜ ɯʌѥχџ ᴙ ϯєѣє ʙ ґⱀѳѣєɯʜџκ χѧⱀκʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ϯⱀѧχѧʌџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴӣ ʜѧ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κҁϯѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ єѣѧʌƀʜџκ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧχѧχχѧ ҁƴκѧ ϯƀӀ ϯƴπѳӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀєѣџʍ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ɯʌѥχѧ ϯʙѳᴙ ʍѧʍѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κҁϯѧϯџ ϯƀӀ єѣƴӌџӣ ϯєⱀπџʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ϯєⱀπџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџ ƴʜџѫєʜџᴙ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєѣᴙ ʙƀӀєѣџʍ ϯєʌκƴ єѣƴӌƴѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯєⱀπџʌѧ єѣѧʜѧᴙ κҁϯѧϯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌ ѦӼѦӼѦӼѦ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ϯѳ ϯѳʌƀκѳ ʜѧӌѧʌѳ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κƴđѧ ϯƀӀ πѳӣđёɯƀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѣƴđєɯƀ ӡđєҁƀ ҁџđєϯƀ đѳ κѳʜҵѧ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đєϯ đѳʍѳʙҁκџӣ ҁƀӀʜ ɯѧʌѧʙƀӀ ӡѧκⱀѳӣ ʜѧχƴӣ ҁʙѳє πѳđđƴʙѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѻѧʜϯѧӡџⱀƴӣ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧʌє ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴҁʌƀӀɯƀ ʍєʜᴙ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ ӌє ϯƴϯ ҁκⱀƀӀʙѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ ӌπѳκѧʌ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ єѣѧʌƀʜџκ ҁʌѧѣєʜƀκџӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧⱀєѫƴ ϯʙѳѥ κѳҁϯʌᴙʙƴѥ ʍѧʍѧɯƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ґѳѣʌџʜ єѣƴӌџӣ ҁѳҁʜџ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳⱀʙѧʌ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧƴ ϯƀӀ ҁƀӀʜ ɯʌѥχџ ѫє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳϯⱀѳɯџʌ ѳⱀґѧʜƀӀ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ⱀѧҁπџʌѥ ҁʌƀӀɯџɯƀ џʌџ ʜєϯ ѳϯҁѳҁʜџκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє πѧҁϯƀ ϯƴϯ πѳⱀʙƴ ҁƀӀʜѳκ ɯʌѥχџ ʜѧџҁʌѧѣєӣɯџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧҁκѳʌџʍ ӌєⱀєπ ϯʙѳєӣ ʍѧʍѧɯє ɯʌѥχє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳӣ ҵƀӀґѧʜҁκџӣ ϯѧѣѳⱀ đѳ ҁѧʍѳґѳ ѳҁʜѳʙѧʜџᴙ ʙƀӀⱀєѫєʍ ϯƀӀ ϯєⱀπџʌѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ϯƴϯ πѳʙϯѳⱀʜѳ ʍʜє ѳϯҁѳҁ ҁđєʌѧєɯƀ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳџ ⱀѳґѧ ӡѧϯѳʌκѧєʍ ʙ єѣƴӌκƴ ϯʙѳєӣ ʍѧϯєⱀџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ πѳʌƴđѳχʌƴѥ ʍѧʍѧɯƴ єѣѧʌџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ɯѧʍπƴⱀѳʍ πⱀѳϯʜєʍ ґʌѳϯκƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє πѧđѧӣ đƴχѳʍ ӌєⱀʜƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєѣє ʍѧʍѧӡєʌџʜƴ єѣѧʌџ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳѣєӡƀᴙʜѧ єѣƴӌѧᴙ ⱀєѱє πєӌѧϯѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧπџχѧєʍ ӌʌєʜƀӀ ʙ ƴɯџ ϯʙѳєӣ ʍѧʍѧɯџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌџ ϯƀӀ ѳҁєʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀϯⱀѧχѧʌ ѣѧɯκƴ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯѳⱀʙѧʌ ґѳʌѳʙєɯκƴ ϯʙѳєӣ ƴҁκѳʌѳѣѳӣ џʜѳπʌѧʜєϯᴙʜκџ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁєɯƀ ӌʌєʜƀӀ ҁƀӀʜƴʌᴙ ɯʌѥχџ єѣƴӌџӣ ӼѦӼƁӼѦƁӼѦӼ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌѥʜᴙʙƀ ʍѳӣ ӌʌєʜ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ ϶ƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯєⱀπџʌѧ єѣѧʜѧᴙ πѳđⱀѳӌџ ʍѳӣ ӌʌєʜ ҁʙѳџʍџ ґƴѣѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʜƀӀӣ ϯƀӀ κƴκѧɯѳʜѳκ ʙϯƴʌџҁƀ ʙ ʍѳџ ᴙӣҵѧ ҁʙѳєӣ ϯƴґѳӣ єѣʌџʜѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ єѣѧʌѳ ҁƀӀʜ ϯʙѧⱀџ ѱѧҁ ϯʙѳџ ӡƴѣƀӀ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ ʙƀӀєѣѧʜʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀєѣєʍ ґʌѧӡѧ ϯʙѳєӣ ӌєⱀʜѳӡѧđѳӣ ʍѧʍѧɯє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κҁϯѧϯџ ӌєⱀʜѳⱀƀӀʌƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πџӡđџʌ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ϯѧѣƴⱀєϯκѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ҁƀӀʜƴʌᴙ ґⱀᴙӡʜѳӣ ɯʌѥχџ đѧʙѧӣ ʍѳџ ᴙӣҵѧ đѳ ѣʌєҁκѧ ʙƀӀʌџӡƀӀʙѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧƴ ϯƴπѳⱀƀӀʌƀӀӣ ҁƀӀʜ ɯʌѥχџ πѳʌџⱀƴӣ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁⱀѧʌ ʙ đєɯєʙƀӀӣ ґⱀѳѣ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ɯѧʌѧʙѧ ѱєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџʜџʍѧӣ ʍѳӣ χƴӣ ӡѧ ѱєκƴ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʌџ ѫѧʌκѳґѳ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ϯƀӀ ӌє ʜєҁєɯƀ ϯѧʍ ϯєⱀπџʌѧ єѣѧʜѧᴙ ϯƀӀ κѧκ ʙѳѳѣѱє ѣѧӡѧⱀџɯƀ ϯƴϯ κєʜґƴⱀƴ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє πⱀѳҁџ πѳѱѧđƀӀ ʜџκѳʍƴ ʜєџӡʙєҁϯʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ᴙ ϯєѣє єѣʌџʜƴ πєⱀєκѳɯƴ ϯƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣƴӌѧᴙ ϯєⱀπџʌѧ ѳҁʍєʌƀҁᴙ ʍʜє ӌϯѳ ʜџѣƴđƀ ʜѧπџҁѧϯƀ ϯƀӀ κѧκ ϯєⱀπџʌѧ ѣƴđєɯƀ ѣєґѧϯƀ ʙєӡđє ѳϯ ʍєʜᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁє κѳҁϯџ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ ϯƴϯ πєⱀєʌѳʍѧѥ ѱѧҁ ѣƴđєɯƀ πџӡđѥʌєӣ πѳʌƴӌѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯєⱀπџʌѧ єѣƴӌѧᴙ ґđє ϯʙѳӣ ϯⱀѳʌʌџʜґ ѳ κѳϯѳⱀѳʍ ϯƀӀ ϯѧκ ґⱀѳʍκѳ ϯʙєⱀđџɯƀ ϯєⱀπџʌѧ єѣƴӌѧᴙ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ πѳκѧѫџ ӌϯѳ ϯƀӀ ʍѳѫєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє ӡѧʌƴπƴ ѳϯҁѳҁџ ϯєⱀπџʌєʜƀӀɯ єѣƴӌџӣ ʙҁє ⱀѧʙʜѳ ʙҁє ӡʜѧѥϯ ӌϯѳ ϯƀӀ ʜѧџҁʌѧѣєӣɯџκ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ κѳґѳ ϯƴϯ ϯⱀѳʌʌџɯƀ ʍѧʍѧɯƴ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє єѣџҁƀ ʙ ґʌѧӡѧ ϯєʌκѧ џ ʙҁʍѧϯⱀџʙѧӣҁᴙ ʙ ҁʙѳџ ѳϯҁѳҁƀӀ ҁƀӀʜѳκ ɯʌѥχџ џʌџ ᴙ πⱀᴙʍ ӡđєҁƀ ѣѧɯκƴ ϯʙѧєӣ ʍѧϯєⱀџ ѳϯκⱀƴӌƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴҁκѳⱀᴙӣҁᴙ đѧʙѧӣ ҁƀӀʜџɯκѧ ɯʌѥχџ πⱀƀӀѱѧҁϯƀӀӣ ᴙ ϯʙѳѥ ʍѧʍѳӌκƴ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ đⱀƀӀѱєʜƀӀɯ κⱀџʙѳӡƴѣƀӀӣ ᴙ ѳӌκѳ ϯʙѧєӣ ʍѧϯєⱀџ ʜѧ ӡѧʌƴπƴ ҁʙѳѥ ʜѧϯᴙґџʙѧʌ ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧϯƀ ϯⱀѧχѧʌ ʙ ⱀƀӀґѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ӌϯѳ ϯƀӀ ʍѳѫєɯƀ ʜєʍѳѱʜƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯκʜџ єѣƴӌκƴ πƴґѧʌѳ єѣѧʜѳє ᴙ ϯʙѳѥ ʍѧϯƀ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁѧʌѳ ϯʙѧєӣ κѳҁѳʌѧπѳӣ ʍѧʍѧɯџ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳӌκѳʌџӡ єѣƴӌџӣ ʙƀӀπѳʌʜᴙӣ ʍѳџ πⱀџκѧӡƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌџӡƀӀʙѧӣ ʍѳџ ᴙӣҵѧ џ ʜє ʙѳӡʜџκѧӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌєϯ đѧχƴᴙ ѣѧӡѧⱀџɯƀ ҁƀӀʜ ɯʌѥχџ ҁϯᴙʜџ єѣƴӌκƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѧκ ѫє ϯƀӀ ӡѧєѣѧʌ ѣʌᴙđѳⱀƴκџӣ ҁƀӀʜ ɯѧʌѧʙƀӀ ѳϯҁѳҁџ ʍѳџ ᴙӣҵѧ џ ӡѧϯκʜџҁƀ ʜѧχƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєʌѳ ϯʙѳєӣ ʍѧʍѧɯџ κѧⱀѧѣєʌƀʜѳӣ ʍѧӌϯѳӣ єѣѧʌ ӌє ϯƀӀ ҁκѧѫєɯƀ ʍʜє ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍƴʌᴙ ɯѧʌѧʙѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧʌ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯκƴ ϯʙѳѥ ʙƀӀєѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџʌѧ єѣƴӌѧᴙ ҁѳҁџⱀƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌџⱀƴӣ ʍѳџ ᴙӣҵѧ ϯƴґѳđƴʍ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀєѣѧʌ ϯʙѳѥ ӌєⱀʜƴѥ ʍѧʍƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌʌєʜѳєđ єѣƴӌџӣ ґⱀƀӀӡџ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ʙƀӀєѣѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӌє ϯƀӀ πƀӀϯѧєɯƀҁᴙ ҁѧʍѳƴϯʙєⱀđџϯƀҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀʌѳʍѧѥ ϯʙѳџ ӡƴѣєɯκџ ґʜџʌѳєѣʌƀӀӣ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁⱀѧʌ ʙ ϯʙѳѥ ґʌѳϯκƴ ҁƀӀʜ ɯʌѥχџ ӌє ӡѧ ʙƀӀєѣѳʜƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѱє ҁѳҁџ ʍѳӣ ӌʌєʜ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ӡѧⱀєѫƴ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯᴙʜџ єѣѧʌƀʜџκ πџӡđѳʌѳѣƀӀӣ ҁƀӀʜ ϯʙѧⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ӌѧҁϯѳ ѳϯҁѧҁƀӀʙѧєɯƀ ҁƀӀʜ ɯʌѥχџ ӌє ⱀєɯџʌ џҁπѳʌƀӡѳʙѧϯƀ ҁʙѳџ ʜѧʙƀӀκџ ʜѧ πѳʌʜƴѥ κѧϯƴɯκƴ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡѧɯƴґѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ χʙѧϯџϯ ѳϯ ʍєʜᴙ ѣєґѧϯƀ κѧκ ϯєʌκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳӣ ҁѳҁѧʌƀʜџκ πѳⱀʙƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧⱀƴѣџʍ ϯʙѳѥ ґѳʙʜѳⱀƀӀʌƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ єѣєʍ πⱀѳҁƀӀπѧӣҁᴙ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧʙѧӣ πѳđϯѧѱџ ҁѥđѧ ҁʙѳє ҁѳπʌџʙє єѣʌџѱє ᴙ єґѳ єѱє ⱀѧӡ ϯⱀѧχʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧʜ єѣѧʌ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧʙѧӣ ҁѥđѧ πⱀџҁƀ ѣƴđєʍ ϯєѣє єѣƴӌκƴ ʙƀӀʙѳⱀѧӌџʙѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜѧ ʍѳєӣ ӡѧʌƴπє џ ӡѧґʌѳχʜєɯƀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ʙѧѻєʌƀʜѳґѳ πџđѳⱀѧҁѧ đѧʙѧӣ πџӡđƀӀ ʍѳʌӌѧ πѳʌƴӌѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴʍѳʌᴙӣ ʍєʜᴙ ӌϯѳ ѣƀӀ ᴙ ϯєѣє ҁʜѳʙѧ ʜє đѧʌ πџӡđƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀʙѧʌ ϯⱀƴπєɯʜџκ ϯʙѳєӣ ʍѧʍѧɯџ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙҁє ϯʙѳџ ⱀєѣⱀѧ ʙʍєҁϯє ҁ ӡƴѣѧʍџ πєⱀєʌѳʍѧѥ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌџҁϯѳ ʍѳӣ χƴӣ ѳϯҁѳҁєɯƀ ϯєⱀπџʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀєѣƴ ϯʙѳѥ ϯƴπѳⱀƀӀʌƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ӡѧϯκʜџ єѣѧʌƀʜџκ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ϯѧʍ πџӡđџɯƀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ єѣʌџʙƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳϯϯⱀѧχѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʌƴπƴ ѳѣҁѳҁџ ҁƀӀʜ ɯʍѧⱀƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀϯⱀѧχѧʌ ѳҁϯѧʜκџ ϯʙѳєӣ ʍѧʍѧɯκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџʌѧ єѣƴӌѧᴙ πѳʌџӡƀӀʙѧӣ ʍѳӣ χєⱀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ϯѧκ ӡѧʙєʌҁᴙ ҁƀӀʜ ɯʌѥχџ ᴙ ϯʙѳѥ ʍѧʍѧɯκƴ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯѳʌƀκѳ πѳπⱀѳѣƴӣ ʍʜє ϯƴϯ πⱀѳєѣѧϯƀ ҁƀӀʜ ɯʌѥχџ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌƀʜџκ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ҁπєⱀʍѳґʌѳϯ єѣƴӌџӣ ӌє ʌƀӀѣƴ đѧʙџɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯѧⱀѳєѣ єѣƴӌџӣ πѳκѧӡƀӀʙѧӣ ʜѧ ӌϯѳ ϯƀӀ ҁπѳҁѳѣєʜ χʙѧϯџϯ ѫⱀѧϯƀ ʍѳє ґѳʙʜѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯѧκѧʌ єѣƴӌџӣ πⱀџѫʍџҁƀ κ ʍѳєӣ ӡѧʌƴπє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳџ ӡƴѣєɯκџ ϯⱀѧχѧʌџ ϯєⱀπџʌѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧґѳʜџ ʍѳӣ χƴӣ ҁєѣє ʙ ѱєκџ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ѫџϯƀ ʜє đѧʍ ҁƀӀʜ ɯʌѥχџ ѣƀӀҁϯⱀєє ϯѧʍ πџɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳџ κⱀƀӀʌƀᴙ ѳѣⱀƴѣʌѥ ӌʌєʜѳʍ ҁƀӀʜ ɯʌѥχџ πєϯƴɯџʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ єѣѧʌ ʜƴ ʜє ҁƴϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѫƴӣ χƴӣ ʍѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πʌѧκҁѧ єѣƴӌѧᴙ χʙѧϯџϯ ѣєґѧϯƀ ѳϯ ʍєʜᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ƴѫє πѳ ґѧӡѧʍ đѧʌ ҁʌѧѣƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʙ ⱀƀӀʌѳ ҁʙѳӣ χƴӣ ӡѧκџʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ƴѫє ϯѧʍ ҁџđᴙϯ ʍѳѥ ҁϯⱀѧʜџӌκƴ ʌџҁϯѧєϯ ʙ ʜѧđєѫđє ӌϯѳ ᴙ єґѳ ʜє ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳӡѳⱀџѱє єѣѧʜѳє ӌʌєʜ ҁѳ ⱀϯѧ ʙƀӀʜƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣʌџѱє ϯʙѳє ѳϯϯⱀѧχѧєʍ ϯƴϯ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ⱀѳґѧ ʙ ѳѣⱀѧϯʜƴѥ ҁϯѳⱀѳʜƴ ʙπⱀѧʙʌѥ ϯєʌκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳϯҁѳҁєⱀ єѣѧʜƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳӣ ⱀѳϯ ϯⱀєӡʙѳ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣʌџѱє ӡѧѱєʌκʜџ ʙҁєʍ πѳχƴӣ ʜѧ ϯєѣᴙ ҁƀӀʜ ɯʌѥχџ ҁʍѧӡʌџʙƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡѧѱєκѧʜєҵ єѣѧʜƀӀӣ ƴϯⱀџ ҁʌєӡƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ӡƴѣƀӀ ʙƀӀѣƀѥ ӌєⱀʜѳѫѳπƀӀӣ ѧⱀʍᴙʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє πѳҁѳҁџ χƴӣ ҁʌѧѣƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѳϯҁѳҁџ ʍʜє ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє κѳπџⱀƴєɯƀ ʍѳӣ ҁϯџʌƀ ѫѧʌκџӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳ ӌєⱀđѧκƴ ϯʙѳєӣ ʍѧϯєⱀџ ӡѧʌƴπѳӣ ʙʍѧѫƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđџʌ ϯʙѳѥ ѣєⱀєʍєʜʜƴѥ ɯʌѥχƴ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀєʍ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯѧκ πѳđƴʍѧʌ џ ѳκѧӡѧʌѳҁƀ ӌϯѳ ʍѧʍѧ ϯʙѳᴙ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ϯƴχʜџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ѳπƴҁκѧӣ ⱀƴκџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєѣᴙ ʙєӡđє єѣѧʌџ πѳϯѳʍƴ ӌϯѳ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯƴϯ ҁκѳʜӌѧєɯƀҁᴙ ⱀѧʜѳ џʌџ πѳӡđʜѳ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜє πⱀᴙӌƀҁᴙ ʍƀӀ єѣѧɯџʌџ ϯє ʍѧʍѧʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙєҁƀ ϯʙѳӣ ҁƴʍʍѳҁѣⱀѳđ đєϯџɯєκ ɯʌѥχ ӌϯѳ ϯƀӀ ʜѧӡƀӀʙѧєɯƀ ҁєʍƀєӣ ƴʜџӌϯѳѫƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴӣ ѳϯҁѳҁџ ϯєⱀπџʌџѱє єѣƴӌєє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґѳϯѳʙƀҁᴙ ҁѳҁѧϯƀ ʍѳѥ ӡѧʌƴπƴ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πєⱀєҁѳҁʜџκ єѣƴӌџӣ ѧ ϯʙѳᴙ ʍѧϯƀ ɯѧʌѧʙѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙ ґʌѧʜđƀӀ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ єѣѧʌѳ єѣƴӌџӣ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯƴϯ ʍѳџ πʌєʙκџ ѣƴđєɯƀ ɯκʙѧʌѳʍ πⱀџʜџʍѧϯƀ ѳϯҁѳҁʜџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣѧʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ᴙ ϯєѣє ʙ ӌєⱀєπ ҁⱀѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ⱀєѧʌƀʜѳ єѣѧʜѧᴙ ϯєʌκѧ ӌϯѳ ϯƀӀ πƀӀϯѧєɯƀҁᴙ ϯƴϯ πѳκѧӡѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πⱀџ κѧѫđѳӣ ʙҁϯⱀєӌє ҁ ϯʙѳєӣ ʍѧʍѧɯєӣ єє ʌѳѣєɯʜџκ ҁϯѧʌκџʙѧʌ ҁѳ ҁʙѳєӣ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁъєѣѧʌҁᴙ ʙ ҁϯⱀѧχє ѳϯҁѥđѧ κƴⱀʌƀӀκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣƀӀҁϯⱀєє πџɯџ ҁƀӀʜ ɯʌѥχџ єѣѧʌџ ϯʙѳѥ ӌєⱀʜƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ đѧʙѧӣ ϯѧѱџ ҁѥđѧ ҁʙѳє єѣѧʌѳ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯҁѳҁџ ʍʜє ҁƀӀʜ ɯʌѥχџ џ ӡѧϯƀӀχѧӣ ҁʙѳє єѣʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡѧκⱀѳӣ єѣѧʌѳ џ πⱀџҁϯƴπѧӣ ѳϯҁѧҁƀӀʙѧϯƀ ʍʜє ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧҁѳҁџ ʍѳӣ χƴӣ ҁʙѳџʍ ѣʌᴙđҁκџʍ ⱀϯѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ѳϯҁѥđѧ ʙπєⱀєđ ʜѳґѧʍџ ʙƀӀʜєҁƴ ҁƀӀʜ ɯʌѥχџ ϯƀӀ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀƀӀґʌџѱєʍ ҁʙѳџʍ ӌʌєʜ ѳϯҁѳҁџ ʍʜє ϯƴϯ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѣƴӌџӣ ґⱀџѣѳκƴⱀ ӡѧʙѧʌџ єѣѧʌѳ џ ѳѣʌџѫџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ⱀєѧʌƀʜѳ ѳϯҁѳҁєⱀ єѣƴӌџӣ ҁ 2020 ґѳđѧ ӌϯѳ ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍƴ єѣєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ϯєⱀπџʌѧ ᴙ ϯʙѳѥ ʍѧϯƀ ʙƀӀєѣѧʌ ӌє ϯƀӀ ѳϯʍѧӡƀӀʙѧєɯƀҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ѻѧʜϯѧӡџᴙ ƴⱀѳʙʜᴙ πєⱀʙѳκʌѧҁҁʜџκѧ ѳϯҁѳҁџ ʍѳѥ ӡѧʌƴπƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѧʌѧѣѧӣ єѣѧʜƀӀӣ ӡѧʙѧʌџ єѣѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌџ ϯƴϯ ʜє ⱀѧҁҁʌѧѣʌᴙӣҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡƴѣƀӀ ϯєѣє πєⱀєʌѳʍѧѥ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀєѣєʍ ϯʙѳѥ ӌєⱀʜѳѫѳπƴѥ ʍѧʍѧɯƴ ɯʌѥχƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳӣ ⱀѳϯ єѣѧʌ ѳҁєʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκⱀѳӣ χѧʙѧʌѳ ƴ ϯєѣᴙ ʍѧʍѧɯѧ ɯʌѥχѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣᴙ ҁƀӀʜκѧ κѧʌѣџϯѧ єѣѧʜѳґѳ ʙʜѧϯƴⱀє ʜѧ ҁʙѳѥ ӡѧʌƴπƴ ҁѧđџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ɯʌѥχѧ πџđѧⱀѧҁџʌџ ѱєʜᴙⱀѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ʙƀӀєѣєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧӡ đʙѧ ϯⱀџ ӌєϯƀӀⱀє πᴙϯƀ ϯⱀѧχѧʌ ϯʙѳѥ ɯʌѥχƴ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳđџʜ χƴӣ ᴙ ϯєѣє ҁѳҁѧʌƀʜѥ ϯƴϯ ʙƀӀϯⱀѧχѧѥ џ ϯƀӀ πѳϯєⱀᴙєɯƀ ҁʙѳє єѣʌџѱє ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣʌџӡƀӀʙѧӣ ʍѳџ ᴙӣҵѧ ϯƴπєʜƀκџӣ ҁƀӀʜџɯκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳϯⱀѧχѧʌ χѧⱀκѧʌѳ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ ҁϯџʌє ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєɯκѧ єѣƴӌѧᴙ ʜє ѣєґѧӣ ѳϯ ʍєʜᴙ ʙҁє ⱀѧʙʜѳ πџӡđƀӀ πѳʌƴӌџɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳџ κⱀƀӀʌƀᴙ ʙƀӀⱀʙƴ џʜđєєҵ єѣѧʜƀӀӣ ѣƴđєɯƀ ѳϯ ʍѳєӣ ӡѧʌƴπƀӀ ѣєґѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧɯѧ єѱє ϯѧ ɯʌѥχѧ ӌєʍƴ ϯƀӀ ƴđџʙʌᴙєɯƀҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧѣƴđƀ πⱀѳ ϯⱀѳʌʌџʜґ đєʙӌѳʜκѧ єѣѧʜѧᴙ ϯєѣᴙ ӡđєҁƀ κѧѫđƀӀӣ πџʜѧϯƀ ѣƴđєϯ κѧκ єѣѧʜѳґѳ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍєϯⱀѳʙƀӀӣ ѫєӡʌ ʙ πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ ʙҁϯѧʙʌᴙʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ʜѧ ӌʌєʜє κѧκ ѥʌƴ ⱀѧҁҁκⱀƴӌџʙѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє đѳ ҁџχ πѳⱀ ҁѥđѧ πџɯєɯƀ ҁƀӀʜ ɯʌѥχџ? κѳπƀӀϯѧ ѳϯ κѳʜѻƀӀ ƴѣєⱀџ ϯєⱀπџʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ πⱀѳҁϯџϯƴϯκџ єѣƴӌџӣ χʙѧϯџϯ ʍєʜᴙ ϯєⱀπєϯƀ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѣƴđєɯƀ πⱀѳҁџϯƀ ʍєʜᴙ ӌϯѳѣƀӀ ᴙ ѳҁϯѧʜѳʙџʌҁᴙ џ ʜє πџӡđџʌ ϯʙѳє đƀӀⱀᴙʙѳє єѣʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєӌѧϯѧӣ ѣƀӀҁϯⱀєє ϯєʌκѧ єѣѧʜʜѧᴙ ᴙ ϯʙѳѥ ʍѧϯƀ ʙ ѫѳπƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ѱєκџ єѣѧʌ ϯєʌκѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯƴґѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ ӌʌєʜѳπⱀџєʍʜџκ єѣѧʜƀӀӣ ᴙ ϯєѣє ʍѧϯƴɯκƴ ϯʙѳѥ єѣѧʌ ҁʌѧѣѧκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ѣѳʍѣџ đѧʙѧӣ ѧʌѣѧʜєҵ єѣƴӌџӣ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ џӡ ѳκʜѧ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ʙ ѳӌκѳ ӌєⱀєӡ ѣѧʌκѳʜ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ χѳʌѳđє ʍѳӣ ӌʌєʜ ѳϯҁѧҁƀӀʙѧʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ χѧⱀѧɯѳ єѣѧʌ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ҁƀӀʜѳκ ɯʌѥχџ πⱀџӡєʍʌџҁƀ ҁʙѳџʍ ᴙӡƀӀκѳʍ ʜѧ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ʜѧ ҁєκҁ ⱀѧӡʙєʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ πⱀџ ϯєѣє єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ ʙєⱀɯџʜє ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧӡđѳʌѣџʌ ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ χƴӣ ҁѳҁѧʌѧ ʙҁєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣƀѥ ϯʙѧєӣ ʍѧʍє ʙ ʌѳѣ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʙ ѳđєѫđє єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳєӣ ӡѧʌƴπє κѧϯѧєϯҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳᴙ ʙ ҁʙѳє ҁʙџʜѳє ⱀƀӀʌѳ χƴџ ѣєⱀєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯʙєӌѧѥ ʍѧϯƀ єѣѧʌ ϯʙѳѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁєӣ ⱀѳϯѳӣ ϯʙѳѥ ϯѳʌҁϯƴѥ ʍѧʍѧɯƴ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ єѣѧʌѳ ʍѳѥ ҁπєⱀʍƴ πⱀџʜᴙʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ⱀѳϯѧʜ ѣєⱀєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѧѥ ѣʌѳχѧҁϯƴѥ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӡѧʌƴπѳӣ ѳҁʌєπџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ҁѳѣѧκƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳҁѳҁџ ѣʌᴙđҁκџӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧ ϯʙѳᴙ χƴӣ πѳҁѳҁѧʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ӡѧʌƴπє κⱀƴϯџϯҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ӡѧʌƴπѳӣ ҁκⱀƴϯџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѧѥ єѣѧʌ πѳʍⱀџ ƴѫє ҁƀӀʜѳκ ʍⱀѧӡџ єѣѧʜѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʙ ʍѳџχ ᴙӣҵѧχ ӡѧѣџʌҁᴙ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ χƴєʍ єѣѧɯƴ κѧκ ґⱀƴɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌѧѣƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ χƴӣ ҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ πѳⱀᴙđκє ѫџʙѳӣ ѳӌєⱀєđџ єѣѧʌ ʍѧϯƀ ϯʙѳѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѧѫđƀӀӣ đєʜƀ ϯʙѳᴙ ʍѧʍѧɯѧ ѳϯҁѧҁƀӀʙѧʌѧ ʍѳӣ χƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯєⱀџ ϯʙѳєӣ πѳđ ґʌѧӡѧ κѳʜӌџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ єѫєҁєκƴʜđʜѳ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍѳχʜѳѣʌᴙҵκѳє πџӡđѧёѣџѱє κѳϯѳⱀѳє ѳϯҁѧҁƀӀʙѧʌѳ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳχѳⱀѳʜѥ ӡѧѫџʙѳ ϯʙѳѥ єѣѧʜƴѥ ҁєʍєӣκƴ ҵƀӀґѧʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀϯⱀѧχѧʌџ πѧϯʌџɯκџ ϯʙѳєӣ πʌѳҁκѳєѣʌѳӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁϯѳӣʌѳ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ϯƀӀ ҁʌѧѣєʜƀκџӣ ҁƀӀʜ ɯʌѥχџ πѳκѧѫџ ѻѧʜϯѧӡџѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀєӡѧʌ ϯⱀƴπʌџѱє ϯʙѳєӣ ҵƀӀґѧʜҁκѳӣ ɯʌѥχє ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧđєʜƴ ґѳⱀɯѳκ ʜѧ єѣʌџѱє ϯʙѳєӣ ӌƴⱀκџ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџʌѧ єѣѧʜѧᴙ ʜѧπџҁƀӀʙѧӣ ҁκѳⱀєє πѳκѧ ᴙ ϯʙѳѥ ʍѧϯƀ ʜє ʙƀӀєѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џɯѧӌџʌџ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧʍƴʌѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџɯʙѧⱀϯƴѥҁƀ ӡѧʌƴπѳӣ κ єѣʌџѱƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁκⱀƀӀʙѧʌџ κⱀƀӀɯκƴ ґⱀѳѣѧ ϯʙѳєӣ ʍѧʍѧɯџ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєđѧʌџ ϯʙѳєӣ ʍѧʍѧɯџ ѳϯκⱀƴӌƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ɯϯƴⱀʍѳʙѧʌџ χѧⱀκѧʌџѱє ϯʙѳєӣ ʍѧʍѧɯџ ӡѧʌƴπѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κџđѧʌ ӡѧʌƴπƴ ʙ κѧѣџʜƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀⱀƀӀʙѧʌ πѧϯʌƀӀ κѧѫđѳґѳ ҁƀӀʜκѧ ɯʌѥχџ џӡ ϯʙѳєӣ ѳѣѱџʜƀӀ đѳʌѣѧєѣѳʙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ɯѧѣѧɯџʌџ ⱀƀӀʌƀʜџκ ϯʙѳєӣ πѳʌƴπѳκєⱀҁκѳӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџʌѧ ёѣѧʜѧᴙ đѧʙѧӣ πџɯџ ⱀєѱє ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁϯѧʜҵƴӣ ʜѧ ʍѳєӣ ӡѧʌƴπє ѱєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʙҁє κѳҁϯџ πєⱀєʌѳʍѧѥ χѧӌџκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєⱀєκⱀѧҁџʍ ϯʙѳє χѧӌєʙҁκѳє єѣʌџѱє ѣѧⱀѧʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ ӡƴѣƀӀ ϯʙѳєӣ ʍѧʍѧɯџ ҁ ʜѳґџ ʙʌєϯѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳⱀѳʙѳӡџκѳʍ ӡѧʙѳӡџʌџ ӡѧʌƴπƀӀ ʙ ⱀѳϯ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱєʜᴙⱀѧ єѣѧʜѧᴙ πѳӌџҁϯƀ ҁʙџʜѧⱀʜџκ ҁʙѳєӣ ʍѧʍѧɯџ ҁʙѳџʍ ᴙӡƀӀκѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳ ϯʙѳџʍ ʙџҁʌѳƴχџʍ ƴɯѧʍ πⱀѳєχѧʌџҁƀ ӡѧʌƴπѧ đѳʌѣѧєѣ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁⱀѧʌ ʙ ʜѳҁѳґʌѳϯκƴ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙƀӀҁϯєґʜƴ ϯʙѳѥ ґѳʌѳӡѧđƴѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ѱєʜѳκ єѣƴӌџӣ ᴙ ϯєѣє κѳҁϯџ ʙƀӀđєⱀʜƴ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʙʜѧϯƴⱀє џɯѧκ єѣƴӌџӣ ʙѳӡџ ʍѳѥ ӡѧʌƴπƴ ʜѧ ҁʙѳєʍ ґѳⱀѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ κⱀƀӀɯκє ґⱀѳѣѧ ϯʙѳєӣ ʍѧϯєⱀџ πѳҁⱀѧʌ џ ӡѧҁϯѧʙџʌ ϯєѣᴙ ϶ϯѳ ʙҁє ҁѳѫⱀѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєӡѧʌџ ʍџʜџ єѣʌѳ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀƀӀѫџӣ ҁƀӀʜ ɯʌѥχџ πѳκѧѫџ χѳϯƀ ѳđʜƴ πⱀџӌџʜƴ πѳӌєʍƴ ᴙ ʜє đѳʌѫєʜ ϯⱀѧχѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ѳѣџѫѧӣҁᴙ ҁƀӀʜѳκ ɯʌѥχџ ᴙ ʙҁєґѳ ʌџɯƀ ϯѳ πєⱀєʌѳʍѧʌ κѳʜєӌʜѳҁϯџ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ѳϯⱀєѫƴ ґѳʌѳʙƴ ϯʙѳєӣ ʍѧϯєⱀџ џ ʜѧҁѧѫƴ ʜѧ ҁʙѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ҁєҁϯⱀƴ єѣѧʌ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳđ ʍƴӡʌѳ џӡ ʍѧґʜџϯѳѻѳʜѧ ϯʙѳѥ ʍѧʍѧɯƴ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙєⱀʜƴʌҁᴙ ӌϯѳ ѣƀӀ ʙƀӀєѣѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѳӣ ҁєѣє ʍѳґџʌƴ єѣƴӌџӣ ʍƴχϯѧⱀ ᴙ ϯʙѳѥ ҁєʍƀѥ đєϯєӣ ɯʌѥχ ƴʜџӌϯѳѫƴ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯⱀƴπџѱє ґʜџʌѳє ѫџʙƀӀʍ ѳϯҁѥđѧ ʜє đѧɯƀ πѳ ϯѧπκѧʍ ʍⱀѧӡƀ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ đʙѧ ӌʌєʜѧ ϯʙѳѥ ⱀѳѫƴ πѳđҁѧđџʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʜѧ єѣѧʌѳ κѧʍɯѳϯ ѱѧҁ ҁκџʜƴ χƴєϯѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ҁ ʍѳџʍ χƴёʍ ƴ ҁєѣᴙ ʙ ґѳⱀʌє χѳđџɯƀ πⱀѳҁϯƴɯκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ѣѧѣƴɯκє πѳ χⱀєѣϯƴ ʜѧκѳҁϯƀӀʌᴙѥ ҁƀӀʜ χƴӣʜџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґѳʜџ ҁѥđѧ єѣѧʌƀʜџκ ҁʙѳєӣ ʍѧʍƀӀ ᴙ єґѳ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ҁʙѳєӣ πѧҁϯƀѥ ʙ ʍѳёʍ χƴє ƴϯѳʜƴʌ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϶ϯѳ ӡѧ ѻѧʜϯѧӡџᴙ ƴⱀѳʙʜᴙ ʜƴʌёʙκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʌѳѫџ χƴӣ ҁєѣє ʙ ѫѳπƴ ґѳʍѳҁєκ єѣʌџʙƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯѧκ ґʌᴙđџ џ ӌʌєʜ ѳϯҁѳҁєɯƀ ᴙ ƴʙєⱀєʜ ѧχχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯƀӀ ӌє ʜѧ ʍѳєӣ ӡѧʌƴπє ϯѳ ӡѧѣƀӀʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ʍѧϯκƴ ⱀѧӡⱀƀӀʙѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ӌє ʍѧʍƴ ϯʙѳѥ єѣѧϯƀ ѣƴđєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧχƴӣ ϯƀӀ ʌєӡџɯƀ ϯƴđѧ ґđє ϯʙѳѥ ʍѧʍƴ πѳ κⱀƴґƴ πƴҁϯᴙϯ џ κѧѣџʜƴ єӣ ⱀѧӡъєѣƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱѧҁ ϯʙѳѥ ʍѧϯєⱀƀ ʜѧ ҁπџʜє ƴ ϯєѣᴙ ʙƀӀєѣєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ πѳ ҁϯєʜκџ ґѳⱀʌѧ ʙʙєⱀχ ϯѳⱀʍѧɯκѧʍџ đⱀѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ᴙӣҵѧʍџ πѳ ɯєє χƴᴙⱀџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙҁѥ ϯʙѳѥ ҁєʍƀѥ đѳ єđџʜѳґѳ πѳχѳⱀѳʜѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳӣ χƴӣ ʙ ʍѳⱀđƴ ϯʙѳєӣ ʍѧʍє ҁπєⱀʍѳӣ πѳ χⱀѥʜđєʌѥ ѣџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ӡѧҁƀӀπѧӣ ϯѧʍ ҁƀӀʜ χƴӣʜџ ҁџđџ ϯƴϯ ʙҁѥ ҁʙѳѥ ʙƀӀđєⱀѫκƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ӌʌєʜѳʍ πѳ πџӡđє ϯʙѳєӣ ʍѧʍє ʙѳѫƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє ӡѧ ҁƀӀʜѧ ɯʌѥχџ ӡđєҁƀ ѳϯʙєϯџɯƀ ʜѳʙџӌѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ѱѧҁ ʌѳҁᴙ πⱀѳѣƀѥ єѣʌѳ ѧχƴєʙɯѳє </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʌƴӌɯє ʜє ҁπⱀѧɯџʙѧӣ ӌє ƴ ϯʙѳєӣ ʍѧʍƀӀ πџӡđѧ џ ⱀѳϯ ѣѳʌџϯ ӼѦӼѦӼѦ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳґƴ ҁʍєʌѳ ҁκѧӡѧϯƀ ӌϯѳ ᴙ ϯʙѳєӣ ʍѧʍє ⱀѳϯ ⱀʙѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍƴ ϯʙѳѥ ⱀѧӡѳⱀʙѧʌѳ ѳϯ ʍѳєӣ ҁπєⱀʍƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳӣ ɯєӣʜƀӀӣ πѳӡʙѳʜκџ ϯⱀѧχʜƴ ϯƀӀ ӌє ⱀєκҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѥđѧ џđџ џʍѣџҵџʌ єѣƴӌџӣ ᴙ ϯєѣє єѣѧʌѳ ʜѧѣƀѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣєӡƀᴙʜѧ єѣѧʜѧᴙ ѱѧҁ ϯєѣᴙ ʙ κʌєϯκƴ πѳҁѧđџʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣⱀѧѱѧӣҁᴙ ҁ ʍѳџʍ χƴёʍ κѧκ πѳʌѳѫєʜѳ, đєϯё ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴπʌџϯѧӣ ʍѳӣ χƴӣ ҁєѣє ӡѧ ѳѣє ѱєκџ ⱀѧҁπѧɯёʜκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєʍ ʙⱀєʍєʜєʍ ᴙ ϯʙѳѥ ʍѧϯƀ ƴѫє ʙƀӀєѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ ʙҁє ⱀѧʙʜѳ ӌϯѳ πʜƴϯƀ ʍƴҁѳⱀʜƀӀӣ ѣѧκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧѣєӣ ᴙ ʍѧʍƴ ϯʙѳѥ đⱀѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʙ ѣѳɯκƴ ҁ ʜѳґџ ӡʙєӡđѧʜƴ χƴєπƴϯѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌƴӌѧӣ πѳ ʍѧҁκє ґⱀєѣєʜƀ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđѧκ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀⱀʙѧʌѳ ʜѧχƴӣ ҁƴκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁ ґѧʜđѳʜѳʍ єѣѧʌ ϯʙѳѥ ʍѧʍƴ ӌƴⱀκƴ ӡѧϯⱀёπѧʜƴѥ ҁπџđѳӡʜƴѥ ɯʌѥχƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀʙєʍ ʜѧ ϯⱀᴙπκџ ϯʙѳѥ đєϯҁκƴѥ πҁџχџκƴ χѧχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ϯєʌκƴ ϯⱀѧχѧʌ πѳκѧ ϯƀӀ ҁπѧʌ κƴκѳʌđ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣʌџѱє ϯʙѳєʍƴ πѧπѧɯє ʍєӌƴ κƴҁκѧʍџ ҁπєⱀʍƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳё πѳϯʜѳє єѣʌѳ ʜѧ ӌʌєʜᴙⱀƴ ʜѧϯᴙʜƴ χⱀѥκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌџҁϯѳ ʙ ϯʙѳё ѳѣχѧⱀκѧʜѳє χѧӌєʙҁκѳє ⱀƀӀʌѳ ҁҁƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ƴʍєⱀʌѧ ϯʙѳᴙ ʍѧϯƀ єѣƴӌѧᴙ ɯѧѣѳʌđѧ κѧκ ɯѧʙκѧ πѳđӡѧѣѳⱀʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ κѳҁϯџ ʜѧ ʍѳʌєκƴʌƀӀ ⱀѧҁπџđѳⱀѧҁџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧⱀκѧʌџѱє ϯʙѳєӣ ʍѧʍƴʌџ πџđѳⱀѧҁџʍ ƴ ϯєѣᴙ ʜѧ ґʌѧӡѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧɯƴ ϯᴙ ѱєʜκѧ єѣѧʜѳґѳ πѳ πѳӌκѧʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѳҁϯџ ϯʙѳџ ʜѧ đⱀѳʙѧ κџʜєʍ ҁʌѧѣѧκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌёϯєʜƀκѳ χƴᴙⱀџʍ ϯᴙ ѱєґѳʌ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѳⱀѳϯƀӀɯκѧ ӡʌѳєѣѧʜƀӀӣ ѳϯҁѳҁџ χƴӣ ʍʜє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ єѣѧʌѳ ʜѧχƴᴙⱀѥ ϯє ҁπєⱀʍѳӣ ʜѧχƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳ єѣʌƴ ϯʙѳᴙ ʍѧϯƀ ϯєⱀπџʌѧ ɯʌѥχѧҁϯѧᴙ πѳʌƴӌѧєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌєⱀκѧɯ ϯƴѧʌєϯʜƀӀӣ єѣѧʌѳ ӡѧκⱀѳӣ ѳϯҁѳҁʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ѫѧχʜєʍ ƴϯєʜѳκ ӡʌѳєѣѧʜƀӀӣ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁ ʙєⱀϯƴχџ ϯʙѳӣ єѣѧʌƀʜџκ ҁʜєҁƴ ҁƀӀʜ ɯѧʌѧʙƀӀ ѣʌᴙđҁκџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍєѫ đʙєⱀєӣ ӡѧѫʍƴ єѣʌџʜƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѳ ϯѧʌѳґѳ ѣƴđƴ ϯʙѳє єѣʌџѱє ʍᴙϯѳє χƴᴙⱀџϯƀ ѱєґʌџʜѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѧⱀӌєʌƀʜџκ ϯʙѳӣ ʜѧπџӡѫєʜʜƀӀӣ đѳ ҁџʜᴙκѳʙ ϯƴϯ ʜѧєѣѧɯƴ ⱀєκҁ єѣƴӌџӣ ʜѧχƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ɯʌѥχƴ ʍєⱀϯʙƴѥ ҁѳѫⱀƴ đѳʌѣѳєѣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєӌєʜƀ ϯʙѳєӣ ʍѧϯєⱀџ ӡѧʌƴπѳӣ ƴѣƀѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁџҁƀκџ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ ʙƀӀⱀʙєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ πєⱀєκѳɯєʜƀӀӣ ᴙӣҵѧ ʍѳџ ѳѣʌџӡƀӀʙѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ҁƀӀʜѳκ ɯʌѥχџ ӌєⱀʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєⱀđѳʌџʌ ϯʙѳѥ ʍѧʍѧʜƀκƴ ɯʌѥχƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧӡѳⱀʙєʍ ѱєʜκѧ єѣƴӌєґѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ɯѧʌѳπѧӣ єѣƴӌџӣ ҁѳҁџ ʍѳӣ ӌʌєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌєπѳɯѧⱀѧ ⱀѧӡƴӣ ґʌѧӡѧ ᴙ ϯʙѳѥ ʍѧϯƀ єѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯѧʍ ʙ ҁϯⱀѧχє πєⱀєđ ʍѳʜџϯѳⱀѳʍ ѣƀєɯƀҁᴙ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κʌџκʜєʍ πѳ єѣѧʌƀʜџκƴ ϯʙѳєӣ ʍѧϯєⱀџ ӌʌєʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁѧѫƴ κѳʌ ʙ πџӡđƴ ϯʙѳєӣ ѫџⱀʜӣѳ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʌџ ϯʙѳѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀѳѣџʌ ɯєѥ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜѧ ɯʌѥχџ ϯƴϯ đѳ ҁƴџҵџđѧ đѳʙєđєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳӡƀʍџ ʍѳӣ χƴӣ ʙ ⱀѳϯ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯєⱀπџ ʍєʜᴙ ҁƀӀʜ ɯѧʌѧʙƀӀ ѳϯъєѣѧʜʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀʙєʍ ϯⱀƴπ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џӡʜѧҁџʌѳʙѧʌџ ʙҁє ϯʙѳє πѳκѳӣʜѳє ҁєʍєӣϯʙѳ đєϯџɯєκ ɯʌѥχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʌѳƴҁκџʌƀʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ᴙ ϯʙѳє ⱀƀӀʌџѱє χѧⱀκѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁʌѧѣƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ᴙ ϯʙѳё ⱀƀӀʌѳ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ đƴɯєʜκƴ ʙƀӀєѣƴ џɯѧκ єѣѧʜʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙϯѳπџʍ єѣƴӌκƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌϯѳ ҁ ϯѳѣѳӣ ҁƀӀʜ ɯʌѥχџ πџɯџ ⱀєѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѳʌѣџ πѳ κʌѧʙџɯѧʍ πѳκѧ ᴙ đѳʌѣʌѥ ϯʙѳѥ ʍѧʍѧɯƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χⱀѥκѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁ πƀӀⱀѧ ʙъєѣƴ ϯʙѳєӣ ʍѧʍѧɯє πѳ єѣƴӌκє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ πѳѫџʌƴѥ ʍѧʍѧɯƴ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳєѣƀӀʙѧєʍ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳϯⱀџ ҁʌєӡƀӀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳџ κѳҁϯѳӌκџ ʌѳʍѧʌџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍѳєӣ χѧⱀӌѳӣ ѣƴđєɯƀ ƴʍƀӀʙѧϯƀҁᴙ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳⱀєӡѧʌџ ϯʙѳѥ ʍѧʍѧɯƴ ʜѧ ⱀєʍʜџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ʙ єє ґʌѧӡѧ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ӡѧϯκʜџ єѣѧʌƀʜџκ ҁƀӀʜѳӌєκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁκѧѫџ ӌϯѳ ʜџѣƴđƀ ʙ ѳϯʙєϯ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡƴѣƀӀ ϯʙѳєӣ ʍѧʍѧɯџ κⱀѳɯџʌџ ѱєґʌєʜƀӀɯ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҵєπџҁƀ ʙ ʍѳѥ ӡѧʌƴπƴ ʍƴχϯѧⱀєʜƀӀɯ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀđєⱀʜƴ κѳʜєӌʜѳҁϯџ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʍєʌџ κѳҁϯџ ϯʙѳєӣ ʍѧϯєⱀџ ʙ ϯʙѳє ⱀƀӀʌџѱє ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ ʍѳӡґџ ϯʙѳєӣ ʍѧϯєⱀџ χѧⱀκѧʌ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜѧџҁʌѧѣєӣɯџӣ ҁƀӀʜ πџđѳⱀѧҁѧ ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍκƴ ʙ πџӡđѧκ єѣѧʌ ґʜџʌѳєѣκѧ ϯƀӀ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀѳѣџʌ ґѳʌѳʙƴ ϯʙѳєӣ ʍѧʍѧɯџ κѳʌєʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ҁʙѳѥ ѻѧʜϯѧӡџᴙ ӌєⱀϯᴙґѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁʌџϯƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ҁƴκѧ ӌƴⱀѣѧʜ єѣѧʜƀӀӣ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ӌџҁϯѳ ʙƀӀєѣƴ џ ʙƀӀκџʜƴ єѣѧʜƀӀӣ ϯƀӀ џɯѧκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ χƴєҁѳҁκƴ ӡѧπџӡđџʌ ҁʙѳџʍ ӌʌєʜѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ χƴєπʌєϯ єѣƴӌџӣ ʙϯƴʌџҁƀ ҁʙѳџʍ ⱀƀӀʌѳʍ ʙ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡʜѧєɯƀ ӌϯѳ ϯʙѳᴙ ʍѧϯƀ ʜєѳđʜѳκⱀѧϯʜѳ ʜѧⱀƴɯѧʌѧ πⱀѧʙџʌѧ đѳⱀѳѫʜѳґѳ đʙџѫєʜџᴙ џ ӡѧ ϶ϯѳ ѣƀӀʌѧ ʜѧκѧӡѧʜѧ ʍѳџʍџ ᴙӣҵѧʍџ ѳѣ ҁʙѳӣ єѣѧʌƀʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χⱀᴙѱџκџ ϯʙѳєӣ ʍѧϯєⱀџ єѣѧʌ ѱєґѳʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ѳґⱀєʌ ӡѧʌƴπѳӣ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁѳҁʜƴʌѧ ʍʜє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѧѥ ʍѧʍƴ ʙ ѳӌκѳ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍƴʌƀκƴ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѧᴙ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ πєⱀđѳʌџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣʌᴙ ѣƴđƴ ϯʙѳᴙ ʍѧʍѧɯѧ ʍѳџ ᴙӣҵѧ ʌџӡѧʌѧ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ҁʌѧѣѳґѳ ҁʌѧѣѳґѳ ҁƀӀʜѧ ɯʌѥχџ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ʍѳѥ ӡѧʌƴπƴ ҁѳҁєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϶ϯѳґѳ ѱєʜκѧ ʜѧ ӌʌєʜ ʜѧҁѧđџʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ đѳʌѣџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌѧѣƀӀӣ ҁƀӀʜ ɯʌѥχџ ҁѳҁџ χƴӣ ʍѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѧѥ ӡѧʌƴπѳӣ ѳϯπџӡđџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳєӣ ʍѧʍѧɯє χƴєʍ ѣѧɯʜѥ ҁʜєҁ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳᴙ ʜѧ ʍѳєӣ ӡѧʌƴπє ӡѧґʌѳχʜєϯ ҁʌƀӀɯƀ ҁʌѧѣƀӀӣ ҁƀӀʜѳκ ɯʌѥχъџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ѣѧӡѧⱀѥ ϯƀӀ ѳϯҁѥđѧ ʙƀӀӣđєɯƀ ҁ πⱀѳѣџϯƀӀʍ єѣѧʌƀʜџκѳʍ ѱєґѳʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ʙ ґʌѧӡѧ κѳʜӌџʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧ ѱєκџ ϯʙѳєӣ ʍѧʍѧɯє ʜѧκџđѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁϯѧʙѧӣ ҁƀӀʜѳκ ɯʌѥχџ ᴙ ϯʙѳџ κѳҁϯџ ʌѳʍѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ҁʌѧѣѧκ ᴙ ϯʙѳѥ ʍѧϯƀ ʙ ʜѳҁ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ѳѣѳґⱀєʙѧϯєʌєʍ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ κѧʌџϯκє єѣѧʌ ʍѧϯƀ ϯʙѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ӡѧѣѳⱀџʜѳӣ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴᴙӌƴ ʙ ѳӌκѳ ϯʙѳѥ ʍѧʍƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ҁπєⱀʍѳӣ ϯѳπʌѥ ҁʌƀӀɯџɯƀ ѱєʜᴙⱀѧ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ ϶ϯѳӣ κѳʜѻє ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀᴙʍѳ ϯƴϯ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѳґѳӣ ʙ πџӡđƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳєӣ ӡѧʌƴπє ѳґʌѳχʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ѳґʌƴɯџʌ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌ џ 4є  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍƴ πⱀѳҁϯѳ ϯѧκ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ χƴєʍ єѣѧʌ χѧѧχѧχѧχѧχѧχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ӡѧґʌѳχʜџ ϯƴϯ ҁʌѧѣƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ʍѧϯƀ ϯʙѳᴙ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌѧҁϯѳ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳ ӌєҁϯʜѳʍƴ ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣѧӡѧⱀѥ ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѳϯ ʍѳєӣ ӡѧʌƴπƀӀ ƴѫє ӡѧџκѧєϯҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣđџϯєʌƀʜѳ єѣѧʌ ʍѧϯƀ ϯʙѳѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧʌ ʍѧʍƴ ϯʙѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳѥ ӡѧʌƴπƴ ѳϯҁѧҁƀӀʙѧʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴӣ ʍʜє ҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѧҁѧҁєɯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ʙєʜƀӀ ӡѧʌƴπѳӣ ʙҁκⱀƀӀѳ ҁʌƀӀɯџɯƀ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧѥ ϯєѣᴙ ʙ єѣʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ χƴӣ ҁѳҁєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍџʌʌџѳʜ ⱀѧӡ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ ʍѳєӣ ӡѧʌƴπѳӣ πⱀѳκѧϯʜџҁƀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧϯƀ ϯʙѳѥ πѳ đєѻѳʌϯƴ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍƴʌƀκƴ πҁџʜƴ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ πѳđѳκѳʜџκє χƴӣ ҁѳҁєϯ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ πѳκѧʌєӌџʍ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀѳϯκʜєʍ єѣʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ κѳπƀᴙʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѧʌѧʍџʌџ ϯʙѳѥ ʍѧʍѧӡєʌƀκƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯⱀѧχѧʌ ƴɯџ ϯʙѳєӣ ʍѧʍѧɯџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜѳκ ɯʍѧⱀƀӀ ϯƴπѧʜџ єѣѧʌƀʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѣƴđєɯƀ ʙєӌʜѳ ѳϯχʙѧϯƀӀʙѧϯƀ ʙ ҁѳҁѧʌѳ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʜѳѣđџʌџ ʍѳⱀđƴ ϯʙѳєӣ ʍѧϯєⱀџ ӡѧʌƴπѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ πѳʌƴπѳκєⱀ єѣƴӌџӣ ӌʍѳκʜџ ʍѳӣ ӌʌєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴϯⱀџ ҁʌёӡƀӀ ҁƀӀʜѳκ ɯʌѥχџ ʜєʍѳѱʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ϯⱀᴙҁєɯƀҁᴙ ҁƀӀʜ ɯʌѥχџ đѧκ єѱє џ ҁѳ ʍʜѳӣ ϯƴϯ πƀӀϯѧєɯƀҁᴙ χƴᴙⱀџϯƀҁᴙ ϯƀӀ ʙʜѧϯƴⱀє πѳκѳӣʜџκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ɯʌѥχƴ єѣѧʜƴѥ ϯⱀѧχʜƴ ϯѧκ ӌϯѳ ƴ ʜєє ʙѧⱀєʜџκ ʙƀӀʌєӡєϯ ʙ ѳѣⱀѧϯʜƴѥ ҁϯѳⱀѳʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κʌџϯѳⱀ ϯʙѳєӣ ʍѧϯєⱀџ πѳⱀʙƴ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ đⱀџҁϯѳєđ єѣƴӌџӣ ѳ κѧκѳʍ єѣѧɯџʌѳʙє ϯƀӀ ґѳʙѳⱀџɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧƴ ѣѧⱀѧʜ єѣƴӌџӣ ϯƀӀ πєӌѧϯѧϯƀ ʜє ƴʍєєɯƀ πⱀѳ κѧκѳӣ ʜѳʜ ҁϯѳπ ϯƀӀ ґѳʙѳⱀџɯƀ ҁƀӀʜ ɯѧʌѧʙƀӀ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳπѧđѧӣ πѳ κʌѧʙџɯѧʍ єѣƴӌџӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџҵєʌѥҁƀ ҁʙѳєӣ ӡѧʌƴπѳӣ ʙ ʌѳѣєɯʜџκ ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁκʙѳⱀєɯʜџκ ϯʙѳєӣ ʍѧʍѧɯџ χƴєʍ ⱀѧӡѳⱀʙƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱєʜκƴ ⱀƀӀʌѳ πѳⱀʙѧʌџ ѳʜ ҁџđџϯ ҁʌєӡƀӀ ʌƀєϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁʙѳџ κѳπєӣκџ ϯƴϯ ҁѳʌƀєɯƀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯƴϯ ѣƴđƴ đѳ ѣєҁκѳʜєӌʜѳҁϯџ ϯⱀѧχѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ᴙӣҵѧʍџ ӡѧđƴɯƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κϯѳ ϯѧκѳӣ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣʌџӡƀӀʙѧӣ πѧⱀѧɯƴ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯκʜџ єѣѧʌƀʜџκ đᴙϯєʌ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѧѻʌєⱀ єѣƴӌџӣ πⱀџҁѳҁџҁƀ κ ʍѳєʍƴ ӌʌєʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πᴙʌџʍ ϯʙѳѥ ʍѧʍƴʌƀκƴ ɯʌѥχƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣѧʌҁᴙ ҁ ϯʙѳєӣ πѳκѳӣʜѳӣ ʍѧʍѧɯєӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ đѳ ҁʍєⱀϯџ ӡѧϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ѱєκѧҁϯџκ єѣƴӌџӣ ϯƀӀ ѫє ʍєʜᴙ κѧκ ҁʍєⱀϯџ ѣѳџɯƀҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀⱀєѫƴ ʍѳӡґџ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґѳđѳπʌᴙҁ єѣƴӌџӣ ӌє ϯƀӀ ϯѧʍ ⱀѧҁҁκѧӡƀӀʙѧєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧҁκⱀƀӀʙѧӣ ҁʙѳӣ ϯѧʌѧʜϯ ҁѳҁѧϯƀ ʜѧ πѳʌʜƴѥ κѧϯƴɯκƴ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁʙѳӣ єѣѧʌƀʜџκ ʙџđєʌ ѳⱀκ єѣƴӌџӣ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯⱀѧχѧʌ ϯʙѳѥ ѱєκѧҁϯƴѥ ʍѧʍѧɯƴ ӌƴⱀκƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌƴⱀκѧєѣʌџκ єѣƴӌџӣ ƴҁκѳⱀƀ ҁʙѳӣ ʜѳʜ ҁϯѳπ џɯѧκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳҁʌџʜѧ єѣѧʜѧᴙ πѳκѧѫџ ҁʙѳџ ʜѧʙƀӀκџ ʜѳʜ ҁϯѳπєⱀѧ ѧ ʜє ѳϯҁѳҁʜџκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє πƀӀϯѧєɯƀҁᴙ πѳđ ʍєʜᴙ κѳҁџϯƀ ⱀѧӡđѳʌѣѧӣ єѣƴӌџӣ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χʙѧϯџϯ ʍєʜᴙ κѳπџⱀѳʙѧϯƀ ҁƀӀʜџɯκѧ ɯѧʌѧʙƀӀ єѣƴӌєӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ӡѧϯƴπѳκ єѣƴӌџӣ ѧ ϯƴϯ єѱє ᴙ ϯʙѳџ ʍѧʌѳӌџҁʌєʜʜƀӀє ʍѳӡґџ ҁπєⱀʍѳӣ єѫєđʜєʙʜѳ ӡѧʌџʙѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ӌʌєʜѳѫƴӣ ѳϯъєѣѧʜʜƀӀ ѳϯӡѳʙџҁƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҵƀӀґѧʜєʜѳκ єѣƴӌџӣ ӡѧϯκʜџ єѣѧʌџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁʍѳϯⱀѥ ϯƀӀ ѧχƴєϯƀ κѧκ đєⱀӡκѳ ѣѧӡѧⱀџɯƀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯџɯє ѣƴđƀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍєҁџʌџ ϯєʌѳ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧđⱀƴґѧʌџҁƀ ʜѧđ ϯⱀƴπѧκѳʍ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʌѳʍѧʌ ґѳʌѳʙєɯκџ ϯʙѳєґѳ ҁєʍєӣҁϯʙѧ đєϯџɯєκ ɯʌѥχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧҁⱀѧʌ ʜѧ ґѳʌѳʙƴ ϯʙѳєґѳ ѳϯҵѧ πџđѳⱀκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χџʌѳє ϯєʌƀҵє ϯʙѳєӣ ʍѧʍѧɯџ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡѧɯƴґѧʜʜƀӀӣ ѳϯҁѳҁʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁъєѣƀӀʙѧӣ ѳϯҁѥđѧ πѳҁκѳⱀєє ҁƀӀʜѳκ ɯʌѥχџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґđє ϯʙѳӣ đƴχ ҁƀӀʜ ɯѧʌѧʙƀӀ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧϯᴙʜџ ʍѳџ ᴙӣҵѧ ʜѧ ҁʙѳѥ ӡѧπʌѧκѧʜʜƴѥ ⱀѳѫƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙҁκѳπѧѥ ґⱀѳѣʜџҵƴ ϯʙѳєӣ ʍѧϯєⱀџ ƴєѣџѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜƴʌᴙ ɯʌѥχџ ӡѧđʜєπⱀџʙѳđʜƀӀӣ ҁʌƀӀɯƀ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧχѧⱀκѧєʍ ґʌѧӡџѱѧ ʍѧʍѧɯє ϯʙѳєӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ ҁʙѳё єѣʌџѱє ҁƀӀʜѳκ ɯʌѥχџ ʍєⱀϯʙƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џɯѧκƴ єѣѧʌƀʜџκ єѣєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ɯʌѥχƴ ʜѧ ʙҁєχ πѧⱀѧχ єѣѧʌ ϯƴϯ ӌєⱀϯџʌѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ʜѳґѧʍџ џ ⱀƴκѧʍџ πџӡđџʌ đѳ ѳʜєʍєʜџᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧѫѧⱀџʍ ϯєѣᴙ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁπⱀѧʙџʌ ʜƴѫđƴ ʙ єѣʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ χѧⱀӌєʌƀʜџκ ϯєѣᴙ єѣєʍ ҁƀӀʜѳκ ɯʌѥχџ ʜџѱџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ⱀƀӀґѧʌƀʜѥ ʙƀӀєѣƴ ӌєⱀϯџʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґʌѧʜđƀӀ ϯʙѳєӣ ʍѧϯєⱀџ ʙƀӀⱀʙѧʌ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πєⱀєκѳʌѳϯџʍ κѳҁϯџ ϯʙѳєӣ ʍѧϯєⱀџ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯѧκѳє ӡƴѣⱀџʌѧ єѣѧʜѧᴙ ѧϯҁѳҁџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѣⱀѧ ϯʙѳєӣ ʍѧʍѧɯџ ɯʌѥχџ ʙʍєҁϯє ҁ ʌєґκџʍџ џ ҁєⱀđҵєʍ ʙƀӀⱀʙƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єѣʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ κѧκ ϯⱀᴙπκƴ ѣƴđƴ ѥӡѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ єѣƴӌѧᴙ ʜє ҁʍѳґʌѧ ϯєѣє πⱀџđƴʍѧϯƀ џʍᴙ џ ʜѧӡʙѧʌѧ ϯєѣᴙ ҁƀӀʜѳʍ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ϯѧʍ πѳϯєⱀᴙʌҁᴙ ӌϯѳ ʌџ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ʜџѱєѣⱀѳđҁκџӣ ʍѳӣ ӌʌєʜ ϯƴϯ ѣєⱀєɯƀ ʙ єѣѧʌѳ ѳϯ ґѳʌѳđѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ єѣѧʌѳ ӌƴⱀκѧ ᴙ ϯʙѳѥ ʍѧϯƀ ѣƴđƴ ҵєʌƀӀʍџ đʜᴙʍџ ϯⱀѧχѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πƴҁϯџʍ ϯʙѳѥ ѣѧѣƴɯκƴ ɯʌѥχƴ ʜѧ ѻѧⱀɯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌπѳκѧʌ ҁѳҁѧʌƀʜџκ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πⱀѳѣџʌ ѣѧɯʜѥ ϯʙѳєӣ ʍѧϯєⱀџ ӡѧʌƴπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ єѣѧʌ κџɯκџ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀđєⱀѫκѧʍєʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ πѳӡѳⱀџѱє єѣѧʜѳє πѳɯєʌ ʜѧχƴӣ ѳϯҁѥđѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳӡѳⱀʜџκ єѣƴӌџӣ ѳѣʙѧʌѧκџʙѧӣ ʍѳџ ᴙӣҵѧ ҁʙѳџʍџ ґƴѣѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ґѳⱀʌѳ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧϯєⱀџ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧґʜѧʌџ ʌƀӀҁѳґѳ ʙ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌѳʍѧєʍ ʜѳҁ ϯʙѳєӣ ʍѧʍƴʌє ɯʌѥχє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀѧӡъєѣƴ ʙҁё ϯʙѳё ⱀѳđҁϯʙѳ ҵƀӀґѧʜѳʙ ϯƀӀ ʙҁʌєđ ӡѧ ʜџʍџ πѳӣđєɯƀ ӌƴⱀѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџʜџʍѧӣ ҁπєⱀʍѧκ ʜѧ ⱀƀӀʌџѱє ҁʙџʜƀᴙ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍєⱀӡκѳєѣʌƀӀӣ ҁƀӀʜ ɯʌѥχџ ӡѧϯκʜџ єѣѧʌƀʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʙѳ ʙҁє єє ƴѱєʌƀᴙ ѳϯϯⱀѧχѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁⱀѧʌ ʙ ѧⱀϯєⱀџѥ ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ϯⱀѧχѧʌ đѳ ѳʜєʍєʜџᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌџʜґѧӌѣƴκ єѣƴӌџӣ ҁѣʌџӡƀҁᴙ ҁ ʍѳџʍџ ᴙӣҵѧʍџ ҁʙѳџʍ єѣѧʌƀʜџκѳʍ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀѧӡⱀєѫєʍ ϯʙѳє đѳχʌѳє ϯєʌƀҵє ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳѣƀєʍ κѳʌƀᴙ ʙ ϯⱀƴπ ϯʙѳєӣ ʍѧʍѧɯџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ѳѣχѧⱀκѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӡѧʙѧʌџ єѣѧʌƀʜџκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ⱀєѱє πєӌѧϯѧӣ ҁʙѳџʍџ ѫџⱀʜƀӀʍџ πѧʌƀҵѧʍџ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀєѣƴ ϯʙѳѥ ʍѧϯƀ ʜє ҁѳʍʜєʙѧӣҁᴙ πєɯκѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯƴґѧʜʜƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ ӡѧʙѧʌџ єѣѧʌѳ ҁʙѳє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍƀӀ ϯєѣᴙ єѣѧʜѳґѳ ҁƀӀʜκѧ ɯʌѥχџ ϯƴϯ đѳ ѣєʌѳґѳ κѳʌєʜџᴙ đѳʙєđєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χєʌʌѳƴ ҁƀӀʜ ɯʌѥχџ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ѻƴѻʌƀӀѫʜџκ єѣƴӌџӣ ᴙ ʙ ϯʙѳєӣ ⱀƀӀʌѳ χѧⱀκѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣᴙ ƴӡʜѧʌ ϯƀӀ ѫє ϯѳϯ ҁѧʍƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁѧʍѣѳҁ ʜѧʍƴϯџ єѣƴӌџӣ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌєӡѧӣ ҁѳ ҁʙѳєӣ πѧʌƀʍƀӀ ϯƴπѳⱀƀӀʌƀӀӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ӡѧⱀєѫƴ ϯʙѳѥ ʍѧϯƀ πѳκѧ ϯƀӀ ѣƴđєɯƀ ϯƴϯ ҁϯⱀѳӌџϯƀ ҁƀӀʜ ɯʌѥχџ πџɯџ ⱀєѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧ ϯƀӀ ϯѧʍ ҁʙѳџʍџ ѫџⱀʜƀӀʍџ πѧʌƀҵѧʍџ ϯƀӀκѧєɯƀ πѳ κʌѧʙџɯѧʍ πѳʌ ⱀѧӣѳʜѧ ƴҁπєʌѳ ʙƀӀєѣѧϯƀ ϯʙѳѥ ʍѧϯƀ ҁƀӀʜџɯκѧ ɯʌѥχџ ϯƀӀ ϶ϯѳ πѳʜџʍѧєɯƀ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ҁƀӀʜ ɯʌѥχџ đѧκ ϯƀӀ єѱє џ κѧѫđƀӀӣ ҁѳѳѣѱєʜџєʍ ƴϯʙєⱀѫđѧєɯƀ ϶ϯѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯⱀєπєϯʜѳ єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ ҁƀӀʜџɯκѧ ʍⱀѧӡџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʌƀӀѣƴ đѧʙџɯƀ ҁƀӀʜ ϯʙѧⱀџ єѣѧʜѳӣ ѳѣʌџѫџ ʍѳџ ᴙӣҵѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ χⱀѥʜđєʌƀ єѣƴӌџӣ ᴙ ϯʙѳӣ πᴙϯѧκ ʜѧ ӡѧʌƴπƴ ʜѧҁѧѫџʙѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ҁƀӀʜ ɯʌѥχџ χʙѧϯџϯ ѳπⱀѧʙđƀӀʙѧϯƀҁᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌϯѳ ӡѧ ɯƴϯκџ ҁƀӀʜ ɯʌѥχџ ᴙ ʍѧϯƀ ϯʙѳѥ ϯⱀѧχѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ʍƴχϯѧⱀ єѣƴӌџӣ ӡѧʙѧʌџ єѣѧʌѳ ҁʙѳє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯѧκѳʍƴ ѱєґʌƴ ѣƴđƴ ʙҁє ӡƴѣƀӀ ʌѳʍѧϯƀ џ ʙƀӀđєⱀґџʙѧϯƀ πѳʌѳҁκѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯƴʌџ єѣѧʌѳ ҁʙѳє ѳπƴđđѧʌѳ єѣƴӌєє ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ πџґʌџҵѧ єѣƴӌѧᴙ πѳҁѧҁџ ʍѳӣ ӌʌєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πѳʌƴґѳđѳʙѧʌƀӀӣ ҁƀӀʜ ɯʌѥχџ ӌє ϯƀӀ ʍʜє ϯƴϯ ӌєɯєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ đѳ ҁџχ πѳⱀ ѫđƴ κѳґđѧ ϯƀӀ ӡѧκⱀѳєɯƀ ҁʙѳӣ πⱀѳѣџϯƀӀӣ єѣѧʌƀʜџκ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀϯⱀѧχѧѥ ѳɯʍєϯκџ ϯʙѳєӣ ʍѧʍѧɯџ џ πѳʍєѱƴ џχ ʙ ϯʙѳѥ πⱀѳϯⱀѧχѧʜʜƴѥ ґʌѳϯκƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ϯƀӀ ѫє ҁƀӀʜ ɯʌѥχџ ʙ κѳʜҵє κѳʜҵѳʙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳѣⱀєѫƴ ϯʙѳџ πѧϯʌƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳʌџӡƀӀʙѧӣ ʍѳџ ᴙӣҵѧ ҁƀӀʜ ɯʌѥχџ џ ҁџđџ ʍѳʌӌѧ πѳκѧ ᴙ ϯєѣє ʙʜѧϯƴⱀє ϯƴϯ πⱀᴙʍѳ ѣѧɯʜѥ ʜє ҁʜєҁ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѳҁѳʌѧπƀӀӣ ҁƀӀʜ ϯʙѧⱀџ πⱀџѫʍџҁƀ κ ʍѳєӣ ӡѧʌƴπє ᴙӡƀӀκѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴᴙӌџʍ ϯʙѳѥ ʍѧϯƀ ɯʌѥχƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ґѳⱀѣѧϯƀӀӣ ҁƀӀʜ ɯʌѥχџ ᴙ ʍѧϯƀ ϯʙѳѥ єѣѧʌ ʜѧ ҁπџʜє ϯʙѳєґѳ πѧπѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳҵєʌƴӣҁᴙ ҁ ʍѳџʍџ ᴙӣҵѧʍџ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁκѧѫєɯƀ ʙ πⱀѳϯџʙѳʙєҁ ҁʌѧѣƀӀӣ ʜєđѳⱀѧӡʙџϯƀӀӣ ҁƀӀʜ ɯʌѥχџ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ κѧκ πѳʌƴʍєⱀϯʙƀӀӣ ҁƀӀʜ ɯʌѥχџ πѳ ӡєʍєʌƀκє ѣєґѧєɯƀ ѧ ҁʙѳџʍџ ѳϯҁѳҁѧʍџ ϯƀӀ đѳπѳʌʜᴙєɯƀ κѧⱀϯџʜƴ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧκ ϯƀӀ ʙƀӀєѣѧʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ӡѧӌєʍ ʍʜє ϯєѣє ϶ϯѳ đѳκѧӡƀӀʙѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙƀӀκѳπѧѥ ϯⱀƴπʌѳ ϯʙѳєґѳ ѳϯҵѧ πџđѳⱀѧҁѧ џ πⱀџ ʜєʍ ѫє ʙƀӀєѣƴ ϯʙѳѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ʜѧ πѳʌʜѳʍ ҁєⱀƀєӡє ґѳʙѳⱀѥ ӡѧϯκʜџ ҁʙѳє đƴπʌѳ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳκѧѫџ ҁʙѳџ ҁπѳҁѳѣʜѳҁϯџ ϯєⱀπџʌѧ єѣƴӌѧᴙ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ⱀєӡѧʌ ϯⱀƴπ ϯʙѳєӣ ʍѧʍѧɯџ ɯʌѥχџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ҁƀӀʜ ɯʌѥχџ ᴙ єѣѧʌ ϯʙѳѥ ӌєⱀʜƴѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ѣƴđƴ ϯⱀѧχѧϯƀ ϯʙѳє ҁʍѧӡʌџʙѳє єѣѧʌѳ єѫєҁєκƴʜđʜѳ ϯƀӀ ʍєʜᴙ ҁʌƀӀɯџɯƀ ҁƀӀʜѳκ ɯʌѥχџ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳӣ ϯⱀƴπ єѣѧʌ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧɯѧ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳᴙ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜџɯκѧ ɯʌѥχџ ϯƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜƴʌᴙ ɯʌѥχџ ϯƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜᴙⱀѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє πѳđєʌѧϯƀ єҁʌџ ϯƀӀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ӌєⱀʜѳѫѳπƀӀӣ ҁƀӀʜ ɯʌѥχџ πѳҁѳҁџ ʍѳџ ᴙӣҵѧ϶  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πєⱀєϯⱀѧχѧѥ ѳɯʍєϯκџ ϯʙѳєӣ ʍѧϯєⱀџ ҁƀӀʜџɯκѧ ʍⱀѧӡџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѧʍѳє ʙⱀєʍᴙ ʙƀӀєѣѧϯƀ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє κƴκѳʌđᴙⱀѧ єѣѧʜѧᴙ κѧκ ϯєѣє ƴʍѧ χʙѧϯџʌѳ ҁѳ ʍʜѳӣ ʜѧӌѧϯƀ єѣѧɯџϯƀҁᴙ ҁʌѧѣƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ κѧκ ѳѣƀӀӌʜѳ ӡѧѣƀѥ ҁʙѳѥ ӡѧʌƴπƴ ʙ ґʌѳϯκƴ ϯʙѳєӣ ʍѧϯєⱀџ џ ϯƀӀ ʍʜє ʜџӌєґѳ ʜє ҁđєʌѧєɯƀ ʜѧџҁʌѧѣєӣɯџӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє πѳʜџʍѧєɯƀ ӌϯѳ ϯƀӀ ʙҁєґѳ ʌџɯƀ ҁʌѧѣƀӀӣ ҁƀӀʜ ɯʌѥχџ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁє πⱀєκⱀѧҁʜѳ πѳʜџʍѧѥϯ ӌϯѳ ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ χʙѧϯџϯ ҁʌєπѳ ʙєⱀџϯƀ ʙ єє ɯѧʌѧʙƀџ ҁκѧӡκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧʜѧʌџѱє ϯʙѳєӣ ӌєⱀʜѳӣ ʍѧϯєⱀџ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳϯπџđѳⱀѧҁџʍ ϯʙѳѥ ʍѧʍƴʌƀκƴ κѳӌєⱀґѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ϯѧʍ πџӡđџɯƀ ҁƀӀʜ ɯѧʌѧʙƀӀ ϯƀӀ ʍєʜᴙ ӡѧєѣѧʌ ᴙ ϯєѣє ӡѧʌƴπѳӣ єѣѧʌƀʜџκ ⱀѧӡѳѣƀѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳҁѧҁƀӀʙѧӣ ʍѳӣ ӌʌєʜ џ ҁџđџ ϯџχѳ ѱєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ ҁʙѳӣ єѣѧʌƀʜџκ ѫєⱀєѣєʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʙ πѳӡʙѳʜκџ ϯʙѳєӣ ʍѧʍѧɯџ ʙґѳʜѥ ҁʙѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ κѳʌєʜʜƀӀє ӌѧɯѧӌκџ ϯʙѳєӣ ʍѧʍѧɯџ ʙґѳʜѥ ʍѧϯєʌʌџӌєҁκџє đџҁκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀѧχѧʌ ϯʙѳѥ ʍѧϯƀ ɯʌѥχѧ ʙ ѱєκџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ϯƀӀ ϯѧʍ ґѳⱀѳđџɯƀ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ʍєʜᴙ ʜѧӌџʜѧєɯƀ ѣєҁџϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѳʜӌѧʌ ʜѧ ґѳʌѳʙƴ ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʍѧʌѳӌџҁʌєʜʜƀӀє џӡʙџʌџʜƀӀ ϯʙѳєӣ ʍѧʍѧɯџ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє πѳɯєʌ ʜѧχƴӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯκʜџƀ ʜѧχƴӣ ϯєⱀπџʌѧ єѣƴӌѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁѳҁѧʌ ʍѳџ ᴙӣҵѧ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ϯⱀѧχѧєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳґʜѧʌ ʌƀӀҁѳґѳ ʙ ϯʙѳѥ ʍѧϯƀ ɯʌѥχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯџҁʜџҁƀ ҁƀӀʜ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳⱀʙєʍ κѳѫƴ ҁ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє πѳʜџʍѧєɯƀ ӌϯѳ ϯƀӀ πѳđҁѳҁʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍєӌϯѧʌ ѳ ϯѳʍ ӌϯѳ ҁʍѳѫєɯƀ ҁѳ ʍʜѳӣ ϯᴙґѧϯƀҁᴙ ѧ πѳ џϯѳґƴ ѳϯҁѳҁѧʌ ʍѳӣ ӌʌєʜ?  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" єƴ ӌѧӣʜџκ єѣƴӌџӣ ӡѧκⱀѳӣ ҁʙѳє єѣѧʌџѱє </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ χƴӣʜџ ʜє ӌѧʙκѧӣ κѳґđѧ ʍѳӣ χƴӣ ҁѳҁєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣᴙ ϯƴϯ ʍѧʜєⱀѧʍ ʜѧƴӌƴ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳʌџҁƀ ʜѧ ʍѳѥ ӡѧʌƴπƴ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ ʙҁє κџɯκџ ʙƀӀⱀʙƴ ҁ κѳⱀʜєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁ ϯєѣᴙ ҁƀӀʜκѧ ɯʌѥχџ ӡѧ ϯѧκƴѥ χƴӣʜѥ ҁπⱀѳҁџʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯⱀƴπ ϯʙѳєӣ ʍѧʍƀӀ ҁєӣӌѧҁ ʙҁκⱀѳѥ ƴ ϯєѣᴙ ʜѧ ґʌѧӡѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜƴ-ѫє, πѳκѧѫџ ʍʜє ƴⱀѳʙєʜƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѧɯ ҁκџʌʌ κѧκ ƴ đєϯєӣ ɯʌѥχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πⱀѳϯџʙ κѳґѳ ϯѳπџɯƀ єѣʌѧʜ ϯƴπѳґѳʌѳʙƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ ʍѳґџʌѧχ ϯʙѳџχ ⱀѳđҁϯʙєʜʜџκѳʙ πʌᴙҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ѫđџ ѣєđƀӀ ҁ ϯʙѳєӣ ʍѧʍѳӣ ѧχχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜѳκ ɯʌѥχџ ᴙ ϯєѣᴙ ʜѧ ӡєʍʌѥ ӡđєҁƀ ҁπƴѱƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χƴʌџ ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ʌѳɯѧⱀѧ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πʌѳϯƀ ϯʙѳєӣ ʙƀӀєѣѧʜѳӣ ʍѧʍƀӀ ҁѫџґѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ πѳ ӌєⱀєπƴ ϯʙѳєӣ ʍѧϯєⱀџ χѳđџʌ πⱀѳđѧʙʌџʙѧᴙ єґѳ ʙʜџӡ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ χƴӣʜџ πѳκѧѫџ ʍʜє κϯѳ ҁѳπєⱀʜџκ đʌᴙ ʍєʜᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍѧκҁџʍƴʍ πѳđχѳđџɯƀ đʌᴙ ⱀѧӡѳґⱀєʙѧ ҁƀӀʜƴʌᴙ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜџκѳʍƴ ʜєџӡʙєҁϯєʜ, ʍѧʌƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁπѳʍџʜѧӣ ʍєʜᴙ κѳґđѧ ѣƴđєɯƀ ҵєʌѳʙѧϯƀ ʙ ґƴѣƀӀ ҁʙѳѥ đєʙƴɯκƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѧκ ϯѳʌƀκѳ ϯʙѳᴙ ʍѧϯƀ ƴʙџđєʌѧ ʍѳӣ ӌʌєʜ, єё ʜѳґџ ҁⱀѧӡƴ ⱀѧӡđʙџʜƴʌџҁƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌџӡƀӀʙѧӣ ҁ ʍѳєӣ ӡѧʌƴπƀӀ ҁπєⱀʍƴ, ϶ϯѳ πⱀџκѧӡ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ џ ґđє-ѫє ϯʙѳᴙ ʍѳѱʜѳҁϯƀ ʜƴʌєʙѳӣ πχѧχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡđєҁƀ ϯєѣє єѣѧʌѳ ѳϯѳѣƀѥϯ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧʙѧʌџ єѣѧʌѳ κѳґđѧ πєⱀєđ ϯѳѣѳӣ ʍѳё ʙєʌџӌєҁϯʙѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳʙєϯƴѥ ϯєѣє ⱀѧҁҁӌџϯƀӀʙѧϯƀ ʜѧ ʌƴӌɯєє ҁʌѧѣѧκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯєѣє ʍєʜᴙ ʜџκѧκ ʜє πєⱀєπʌѥʜƴϯƀ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџʍџ ϯѳϯ ѻѧκϯ ӌϯѳ ϯƀӀ ϯƴϯ ѳϯҁѳҁєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӡđєҁƀ ѣƴđєɯƀ ʙƀӀѫџʙѧϯƀ ʙ ʍѳёʍ πⱀџҁƴϯҁϯʙџџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ πџđѳⱀѧ ѣєґџ ѳϯ ʍєʜᴙ πѳκѧ ʍѳѫєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁъєѣѧʌҁᴙ ʜѧχƴӣ ѳϯҁѥđѧ πⱀєđҁϯѧʙџϯєʌƀ πєϯƴɯџʜѳӣ ʍѧҁϯџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ϯѧκ đѧʙѧӣ ҁѳҁџ ʍʜє χƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ʍʜє χƴӣ ϯѧκ ҁџʌƀʜѳ ѳϯҁѳҁѧϯƀ χѳϯєʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ҁϯџҁʜџ ʜѧχƴӣ ҁʙѳё єѣѧʌѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯєⱀƀ ʍёⱀϯʙƴѥ ʙ ʍѳⱀđƴ ϯⱀѧχѧʌ ҁʌƀӀɯƀ ӌєπƴχѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє χƴӣ ϯƴϯ ʌѧҁκѧϯƀ ѣƴđєɯƀ ҁʙѳџʍ єѣѧʌѳʍ ѳπƴѱєʜʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜѳκ ɯʌѥχџ πѳɯёʌ ʜѧχƴӣ ҁ ϶ϯѳӣ ѣєҁєđƀӀ ᴙ ϯєѣє єѣѧʌѳ ӡđєҁƀ ҁʌѳʍѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ɯʌѥχє ѱѧҁ ʙ ⱀѳϯ κѳʜӌƴ ҁϯⱀƴєӣ ҁπєⱀʍƀӀ, ʙѧѻʌєⱀɯѧ ϯƀӀ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ χƴʌџ ӡѧđʜѥѥ đѧєɯƀ ҁƀӀʜ ɯʌѥχџ ᴙ ϯʙѳѥ ʍѧʍƴ ϯƴπƴѥ ʙƀӀєѣƴ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ҁʙѳӣ χƴӣ ʙ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯƴχє ѫџⱀʜѳӣ ӡѧϯѳʌκѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜѧχƴӣ ʍʜє ӡѧʌƴπƴ ѳϯҁѳҁѧʌѧ ϯѳ, ӡѧѱєκѧʜκѧ ϯƀӀ ѫѧʌκѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁƀӀʜ χƴӣʜџ ӡѧʙѧʌџ χʌєѣƴɯʜѥ ᴙ ϯєѣє єѣѧʌѳ ʙ ѻѧⱀɯ ϯƴϯ πⱀєʙⱀѧѱƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ џđџ ҁѥđѧ ѣєⱀџ χƴӣ πѳđ ᴙӡƀӀκ, ʍѧӡʜᴙ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ӡѧґʌѧϯƀӀʙѧӣ ʍѳӣ ѣѳʌƀɯѳӣ χƴӣ πѳ ҁѧʍƀӀє ґʌѧʜđƀӀ ʍѧʌѳӣ ѧχχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯʙѳᴙ ʍѧʍѧ κƴⱀʙѧ єѣƴӌѧᴙ ʍʜє ʙ χƴӣ ӡƴѣѧʍџ ʙҵєπџʌѧҁƀ, ʙѧʍπџⱀɯѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯѳʌƀκѳ πѳπⱀѳѣƴӣ ϯƴϯ ӌѧҁ πѳκѧӡѧϯƀ ᴙ ϯєѣє єѣѧʌѳ ҁʙєⱀʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜκƴ ɯʌѥχџ ϯєѣє ʍѧϯƴɯκƴ ʙƀӀєѣєʍ ϯѳʌπѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯєⱀƀ đѳχʌƴѥ πѳ κⱀƴґƴ ϯƴϯ πƴѱƴ ϯƀӀ ӌє ҁƀӀʜ ѣʌᴙđџ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ πџđѳⱀѧ єѣѧʜѳґѳ πѳκѧѫџ ʍʜє ʙҁѥ ҁʙѳѥ ʙƀӀđєⱀѫκƴ κʌѳƴʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđєҵ ϯƀӀ ӌє ʍѳџʍ χƴєʍ πѳđѧʙџʌҁᴙ ӌϯѳ ʌџ đѳʌѣѳёѣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ѱѧҁ ʙʜѧϯƴⱀє єѣѧʌѳ ʜѧєѣѧɯƴ ҁ ʜѳґџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ɯʌѥχƴ ϯⱀѧχѧѥ џ χƴʌџ ϯƀӀ ʍʜє ҁđєʌѧєɯƀ ϯєⱀπџʌѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ϯƴϯ πєϯƴɯѧⱀѳӣ ѱѧҁ ҁϯѧʜєɯƀ єѣѧʌѳ ʙϯѳπџ ʜѧχƴӣ ʙƀӀđⱀѧ ѳѣъёѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ɯѧʙκѧ єѣѧʜѧᴙ ѣєⱀєґѧ πѳπƴϯѧʌ џʌџ ӌє ᴙ ʜє πѳӣʍƴ ҁƴӌєʜѳκ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧ ʜƴ đѧʙѧӣ ʜѧκѧϯџ ʍѳєӣ ҁπєⱀʍƀӀ ҁєѣє ʙ ⱀƀӀʌѳ ӌєπƴɯ єѣѧʜƀӀӣ χχѧχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ џ ϯѧκ ѳπƴѱєʜєҵ єѣѧʜƀӀӣ κƴđѧ ϯєѣє єѱё ʜџѫє ϯƴπѳӣ ҁƴκѧ ѧχѧχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ʙҁє ҁƀӀʜ ɯʌѥχџ ϯєѣє πџӡđєҵ ϯѧѱџ ҁʙѳѥ χѧⱀѥ κⱀџʙƴѥ ҁѥđѧ ᴙ єё ϯєѣє ҁʌѳʍѧѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ϯƀӀ ҁѳҁѧʌ џ ӌє đѧʌƀɯє ʙƀӀѣʌᴙđƀ ƴєѣџѱʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ џđџ ʍʜє ʜѳҁκџ ҁϯџⱀѧϯƀ ɯʜƀӀⱀƀ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѱё ӌє ӡѧ ʜѳƴ ʜєӣʍ єѣѧʜƀӀӣ, ҁъєѣѧʌҁᴙ ʜѧχƴӣ ҁ ʍѳєґѳ πƴϯџ ѱєʜѳκ єѣʌџʙƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ ӌє ʜѧχƴӣ ѣџӌѧⱀѧ ѧχƴєʙɯѧᴙ ҁџđџ џ ʜє ⱀƀӀπѧӣҁᴙ đƴⱀѧ єѣѧʜƴϯѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜџӌє ӌϯѳ ϯƴϯ κѧѫđƀӀӣ ƴҁπєʌ ϯʙѳѥ ʍѧϯƀ πѳϯⱀѧχѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧѱєʍџ єѣʌџʜƴ џʜѧӌє ᴙ ϯʙѳєӣ ʍѧϯƴχє ѳӌƴʍєʙɯѳӣ κѧѣџʜƴ ⱀѧҁπџđѳⱀѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ʌѳʙџ χѧⱀӌџʜƴ ʙ ʍѳⱀđƴ ѱєґѳʌ ѳѣѳҁҁѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱѧҁ ҁ ϯєѣᴙ ҁƀӀʜκѧ ɯʌѥχџ ҁπⱀѳҁџʍ ӡѧ ϯѧκƴѥ χƴӣʜѥ ʌѳɯѧⱀѧ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ᴙ ϯєѣє єѣѧʌѳ ϯʙѳё ґⱀᴙӡʜѳє ϯƴϯ κ χƴᴙʍ ҁѳѣѧӌƀџʍ πєⱀєκѳɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ϯѧʍ ⱀѧҁҁʌѧѣѳʜƀӀ ʌѳʙџɯƀ ѳӌκѧⱀџκ єѣѧʜƀӀӣ πѳϯєӣ ϯƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ƴѫє ϯʙѳӣ πᴙϯѧκ ҁʙџʜʜѳӣ ʜѧϯⱀѧχѧʌ κⱀƀӀҁѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯєѣє ѳϯʙєӌѧѥ ѱѧҁ ϯʙѳѥ ʍѧʍѧɯƴ κⱀѧҁʜѳѫѳπƴѥ ϯⱀѧχʜєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ χƴӣʜџ єѣѧʜѳӣ πѳʌƴӌѧӣ πџӡđƀӀ πѳ ⱀѳѫє ʍƴҁѳⱀ єѣѧʜƀӀӣ   </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđєҵ đѧ ϯƀӀ ӌє ʜƴʌёʙκѧ єѣѧʜѧᴙ ʙ ҁєѣᴙ πѳʙєⱀџʌѧ џʌџ ӌє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ѳʙӌѧⱀκџ ϯƴπѳӣ πⱀџʌџʙ ҁџʌ πѳӌƴᴙʌ ʙ ҁєѣє џʌџ ӌє ҁ ϯѳѣѳӣ ҁʌѧѣѧκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜѳκ ɯʌѥχџ ʜє ҁπѧϯƀ, ᴙ єѱё ϯⱀѧχѧѥ ϯʙѳѥ ʍѧʍƴ ʙ ѳӌκѳ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʜƀѥѻѧґ єѣѧʜƀӀӣ ᴙ ϯєѣє єѣѧʌƀʜџκ ϯʙѳӣ πѳ ҁϯєʜκє ⱀѧӡʍѧѫƴ ґѳʙʜѧⱀƀ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ѣєґџ ѣƀӀҁϯⱀєє ӡѧѣџⱀѧӣ ƴѫє ҁʙѳѥ ʍѧʍѧʜѥ πⱀѳҁϯџϯƴϯκƴ </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ѫє ϯʙѳѥ ʍѧϯƴɯκƴ ґʌƴχƴѥ єѣѧʌ ʙ ⱀѳϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧκѧϯџ єѣѧʌѳ ґⱀєѣєʜƀ ϯƀӀ єѣƴӌџӣ џ ҁѳҁџ ʍѳӣ πєʜџҁ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ѱѧҁ ϯʙѳѥ ʍѧʍƴ ɯʌѥχƴ ʜѧ πѧⱀƴ ҁ ϯѳѣѳӣ ѳϯχƴᴙⱀѥ ʜѳґѧʍџ џ ⱀƴκѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳӣ đѧ ҁѳҁџ ϯƀӀ ƴѫє ҵєʌκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ κѧ ʙκƴҁџ ʍѳӣ χƴӣ ҁʌƀӀɯƀ ӌє џʜʙѧʌџđ єѣѧʜƀӀӣ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯѧʌѧʙƀӀ ҁѳҁџ ʍѳѥ ӡѧʌƴπƴ πѳⱀєѱє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӌє ґѳʙѳⱀџɯƀ ʍѧʍѧ ϯʙѳᴙ ɯʌѥɯκѧ ʍʜє ѳϯҁѳҁєϯ đѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ єѱё ʜѧ ѳʌџʍπє ʍʜє χƴӣ ѳϯҁѧҁƀӀʙѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ ѱєʌƀ єѣѧʜѧᴙ ѳѣʌџӡʜџ ʍѳӣ χƴӣ đƀӀⱀκѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ϯʙѳѥ ʍѧʍƴ ϯƴđѧ ҁѥđѧ ϯⱀѧχʜєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ӡѧ ϯѳ ӌϯѳѣƀӀ ϯƀӀ χƴӣ ʍʜє ѳϯҁѳҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ πⱀѳҁϯџϯƴϯκџ єѣѧʌѳʍ ҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѣʌᴙ ѣƴđƴ χƴӣ ϯƀӀ ҁѳҁѧʌ џ ʜє ⱀѧӡ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đєϯё ɯʌѥχџ ѫѧʌκѳӣ ʙҁѳҁџ ʍʜє ӌʌєʜ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ѣѧχʜџ ʍѳєґѳ χƴᴙ ӌϯѳ ʌџ ʍѧʌѳӣ ѧχχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧ ʜƴ ϯѧκ ϯѳ ϯʙѳѥ ʍѧϯƀ ӡѧϯⱀѧχѧʌџ ѱѧҁ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜє πⱀѳєѣџ ҁʙѳё đʜџѱє κѳґđѧ ᴙ ʙ ϯʙѳѥ ʍѧʍƴ ӌʌєʜѳʍ ӡѧєđƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳӣ χƴӣ ѱѧҁ ʍѧҁκƴ ϯʙѳєӣ ʍѧʍє ʙƀӀєѣєϯ πƀӀʌƀ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁѳҁџ κѳʜєɯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ đѧ ʍѧϯƀ ϯєѣє єѣƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜџχƴєʙѳ ϯѧκ ϯєѣє ʙ ʍѧϯƀ ʙѳɯєʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ єѣѧʌѳ ϯⱀƴπƴ ϯʙѳєӣ ʍѧʍƀӀ ҁҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ƴ χѧӌџʜѧ єѣѧʜѧᴙ ѳϯҁѳҁ đєʌѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѧϯƀ ϯєѣє єѣѧʌ đєѣџʌ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧӣ ҁѥđѧ ҁʙѳё χʌєѣѧʌѳ ᴙ єґѳ ϯƴϯ ѣƀӀҁϯⱀѳ ʙƀӀєѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ʙѳϯ ϯƀӀ џ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧ ϯƀӀ χƴӣ ʍѳӣ ʌѥѣџɯƀ ҁѳҁѧϯƀ ʜѳӌѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧ ɯʌѥχѧ џ ϶ϯџʍ ʙҁё ҁκѧӡѧʜѳ ϯѧκ ӌϯѳ ѣєⱀџ ʙ χѧʙѧʌѳ χƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ πⱀᴙʍ ѱѧҁ ѣєⱀєɯƀ џ ҁѳҁєɯƀ ʍʜє πєʜџҁᴙⱀƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πⱀџӡʜѧӣ ӌϯѳ ᴙ ϯʙѳѥ ʍѧϯєⱀƀ πѳʌƴʍёⱀϯʙƴѥ єѣѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁє џđџ ҁѳҁџ ƴѫє ӡѧєѣѧʌ ɯκѳʌƀʜџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ʜѳӣ ʍʜє ϯƴϯ ҁѳπʌᴙκ єѣѧʜƀӀӣ ϯƀӀ ҁєӣӌѧҁ χƴӣ ҁѳҁѧϯƀ ѣƴđєɯƀ ҁʜѳʙѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ʜƴ ʙѳѳѣѱє ϯѳ ϯʙѳѥ ʍѧϯƀ єѣєʍ ҁ κєʜϯѧʍџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κѧκѳӣ ⱀѧӡ ƴѫє χƴӣ ѳϯҁѧҁƀӀʙѧєɯƀ ҁκѧѫџ ʍʜє, ѳϯҁѳҁʜџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ѣʌᴙđџ ҁѧʍѳ ҁѳѣѳӣ ᴙ ʙ ϯʙѳѥ ʍѧʍƴ ɯʌѥχƴ κѳʜӌƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ӌє ϯѧκѳӣ ҁƀӀʜѳκ πџđѳⱀѧ ᴙ ѫє ϯєѣє ʍѧʍκƴ єѣƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ϯƀӀ ҁʜѳʙѧ ѳϯҁѳҁєɯƀ ʍʜє ʜƴ κѧκ ʙҁєґđѧ ʙπⱀѳӌєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳπѧ ʜѧ ѱѧҁ ϯʙѳѥ ʍѧʍƴ єѣѧɯџϯƀ ѣƴđєʍ πѳ ʍѳⱀđє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє χƴӣ єѱё ҁ ⱀѳѫđєʜџᴙ ҁѳҁѧʌ ҁƀӀʜ χƴӣʜџ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ χѧⱀє ϯєѣє χƴӣ ʍѳӣ ҁѳҁѧϯƀ πџᴙʙκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙҁѳҁџ ϯƴϯ џ ѱѧҁ ҁƀӀʜ ѣʌᴙđџʜƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ʜѧ ʍѳґџʌє ϯʙѳєӣ ҁđѳχɯєӣ ʍѧʍƀӀ πʌᴙҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ ϯƀӀ џ ҁƀӀʜѳκ πⱀѳҁϯџϯƴϯκџ κѳʜєɯ ѳϯҁѳҁѧʌ ϯѧκ ѳϯҁѳҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜѧ ϶ϯѳӣ πʌѧʜєϯє ϯʙѳᴙ ʍѧʍѧ ҁѧʍѧᴙ ʌƴӌɯѧᴙ ɯʌѥχѧ πѳ ҁϯѧϯџҁϯџκє ѳϯҁѳҁѳʙ ӡѧ ʙєҁƀ 2020 ґѳđ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜє ҁʍѳϯⱀџ ʜѧ ʍѳӣ ӌʌєʜ ѧ χʙѧϯѧӣ џ ҁѳҁџ ҁκѳⱀєє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ɯѳ ƴѫє χƴџʜƴ ѳϯҁѳҁʜƴʌ ӡѧ ҁƴϯκџ đѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳɯʌџ ᴙ ϯєѣᴙ ʙ πѧҁϯƀ ʙƀӀєѣƴ κѧκ πѳҁʌєđʜєґѳ ʌѳχѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳϯ ѱѧҁ ϯƀӀ χƴєʙѳ ʍʜє đєʌѧєɯƀ ѳϯҁѳҁ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧ ᴙ ʍѧʍѧɯƴ ϯєѣє ʙƀӀєѣѧʌ ʙѳϯ џ ʙҁє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џ ӌє ϯƀӀ ѱѧҁ ѳπᴙϯƀ ѣƴđєɯƀ ʜѧ ʍѳӣ χƴєҵ ѣⱀѳҁѧϯƀҁᴙ ҁʙѳџʍ єѣѧʌѳʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯƀӀ ʍѳѫєɯƀ ƴѫє πѳ ϯџχѳʜƀκƴ χƴӣ πѳҁѳҁѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜκѧ ɯʌѥχџ ʙ ʜѳӡđⱀџ џ ƴɯџ єґѳ ϯⱀѧχѧєʍ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πѳґѳđџ єѱє ʍџʜƴϯƴ џ ᴙ ϯєѣє ʍѧϯƀ ʙƀӀϯⱀѧχʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳϯ ѱѧҁ πѳӣđџ џ ѳϯҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" πџӡđєҵ ϯƀӀ κѳʜєӌʜѳ ҁѳҁѧʌ ʍʜє ϯƴϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʙ ѫѳπƴ єѣѧʌ đѳӌƀ ɯʌѥχџ єѣѧʜѳӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁџ κѧκ ᴙ χѳӌƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍʜє ʙҁѧҁƀӀʙѧʌ πⱀџ ʙҁєχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѧ ϯƀӀ ҁѳҁєɯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁѳҁџ ʍѳѥ χƴᴙʜƴ ʙ κѧʜѧʙє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє πѳđѧⱀѥ ҁʙѳӣ χƴӣ ʜѧ đєʜƀ ⱀѳѫđєʜџᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" џ κ ӌєʍƴ ϯƀӀ ϶ϯѳ πⱀѳєѣѧʌ ʍʜє ϯƴϯ ѳϯҁѳҁƴʜ ƴєѣџѱʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱѧҁ ϯƀӀ ʙҁє ⱀѧʙʜѳ ʍʜє џ ϯѧκ џ ϯѧκ ѳϯҁѳҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯѧʌѧʙƀӀ κѳϯѳⱀƀӀӣ ᴙʙʜѳ ʍʜє χƴӣ ҁѳҁѧʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʍєⱀϯʙᴙκ єѣѧʜƀӀӣ ʜѧ πѳҁѳҁџ ʍʜє χƴᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ӡѧϯκʜџҁƀ ʜѧχƴӣ ҁƀӀʜ χƴӣʜџ џ πƀӀϯѧӣҁᴙ ϯƴϯ ҁѳҁѧϯƀ ʍʜє ӌʌєʜ κѧκ ʜџѣƴđƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧ ϯⱀѧχѧʜѧ ʍѳџʍ ӌʌєʜѳʍ πѳʜᴙʌ đѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʜƴ κѳⱀѳӌє ϯƀӀ џ ϯƴϯ πѳҁѳҁѧϯƀ ʍʜє πⱀџƴҁπєʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ đєϯё ɯʌѥχџ ґѧӡƴӣ ҁѥđѧ ʜѧ ⱀѳϯѧʜ ϯєѣє đѧʍ χƴӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ѫє ҁƀӀʜ ɯʌѥɯκџ ӌєⱀʙƀ єѣѧʜƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѳ ϯƀӀ ʍʜє κѧκ ⱀѧӡ џ πѳʌџѫєɯƀ χƴӣҵѧ, ɯʍѧⱀѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙѳϯ џđџѳϯ ϯƀӀ єѣѧʜƀӀӣ ʍѧϯƀ ҁʙѳѥ πⱀѳєѣѧʌ ʍʜє  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜ χƴӣʜџ ϯƴπѳӣ ϯʙѳᴙ ʍѧʍѧ đƴⱀѧ ʜѧ ʍѳєʍ χƴє ҁџđџϯ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ѫє ϯʙѳѥ ʍѧʍѳӌκƴ πѳđ ѳđєᴙʌѳʍ ϯⱀѧχʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ ʌџѫџ ʍѳџ πѳϯʜƀӀє ᴙӣҵѧ ӌƴⱀκѧɯ ʙƀӀєѣџҁϯƀӀӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ⱀѧκ єѣѧʜƀӀӣ ҁѳҁʜџ ʍʜє ƴѫє đѧʙѧӣ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜκѧ ɯʌѥχџ ϶ϯѳґѳ єѣѧʌџ ʙ χѧⱀѥ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ѧ ʜƴ ѣѧχʜџ ҁϯѳπѧⱀƀ ʍѳєӣ ҁπєⱀʍƀӀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍƀӀ ϯʙѳѥ ʍѧʍѧɯƴ ʙ πєⱀџѳđ ʍєҁᴙκѳʙ єѣѧʌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ѱѧҁ ϯʙѳѥ ʍѧϯƴχƴ πџʜκѳʍ πѳđ ӡѧđ ʙ κѧʜѧʙƴ πџӡđѧʜƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯⱀџ ʍєđʙєđᴙ ʙѧⱀᴙϯ κѧɯƴ ᴙ єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϶ϯѳґѳ ҁƀӀʜѧ ɯʌѥχџ ϯƴϯ πѳχѳⱀѳʜѥ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" đѧʙѧӣ єѣѧϯƀ ϯʙѳѥ ʍѧϯƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" κѧκ ϯƀӀ ҁʍѳϯⱀџɯƀ ʜѧ ϯѳ, ӌϯѳѣƀӀ ᴙ ϯʙѳѥ ʍѧʍƴ ϯⱀѧχʜƴʌ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ϯƀӀ κƴđѧ ϶ϯѳ ҁѳѣⱀѧʌҁᴙ ҁƀӀʜ χƴӣʜџ ѧχѧχ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴɯκє ҁϯѧⱀѳӣ ʙҁє κџɯκџ џӡ ѣⱀѥχѧ ʙƀӀⱀєѫƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ ӌє ѣѳѣџκ єѣѧʜƀӀӣ χƴӣ ҁѳҁџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʙ ϯʙѳѥ ʍѧʍƴ џӡ ϯⱀѧʍʙѧᴙ πѧʌџʌ κѧκ ʙ єѣѧʜƴѥ ʍџɯєʜƀ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁƀӀʜκѧ ɯʌѥχџ ƴѫє ʙ πѳʌ πʌѥѱџϯ ѳϯ ʍѳєӣ ʍѳӌџ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ҁєӣӌѧҁ ᴙ ϶ϯѳʍƴ ҁƀӀʜκƴ ɯʌѥχџ ƴⱀѳđҁκѳӣ ʙ єѣʌѳ πⱀѳπџɯƴ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" χѳϯƀ-ѣƀӀ ϯʙѳᴙ ʍѧʍѧʜᴙ ʍʜє ӌʌєʜ ʜє ѳϯҁѳҁѧʌѧ  </a> <emoji document_id=5404336676879216590>🤡</emoji> ",
" ʍѳӣ χƴӣ ʙєҁƀ ƴѫє ӡѧҵєʌѳʙѧʜƀӀӣ ϯʙѳєӣ ʍѧϯєⱀƀѥ κѳҁѳӡƴѣѳӣ </a> <emoji document_id=5404336676879216590>🤡</emoji> "]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl10))
            await sleep(0.1)
            await sleep(time)

    async def богcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>Б᧐ᴦ ɜᥲκ᧐нчᥙ᧘ κᥲɜнь ᥰ᧐ ᥴынκᥲʍ δ᧘ядᥱᥔ <emoji document_id=5341497469932938890>🚬</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Б᧐ᴦ нᥲчᥲ᧘ κᥲɜнь ᥰ᧐ ᥴынκᥲʍ δ᧘ядᥱᥔ <emoji document_id=5341497469932938890>🚬</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl11 = [" ӌπџđѳⱀʜєʍ ƴєѣѧʜκѧ χѳđᴙӌєґѳ πѳ ҁѧʍƀӀє κџɯκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧɯџʍ ҁƀӀʜκѧ ɯʌѥχџ ѳχƴєʙɯєґѳ ʙѳ ʙҁѥ ʍѳѱƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍƀӀɯƀ єѣѧʜѧᴙ ӌʌєʜ ʍѳӣ ʙƀӀҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙџӌѳʙƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ πѳӌκџ ϯє ѳϯπџӡđџʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧєѣѧɯџʍ đѳ κⱀѳʙџ ϯʙѳѥ ѳϯπѧʙɯƴѥ πєӌєʜƀ ʜѧχƴӣ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѳʙʜѳ єѣѧϯƀ ҁѳҁџ ʍʜє ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ϯƀӀ ӌє πџđѳⱀɯѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧӡƴӣ ѳϯҁѥđѧ ϯёʌκѧ єѣѧʜѧᴙ ѱѧҁ ϯѳѫє πџӡđƀӀ đѧʍ ϯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍⱀѧӡѳϯѧ ʜѧχƴӣ ʙ ґѳʙʜџѱє ҁʙѳёʍ πѳπʌѧʙѧӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯʍѧⱀѧ єѣʌџʙѧᴙ ҁʌєӡƀӀ ʙƀӀϯⱀџ џ ʜє χʜƀӀӌƀ πʌѧκҁѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӡѳⱀџѱє єѣѧʜѳє ƴ ϯєѣᴙ єѣѧʌƀʜџκ πѳѣџϯƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєⱀπџʌѧ ϯƀӀ єѣѧʜƀӀӣ ʙ ϶ϯѳӣ κѳʜѻє ʜѧχƴӣ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌёⱀʜѳʍѧӡƀӀӣ єѣʌѧʜѳџđ đѧʙѧӣ ӌʌєʜ ʍʜє đєⱀʜџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫџⱀʜѳґѳ ҁƀӀʜѧ ɯʌѥχџ ʍѧϯƀ ҁѳҁєϯ ʜѳⱀʍ ϯѧκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πєϯƴχ єѣѧʜƀӀӣ ӡѧʙѧʌџ єѣʌџѱє џ ҁѳҁџ ϯѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ ʜѧχƴӣ πѳ κѧѣџʜє ϯʙѳєӣ πџӡđƀӀ ϯє ʜѧҁƴёʍ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧϯƀ ϯƀӀ ѧⱀѧ єѣѧʜƀӀӣ χƴᴙⱀƴ ʍѳѥ ӡѧҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ҁƴκѧ ѻƴѻєʌƴ ӌʍѳɯʜѳʍƴ єѣѧʌѳ ʙƀӀѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ ɯπѧκ ƴёѣџѱʜƀӀӣ ӡѧʌƴπƴ ϯƴϯ πⱀѳґʌѳϯџɯƀ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєґѳ πѧπѧɯƴ ʙ ⱀѳϯ єѣѧʌ ʜѧχƴӣ ϯєⱀπџʌѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙʜѧϯƴⱀє єѣѧʌѳ ʙκⱀƴϯџ џ ᴙӣҵѧ ʌџӡʜџ ʍѳџ ӌёⱀϯ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƴκѧ ϯѧκѳӣ ϯƀӀ ʙѧѻʌёⱀ єѣѧʜƀӀӣ ёѣѧʜƀӀӣ ϯʙѳӣ ⱀѳϯ πҁџʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳϯʜѳє єѣʌѳ ҁʙѳє ӡѧκⱀѳӣ ʍџҁϯєⱀ ӡѧχѧⱀκѧʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀ ʙҁє ҁƀӀʜκџ ɯʌѥχ ƴӡκѳⱀѳґџє ʜѧχƴӣ πѳҁѳҁџϯє χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧґџѣѧӣҁᴙ ⱀѧκѳʍ ҁƀӀʜѳκ ɯʌѥχџ ʙƀӀёѣџҁϯƀӀӣ ѫѳπƴ ϯʙѳѥ πѳєѣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ πѳκѳӣʜѳӣ ӌƴⱀκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѳӣ ҁѧҁџ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƴκѧ ҁѳҁџ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌƴⱀκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌѥʜϯᴙʙƀӀӣ ҁƀӀʜ ɯʌѥχџ ѳϯҁѳҁџ ӡѧʌƴπƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀєѣєʍ ϯє ʍѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѳϯ ϯʙѳӣ πѳєѣѧʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ѫѳπƴ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣƴϯ ϯᴙ ҁƀӀʜѧ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁџ πєϯƴχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ κѳʜӌєʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ πєʜџҁᴙⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴєѣѳκ ӡѧʌƴπӌѧϯƀӀӣ χƴӣ ʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєʜџҁ ʍѳӣ ҁѳҁѧʌ ϯƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧϯƀ ϯƀӀ ҁƀӀʜ πƴϯѧʜƀӀ єѣѧʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫџ єҁϯƀ ҁѧҁџ ӌʌєʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌʌєʜ ҁѳҁџ ѫє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀєκҁ єѣѧʜƀӀӣ єƴ ϯƀӀ ӌє ʜє ҁʌƀӀɯџɯƀ ʍєʜᴙ ʍѧϯƀ ϯʙѳᴙ ɯʌѥχѧ єѣѧʜѧᴙ ґѳʙѳⱀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πҁѧ ʍѧϯƀ ϯⱀѧχѧʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʜѧ χƴє ʙєⱀϯєʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣ ҁѳҁєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍєӣѣџ ѳϯҁѳҁєɯƀ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ɯʌѥχѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџđєⱀѧҁϯѧ ʍѧϯƀ ʙƀӀєѣєʍ ʙ πџӡđƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧʜѧʌ ϯʙѳӣ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєⱀʙƀ єѣѧʜƀӀӣ χƴӣ ѣєⱀџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ҁƀӀʜ ɯʌѥχџ ѳϯҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳѣєӡƀᴙʜѧ єѣѧʜѧᴙ ӌє ґѳʙѳⱀџɯƀ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜє ҁʌƀӀɯƴ ϯєѣᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ đѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ ϯєπєⱀƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ κѳʜҵє κѳʜҵѳʙ ʍѧϯƀ ϯʙѳѥ єѣєʍ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϶ƴ ʜѧχƴӣ ϯёʌκѧ єѣѧʜѧᴙ ϯƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁѳҁѧʌ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʙѧʌџ єѣѧʌѳ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ҁʌѧѣєӣɯџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁџ πєϯƴχ єƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ ϯƀӀ ʍƴχϯѧⱀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѱѧҁ đѧʙѧӣ ҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧ ʍʜє πѳχƴӣ єѣѧʌѳ ӡѧκⱀѳӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ єѣѧʌ ҁƀӀʜ ɯʌѥχџ κѳϯѳⱀѳʍƴ ʜє πѳχƴӣ ʜѧ ӌѧҁ џґʜѳⱀѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳʍ ҁʙѳџʍ ҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫѳπƴ ʜѧҁѧđџ ҁʙѳѥ ʜѧ χƴӣ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ҁʙѳєӣ ʍѧʍƀӀ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ϯƀӀ ʜƀӀϯџκ єѣѧʜƀӀӣ ҁѳҁџ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣʌᴙϯƀ ᴙ ϯʙѳѥ ҁєʍƀѥ ʙƀӀєѣƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҵƀӀґѧʜ єѣѧʜƀӀӣ đѧʙѧӣ ҁѳҁџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧӡƴӣ κ χƴᴙʍ ҁѳѣѧӌƀџʍ ѳϯҁѥđѧ ѫѳπѧʌџӡ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳκѧѫџ ʍʜє ҁκѳⱀѳҁϯƀ ҁʙѳѥ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ƴѫє ҁđƴʙѧєɯƀҁᴙ ҁƀӀʜᴙⱀѧ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀѳҁʜџҁƀ ϯѧʍ đѧʙѧӣ χƴєҁѳҁ ϯƴπѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ϶ƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧ џđџ ʜѧχƴӣ ѳϯҁѥđѧ ӌƴⱀκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѳʌѣѳёѣ єѣƴӌџӣ ҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯƴπѳӣ ҁƀӀʜ ɯʌѥχџ, ᴙ ϯєѣє ґѳʙѳⱀѥ χƴӣ ҁѳҁџ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʙѧʌџҁƀ ʜѧχƴӣ ҁƀӀʜ ӌƴⱀκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯёʍʜƀӀӣ ҁƀӀʜѳκ πƴϯѧʜƀӀ ҁѧҁєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁџ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣ єѱё ⱀѧӡ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ϯєⱀπџʌѧ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧχѧχѧѧχѧѧ ϯєⱀπџʌѧ ҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜƴ-κѧ đѧʙѧӣ ҁƀӀʜ ɯʌѥχџ πѳҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє πѧđѧӣ đƴχѳʍ ҁʌѥʜᴙʙƀӀӣ χƴєґʌѳϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґđє ϯʙѳӣ ѳѣєѱѧʜʜƀӀӣ ʜѳʜ-ҁϯѳπ đѧƴʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ʜєđѳʜѳʜ-ҁϯѳπєⱀ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧχχѧχѧ ӌƴⱀκѧ єѣѧʜѧᴙ ӡѧκⱀѳӣ ⱀƀӀʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ѣƴđєɯƀ ʍєʜᴙ κѧѫđƀӀӣ đєʜƀ ϯƴϯ ϯєⱀπєϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴɯѧҁϯƀӀӣ ʙƀӀѣʌᴙđѳκ ѳϯҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍʜє πѳχƴӣ ʜѧ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ӌѧҁ ʜє πѳκѧѫџ ҁʌƀӀɯƀ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʍѧϯƀ єѣѧʌ κʌѳƴʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧ ϯƀӀ ϯєⱀπџʌѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁҁƴ ʙ ϯʙѳё єѣѧʌѳ ϯƴϯ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳҁϯџ ϯє ҁʌѳʍѧєʍ єƴ πџđѳⱀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѳʌƴѣѳӣ ҁƀӀʜ ɯʌѥχџ ʙҁѳҁџ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџđѳⱀѧҁϯʜᴙ ϯƀӀ ѳϯҁѳҁџ ƴѫє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳɯєʌ ʜѧχƴӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ϯƀӀ ϯѧκѳӣ ϯєⱀπџʌѧ єѣѧʜƀӀӣ ϯƀӀ ѫє ӌџҁϯѳ ϯƴϯ χѧⱀӌƴ єѱє ⱀѧӡ ʙ ⱀƀӀʌѳ πѳʌƴӌџɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯƀӀ ҵєʌƴєɯƀ ʙ πџӡđƴ ҁʙѳѥ ʍѧϯєⱀƀ ѣʌᴙđƀ ᴙ ѫє κѳʜӌѧʌ ϯƴđѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣƴӌџӣ ҁʍѳⱀӌѳκ ϯƀӀ ҁ κєʍ πƀӀϯѧєɯƀҁᴙ ҁѳπєⱀʜџӌѧϯƀ ʜƀѥҁκƴʌʌ ʙƀӀёѣџҁϯƀӀӣ ᴙ ϯєѣᴙ ϯƴϯ ҁ ʜѳґ đѳ ґѳʌѳʙƀӀ ӌџҁϯѳ ӡѧҁҁƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯєⱀџ ϯʙѳєӣ ѫџⱀʜѳӣ ɯʌѥχџ ʙ πџӡđƴ ѳѣⱀѧϯʜѳ κƴӌѧ đєⱀƀʍѧ ѳϯʌєϯєʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙҁё ϯʙѳє πѳʍᴙϯѳє єѣʌџѱє ӌєⱀʜѳє ӡѧʌƴπѧʍџ ѳѣʌѳѫƴ ϯƴϯ ҁƀӀʜ ɯʌѥχџ ʍѧʍѧɯƴ ϯʙѳѥ ѳϯπџđѳⱀѧҁџʍ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ϯʙѳё ʍєⱀϯʙѳє єѣѧҁѳҁџѱє ʙ đʙѧ ӌʌєʜѧ ϯⱀѧχʜєʍ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁⱀѧӌєʌƀʜџκ ϯʙѳєӣ ѳѣκѳʜӌєʜѳӣ ʍѧʍƴʌє ɯѧʌѧʙє ʙƀӀєѣƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ ӌєⱀєπʜѳ ʍѳӡґѳʙѧᴙ ѳϯ ƴđѧⱀѧ ӡѧʌƴπѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙҁє ϯʙѳџ ѳⱀґѧʜƀӀ џ ϯʙѳѥ ϯƴɯƴ ʙ κⱀѳʙƀ ⱀѧӡⱀєѫƴ ʜѧχƴӣ ʍⱀѧӡƀ єѣƴӌѧᴙ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀχʌѳπʜƴѥ ҁџҁϯєʍƴ ϯʙѳєӣ ʍѧʍƴʌє ɯʌѥχє πєⱀєχƴᴙⱀџʍ πѧӌκѧʍџ ӡѧʌƴπ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧκʌџ ʙƀӀⱀʙєʍ πєϯƴɯκƴ єѣѧʜѳʍƴ ӡѧ єґѳ ʌџɯʜџє ʙƀӀєѣѳʜƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ πѳʌƴʍёⱀϯʙѳӣ ʍѧϯєⱀџ ʙҁє κѳҁϯџ ϯƴϯ πєⱀєҁӌџϯѧѥ πѳєѣѳϯѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ҁ ѳѣκѳʜӌєʜƀӀʍ єѣʌџѱєʍ ϯƀӀ κƴđѧ πѳ ϯѧπκѧʍ ϯѧʍ ʙъєѣѧʌ џɯѧκ єѣƴӌџӣ ϯƀӀ ϯƴϯ ѣƴđєɯƀ ҁϯⱀѧđѧϯƀ κѧѫđƀӀӣ đєʜƀ ʙ ʍѳєʍ πⱀџҁƴϯҁϯʙџџ ӌƴⱀκѧɯ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đⱀѳӌџʌʌѧ єѣѧʜƀӀӣ đѧʙѧӣ ѳϯҁѳҁџ ʍѳѥ χƴᴙⱀƴ ⱀєѱє ҁʌƀӀɯƀ ⱀєκҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ єѣѧʜƀӀӣ ᴙ ϯʙѳєӣ ʍѧʍѧɯє ʜѧ ґƴѣƴ ӡѧʌƴπƴ ʜѧκџđѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ѧʜѧʌƀʜѳӣ đƀӀⱀє ϯʙѳєӣ ʍѧϯƴχџ πⱀѳҁϯџϯƴϯκє єѣѧʜѳӣ κⱀєҁϯ ʙƀӀҵѧⱀѧπѧʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ ѧɯѳϯ єѣѧʜƀӀӣ ҁ ѳʙѳѱʜѳґѳ ⱀƀӀʜκѧ єѣѧʌџѱє ҁʙѳє ƴⱀѳʜџ ᴙ ϯєѣє πѳӡʙѳʜѳӌʜџκ ʜѧχƴӣ ʙƀӀʌѳʍѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ҁ ϯʙѳєӣ ʍѧʍѧɯκџ ɯʌѥχџ πⱀᴙʍѳϯѳκ πƴҁϯџʌ ѳʜѧ κѳʜџ đʙџʜƴʌѧ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ӡѧ ϯⱀѥκџ ҁʙѳџʍ єѣѧʌƀʜџκѳʍ ӌƴʍʜƀӀʍ πⱀѳʙѳⱀѧӌџʙѧєɯƀ ҁ ʍѳџʍ ӌʌєʜѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ πѳʌƴπѳκєⱀ єѣѧʜƀӀӣ ӡѧѣƀӀʌ κϯѳ ϯєѣє đѧʌ χƴӣ ѳϯҁѳҁѧϯƀ πџđѳⱀѧҁ єѣѧʜƀӀӣ ѱѧҁ πѳʙϯѳⱀџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєѣє ϯʙѳᴙ ʍѧʍѧɯѧ ɯѧʌѧʙѧ ґѳʙѳⱀџʌѧ ʍєʜƀɯє πџӡđџ χƴӣʜџ ѧ ϯƀӀ єё ʜє ҁʌƴɯѧʌ ϯєπєⱀƀ πѳʌƴӌѧӣ ʙ єѣѧҁѳҁџʜƴ πџӡđƀӀ ӡѧʌƴπѧʙɯџӣҁᴙ ҁƀӀʜџɯκѧ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣʌџѱє ϯʙѳё ƴѫє ʜѧ ґѳϯѳʙє ѳϯҁѳҁѧϯƀ ʍʜє χƴӣ πӡđҵ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ πѳđҁѳҁ єѣƴӌџӣ χƴʌџ ϯƀӀ πѧʌџɯƀ ʍʜє ʙ ᴙӣҵѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧκⱀѳӣ ҁʙѳѥ πѧҁϯƀ ɯπџҵ єѣƴӌџӣ ϯƀӀ ӌє ϯƴϯ ϯᴙʙκѧєɯƀ χƴӣʜᴙ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳєӣ ѣѧɯκѳӣ ҁƀӀʜκѧ ɯʌѥχџ єѣƴӌєґѳ ʙ ѻƴϯѣѳʌ џґⱀѧʌџ χƴʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ πƴϯѧʜƀӀ ӡʌѳєѣƴӌџӣ ʜѧχƴӣ ϯƀӀ κѧκ κⱀѳϯ єѣѧʜƀӀӣ џѱєɯƀ ʍѳґџʌƴ ҁʙѳєӣ ʍѧϯєⱀџ πⱀѳҁϯџϯƴϯκџ ѳϯъєѣѧʜѳӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ϯƴϯ єѣѧʌ ѧ ϯƀӀ đѳ ҁџχ πѳⱀ ʜє ʙκƴⱀџʌ χƴʌџ ѳʜѧ ϯѧκѧᴙ ҁӌѧҁϯʌџʙѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍʜє ӌʌєʜ ҁѳҁѧʌѧ ϯʙѳᴙ ʍѧϯєⱀƀ єѣѧʌѳʍ ϯʙѳєґѳ πѧπѧɯџ ʙƀӀҁⱀѧϯѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ ϯʙѳєӣ ʍѧʍӡєʌʌџ ѻѧⱀɯ ӡѧʍƴϯџʍ κѳϯѳⱀƀӀӣ ϯƀӀ ҁѳѫⱀёɯƀ єѣƴӌџӣ ʙҁѳҁєⱀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧκⱀѳӣ єѣѧʌƀʜџκ πѳӡѳⱀџѱє єѣƴӌєє ϯʙѳѥ ʍѧϯƀ ϯƴϯ ʜѧ ʍᴙҁѳκѳʍѣџʜѧϯ єѣѧʜƀӀӣ πƴҁϯџʍ єҁʌџ ѣƴđєɯƀ ʙƀӀёѣƀӀʙѧϯƀҁᴙ ӌƴⱀκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ χƴє ϯʙѳѥ ʍѧϯƀ đєⱀѫƴ κѧκ ʜѧ ҵєπџ єѣѧʜѳґѳ ѣƴʌƀđѳґѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ϯƀӀ ϯєⱀπџɯƀ ʍєʜᴙ єѣѧʜƀӀӣ ʙƀӀѣʌᴙđѳκ χѧ-χѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѳϯъєѣѧʌ џ πⱀѳҁϯⱀєʌџʌ єӣ ӌєⱀєπ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѳґѧ ʌѳʍѧєʍ ϯє ʜѧ ӌѧҁϯџ ѣѧⱀѧʜ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ єѣƴӌѧᴙ ʍⱀѧӡѳϯѧ ѣƴđєɯƀ κѧѫđƀӀӣ đєʜƀ πџӡđƀӀ πѳʌƴӌѧϯƀ ƴʜџѫєʜѳє ӌѧđѳ ҁʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁπєⱀʍѧ ʜѧ єѣѧʌѳ ϯʙѳєӣ ʍѧʍѧɯџ ʙѧʌџϯ єѣѧʜƀӀʍ ґⱀѧđѳʍ ҁƴκѧ κѧκ πѳđ đѳѫđєʍ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϶ϯѳӣ πⱀѳʙѳκѧҵџєӣ ᴙ ⱀʙѧʌ ʙѳʌѳҁƀӀ ʜѧ πџӡđє ϯʙѳєӣ ʍѧʍƴʌџ ƴґѧɯєʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌєʙѳє κѳʌєʜѳ ϯє ʜѧχƴӣ ʙƀӀѣƀѥ ʜѧⱀƴѫƴ єѣƴӌџӣ ϯƀӀ ҁƴκџʜ ҁƀӀʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ đѳχʌѳӣ ʍѧϯєⱀџ ҁѳѣѧκє єѣѧʜѳӣ ʍѳʜϯџⱀѳʙκѳӣ πѳ єѣʌƴ πєⱀєπџӡđџʌ џ πѳ πєӌєʜџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ɯʌѥχƴ єѣѧʌ ʜѧκƴⱀџʙɯџҁƀ ʍџκҁѧʍџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ϯʙѳё ӌƴʍѧӡѳє єѣʌџѱє đѧʌ ѳϯҁєӌκƴ ҁ ʙƀӀχʌѳπѧ πѳ єѣѧʌƴ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ κѳⱀѳϯκѳʜѳґџӣ ҁƀӀʜ ѣʌᴙđџʜƀӀ πѳɯёʌ ʜѧχƴӣ ѳϯҁѥđѧ ᴙ ϯєѣє ʙҁє κєґʌџ ʙƀӀκⱀƴӌƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʙƀӀєѣѧʜѧᴙ ʍѳџʍ ӌʌєʜѳʍ ҁϯѳ ⱀѧӡ ɯѧѣѳʌđѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ᴙ ϯʙѳѥ ʍѧʍƴ єѣѧʌ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ϯƴϯ ʙ ʍƴκѧχ ƴϯѳʜєɯƀ ʙʍєҁϯє ҁ ʜєӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧҁⱀѧʌџ ʜѧ єѣʌѳ ϯʙѳєӣ ʍѧϯƴχє πѳκѧ ϶ϯѧ ѳѣєӡƀᴙʜѧ єѣѧʜѧᴙ ѣєӡ ҁѳӡʜѧʜџᴙ ѣƀӀʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙ πџӡđѧӌџʜƴ ҁκѳⱀѳҁϯⱀєʌƀʜѳ єѣѧʌ ɯʌѥɯџӣ ҁƀӀʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁʜѧᴙ ɯʌѥχѧ ӌʌєʜ џӡѳ ⱀϯѧ ʙƀӀҁƴʜƀ ѳҁʌџχѧ єѣѧʜѧᴙ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ χƴёʍ ʙѳ ⱀϯƴ ӌє ҁπџӡđѧʜєɯƀ ҁƀӀʜџɯκѧ ѫѧʌκѳӣ ɯѧѣѳʌđƀӀ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁπєⱀʍѳʙƀӀκџđƀӀɯƀ єѣѧʜƀӀӣ ʍѧʍѧɯє ϯʙѳєӣ πѳđ ґƴѣƴ ӡѧʌƴπƴ ʜѧⱀƴʌѥ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʜџʌƀӀє ѳⱀґѧʜƀӀ ϯʙѳєӣ єѣѧʜѳӣ ʍѧϯƴχџ ʜѧѻѧⱀɯџⱀƴєʍ џӡʜƴϯⱀџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ӌєʌѥҁϯƀ ʙƀӀđєⱀʜƴ ҁʙѳєӣ ӡѧʌƴπѳӣ ѳϯҁѳҁєⱀɯѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ ϯʙѳєӣ ѳϯѣџϯѳӣ ѣѧɯκџ πѳҁʌєđʜџє ѳҁϯѧϯκџ ϯʙѳєґѳ ʍѳӡґѧ ʙƀӀѣџʙѧєʍ ϯєѣє ӌєⱀєӡ ϯʙѳѥ ʙƀӀєѣѧʜƴѥ ⱀѳϯѳʙƴѥ πѳʌѳҁϯƀ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧҁџʌƀʜѳ ӡѧҁϯѧʙʌѥ ҁѳѫⱀѧϯƀ ѳҁκѳʌκџ ґѳⱀᴙӌєґѳ ҁϯєκʌѧ єѣѧʜѧᴙ ɯєʌƀʍѳʙѧᴙ ɯʌѥχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґџđⱀѳҵєѻѧʌ єѣѧʜƀӀӣ ѳπƴҁϯџʍ ϯєѣᴙ ʜџѫє πʌџʜϯƴҁѧ ƴёѣџѱє ґѧʌџʍѳє ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀʙєʍ ϯʙѳџ χⱀƴҁϯѧʌƀʜƀӀє ҁƴҁϯѧʙƀӀ ҁ ϯⱀєҁκѳʍ єѣѧʜƀӀӣ πџđѳⱀѧҁ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ κѧκ єѣѧʜѳґѳ ѣѧⱀѧɯκѧ ɯѳʜѧ ϯєѣᴙ ϯƴϯ ӡѧєⱀєѫєʍ єѣѧʜѳє ϯƀӀ ҁƴκѧ ʍᴙҁѳ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯє đёҁʜѧ ʙƀӀⱀєӡѧʌ ʜѧⱀƴѫƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ʙƀӀⱀƴѣџʌ ʜѧ πѳπѳʌѧʍ ӌєⱀєπ ҁ πҁџχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯʙѳѥ ʙƀӀєѣѧʜƴѥ ʍѧϯєⱀƀ џӡѣџϯƴѥ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ єѣѧʌƀʜџκѧ џ đѳ κѳπƀӀϯ ϯєѣᴙ ϯƴϯ ʙ ҁπєⱀʍƴ ѳκƴʜєʍ ϯєⱀπџʌƀʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πⱀѳҁϯѳ єѣѧʜƀӀӣ ѳѣџѫєʜʜƀӀӣ ҁѳπʌёʜƀӀɯƀ џ ʜє ѣѳʌєє ϯѳґѳ єѣƴӌџӣ ґʌџʜѳʍєҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳđѧʙʌᴙєʍ ϯʙѳѥ ʜџӌєґѳ џӡ ҁєѣᴙ ʜє πⱀєđҁϯѧʙʌᴙѥѱƴѥ ʌџӌʜѳҁϯƀ ҁƀӀʜκѧ ɯʌѥχџ ƴʜџѫєʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌџҁϯѳ єѣѧʜƀӀӣ ѳϯʍєҁѳκ κѳϯѳⱀƀӀӣ ʍѳӣ χƴӣ ҁѳҁєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ⱀєӡѧʌ ѳʜѧ єѣѧʜѧᴙ ӌƴⱀκѧ ӡѧπƴґѧʜƀӀӣ ҁƀӀʜƴʌƀκѧ πⱀѳѣʌᴙđџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѣʌᴙđџʜƴ ʜѧχƴӣ ӡѧđƴɯџʌ πѳκѧ ѳʜѧ ҁπѧʌѧ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ϯʙѳєʍ єѣʌџѱє ɯⱀѧʍƀӀ ѳҁϯѧѥϯҁᴙ πѳҁʌє ϯѳґѳ κѧκ ᴙ đѧѥ ϯєѣє πџӡđƀӀ ʌѳχ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ґʌѧӡѧ ʙƀӀⱀєӡѧʌ ϯєπєⱀƀ ѳʜѧ џѱєϯ ʍѳӣ ӌʌєʜ ʜѧ ѳѱƴπƀ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙҁєʍƴ ϯʙѳєʍƴ ⱀѳđҁϯʙƴ єѣѧʜƀӀχ ʙƀӀѣʌᴙđκѳʙ ƴҁϯⱀѳѥ ʍѧҁҁѳʙѳє κⱀѳʙѳπⱀѳʌџϯџє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєѣᴙ ϯʙѳᴙ ѫє ʍѧϯƀ ɯʌѥχѧ χƴєҁѳҁџϯ ʜѳ ϯƀӀ єѣѧʜƀӀӣ ϯєⱀπџʌѧ џ ҁ ϶ϯџʍ ʜџӌє ʜє πѳđєʌѧєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ πѳʌƴʙƀӀєѣѧʜѳӣ ʍѧʍѧɯє κѧҁϯєϯѳʍ πѳ єѣʌџѱƴ đʙџʜƴʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ɯѧʌѧʙє ӌєⱀʜѳӣ ʜѧ ѫѳπє ʜѳѫѳʍ ҁʙѧҁϯџκƴ ʙƀӀҵѧⱀѧπѧʌ ϯѧđѫџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯƀӀ ʍʜє ӌʌєʜ ҁѳҁѧʌ ʜѧ ʍѧӣđѧʜє єѣʌѧʜџѱє ϯƴπѳⱀƀӀʌѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ϯⱀѧχѧʌ ʜѳʜ-ҁϯѳπʜѳ ӌџҁϯѳ ʜѧχƴӣ ѻѧҁϯѳʍ єӣ ѧʜѧʌ ⱀѧӡⱀѧѣѳϯѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ҁπєⱀʍѳχѧⱀʜѳӣ κѳҁϯџ ʙ πѧʌƀҵѧχ ʙӡъєѣƴ ѫѧʍѣѳʌѧϯ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ӡѧʌƴπѳӣ ʙ ҁʙѳєӣ χѧӌєʙҁκѳӣ ѫѳπє ӌє πџӡđєʌ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ѳκƴɯєⱀκџ єѣʌџʙƀӀӣ ᴙ ϯєѣє ʙҁє κƴđⱀџ ʜѧχƴӣ ʙƀӀđєⱀʜƴ єѣƴӌѧᴙ ҁκѳϯџʜѧ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ χѧⱀκѧʌƀʜџκ ϯєѣє ҁπєⱀʍѳӣ ʜѧҁҁѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ єѣѧʜƀӀӣ ʌѳχ ᴙ ϯʙѳё єѣѧʌѳ ʙƀӀєѣƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ ϯƴϯ ʍѳџ ᴙӣҵѧ єѣѧʜƀӀӣ ϯєⱀπџʌѳџđ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ ʙƀӀⱀʙƴ ѳϯ ҁʙѳєґѳ ӌʌєʜѧ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƀӀ ϯєѣє ʙʌѳʍџʌџ πѳ єѣʌџѱƴ χƴєҁѳҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ɯѧʌѧʙє ӡƴѣƀӀ ӌʌєʜѳʍ ӌџҁϯџʌ đѳ κⱀѳʙᴙκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜƴ-κѧ đѧʙѧӣ ҁƀӀʜ ɯʌѥχџ πѳҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє πѧđѧӣ đƴχѳʍ ҁʌѥʜᴙʙƀӀӣ χƴєґʌѳϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґđє ϯʙѳӣ ѳѣєѱѧʜʜƀӀӣ ʜѳʜ-ҁϯѳπ đѧƴʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ʜєđѳʜѳʜ-ҁϯѳπєⱀ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧχχѧχѧ ӌƴⱀκѧ єѣѧʜѧᴙ ӡѧκⱀѳӣ ⱀƀӀʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ѣƴđєɯƀ ʍєʜᴙ κѧѫđƀӀӣ đєʜƀ ϯƴϯ ϯєⱀπєϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴɯѧҁϯƀӀӣ ʙƀӀѣʌᴙđѳκ ѳϯҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍʜє πѳχƴӣ ʜѧ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ӌѧҁ ʜє πѳκѧѫџ ҁʌƀӀɯƀ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʍѧϯƀ єѣѧʌ κʌѳƴʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧ ϯƀӀ ϯєⱀπџʌѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁҁƴ ʙ ϯʙѳё єѣѧʌѳ ϯƴϯ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳҁϯџ ϯє ҁʌѳʍѧєʍ єƴ πџđѳⱀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѳʌƴѣѳӣ ҁƀӀʜ ɯʌѥχџ ʙҁѳҁџ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџđѳⱀѧҁϯʜᴙ ϯƀӀ ѳϯҁѳҁџ ƴѫє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳɯєʌ ʜѧχƴӣ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ϯƀӀ ϯѧκѳӣ ϯєⱀπџʌѧ єѣѧʜƀӀӣ ϯƀӀ ѫє ӌџҁϯѳ ϯƴϯ χѧⱀӌƴ єѱє ⱀѧӡ ʙ ⱀƀӀʌѳ πѳʌƴӌџɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯƀӀ ҵєʌƴєɯƀ ʙ πџӡđƴ ҁʙѳѥ ʍѧϯєⱀƀ ѣʌᴙđƀ ᴙ ѫє κѳʜӌѧʌ ϯƴđѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣƴӌџӣ ҁʍѳⱀӌѳκ ϯƀӀ ҁ κєʍ πƀӀϯѧєɯƀҁᴙ ҁѳπєⱀʜџӌѧϯƀ ʜƀѥҁκƴʌʌ ʙƀӀёѣџҁϯƀӀӣ ᴙ ϯєѣᴙ ϯƴϯ ҁ ʜѳґ đѳ ґѳʌѳʙƀӀ ӌџҁϯѳ ӡѧҁҁƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯєⱀџ ϯʙѳєӣ ѫџⱀʜѳӣ ɯʌѥχџ ʙ πџӡđƴ ѳѣⱀѧϯʜѳ κƴӌѧ đєⱀƀʍѧ ѳϯʌєϯєʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙҁё ϯʙѳє πѳʍᴙϯѳє єѣʌџѱє ӌєⱀʜѳє ӡѧʌƴπѧʍџ ѳѣʌѳѫƴ ϯƴϯ ҁƀӀʜ ɯʌѥχџ ʍѧʍѧɯƴ ϯʙѳѥ ѳϯπџđѳⱀѧҁџʍ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ϯʙѳё ʍєⱀϯʙѳє єѣѧҁѳҁџѱє ʙ đʙѧ ӌʌєʜѧ ϯⱀѧχʜєʍ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁⱀѧӌєʌƀʜџκ ϯʙѳєӣ ѳѣκѳʜӌєʜѳӣ ʍѧʍƴʌє ɯѧʌѧʙє ʙƀӀєѣƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ ӌєⱀєπʜѳ ʍѳӡґѳʙѧᴙ ѳϯ ƴđѧⱀѧ ӡѧʌƴπѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙҁє ϯʙѳџ ѳⱀґѧʜƀӀ џ ϯʙѳѥ ϯƴɯƴ ʙ κⱀѳʙƀ ⱀѧӡⱀєѫƴ ʜѧχƴӣ ʍⱀѧӡƀ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀχʌѳπʜƴѥ ҁџҁϯєʍƴ ϯʙѳєӣ ʍѧʍƴʌє ɯʌѥχє πєⱀєχƴᴙⱀџʍ πѧӌκѧʍџ ӡѧʌƴπ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧκʌџ ʙƀӀⱀʙєʍ πєϯƴɯκƴ єѣѧʜѳʍƴ ӡѧ єґѳ ʌџɯʜџє ʙƀӀєѣѳʜƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ πѳʌƴʍёⱀϯʙѳӣ ʍѧϯєⱀџ ʙҁє κѳҁϯџ ϯƴϯ πєⱀєҁӌџϯѧѥ πѳєѣѳϯѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ҁ ѳѣκѳʜӌєʜƀӀʍ єѣʌџѱєʍ ϯƀӀ κƴđѧ πѳ ϯѧπκѧʍ ϯѧʍ ʙъєѣѧʌ џɯѧκ єѣƴӌџӣ ϯƀӀ ϯƴϯ ѣƴđєɯƀ ҁϯⱀѧđѧϯƀ κѧѫđƀӀӣ đєʜƀ ʙ ʍѳєʍ πⱀџҁƴϯҁϯʙџџ ӌƴⱀκѧɯ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đⱀѳӌџʌʌѧ єѣѧʜƀӀӣ đѧʙѧӣ ѳϯҁѳҁџ ʍѳѥ χƴᴙⱀƴ ⱀєѱє ҁʌƀӀɯƀ ⱀєκҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ єѣѧʜƀӀӣ ᴙ ϯʙѳєӣ ʍѧʍѧɯє ʜѧ ґƴѣƴ ӡѧʌƴπƴ ʜѧκџđѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ѧʜѧʌƀʜѳӣ đƀӀⱀє ϯʙѳєӣ ʍѧϯƴχџ πⱀѳҁϯџϯƴϯκє єѣѧʜѳӣ κⱀєҁϯ ʙƀӀҵѧⱀѧπѧʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ ѧɯѳϯ єѣѧʜƀӀӣ ҁ ѳʙѳѱʜѳґѳ ⱀƀӀʜκѧ єѣѧʌџѱє ҁʙѳє ƴⱀѳʜџ ᴙ ϯєѣє πѳӡʙѳʜѳӌʜџκ ʜѧχƴӣ ʙƀӀʌѳʍѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙ ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯκџ ɯʌѥχџ πⱀᴙʍѳϯѳκ πƴҁϯџʌ ѳʜѧ κѳʜџ đʙџʜƴʌѧ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ӡѧ ϯⱀѥκџ ҁʙѳџʍ єѣѧʌƀʜџκѳʍ ӌƴʍʜƀӀʍ πⱀѳʙѳⱀѧӌџʙѧєɯƀ ҁ ʍѳџʍ ӌʌєʜѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ πѳʌƴπѳκєⱀ єѣѧʜƀӀӣ ӡѧѣƀӀʌ κϯѳ ϯєѣє đѧʌ χƴӣ ѳϯҁѳҁѧϯƀ πџđѳⱀѧҁ єѣѧʜƀӀӣ ѱѧҁ πѳʙϯѳⱀџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєѣє ϯʙѳᴙ ʍѧʍѧɯѧ ɯѧʌѧʙѧ ґѳʙѳⱀџʌѧ ʍєʜƀɯє πџӡđџ χƴӣʜџ ѧ ϯƀӀ єё ʜє ҁʌƴɯѧʌ ϯєπєⱀƀ πѳʌƴӌѧӣ ʙ єѣѧҁѳҁџʜƴ πџӡđƀӀ ӡѧʌƴπѧʙɯџӣҁᴙ ҁƀӀʜџɯκѧ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣʌџѱє ϯʙѳё ƴѫє ʜѧ ґѳϯѳʙє ѳϯҁѳҁѧϯƀ ʍʜє χƴӣ πӡđҵ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ πѳđҁѳҁ єѣƴӌџӣ χƴʌџ ϯƀӀ πѧʌџɯƀ ʍʜє ʙ ᴙӣҵѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧκⱀѳӣ ҁʙѳѥ πѧҁϯƀ ɯπџҵ єѣƴӌџӣ ϯƀӀ ӌє ϯƴϯ ϯᴙʙκѧєɯƀ χƴӣʜᴙ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳєӣ ѣѧɯκѳӣ ҁƀӀʜκѧ ɯʌѥχџ єѣƴӌєґѳ ʙ ѻƴϯѣѳʌ џґⱀѧʌџ χƴʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ πƴϯѧʜƀӀ ӡʌѳєѣƴӌџӣ ʜѧχƴӣ ϯƀӀ κѧκ κⱀѳϯ єѣѧʜƀӀӣ џѱєɯƀ ʍѳґџʌƴ ҁʙѳєӣ ʍѧϯєⱀџ πⱀѳҁϯџϯƴϯκџ ѳϯъєѣѧʜѳӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ϯƴϯ єѣѧʌ ѧ ϯƀӀ đѳ ҁџχ πѳⱀ ʜє ʙκƴⱀџʌ χƴʌџ ѳʜѧ ϯѧκѧᴙ ҁӌѧҁϯʌџʙѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍʜє ӌʌєʜ ҁѳҁѧʌѧ ϯʙѳᴙ ʍѧϯєⱀƀ єѣѧʌѳʍ ϯʙѳєґѳ πѧπѧɯџ ʙƀӀҁⱀѧϯѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ ϯʙѳєӣ ʍѧʍӡєʌʌџ ѻѧⱀɯ ӡѧʍƴϯџʍ κѳϯѳⱀƀӀӣ ϯƀӀ ҁѳѫⱀёɯƀ єѣƴӌџӣ ʙҁѳҁєⱀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧκⱀѳӣ єѣѧʌƀʜџκ πѳӡѳⱀџѱє єѣƴӌєє ϯʙѳѥ ʍѧϯƀ ϯƴϯ ʜѧ ʍᴙҁѳκѳʍѣџʜѧϯ єѣѧʜƀӀӣ πƴҁϯџʍ єҁʌџ ѣƴđєɯƀ ʙƀӀёѣƀӀʙѧϯƀҁᴙ ӌƴⱀκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ χƴє ϯʙѳѥ ʍѧϯƀ đєⱀѫƴ κѧκ ʜѧ ҵєπџ єѣѧʜѳґѳ ѣƴʌƀđѳґѧ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯѧѣѳʌđѧ єѣƴӌѧᴙ ʜѧ ʍѳєӣ χƴᴙⱀє ʙєʜƀӀ ҁєѣє ʙҁκⱀƀӀʌѧ џđџѳϯџʜѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѣѧҁʜѳҁʌѳʙʜѳ ѳϯѣџʌ πѳ ѣєđⱀѧʍ κѳⱀѳʙƴ єѣѧʜƴѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʜѳʙѧ ϯʙѳᴙ ѣєđʜѧᴙ ӡѧєѣѧɯєʜѧᴙ ʍѧϯƴɯκѧ πѳʌƴӌѧєϯ πџӡđƀӀ ѳϯ ʍєʜᴙ ѣƴχџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳѣѳҁҁƀӀʍ єѣƴӌєґѳ ҁѧʌѧґƴ ӡѧ єґѳ ѣѧӡѧⱀ ҁ ʜѳґ đѳ ґѳʌѳʙƀӀ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χʌѥπџκ єѣƴӌџӣ πѳӣʍџ ӌϯѳ ᴙ ϯєѣє ʙ ƴɯџ ʜѧҁҁƴ ӡѧ ϯʙѳџ ʙƀӀєѣѳʜƀӀ ӌƴⱀκѧѣєҁ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯƴχє ʜѧπѳⱀџʍ ӡѧʌƴπѧʍџ đѳ πѳӌєⱀʜєʜџӣ ӌєⱀʜѳєѣƴӌєӌʜƀӀӣ ҁƀӀʜƴʌᴙ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌєґєʜđѧ χѳӡᴙџʜ ϯʙѳѥ ʍѧϯƀ ʙ ѳӌκѳ πєⱀєєѣѧʌ ҁϯѳ ⱀѧӡ ѳʙҵєєѣ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ҁґʜџʙɯƴѥ ʍѧʍѧɯƴ ʙ єѣѧҁѳҁџџѱє ѳϯъєѣƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧ џđџ πєϯƴχ єѣѧʜƀӀӣ ϯʙѳѥ ʍѧʍѧɯƴ ϯƴϯ ѳϯъєѣєʍ ʙ ѳϯҁєӌκƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϶ϯџʍџ ҁʌѳʙѧʍџ ѳϯъєѣѧʌџ ϯƴχʌƀӀӣ ϯⱀƴπ ϯʙѳєӣ ʍѧʍѧɯџ ѫʍƴⱀ ϯƀӀ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ʙ ⱀѳϯ πѳⱀѳʌ ϶ƴ ӌƴđѧκ єѣѧʜƀӀӣ πѳʌƴӌџ ʌєѱѧ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϯⱀƴπѧ ϯʙѳєӣ ʍѧϯєⱀџ χѧ-χѧ ϯƴϯ ʌѳʙџʍ ѳϯ єё πⱀѳҁϯⱀєʌєʜʜѳґѳ єѣѧʌƀʜџκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ҁʌѧѣƀӀӣ ӡѧєѣєɯƀҁᴙ ϯƴϯ ѳϯ πџӡđѥʌєӣ ѳϯѣџʙѧϯƀҁᴙ πѳҁϯѳᴙʜʜѳ ⱀєκҁџѱє єѣƴӌєє ϯƀӀ đѧʙѧӣ ϯѧʍ κѧӣѻƀӀ ʜє ʌѳʙџ џ ҁѳҁџ ʍѳӣ ѫџⱀʜƀӀӣ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯєⱀƀ ϯʙѳєӣ ѳϯѳⱀʙѧʜѳӣ ʜѳґѳӣ єѣѧʌ πѳκѧ ϯƀӀ ʜƀӀʌ ҁѳπʌᴙκ ϯєⱀπџʌƀʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ đƴʌѳ ʙđƴʌ ϯʙѳєӣ ʍѧʍѧɯџ ҁƀӀʜ ɯʌѥχџ ӡʌѳєѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯъєѣєʍ χѧӌєʙҁκџӣ ϯʙѳџʍ ѫѧʌκџʍ πⱀєđκѧʍ πѳʌƴπѳκєⱀѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ϯʙѳѥ ʍѧϯƀ ʜѧ đʙџѫʜᴙκѧχ єѣƴ ʙҁєґđѧ џ ʙєӡđє ϯєⱀπџʌѧ ѳϯπџӡѫєʜʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϶ϯѳӣ πⱀѳʙѳκѧҵџєӣ ᴙ ѳѣκѳʜӌѧʌ πѳʌѳʙƀӀє ґƴѣƀӀ ϯʙѳєӣ ʍѧϯєⱀџ ҁƀӀʜѳκ πƴϯѧʜƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ ʙ ʍѧⱀϯџʜҁѧχ є6ѧʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ πѳđ ʍєϯѧđѳʜѳʍ ѳϯъєѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ƴɯџ ҁҁƀӀʍ ϯє ҁƀӀʜѳκ ɯʌѥχџ ѳχƴєʙɯџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳҁϯџ ϯʙѳџ ʙ ӌєʌѥҁϯƀ ϯєѣє ʜѧґⱀƴӡџʍ ʙѧѻєʌƀ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ҁƀӀʜѳκ ɯʌѥχџ єѣѧʌѳ ʙƀӀɯє ҁʙѳє πѳđκⱀƴϯџ đƴχ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ҁƀӀʜƴʌᴙ ɯʌѥχџ ᴙ ϯєѣᴙ đѳ ҁʌєӡ ʙʜѧϯƴⱀє đѳʙєđƴ ҁʌѧѣѧκ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧ ҁϯⱀѳӣѣѧϯє єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ɯʌѥχџ ҁҁѧʜƀӀӣ ʙ ɯѧⱀƀӀ ϯѧʍ ѳѣъєѣѧʌҁᴙ џʌџ ӌє πџđѳⱀѧҁ єѣѧʜƀӀӣ ϯʙѳѥ ʍѧϯƀ ʜѧ κѳʌєʜџ ϯƴϯ ѳπƴҁϯџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πᴙϯκџ ϯʙѳєӣ ʍѧʍѧɯє ҁѳѫѫєʍ ʙʍєҁϯє ҁ єё πџӡđѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʌѳϯκƴ ϯʙѳєӣ ʍѧʍѧɯє χƴᴙʍџ πєⱀєκⱀѳєʍ ѱєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯ ʍѳєӣ ӡѧʌƴπƀӀ єѣʌџѱє ϯʙѳєӣ ʍѧϯєⱀџ κƴʍѧϯѳӡџϯ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѧⱀƀ єѣѧʜѧᴙ πѳ ϯⱀƴπƴ ϯʙѳєӣ ʍѧϯєⱀџ πⱀѳӣđƴҁƀ ϯƴϯ ґʜџđѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џʜɯѧʌѧ єѣѧʜƀӀӣ ƴёѣƀӀʙѧӣ ʜѧχƴӣ ѳϯҁѥđѧ ʜџӌϯѳѫʜѧᴙ πѧџʜƀκѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƴκѧ ƴʍҁϯʙєʜʜѳ ѳϯҁϯѧʌƀӀӣ đѧƴʜ ʙ ⱀѧӡʙџϯџџ đѧʙѧӣ ᴙ ϯєѣє єѱє ҁџʌƀʜєє ґѳʌѳʙƴ ѳϯѳѣƀѥ ѻѳⱀɯʍѧκ єѣѧʜƀӀӣ ӌџҁϯѳ ѣƴđєɯƀ ѫџⱀ ϯƴϯ ҁʙѳӣ ѫє ӡѧ ѳѣє ѱєκџ ƴπʌєϯѧϯƀ χƴєϯѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϶ϯѳӣ πⱀѳʙѳκѧҵџєӣ ᴙ κѳʜӌџʌ ʜѧ κѧđƀӀκ ϯʙѳєӣ ʍѧϯƴχџ πⱀѳҁϯџϯƴϯκє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯƴѻϯѧ ƴʜƀӀʌѧᴙ ᴙ ϯєѣє ⱀѳґѧ ҁʌѳʍѧѥ ϯƴϯ ӡѧ ϯʙѳӣ ѣѧӡѧⱀ πєϯƴχ єѣѧʜƀӀӣ єѣʌџѱє ҁʙѳё ʜѧχƴӣ ӡѧʙѧʌџ ɯєⱀҁϯƀ єѣƴӌѧᴙ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ʙ ʌєѻѳⱀϯѳʙѳ єѣѧʌ πѳđ ѧʜđєґⱀѧƴʜđ πѧⱀѧɯʜџκ ϯƀӀ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳʌƴӌџ πѳ єѣѧʌƀʜџκƴ ӌƴđѳʙџѱє єѣѧʜѳє ʍѧϯƀ ϯʙѳѥ πѳϯⱀѧχѧєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєⱀєπ ϯє πⱀѳѣƀѥ ɯѧκѧʌ єѣѧʜƀӀӣ ϯʙѳᴙ ʍѧʍѧ ɯʌѥχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴҁκѳⱀѳӣҁᴙ đѧʙѧӣ ƴʌџϯκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍєđʌєʜʜƀӀӣ ҁƀӀʜ ɯʌѥχџ ϯƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀєѱє πџɯџ ҁƀӀʜ ӌƴⱀκѧɯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍѧϯƀ ѣʌᴙđџʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ʍѧϯєⱀƀ ϯʙѳѥ ҁπєⱀʍѳӣ џӡ κʌџӡʍƀӀ ʜѧκѳʜӌѧʌ ґѳʙʜѧⱀƀ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ӌƴⱀκє єѣѧʜѳӣ ѫєʌƴđѳκ ҁʙѳєӣ ʍѳӌѳӣ πⱀѳʍƀӀʌ ʜѧҁҁѧʙ єӣ ʙ πѧҁϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ єѣƴӌџӣ ӌєⱀʙᴙκ ʙ џӡѣџϯѳӣ ѫѳπє ҁʙѳєӣ ʍѧϯєⱀџ πⱀѳҁϯџϯƴϯκџ ѳѣџϯѧєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ πѳđ ѣєđ ϯⱀџπѳʍ πѳκѧ ϯƀӀ ʜƀӀʌ ʍʜє ʙ ᴙӣҵѧ ѳѣѳҁⱀѧʜƀӀӣ ѳҁєʌ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣʌџѱє ѳѣ ҁʙѳӣ χƴӣ ϯƴϯ πѳϯƴɯƴ κѧκ ӌёⱀʜƴѥ єѣѧʜƴѥ ҁџґѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧ ʍѳёʍ ӌʌєʜє ҁκѧӌєɯƀ κѧκ κєʜґƴⱀƴ єѣƴӌџӣ ҁѳ ҁʙѳєӣ ʍѧϯєⱀƀѥ πѳđ πѧχѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣᴙ єѣѧʌ κѧҁϯⱀџⱀѳʙѧʜʜѳґѳ єʙʜƴχѧ єѣѧʜѳґѳ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєđѧʌџ ϯʙѳєӣ ҁєʍƀє ӌƴⱀκѧʜѳʙ ѳϯъєѣѧʜƀӀχ ҁ χⱀƴҁϯѳʍ πџӡđџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ѳϯҁѳҁѧʙɯџӣ đѧʙѧӣ ʍѳџ ᴙӣҵѧ πѳ ʙϯѳⱀѳʍƴ κⱀƴґƴ ѳϯʌџѫџ ϯƴϯ ӌёⱀϯ єѣѧʜƀӀӣ ҁƴκѧ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ πџӡđƀӀ ϯʙѳєӣ κѳʜӌєʜѳӣ ʍѧʍѧɯџ κⱀѳʙƀ єѣѧɯџϯ ʜѧ єѣѧʌƀʜџκ ϯʙѳєӣ ϯєʌκє ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ѫѳπѧʌџӡ єѣѧʜƀӀӣ ʜѧπⱀᴙґџ ҁʙѳџ ʍєʌκџє џӡʙџʌџʜƀӀ џ ѳϯҁѳҁџ ʍѳӣ ӡđѳⱀѳʙƀӀӣ ӌʌєʜ ҁѳ ҁʙѳєӣ ʍѧʍѧɯєӣ ʜѧ πѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κџɯκџ џӡ ѣⱀѥχѧ ϯʙѳєӣ ʍѧϯєⱀџ ɯѧʌѧʙƀӀ ʙƀӀѣƀєʍ ϯѧκ ӌϯѳ ѳʜџ ӌєⱀєӡ πџӡđƴ ƴ ʜєё πƴʌєӣ πѳʌєϯᴙϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ ʜѧ ҁʜєґƴ ʙ ᴙʜʙѧⱀє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳӣ ѳϯєҵ ӡѧɯџϯѳє ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀʌџӡѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ɯʌѥχƴ ӡѧʌƴπѳӣ ʙ ѣѳκ πџχѧʌ πѳ πєӌєʜџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ϯʙѳё єѣѧʌџѱє ʍѳӌƴ ϯʙѳєӣ ҁѳѣѧκџ ʙƀӀʌƀѥ πџđѳⱀџʌʌѧ ƴɯѧҁϯƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʌƴπѳӣ ʙ ϯʙѳӣ ʍєⱀӡκџӣ єѣѧʌƀʜџκ πⱀѳⱀʙѧʌҁᴙ ҁ ⱀѧӡʍѧχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ʙҁϯѧʙʜƴѥ ӌєʌѥҁϯƀ ʙƀӀⱀʙƴ ҁ κⱀѳʙƀѥ џ ʍᴙҁѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ϯʙѳё єѣѧʌѳ ʜѧ κƴⱀѳκ ʜѧѫʍƴ ҁƀӀʜᴙⱀѧ ɯʌѥχџ ӡʌѳєѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀʙєʍ ϯʙѳѥ ѳϯѣџϯƴѥ ϯƴɯƴ ѳπƴѱєʜʜѳӣ ϯєⱀπџʌƀӀ ʜѧ ʍєʌκџє κƴҁκџ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ϯƀӀ ϯєⱀπџɯƀ ʍєʜᴙ єѣѧʜƀӀӣ ʙƀӀѣʌᴙđѳκ χѧ-χѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѳϯъєѣѧʌ џ πⱀѳҁϯⱀєʌџʌ єӣ ӌєⱀєπ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѳґѧ ʌѳʍѧєʍ ϯє ʜѧ ӌѧҁϯџ ѣѧⱀѧʜ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ єѣƴӌѧᴙ ʍⱀѧӡѳϯѧ ѣƴđєɯƀ κѧѫđƀӀӣ đєʜƀ πџӡđƀӀ πѳʌƴӌѧϯƀ ƴʜџѫєʜѳє ӌѧđѳ ҁʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁπєⱀʍѧ ʜѧ єѣѧʌѳ ϯʙѳєӣ ʍѧʍѧɯџ ʙѧʌџϯ єѣѧʜƀӀʍ ґⱀѧđѳʍ ҁƴκѧ κѧκ πѳđ đѳѫđєʍ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ϶ϯѳӣ πⱀѳʙѳκѧҵџєӣ ᴙ ⱀʙѧʌ ʙѳʌѳҁƀӀ ʜѧ πџӡđє ϯʙѳєӣ ʍѧʍƴʌџ ƴґѧɯєʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌєʙѳє κѳʌєʜѳ ϯє ʜѧχƴӣ ʙƀӀѣƀѥ ʜѧⱀƴѫƴ єѣƴӌџӣ ϯƀӀ ҁƴκџʜ ҁƀӀʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ đѳχʌѳӣ ʍѧϯєⱀџ ҁѳѣѧκє єѣѧʜѳӣ ʍѳʜϯџⱀѳʙκѳӣ πѳ єѣʌƴ πєⱀєπџӡđџʌ џ πѳ πєӌєʜџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ɯʌѥχƴ єѣѧʌ ʜѧκƴⱀџʙɯџҁƀ ʍџκҁѧʍџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ϯʙѳё ӌƴʍѧӡѳє єѣʌџѱє đѧʌ ѳϯҁєӌκƴ ҁ ʙƀӀχʌѳπѧ πѳ єѣѧʌƴ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ κѳⱀѳϯκѳʜѳґџӣ ҁƀӀʜ ѣʌᴙđџʜƀӀ πѳɯёʌ ʜѧχƴӣ ѳϯҁѥđѧ ᴙ ϯєѣє ʙҁє κєґʌџ ʙƀӀκⱀƴӌƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʙƀӀєѣѧʜѧᴙ ʍѳџʍ ӌʌєʜѳʍ ҁϯѳ ⱀѧӡ ɯѧѣѳʌđѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ᴙ ϯʙѳѥ ʍѧʍƴ єѣѧʌ ҁƀӀʜ ɯʌѥχџ ϯƀӀ ϯƴϯ ʙ ʍƴκѧχ ƴϯѳʜєɯƀ ʙʍєҁϯє ҁ ʜєӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧҁⱀѧʌџ ʜѧ єѣʌѳ ϯʙѳєӣ ʍѧϯƴχє πѳκѧ ϶ϯѧ ѳѣєӡƀᴙʜѧ єѣѧʜѧᴙ ѣєӡ ҁѳӡʜѧʜџᴙ ѣƀӀʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙ πџӡđѧӌџʜƴ ҁκѳⱀѳҁϯⱀєʌƀʜѳ єѣѧʌ ɯʌѥɯџӣ ҁƀӀʜѳκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁʜѧᴙ ɯʌѥχѧ ӌʌєʜ џӡѳ ⱀϯѧ ʙƀӀҁƴʜƀ ѳҁʌџχѧ єѣѧʜѧᴙ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ χƴёʍ ʙѳ ⱀϯƴ ӌє ҁπџӡđѧʜєɯƀ ҁƀӀʜџɯκѧ ѫѧʌκѳӣ ɯѧѣѳʌđƀӀ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁπєⱀʍѳʙƀӀκџđƀӀɯƀ єѣѧʜƀӀӣ ʍѧʍѧɯє ϯʙѳєӣ πѳđ ґƴѣƴ ӡѧʌƴπƴ ʜѧⱀƴʌѥ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʜџʌƀӀє ѳⱀґѧʜƀӀ ϯʙѳєӣ єѣѧʜѳӣ ʍѧϯƴχџ ʜѧѻѧⱀɯџⱀƴєʍ џӡʜƴϯⱀџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ӌєʌѥҁϯƀ ʙƀӀđєⱀʜƴ ҁʙѳєӣ ӡѧʌƴπѳӣ ѳϯҁѳҁєⱀɯѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ ϯʙѳєӣ ѳϯѣџϯѳӣ ѣѧɯκџ πѳҁʌєđʜџє ѳҁϯѧϯκџ ϯʙѳєґѳ ʍѳӡґѧ ʙƀӀѣџʙѧєʍ ϯєѣє ӌєⱀєӡ ϯʙѳѥ ʙƀӀєѣѧʜƴѥ ⱀѳϯѳʙƴѥ πѳʌѳҁϯƀ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧҁџʌƀʜѳ ӡѧҁϯѧʙʌѥ ҁѳѫⱀѧϯƀ ѳҁκѳʌκџ ґѳⱀᴙӌєґѳ ҁϯєκʌѧ єѣѧʜѧᴙ ɯєʌƀʍѳʙѧᴙ ɯʌѥχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґџđⱀѳҵєѻѧʌ єѣѧʜƀӀӣ ѳπƴҁϯџʍ ϯєѣᴙ ʜџѫє πʌџʜϯƴҁѧ ƴёѣџѱє ґѧʌџʍѳє ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀʙєʍ ϯʙѳџ χⱀƴҁϯѧʌƀʜƀӀє ҁƴҁϯѧʙƀӀ ҁ ϯⱀєҁκѳʍ єѣѧʜƀӀӣ πџđѳⱀѧҁ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ κѧκ єѣѧʜѳґѳ ѣѧⱀѧɯκѧ ɯѳʜѧ ϯєѣᴙ ϯƴϯ ӡѧєⱀєѫєʍ єѣѧʜѳє ϯƀӀ ҁƴκѧ ʍᴙҁѳ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯє đёҁʜѧ ʙƀӀⱀєӡѧʌ ʜѧⱀƴѫƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ʙƀӀⱀƴѣџʌ ʜѧ πѳπѳʌѧʍ ӌєⱀєπ ҁ πҁџχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯʙѳѥ ʙƀӀєѣѧʜƴѥ ʍѧϯєⱀƀ џӡѣџϯƴѥ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ єѣѧʌƀʜџκѧ џ đѳ κѳπƀӀϯ ϯєѣᴙ ϯƴϯ ʙ ҁπєⱀʍƴ ѳκƴʜєʍ ϯєⱀπџʌƀʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πⱀѳҁϯѳ єѣѧʜƀӀӣ ѳѣџѫєʜʜƀӀӣ ҁѳπʌёʜƀӀɯƀ џ ʜє ѣѳʌєє ϯѳґѳ єѣƴӌџӣ ґʌџʜѳʍєҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳđѧʙʌᴙєʍ ϯʙѳѥ ʜџӌєґѳ џӡ ҁєѣᴙ ʜє πⱀєđҁϯѧʙʌᴙѥѱƴѥ ʌџӌʜѳҁϯƀ ҁƀӀʜκѧ ɯʌѥχџ ƴʜџѫєʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌџҁϯѳ єѣѧʜƀӀӣ ѳϯʍєҁѳκ κѳϯѳⱀƀӀӣ ʍѳӣ χƴӣ ҁѳҁєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ⱀєӡѧʌ ѳʜѧ єѣѧʜѧᴙ ӌƴⱀκѧ ӡѧπƴґѧʜƀӀӣ ҁƀӀʜƴʌƀκѧ πⱀѳѣʌᴙđџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѣʌᴙđџʜƴ ʜѧχƴӣ ӡѧđƴɯџʌ πѳκѧ ѳʜѧ ҁπѧʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ϯʙѳєʍ єѣʌџѱє ɯⱀѧʍƀӀ ѳҁϯѧѥϯҁᴙ πѳҁʌє ϯѳґѳ κѧκ ᴙ đѧѥ ϯєѣє πџӡđƀӀ ʌѳχ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ґʌѧӡѧ ʙƀӀⱀєӡѧʌ ϯєπєⱀƀ ѳʜѧ џѱєϯ ʍѳӣ ӌʌєʜ ʜѧ ѳѱƴπƀ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙҁєʍƴ ϯʙѳєʍƴ ⱀѳđҁϯʙƴ єѣѧʜƀӀχ ʙƀӀѣʌᴙđκѳʙ ƴҁϯⱀѳѥ ʍѧҁҁѳʙѳє κⱀѳʙѳπⱀѳʌџϯџє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєѣᴙ ϯʙѳᴙ ѫє ʍѧϯƀ ɯʌѥχѧ χƴєҁѳҁџϯ ʜѳ ϯƀӀ єѣѧʜƀӀӣ ϯєⱀπџʌѧ џ ҁ ϶ϯџʍ ʜџӌє ʜє πѳđєʌѧєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ πѳʌƴʙƀӀєѣѧʜѳӣ ʍѧʍѧɯє κѧҁϯєϯѳʍ πѳ єѣʌџѱƴ đʙџʜƴʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ɯѧʌѧʙє ӌєⱀʜѳӣ ʜѧ ѫѳπє ʜѳѫѳʍ ҁʙѧҁϯџκƴ ʙƀӀҵѧⱀѧπѧʌ ϯѧđѫџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯƀӀ ʍʜє ӌʌєʜ ҁѳҁѧʌ ʜѧ ʍѧӣđѧʜє єѣʌѧʜџѱє ϯƴπѳⱀƀӀʌѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ϯⱀѧχѧʌ ʜѳʜ-ҁϯѳπʜѳ ӌџҁϯѳ ʜѧχƴӣ ѻѧҁϯѳʍ єӣ ѧʜѧʌ ⱀѧӡⱀѧѣѳϯѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє ҁπєⱀʍѳχѧⱀʜѳӣ κѳҁϯџ ʙ πѧʌƀҵѧχ ʙӡъєѣƴ ѫѧʍѣѳʌѧϯ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ӡѧʌƴπѳӣ ʙ ҁʙѳєӣ χѧӌєʙҁκѳӣ ѫѳπє ӌє πџӡđєʌ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜ ѳκƴɯєⱀκџ єѣʌџʙƀӀӣ ᴙ ϯєѣє ʙҁє κƴđⱀџ ʜѧχƴӣ ʙƀӀđєⱀʜƴ єѣƴӌѧᴙ ҁκѳϯџʜѧ ӌџҁϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ χѧⱀκѧʌƀʜџκ ϯєѣє ҁπєⱀʍѳӣ ʜѧҁҁѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ єѣѧʜƀӀӣ ʌѳχ ᴙ ϯʙѳё єѣѧʌѳ ʙƀӀєѣƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ ϯƴϯ ʍѳџ ᴙӣҵѧ єѣѧʜƀӀӣ ϯєⱀπџʌѳџđ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ ʙƀӀⱀʙƴ ѳϯ ҁʙѳєґѳ ӌʌєʜѧ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƀӀ ϯєѣє ʙʌѳʍџʌџ πѳ єѣʌџѱƴ χƴєҁѳҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ɯѧʌѧʙє ӡƴѣƀӀ ӌʌєʜѳʍ ӌџҁϯџʌ đѳ κⱀѳʙᴙκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє πѳʌ ѣѧɯκџ ҁʜєҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫѧχʜєʍ ϯєѣᴙ ҁƀӀʜκѧ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ҁƀӀʜκƴ ɯʌѥχџ ҁ ʜѳґџ ӡƴѣƀӀ ʙƀӀѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ƴҁκѳⱀᴙӣҁᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀѫџʙѧӣ ϯƴϯ ҁƀӀʜ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧϯⱀѧχѧєʍ ϯєѣє ʍѧʍѧʜѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌƀʜџκ ӡѧʙѧʌџ πƴѣʌџӌʜѳ ƴʜџѫєʜѧᴙ ϯєʌκѧ єѣѧʜѧᴙ ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєđѧʌџ ѳϯѳѣƀєʍ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀπєⱀđʜƴϯƀӀӣ ґʌџҁϯ єѣƴӌџӣ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀπєⱀđƀӀɯƀ єѣѧʜƀӀӣ ᴙ ϯєѣє ⱀƀӀʌѳ ƴϯⱀƴ ϯƴϯ ʍⱀѧӡџѱє єѣѧʜѳє ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ɯѧʌѧʙє ѣєҁχⱀєѣєϯʜѳӣ ʙ ґѳʌѳʙƴ ӡѧєχѧʌ ӡѧʌƴπѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ϯʙѳё ӡѧπџʜѧʌ đѳ πѳκⱀѧҁʜєʜџӣ ҁѧʌѧґѧ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳєӣ ҁєʍєӣκє єѣѧʜƀӀχ ӌƴⱀѣѧʜѳʙ ѣѳɯκџ ѳϯѳⱀʙƴ ҁ πѳӡʙѳʜѳӌʜџκѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧʜƀκѧ ɯʌѥχѧ ʜѧ ʍѳєӣ ӡѧʌƴπє ӌџʌџϯ ӌџҁϯѳ đƴⱀѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧπџʜѧєʍ ѫџⱀʜƴѥ χⱀѥɯκƴ єѣѧʜƴѥ đѳ ҁƴѣҁϯѧʜҵџџ đєⱀƀʍџѱѧ ҁ ⱀƀӀґѳϯѳӣ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƴ ϯʙѳєӣ ϯёʌκџ ѳϯъєѣѧʌ ϯѧκ ӌϯѳ ѳʜѧ ƴ ʜєё πƴʌƀҁџⱀƴєϯ ϯєπєⱀƀ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌʌєʜ ӡѧ ѱєκƴ ҁєѣє πⱀᴙӌƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳєӣ ʍѧϯєⱀџ ʜѧ єѣʌѳ ʍџʌκɯєӣκ πƴҁϯџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʙҁѥ ѫџӡʜƀ ҁʌѳʍѧѥ χƴєҁѳҁ đƀӀⱀᴙʙƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧʍѳӌκƴ ϯʙѳѥ єѣєʍ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳє ҁκⱀџʙʌєʜʜѳє єѣʌџѱє ʙƀӀʜƴѫđєʜ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯƀ ϯѧκџχ đєϯєӣ ɯʌѥχ ʌџӌʜѳ єѣѧʌ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ҵєʌѳҁϯʜƴѥ πџӡđƴ πʌѳϯʜѳ πѳєѣѧʌџ đєʙκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ πѳđ ґџʍʜ Ƥѳҁҁџџ єѣѧʌ χƴʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ҁѳӌʜƴѥ ѫѳπƴ ʙєҁƀ ґѳđ ʌѳχ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍʜє ʙ ӌʌєʜ ʙҁᴙκƴѥ χƴӣʜѥ πџӡđџɯƀ ҁƀӀʜ ɯʌѥχџ ѳϯƴπʌєʜʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣѧʌѳ ʜѧ ѣџϯє єѣƴ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ єѣʌѧʜ ϯƴπѳґѳʌѳʙƀӀӣ ϯʙѳᴙ ʍѧϯƀ ҁѳҁєϯ ѣєӡ ⱀʙѳϯʜѳґѳ ⱀєѻʌєκҁѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƴκѧ đѧƴʜ ʜѧχƴӣ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ґʜџđƴ ϯƴπѳⱀƀӀʌƴѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧʌџʍƀӀӣ χƴєҁѳҁ, ᴙ ϯʙѳӣ ⱀѳϯ ʙ ƴπѳⱀ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʌѧӡʜƀӀє ᴙѣʌѳκџ ϯєѣє ʙƀӀκѳʌѥ ƴёѣџѱє ʜѧχƴӣ єѣѧʜѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯџɯƀ ϯⱀƴπ єѣѧʜƀӀӣ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ӌє ϯƀӀ ʜѳєɯƀ ѣʌᴙϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ʜѳκѧƴϯ ϯʙѳѥ ʍѧϯƀ ѳϯπⱀѧʙџʌ ƴđѧⱀѳʍ ӡѧʌƴπƀӀ πѳ єѣѧʌƴ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ єѣѧʌƀʜџκє ϯʙѳєӣ ʍѧʍѧɯє ʙƀӀⱀєӡѧʌ đѧϯƴ ϯʙѳєӣ ҁʍєⱀϯџ ҁƀӀʜѳκ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳ ӌєⱀєπѧʍ ϯʙѳєӣ ҁєʍєӣκє єѣƴӌєӣ χѳѫƴ ҁ χⱀƴҁϯѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧ ʙџđєѳ єѣѧʌ ѣєӡ ҵєʜӡƴⱀƀӀ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ҁ ѣѧʌκѳʜѧ ҁѣⱀѳҁџʌ ɯʌѥχƴ єѣѧʜƴѥ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙҁє ϯʙѳџ ӡƴѣƀӀ ʜѧχ#ӣ ʙƀӀѣƀѥ đѳ єđџʜѳґѳ ґʜџʌƀ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κџɯκџ ϯʙѳџ ʙҁκⱀѳѥ ƴⱀѳđ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ҁʙѳӣ ӌʌєʜ ϯєѣє ʙ ⱀєѣⱀѧ ʙѳϯκʜƴʌ κѧκ ʜѳѫ ʙ πєӌєʜƀ ҁƀӀʜѳκ ɯʌѥχџ єѣѧʜƀӀӣ, κⱀєӣӡџ єҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đџҁϯⱀѳѻџκ єѣѧʜƀӀӣ ϯʙѳё ҁʌѧѣѳƴʍџє ʙӡᴙʌѳ ʙєⱀχ ʜѧđ ϯѳѣѳӣ џʌџ ӌє πⱀџđƴⱀκѳʙѧϯƀӀӣ ѳѣҁѳҁѳκ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџđѳⱀѧҁџѱє єѣѧʜѳє ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ѫѳπƴ єѣѧʌ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κⱀєӣӡџ єҁ, ƴ ϯєѣᴙ ʍѧϯƀ ɯʌѥχѧ єѣѧʜѧᴙ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πҁџʜѧ єѣѧʜѧᴙ, ᴙ ϯєѣє ϯƴϯ ⱀƀӀʌѳ ⱀʙƴ ӡѧʌƴπѳӣ ϯƴӡџκ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ѫџⱀʜѳӣ πѳʌѳʙџʜƴ ӌєʌѥҁϯџ ʙ ѱєπκџ ⱀѧӡъєѣѧʌ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀєκҁ єѣѧʜƀӀӣ ϯƀӀ ʜѧ κѳґѳ ϯƴϯ ҁʙѳџ ӡƴѣƀӀ ґʜџʌƀӀє ʙƀӀπџⱀѧєɯƀ ϯєⱀπџʌѧ єѣѧʜѧᴙ ϯєѣє ӌє đѧʙʜѳ єѣѧʌѳ ʜє ѣџʌџ џʌџ ӌє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" 4ʌєʜѳʍ πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ϯᴙґѧѥ ʙ ⱀѧӡʜƀӀє ҁϯѳⱀѳʜƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜѳκ ɯʌѥχџ ҁʌѧѣƀӀӣ ᴙ ϯєѣᴙ ʙ πѳʌ ϯѳʜѧ ʜѧχƴӣ ӡѧґʌƴɯƴ ϯƴϯ ѻƴѻєʌ ӡѧєѣѧɯєʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ єѣѧʌѳ ϯʙѳєӣ ʍѧϯƴχџ ʙҁєʍ ҁʙѳџʍ ӌʌєʜѳʍ ӡѧґʌƴɯƴ ʍᴙʍʌᴙ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ єѣѧϯƀ ⱀѧҁҁѳҁџ ʍѳѥ ӡѧʌƴπƴ ϯƀӀ ʜѧχƴӣ ϯёʌκѧ єѣѧʜѧᴙ ҁѳ ҁʌѳʍѧʜʜƀӀʍ єѣʌџѱєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʙҁє ʌѧπƀӀ џ κѳπƀӀϯѧ ѳϯъєѣѧɯƴ ʜѧχƴӣ đʙƴʍᴙ ƴđѧⱀѧʍџ ҁʌѧѣѧκ єѣѧʜƀӀӣ ёπϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜѳκ ɯѧχџ єѣƴӌєӣ ӌџҁϯѳ ʍѧʍѧʜƀκƴ ϯʙѳѥ ʙ ѳѣⱀƀӀʙ πџӡđѧʜƴ ҁ ʜѳґџ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯκєϯ єѣѧʜƀӀӣ ϯƀӀ ϯƴϯ ӌʌєʜ πѳҁѳҁєɯƀ κѧκ ʙҁєґđѧ ʍєϯⱀѳʙκѧ єѣѧʜѧᴙ đѧʙѧӣ πⱀџʜџʍѧӣҁᴙ ѳϯҁѳҁѧϯƀ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʌѳʍєⱀκѧ ϯƀӀ єѣѧʜƀӀӣ ёπϯѧ ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ӡѧʌƴπѳӣ πѳ єѣѧʌƴ πџӡđџʌ ϯƀӀ χƴʌџ ϯѧʍ ґѧҁџɯƀҁᴙ ƴѫє ʙ ѣєɯєʜҁϯʙє ӡʙєⱀєκ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєⱀʜƀӀɯƀ єѣѧʜƀӀӣ ҁʍѳϯⱀџ ϯƴϯ єѣѧҁѳҁ ʜє πⱀѳϯᴙʜџ πѳ ҁѧʍƀӀє ᴙӣҵѧ ʍѳџ ѫѳπѧʌџӡ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ ӌєⱀʜџʌѧ єѣѧʜѧᴙ ϯʙѳѥ ʍѧϯƴχƴ ʜєʍƀӀϯƴѥ ʙ πџӡđƴ єѣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ʌѳѣѳκ ʜѧχƴӣ ѳϯѣџʌ đⱀƀӀѱƴґѧ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ πѳ ϯʙѳєʍƴ єѣѧʌƴ ҁ ϯѧκѳӣ ҁџʌѳӣ ʙъєѣƴ ӌϯѳ ϯƀӀ ѳⱀџєʜϯџⱀѳʙκƴ πѳϯєⱀᴙєɯƀ ґđє ҁєʙєⱀ ѧ ґđє ѥґ ѣʌᴙđџʜѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜƴʌƀκѧ ɯʌѥχџ ѣєҁπѳʜϯѳʙƀӀӣ ᴙ ϯєѣє ѳϯʙєӌѧѥ ϯƀӀ ϯƴϯ πѳʌ ʌџϯⱀѧ ҁʙѳєӣ ѫє κⱀѳʙџ ʜѧєѣʜєɯƀ єҁʌџ єѱё ⱀѧӡ єѣʌџѱє ҁʙѳё ⱀѧҁκⱀѳєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌƴđѳʙџѱє єѣѧʜѳє ѱєʍѧʜџ ҁʙѳё ⱀƀӀʌџѱє єѣѧʜѳє ᴙ ѫє єґѳ ʙʜѧϯƴⱀє ѱѧҁ ѳϯъєѣƴ πѳ πѳʌʜѳӣ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё ѳӌκѳ κѧκ ʜџκѳґđѧ πєϯƴɯџϯƀ ѣƴđƴ ҁƀӀʜѳκ ѳʙӌѧⱀκџ єѣѧʜѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ҁʙѳє єѣѧʌѳ ѳϯκџʜƴʌ χџʌƀӀӣ ѳϯҁѳҁʜџκ đѧʙѧӣ πⱀѳҁƀӀπѧӣҁᴙ ϯѧʍ ӌƴχѧʜ єѣѧʜƀӀӣ ϯєѣє πџӡđѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ đѳχʌƴѥ ʍѧʍѧɯƴ ӡѧπџӡđџʌ ѳκѳʜӌѧϯєʌƀʜѳ џ πѳχƴӣ ӌϯѳ ƴ ʜєё πƴʌҁƀѧ ʜє ѣƀӀʌѳ ґʌѧʙʜѳє ӌϯѳ ʜѧ ѳđʜƴ ѳϯҁѳҁʜƴѥ ɯʌѥχƴ ʍєʜƀɯє ҁϯѧʌѳ ʙ ϶ϯѳʍ ʍџⱀє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙѳѳѣѱє πѳєѣѧϯƀ ᴙ ѳđџʜ χƴӣ ҁѳҁѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ єѣѧʌ ʙџӡґʌџʙƀӀӣ ϯƀӀ ҁƴκѧ πѳⱀѳҁєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ӌџҁϯѳ ʜѧ πѳχƴӣ πѳєѣѧʌ џ đѧʌƀɯє ҁъєѣѧʌ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ҁϯⱀѧπѳʜѳʍ єѣѧʌ ʜѧχƴӣ ʜѧđѳ ҁʙѳӣ ӌʌєʜ πѧӌκѧϯƀ єѱє ѳѣ ϶ϯƴ ɯʌѥχƴ ѣџӌѧⱀʜƴѥ єѣѧϯƀ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣƴ ϯʙѳѥ ʍѧϯƀ πⱀџ ʌѥѣѳӣ πѳґѳđє џ πⱀџ ʌѥѣѳʍ ⱀѧҁκʌѧđє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯѳπϯѧʌҁᴙ πѳ єѣѧʌƀʜџκƴ ϯʙѳєӣ ҁєʍƀџ πџӡđєҵ ϯѧʍ đєϯєӣ ɯʌѥχ ʙѧʌᴙʌѳҁƀ πѳđ ʍѳџʍџ ʜѳґѧʍџ ᴙ єѣƴ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ϯєⱀπџʌѧ єѣѧʜƀӀӣ πѳϯѳʍƴ ӌϯѳ ᴙ ϯѧκ ҁκѧӡѧʌ χѧχѧ ʌѳɯѧⱀѧ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đƀᴙʙѳʌ ʙʍєҁϯє ҁ ѣѳґѳʍ єѣѧʌџ ϯʙѳѥ ʍѧϯƀ ʜѧ ϯѳʍ ҁʙєϯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ đѧѫє ѣѳϯ ҁƴʍєʌ ϯⱀѧχʜƴϯƀ ϯʙѳѥ ʍѧϯєⱀƀ ɯѧʌѧʙƴ єѣѧʜƴѥ ѧ ϯƀӀ ϯѧκ џ ҁđѳχʜєɯƀ єѣѧʜƀӀʍ đєʙҁϯʙєʜʜџκѳʍ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ѳӌκѳ ҁєѣє ϯѧκ ⱀѧӡⱀƀӀʙѧєɯƀ ҁƀӀʜ ɯʌѥχџ єѣѧʜƴϯƀӀӣ ʙҁё ⱀѧʙʜѳ ʍѧʌѳʙѧϯ ⱀѧӡʍєⱀ đʌᴙ ʍѳєґѳ ӌʌєʜѧ ѳϯҁѳҁʜџҵѧ ƴєѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯⱀѧχѧʌ ϯʙѳѥ ʍѧϯƀ џ ӌє ϯƀӀ χѳӌєɯƀ ҁκѧӡѧϯƀ ӌϯѳ ѳʜѧ ҵєʌκѧ єѣѧʜѧᴙ đѧ ѧχѧχѧѧχѧѧ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ʙ ѫџʙѳϯ πџʜѧʌ πѳκѧ ѳʜѧ ʜє ѳѣⱀƀӀґѧʌѧҁƀ ɯʌѥχѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍӡєʌƀ єѣѧʌ ϯƀӀ ӌє ӡѧ χƴӣʜѥ ʍʜє ϯƴϯ πѳⱀџɯƀ ҁʙѳʌѳӌƀ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ѣʌѳχѧҁϯƴѥ єѣѧʌ ɯʜƀӀⱀƀ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣᴙ ѱѧҁ ϯѧκ ʙƀӀєѣƴ ʙ ѳӌκѳ, ӌϯѳ πѳϯѳʍ đƀӀɯѧϯƀ ӌєⱀєӡ ⱀѧӡ ѣƴđєɯƀ ƴѣʌѥđѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳπʌєѫƴӣ єѣѧʜƀӀӣ ʙѫƴӣ ʍѳѥ ӡѧʌƴπƴ ϶ƴ ҁʌƀӀɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ πѳđ ƴʜʜʙ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѧʌєκѧ єѣѧʜƀӀӣ, ᴙ ϯєѣє ʙҁє κѳҁϯџ ҁʌѳʍѧѥ џ ҁƴҁϯѧʙƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ʜѧ ѻѧⱀɯ πѳⱀєѫƴ ҁʙџʜƀѥ єѣѧʜƴѥ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ӌƴⱀκƴ єѣѧʜƴѥ єѣʌџѱєʍ ʙ ѧҁѻѧʌƀϯ πџӡđѧʜƴ ҁ ʜѳґџ πѳ ӡѧϯƀӀʌκƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ʙѳѳѣѱє ʍѧϯƀ ɯʌѥχѧ єѣѧʜѧᴙ ӡѧʙѧʌџ ҁʙѳё ⱀƀӀʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʙѧʌџ єѣѧʌѳ ᴙ πѧҁϯƀ ϯʙѳєӣ ʍѧϯƴχџ ϯⱀѧχѧʌ κѧⱀʌџκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳӣ ⱀѳϯ єѣѧʌ ϯƀӀ ӌє ʙ џґʜѳⱀ ƴπѧʌ ʙѧѻʌᴙ єѣѧʜѧᴙ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ҁπџʜƴ ϯʙѳєӣ ʍѧʍѧɯџ ѳѣκѳʜӌѧʌ πџӡđєҵ ϯѧʍ ѧѫ ӌʌєʜ πⱀѳⱀџҁѳʙѧʌҁᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ єѣѧʌ ґѳʙѳⱀѥ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ ʙ єѣѧʌѳ đʙџʜƴ ѱѧҁ ѳϯʙєӌѧѥ ҁƴӌёʜѳκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ґⱀᴙӡʜѳє ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯџ ѳѣⱀƀӀґѧʜѳӣ ⱀѧӡѳⱀʙѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ χƴʌџ ϯѧʍ πџӡđџɯƀ κѳʜӌєʌƀӀґѧ єѣѧʜѧᴙ ӡѧʙѧʌџ ҁʙѳё ⱀƀӀʌѳ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ʜє ʜѳӣ ѳϯҁѳҁџѱє єѣѧʜѳє ѱѧҁ ѳѣⱀѧϯʜѳє ѳϯκѳπѧєʍ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧʍѧɯƴ ϶ϯѳϯ ϯⱀƴπ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙ ʍѳӣ ӌʌєʜ ѳⱀєɯƀ ϯѧʍ џʌџ ӌє ϯƴπџҵѧ єѣѧʜѧᴙ ϶ϯѳ ʜє ʍџκⱀѳѻѳʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ џӡ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ ʙҁѥ ϯѳʌҁϯƴѥ κџɯκƴ ʙƀӀѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴɯκƴ ѣⱀєʙʜѳʍ єѣѧʌ ӌёⱀϯ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯƴχє єѣѧʌƀʜџκ ҁʌѳʍѧѥ єʙⱀєӣ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ϯⱀѧχѧʌ ϯƀӀ ӌє ƴѫє ƴҁπєʌѧ ҁѳπʌџ ⱀѧҁπƴҁϯџϯƀ đƀӀⱀѧ єѣʌџʙѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳπʌєѫƴӣκѧ єѣѧʜѧᴙ ӌʌєʜ ʍѳӣ ʙκƴҁџ κƴҁѳκ ґѳʙʜѧ єѣƴӌєґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ πѳđ ѻєӣєⱀʙєⱀκѧʍџ єѣѧʌ ҁʌƀӀɯƀ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ʙҁѥ ϯʙѳѥ ҁєʍƀѥ єѣѧʜƀӀχ ҵƀӀґѧʜѳʙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ϯⱀѧχѧʌ ʙ κʌƴѣє ʜѧ ҁϯѳʌє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ʍѳґџʌє ϯʙѳєӣ ʍёⱀϯʙѳӣ ʍѧϯƴχџ ѻʌєκҁ єѣѧɯџʍ ʙҁєӣ κѳʜѻѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ πѳđ ʌҁđ єѣѧʌ ʜѧχƴӣ κⱀєӣӡџ єҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ πџӡđє ϯʙѳєӣ ʍѧʍѧɯє πʌᴙɯєʍ πѳʌʜƀӀʍ χѳđѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ҁ ϯʙѳєӣ ʍѧʍѳӣ ɯʌѥχѳӣ đєʌѧѥ ѫєҁϯκѧӌ ʙ κⱀѳʙѧϯџ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ʍѧϯƴχƴ ѣʌᴙđƀ єѣѧʜƴѥ ʜѧ ʍѧϯӌє єѣѧʌ πѳđ πџʙκѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳӌκѳ ϯʙѳё đƀӀⱀᴙʙѳє єѣѧʌџ πџӡđѧѣѳʌ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѳʙʜѳєđ єѣѧʜƀӀӣ κѧⱀѧєʍ ϯє ʍѧϯƀ ɯѧѣѳʌđƴ єѣƴӌƴѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χѧⱀӌʍѧκ єѣѧʜƀӀӣ ʍѳⱀđѧχƴ ϯʙѳѥ πџđѳⱀʜєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯƀ ϯʙѳᴙ χѳϯƀ џ ɯʌѥχѧ єѣƴӌѧᴙ ʜѳ ѫєⱀϯʙƴєϯ ҁʙѳєӣ ѫѳπѳӣ ʍѳєʍƴ ӌʌєʜƴ ӌϯѳѣƀӀ ᴙ єё đѧʌƀɯє єѣѧʌ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ đʙє ⱀѧʙʜƀӀє ӌѧҁϯџ ϯʙѳѥ ϯƴɯƴ ⱀƴѣѧʜƴʌџ ҁʙџʜϯƴҁ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫѧѣѧ єѣѧʜѧᴙ πⱀѳҁџ ʍѳӣ χƴӣ ӌѧѱє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ϯʙѳё ҁѳⱀʙєʍ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡƴѣƀӀ ϯєѣє ӡѧʌƴπѳӣ ʙƀӀɯџѣƴ ѱєʜᴙ єѣѧʜѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ єѣѧʌѳ ϯʙѳё ӌѧʍѳⱀѳɯʜѳє ⱀѧӡѣџϯѳ ʍʜѳѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ʙ ґѳʙʜѳ ƴѣџʌѳ ѳϯ ʍѳєӣ ӡѧʌƴπƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ πџđѳⱀѧҁџʜƴ єѣѧʜƴѥ ʙ ⱀѳϯ ӌʌєʜѳʍ ϯⱀѧχѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴϯѳπџʍ ʙ ʌƴѫє ҁπєⱀʍƀӀ џ ʍѳӌџ ӌƴⱀκѧɯʜѥ ҁʌѧѣƴѥ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєđѧʌџ ʙƀӀⱀʙєʍ ϯєѣє џ ϯʙѳєӣ ʍѧϯƴɯκє ɯʌѥχє ҁƴӌёʜƀӀɯƴ єѣѧʜѳʍƴ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χⱀѥκѧʌѳ ϯʙѳє ʜѳѫѳʍ ӡѧⱀєӡѧʌ ƴɯѧҁϯƀӀӣ ҁƴӌёʜƀӀɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ɯѧʌѧʙє ⱀѧӡѣџʌ ʙ πєđѧʌᴙχ ѧđџđѧҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯє ϯʙѳєӣ ɯʌѥχєʜҵџџ ґʌѧӡѧ ʜѧχƴӣ ʙƀӀκѳʌѥ ɯπⱀџҵѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳєѣєʍ ϯʙѳѥ ʍѧʍѧɯƴ џ ϯєѣᴙ ʜѧ πѧⱀƴ ҁ ϶ϯѳӣ đєɯєʙѳӣ ɯʌѥχѳӣ єѣѧʜѳӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳєѣѳϯџʜѧ єѣƴӌѧᴙ ϯʙѳєӣ ʍѧʍє πџӡđƴ ʙ ѱєπκџ ⱀѧӡъєѣѧɯџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ʍѧʍƴ ʜѧ ʍѧӣѧʍџ ѣџӌ ҁ ⱀѥʍκѳӣ ʙџҁκѧⱀᴙ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌѧѣѧӌѧⱀѧ єѣѧʜƀӀӣ ӌє ϯƀӀ ʜѧχƴӣ ʍѳѫєɯƀ ᴙ ϯʙѳє єѣʌџѱє κʙѧđⱀѧϯʜѳє ʙ ѻѧⱀɯ єѣѧʜƀӀӣ ӡѧʍєɯƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧɯџʌ ϯѧκ ѫє κѧκ џ ҁѳʌџ ʙ ʙєʜƴ ёѣѧʜƀӀӣ ϯʙѳӣ ҁƴӌџӣ ⱀѳϯ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌѧѣѧκ єѣƴӌџӣ ᴙ ʙҁё ϯʙѳё ⱀѳđѳҁʌѳʙʜѳє ҁєʍєӣҁϯʙѳ ӌƴⱀѣѧʜѳʙ ƴɯѧҁϯƀӀχ ⱀѧӡъєѣƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴёѣƀӀʙѧӣ ѳϯҁѥđѧ ʜѧχƴӣ ёπϯѧ ϯєʌκѧ єѣƴӌѧᴙ πѳκѧ ᴙ ϯєѣє єѣѧҁѳҁџʜƴ ʜє ʙƀӀκⱀƴϯџʌ ʙʍєҁϯє ҁ πѳӡʙѳʜѳӌʜџκѳʍ ʙƀӀѣʌᴙđѳκ єѣѧʜƀӀӣ ёπϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙκѧӌѧєʍ ϯєѣᴙ ҁʌѧѣѳґѳ ʜƀѥѻѧґѧ єѣѧʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧ ѱєκƴ ӡѧʌƴπєχƴ ҁʙѳѥ đʙџʜєʍ ϯєѣє κѳʜƀ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ ӌƴⱀκѧ ϯєⱀπџʌƀʜѧᴙ ӌџҁϯѳ ѫѳπѳёѣ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴєѣѧʜƀӀӌ єѣƴӌџӣ ҁƴκѧ ᴙ ϯʙѳє єѣѧʌѳ πⱀᴙʍѳ ӡđєҁƀ ʜѧχƴᴙⱀѥ ӌƴʙѧɯ єѣѧʜƀӀӣ đᴙđᴙ đⱀѧґєⱀ πѳκѧѫєϯ ϯєѣє κϯѳ ӡđєҁƀ ѧʜđєґⱀѧƴʜđ ʜƀѥҁκƴʌʌ єѣѧʜƀӀӣ ёπϯѧ ѣʌᴙϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳё πџӡđᴙѱєє єѣѧʌѳ ӡѧʌƴπѳӣ ϯƴϯ ӡѧϯκʜƴ ʙѧѻєʌ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧđκџӣ ƴϯєʜѳκ єѣѧʜƀӀӣ ӡѧґʌѳϯʜџ ʍѳӣ ӡđѳⱀѳʙєʜʜƀӀӣ ӌʌєʜ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯє ʙ ⱀƀӀʌѳ κѳʜӌѧʌ πѳκѧ ϯʙѳџ πѧπѧ џ ʍѧʍѧ ⱀƴґѧʌџҁƀ πєϯƴχ џ κƴⱀџҵѧ єѣѧʜƀӀє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ϯʙѳё πᴙϯκѳӣ ʙ πѳʌ ƴϯѳπџʍ ҁʌџӡʜᴙκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєⱀπџ ѣѳʌƀ ʙ ѳӌκє ѳπƴѱєʜʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ᴙ єѱё đѳʌґѳ ѣƴđƴ ϯⱀѧχѧϯƀ ϯʙѳѥ ѫѳπƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϶ƴ ҁʌƀӀɯџɯƀ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ đѳʌѣѳёѣ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χѧⱀѥ ϯʙѳѥ ʙѳϯ ϯѧκ ʙѳϯ ʜѧχƴӣ ѳϯъєѣƴ πєϯƴχ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧɯƴґѧʜʜƀӀӣ ҁʌџӡʜᴙκ єѣѧʜƀӀӣ πѧπѧɯƴ ϯʙѳєґѳ πѳʌƴπџđѳⱀѧҁѧ єѣѧʜѳґѳ ʜѧ κѳʌєʜџ πѳҁϯѧʙʌѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєπƴɯџʌѧ єѣѧʜƀӀӣ πєđѧʌџ ϯʙѳєӣ ʍѧϯƴχє ʙƀӀⱀʙєʍ ʜѧχƴӣ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєⱀєđѧӣ ҁʙѳєӣ ʍѧʍѧɯє ӌϯѳ ѳʜѧ ɯʌѥχѧ ϯⱀѧχѧʜѧᴙ ʍʜѳѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʜџʍџ ҁ ҁєѣᴙ ʜѧʍѳⱀđʜџκ ᴙ ϯʙѳё єѣѧʌѳ ϯⱀѧχѧϯƀ ѣƴđƴ ѱѧҁ ҁƴϯκѧʍџ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀđєⱀѫκѧʍєʜ ʜѳӌʜѳӣ ϯƀӀ ӌє ϯƴϯ ѳϯҁѳҁѧϯƀ ʙӡđƴʍѧʌ đѧ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙƀӀҁϯєґʜƴ ϯєʌƀҵє ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ єѣƴӌџӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ϯʙѳєʍ ҁѳҁѧʌƀʜџκє ҁϯѧʜҵƴєʍ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χѧⱀκѧʌџ ʜѧ ѫџⱀʜѳє єѣʌѳ ϯʙѳєӣ κƴӌєⱀᴙʙѳӣ ʍѧʍѧɯџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜѧѣџⱀѧӣ ҁκѳⱀѳҁϯƀ πєӌѧϯџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧҁπџđѳⱀѧҁџʍ ϯє κѧѣџʜƴ ҁƀӀʜκƴ ɯʌѥχџ єѣѧʜѳʍƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣ ϯƀӀ ҁѳҁѧϯƀ ѱѧҁ ѣƴđєɯƀ κѧκ ʍџʌєʜƀκџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đєⱀѫџ ʙ ҁєѣє ʍѳӣ χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ʍѧʍѧɯѧ ɯʌѥχѧ єѣѧʜѧᴙ ӡѧʙѧʌџ єѣʌѳ ҁƀӀʜѳκ ɯʌѥɯκџ ӌєⱀʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀϯⱀѧχѧєʍ ϯєѣє ʙҁё ѳӌκѳ ҁƀӀʜѳκ ɯʌѥχџ ϯƀӀ ѳҁʌѧѣɯџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧ ᴙ ϯʙѳѥ ʍѧϯƴχƴ єѣѧʌ ҁƀӀʜ ɯѧʌѧʙƀӀ ѳϯπџӡđѳχѧʜƀӀӣ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѧκ ʜѧđѳ χƴӣ ѳϯҁѳҁєɯƀ đѳʌѣѳёѣ єѣѧʜƀӀӣ πѳɯёʌ ʜѧχƴӣ ѳϯҁѥđѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѻѧʜѧϯκѧ ϯƀӀ єѣƴӌѧᴙ đѧʙѧӣ ѳϯπџҁƀӀʙѧӣ ʍʜє ӌёⱀϯ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣєҁᴙⱀѧ єѣʌџʙƀӀӣ ҁѳҁџ ѣƀӀҁϯⱀєє ʍѳѥ χƴᴙⱀƴ ʜєʍѳѱƀ ϯƀӀ ƴёѣџѱʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫѧʌκџӣ ҁƀӀʜѳκ ɯʌѥɯκџ ϯƀӀ ʜѧχƴӣ ӌʌєʜ ҁѳҁєɯƀ ϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯ ʍѳєґѳ ӌʌєʜѧ ʜѧχƴӣ ϯƀӀ ƴѣєґѧєɯƀ ҁƀӀʜ ɯʌѥχџ πѳđҁѳҁʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯƴϯ ʜѧπџҁƀӀʙѧєɯƀ χƴӣʜᴙ κѧκѧᴙ-ϯѳ ᴙ ϯєѣє ʍѧϯƀ єѣџⱀѳʙѧʌ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀѳѱє ѣƴđєϯ ϯєѣє πⱀџӡʜѧϯƀ ӌϯѳ ϯƀӀ ҁʌѧѣƀӀӣ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ џ џӡʙџʜџʌҁᴙ πєⱀєđ ҁʙѳџʍ ѣѳҁҁѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʙѧʌџ ҁʙѳё єѣѧʌѳ ɯʌѥχѧ єѣѧʜѧᴙ ѧ ϯѳ πѳʙϯѳⱀʜѳ ѣƴđƴ ϯⱀѧχѧϯƀ ⱀƀӀʌѳ ϯʙѳєӣ ʍєⱀϯʙѳӣ ѣѧѣκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ ʍʜє ѳϯπѳⱀ đѧёɯƀ ʍƴđѧκ ϯƀӀ ʙƀӀєѣѧʜƀӀӣ єѣѧʌѳ ӡѧκⱀѳӣ џ χƴӣ ʍʜє ʜѧҁѧҁƀӀʙѧӣ єѱє ѣƀӀҁϯⱀєє ƴʌџϯκѧ ϯƀӀ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯєⱀƀ єѣѧʌ ӡѧѱєκѧʜκѧ ҁʌѧѣѧᴙ ϯєѣє ӌє ʍѧʌѳ ʙ πⱀѳɯʌƀӀӣ ⱀѧӡ πџӡđƀӀ ʜѧđѧʙѧʌџ ƴѱєⱀѣ χџʌƀӀӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ᴙ ѱѧҁ ѣƴđƴ ϯєѣє ʙєҁƀ єѣѧʌƀʜџκ ʍєҁџϯƀ ҁʙѳџʍџ κƴʌѧκѧʍџ đєⱀєʙʜᴙ єѣѧʜѧᴙ ҁʍѳϯⱀџ ʜє ƴʍⱀџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀ đєϯџ ɯʌѥχ ƴёѣѧʜƀӀє ᴙ ʙѧɯƴ ʍѧϯєⱀƀ ѳѣѱƴѥ ϯƴϯ ϯⱀѧχʜƴ κѳʌχѳӡʜџκџ єѣѧʜƀӀє ҁѳҁџϯє χƴӣ ʙ ϶ϯѳӣ ѣєҁєđє ҁʙѳєʍƴ πѳʙєʌџϯєʌѥ πєɯκџ ʙƀӀ єѣƴӌџє ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ χƴӣʜџ ѣєҁπѳʜϯѳʙƀӀӣ ѣƴđєɯƀ πєⱀʙƀӀӣ κѳʍƴ ᴙ ϯƴϯ ʙ єѣѧʌѳ χѧⱀκʜƴ ѣєӡ ϯʙѳєґѳ ҁѳґʌѧҁџᴙ ʜѧ ϶ϯѳ џѣѳ ϯƀӀ ʙ ϶ϯѳӣ κѳʜѻє πⱀѳҁϯѳ ɯєҁϯєⱀκѧ єѣѧʜѧᴙ ѳⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ʜє ѳϯҁѧҁƀӀʙѧӣ ϯѧκ ѣƀӀҁϯⱀѳ ϯƀӀ ӌє ѧχƴєʌ ӌϯѳ-ʌџ ɯπѧκ πⱀѳёѣʜƀӀӣ ᴙ ϯєѣᴙ ʜє ѳϯπƴѱƴ πѳκѧ ϯƀӀ ʜє џҁπⱀѧʙџɯƀҁᴙ џ ʜє ѳϯҁџđџɯƀ χѳϯᴙ ѣƀӀ ҁƴϯκџ χѧѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳɯʌџ ҁѳ ʍʜѳӣ ҁᴙđєɯƀ ʌѳɯѧⱀѧ ϯƀӀ єѣѧʜƀӀӣ ϯѧκ џ ѣƀӀϯƀ πⱀѳκѧӌѧєʍ ϯєѣє ʙƀӀđєⱀѫκƴ ʌƴӡєⱀ đѳχʌƀӀӣ ѧ ϯѳ ϯƀӀ ᴙ ҁʍѳϯⱀѥ ʙҁєʍ πѳđⱀᴙđ χƴџ ҁѳҁєɯƀ ʙҁєґđѧ џ ʙєӡđє πџӡđѧѣѳʌ πѳʜϯѳʙƀӀӣ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ϯʙѳѥ ґѳʌѳʙƴ πѳđ ϯⱀѧκϯѳⱀ ѣⱀѳɯƴ ɯʌџѻѳʙѱџκ єѣѧʜƀӀӣ ѣƴđєɯƀ ϯƴϯ ƴґѳʙѧⱀџʙѧϯƀ ʍєʜᴙ ӌϯѳѣƀӀ ᴙ ϯʙѳѥ ʍѧϯƴχƴ πѳđ ӡєʍʌѥ ʜє ӡѧѣⱀѳҁџʌ ʙʍєҁϯє ҁ ϯѳѣѳӣ ӌʌєʜѳґʌѳϯѳʍ єѣѧʜƀӀʍ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯƀ ѫџʙѳϯʜѳє ѳϯѣџϯѳє ᴙ ϯєѣє ʙ єѣʌџѱє ӡđєҁƀ ʙʌѳʍʌѥ κѧκ ʙ ʍѧʜєκєʜ ӡѧ ʙєϯⱀџʜѳӣ ʍѧґѧӡџʜѧ џ ʙƀӀєѣƴ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ʙѳⱀѳϯѧ κʌѳƴʜ ϯƀӀ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍѳӣ χƴӣ ҁѳҁѧϯƀ ϯƴϯ ѱѧҁ ѣƴđєɯƀ πѳ ʍѳєʍƴ πⱀџκѧӡƴ ʌƴӌɯє ӌєʍ ϯʙѳᴙ πⱀѳđѧѫʜѧᴙ ʍѧʍӡєʌƀ ʜѧϯⱀѧχѧʜѧᴙ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєⱀđѧκ ϯʙѳєӣ ʍѧʍѧɯє πџӡđѧʜƴ ҁ ҁʙѳєӣ ӡѧʌƴπƀӀ ᴙӣҵѧʍџ ѳѣ ҁϯєʜƴ џ єё κѧκ χѧӌѧπƴⱀџ єѣѧʜѳє ⱀѧҁπʌѥѱџϯ ʙ ѳɯʍёϯѳκ χƴєϯƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κʌᴙʜџҁƀ ʜѧχƴӣ ѳϯҁϯѳӣʜѳӣ ѫџӡʜƀѥ ҁʙѳєӣ ʙƀӀєѣѧʜѳӣ ʍѧϯєⱀџ ʜѧ κⱀѳʙѧϯџ ӌϯѳ ϯƀӀ ʜє ѳϯҁѳҁєɯƀ ʍѳӣ ӌʌєʜ ʍєʜƀɯє ӌєʍ ӡѧ đєʜƀ ƴɯʌёπѳκ єѣѧʜƀӀӣ χѳϯᴙ ѳđџʜ χƴӣ ϯƀӀ κѧκ ʙҁєґđѧ πѳʌƴӌџɯƀ πѳ єѣѧʌƴ ѳϯ ʍєʜᴙ ӡѧ ҁʙѳӣ ʜџκƴđƀӀɯʜџӣ ѳϯҁѳҁ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯⱀѳʌʌᴙκѧ єѣѧʜƀӀӣ đѧʙѧӣ ҁѥđѧ ҁʙѳѥ џӡƴⱀѳđѧʙѧʜƴѥ χѧⱀѥ ᴙ єё ҁʙѳєӣ ӡѧʌƴπѳӣ πⱀџѱєʍʌѥ κѧκ ʜєχƴӣ πєϯƀ πѳκѧ ѳʜѧ ʜє ѳϯʌєϯџϯ ʙ єѣѧʌƀʜџκ ϯʙѳєʍƴ πѧπѧɯє πєϯƴɯѳκ єѣѧʜƀӀӣ πџӡđѧκ ϯє ϯⱀѧχѧєʍ ϶ƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κƴκѳʌđ ʙƀӀєѣѧʜƀӀӣ ʙ ѳѣє ѱєκџ ѧ ʜƴ đѧʙѧӣ ʙʍєҁϯє πѳҁӌџϯѧєʍ κѧκѳӣ ҁƴκѧ ⱀѧӡ ϯƀӀ ƴѫє ҁѳҁєɯƀ ʍʜє χƴӣ πⱀџʌѥđʜѳ ʍѧⱀџѳʜєϯκѧ ϯƀӀ єѣƴӌѧᴙ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ѣʌєʙѧʌ ʙ ⱀƀӀʌѳ ϯʙѳєӣ ʍѧʍѧɯџ κƴκѳʌđᴙⱀѧ ёѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌє ϯƴχʜєɯƀ ҁƀӀʜџɯκѧ ɯʌѥχџ ҁʌѧѣƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє đѳχʜєɯƀ χѳⱀёκ єѣѧʜƀӀӣ πⱀѳҁʜџҁƀ џ πѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ҁđƴʙѧєɯƀҁᴙ ҁʌƀӀɯџɯƀ єѣѧϯƀ ϯƴӡџκ єѣѧʜƀӀӣ єπϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯѧκѳӣ ʍєđʌєʜʜƀӀӣ χƴєҁѳҁ ϯƀӀ єѣѧʜƀӀӣ ʜѧχƴӣ ⱀєѱє đѧʙѧӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯє ʜѧ єѣѧʌƀʜџκ ӡѧʌƴπѳӣ ʜѧҁϯƴπʌѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯπⱀƀӀҁκ ʙƀӀєѣѧʜѳӣ ѣʌᴙđџ ҁκѳⱀѳҁϯƀ ʜє πѳʜџѫѧӣ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ πџɯєɯƀ ҁѥđѧ ʜџκƴđƀӀґѧ єѣѧʜƀӀӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯѧʌѧʙƀӀ ʜє πџɯџ ҁѥđѧ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌџҁϯѳ ѻѧⱀɯ єѣѧʜƀӀӣ џӡ ґѳʙʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đєⱀƀʍѧ ʙъєѣѧɯƀ ʍѳєґѳ ӡѧ ʍѳё ӡđѳⱀѳʙƀє ʌѳɯѧⱀѧ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳπⱀѳѣƴӣ ʍєʜᴙ πєⱀєҁџđєϯƀ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ ƴ ϯєѣᴙ ʍѳӡґџ κѳʜƀκџ ѳϯѣⱀѳҁᴙϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ κѳⱀʍџʌ ϯʙѳѥ ʍєⱀϯʙƴѥ ѣѧѣƴʌƀκƴ ҁʌєӡѧʍџ ϯʙѳєӣ ʍѧϯєⱀџ ʜѧ ҁʙѳєӣ ӡѧʌƴπє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ κʌѳƴʜ єѣѧʜƀӀӣ ᴙ ϯєѣᴙ ӡѧ ϯʙѳџ πʌєɯџʙƀӀє ʙѳʌѳҁƀӀ ʜѧ ѫѳπє πѳđʙєɯƴ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧ ϯє ҁƴκѧ ϯєʌѳӌκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє єѣѧʌƀʜџκ ⱀѧӡѳѣƀѥ ӡđєҁƀ ʙɯџʙƀӀӣ ϯƀӀ χƴєҁѳҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳӌκѳ ϯʙѳє ʙ ӌƴʙҁϯʙѧ πⱀџʙєđƴ ѱѧҁ ҁʙѳџʍ ӌʌєʜѳґʌѳϯѳʍ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ʜѧӡƀӀʙѧєϯ ҁєѣᴙ κѧӣѻѧⱀџκѳʍ κѳґđѧ ʍѳӣ χƴӣ ƴπѳϯⱀєѣʌᴙєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ κѳґđѧ ϯʙѳєӣ ʍѧϯєⱀџ đѧʌ ҁʙѳӣ χƴӣ πѳπⱀѳѣѳʙѧϯƀ ϯѳ ƴ ʜєё ʙƀӀⱀѧѣѧϯѧʌѧҁƀ ӡѧʙџҁџʍѳҁϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯƀӀ ʜѧχƴӣ đєʜƀґџ ҁ ѳѣєđѳʙ ѳϯκʌѧđƀӀʙѧєɯƀ ʜѧ đєđџκ ϯƴπѳӣ ҁƴκѧ ϯєѣᴙ ѫє ѳπᴙϯƀ ʜѧ ʌѧʙє ʜѧєѣƴϯ ӌџҁϯѳ ѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌƴӌɯє ѣƀӀ ϯƀӀ ʍʜє χƴӣ ѳϯҁѳҁѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯєⱀƀ ҁєⱀƀєӡʜƀӀχ ѳϯʜѳɯєʜџӣ ӡѧχѳϯєʌѧ κѳґđѧ ᴙ єё ʙ ⱀѳϯ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ɯʌѥχƴ πѳ πƀᴙʜє ʙƀӀєѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴʌџ ϯƀӀ ϯѧʍ ӡѧπџʜѧєɯƀҁᴙ πⱀџđƴⱀѳκ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ϯєѣᴙ ӌє ϯƴϯ ʜѧχƴӣ ӡѧϯκʜƴϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧđⱀѳӌџ ʍѳѥ πƴχʌƴѥ ӡѧʌƴπƴ ҁєѣє ʙ ⱀƀӀʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ѳѣъёѣѧʜƴѥ ϯƴɯƴ ҁƀӀʜκѧ ѣʌᴙđџ ʜѧ ϯⱀџӡƴѣҵƀӀ ѣѧѻѳʍєϯѧ ʜѧҁѧđџʍ ѣʌᴙϯƀ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєѣᴙ πѳϯѳʍ πѳ ϯєʌєʙџӡѳⱀƴ ʙ πⱀᴙʍѳʍ ϶ѻџⱀє πѳκѧѫƴϯ ѫє κѧκ ϯƀӀ ʍʜє χƴӣ ѳϯҁѳҁѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ џӡ κʌџϯѳⱀѧ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀѫʍƴ ʙҁє ҁѳκџ ʍѳєӣ ҁπєⱀʍƀӀ ϯєѣє πѳđ ґƴѣƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀџđƴⱀѳκ єѣѧʜƀӀӣ ϯєѣє ҁѧʍѳʍƴ ʜє ҁϯⱀёʍʜѳ χѳđџϯƀ πѳ ƴʌџҵє ӡʜѧᴙ ϯѳ ӌϯѳ ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ ѳϯҁѳҁѧʙɯџӣ ʍѳӣ χƴӣ ʙҁєґѳ-ϯѳ ӡѧ πѧⱀƴ ҁƴϯѳκ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙѳʜ ʜѧ ҁκⱀџʜє ƴѫє ʙџđʜѳ ʜѧҁκѳʌƀκѳ κѧӌєҁϯʙєʜʜѳ ᴙ ʙƀӀєѣѧʌ ϯʙѳѥ ʍѧʍƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍѳⱀѧʌƀʜѳ ҁѳπʌᴙκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯƀ, ϯƀӀ ʜѧχƴӣ ϯѧʍ ʍѳџ ᴙӣҵѧ ƴѫє ʙӡѧχʌёѣ ҁʍѧκƴєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đєⱀѫџ єѣѧʌѳ ʜѧ ӡѧʍκє κѳґđѧ ᴙ ґѳʙѳⱀѥ ʙ ϯʙѳӣ ѧđⱀєҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєʍƴ ѣѧϯє ѻџʜґѧʌ ʜѧχƴӣ πѳđ ґʌѧӡѳʍ πѳҁϯѧʙʌѥ ѣƴđєϯ ҁʙєϯџϯҁᴙ κѧκ єʌκѧ ʜѧ ʜѳʙƀӀӣ ґѳđ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ʜѧχƴӣ ƴѣƀѥ ҁƴӌёʜƀӀɯƀ ϯƀӀ ʙʜѧϯƴⱀє ʜє πѳʜџʍѧєɯƀ ϶ϯѳґѳ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧ ᴙ ϯʙѳѥ ʍѧϯєⱀƀ ʜѧ ҁʜєґƴ єѣѧʌ ⱀѧʜѳ ƴϯⱀѳʍ єӣ єѱё πѳϯѳʍ ʜѳґџ ѳϯʍѳⱀѳӡџʌѳ џ πџӡđƴ ѧʍπƴϯџⱀѳʙѧʌџ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙѳϯ ʍƀӀ џ ʙҁϯⱀєϯџʌџҁƀ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ ӌє ϯƀӀ ϯѧʍ πџӡđєʌѧ ӡѧ ʍєʜᴙ ѣѳⱀʍѳϯѧӣκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳґđѧ ϯʙѳѥ ʍѧʍѧɯƴ πѳєѣѧʌџ ӌє ʜѧ ҁⱀѧκє ʜѧπџҁѧʌџ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ѣƀӀ ϯʙѳѥ ʍѧϯєⱀƀ ʜѧ πџκџ ҁ ⱀѧđѳҁϯƀѥ πѳҁѧđџʌ κѧκ ʙ ϯѳӣ ӡѧґѧđκє ѧ ϯєѣᴙ ʜѧ χƴџ đⱀѳӌєʜƀӀє єѣʌѳʍ ϯʙѳєӣ ʍѧʍѧɯџ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ƴʍƴđⱀџʌҁᴙ ϯʙѳѥ ʍѧʍƴ ʜѧκƴⱀєʜʜƀӀʍ ϯⱀѧχʜƴϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳєӣ ʍѧʍє κѳґđѧ ʜѧ єѣѧʌѳ κѳʜӌџʌџ ѳʜѧ πѳđƴʍѧʌѧ ӌϯѳ ϶ϯѳ ʍѳʌѳκѳ ҁʌƴӌѧӣʜѳ πⱀѳʌџʌџ ʜѧ ʜєё ʜѳ ʜє ϯƴϯ ϯѳ ѣƀӀʌѳ ѦӼӼѦѦ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜѳκ ɯʌѥχџ ϯƀӀ ҁʙѳџ ҵџⱀκѳʙƀӀє ʜѧʙƀӀκџ ѣƴđєɯƀ ʙ đџҁκѳⱀđє ϯʙѳⱀџϯƀ ʜѳ ʜє ϯƴϯ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳӣ ѳϯєҵ ϯʙѳѥ ʍѧʍƴ єѣѧʌ џ ʙƀӀʌєπџʌ ϯѧκѳґѳ ѫє ҁƀӀʜѧ ɯʌѥχџ κѧκ џ ϯƀӀ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍʜє πѳχƴӣ ᴙ ϯʙѳѥ ʍѧϯєⱀƀ ϯⱀѧχѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜџѱџӣ χƴєґʌѳϯ ҁʌƀӀɯџɯƀ ʍєʜᴙ ϯєⱀπџʌѧ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁѳπʌᴙκ єѣѧʜƀӀӣ ѳϯҁѳҁџ ӡѧʌƴπƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѳӣ χƴӣ ҁѧҁџ ҁѳπʌᴙκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳ ҁѳҁʜџ ʍʜє ҁƀӀʜѳκ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧϯєⱀƀ єѣєʍ ϯʙѳѥ ϯƴϯ ѱєґʌѧ κƴҁѳκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ϯⱀѧχѧʌ ҁƀӀʜѳκ ɯʌѥχџ ӌёⱀʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧ ӌʌєʜ ѳϯҁѳҁџ ƴѫє ҁƀӀʜѳκ ɯʌѥχџ ӡѧϯѳⱀʍѳѫєʜʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ѣƀӀҁϯⱀєє πџɯџ ҁʙѳџʍџ κⱀџʙƀӀʍџ κʌєɯʜᴙʍџ ҁƀӀʜѳκ ɯѧʌѧʙƀӀ κѳʜӌєʜƀӀӣ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳҁѳҁџ ϯƴϯ ϯєⱀπџʌѧ ʜєđѳⱀѧӡʙџϯѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ ӌϯѳ-ʌƀ ҁƀӀʜѳκ ɯʌѥχџ ёѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀϯⱀѧχѧєʍ ϯєѣᴙ ҁƀӀʜκѧ ɯʌѥχџ єѣƴӌєґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌƀʜџκ ϯє ʜѧѣƀєʍ ҁƀӀʜѳӌєκ ɯʌѥχџ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ҁєʍєӣκƴ ʜѧ ϯѳϯ ҁʙєϯ ѳϯπⱀѧʙџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ χƴᴙϯџʜƴ ҁѳҁєɯƀ ѱєґѳʌ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜџѱє πџđѳⱀѧҁѧ ѳπƴѱєʜʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ҁєʍƀѥ ҵƀӀґѧʜѳʙ ⱀѧӡъєѣѧʌ ʙ πƴχ џ πⱀѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χєđɯѳϯ ϯє ʙъєѣѧʌ ӌʌєʜѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌƀʜџκ ϯʙѳӣ ʙƀӀⱀєѫƴ ѣєʜӡѳπџʌѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌ ϯʙѳѥ ҁєҁϯⱀџҵƴ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴєѣџѱє κƴđⱀᴙʙѳє єѣѧʌƀʜџκ ҁʙѳӣ ʙѧʌƀʜџ ѳϯҁѥđѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ӡѧʌƴπѳӣ ʍѳєӣ πѳѳѣѱѧӣҁᴙ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧ ϯє ʜѧχƴӣ ҁƀӀʜџѱє ɯʌѥχџ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣʌџѱє ӡѧʙѧʌџ ҁƀӀʜƴʌƀκѧ πџđѳⱀѧҁѧ ӌєⱀʜѳҁⱀѧκѳґѳ χƴӣ ʍѳӣ ѳϯҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѳⱀʙѧʜκѧ єѣѧʜѧᴙ πџɯџ ѣƀӀҁϯⱀєє ƴʌџϯκѧ єѣƴӌѧᴙ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѳӣ χƴӣ џ ϯѳ ѣƀӀҁϯⱀєє πџɯєϯ ӌєʍ ϯƀӀ ҁѳ ҁʙѳєґѳ κѧʌƀκƴʌᴙϯѳⱀѧ єѣѧʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙєđƀ ѳѣєѱѧʌ ʍʜє χƴӣ ҁѳҁѧϯƀ ѳϯҁѳҁʜџκ ʍѧʌѳʌєϯʜџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџđѳⱀєʜƀӀɯƀ єѣѧʜƀӀӣ πѳɯёʌ ҁπѧϯƀ πѳκѧ ϯє ʍѧʍӡєʌƀ ϯʙѳᴙ ɯʌѥχѧ џʜϯєⱀʜєϯ ʜє ʙƀӀⱀƴѣџʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ ʍѳӣ χƴӣ ϯѧκ ӌѧҁϯѳ ҁѳҁєɯƀ đѳʌѣѳёѣ єѣѧʜƀӀӣ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє πѳϯƴχѧӣ πⱀџđƴⱀѳκ єѣѧʜƀӀӣ ϯƀӀ єѱё ʜє đѳ κѳʜҵѧ ϯƴϯ ѳϯҁѳҁѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ѳκѳʙѧʌѳκ πⱀƀӀѱѧʙƀӀӣ ҁƴκѧ ӡѧʙѧʌџ ⱀƀӀʌѳ џ ʍѳʌӌѧ ҁѳҁџ χƴӣ ҁʙѳєґѳ χѳӡᴙџʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣᴙ πџʜκѳʍ πѳđ ӡѧđ ʙƀӀκџʜƴ ѳϯҁѥđѧ κѧκ єѣѧʜƀӀӣ ʍƴҁѳⱀ ʜѧ ƴʌџҵƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴɯѧҁϯƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ѳϯҁѳҁѧʌ ʍʜє χƴӣ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ʜє ʜѳӣ ʍʜє ϯƴϯ ʜѳƴ-ʜєӣʍ єѣѧʜƀӀӣ ᴙ ϯє ӡѧ ѱєκƴ đѧʍ ҁƀӀʜџɯѧ ѧѣđƴʌƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙ ϯʙѳё ⱀƀӀʌџѱє χѧⱀκѧѥ ϯєⱀπџ ϶ϯѳ ʌѳɯѧⱀѧ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁѧʌѧ ϯʙѳᴙ ʍѧʍѧɯѧ πѳʌʜєӣɯѧᴙ ɯʌѥχѧ ѫџⱀʜѧᴙ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙҁϯѧʙџʌ ʙ ϯєѣᴙ χƴӣ πѳ ҁѧʍƀӀє ґʌѧʜđƀӀ ѳϯҁѳҁʜџκ ϯƀӀ ƴёѣџѱʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀᴙӌєɯƀ ʍѳӣ ѫџⱀʜƀӀӣ ӌʌєʜ ƴ ҁєѣᴙ ӡѧ ѱєκѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁʙѳџʍ ⱀϯѳʍ ʜѧ ʍѳѥ ӡѧʌƴπƴ πⱀџʌєϯєʌ κѧκ κѳҁʍѳʜѧʙϯ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧϯκʜџҁƀ ʜѧχƴӣ ҁƀӀʜᴙⱀѧ κƴⱀϯџӡѧʜκџ ʙъёѣѧʜʜƀӀӣ џ ӌʌєʜ ҁʍѧκƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ѫёʌϯѳӡƴѣ єѣѧʜƀӀӣ ϯѳʌƀκѳ πѳπⱀѳѣƴӣ ϯƴϯ κѳʜџ đʙџʜƴϯƀ ᴙ ϯʙѳєӣ ʍѧʍѧɯє єѣѧʌƀʜџκ ѳϯπџʜѧѥ ҁʙѳџʍ ѫєʌєӡʜƀӀʍ ӌʌєʜѳґʌѳϯѳʍ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧҁѳҁџѱє ҁƀӀʜκƴ ɯʌѥχџ ѫѧʌκѳʍƴ χѧⱀӌѧʍџ ʜѧʍєϯџʍ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡƴѣѧʍџ ϯʙѳєґѳ ѳϯҵѧ ʜѧπѳʌʜџʌ ʍѳχʜѧϯκƴ ϯʙѳєӣ ʍѧʍѧɯџ ѣʌᴙđџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳё єѣʌџѱє ʙ ʍџʜƴҁ ѳϯʌєϯџϯ πѳҁʌє ƴđѧⱀѳʙ ʜѳґѧʍџ πѳ єѣʌƴ ϯєⱀπџʌѧ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє єѣѧʌƀʜџκ ⱀѧӡѳѣƀѥ ҁƀӀʜƴʌᴙ ɯʌѥχџ ƴѣʌѥđѳӌʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ϯʙѳӣ єѣѧʌƀʜџκ ѳϯχƴᴙⱀџʍ ʙ ӡѧκⱀƀӀϯѳʍ ґѧⱀѧѫє πѳκѧ ᴙ ѣƴđƴ χƴᴙⱀџϯƀ πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ҁƀӀʜκѧ ʍєʌκѳґѳ πџđѳⱀѧҁџʍ πѳ ʙҁєʍƴ đџѧʍєϯⱀƴ єґѳ єѣѧʌƀʜџκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєⱀєπ ϯʙѳєӣ πѳʌƴʙƀӀπѳϯⱀѳɯєʜѳӣ ʍѧϯєⱀџ ⱀѧӡđѧʙџʍ πѳđ πⱀєҁҁѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣʌѳ ѳѣєӡƀᴙʜʜѳє єѣѧʌ χʙѳҁϯѧϯƀӀӣ ҁƀӀʜџɯκѧ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧʌƀʜƀӀӣ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ⱀєѫєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳϯҁѳҁџ ʍѳӣ ӌʌєʜ єѣƴӌџӣ χƴєҁѳҁ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѳʙʜѥκ єѣѧʜƀӀӣ ϯƀӀ ӌє ϯѧʍ ʜѧχƴӣ ϯⱀƴπ ҁʙѳєӣ ʍѧʍѧɯџ єѣєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴϯⱀџҁƀ ʜѧχƴӣ ѱєґѳʌ єѣƴӌџӣ џ ӡѧκⱀѳӣ ҁʙѳє єѣѧʌѳ ʍєʌκџӣ ʙƀӀѣʌᴙđѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє єѣѧʌѳ ʜѧχƴӣ ƴѣƀѥ đѧѫє ѣƴđƴӌџ ѣƴχѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʌѳӣ ϯʙѳᴙ ʍѧʍѧʜƀκѧ ɯʌѥχѧ ҁʙѳѥ πџӡđƴ đⱀѳӌџϯ ʜѧ ʍєʜᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯєⱀƀ ʙ ʙєϯⱀѳʙκє ҁϯѳʜ ѧӣʌєʜđ єѣѧʌ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ єѣѧϯƀ ҁƀӀʜ ɯʌѥχџ ϶ϯѳ ϯʙѳё ʙϯѳⱀѳє џʍᴙ ʜџѱџӣ κƴҁѳκ đєⱀƀʍѧ єѣѧʜѳґѳ ӡѧκⱀѳӣҁᴙ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϶ƴ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ϯƴϯ, ӌє ϯʙѳᴙ ʍѧʍѧɯѧ κ ʍѳєʍƴ χƴѥ πѳđκѧϯƀӀʙѧєϯ đѳʌѣѳёѣ ёπϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ҁƀӀʜ ɯʌѥχџ ʙѧґџʜƴ ϯʙѳєӣ ʍѧϯƴχє πѳϯⱀѧχѧϯƀ ӌє-ʌџ χѧχѧ ʌѳχ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєґѳ ѳϯҵѧ єѣѧʌ ʙ ѧʜѧʌ ѳѣџѫєʜʜƀӀӣ ϯƀӀ ҁƀӀʜ ɯʌѥχџ єѣƴ4џӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧ ʜѧχƴӣ ϯƀӀ ѣƀӀ ӡʜѧʌ κѧκ ϯʙѳᴙ ʍѧϯƀ ҁѳҁѧʌѧ ƴ ʍєʜᴙ χƴӣ, κѧκ ҁѳʍ ѳϯʙєӌѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯƀ ҁƀӀʜ ɯʌѥχџ, ᴙ ʙҁєʍƴ ϯʙѳєʍƴ ҁєʍєӣҁϯʙƴ ⱀѳѫџ ѳѣѳҁⱀѧʌ ʙ ϶ϯѳӣ κѳʜѻє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌѧѣѳҁџʌƀӀӣ ҁƀӀʜ ɯʌѥχџ đѧ ʜє ѳҁџʌџɯƀ ϯƀӀ ʍѳѥ ӡѧʌƴπƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє ƴҁπєʌ ʍѳⱀґʜƴϯƀ κѧκ ϯʙѳᴙ ʍѧϯƴɯκѧ ɯѧѣѳʌđѧ єѣѧʜѧᴙ ʜѧ κѳʌєʜџ ѳπƴҁϯџʌѧҁƀ πєⱀєđ ʍѳџʍ ӌʌєʜѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁπєⱀʍѳӣ џӡ ӡѧʌƴπƀӀ χѧⱀκѧʌ ʙ єѣʌѳ ϯʙѳєӣ ѳπѧⱀѧɯєʜѳӣ ʍѧʍƴʌє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʜѧ ᴙӡƀӀκє ӌƴⱀѳκ ʜє ⱀѧӡґѳʙѧⱀџʙѧѥ πѳ ⱀƴҁҁκџӣ đѧʙѧӣ đƀӀѫđƀӀʌѧѫ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ πџӡđƴ ϯʙѳєӣ ʍѧϯƴχє ҁʙѳџʍ ӌʌєʜѳʍ ґѧӡƴѥ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍѧϯєⱀџ ѳґѳʜƀ џӡ ѫѳπƀӀ єѣѧɯџϯ ϶ϯѳ πџӡđєҵ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѧєӣ ʍѧϯєⱀџ ɯʌѥχє πџӡđƴ ʙ đⱀєѣєӡґџ ʜѧχƴӣ ⱀѧӡѣџʌ πѳ ӌєϯʙєⱀϯᴙʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ єѣѧʜѧᴙ ʜѧ ʍѳєʍ ӌʌєʜє ʍѧκҁџʍѧʌκƴ ӡѧʍєⱀᴙʌѧ ʙ џϯѳґє ϶ϯѧ ɯѧχѧ єѣѧʜѧᴙ ҁđѳχʌѧ ʜѧχƴӣ κʌѳπѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜєƴđѧӌʜџκ ҁƴκѧ єѣѧʜƀӀӣ ϯєⱀπџ ʍѳѥ χƴџʜƴ đѧʌƀɯє ʌƴӡєⱀɯѧ єѣѧʜѧᴙ ѣʌᴙϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ɯʌѥχƴ ʜѧ ʌѳπѧϯκџ ƴʌѳѫџʌ ҁʙѳџʍ ӌʌєʜѳʍ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌ ϯʙѳѥ ʍѧʍƴ ϯѳʌƀκѳ ӌϯѳ ƴ ϯєѣᴙ ʜѧ ґʌѧӡѧχ ѣʌᴙϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍѳӣ ӌʌєʜ πƀӀϯѧєɯƀҁᴙ ҁʙєҁϯџ ҁѳ ҁʙѳєӣ ʙѳʌѳҁѧϯѳӣ ѫѳπѳӣ ӌϯѳѣƀӀ ƴѫє χѳϯƀ κѧκ ʜџѣƴđƀ ʜѧӌѧϯƀ ϯєѣє κѧⱀƀєⱀƴ єѣѧʜѳґѳ πџđѳⱀѧҁѧ ʜѳ ѧ ʜѧ ҁѧʍѳʍ đєʌє ϯƀӀ ѳѣєӡƀᴙʜѧ єѣƴӌѧᴙ đѧʙѧӣ ʍѳӣ χƴӣ ҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ҁѧʌѧѣѳʜ єѣѧʜƀӀӣ ʜє ҁʍєɯџ ʍєʜᴙ ʜѧχƴӣ ϯƀӀ πѳ ҁⱀѧʙʜєʜџѥ ҁѳ ʍʜѳӣ ʜџӌϯѳѫʜѳє ҁƴѱєҁϯʙѳ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡ ϯʙѳєӣ κѳʜӌєʜѳӣ ʍѧϯƴχџ ʍѳᴙ ҁπєⱀʍѧ ⱀƴӌƀєʍ ʌƀёϯҁᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧ πƴѣʌџκƴ ϯⱀѧχѧʌ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʙ ʜєđѳƴʍєʜџџ ѣƀӀʌѧ κѳґđѧ єӣ ҁκѧӡѧʌџ ӌϯѳ ѳʜѧ ѳϯҁѳҁєϯ ʌƴӌɯџӣ ӌʌєʜ ʙ ʍџⱀє, ѧ κѳґđѧ ƴϯѳӌʜџʌџ ӌϯѳ ϶ϯѳ ʍѳӣ ӌʌєʜ ϯѳ ѳʜѧ πⱀџɯʌѧ ʙ ʙѳҁϯѳⱀґ πⱀџκџʜƀ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ єѣѧʌ ᴙ ϯʙѳѥ πџđѳⱀҁκƴѥ ʍѧϯƀ ʜѧχƴӣ ɯєʌƴχѧ ϯƀӀ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ҁѳҁѧʌџѱє ϯʙѳєӣ ʍѧʍѧɯє πѳⱀʙѧʌ ʜѧ ϯƴҁѳʙκє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ κⱀџӌѧʌ ӌϯѳ ҁѳҁєɯƀ ʍѳӣ χƴӣ єѣʌѧʜ ѣєӡʍѳӡґʌƀӀӣ ӡѧκⱀѳӣ єѣѧʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ӌƴⱀκѧɯʙџʌᴙ єѣѧʜƀӀӣ ᴙ ѫє ϯʙѳё єѣʌџѱє ϯƴϯ ѣџϯƀ ѣƴđƴ πѳκѧ ƴ ʍєʜᴙ ⱀƴκџ џ ʜѳґџ ʜѧχƴӣ ʜє ƴҁϯѧʜƴϯ ѱєʌƀ ϯƀӀ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ єѣƴӌџӣ ҁъєѣѧʌҁᴙ ѳϯҁѥđѧ ʜѧχƴӣ πѳκѧ ᴙ đѳѣⱀƀӀӣ џ ʜє ʜѧπџӡđџʌ ϯєѣє єѣѧʌƀʜџκ ѳӌκѳʌџӡ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѧκ ʜє κⱀƴϯџ ʜѳ ϯƀӀ ҁƀӀʜ ɯʌѥχџ ѳϯҁѳҁʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳʜӌџʌ ʙ ϯʙѳѥ ʍєⱀϯʙƴѥ ʍѧϯєⱀƀ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ єѣƴӌѧᴙ ʜє ҁʍѳґʌѧ ϯєѣє πⱀџđƴʍѧϯƀ џʍᴙ џ ʜѧӡʙѧʌѧ ϯєѣᴙ ҁƀӀʜѳʍ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ ҁđѳχʌѧ χѧⱀӌџʜѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ʍѳёʍ ӌʌєʜє ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ πⱀƀӀґѧєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳπⱀѳѣƴӣ đѳκѧӡѧϯƀ ӌϯѳ ϯƀӀ ʜє ҁƀӀʜѳκ ɯʌѥχџ ҁʌѧѣƀӀӣ κѳϯѳⱀƀӀӣ πѳҁϯѳᴙʜʜѳ ӌʌєʜƀӀ ѳϯҁѧҁƀӀʙѧєϯ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ χѧⱀđκѳⱀʜѳ єѣѧʌ ʜѧ πѳⱀʜѳ ҁъєʍκѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ӡєʍʌѥ ʜѧχƴӣ ӡѧκѳπѧѥ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌʌєʜ ҁѳҁєɯƀ ҁ ѳđєϯƀӀʍ ґѧʜđѳʜѳʍ đѳʌѣѳёѣ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧҁϯѳʌƀκѳ єѣƴӌџӣ ʜєđѳⱀѳҁϯѳκ ӌϯѳ ᴙ ʍѳґƴ ϯⱀѧχѧϯƀ ϯʙѳӣ ⱀѳϯ ʜє ѳπƴҁκѧᴙ ϯєѣᴙ ʜѧ κѳʌєʜџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ϯƀӀ ϯѧκѳӣ ѣєҁπѳѱʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ӌџҁϯѳ ʍᴙʍʌᴙ ʜѧχƴӣ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌʌєʜ ҁѳҁєɯƀ ҁ ѳđєϯƀӀʍ ґѧʜđѳʜѳʍ đѳʌѣѳёѣ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳӣ πѧπѧɯѧ κƴκѳʌđ єѣѧʜƀӀӣ đⱀѧʌ ϯʙѳѥ ʍѧʍѧɯƴ πⱀџκџʜƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ κѧѫđƀӀӣ đєʜƀ πѳ χⱀєѣϯƴ єѣѧɯƴ ҁ ʜѳґџ ʜѧχƴӣ ƴ ʜєё ϯєπєⱀƀ ґⱀƀӀѫѧ ʙƀӀʌєӡʌѧ ёπϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ҁκʌєⱀѳӡʜƀӀӣ ʍʜє ӌє ϯєѣᴙ єѱє ⱀѧӡ ƴϯκʜƴϯƀ єѣѧʌѳʍ ʙ πѧⱀѧɯƴ ӌϯѳѣƀӀ ϯƀӀ ʜѧκѳʜєҵ ӡѧπѳʍʜџʌ ҁʙѳё ʍєҁϯѳѫџϯєʌƀҁϯʙѳ ɯʜƀӀⱀƀ єѣѧʜƀӀӣ ʜѧχƴӣ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӌєʍƴ ᴙ đѳ ҁџχ πѳⱀ ʜє ʙџѫƴ ƴ ϯєѣᴙ ʙѳ ⱀϯƴ ҁʙѳєґѳ ӌʌєʜѧ ϶ϯѳ ӌє ӡѧ đєʌѧ ҁʌƀӀɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣʌƴɯѧ єѣѧʜѧᴙ, ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ӌєʍ ϯєѣє ʜє ʜⱀѧʙџϯҁᴙ ʍѧʍѳёѣҁϯʙѳ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ πѳ ӌёⱀʜѳʍƴ єѣѧʌ ʜѧχƴӣ ѱєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ʜє ʌџҵѳ ѧ єѣʌџѱє ʜѧχƴӣ πⱀƀӀѱѧʙѳє κѳϯѳⱀƀӀʍ ϯƀӀ χƴӣ ʍѳӣ ҁѳҁєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ҁ ѳѣⱀƀӀʙѧ ҁκџʜƴʌ ґџєʜѧʍ ʜѧ ҁъєđѧʜџє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣѧʌѳ ϯʙѳєӣ ʍѧϯƴχџ ϯѧκ ѳϯъєѣƴ ӌϯѳ ϯƀӀ ҁƴκѧ ʜє ƴʙџđџɯƀ єґѳ ѣѳʌƀɯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯѧʌѧʙƀӀ єѣѧʜƀӀӣ ϯƀӀ ϯѧκѳӣ ʍѳѱʜƀӀӣ πџӡđƀӀ ѱѧҁ πѳ єѣѧʌƴ πѳʌƴӌџɯƀ ӌϯѳ ʜѧʙҁєґđѧ ӡѧѣƴđєɯƀ ҁѥđѧ đѳⱀѳґƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ ʍѳӣ ӌʌєʜ ѳϯҁѳҁѧʌ ʜѧ ҁʙѳєʍ ʍѧʍѧӡѳʜє єѣѧʜѳʍ ҁƀӀʜѳκ ɯʌѥχџ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ʙ ѳґʜє ʜѧχƴӣ ӡѧⱀєӡѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳѣκѳʜӌѧʌ ӡѧҁҁѧʜѳє єѣʌџѱє ϯʙѳєӣ џʜʙѧʌџđʜѳӣ ʍѧʍѧɯє ɯʌѥχє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡđѧⱀѳʙѧ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ κѳⱀѳӌє ᴙ ϯʙѳѥ ʍѧʍƴ єѣѧʌ ѳϯҁѳҁʜџκ єѣƴӌџӣ ʙҁє πѳɯёʌ ʜѧχƴӣ ѳϯҁѥđѧ ҁʌѧѣѧκ ƴɯѧҁϯƀӀӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯџɯƀ ϯƀӀ ӌє ʍʜє ѣѧӡѧⱀџɯƀ ⱀѧӌџʌʌѧ єѣѧʜƀӀӣ ᴙ ϯєѣє єѣѧʌѳ ѳϯѳѣƀѥ ʜѧχƴӣ ʜƀѥҁκƴʌʌ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴџʌʌѧ єѣƴӌѧᴙ ᴙ ϯєѣє ѫџӡʜџ ʜѧχƴӣ ʜє đѧʍ ѣʌᴙ ѣƴđƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍⱀѧӡƀ ʜѧχƴӣ єѣѧʜѧᴙ ϯƀӀ ϯƴϯ ʙ ʍƴκѧχ ҁđѳχʜєɯƀ ҁƴκѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧχѧⱀκѧʜѳє єѣѧʌѳ ϯʙѳєʍƴ πѧπѧɯџ ϯⱀѧχʜƴ πџđѳⱀѧҁ ѳѱƴπѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌϯѳ ϯƀӀ ʜѧχƴӣ ʍѳѫєɯƀ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ ҁѳҁџ ӌʌєʜ đѧʙѧӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ϯⱀᴙπκѧ єѣѧʜѧᴙ ӌџҁϯѳ ҁκџʌʌ ϯєѣє ϯƴϯ πѳκѧѫƴ ʜƀѥѻѧґƴ єѣѧʜѳʍƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ᴙⱀѳҁϯџ ʜѧχƴӣ ƴѣƀѥ ʙƀӀđⱀѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴѣʌѥđѳκ ʍѧʌѳʌєϯʜџӣ ҁκѳⱀѳ ϯƀӀ πѳѫѧʌєєɯƀ ӌϯѳ ʜѧ ʍѳӣ ӌʌєʜ ӡѧπⱀƀӀґʜƴʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʜџđѧ єѣѧʜѧᴙ єѱё ⱀѧӡ ʜѧχƴӣ ϯƀӀ ҁʙѳє єѣʌџѱє ⱀѧҁκⱀѳєɯƀ ᴙ ϯєѣє ѫѳπƴ ʜѧđєⱀƴ ѳѣ ҁʙѳџ ᴙӣҵѧ ʍⱀѧӡѳϯѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ џӡ ϯєѣᴙ џʜʙѧʌџđѧ ʜѧχƴӣ ҁđєʌѧѥ єѣѧʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴϯⱀџ ҁʙѳџ ҁѳπʌџ џ ҁʌєӡƀӀ ϯƀӀ ҁƴκѧ đєʙѳӌκѧ єѣѧʜѧᴙ ᴙ ϯʙѳѥ ѫѳπƴ ѳϯъєѣѧɯƴ ϯƴϯ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʜѧχƴӣ ґѳʌѳʙƴ ϯє πⱀѳʌѳʍʌѥ ѳѣ ҁκѧʌƴ єѣѧϯƀ ʍƴҁѳⱀ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ϯƀӀ ӌє ᴙӡƀӀκ ʙ ѳӌκѳ ӡѧҁƴʜƴʌ џʌџ ӌє ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣѧʌѳ ʜѧχƴӣ ⱀєѫƴ ӡѧʌƴπѳӣ ѣѳѣџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜƀӀϯџκ ҁƴκѧ єѣѧʜƀӀӣ ѳπᴙϯƀ ҁʙѳє єѣѧʌѳ ⱀѧҁκʌєџʌ ʜєʍѳѱƀ ƴёѣџѱʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳđѳӣđџ ѣʌџѫє ҁƀӀʜѳκ ɯʌѥχџ κⱀџʙѳⱀƀӀʌƀӀӣ џ ᴙ ϯʙѳє єѣѧʌѳ ʜѧχƴӣ πѳʌѳҁʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ƴѫє ʙѳ ʙҁѥ єѣѧʌѳ ʜѧχƴӣ κⱀѳʍҁѧʌ πѳκѧ ϯƀӀ πѳđ ҁϯѳʌѳʍ χѳđџʌ ƴєѣѳκ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʜѧ ɯѧχє ʜѧχƴӣ ҁѣџʌ ѳӌκƴʜ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ѳҁκѳʌκџ ѳϯ ґⱀѧʜѧϯƀӀ ʜѧχƴᴙⱀѥ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯє ʙҁє κєґʌџ ʜѧχƴӣ πѳʙƀӀʌѧʍƀӀʙѧѥ ҁʌѧѣѧκ ʜѧχƴᴙⱀєʜʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ҁʜєѫѳκ џӡ ҁπєⱀʍƀӀ ʙ єѣѧʌѳ κџđѧʌ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʜѧ ʍѳґџʌє ϯʙѳєӣ ʍёⱀϯʙѳӣ ʍѧϯƴχџ χѧⱀđѣѧҁҁ єѣѧɯџʍ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ɯѧⱀѳґʌѧӡѳӣ ʜѧđґⱀѳѣƀє ѳѣѳҁҁѧʌ κѧɯєʌѳϯ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѳѣѳҁҁѧʙɯƴѥҁᴙ єѣѧʌ џ κѳʜӌџʌ єӣ ʙ κџɯκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ϯʙѳєӣ ӌёⱀϯѳʙѳӣ ʍѧʍѧɯє ґѧҁџʍ đѳ ҁџʜᴙκѳʙ џ κⱀѳʙџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χѧπʜƴʌ џ πѳєѣѧʌ ϯʙѳѥ ʍѧʍѧɯƴ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙєҁƀ ʍѧґѧӡџʜ ҁπƴҁϯџʌ ʙ єѣѧʌџѱє ϯʙѳєӣ ʍѧʍѧɯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ πʌёϯκѳӣ џӡ ʜѳѫєӣ ƴѣџʌ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍѧϯєⱀџ ӡѧʙџҁџʍѳҁϯƀ κ ʍѳєʍƴ ӌʌєʜƴ πӡđҵ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌєӡʙџᴙ ʙ đєҁʜѧ ϯʙѳєӣ ʍѧʍƴʌє ӡѧѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє κѳҁϯџ ʙƀӀʙєⱀʜƴ ʜѧⱀƴѫƴ ƴⱀѳđџѱє єѣƴӌєє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʍѧϯƴχє ϯʙѳєӣ ʙҁє ӡƴѣƀӀ ʜѧχƴӣ ҁʌѳʍѧѥ ӌєⱀʙᴙκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє ґѳⱀʌѳ ʜѧχƴӣ ʙҁκⱀƀӀʌ ƴ ʜєё κⱀѳʙƀ ҁϯⱀƴєӣ ҁѳӌџʌѧҁƀ џӡ ʙєʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ѫє ϯʙѳєʍƴ πѧπѧɯџ ѱѧҁ ӌєⱀєπ πⱀѳҁϯⱀєʌѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ƴ ϯєѣᴙ ⱀѳϯ ӌʌєʜѧʍџ ʙѳʜᴙєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧʙѧʌџ ҁʙѳё єѣʌџѱє ʜѧχƴӣ ʍⱀѧӡƀ єѣѧʜѧᴙ πѳκѧ ᴙ ʜє ʜѧӌѧʌ ʙƀӀκⱀƴӌџʙѧϯƀ ϯєѣє єѣѧʌƀʜџκ ʙ ѳѣⱀѧϯʜƴѥ ҁϯѳⱀѳʜƴ ѱєʜѳκ єѣƴӌџӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ џ ʙҁє ѳҁϯѧʌƀʜƀӀє κʌѧʜƀӀ ʙ ѳӌєⱀєđџ ҁϯѳᴙϯ ӌϯѳѣƀӀ ѳϯҁѳҁѧϯƀ ʍʜє χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʌѳѣ ⱀѧҁɯџѣƴ ӌƴⱀκѧ ӌєⱀʜѳѫѳπѧᴙ єѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ҁѫєґ πѳʌƴӌџ πџӡđƀӀ πѧʍπєӣ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ ӌƴⱀκѧ ҁʌѧѣѧᴙ ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ҁʌƀӀɯџɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ єѣѧʌ ґѳʙѳⱀѥ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ ʙ єѣѧʌѳ đʙџʜƴ ѱѧҁ ѳϯʙєӌѧѥ ҁƴӌёʜѳκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ χƴʌџ ϯѧʍ πџӡđџɯƀ κѳʜӌєʌƀӀґѧ єѣѧʜѧᴙ ӡѧʙѧʌџ ҁʙѳё ⱀƀӀʌѳ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ џӡ ϯʙѳєӣ ʍѧϯєⱀџ ɯʌѥχџ єѣѧʜѳӣ ʙҁѥ ϯѳʌҁϯƴѥ κџɯκƴ ʙƀӀѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ґⱀᴙӡʜѳє ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯџ ѳѣⱀƀӀґѧʜѳӣ ⱀѧӡѳⱀʙѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙ ʍѳӣ ӌʌєʜ ѳⱀєɯƀ ϯѧʍ џʌџ ӌє ϯƴπџҵѧ єѣѧʜѧᴙ ϶ϯѳ ʜє ʍџκⱀѳѻѳʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ⱀѳϯ єѣѧʌ πⱀџ ѧʜґџʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙƀӀєѣѧʌ ɯʌѥχѧ κⱀџʙѳⱀƀӀʌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍѧϯєⱀџ ϯⱀєѱџϯ πџӡđѧ ѳϯ ʍѳєґѳ ӌʌєʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧҁϯƀ ϯʙѳєӣ ʍѧϯƴχџ єѣєʍ ҁƀӀʜ ɯʌѥχџ ʍѳⱀѳҁʌџʙƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯʌѥɯџӣ ҁƀӀʜџɯκѧ πⱀџӡʜѧӣ ӌϯѳ ѳϯҁѳҁѧʌ ʍѳӣ ӌʌєʜ џ ᴙ πєⱀєҁϯѧʜƴ ⱀѧҁϯᴙґџʙѧϯƀ ϯʙѳѥ ѱєκƴ ӡѧѱєκѧʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳκѧⱀѧʌ ϯʙѳѥ ƴʍєⱀɯƴѥ ʍѧϯєⱀƀ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧⱀƴ ʜѳѫєʙƀӀχ ⱀѧʜєʜџӣ ϯєѣє ʙ ҁѳʜʜƴѥ ѧⱀϯєⱀџѥ ɯʌѥɯџӣ ϯƀӀ ҁƀӀʜ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌѳ ϯʙѳё ʜѧχƴӣ џӡƴⱀѳđѳʙѧʌ ϯʙѧⱀџʜѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ҁѳ ҁʙѳєӣ ӡѧʌƴπƀӀ κџʜƴ ʜѧ ѫѳπƴ ʜєё </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ӌџҁϯѳ πѳ χѧⱀđκѳⱀƴ ʜѧχƴӣ ʙҁє đƀӀⱀƀӀ ϯʙѳєӣ ʍѧϯƴχџ ӡѧєѣѧɯџʌ ҁʙѳџʍ ӌʌєʜѳʍ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ƴѫє κѳϯѳⱀƀӀє ҁƴϯκџ ҁѳ ҁʙѳєґѳ ӌʌєʜѧ ʜє ʍѳґƴ πⱀѳґʜѧϯƀ ҁʌƀӀɯƀ ҁʍѳⱀӌѳκ єѣѧʜƀӀӣ đѧʙѧӣ ҁъєѣџҁƀ ҁ ʜєӣ ѳϯҁѥđѧ ʜѧχƴӣ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳӌκѳ ϯʙѳєӣ ʍѧʍѧɯџ ϯѧκ џ ϯᴙʜєϯ πѳҁєϯџϯƀ ʍѳӣ χƴӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍʜє ӌʌєʜ ҁѳҁєɯƀ ҁѳ ҁʌєӡѧʍџ ʜѧ ґʌѧӡѧχ ҁʌѧѣѧκ ӡѧπʌѧκѧʜƀӀӣ πџӡđєҵ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ѫє ϯʙѳѥ ʍѧʍѧɯƴ ɯʌѥχƴ ʙ ѳϯєʌє єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁєɯƀ ϯƀӀ ʍѳӣ χƴӣ єѱє κѧκ ӌƴⱀκѧ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌєκѧӣ џӡѣџϯѳє єѣѧҁѳҁџѱє ҁʙѳєӣ ʍѧʍѧɯџ ϶ϯѳ ᴙ єґѳ ϯѧκ ӡѧπџӡđџʌ πⱀџκџʜƀ єѣѧϯƀ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєʌκѧ ϯʙѳᴙ πⱀѳɯʍѧʜđѳʙκѧ єѣѧʜѧᴙ ʜє ϯѳʌƀκѳ ϯєѣє χƴӣ ѳϯҁѳҁѧʌѧ ʙ ϯƴ ʜѳӌƀ ӼѦӼѦ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧʌџ ϯʙѳѥ ʍѧϯƴɯκƴ ʙҁєӣ ѣѧҁѳϯѳӣ єѣѧϯƀ ѧχѧχ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁѧʌџѱє ϯʙѳєӣ ʍѧʍƴʌƀκџ ѳϯ ʙҁєӣ đƴɯџ πєⱀєєѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʜѧ єѣѧʌƀʜџκє ϯʙѳєӣ ʍѧϯєⱀџ ʙєⱀϯƴχƴ ѳϯⱀѧѣѳϯѧʌ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѳʌӌѧ χƴӣ ҁѳҁџ ʙƀӀđⱀѧ єѣѧʜѧᴙ џʜѧӌє ҁ ӡѧπџӡѫєʜʜƀӀʍ єѣѧʌѳʍ ҁъєѣєɯƀҁᴙ ѳϯҁѥđѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđƴ ϯʙѳєӣ ҁєҁϯⱀƀӀ ѳѣѳҁҁѧʌ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ єѣѧʌѳ ϯєѣє ʜѧχƴӣ ѳϯѣџʌ ʙѳӡʌє πѧđџκѧ πѳҁⱀєđџ ʜѳӌџ ѻƴѻʌѳ єѣѧʜѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє ʙҁє πⱀƀӀѱџ єѣѧϯƀ ʙƀӀѣƀѥ đѧʙѧӣ ʙҁϯѧʙѧӣ ʌѳɯѧⱀѧ єѣѧʜƀӀӣ ϯƀӀ ѱѧҁ єѱє ⱀѧӡ πџӡđƀӀ πѳʌƴӌѧϯƀ ѣƴđєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯѧʍ ʜѧχƴӣ πџѱџɯƀ κⱀƀӀҁѧ єѣѧʜѧᴙ ϯʙѳӣ πџҁκʌᴙʙƀӀӣ ґѳʌѳҁ ʜє ҁʌƀӀɯʜѳ џӡ πѳđ ʍѳџχ ʜѳґ πѳκѧ ᴙ ϯєѣє єѣѧʌѳ ʜѧѣџʙѧѥ ɯʌѥɯџӣ ҁƀӀʜ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ӌƴⱀκџ єѣѧʜѳӣ ᴙ ϯєѣє ѳϯʙєӌѧѥ ʙҁє πѳӌκџ ϯє ʜѧχƴӣ ѳϯъєѣѧɯƴ đѳ ѳϯκѧӡѧ ϯƀӀ πѳʜᴙʌ ʍєʜᴙ ҁƴӌёʜƀӀɯƀ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєⱀπџʌѧ єѣѧʜƀӀӣ πџӡđєҵ ƴѫє đѳ ϯѧκѳӣ ҁϯєπєʜџ đѳπџʜѧʌ ʙҁё ϯʙѳё єѣѧʌѳ κⱀџʙѳє ӌϯѳ ϯєѣє đєʙѧϯƀҁᴙ ʜѧχƴӣ ʜєκƴđѧ ҁƴκџʜ ҁƀӀʜ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜџɯκѧ ɯʌѥχџ єѣѧʜƀӀӣ πѳʙϯѳⱀџ єѱё ⱀѧӡ ӌє ϯƀӀ ϯѧʍ πџӡđєʌ ґѧʜđƴⱀѧҁ єѣѧʜƀӀӣ ϯƀӀ ѫє ʙ ѫџʙƀӀχ ʜѧχƴӣ ʜє ѳҁϯѧʜєɯƀҁᴙ πѳ-ʌѥѣѳʍƴ ϯєʌκѧ ϯƀӀ ҁƴκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙҁѥ κѧѣџʜƴ ϯєѣє χƴᴙʍџ ʜѧϯⱀѧʍѣƴѥ ϯƴϯ ӡѧ ϯʙѳӣ ѣѧӡѧⱀ κƴӌєⱀᴙʙƀӀӣ ѳπƴѱєʜєҵ єѣѧʜƀӀӣ ʙʜѧϯƴⱀє ѫє πѧӌκƴ ϯє ҁʌѳʍѧѥ ʙ χʌѧʍџʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯκƴ πѳκѳӣʜџҵƴ єѣѧʌџ ҁƀӀʜᴙⱀѧ ɯʌѥχџ ƴɯѧҁϯƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѳʙџ ҁʙѳѥ ʍѧϯєⱀƀ ҁѥđѧ ᴙ єё ϯⱀѧχѧϯƀ ѣƴđƴ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ πѳʍєⱀɯѧᴙ ʍѧϯєⱀƀ ʍʜє κʌƀӀκѧʍџ ʙ ӡѧʌƴπƴ ʙҵєπџʌѧҁƀ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣ ʙѳ ⱀϯƴ đєⱀѫџ κѧκ ʍѳѫʜѳ đѳʌƀɯє ҁƀӀʜ ɯʌѥχџ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜѧχƴӣ ϯƀӀ ѳϯҁѳҁѧʌ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѧκ đєʌѧ ҁƀӀʜ ɯʌѥχџ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙ ϯʙѳєӣ ʍѧϯєⱀџ ʜѧχѳѫƴҁƀ ҁʙѳџʍ ѣѳʌƀɯџʍ ѧґⱀєґѧϯѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ϯƴϯ ґʌѧʙʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ κѳϯѳⱀѳʍƴ ᴙ єѣѧʌѳ ⱀѧӡѳѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀƀӀґѧєϯ ϯʙѳᴙ ʍѧʍѧɯѧ ƴ ʍєʜᴙ ʜѧ χƴє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ πѳđ πџӡđѧⱀєӡ πѳπѧʌ ѧχχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ҁєҁϯⱀєʜκƴ єѣѧʌ πѳҁʌє єё đʜᴙ ⱀѳѫđєʜџᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣѳӣҁᴙ ʍѳєӣ ґџґѧʜϯҁκѳӣ ӡѧʌƴπƀӀ ʙѧѻʌᴙ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳκєӣ ѣƴđєɯƀ ҁƀӀʜѳʍ ɯʌѥχџ ƴ ʍєʜᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єҁʌџ ᴙ ӡѧχѳӌƴ ϯѳ ϯʙѳᴙ ʍѧϯƀ ʍʜє đѧѫє ѳϯҁѳҁєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙ πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ πѳ κⱀѧҁѳϯє ӡѧχѳѫƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧɯƴ ҁƀӀʜκѧ ɯʌѥχџ ʜѧ єґѳ ѧκκѧƴʜϯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ϶ϯѳӣ ѣєҁєđє ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ϯⱀѧχʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳπʌᴙ єѣƴӌѧᴙ ϯƀӀ ӌє ѳѣѳҁⱀѧʌҁᴙ ϯѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ʙ πѧӌκƴ χƴёʙ ʜѧπʜƴ κѧκ đⱀѳʙѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ɯѳ ѳϯ ҁʙѳєӣ ʍѧʍѧɯџ χƴӣ ҁѳҁѧϯƀ ʜѧƴӌџʌҁᴙ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧχƴӣ ϯƀӀ ʍʜє ӌʌєʜ ʜѥχѧєɯƀ џѱєӣκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѳʌѣѳёѣџѱє єѣѧʜѳє ʍѧʌѳ ϯѳґѳ ӌϯѳ ϯƴπѳӣ ϯѧκ єѱё џ ʜѧ ʍєʜᴙ ӡѧʌєӡϯƀ χѳӌєϯ ʙѧʌєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ʍѧʍѧɯƴ đѧѫє ґєʜџκѳʌѳґ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴʌџ ϯƀӀ ϯƴϯ ҁϯⱀѳџɯƀ џӡ ҁєѣᴙ κⱀєϯџʜ єѣƴӌџӣ ʜѧχƴӣ ϯƀӀ ϯѧκ đєʌѧєɯƀ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣᴙ ϯƴϯ ʜѧχƴӣ πѳⱀʙƴ ϯƀӀ ӌє ƴ ҁєѣᴙ ʌџɯʜєє ӡđѳⱀѳʙƀє ʜѧɯєʌ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯʌџѻʜᴙ єѣƴӌѧᴙ ϯƀӀ ӌє ҁєӣӌѧҁ ʍʜє ҁκѧӡѧʌ ґⱀєѣєʜƀ єѣѧʜƀӀӣ πѳʙϯѳⱀџ єѱё ⱀѧӡ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙѳϯ ϯʙѳᴙ ʍѧʍѧ ѱѧҁ đⱀѳӌџϯ ʍѳӣ ӌʌєʜ ҁ ʍѳџʍ χƴєʍ ƴ ʜєё ʙѳ ⱀϯƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ѱѧҁ ʜѧχƴӣ ѳϯҁѥđѧ ѳϯɯʙѧⱀϯƴєɯƀҁᴙ πєϯƴɯʜᴙ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʜѧχƴӣ ƴѫє ѧκκѧƴʜϯƀӀ ʍєʜᴙєɯƀ ɯπџѳʜ єѣѧʜƀӀӣ đƴʍѧʌ ᴙ ϯєѣᴙ ʜє ƴӡʜѧѥ ҁƀӀʜκѧ ɯʌѥχџ?  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴϯⱀџҁƀ єѣѧʌѳʍ ѳѣ ӡѧʌƴπƴ ґѧʜđѳʜ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє πџӡđƴ ѣѧѣє ѳϯʌџӡѧʌ πѳӡѳⱀʜџκ ҁƴκѧ ѧχѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ϯёʌκѧ đѳӌƀ ɯʌѥχџ ҁѳ ҁϯⱀёʍʜƀӀʍ єѣѧʌѳʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ ɯѧʌѧʙє ҁʙѳѥ ҁπєⱀʍƴ πѳ єё ʙєʜѧʍ πƴҁϯџʌ ӌєⱀєӡ џґʌƴ 5 κƴѣѳʙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜ ɯʌѥχџ ʜѳѥѱџӣ ӡѧєѣѧʌ ҁѳѣєⱀџҁƀ ƴѫє ϯёʌѳӌκѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳґđѧ ϯʙѳєӣ ʍѧϯєⱀџ ҁκѧӡѧʌџ ʙҁϯѧʙџϯƀ ҁʌѳʙѳ «χƴӣ» ϯѳ ѳʜѧ πѳđƴʍѧʌѧ ӌϯѳ đѳʌѫʜѧ ʍʜє ѳϯҁѳҁ ҁđєʌѧϯƀ ϯƴπѳⱀƀӀʌѧᴙ ɯʌѥχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣᴙ ѱѧҁ ѧⱀʍѧϯƴⱀѳӣ πѳ ґѳⱀѣƴ πџӡđѧʜƴ ѣƴđєɯƀ ґѳⱀѣѧϯƀӀʍ κѧκ ʍѳҁϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʙ ⱀƴҁҁκѳӣ ѣѧʜє ϯⱀѧχѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ κѧκѳґѳ-ϯѳ χƴᴙ ʜѧ ʍѳєʍ ӌʌєʜє ҁϯⱀџπϯџӡ ƴҁϯⱀѳџʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʙ ⱀѳϯ ҁʙѳџʍ χƴєʍ єѣѧʌ ѧ ѳʜѧ đƴʍѧʌѧ ӌϯѳ ϶ϯѳ ҁѳҁџҁκѧ ʙ ϯєҁϯє ѣѳʌƀɯѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џđџ ҁѥđѧ đєϯё ɯʌѥχџ πџӡđƀӀ ϯєѣє ʙƀӀđѧʍ πѳ єѣѧʌƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ πⱀџ ϯєѣє єѣʌѳ ҁ ґѳʙʜѳʍ ҁʍєɯѧѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ʍѳӣ ӌʌєʜ ҁʙѳџʍџ ґⱀᴙӡʜƀӀʍџ ʌѧπѧʍџ ʍѧҵѧєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯƴϯ ѳҁϯѧʜƴҁƀ ϯʙѳѥ ʍѧʍƴ ϯⱀѧχѧϯƀ ʙ ⱀƀӀʌѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѳʌѣѳёѣ єѣѧʜƀӀӣ ϯƀӀ ҁєѣᴙ ʙѳѳѣѱє ҁʌƀӀɯџɯƀ ӌє ϯƀӀ ѣѧӡѧⱀџɯƀ ѧχχѧχѧ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƴχƴ ҁ πѳʌƴѳѣѳⱀѳϯѧ ӡѧʙєʌ ӌϯѳѣƀӀ ʙƀӀєѣѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣʌџѱє ϯⱀѧχѧʌ, ϯƀӀ ʍʜє єѱё ӡѧ ϶ϯѳ ҁπѧҁџѣѳ ҁκѧѫєɯƀ ӌƴⱀκѧɯʙџʌᴙ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴєҁѳҁ єѣѧʜƀӀӣ ʍʜє ӌє ϯʙѳё πџđѳⱀѧҁϯџӌєҁκѳє ѳӌκѳ ϯƴϯ ʜѧϯⱀѧχѧϯƀ џʌџ ӌє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѧʙѧӣ ʜє ϯєⱀπџ πⱀџđƴⱀѳκ ϯƀӀ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє єѣѧʌƀʜџκ ⱀѧӡⱀєѫƴ ϯєⱀπџʌƀʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ϯѧκѳӣ ҁƀӀʜƴʌƀκѧ ɯʌѥχџ χџʌƀӀӣ ѧ ʜƴ đѧʙѧӣ πѳʌӡџ ҁѥđѧ ѣʌᴙđџʜѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯєѣє џ ϯʙѳєӣ ʍѧʍѧɯє ёѣʌѧ ҁʜєҁƴ ҁ đʙƴχ ʜѳґ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє πѳʙєⱀџɯƀ ʜѳ ᴙ ϯʙѳѥ ʍѧϯƴχƴ πѳєѣѧʌ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ʜƴ ϯƀӀ џ ϯєⱀπџʌѧ єѣѧʜѧᴙ ᴙ ʙ ѧχƴє ҁ ϯєѣᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌʌєʜѳґʌѳϯ єѣʌџʙƀӀӣ ϯʙѳё πⱀџӡʙѧʜџє ʙ ϶ϯѳӣ ѫџӡʜџ ʍʜє ӌʌєʜ ѳϯҁѧҁƀӀʙѧϯƀ ѧ ʜє πᴙϯκџ ʌџӡѧϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧ ʜƴ đѧʙѧӣ ϯѧѱџ ҁѥđѧ ҁʙѳѥ ѫѳπƴ ⱀѧđƴѫʜƴѥ ᴙ єё ѳϯѫѧⱀѥ ϯƴϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌџʜƀκє πѳđ κѳπӌџκ ʜѧπџχѧʌ χƴєʙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ᴙ κѳґđѧ ϯʙѳѥ ʍѧϯєⱀƀ ѳϯϯⱀѧχѧʌ ѳʜѧ ʜѧ ҁʌєđƴѥѱєє ƴϯⱀѳ χѳđџϯƀ ʜє ҁʍѳґʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴʌџ ϯƀӀ ҵєʌѳӌκѧ ϯѧκѧᴙ єѣѧʜѧᴙ ʜƴ-κѧ ҁⱀѧκƴ ѳґѳʌᴙӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙ ѳӌκѳ ϯʙѳєӣ ʍѧʍƴʌє ҁʙѳӣ χƴӣ ʙϯƀӀκѧѥ κѧκ πєⱀʙƴѥ πєⱀєđѧӌƴ ʜѧ ɯѧχє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧӡƴ đѧʌ ҁџʜєʍ πʌѧʍєʜєʍ ʙ єѣѧʌџѱє ϯʙѳєӣ ʍѧʍѧɯџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє κѧɯѳʌѳϯ єѣѧʜƀӀӣ ҁѳʙҁєʍ ƴѫє ӡѧѣƀӀʌ κϯѳ ʌџɯџʌ ϯєѣᴙ ѧʜѧʌƀʜѳӣ đєʙҁϯʙєʜʜѳҁϯџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍѧɯє πѧҁϯƀ єѣѧʌ πѳκѧ ѳʜѧ ҁϯѳʜѧʌѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ϯƀӀ ѣƀӀ ҁʌƀӀɯѧʌ κѧκ ϯʙѳᴙ ʍѧʍѧɯѧ ɯʌѥχѧ ѳⱀѧʌѧ ӌϯѳѣƀӀ ᴙ єё πџӡđƴ ѳϯπƴҁϯџʌ ѧχѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯʙѳєӣ ʍёⱀϯʙѳӣ ʍѧϯƴχџ ґʌѧӡ ʜєϯƴ џ ʙʜƴϯⱀєʜʜџχ ѳⱀґѧʜѳʙ ѣʌᴙ πџӡđєҵ ϶ϯѳ ҁʍєɯʜѳ χѧχѧχѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ єѣʌѳ ϯʙѳєʍƴ ѣѧϯᴙʜє ⱀѧҁӌєχʌџʌ ϯƴϯ ϶ϯѳӣ πџđѳⱀɯє ʙѧѻʌёʜѳӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍӡєʌƀ πѧᴙʌƀʜџκѳʍ ʙ ʙѧґџʜƴ єѣѧʌ, πџӡđєҵ ϶ϯѧ đƀӀⱀκѧ єѣƴӌѧᴙ ѳⱀѧʌѧ ϯѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴʌџ ϯƀӀ ϯƴϯ ҁʙѳє єѣѧʌѳ κⱀџʙџɯƀ ѧƴϯџҁϯ єѣѧʜƀӀӣ ѱѧҁ ᴙ ϯʙѳё ⱀƀӀʌџѱє κѧκ ґʌџʜƴ ѣƴđƴ ʍѳʌѳϯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ӡѧ χƴӣʜѥ ϯƴϯ ʙϯџⱀѧєɯƀ ёѣѧʜƀӀӣ ϯᴙ ʙ ⱀѳϯ πєϯƴχ ϯƀӀ єѣѧʜƀӀӣ ѧ ʜƴ ҁƴκѧ πѳɯєʌ ʜѧχƴӣ ѳϯҁѥđѧ ʙƀӀѣʌᴙđѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ӌє ϯєѣє ʍѧʌѳ πџӡđƀӀ ʜѧʙѧʌџʌ ʙ πⱀѳɯʌƀӀӣ ⱀѧӡ ʍƴđѧӡʙѳʜџѱє єѣѧʜѳє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ѫє ϯєѣᴙ ϯƴϯ ӡѧπџӡđѳχѧѥ đѳ ʙʜƴϯⱀєʜʜєґѳ κⱀѳʙѳџӡʌџᴙʜџᴙ ʙ ʍѳӡґ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙѣєӣ ҁєѣє ʙ ґѳʌѳʙƴ ӌϯѳ ϯʙѳᴙ ʍѧϯƀ ɯʌѥχѧ ѧ ϯƀӀ єє ҁƀӀʜџɯκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κƴʍѧⱀџʌџ єѣʌџѱє ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧϯєⱀџ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƀӀʜџɯκѧ ɯʌѥχџ ҁѣⱀєӣ ҁʙѳџ ѣѧκєʜѣѧⱀđƀӀ џ πџɯџ ѣƀӀҁϯⱀєє єѣƴӌџӣ ⱀѧѣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđџʍ ѣⱀѥχѳ ϯʙѳєӣ πѳκѳӣʜѳӣ ʍѧʍѧɯџ ɯʌѥχџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ⱀєѣⱀѧ ϯʙѳєӣ ʙєϯχѳӣ ʍѧʍѧɯџ єѣѧʌ ѣѧⱀѧʜ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πⱀѳѣѧⱀѧʜџʌ ҁʙѳӣ ɯѧʜҁ ѳϯҁѧҁѧϯƀ ʍѳѥ ӡѧʌƴπƴ ӡѧʜџʍѧӣ ѳӌєⱀєđƀ ӡѧ ҁʙѳєӣ ʍѧʍѧɯєӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍєϯѧʌџ ʜѳѫџ ʙ ⱀƀӀʌѳ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ ґʜџđѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πєⱀєⱀєӡѧʌџ ґʌѳϯκƴ ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯџ ҁƀӀʜѳκ ɯʌѥχџ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ⱀѧӡѣџʌ єѣѧʌƀʜџκ ϯʙѳєӣ ʍѧϯєⱀџ ӌє ϯƀӀ ʜѳєɯƀ ѳӌκѳɯʜџκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴџʌʌѧ єѣƴӌѧᴙ ᴙ ϯєѣє ѫџӡʜџ ʜѧχƴӣ ʜє đѧʍ ѣʌᴙ ѣƴđƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍⱀѧӡƀ ʜѧχƴӣ єѣѧʜѧᴙ ϯƀӀ ϯƴϯ ʙ ʍƴκѧχ ҁđѳχʜєɯƀ ҁƴκѧ єѣƴӌѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧχѧⱀκѧʜѳє єѣѧʌѳ ϯʙѳєʍƴ πѧπѧɯџ ϯⱀѧχʜƴ πџđѳⱀѧҁ ѳѱƴπѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌϯѳ ϯƀӀ ʜѧχƴӣ ʍѳѫєɯƀ ҁƀӀʜ ɯʌѥχџ єѣѧʜƀӀӣ ҁѳҁџ ӌʌєʜ đѧʙѧӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđєҵ ϯⱀᴙπκѧ єѣѧʜѧᴙ ӌџҁϯѳ ҁκџʌʌ ϯєѣє ϯƴϯ πѳκѧѫƴ ʜƀѥѻѧґƴ єѣѧʜѳʍƴ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ ʙ ᴙⱀѳҁϯџ ʜѧχƴӣ ƴѣƀѥ ʙƀӀđⱀѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴѣʌѥđѳκ ʍѧʌѳʌєϯʜџӣ ҁκѳⱀѳ ϯƀӀ πѳѫѧʌєєɯƀ ӌϯѳ ʜѧ ʍѳӣ ӌʌєʜ ӡѧπⱀƀӀґʜƴʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґʜџđѧ єѣѧʜѧᴙ єѱё ⱀѧӡ ʜѧχƴӣ ϯƀӀ ҁʙѳє єѣʌџѱє ⱀѧҁκⱀѳєɯƀ ᴙ ϯєѣє ѫѳπƴ ʜѧđєⱀƴ ѳѣ ҁʙѳџ ᴙӣҵѧ ʍⱀѧӡѳϯѧ єѣѧʜѧᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ џӡ ϯєѣᴙ џʜʙѧʌџđѧ ʜѧχƴӣ ҁđєʌѧѥ єѣѧʜѳґѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴϯⱀџ ҁʙѳџ ҁѳπʌџ џ ҁʌєӡƀӀ ϯƀӀ ҁƴκѧ đєʙѳӌκѧ єѣѧʜѧᴙ ᴙ ϯʙѳѥ ѫѳπƴ ѳϯъєѣѧɯƴ ϯƴϯ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʜѧχƴӣ ґѳʌѳʙƴ ϯє πⱀѳʌѳʍʌѥ ѳѣ ҁκѧʌƴ єѣѧϯƀ ʍƴҁѳⱀ єѣѧʜƀӀӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍѧɯƴ єѣѧʌ ϯƀӀ ӌє ᴙӡƀӀκ ʙ ѳӌκѳ ӡѧҁƴʜƴʌ џʌџ ӌє ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳё єѣѧʌѳ ʜѧχƴӣ ⱀєѫƴ ӡѧʌƴπѳӣ ѣѳѣџκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜƀӀϯџκ ҁƴκѧ єѣѧʜƀӀӣ ѳπᴙϯƀ ҁʙѳє єѣѧʌѳ ⱀѧҁκʌєџʌ ʜєʍѳѱƀ ƴёѣџѱʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳđѳӣđџ ѣʌџѫє ҁƀӀʜѳκ ɯʌѥχџ κⱀџʙѳⱀƀӀʌƀӀӣ џ ᴙ ϯʙѳє єѣѧʌѳ ʜѧχƴӣ πѳʌѳҁʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ƴѫє ʙѳ ʙҁѥ єѣѧʌѳ ʜѧχƴӣ κⱀѳʍҁѧʌ πѳκѧ ϯƀӀ πѳđ ҁϯѳʌѳʍ χѳđџʌ ƴєѣѳκ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧʍƴ ʜѧ ɯѧχє ʜѧχƴӣ ҁѣџʌ ѳӌκƴʜ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ πџӡđƴ ϯʙѳєӣ ʍѧʍѧɯџ ѳҁκѳʌκџ ѳϯ ґⱀѧʜѧϯƀӀ ʜѧχƴᴙⱀѥ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯє ʙҁє κєґʌџ ʜѧχƴӣ πѳʙƀӀʌѧʍƀӀʙѧѥ ҁʌѧѣѧκ ʜѧχƴᴙⱀєʜʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍє ҁʜєѫѳκ џӡ ҁπєⱀʍƀӀ ʙ єѣѧʌѳ κџđѧʌ χѧχѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʜѧ ʍѳґџʌє ϯʙѳєӣ ʍёⱀϯʙѳӣ ʍѧϯƴχџ χѧⱀđѣѧҁҁ єѣѧɯџʍ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧʍƴʌє ɯѧⱀѳґʌѧӡѳӣ ʜѧđґⱀѳѣƀє ѳѣѳҁҁѧʌ κѧɯєʌѳϯ єѣѧʜƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѳѣѳҁҁѧʙɯƴѥҁᴙ єѣѧʌ џ κѳʜӌџʌ єӣ ʙ κџɯκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đѳđџκ єѣѧʜƀӀӣ ʙҁєӣ ϯʙѳєӣ ҁєʍƀє πѳӡʙѳʜѳӌʜџκ ⱀѧӡъєѣѧɯџʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѳπƴҁϯџʍ ϯѳϯ ѻѧκϯ ӌϯѳ ϯƀӀ ҁƀӀʜѳκ ɯʌѥχџ џ πѳⱀƴѣџʍ κѳҁϯџ ϯʙѳєӣ ʍѧϯєⱀџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πџӡđѧκ ϯʙѳєӣ ʍѧʍѧɯџ ʙƀӀⱀʙѧʌѳ ʜѧχƴӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ґѧʜđѳʜѳʍ єѣѧʌ ϯʙѳѥ ʍѧʍƴ ӌƴⱀκƴ ӡѧϯⱀёπѧʜƴѥ ҁπџđѳӡʜƴѥ ɯʌѥχƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀʙєʍ ʜѧ ϯⱀᴙπκџ ϯʙѳѥ đєϯҁκƴѥ πҁџχџκƴ χѧχѧχѧ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ϯᴙ ⱀѧӡѣєҁџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣєӡ ʜѧđѳѣʜѳҁϯџ ҁѧҁєɯ ϯƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ ʙ ґⱀƴđџʜƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁєɯƀ ʍʜє ʙ ѣʌѳκє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧʙϯѧʜѳʍʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ ʌѳχѧʙҁκƴѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џґʜѳⱀџⱀƴᴙ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯƀ κѧκ ʍѧҁϯєⱀ ѳⱀџґѧʍџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ѻѳⱀєʙєⱀ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧҁκѳɯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ґʌѧʜđƀӀ ʙƀӀєπѧʌ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ʙ ϯᴙ ʙҁϯƴπџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ⱀϯѳʍ ҁѳҁєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧӣѥ ҁπєⱀʍƴ ҁѧѣџⱀѧєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯƀ πѧđ ʜѧѫđѧӌκѧӣ </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ϯєʌκƴ ϯⱀѧχѧʌ πѳκѧ ϯƀӀ ҁπѧʌ κƴκѳʌđ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣʌџѱє ϯʙѳєʍƴ πѧπѧɯє ʍєӌƴ κƴҁκѧʍџ ҁπєⱀʍƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳё πѳϯʜѳє єѣʌѳ ʜѧ ӌʌєʜᴙⱀƴ ʜѧϯᴙʜƴ χⱀѥκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ʙ ϯʙѳё ѳѣχѧⱀκѧʜѳє χѧӌєʙҁκѳє ⱀƀӀʌѳ ҁҁƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ƴ ϯєѣᴙ ƴʍєⱀʌѧ ϯʙѳᴙ ʍѧϯƀ єѣƴӌѧᴙ ɯѧѣѳʌđѧ κѧκ ɯѧʙκѧ πѳđӡѧѣѳⱀʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєӣ ʍѧϯєⱀџ κѳҁϯџ ʜѧ ʍѳʌєκƴʌƀӀ ⱀѧҁπџđѳⱀѧҁџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χѧⱀκѧʌџѱє ϯʙѳєӣ ʍѧʍƴʌџ πџđѳⱀѧҁџʍ ƴ ϯєѣᴙ ʜѧ ґʌѧӡѧχ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧɯƴ ϯᴙ ѱєʜκѧ єѣѧʜѳґѳ πѳ πѳӌκѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳҁϯџ ϯʙѳџ ʜѧ đⱀѳʙѧ κџʜєʍ ҁʌѧѣѧκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌёϯєʜƀκѳ χƴᴙⱀџʍ ϯᴙ ѱєґѳʌ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κѳⱀѳϯƀӀɯκѧ ӡʌѳєѣѧʜƀӀӣ ѳϯҁѳҁџ χƴӣ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ єѣѧʌѳ ʜѧχƴᴙⱀѥ ϯє ҁπєⱀʍѳӣ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳ єѣʌƴ ϯʙѳᴙ ʍѧϯƀ ϯєⱀπџʌѧ ɯʌѥχѧҁϯѧᴙ πѳʌƴӌѧєϯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌєⱀκѧɯ ϯƴѧʌєϯʜƀӀӣ єѣѧʌѳ ӡѧκⱀѳӣ ѳϯҁѳҁʜџκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍѧʍѧɯƴ ϯʙѳѥ ѫѧχʜєʍ ƴϯєʜѳκ єѣѧʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πџđѳⱀѧҁ єѣѧʜƀӀӣ ʙ ѳӌκѳ ɯπѧⱀџɯƀҁᴙ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌπџđѳⱀʜєʍ ƴєѣѧʜκѧ χѳđᴙӌєґѳ πѳ ҁѧʍƀӀє κџɯκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧɯџʍ ҁƀӀʜκѧ ɯʌѥχџ ѳχƴєʙɯєґѳ ʙѳ ʙҁѥ ʍѳѱƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍƀӀɯƀ єѣѧʜѧᴙ ӌʌєʜ ʍѳӣ ʙƀӀҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙџӌѳʙƀӀӣ ҁƀӀʜ ɯѧʌѧʙƀӀ πѳӌκџ ϯє ѳϯπџӡđџʌџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧєѣѧɯџʍ đѳ κⱀѳʙџ ϯʙѳѥ ѳϯπѧʙɯƴѥ πєӌєʜƀ ʜѧχƴӣ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѳʙʜѳ єѣѧϯƀ ҁѳҁџ ʍʜє ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ϯƀӀ ӌє πџđѳⱀɯѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧӡƴӣ ѳϯҁѥđѧ ϯёʌκѧ єѣѧʜѧᴙ ѱѧҁ ϯѳѫє πџӡđƀӀ đѧʍ ϯє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍⱀѧӡѳϯѧ ʜѧχƴӣ ʙ ґѳʙʜџѱє ҁʙѳёʍ πѳπʌѧʙѧӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯʍѧⱀѧ єѣʌџʙѧᴙ ҁʌєӡƀӀ ʙƀӀϯⱀџ џ ʜє χʜƀӀӌƀ πʌѧκҁѧ єѣѧʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳӡѳⱀџѱє єѣѧʜѳє ƴ ϯєѣᴙ єѣѧʌƀʜџκ πѳѣџϯƀӀӣ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯєⱀπџʌѧ ϯƀӀ єѣѧʜƀӀӣ ʙ ϶ϯѳӣ κѳʜѻє ʜѧχƴӣ ҁƀӀʜ ɯѧʌѧʙƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌёⱀʜѳʍѧӡƀӀӣ єѣʌѧʜѳџđ đѧʙѧӣ ӌʌєʜ ʍʜє đєⱀʜџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫџⱀʜѳґѳ ҁƀӀʜѧ ɯʌѥχџ ʍѧϯƀ ҁѳҁєϯ ʜѳⱀʍ ϯѧκ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ πєϯƴχ єѣѧʜƀӀӣ ӡѧʙѧʌџ єѣʌџѱє џ ҁѳҁџ ϯѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єƴ ʜѧχƴӣ πѳ κѧѣџʜє ϯʙѳєӣ πџӡđƀӀ ϯє ʜѧҁƴёʍ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єѣѧϯƀ ϯƀӀ ѧⱀѧ єѣѧʜƀӀӣ χƴᴙⱀƴ ʍѳѥ ӡѧҁѳҁџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌџҁϯѳ ҁƴκѧ ѻƴѻєʌƴ ӌʍѳɯʜѳʍƴ єѣѧʌѳ ʙƀӀѣƀѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ӌє ʜѧχƴӣ ɯπѧκ ƴёѣџѱʜƀӀӣ ӡѧʌƴπƴ ϯƴϯ πⱀѳґʌѳϯџɯƀ   </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳєґѳ πѧπѧɯƴ ʙ ⱀѳϯ єѣѧʌ ʜѧχƴӣ ϯєⱀπџʌѧ ҁƴκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʙʜѧϯƴⱀє єѣѧʌѳ ʙκⱀƴϯџ џ ᴙӣҵѧ ʌџӡʜџ ʍѳџ ӌёⱀϯ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁƴκѧ ϯѧκѳӣ ϯƀӀ ʙѧѻʌёⱀ єѣѧʜƀӀӣ ёѣѧʜƀӀӣ ϯʙѳӣ ⱀѳϯ πҁџʜƀӀӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳϯʜѳє єѣʌѳ ҁʙѳє ӡѧκⱀѳӣ ʍџҁϯєⱀ ӡѧχѧⱀκѧʜƀӀӣ ҁƀӀʜѳκ ɯʌѥχџ ʜѧχƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀ ʙҁє ҁƀӀʜκџ ɯʌѥχ ƴӡκѳⱀѳґџє ʜѧχƴӣ πѳҁѳҁџϯє χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧґџѣѧӣҁᴙ ⱀѧκѳʍ ҁƀӀʜѳκ ɯʌѥχџ ʙƀӀёѣџҁϯƀӀӣ ѫѳπƴ ϯʙѳѥ πѳєѣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁƀӀʜѳκ πѳκѳӣʜѳӣ ӌƴⱀκџ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ʙєҁƀ ϯʙѳӣ ӡʙєⱀџʜєҵ đєϯџɯєκ ɯʌѥχ єѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀⱀʙѧʌ ҁєⱀđҵє ϯʙѳєӣ ʍєⱀϯʙѳӣ ʍѧʍѧɯє ɯʌѥχє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґѧӡƴӣ ѳϯҁѥđѧ ӡѧđѳχʌџκ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳџ πѧϯʌџɯκџ ʙƀӀⱀʙƴ ґѳʙʜѧⱀƀ єѣƴӌџӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ʍѳӣ χƴӣ ҁѳҁѧʌ ʜѧ ҁϯџʌє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ ҁϯⱀџʍᴙʜκџ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ѳѣ ҁʙѳӣ χƴӣ ѳϯѫѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ʜƀӀϯƀєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁ ʙєⱀѧӣ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳ ƴɯџ ϯᴙ ѧѣѧҁҵѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ κѧκ đƀӀɯєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κʙѧɯƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀџʌє ʍѳӣ χƴӣ ƴ ҁєѣᴙ ʙ πџđѫѧκє ҁѫџʍѧєɯƀ ӌϯѳѣƀӀ ѳʜ ҁѳѣѧӌџӣ κѧӣѻ πѳʌƴӌџʌ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧκџđƀӀʙѧєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" џӡє єπџⱀƴѥ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧєѣѧʌ ϯᴙ ҁѳӡⱀєđѧϯѳӌєʜʜѧ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍƀӀҁʌџ ϯє χƴӣєʍ ӡѧѣџʌ џӡє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χʌѳπѧӣᴙ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧӡʙєϯʙџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙⱀѧʜƀёʍ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʜᴙʌҁᴙ ʍѧџʍ χƴӣєʍ џӡє ϯѧκϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡʙєӡđʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀѳҁϯџϯƴϯɯʜѧ ҁѧҁєɯƀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ʍʜє đѧ ҁєӣ πѧⱀƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ πѧđ ѣєⱀёӡѧӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳ πѧʙѧđƴ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ϯᴙ πѧđҵєπџʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧⱀѧʜѧⱀʍѧʌƀʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ⱀџʌє ҁѳҁєɯƀ ʙ ʍѧⱀϯє ѫƴⱀѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁєɯ ϯƀӀ ʍѳӣ ӌʌєʜ κѧɯєʌѳϯκѧ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʍџʜєⱀѧʌƀʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґƴđʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ʍʜє đƴⱀѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ϯᴙ ѧѣκѧʜӌѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧґѧđѧӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧ đєʙџӌƀџ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" κєκʌџʙѧ єπƴ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧӡƀєѣѧʌ ϯᴙ χƴӣєʍ ʌєχκѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" đџκѧ ʍʜє ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜѧ πѧʌєʙє єπƴ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѫʍєɯƀҁᴙ ѧϯ ʍѧџґѳ χƴӣᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ɯєʌκѧʙџҁϯѧ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀѧϯџʙʜѧ єπƴ ϯᴙ ɯѳʌѧʙƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ʙ ϯᴙ κѧϯѳⱀƀӀӣ ⱀѧӡ џӡє ϯѧκϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧӡπѳϯⱀѧɯџʌ ϯᴙ ӌʌєʜѧʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ ʙ ӡƴѣƀӀ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀґʜѧʌ ϯᴙ χƴӣєʍ ʌєχκѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁϯⱀѧπϯџʙѧ ҁѧҁєɯ ϯƴπѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ ҁӌѧҁϯʌџʙƴѥ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πⱀѧѣʌєʍѧϯџӌʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӡѧґʜƴʌ ʙ ϯє χƴӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѳⱀєɯѧʌ ϯᴙ ӡѧʌƴπѳӣ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌϯѳ ϯѳ ϯƀӀ ɯѳʌѧʙѧ ѳϯҁѳҁѧʌѧ ʍʜє ʜѧ џӡє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" єπƴ ϯᴙ ʍєϯκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧκѧⱀʍџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣѳʌƀʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧϯҁѧҁѧʌѧ ʍʜє ҁʌєϯѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁⱀѧӡџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌ πⱀџʜƴѫđєʜѧ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ χѧⱀѧɯєʜƀκѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ʙ ϯᴙ πѧπѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѣџⱀєɯƀ ʍѳӣ ӌʌєʜ ϯѧκϯѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ʍʜє κⱀƴϯєӣɯʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁđƴʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ӌєⱀєӡ ѧʜѧʌ џӡє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʜє ѣѧʍѣџ đƴⱀʜѧᴙ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѧҁєɯ ʍʜє ɯѳʌѧʙʌџʙѧᴙ κƴⱀʙѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ӌʌџʜ ҁѧҁєɯƀ πѧ ѳѣƀёʍƴ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯʙѧᴙ ʍѧϯƀ ɯʌєɯκѧ єѣƴ єё ϯѧκ ϯѳ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" χƴӣєʍ ϯᴙ πѧєπѧʌ џӡє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ᴙ ϯᴙ ʙƀӀđⱀƴ ӌʌєʜѧʍ πʜƴʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ⱀѧҁѣєʌ ϯє єπѧʌѳ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧ πⱀѧκƴⱀѧϯƴⱀҁκє ϯƀᴙ πѧєѣѧʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ѧϯʌџӌʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πѧđѣџⱀѧѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁѳҁєɯƀ ʍʜє πѳ ʜѧҁϯѳᴙѱєʍƴ κⱀƴϯѳ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ґƴʌᴙѥ πѧ ϯє χƴӣєʍ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ϯƀӀ ҁѧҁѧʌѧ ʍʜє đџκѳʙџʜѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙƀӀєѣѧʌ ϯᴙ ƴ đєⱀєʙѧ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" πҁџχџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ҁʌƀӀɯƀ џґʜѳⱀʜѧᴙ ҁѳҁџ ʍʜє ƴѫє  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʌѧχѧϯʌџʙѧᴙ χƴӣєʍ ϯᴙ ⱀѧӡѣєʌ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",
" ʙ ӡƴѣƀӀ ϯʙѳџ ᴙ ҁʙѳӣ ӌʌєʜ ѣⱀѳҁџʌ ѧⱀƴ  </a> <emoji document_id=5341497469932938890>🚬</emoji> ",]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl11))
            await sleep(0.1)
            await sleep(time)

    async def кровьcmd(self, message):
        """интᴇᴘвᴀл в сᴇкʏндᴀχ + тᴇкст """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
                               "<b>𐌺ρ᧐ʙь ɜᥲκ᧐нчᥙ᧘а ʙыᥰᥙʙᥲᴛь κρ᧐ʙь δ᧘ядᥱᥔ <emoji document_id=5784974820592586088>🔥</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>𐌺ρ᧐ʙь нᥲчᥲ᧘ᥲ ʙыᥰᥙʙᥲᴛь κρ᧐ʙь δ᧘ядᥱᥔ <emoji document_id=5784974820592586088>🔥</emoji></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl12 = [" ϯƀӀ πџđѳⱀѧҁ єѣѧʜƀӀӣ ʙ ѳӌκѳ ɯπѧⱀџɯƀҁᴙ ҁƴκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧ ҁπƴϯʜџκѧ ʙ ϯᴙ ҁҵѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌѧđџʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ⱀƴκѧʙџҵƀӀ ҁҵƴ ϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƀӀπⱀᴙʍџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џҁϯєⱀџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ џґʜѳⱀʜѧᴙ ҁѳҁџ ʍʜє ƴѫє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ӡѧπѧҁє ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʍџⱀѧєɯƀ ƴѫє ʜѧ ʍѳєʍ χƴє χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍđᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ⱀџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧⱀѧӡʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ӡѳʜє ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡҁѳʙєҁʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʙ ƴґѧʌ ʙƀӀґʜѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѧᴙ ʍѧϯƀ ҁѧҁєɯ ґѳʌѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧϯκⱀѧʙєʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʜѧđʙџʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣƴχѧᴙ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧⱀʙѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯёⱀ ϯᴙ ɯѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯє ѧđєѫđƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳχʜєɯƀ πѳ ʍѳєʍƴ χƴӣѥ ɯѳʌѧʙʜѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧκⱀѧѣѧϯʌџʙѧᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πѧđѧґⱀєʌ ɯѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ѳѣʌѧπѳɯџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џπƴ ϯᴙ ʌєχκѳʙѧϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѳѣƴџɯ ʍѳӣ ӌʌџʜ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌʌєʜѳʍ ϯƀӀ ⱀџʌє πџӡđѳɯџʌ ѫѧѣƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣѧʌ ϯᴙ ӡѧѫџϯѧӌʜѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κҁϯѧϯє ϯʙѧѥ ʍѧϯƀ џπџⱀƴѥ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ҁϯƴʌє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєⱀχѳʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧґƴⱀϯᴙѱє ҁѧҁєɯ ѧⱀƴѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ӡѧɯκʙѧⱀєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƴɯƴ ϯᴙ ɯѳʌѧʙƴ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʍєϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯєҁϯџκⱀѧϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡʍєⱀʜѧ ҁѧҁʜƴʌѧ ϯƀӀ ʍʜє ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧ ϯƀӀ ҁѳҁєɯƀ ʌѳχ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧπӌƴ ϯᴙ ҁʙѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡє ґʌѧϯѧєɯƀ ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πƀӀχϯџɯƀ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡѣⱀѧʜѳ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѧϯ ѣѧʌđƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ɯѧκѧʙʌџʙѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀѧʙѧπѧϯєⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴѣџđџϯєʌƀʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κҁϯѧϯџ ҁҁѧʌ ʙ ϯᴙ ɯκƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ϯѧκϯѧ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ʙ ϯᴙ ʍѧχʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧʍѣєɯ ɯʌѥχӡѧʙѧϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙѧѱєϯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ ϯѧⱀџѻ ҁʍѧⱀϯ ϯᴙ єπѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ⱀџʌє ҁѳҁѧʌѧ ʍʜє ѳκѳʌѳ ʍєҁᴙҵѧ ʜѧӡѧđ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯєⱀӡѧӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʌѥɯκѧ ҁѧҁєɯ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴđѧⱀџʌѧҁƀ ϯƀӀ ѧѣ ʍѳӣ χƴӣ ʙѱєϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁ ƴϯⱀѧ ҁѧҁєɯ ʍѳӣ ӌʌєʜ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đⱀѳѣџɯƀҁᴙ ѳѣ ʍѳӣ χƴӣ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧκⱀѧѣѧϯџɯƀ ʜѧ ʍѧӣѳʍ χƴӣѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧӌєɯƀ ʜѧ χƴӣѥ χџχџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʌѧѫџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙʌѥѣџʌ ϯᴙ ʙ ҁʙѳӣ χƴӣ ʌєχκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κҁϯѧϯџ κѧκ ґѧʍʌєϯ ϯᴙ єѣѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ʜѧϯƴⱀє ҁѳҁєɯƀ κѧʌѳⱀџӣʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ κⱀѧєʍ ҁѧҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ đєκѧⱀƀ єѣѧʌ ϯᴙ κєκ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ʙ ɯѧⱀѧɯκє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙƀӀđⱀƴ ʜѧ πєⱀџʌє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπѧʌ ϯᴙ đƴⱀʜƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣџѫєʜѧᴙ ᴙ ϯᴙ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧđⱀєʜѧʌџʙѧʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧϯʍџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ʍѳӣ χƴӣ ҁѳҁѧʌ ʜѳѥѱѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʙᴙӡѧʜѧ κ ʍѳєʍƴ χƴӣѥ ɯѳʌѧʙʜѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ πєʜџҁ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє κⱀƴϯєӣɯʜѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀџʌ ϯᴙ χƴӣєʍ ʙƀӀⱀѧѱƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƴєɯƀҁᴙ ʜѧ ʍѳӣ χƴӣ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ χƴӣ ҁѳҁџ ʍʜє πѳκѧ ƴ ϯєѣᴙ єѱє ґƴѣƀӀ ʜє ѳѣҁѳχʌџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧⱀѧҁϯⱀєʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ƴӌєѣʜѧ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʜᴙʌҁᴙ ʍѧџʍ χƴӣєʍ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌƴʙҁϯʙƴᴙ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ɯκѳʌє ҁѧҁєɯ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πѧҁϯєʌє ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙʌџʙѧᴙ χƴӣєʍ ϯᴙ πѧđѧⱀʙѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκⱀџѣƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ χє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ϯѧӣҁκѧ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡѧѣѳϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧⱀƴ ҁѳҁєɯƀ ʙ ѣƴχϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƀӀɯѧ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ πѧ πⱀѧʙѧʍƴ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ʌєϯƴ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀκѧѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡʙѧʌџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đџπʌѳʍѧϯџӌєҁκџ ҁѧҁєɯ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πѳⱀʜѧѻџʌƀʍє ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ѳӌєⱀєđџ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ єѣѧʌ ʜє ƴκѧӡѧʜʜѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʍєϯκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʍƴӌѧӣѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ʜєʙџđџʍѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πєⱀєʍєʜє ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ πѳκѧ ʍєʜᴙ ʜєϯ đѳʍѧ ѧⱀƴ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѧѥ ʍѧϯƀ χƴӣєʍ πѧ ʍѧⱀѱџʜѧʍ ϯⱀѳґѧѥ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ѧӡѧʌѧϯџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χѧⱀʌѳʙѧ ҁѳҁєɯƀ πѳ χѧⱀđκѳⱀƴ ⱀџʌє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ πџӡѫєʜʜƴѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧʍѣʌѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧџʙʜѧ ҁѧҁєɯ ɯѳʌѧʙʜѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ґʌѧӡ ʌѧɯʌџʙѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁƴ ϯє ʙ ґѳⱀʌѳʙџʜƴ ґƴҁƀӀʜє єѣѧʜѳӣ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ đѳχʜєɯ ʌєχκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧҁϯƴπџʌ ʜѧ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πƴҁϯѳϯʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ҁ đѧҁϯѳџʜҁϯʙѧʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧκⱀѳҁєʌ ϯᴙ ӌʌєʜѧʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳđʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌѧʙʜєє ʙҁєχ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳϯⱀᴙҁѧѥѱє ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѳʍѣʌѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳѣџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ κⱀƴϯџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѳҁϯџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧӡѧⱀϯʜѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҵєʌƴєɯƀҁᴙ ҁ ʍѳџʍ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џɯѧӌƴ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧκџʜƴʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧχѧᴙ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁƴʍѧҁɯєđɯє ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁπџҁѧʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѫџӡʜєʜʜѳ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴπѳⱀʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƀӀπѧⱀџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧκϯєⱀҁκџ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƀӀⱀᴙʙѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ӡѧʍєӌѧϯєʌƀʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧѥκѧѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙπџϯƀӀʙѧєɯƀ ʍѳѥ ҁπєⱀʍƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ κѧӡѧⱀʍє ҁѳҁѧʌѧ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʜҵџπџѧʌƀʜѳ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙҁϯⱀєӌє єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙѳɯєʌ ʙ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯєⱀєѣџɯƀ ʍѳӣ χƴӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѳʜӌѧѥ ϯє ʙ ґѳⱀʌѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʍєᴙҁƀ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ⱀѧӡʌѳʍџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєđѳʙѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѳʌѣџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєⱀєѱѧ ʍʜє ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ґѧⱀѧʜϯџџ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧʜҵƴѥ ҁʙѳџʍ χƴєʍ ʜѧ ϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁ ʍѳџʍ χƴєʍ ѣєґѧєɯƀ ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯⱀєʍᴙҁƀ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʜѧӣҁ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ӡѧѱџϯџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ κѧϯѧʌҁᴙ ʜѧ ϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєⱀєѧʌƀʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƀӀґѳđʜѳ ʍʜє ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ʙ κƴđⱀџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙƀӀґѳđє ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳđѧⱀѳӌʜѳ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀѧҁʜѳʙѧϯѧ ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґѳʙѳⱀʌџʙѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ʙ ӡƴѣƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџ đѳѫđє ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ κѧⱀѧӌκѧχ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѳϯџʙʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ κѧʌѧӌƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʌƀӀѣѧᴙҁƀ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ʙƀӀκⱀƴϯџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ κѧʜҵєʌᴙⱀџџ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ѣєӡ πⱀџӌџʜƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƴⱀʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯєҁϯџκⱀѧϯʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ѣєʌѳʍ ѻѳʜє ҁѳҁєɯƀ πєⱀєʍєʜє </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ χƴӣ κⱀѧҁџʙѳ ҁѳҁєɯƀ ϯƀӀ ϯѳπѳʙƀӀӣ χƴєҁѳҁ ʙκѳʜϯƴκϯє ӌϯѳ ʌџ?   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ѳѣѳҁҁѧʌ ϯʙѳѥ ʍѧϯƀ ҁ ʜѳґ đѳ ґѳʌѳʙƀӀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ʍѧϯƀ ϯʙѳѥ ʙʙєⱀχʜѳґѧʍџ єѣƴ ѣʌᴙϯƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ʍѧϯƀ ϯʙѳᴙ ʍѳӣ χƴӣ ҁѳҁёϯ κѧκ ʌᴙʙⱀѧ єѣѧʜѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ⱀџʌџ ѱѧҁ ϯʙѳєӣ ʍѧϯєⱀџ χƴєʍ ѻѳѻѧʜѧ πⱀѳπџɯƴ χƴєҁѳҁ ϯƀӀ єѣѧʜƀӀӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ џӡє єѣƴ ҁʌєϯѧκ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳџʍ χƴёʍ ʍѳʜџπƴʌџⱀƴєϯ єӡ єӡ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌ κѧѣєʌєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍƴ ϯʙѳѥ πⱀџκƴⱀџʙѧϯєʌєʍ єѣƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀџʌ ϯʙѳᴙ ʍѧʍѧ χƴӣ ҁѳҁёϯ ʙ πѳʌᴙχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧʍƴ πѳ ѣʌѧϯƴ єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴёʍ ґƴʌᴙєϯ κѧκ ҁѳѣѧӌκѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳӣϯѧ ʍѳӣ χƴӣ ҁѳҁёϯ ʜѳⱀʍ ϯѧκ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣѧʌ ʜѧ κѳⱀѳѣκє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӌєʜґџҁχѧʜ єѣѧʌ ƴ ʍєʜᴙ ʜѧ ґʌѧӡѧχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ χƴёʍ ҁʙѳⱀџʍ ӌѳϯѧ ӡѧѣџʌ ʙ ҁʍєⱀϯƀ χєχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍє ϯʙѳєӣ ʍʙѳџʍ χƴёʍ ӌѳϯѧ ⱀѳϯ ҁʌѳʍѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ᴙ ϯʙѳєӣ ʍʍє χƴёʍ ѱёκџ πѳⱀʙѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʍѳӣ χƴӣ ҁѧҁёϯ χєχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍƴ ϯʙѳѥ єѣѧʌ ʜѧ κⱀƀӀɯє ӡѧπѳⱀѳѫҵѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӌѳϯѧ єѣѧʌ ʙџʌѧʍџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳӣ χƴӣ ϯʙѳѥ ʍѧϯƀ đƴɯџϯ κƴʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʜѧ ʍѳёʍ χƴ ґѳʌѳπѳʍ ҁκѧӌєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳёʍ χƴѥ đєҁѧʜϯџⱀƴєϯҁᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ҁ ʍѳџʍ χƴёʍ ʙ κџʜѳ χѳđџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ єѣƴ ѧ ɯϯѳ?   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӌѳϯѧ χƴёʍ ⱀѧӡѣџʌ κѧκ ʙѧӡƴ ѻѧⱀѻѳⱀѳʙƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ʜѧ Ǝʙєⱀєҁϯє єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʍʜє ʙ χƴё ʍƴⱀʌƀӀӌџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯ ʍѧϯƀ ϯʙѳѥ єѣƴ ʜѧ ƴʙѧӡџκє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πџӡđѧκ ϯʙѳєӣ ʍѧϯєⱀџ ʙѧґѳʜƀӀ ӡѧґѳʜᴙѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πџӡđѧκє ϯʙѳєӣ ʍѧϯєⱀџ ʌѳκѳʍѧϯџʙƀӀ ʜѳӌƴѥϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πџӡđѧκє ϯʙѳєӣ ʍѧϯєⱀџ πⱀџπѳⱀκѳʙѧʙƀӀѥϯҁᴙ đѧʌƀʜѳѣѳӣѱџκџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍκƴ ϯʙѧѥ ϯⱀѧχѧѥ ʙ єѣѧʌѳ χєχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ єѣƴ ӌѳϯѧ ʙѳ ʙҁє ѱєʌџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʍѳӣ χƴӣ ҁѳҁёϯ πѳҁƴđѳʍѳӣκѧ єѣѧʜѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ πʌєєⱀѳʍ џӡє єѣƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πџӡđѧκ ϯʙѳєӣ ʍѧʍƀӀ ҁѧѣ χƴёʍ ƴҁϯѧʜѳʙџʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ πџӡđѧκѳʍ ϯʙѳєӣ ʍѧϯєⱀџ ʌѧʍπѳӌκџ ʙ πѳđъєӡđѧχ ʙƀӀκⱀƴӌџʙѧѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍƴ ϯʙѳѥ єπƴ κƴʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧʍƴ єѣѧʌ ӌѳϯѧ ƴ ϯєѣᴙ ʜѧ πѳᴙҁʜџҵє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʍѳӣ χƴӣ ҁѳҁёϯ κѧκ џѣѧʜƴϯѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ᴙ ҁʌƴӌѧӣʜѳ χƴёʍ ϯʙѳєӣ ʍѧʍє ⱀѳґѧ ҁʌѳʍѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳѳϯ ʍѧϯƀ ϯʙѳᴙ χƴӣ ʍѳӣ ҁѧҁџⱀƴєϯ κѧκ џѣѧʜѧɯκѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀџʌ ʍѧʍƴ ϯʙѳѥ ӌѳϯѧ єѣƴ ҁϯƴʌѳʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʙƀӀєѣѧʌ ӌѳϯѧ ʜѧ ҁѳѣєҁєđѳʙѧʜџє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ѱѧҁ ʙʜѧϯƴⱀє ϯʙѳѥ ʍѧϯƀ ҵƀӀґѧʜᴙʍ πⱀѳđѧʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ѫє ѱѧҁ ϯʙѳѥ ʍѧϯƀ ʜѧҁ ҁʙѳӣ χƴӣ κѧκ πѳκⱀƀӀɯκƴ ѳđєʜƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ѱѧҁ ⱀџʌκ ϯʙѳѥ ʍѧϯƀ ʜѧ ѳⱀѣџϯƴ ӡѧπƴѱƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ʙʜѧϯƴⱀє ϯʙѳєєӣ ʍѧϯєⱀџ ҁєⱀєѫκџ χƴєʍ ʙҁϯѧʙʌᴙʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ єѣƴ ϯʙѳѥ ʍѧϯƀ ʜѧ πѳđѳκʜʜџκє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ ҁєӣӌѧҁ ⱀџʌ ϯʙѳєӣ ʍѧєϯⱀџ ѳӌκѳ χƴєʍ ⱀѧӡѳґⱀєѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙҁєӣӌѧҁ ϯʙѳѥ ʍѧϯƀ πⱀѳđѧʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ѱѧҁ ʙʜѧϯƴⱀє ϯє ӡƴѣƀӀӣ πєⱀєҁӌџϯѧѥ χƴєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ϯʙѳᴙ ʍϯѧƀ ʜѧ ʍѳєʍ χƴє κѧκ ʌѳɯκѧđκѧ ҁκѧӌєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ ҁєӣӌѧҁ ʙʜѧϯƴⱀє ϯʙѳѥ ʍѧϯƀ ʜѧ ҁʙѳӣ χƴӣ ʜѧҁѧѫƴ κѧκ ʜѧ ϯѧѣƴⱀєϯκƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴєѣѳκ ᴙ ѱѧҁ ʙʜѧϯƴⱀє ϯєѣᴙ χƴєʍ πєⱀєєđƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ϯʙѳѥ ʍѧϯƀ єѣƴ κѧⱀѳӌє ѳʜѧ ƴʍџⱀѧєϯ ѳϯ ϯѳґѳ ӌϯѳ ʍѳӣ χƴӣ ʜѧҁџʌƴєϯ єё ґѳⱀʌѳ-   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ϯʙѳѥ ʍѧϯƀ πѳđ ҁϯѳʌѳʍ єѣƴ ѧ ϯƀӀ χƴӣ ҁѳҁєɯƀ џ ӌє ѳⱀєɯƀ?-   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ єѣѧʜѧᴙ χƴєґʌѳϯџʜѧ ᴙ ʙʜѧϯƴⱀє ϯʙѳѥ ʍѧϯƀ ӌєⱀєӡ ⱀєκƴ κџđѧʌ-   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ ҁєӣӌѧҁ ⱀџʌ єѣƴ ϯʙѳѥ ʍѧʍѧɯƴ-   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ ʙʜѧϯƴⱀє ϯʙѳѥ ʍѧϯƀ єѣƴ ʜѧ ϯѧѣƴⱀєϯκє-   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ πѳʜџʍѧєɯƀ ӌϯѳ ᴙ ⱀџʌ ϯʙѳєӣ ʍѧϯєⱀџ ӡƴѣƀӀ χƴєʍ πєⱀєҁӌџϯѧѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӌѳϯѧ єѣƴ ҁƴϯκѧʍџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ɯѳʌѧʙѧ єѣƴӌѧᴙ χƴӣ ҁѳҁёϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ӌѳϯѧ єѣƴ ҁʍѧⱀϯѻѳʜѧʍџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ʍѧϯƀ ϯʙѳѥ ʙ ϯєʌєѻѳʜʜѳӣ ѣƴđκє єѣѧʌ χєχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳ ᴙ ϯʙѳѥ ʍѧϯƀ єѣƴ ѧ? ⴼє πѳđҁκѧѫєɯƀ?   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ӌѳϯѧ ⱀџʌ єѣƴ πѳđ κʌџπƀӀ ϯџʍѧϯџ χєχ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳ ʍѧϯƀ ϯʙѳᴙ ʜѧ ʍѳёʍ χƴѥ χѳⱀѳɯѳ ҁџđџϯ ҁ4κѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџҁѳєđєʜᴙӣҁᴙ κ ҁʙѳєӣ ʍѧʍє ʍѳӣ ƴχӣ ҁѳҁѧϯƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍƴ ϯʙѳѣѥ єѣƴ ʜѧʍѧʜѧ ϯѧκ πѳκѧ ӌϯѳ ϯƀӀ πʌѧӌєɯƀ χєχ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ӌѳϯѧ єѣƴ ʙ ⱀѳϯѧʜ κєκ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ⱀџʌ ϯʙѳѥ ʍѧϯƀ єѣƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ ƴєѣѳκ ʜѧχƴӣ ᴙ ѱѧҁ ϯʙѳѥ ʍѧϯƀ πⱀѳđѧʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ϯʙѳєґѳ ѳϯҵѧ єґѳ ⱀϯѳʍ κѧϯѧʌ ʜѧ ҁʙѳєʍ χƴє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁϯ ᴙ ϯʙѳѥ ʍѧϯƀ ʙ ґѳⱀʌѳ đⱀѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯʙѳᴙ ʍѧϯƀ ϯєѣє ʜѧ єѣѧʌѳ ⱀƀӀґѧʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ʙʜѧϯƴⱀє єѣƴ ϯʙѳѥ ʍѧʍѧɯѧƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ πѳđ ҁϯѳʌѳʍ ϯʙѳєӣ ʍѧϯєⱀ ґѳʌѳʙƴ ⱀѳӡʌѳʍџʌ χƴєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ᴙ ϯʙѳѥ ʍѧϯƀ ʜѧ ⱀƀӀʜκє πⱀѳđѧʌ ӡѧ ɯѧʙєⱀʍƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєҁѳҁ ϯƀӀ ҁѳҁѧʌ ʍѳӣ χƴӣ ƴєѣѳκ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ҁƴκѧ ѱѧҁ ѫє ҁѳҁєɯƀ ʍѳӣ χƴӣ ƴєѣѳκ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ӡѧѱєκѧʜκѧ єѣѧʜѧᴙ ᴙ ʙʜѧϯƴⱀє ʙъєѣƴ ϯʙѳєӣ ʍѧϯєⱀџ πѳ ґƴѣѧʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ѱѧҁ ʙʜѧϯƴⱀє ѣƴđєɯƀ ҁѳҁѧϯƀ ʍѳӣ χӣ κѧκ κѳʜѻєϯƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ѫє єѣѧʜƀӀӣ ӡѧѱєκѧʜ ҁѳҁєɯƀ ʍѳӣ χƴӣ πⱀџҁџđѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƀӀ ʙʜѧϯƴⱀє κѧκ ⱀƀӀѣѧκ ҁʙѳџʍ ⱀϯѳʍ ʌѳʙџɯƀ ʍѳӣ χƴӣєʍ </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ⱀѧӡⱀєɯєʜџᴙ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƀӀʍᴙ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳӣ χƴӣ ѣєⱀєɯƀ ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ κⱀƴϯѳʍƴ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯє ʙ ʌџҵѳ ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧʙѧʌџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʌѥѣџʍѳ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍƴϯƴѫƴ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯє ƴɯџ πѳⱀʙѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ʙ ґⱀƴđџʜƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣ ʙ ϯᴙ ʙҁƴʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌєⱀʜѳʙѧϯѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳκѧᴙ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ πѳʜᴙϯџᴙʍ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀѧđџҵџѳʜʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀѳʍκѧ ϯᴙ єѣƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƀӀʍѧӡѧʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ⱀєҵєπϯƴ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ⱀѧҁɯџѣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌƴϯκѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙҁϯƴπџʌ ʜѧ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʜє đƴʍѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌѳʍѧʌ ϯє χƴєʍ ʌџҵѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍƴӌѧᴙҁƀ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѳ πѧⱀƀӀ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯⱀєʌᴙʌ ʙ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ґʌƴѣѳκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍѳʌѳđѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁκⱀƀӀʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ʜѳʙѳӣ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍʜє ʙєҁєʌѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳϯκⱀѳʙєʜʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѧʜϯѧѫџⱀƴѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ӡѧʍєⱀџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍʜє χƴӣ ѣєӡƴʍʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đєⱀƴ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁӌѧҁϯʌџʙѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴѱєʍџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєӌƴ ʙ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ џӡʙєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѻѧʜϯѧӡџⱀƴᴙ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳѣѳⱀѳʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳʌѧҁκѧʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙѳʌɯєѣʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ҁκџʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳϯⱀᴙҁ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡⱀᴙ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍʜє πⱀџӌƴđʌџʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍᴙʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƀӀѣⱀѧʜѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ πѳʜᴙϯџᴙʍ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ҁπⱀѳҁѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌƴʙҁϯʙƴᴙ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌѧѣѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡƀӀκѧѥ ʙ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʌѧѣџʌƀʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯƴϯʌџʙѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џҁπѳʌƀӡƴѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʙєʌ ϯᴙ ʙ ӌƴʙҁϯʙѧ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѫџӡʜєʜʜѳ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁ ʙєⱀѳӣ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣѧʌѳ ϯє πѳϯƴɯџʌ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџϯᴙʜƴʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡʍџʜџⱀѳʙѧʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧđƴᴙҁƀ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙѳҁχџϯџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѳʌєӡʜєʜʜѳ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ӡѧκʙѧҁџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ đѳπѳʌʜџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πєⱀєκʌѥӌџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀєѣƴ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁϯѳπџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ʍѧҁϯџ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ϶ʍѳҵџӣ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џҁκѧӡџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѫѧʌєѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ χѳѣѳϯѳκ ϯᴙ χƴєʍ đєⱀѫƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍʜє ʙ ʍѳⱀґє ʍєⱀϯʙѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁџʍπѧϯџӌʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯⱀѳӣʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ѳӌєⱀєđџ ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ҁπѳκѳӣҁϯʙџџ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ πⱀџʍєϯƀӀ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧѣѳϯѧѥ ʜѧ ϯє χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ѣѳʌƀɯѳʍƴ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧҁϯѧʙџʌ ʜѧ ϯᴙ χƴӣ ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧϯƴⱀѧʌƀʜѧ ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєπѳҁєđʌџʙѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʍʜє κⱀџϯџӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѣʌєґӌџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʜџϯѧⱀʜѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκʌѳʜџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πєⱀχѳϯʜѧᴙ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѳʜӌџʌ ϯє ʙ πѧκʌє ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџκѳҁʜƴʌҁᴙ κ ϯє χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ ҁєκƴʜđƀӀ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πєⱀєκѧϯџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍʜєɯƀҁᴙ ѳѣ ʍѳӣ χƴӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʍєⱀʜѧ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ӡѧґҁє ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ʙџʜƀӀ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѧʙđџʙѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѧʌєκѳʙѧϯѳ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ κƴⱀҁƴ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳҁєϯџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ѣѧɯκƴ ϯє ҁҁƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѳⱀʍʌѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳӡđⱀѧʙџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧκʜƴʌ πѳ ϯє χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙҁᴙӌєҁκџ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ҁѳҁʌѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѳʌκѧѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џҁκⱀєʜʜє єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳҁʙєϯџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ґʌѧӡѧχ ʍѳџχ ҁѳҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ ѳϯʜѳɯєʜџӣ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ƴπѳʍʜџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ƴϯєҁє ҁѳҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙѳʌʜє єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧϯʍџʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌџʌ ϯᴙ ʜѧ ҁʙѳӣ χƴӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєӡ đєʌѧ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ⱀѧҁҁϯѳᴙʜџџ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ѳҁʙѳѣѳđџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ⱀѳđʜѳʍƴ єѣƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ƴʌѳʍѧʌ ʌєґκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙᴙκѧᴙ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґѳⱀᴙӌѳ ҁѳҁєɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯєⱀӡѧѥ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡѳӌѧⱀѳʙѧʌ ϯᴙ χƴєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧӡѳⱀʜѧ ҁѳҁєɯƀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
"   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳӣ χƴӣ ϯᴙ ѱѧ ѳϯъєѣєϯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ʜѧ ʍѳєʍ χƴѥ κѧκ đѳʍѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" Ҁκѧӌѧɯƀ ʜѧ ʍѳє χƴѥ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯƀ ʍѳӣ χƴӣ ʜѧ χѧϯє ƴ ҁᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯƀ ʍʜє ӌѳϯѧ ʍєđʌєʜʜѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙπџϯƀӀʙѧєɯƀ ʍѳѥ ҁπєⱀʍƴ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ϯⱀѳʌʌџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ʙ ѧʙϯѳѣƴҁє χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ӡƴѣƀӀ ҁʌѳʍѧʌ ϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѳʜӌѧѥ ϯєѣє ʙ ґѳⱀʌѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" Ҁѧҁєɯƀ ʍѳӣ χƴӣ πџӡđѧκѳʍ ѧⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯƀ ʍѳӣ χƴӣ đƴʍѧєɯƀ ӌϯѳ ʌєđєʜєҵ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ πⱀѳґʜƴʌ ϯᴙ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯƀ ʍѳӣ ƴχӣ đƴʍѧєɯƀ ӌϯѳ ʍѳđʜƀӀӣ?  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯƀ ʍѳӣ χƴӣ ѧϯʌџӌʜѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯᴙ ѱѧ ⱀѧӡʌѳʍѧѥ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ѳϯъєѣѧʌ ϯʙѧѥ ʍѧϯƀ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴєʍ ϯєѣє ѱѧҁ ⱀѳϯ ʙƀӀⱀʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ πѳđ ʙєϯⱀџʜѳӣ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ ʙ ѳӌκѳ πѳєѣƀӀʙѧѥ ҁʌƀӀɯƀ ѳѣѳҁҁѧʌ ʙџҁκџ ϯʙѳєӣ ʍѧϯєⱀџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ єѣƴ κѧκ ʙƀӀđⱀƴ єѣѧʜƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ ӌє ʍѳӣ χƴӣ ҁѳҁєɯƀ κѧκ ʌєʍƴⱀ єѣѧʜƀӀӣ?   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ʍѧʍκƴ ϯʙѳѥ ʜѧ џӡџ ѳѣѳҁҁѧʌ κҁϯѧϯє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ʍѧʍκƴ ѱѧҁ ϯʙѳѥ ⱀџʌџ ʙƀӀєѣƴ ʙ ѳӌκѳ πѧʌκѳӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ѱѧҁ ⱀџʌџ ϯєѣє ѣѧʜѧʜ ʙ єѣѧʌѳ κџʜƴ ѳѣєӡƀᴙʜѧ єѣѧʜѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ѱѧҁ ʙ πџӡđє ϯʙѳєӣ ʍѧϯєⱀџ ʍѳґџʌƴ χƴєʍ ʙƀӀⱀѳѥ џ ϯєѣᴙ ϯѧʍ πѳχѳⱀѳʜѥ ӡᴙѣʌџκ єѣѧʜƀӀӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ χƴєҁѳҁ đѧ đѧ ϯƀӀ χƴӣ ʍѳӣ ҁѳҁџ đѧʙѧӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍκƴ ϯʙѳѥ єѣƴ χƴєʍ κѳⱀѳʌᴙ ѣєҁҁʍєⱀϯʜѳґѳ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ϯʙѳѥ ʍѧϯƀ ʙ đєⱀєʙʜє κѳϯџκѧ ʙєⱀχѳʙʜѳґѳ єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ϯƀӀ ʜѧ ʍѳёʍ χƴѥ κѧκ ѳʙѳѱƀ ѣʌᴙϯƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ϯєѣє ѱѧҁ χƴӣ ʙ єѣѧʌѳ κџʜƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
"  ҁʌƀӀɯƀ ϯʙѳᴙ ʍѧϯƀ πѳđ ҁϯѳʌѳʍ ʍѳӣ χƴӣ đѳ κѳҁϯџ ѳѣҁѧҁƀӀʙѧєϯ ʍѧʜđѳʙѳɯκѧ єѣѧʜѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ϯѥʌєʜƀ єѣѧʜƀӀӣ ʜ ʍѧϯƀ ϯʙѳѥ ʜѧ χƴє ʙєⱀӌƴ κѧκ χѳӌƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ᴙ ѱѧҁ ҁʙѳӣ χƴӣ ʙ πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ κџʜƴ κѧκ ѣƴϯƀӀʌκƴ ʙ ѳӡєⱀѳ    </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌƀӀɯƀ ϯʙѳᴙ ʍѧϯƀ ʍѳӣ χƴӣ ʍѳѱʜѳ ҁѳҁёϯ </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳӌєʍƴ ϯʙѳє єѣѧʌ ѳ κѧκ đʙєⱀƀ ѳϯ ӡѧπѳⱀѳѫҵѧ πѳκѧ ʜє єѣʜєɯϯ ʍѳџʍ χƴєʍ ʜє ӡѧκⱀѳєϯҁᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧѫџ ѧ κѧκ ϯƀӀ ʍѳӣ χƴӣ ҁʙѳєӣ ґƴѣѳӣ ѧκϯџʙџⱀѳʙѧʌ?   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѳѣ ʍѳӣ χƴӣ ӡƴѣƀӀ ϯѳӌџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ƴ ʍєʜᴙ ʜѧ χƴѥ ӡєʌєʜєєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ κ ʍѳџʍ ᴙӣҵѧʍџ κѳⱀʜџ πƴҁϯџʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ κⱀѧҁʜєєϯ ƴ ʍєʜᴙ ʜѧ χƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѳѣ ʍѳӣ χƴӣ ʜѧ πџӡđє ʍѧӡѳʌƀ ʜѧϯєⱀʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳєʍ χƴѥ πʌѧʙѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯѧѳѥ ʍѧϯƀ χƴєʍ ѳϯπϯӡđџʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѫєʜџϯҁᴙ ʜѧ ʍѳєӣ ӡѧʌƴπє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѳϯ ϯʙѳєӣ ʍѧϯєⱀџ ѣⱀѧϯџɯκѧ ʍѳџχ ᴙџҵ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ πⱀѳҁϯ πєⱀđѳʌџⱀƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ґѳⱀџϯ ƴ ʍєʜᴙ ʜѧ χƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ πєⱀđџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴєʍ πѳ ƴϯⱀѧʍ κⱀѳʍ єѣѧɯџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ʙ ⱀѳϯ єѣƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳӣ χƴӣ ѫѳπѳӣ ґⱀƀӀӡєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁѳχʜєϯ ʜѧ ʍѳєʍ χƴѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ҁπєⱀʍѳӣ ҁʍѧӡѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳєʍ χƴѥ κѧκ ʜѧ ϯⱀѳʜє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ӌѳϯѧ ҁⱀƀӀґʜƴʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳɯєʌ ʜѧχƴӣ πѳκѧ ᴙ ϯєѣᴙ χƴєʍ ʜє đѳѣџʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯѧѳѥ ʍѧϯƀ єѣƴ ʙ đєⱀєʙʜє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ πѳёϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ κѧκ πєϯƴχ πѳ ƴϯⱀѧʍ κƴκѧⱀєκѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯʙѳѥ ʍѧϯƀ κѧκ χѳӌƴ ӌѳϯѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӡѧєѣєϯҁᴙ ҁѳҁѧϯƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯѧѳѥ ʍѧϯƀ ӌѳϯѧ ʙ ѳӌєʌѳ єѣƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ƴ ʍєʜᴙ ʜѧ χƴѥ ⱀѧӡʙѧʌџʌѧҁƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ χƴєʍ ҁѳѣⱀѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴєʍ ƴѣєѫѧʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʙʜѧϯƴⱀє ʜѧ χƴѥ ѧʌʌѧχѧ єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳӣ χƴӣ κѧκ ʌџҁϯ єѣѧʜƀӀӣ ƴπѧʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ πʌѧʙѧϯƀ ƴӌџʌѧҁƀ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳӣ ҁπєⱀʍѧκ ѫƴєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳџ ᴙӣҵѧ ʙ πєӡđє ʜѳҁџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯʙѳѥ ʍѧϯƀ ʙ ϯⱀƴҁƀӀ ҁѳⱀє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳєʍ χƴѥ ґʜџєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κƴⱀѥ πџӡđƴ ϯʙѳєӣ ʍѧϯєⱀџ ҁʙѳџʍ χƴєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ӌѳϯѧ ƴ ʍєʜᴙ ʜѧ χƴѥ ѳⱀєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ҁʌєʙѧ єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѳѣ ʍѳӣ χƴӣ ѣⱀєєϯҁᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ƴ ʍєʜᴙ ʜѧ χƴѥ κʜџґџ ӌџϯѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳєʍƴ χƴѥ πѳ϶ʍџ πџɯєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ʙƀӀҁϯƴπѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ џґⱀѧєϯҁᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁѳҁєϯ κѧκ ѳʌєʜƀ єѣѧʜƀӀӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ʍѧϯєⱀє ϯʙѳєӣ χƴєʍ ⱀѳґѧ ʌѳʍѧѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧѳᴙ ʍѧϯƀ ʍѳӣ χƴӣ ѳѣʌџӡѧʌѧ ҁѳⱀє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʙъєѣѧʜѧᴙ ѳʙӌѧⱀκѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴєʍ πџӡđџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ʌѳɯѧđƀ єѣѧʜѧᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ʜѳʜ ҁϯѳπѳʍ πєⱀđѳʌѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ӌѳϯѧ ҁѳҁєϯ ʍѳӣ χƴӣ џӡʜƴϯⱀџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʜѧ ʍѳӣ χƴӣ πєⱀєєχѧʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ʌєӌџϯҁᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳєґѳ χƴᴙ πƀєϯ κѧκ ҁ ⱀѳđʜџκѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʜѧ ʌѳɯѧđџ єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯƀ ʜѳⱀʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҁƴ ʙ ϯᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ҁκѳʌƀӡџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴєʍ ʍƴϯџϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳӣ χƴӣ ґⱀƀӀӡєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ϯʙѳᴙ ʍѧϯƀ ʍѳџ ᴙӣҵѧ ӡѧѫџʙѧʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ґⱀѧʍѳϯƴ πѳʌƴӌџʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ χƴєʍ ҁѳϯⱀƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ єѱє ҁѳҁєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯʙѳӣ ⱀѳϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ҁϯѳᴙ ҁѳҁєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳѥ ʍѧϯƀ ʜѧ ʌѧʙκє єѣѧʌ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ҁѳҁєϯ ʜѧ ϯʙѳєӣ ɯκѳʌƀʜѳӣ πѧⱀϯє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳɯєʌ ʜѧχƴӣ χѧӌ ӡѧєѣѧʜƀӀӣ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯʙѳѥ ʍѧϯƀ ҁ χƴᴙ ѳѣⱀƀӀґѧѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁѳҁєϯ ʜѧ ϯʙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯѧ ϯʙѳᴙ ʍѧϯƀ ƴʍџⱀѧєϯ ҁ ʍѳџʍ χƴєʍ ʙѳ ⱀϯƴ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ѳκƴϯѧʌѧҁƀ ʍѳџʍ χƴєʍ κѧκ πʌєđѳʍ єѣѧʜƀӀʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ƴ ʍєʜᴙ ʜѧ χƴѥ ⱀѧҁҁʙєϯ ʙҁϯⱀєӌѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ҁ ʍѳџʍ χƴєʍ ʙ ѳѣʜџʍκƴ ѣƴχѧєϯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧʍѧɯѧ ӌѳϯѧ ʙʜѧϯƴⱀє ƴ ʍєʜᴙ ʜѧ χƴѥ πⱀџƴʜƀӀʌѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѳᴙ ʍѧϯƀ ʍѳӣ ӡҵӣ ʙ ҁʙѳєӣ πџӡđє πⱀѳπџҁѧʌѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ʙ ϯᴙ ҁⱀƴ џ ҁҵƴ ҁʌєϯѧκ χџχџ єӡ єӡ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁⱀƴ ϯє ʙ ґƴѣƀӀ ʌєχκѳ ʌєχκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙʜѳҁ џ ҁⱀƴ ʙ ƴɯџ χџχџ ʍđѧ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ƴѫє ҁʌєʌҁᴙ ʍđѧ ʌєχκѳϯʜᴙ κѧκѧᴙϯѧ џӡє џӡє ʌєχκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ʙ ϯᴙ ⱀѧκ κѧκѳӣ ѣѳϯ ϯƀӀ ɯѳ đƴⱀѧκ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ӌϯѳϯѳ ҁѧҁєɯ ҵƀӀґѧʜ ʍđѧ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє џχџχ єӡ єӡ џӡє ʌєχκѳ ʍѧʌѧđѳӣ κⱀѧѣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʙ ҁѧƴҁ πѧⱀκє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯᴙ ҁʌєʌ ʜє ѧπⱀѧʙđƀӀʙѧӣҁᴙ ҁʌєϯƀӀӣ πџϯѧⱀѧҁϯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ κѧκ đƀӀɯџɯƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʜѧ ҁѳҁκџ ʍđѧ ӌѳϯѧ ʌєχκѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍđѧ ґѧⱀџɯƀ ƴѫє χџχџχ ʌєχκѧϯʜѧᴙ κѧκѧᴙϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌєʜϯѧ ʜѧҁҵѧʌ ϯє ʜѧ єπѧʌƀʜџκ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧⱀᴙѫѧѥ ҁʙѳџʍ χƴєʍ πџҁϯƴ ϯʙѳєӣ ʍѧʍƀӀ џӡє џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ӌѧʙѳ ʌєʙѧєɯƀ ᴙ ϯᴙ ʜє đѳєπѧʌ((99(9  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ʍʜє ҁџӌѧҁ ҁѧҁѧϯƀ ʜѧӌʜєɯƀ!1!  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѧⱀџɯƀ ʍѳџʍ χƴєʍ ʙ πџҁϯƴ ʍѧʍƀӀ ҁʙѳєӣ?  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧ ᴙ ʜѧҁҵѧʌ ϯє ʜѧ єπѧʌѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳӣ χƴӣ κѧκ ⱀƴѣџʌƀʜџκ đʌᴙ πџҁϯƀӀ ϯʙѳєӣ ʍѧϯєⱀџ ѧѻⱀџκѧʜєҵ ϯƀӀ ϯƴπѳӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯƀӀ ӌѳ ϯѧκѳӣ χƴєҁѳҁѳ ϯѧ? ҁϯⱀѧƴҁ џπѧʜƀӀӣ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѧ κѧκѳӣ ѣѳϯ? ʜє ʜѳӣ ᴙ ϯʙѳѥ ʍѧϯƀ єѣƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѧӣᴙ ʍѧʍκѧ ʍѳӣ χƴӣ ҁѧҁєϯ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ʜƴϯѧⱀƀ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ ɯѳʌѧʙƴ πѧѻѧҁʜѧ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κҁϯѧϯєϯ ϯƀӀ ҁѧҁѧʌѧ ʍʜє џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѧᴙ ʍѧʍκѧ ʍѳӣ ӌʌєʜ ҁѧҁєϯ ʙҁџґđѧ χџџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧ ʙѧđє   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџ ʌƴʜѧʍ ҁʙєϯє ʍʜє ҁѧҁєɯ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣ ҁѧҁєɯ ʌѳχ ᴙ ϯᴙ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ʍѧϯƀ ϯʙѳѥ єҁ єҁ χƴёʍ </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧϯƀ ϯʙѳѥ χƴёʍ κџđѧʌ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ ɯϯƀӀⱀѥ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ єѣѧʌѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍκƴ ϯʙѧӣѥ χƴӣєʍ πⱀѧґʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ χƴӣѥ ϯʙѧӣѥ ʍѧϯƀ ⱀѧҁϯᴙʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ʍѧʍκƴ ϯʙѧӣѥ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌʌєʜ ʍѳӣ ҁѧҁєɯ đџκѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁѧʌѧ ʍʜє ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧӌєɯƀ ʜѧ χƴӣѥ χџχџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ ҁҵƴ ϯє ʙ єπѧʌѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯєѣᴙ ѳπⱀѧκџʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯє ѻѧϯѧʌџʌџϯџ ҁđєʌѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє κѧκ ɯєҁϯєⱀκѧ ʜѧ ӡѳʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ ⱀѧҁπѧⱀѳʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧ ѣєʌѳӣ πѧʌѧҁє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧ ʌєҁѧπѧʌѧҁє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙѧєʜѧʍ πѧⱀѧđє ҁѧҁєɯ κƴⱀʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ κⱀѧҁʜѳʍ κѧʙⱀє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ κⱀѧҁѧϯє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀѧɯƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌѧӡʜƀӀʍџ ᴙѣʌѧκѧʍџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ʙ ϯʙѧӣѥ ʍѧʍκƴ єӡ єӡ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁџⱀƴєɯƀ ʍʜє ҁʌѧđκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ґʌѧđκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ ҁѧҁєɯ κѧκ πѧⱀϯџӡѧʜ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʙєɯѧѥ χџχџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀѧӣʜџκѳʍ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ πєʌєʜѧѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁёɯƀ ʍʜє ґџѣκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đџҁκƴϯʜѳ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ϯєʍπє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ʙ ϯᴙ ҁ ʙƀӀҁѳϯƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ đѧⱀѳґє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁёɯ ʍʜє πⱀѳӡⱀѧӌʜѳ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ґѧɯƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌƴɯƴ ϯᴙ ӌʌєʜѧʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧπѧκѧʙѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ χѳʌѳđє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ ʙѧҁπџϯѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѳκ ҁҵƴ ʙ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣ ʙ ϯᴙ κџʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙєʌџκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁџđᴙ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯѳᴙ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґєʜѧҵџđʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧʜϯƴӡџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ ҁѧҁєɯ ʍʜє џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯᴙ џӡє ϯѧκϯѧ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѣѳҁҵѧʌ ϯᴙ ҁʙєⱀχƴ ʜѧ ʜџӡ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ѳκʜє ʍʜє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁёɯ ʍʜє ґⱀƴҁϯʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀџϯџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧⱀѧӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌєʜѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀєѱџɯƀ ѧϯ χƴӣᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀџπєⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙџҁκџ ϯє ѧѣѧҁҵѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳđ ⱀѳκєʜ ⱀѳʌ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ ᴙ ϯᴙ πѧⱀʙѧʌ χџχџ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀєκⱀѧҁʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧ ҁʌєӡѧʍџ ҁѧҁєɯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєʌџӣɯє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍʌєӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєʌκѧʙѧϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ґⱀѧҵџѳӡʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ ɯϯƴⱀʍƴѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ɯʌѥɯκƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ  ʙ ҁϯⱀєҁє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴёʍ ϯᴙ ɯѧϯѧʜƴʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʜᴙʌ ϯᴙ ɯѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѣѳҁҵѧʌ ϯє κєđƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѧʙѧʌ ϯᴙ ҵєʌκƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀʙєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πƀᴙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁѱєπџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ κѧđƀӀκ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ ӡƴѣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѣѳҁҵѧʌ ϯᴙ đƴⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πѧⱀκє ҁѧҁѧʌѧ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʌѥɯκѧ ҁѧҁєɯ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѧϯκʜƴʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ đєⱀєʙʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣƴ ϯᴙ πѳѫџӡʜєʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џʜѧʍѧⱀѧӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ κѧⱀʍʌѥ єӡ єӡ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѻѧʜѧϯєᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧκѳʙѧʌƀʜѳ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌʍƀӀⱀѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀƀӀʌѧʍ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ӌєκʜƴʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ϯѧҁκѧѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙƴʌƀґѧⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʜѧҁџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧϯєⱀᴙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κҁϯ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧʙєⱀɯєʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ κѧʌѳđҵє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳđ κѧϯʌѳʍ ҁѧҁєɯ ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʜѧ κѧʌєʜᴙχ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πєӌџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀƴɯƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡʙѧʌџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đџʜѧʍџɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀƴӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʌѧπѧϯѧχ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ κⱀѧҁѧϯє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧⱀѧҁѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ѣѧʌƀʜџҵє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ѳϯπƴҁκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πʌѧѱѧđκє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ҁϯѧʜҵџџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯᴙ џӡє χƴӣєʍ ҁʌѧʍѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ʌџʍџӡƴџʜє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀƴҁϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʙӡʌѧʍѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡє ϯᴙ ҁʌєϯѧᴙ χƴӣєʍ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌѧđџʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀєӡѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πџʌѥ ϯᴙ ӌʌєʜѧʍ ɯѧʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁџⱀƴєɯ ʍʜє κʌџϯѧⱀѧʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯѳʜѧʍџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀѧʍѧϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ґѧⱀʍѳʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʌѥχѧʙѧϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ ҁϯⱀєʍʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѱѧϯєʌƀʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєӡđє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁџʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ґʌѧӡѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đєҁєⱀϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ κѧʜκⱀєϯʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ʍⱀѧӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѧ ӌѳⱀʜѧʍƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧ ӡєʌєʜџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ѱєκѧӌƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧӣʌѥʌѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєđѧʌѧґѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ κѳҁʍѧҁє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʙєⱀχѧ ҁҵƴ ʙ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧđ ӡʙєӡđѳӣ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πⱀѧʙѧđѧχ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ đџⱀєκϯѧⱀҁκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ κѧκ đƀӀɯџɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧ πѧⱀϯє ӌѳϯκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πƀӀχѧєɯƀҁᴙ џ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ѣƴʌϯƀӀχѧӣѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѳ ʍƴѫҁκџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѳ đєϯҁκџ ӌѳϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯʙѳӣ κʌџϯѧⱀ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯκѧ ϯᴙ χƴӣєʍ ѧґⱀєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁёɯ ʍʜє đџκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѫƴӣᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʍѧӣʌџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧⱀᴙđѧӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ӌєπƀӀѫƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʜџϯѧⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πⱀџѳⱀє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џʜҁϯⱀƴκϯџʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κʙѧđⱀѧϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѳ ҁϯѧѫєʍ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѣƀӀҁϯⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ϯєґѧѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πѳґⱀџѣє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯёⱀ ϯᴙ ɯѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ κѳʌєʜκѧχ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧκѧʍ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧʌѧʜҁʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧ κʜᴙѫєҁκџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ᴙ ϯᴙ џӡє ϯѧκϯѧ ҁʌєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧⱀѧӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧҁєʌџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κʌџєʜϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πⱀџđѧʙџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџѫџʍѧӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ κѧκ ҁ϶đ ѣѳӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁπѧⱀϯџʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґƴđʜѳ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϶ⱀѳϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣⱀѳҁџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀƀӀӡєɯ ʍѳӣ χƴӣ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀєѣƴɯєѣʜѳ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѳ ⱀѧҁκʌѧđƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κʌџϯѧⱀ ϯʙѳӣ ҁπєⱀʍѧӣ ӡѧʌєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ɯѳʌѧʙƴ κⱀƀӀʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ʌѧӣκѧєɯƀҁᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ κҁϯ đⱀѧѣєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙѧⱀѧϯʜџκ ϯє κѳʜӌџʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙҁκⱀƀӀʌ ϯᴙ χƴӣєʍ ӌѳϯκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ӡđⱀѧʙʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χⱀƴҁϯєɯ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πⱀєѫѧʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧӡʜѧєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁ πⱀѧҵєʜϯѧʍџ ҁѧҁєɯ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πⱀџ ʙҁєχ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπєɯƀҁᴙ ҁ ʍѧџʍ χƴӣєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧⱀѧʌƀʜѧ ҁѧҁєɯ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѧκϯƴѧʌƀʜѧ </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ ґѧⱀᴙӌѳ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁκⱀѧџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳκѧʌđѧʙҁκџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧʌѧӌƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κʌџϯѧⱀ ϯʙѳӣ ʍѧⱀѳӡѫƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πѧʌƀѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѱƴπѧʌ ϯᴙ ɯѳʌѧʙƴ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χʌѳπѧӣᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʜєѫʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ґѳⱀʌѳ ϯᴙ єπƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧҁҵѧʌ ϯє ʙ ґѧⱀϯѧʜƀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀєɯƀ ʍѳӣ ӌʌєʜ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀѧđѧκҁѧʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀϯѳʍ ʍʜє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀєκѧʜҁϯⱀƴϯџʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡє ϯᴙ ɯѳʌѧʙƴ πʜƴʌ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʌєҁєʜκѧӣ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧӣѥ ҁπєⱀʍƴ ґʌѧϯѧєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧҁҵѧʌ ϯє ʜѧ ґѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ѫєʌƴđѧκ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ϯѧʍʌѥ    </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁєⱀđєӌʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ ѣџⱀʌѳґє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ҁѧʍѧʌƀѳϯє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ đƴⱀʜƴѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ҁϯⱀџʍᴙʜκџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ χƴӣє ϯѧџɯƀҁᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєⱀʙʜѧ ҁѧҁєɯ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ πѧđʙѧⱀѳϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʌџѻƴєɯƀҁᴙ ѳѣ ʍѳӣ χƴӣ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ πⱀџϯѧⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡʍѧϯѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѳ κⱀѧҁʜѧϯƀӀ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ѫєʙѳϯʜѧʍƴ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ƴʍƀӀʌ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џӡє ϯѧκϯѧ ϯᴙ đƴⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ κʌƀӀκ ϯє ҁҵѧʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєⱀʙƀӀ ϯʙѧџ χƴӣєʍ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌѧʍѧʌ ϯє πⱀѧϯєӡ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁѧʌѧ ʍʜє ʙ κѧⱀƀӀϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʌѧʍѧӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧʍѣџɯ κʌѧҁʜѧ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁπƴҁϯџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ ґʌѧʜđƀӀ χџχџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁёɯ џʜҁϯⱀƴʍєʜϯѧʌƀʜѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πⱀѧκϯџӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πʌѧҵđѧⱀʍє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʙ πʌѧҵκѧⱀϯє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ πєʜҁџѥ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀѧʙѧʙѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ⱀѧӡʍџʜκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѫџӡʜєʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌѳϯκѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧѱєⱀҁκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ƴϯѧπџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ҁʌѧđєʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀџɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џґʜѳⱀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʌѥχӡѧ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧϯⱀᴙҁʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧ ʌѥѣʙџ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀƴӌƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєⱀχѳʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡʍѧϯѧʌ ϯᴙ χƴӣєʍ џӡє ϯѧκϯѧ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧҁџʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀѧʍѣƴѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѧϯџʙѧӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ⱀѧʜᴙʌ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍʌѧđєџɯƀ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧӌѧⱀѧʙѧϯєʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀѧʜџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣƴκʙѧʌƀʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґџπѧѧʌєⱀґєʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πєӌκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ κѧʜҁєⱀʙƀӀ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ʌџʜӡƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯʙѧӣєӣ ʍѧʍκє χƴӣ đѧӣѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁєκƴʜđʜѧ єπƴ ϯᴙ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀѧκʌᴙʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѧʍѧʜџɯƀҁᴙ ʍѧџʍ χƴӣєʍ ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєđџϯџʙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґєʜєⱀѧʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧʌѧʍѧʌ ϯᴙ χƴӣєʍ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙџϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ⱀѧκѧʙѧʌƀʜє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ҁϯƴѫє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѳѣѳҁҵѧʌ ϯᴙ ґʌƴπƴѥ ɯѳʌѧʙƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πєⱀєđʜєʍ κѧʌєҁє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀєѫƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀџʙѳѫʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѫєҁκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ҁϯⱀѧχѳʙʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ⱀѧκѧʙџʜƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧ ʍѧҁϯџ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ґѧӡѳʜє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѧⱀѧѣѧʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ⱀџѻє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧχѧϯʌџʙѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ ҁʌєϯѧᴙ ґѧⱀџɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πⱀѧʍƀӀʌ đƴⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡџґџđʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ϯєⱀʜᴙχ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κʌєӣʍџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єѣѧʌѧ ϯʙѧӣѳ χƴӣєʍ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ʜѧґʌѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χʌѳπѧӣᴙ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ đєʌє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ґⱀѧѣƴ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁϯⱀѳџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʍκƴ ϯʙѧӣѥ єπƴ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє κⱀѧʙѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ӡєʜџϯє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣєʌѧҁʜєѫʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧӡѧѣⱀѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѧʌᴙʙџϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧєѣѧϯѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ґđє ӡѧχѧӌƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πƀӀⱀʜƴʌ ϯᴙ ӌʌєʜѧʍ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ πџʜґʙџʜ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ ҁ ʙƀӀҁѳϯƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧʌƀӡџɯ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џʜϯєⱀʙѧʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӌєⱀϯєѫʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯᴙ ϯƴϯ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đⱀƀӀґѧєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜџ πѧ ѻѧⱀʍѧϯƴ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѧκϯџʙʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" џҁϯѧⱀџӌєҁκџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ ѧϯʌџӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє ϯѧκϯѧ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ƴʌƀє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳđ єʌƀѥ ҁѧҁѧʌѧ ϯƀӀ ʍʜє đџκѳʙєʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєϯѧӌʜѧ ʌѧʍѧєɯƀҁᴙ ɯѳʌѧʙѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧґʜєҁϯⱀєʌƀʜѧ ҁѧҁєɯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧҁҵѧʌ ϯє κƴđⱀџ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ πѧʌƀʍє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧⱀѳӡѫƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧʙѧⱀѧӌџʙѧᴙҁƀ ҁѧҁєɯ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧκƴӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴʌѧѫџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πⱀѧѣџʌ đƴⱀƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ѧѣѧҁҵѧʌ џӡє ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ πƀӀχϯџɯƀ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀʙєɯƀҁᴙ ҁʌєϯѧᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣѳđⱀѧ ҁѧҁєɯ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ҁʍƀӀʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧʍ πѧ ҁєѣє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧϯ πⱀџⱀѳđƀӀ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁѧʌѧ ϯƀӀ ʍʜє ϶ʜєⱀґџӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍєϯѧєɯƀҁᴙ ҁ ʍѧџʍ ӌʌєʜѧʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯє ʙєʜƀӀ πѧⱀѳʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ϯє ʙ ʙєʜƀӀ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁҵƴ ʙ ϯʙѳӣ ʙєʜѳκ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєκџ ϯє χƴӣєʍ ҁʜєҁ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ґʌƴɯƴ ʌѧҁѳҁʜѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ӡѧ ѣѧκҁƀӀ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѧ πѧʜᴙϯџᴙʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙʜџʍѧϯєʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ҵєʌκƴ ҁʜєҁ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ґⱀѧʍџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧʜѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đƀӀɯєɯƀ ʍѧӣєӣ ҁπєⱀʍѧӣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʌѧʙκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ ѧѣєӡƀᴙʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єӡѫƴ ʙ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧҁџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χⱀѧʜџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍⱀѧӌʜѧ ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" đѧʙʌѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁʌєϯѧᴙ ҵєπʌᴙӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѧѫƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯєѣƴ ϯᴙ ɯѳʌѧʙƴ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯⱀєɯƀҁᴙ ѳѣ ʍѳӣ χƴӣ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ᴙʍє ҁѧҁѧʌѧ ϯƀӀ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѱєκѳϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧʙⱀєʍєʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀʙѧʌ ϯᴙ χƴӣєʍ ҵєʌκƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯѳʌѧʙѧ ҁѧҁєɯ ѣєӡđѧⱀʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧ ⱀѧđʜѳʍƴ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁπєⱀʍƴ ʍѧӣѥ ʌƴѻκѧєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧѣєʌƀʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀᴙӡʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯκʙѧⱀѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧⱀʙѧʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯʜƴⱀƴєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧҁκⱀѧџʌ ϯє єπѧʌѳ χƴӣєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧӡѧⱀϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ƴⱀѧʜџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯєⱀᴙєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ ҁѧҁєɯ ҁκⱀџʜѥ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ϶ϯѧπѧχ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳ ʍѧҁκѳʙҁκє ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ɯџѻⱀƴџɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πџӡѫƴ ϯᴙ χƴӣєʍ ɯѳʌѧʙƴ </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀџʌѥđʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ҁκѳⱀѧҁϯџ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙєɯѧєɯƀҁᴙ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ ѻџʌƀϯⱀ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁϯѧʙʌѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ʙєϯⱀƴ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѳđҁѧӡʜѧϯєʌƀʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ πʌѧʙџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѳʜҁϯѳπʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ϯѧκϯє єπƴ ϯᴙ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀџϯʍџӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣѧґⱀєʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣⱀѧϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πⱀᴙӌƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ κѧӌєⱀґѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ κⱀѧӣѥ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ʙ ϯᴙ ʌєʙʜƴʌ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜёѣѧ ϯє χƴӣєʍ πѧⱀѧӡџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" єπƴ ϯᴙ πѧđ ʙҁё  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ƴϯѧπџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ҁѧʌᴙⱀџџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ʍʜє đʙƴʌџӌʜѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѣџⱀєɯƀ ʍѳӣ ӌʌєʜ ϯѧκϯѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀѧʙʜᴙӣѥ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҵєʌκƴ ϯᴙ ҁѣџʌ єӡ єӡ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ϯѧӌƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґʌѧѫƴ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʍѳӣ χƴӣ ʜѧ ϯє ⱀѧѣѳϯѧџϯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧⱀѧʜџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ҁʙёʌ ʙ ґⱀѳѣ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҵʙєϯєɯƀ ʍѧџʍ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧđ ҁϯѧʌѳʍ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πџӡđѧϯєʜƀκѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧѣƴҁϯⱀѳџʌ ϯᴙ χƴӣєʍ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ⱀƀӀӌᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ đʙџґѧӣѥ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πѧҁʍєⱀϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀєѣєɯ ʍѧџʍ χƴӣєʍ   </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πєӌѧϯʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙѳӡʌє ѣѧϯѧⱀєџ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧʍѧʜđʜѧ єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѻѳⱀҁџɯƀҁᴙ ʍѧџʍ χƴӣєʍ đƴⱀѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κѧκ ѧʙӌѧⱀκѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґѧʙκѧᴙ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜѧ ƴʌџҵє єπƴ ϯᴙ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєⱀʙѳӡʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ ƴɯџ ϯє ҁҵƴ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ѧϯѣџʌ ϯᴙ χƴӣєʍ џӡє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʌѧʍѧєɯƀҁᴙ ѧѣ χƴџ χєχє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʜєπѧʙϯѧⱀџʍѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ґⱀѧʙџϯѧҵџѳʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" χƴӣєʍ ϯᴙ ʙѣџʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁѧҁєɯ ѫџđκѧ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ʙ πєҁđƴ ϯє ʜѧҁҵѧʌ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" ҁκѧӡѧӌʜѧ ҁѧҁєɯ  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" πєⱀєʜѳҁʜѧ ҁѧҁєɯ ʍʜє  </a> <emoji document_id=5784974820592586088>🔥</emoji> ",
" κⱀџϯџӌʜѧ ҁѧҁєɯ </a> <emoji document_id=5784974820592586088>🔥</emoji> "]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl12))
            await sleep(0.1)
            await sleep(time)