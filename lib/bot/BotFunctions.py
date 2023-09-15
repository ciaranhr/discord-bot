import discord
import python_weather
import random

###Moving into cogs
def check_users(bot:discord.Client) -> dict:
    """check users that are in server for some bot
        return: a dictionary of the format {member name: date_joined}
    """
    members = [member for member in bot.get_all_members()]
    users = {members[i].name: members[i].joined_at.date()  for i in range(0, len(members))}
    return users

async def response_handler(message, bot:discord.Client) -> str:
    """from a str message return a str response"""
    if message == 'hello' or message == 'Hello':
        return 'Hello, idiot'
    if message == 'roll':
       return random.randint(1, 6)
    if message.startswith('weather'): 
        try:
            location = message.split()[1]
            return await get_weather(location)
        except Exception as e:
            print(e)
    if message == 'trivia':
        return "very not done yet thanks"
    if message == 'members':
        return  check_users(bot)
        
async def get_weather(location):
    """return current temperature in a given location around the world"""
    async with python_weather.Client(format=python_weather.METRIC) as client:
        try:
            weather = await client.get(location)
            current_temp = str(weather.current.temperature) + ' ' + chr(176) + 'C'
            return current_temp
        except Exception as e:
            print(e)
            return 'check your logs idiot'
 
