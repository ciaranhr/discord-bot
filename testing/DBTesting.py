import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from dotenv import load_dotenv
import lib.bot.config as config
import asyncio
import aiomysql




host = config.credentials.get_hostname()
user = config.credentials.get_username()
password = config.credentials.get_password()
db = config.credentials.get_db()

async def main():

    db_connection = await aiomysql.connect(host=host, user=user, password=password)

asyncio.run(main()) 