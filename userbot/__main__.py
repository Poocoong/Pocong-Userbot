# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import sys
from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot import LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info(
    "📍 POCONG - USERBOT 📍 [SUCCESFULL ACTIVATED!]")
    
    
async def pocong_userbot_on():
    try:
        await bot(JoinChannelRequest("@PocongProject"))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest("@Poconguserbot"))
    except BaseException:
        pass

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
