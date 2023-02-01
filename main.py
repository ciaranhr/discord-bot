import DiscordBot
import os
from dotenv import load_dotenv



if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')
    bot = DiscordBot.UsefulBot(token)
    bot.run_useful_bot()