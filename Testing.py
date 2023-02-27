import DiscordBot
import os
from dotenv import load_dotenv
import config
import asyncio
import aiomysql
import mysql.connector


host = config.credentials.get_hostname()
user = config.credentials.get_username()
password = config.credentials.get_password()
db = config.credentials.get_db()
async def main():

    db_connection = await aiomysql.connect(host=host, user=user, password=password)

asyncio.run(main()) 