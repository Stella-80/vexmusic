from os import getenv

from dotenv import load_dotenv
###
load_dotenv()

# VARS i c 

get_queue = {}
STRING = getenv("STRING_SESSION", "AQAN1ixKZc7e4WgNAGUiMT6Hzfw9bY9erXBT7-az7KEcy4L4tKqQqEKRuXipOMCFWxA8dx4YwnOjS8JNOjVgegAbyi7ENs8saDspcKnH_6-aHQ8PJ9pmEzfxUuuFu3INtQNkuGhv7qVZQWb0A31uztjtGY5VtB80sqdobZyEj8KG6zoX-6DQHh8I0-XJ2ZQfc2xerMHR-BXJ5pDCG56XCN_wt_eWFko3goCVFClnRTtIP_llkfqx3N1tABg-_7WBbSthTdvHqlMpDACiH-ZjAp0XXKRGMZSK8a_rAbXCWDojlQZTvAOaV-HdglAsxqNDVnkruZr9QK9zvrzwfiDlQVJzaA-KyQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1788824202:AAEK67GqkF7Kj_QU2x2n8hwlou0knzmLLu8")
API_ID = int(getenv("API_ID", "8538756"))
API_HASH = getenv("API_HASH", "be2899f8951793b33a8eccfd4adcfb19")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "50"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))

    #done for now 
