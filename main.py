import DiscordBot
import os
from dotenv import load_dotenv
import config
import asyncio
import aiomysql
import random

host = config.credentials.get_hostname()
user = config.credentials.get_username()
password = config.credentials.get_password()
db = config.credentials.get_db()

async def main():
    load_dotenv()
    token = os.getenv('TOKEN')

    intents = DiscordBot.discord.Intents.default()
    intents.message_content = True
    intents.members = True

    db_connection = await aiomysql.create_pool(host=host, user=user, port=3306, password=password, db=db)
    exts = ['cogs.greeting'] 
    async with DiscordBot.UsefulBot(command_prefix='!', intents=intents, trivia_pool=db_connection, initial_extensions=exts) as bot:
        await bot.start(token)
    # @bot.event
    # async def on_ready():
    #     print('Ready!')



 
asyncio.run(main())