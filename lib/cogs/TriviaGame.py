import mysql.connector
from mysql.connector import errorcode
from ..db import db
import discord.ext.commands as commands
import discord
import random


class TriviaGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    def trivia(self, ctx):
        pass
