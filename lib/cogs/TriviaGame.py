import mysql.connector
from mysql.connector import errorcode
from ..db import db
import discord.ext.commands as commands
import discord
import random
from ..bot import TriviaGameProcessing as T

#import sys
#import os
#SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(os.path.dirname(SCRIPT_DIR))


class TriviaGame(commands.Cog):
    def __init__(self, bot):
        self._bot = bot
        trivia_json = T.retrieve_trivia(70, "easy")
        self._trivia = T.Trivia(trivia_json)
        self._trivia.clear_questions()
        self._trivia.input_questions()

    
    @commands.command()
    async def playtrivia(self, ctx):
        question = self._trivia.get_random_question()
        print(question)
        await ctx.send(f'TriviaQuestion is:{question}')

async def setup(bot):
    await bot.add_cog(TriviaGame(bot))