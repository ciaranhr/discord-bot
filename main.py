import DiscordBot
import os
from dotenv import load_dotenv




if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')

    intents = DiscordBot.discord.Intents.default()
    intents.message_content = True

    bot = DiscordBot.UsefulBot(intents=intents)
    # @bot.event
    # async def on_ready():
    #     print('Ready!')
        
    bot.run(token)