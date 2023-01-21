import random
import python_weather
import asyncio
import os
import re

async def getweather(location) :
    async with python_weather.Client(format=python_weather.METRIC) as client:
        try:
            weather = await client.get(location)
            current_temp = str(weather.current.temperature) + ' ' + chr(176) + 'C'
            return current_temp
        except Exception as e:
            print(e)
            return 'check your logs idiot'



 
async def response_handler(message) -> str:
    """from a given str message return a str response"""

    if message == 'hello' or message == 'Hello':
        return 'Hello, idiot'
    if message == 'roll':
       return random.randint(1, 6)
    if message.startswith('weather'): 
        try:
            location = message.split()[1]
            return await getweather(location)
        except Exception as e:
            print(e)
    if message == 'yoga':
        pass