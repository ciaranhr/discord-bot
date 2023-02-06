import ChatResponses
import discord

class UsefulBot(discord.Client):
    """A simple bot able to respond to some commands with meaningful actions"""

    def check_users():
        """check users that are in server against db, if new users add to db"""
        pass

    async def send_message(self, user_message, message):
        """send message to the channel based on user input
        message is defined according to ChatResponses"""
        try:
            response = await ChatResponses.response_handler(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)
    
    async def on_ready(self):
        print(f'We have logged in as{self.user}')

    async def on_message(self, message):
        """command response management. Isolates users message, determines the response to send"""
        if message.author == self.user:
            return
        if not message.content.startswith('!'):
            return

        user_message = str(message.content[1:])
        username = str(message.author)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})" )

        await self.send_message(user_message, message)

        
