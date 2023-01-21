import os
import ChatResponses
import discord
from dotenv import load_dotenv

async def send_message(user_message, message):
    """send message to the channel based on user input according to ChatResponses"""
    try:
        response = await ChatResponses.response_handler(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)
    

def run_useful_bot():
    """run UsefulBot using existing token in .env"""

    load_dotenv()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content[0] != '!':
            return

        user_message = str(message.content[1:])
        username = str(message.author)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})" )

        await send_message(user_message, message)

        

    client.run(os.getenv('TOKEN'))
