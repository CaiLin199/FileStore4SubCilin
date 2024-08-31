#(©)Codeflix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7002822997:AAHnmT_V8j0jOIsnZkREREde8AGMjyYQjIg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26254064"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002015722294"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://nayemgm82:dEAm7U5yB2PBE4QS@cluster0.4kyy5u7.mongodb.net")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002093612362"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002107175667"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002107324666"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002125561929"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Usᴇʀ : {first}\n\n Iᴀᴍ Cᴀɪ Lɪɴ Bᴏᴛ , Oғғɪᴄɪᴀʟ Dɪsᴛʀɪʙᴜᴛᴏʀ Oғ HᴇᴀᴠᴇɴʟʏSᴜʙs Yᴏᴜ Cᴀɴ Gᴇᴛ Eᴘɪsᴏᴅᴇs Oɴʟʏ Tʜʀᴏᴜɢʜ Mᴇ ")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5296584067").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Lᴏᴏᴋs Lɪᴋᴇ Yᴏᴜ Hᴀᴠɴ'ᴛ Jᴏɪɴᴇᴅ Oᴜʀ Cʜᴀɴɴᴇʟs {first} Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Usᴇ Mᴇ Iɴ Fᴜᴛᴜʀᴇ..\n\n ....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False") == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @abidabdullah199"

ADMINS.append(OWNER_ID)
ADMINS.append(5296584067)

LOG_FILE_NAME = "filesharingbot.txt"

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
