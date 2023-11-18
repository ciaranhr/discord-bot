
import discord
from discord.ext import commands

from typing import List

import asyncio
import aiomysql
import os


class UsefulBot(commands.Bot):
    """A simple bot able to respond to commands with some functionality
    accesses mysql database. built from cogs"""
    def __init__(
        self,
        *args, 
        trivia_pool: aiomysql.Pool,
        initial_extensions: List[str],
        **kwargs
     ):
     super().__init__(*args, **kwargs)
     self.trivia_pool = trivia_pool
     self.initial_extensions = initial_extensions

    async def setup_hook(self) -> None:
        """loop through and load extensions into bot"""
        for extension in self.initial_extensions:
            await self.load_extension(extension)
        # async def load():
        #     for filename in os.listdir("./cogs"):
        #         if filename.endswith(".py"):
        #             await self.load_extensions(f"cogs.{filename[:-3]}")

        self.bg_task = self.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        """experimenting with async task runningin background, skeleten for future background db management"""
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(253796469872525325) 
        while not self.is_closed():
            counter += 1
            users = self.check_users()
            await channel.send(counter)
            await asyncio.sleep(180)  # task runs every 60 seconds
    
    def check_users(self) -> dict:
        """check users that are in server for some bot
            return: a dictionary of the format {member name: date_joined}"""
        members = [member for member in self.get_all_members()]
        users = {members[i].name: members[i].joined_at.date()  for i in range(0, len(members))}
        return users

    async def on_ready(self):  
        print(f'We have logged in as{self.user}')

    

