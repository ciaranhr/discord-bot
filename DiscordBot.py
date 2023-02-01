import ChatResponses
import discord

class UsefulBot():
    def __init__(self, token) -> None:
        self.token = token
    
    async def send_message(self, user_message, message):
        """send message to the channel based on user input
        message is defined according to ChatResponses"""
        try:
            response = await ChatResponses.response_handler(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)
        

    def run_useful_bot(self):
        """run UsefulBot using existing token in .env"""
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

            await self.send_message(user_message, message)

        client.run(self.token)
