#(©)Codexbotz

import aiohttp
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait
from plugins.data import DATAODD, DATAEVEN ,BOTEFITMSG, FOMET
from plugins.cbb import DATEDAY
from plugins.link_generator import tlinkgen
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from datetime import datetime
from helper_func import encode
from pyshorteners import Shortener
import string
import re

# /date commend for set date
@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["date"]))
async def date(bot, message):
    dat = await message.reply_text("Select your Date.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.text & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    dateexc = datetime.now().strftime("%d")
    media = message.video or message.document
    filname= media.file_name.split("S0")[0]#[1][2]etc
    botfsno= re.findall("S0.+E\d+\d", media.file_name)
    print("yes find all")
    if int(dateexc) % 2 != 0:#chaeking for ODD
        if filname in media.file_name: #matching name in dict key with arrival video file name
           # chtid=int(DATAODD[filname][3])#for particuler channel id
            pic=DATAODD[filname][0] #particuler images
            SL_URL=DATAODD[filname][1] #for particuler domine name
            SL_API=DATAODD[filname][2] #for particuler api 
            chtid=message.chat.id # if you want pic+formet into bot pm 
            bot_msg = await message.reply_text("Please Wait...!", quote = True) #reply text please wait... to bot
            await asyncio.sleep(1)
            print("fetch successful")
    elif int(dateexc) % 2 == 0: #checking for EVEN
        if filname in media.file_name:
         #   chtid=int(DATAEVEN[filname][3])
            pic=DATAEVEN[filname][0]
            SL_URL=DATAEVEN[filname][1]
            SL_API=DATAEVEN[filname][2] 
            chtid=message.chat.id
            bot_msg = await message.reply_text("Please Wait...!", quote = True) #reply text please wait... to bot
            await asyncio.sleep(1)
            print("fetch successful")
    else:
        pass
    Tlink = tlinkgen(message)
    print("tlink.......")
    Slink = await get_short(SL_URL, SL_API, Tlink) #generating short link with particular domine and api
    print("slink......")
    await bot_msg.edit("Analysing....!")
    await asyncio.sleep(1)
    await bot_msg.edit("Wait Sending Post ▣ ▢ ▢ ")
    await asyncio.sleep(1)
    await bot_msg.edit("Wait Sending Photo ▣ ▣ ▢ ")
    await asyncio.sleep(1)
    await bot_msg.edit("Wait Sending Photo ▣ ▣ ▣ ")
    await asyncio.sleep(1)
    if len(DATEDAY)==0:
        await bot_msg.edit("Error: invalid date please set /date")
    else:
        await client.send_photo(chat_id=chtid, photo=pic, caption=FOMET.format(botfsno[0], DATEDAY[-1], Slink, Slink))
        await asyncio.sleep(1)
    await bot_msg.edit(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[-1])) #msg edit to "please wait...(see line 39" msg ==> and finally the elements belongs to sent serials are updated here
    #await e_pic.edit) # msg edit in forwarder channel = "pic without captions (see line 41)" ==> thats return to our given format and short link ,date are updated here

async def get_short(SL_URL, SL_API, Tlink): #A simple func for shorting link
    # FireLinks shorten
    try:
        api_url = f"https://{SL_URL}/api"
        params = {'api': SL_API, 'url': Tlink}
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, params=params, raise_for_status=True) as response:
                data = await response.json()
                url = data["shortenedUrl"]
        return url
    except Exception as error:
        return error
    
@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
