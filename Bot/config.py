# All Credits Belong to @CipherXBot

import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = 6
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
    BOT_TOKEN = str(getenv('BOT_TOKEN'))
    OWNER_ID = int(getenv('OWNER_ID'))
