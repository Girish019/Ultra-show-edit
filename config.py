#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather 6102959656:AAGNVH5A8IHdGs8fSb7uoVkOT-FHWVXRgwE
#TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6102959656:AAGNVH5A8IHdGs8fSb7uoVkOT-FHWVXRgwE") #miror leech
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6180766269:AAF0jG2fxEc6iu19Ps8HFAQYa3lmQbtyTeg") #new fs
#TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5946382591:AAE6eSYjUSUyfMgACi5zudlfZcdzVRxiSJU") #copy contact 
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "10755921"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d5e49fd3637cba407f17807d31c77977")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001842556179"))
LOG_ID = int(os.environ.get("LOG_ID", "-1001748750847"))
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5636224141"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Chandan:Chandan@cluster0.2lauy.mongodb.net/cluster0?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "PROFS30M")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5678225652 1269341939").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1147676731)
ADMINS.append(1284476297)

LOG_FILE_NAME = "filesharingbot.txt"

LOG_TEXT_P =  """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫

<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
<b>᚛› 𝐅𝐫𝐨𝐦 - <a href="https://t.me/Tkh_fsbot">TKH Store 🏪</a></b>
"""

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
